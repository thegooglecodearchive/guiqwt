# -*- coding: utf-8 -*-
#
# Copyright © 2009-2010 CEA
# Pierre Raybaut
# Licensed under the terms of the CECILL License
# (see guiqwt/__init__.py for details)

"""Simple dialog box based on guiqwt and guidata"""

from PyQt4.QtCore import SIGNAL

import scipy.ndimage

from guidata.dataset.datatypes import DataSet
from guidata.dataset.dataitems import StringItem, IntItem, ChoiceItem
from guidata.dataset.qtwidgets import DataSetShowGroupBox, DataSetEditGroupBox
from guidata.utils import update_dataset

from guiqwt.config import _
from guiqwt.plot import ImagePlotDialog
from guiqwt.builder import make
from guiqwt.tools import OpenImageTool
from guiqwt.io import imagefile_to_array

SHOW = True # Show test in GUI-based test launcher


class ImageParam(DataSet):
    title = StringItem(_("Title"))
    width = IntItem(_("Width"), help=_("Image width (pixels)"))
    height = IntItem(_("Height"), help=_("Image height (pixels)"))


class FilterParam(DataSet):
    name = ChoiceItem(_("Filter algorithm"),
                      (
                       ("gaussian_filter", _("gaussian filter")),
                       ("uniform_filter", _("uniform filter")),
                       ("minimum_filter", _("minimum filter")),
                       ("median_filter", _("median filter")),
                       ("maximum_filter", _("maximum filter")),
                       ))
    size = IntItem(_("Size or sigma"), min=1, default=5)
    

class ExampleDialog(ImagePlotDialog):
    def __init__(self, wintitle=_("Example dialog box"),
                 icon="guidata.png", options=dict(show_contrast=True),
                 edit=False):
        self.filter_gbox = None
        self.data = None
        self.item = None
        super(ExampleDialog, self).__init__(wintitle=wintitle, icon=icon,
                                            toolbar=True, edit=edit,
                                            options=options)        
        self.resize(600, 600)
        
    def register_tools(self):
        opentool = self.register_tool(OpenImageTool)
        self.connect(opentool, SIGNAL("openfile(QString*)"), self.open_image)
        self.manager.register_standard_tools()
        self.manager.add_separator_tool()
        self.manager.register_image_tools()
        self.manager.add_separator_tool()
        self.manager.register_other_tools()
        self.activate_default_tool()

    def create_plot(self, options):
        self.filter_gbox = DataSetEditGroupBox(_("Filter parameters"),
                                               FilterParam)
        self.filter_gbox.setEnabled(False)
        self.connect(self.filter_gbox, SIGNAL("apply_button_clicked()"),
                     self.apply_filter)
        self.layout.addWidget(self.filter_gbox, 0, 0)
        self.param_gbox = DataSetShowGroupBox(_("Image parameters"), ImageParam)
        self.layout.addWidget(self.param_gbox, 0, 1)
        
        options = dict(title=_("Image title"), zlabel=_("z-axis scale label"))
        ImagePlotDialog.create_plot(self, options, 1, 0, 1, 0)
        
    def open_image(self, filename):
        """Opening image *filename*"""
        self.data = imagefile_to_array(filename)
        self.show_data(self.data)
        param = ImageParam()
        param.title = filename
        param.height, param.width = self.data.shape
        update_dataset(self.param_gbox.dataset, param)
        self.param_gbox.get()
        self.filter_gbox.setEnabled(True)
        
    def show_data(self, data):
        plot = self.get_plot()
        if self.item is not None:
            self.item.set_data(data)
        else:
            self.item = make.image(data, colormap="gray")
            plot.add_item(self.item, z=0)
        plot.set_active_item(self.item)
        plot.replot()
        
    def apply_filter(self):
        param = self.filter_gbox.dataset
        filterfunc = getattr(scipy.ndimage, param.name)
        data = filterfunc(self.data, param.size)
        self.show_data(data)


if __name__ == "__main__":
    from guidata import qapplication
    qapplication()
    dlg = ExampleDialog()
    dlg.exec_() # No need to call app.exec_: a dialog box has its own event loop
