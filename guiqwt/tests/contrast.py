# -*- coding: utf-8 -*-
#
# Copyright © 2009-2010 CEA
# Pierre Raybaut
# Licensed under the terms of the CECILL License
# (see guiqwt/__init__.py for details)

"""Contrast tool test"""

import os.path as osp

from guiqwt.plot import ImagePlotDialog
from guiqwt.builder import make
from guiqwt.tools import SnapshotTool

SHOW = True # Show test in GUI-based test launcher

def test():
    """Test"""
    # -- Create QApplication
    import guidata
    guidata.qapplication()
    # --    
    filename = osp.join(osp.dirname(__file__), "brain.png")
    image = make.image(filename=filename, title="Original", colormap='gray')
    
    win = ImagePlotDialog(edit=False, toolbar=True, wintitle="Contrast test",
                          options=dict(show_contrast=True))
    win.register_tool(SnapshotTool)
    plot = win.get_plot()
    plot.add_item(image)
    win.resize(600, 600)
    win.show()
    plot.save_widget('contrast.png')
    win.exec_()

if __name__ == "__main__":
    test()