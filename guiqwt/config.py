# -*- coding: utf-8 -*-
#
# Copyright © 2009-2010 CEA
# Pierre Raybaut
# Licensed under the terms of the CECILL License
# (see guiqwt/__init__.py for details)

"""
guiqwt.config
-------------

The `config` module handles `guiqwt` configuration (options, images and icons).
"""

import os.path as osp

from guidata.configtools import add_image_module_path, get_translation


_ = get_translation( "guiqwt" )


def make_title(basename, count):
    """Make item title with *basename* and *count* number"""
    return "%s %s%d" % (basename, _("#"), count)


APP_PATH = osp.dirname(__file__)
add_image_module_path( "guiqwt", "images" )

DEFAULTS = {
            'plot' :
             {
              "selection/distance" : 6,
              "antialiasing" : False,
              
              "title/font/size" : 14,
              "title/font/bold" : False,
              "label/font/size" : 12,
              "label/font/bold" : False,

              "selected_curve_symbol/marker" : 'Rect',
              "selected_curve_symbol/edgecolor" : "gray",
              "selected_curve_symbol/facecolor" : "black",
              "selected_curve_symbol/alpha" : .3,
              "selected_curve_symbol/size" : 7,

              # Default parameters for plot axes
              "axis/title" : "",
              "axis/color" : "black",
              "axis/title_font/size" : 8,
              "axis/title_font/family" : "default",
              "axis/title_font/bold" : False,
              "axis/title_font/italic" : False,
              "axis/ticks_font/size" : 8,
              "axis/ticks_font/family" : "default",
              "axis/ticks_font/bold" : False,
              "axis/ticks_font/italic" : False,

              # Default parameters for image axes
              "image_axis/title" : _(u"Pixels"),
              "image_axis/color" : "black",
              "image_axis/title_font/size" : 8,
              "image_axis/title_font/family" : "default",
              "image_axis/title_font/bold" : False,
              "image_axis/title_font/italic" : False,
              "image_axis/ticks_font/size" : 8,
              "image_axis/ticks_font/family" : "default",
              "image_axis/ticks_font/bold" : False,
              "image_axis/ticks_font/italic" : False,

              # Default parameters for color scale
              "color_axis/title" : _(u"Intensity"),
              "color_axis/color" : "black",
              "color_axis/title_font/size" : 8,
              "color_axis/title_font/family" : "default",
              "color_axis/title_font/bold" : False,
              "color_axis/title_font/italic" : False,
              "color_axis/ticks_font/size" : 8,
              "color_axis/ticks_font/family" : "default",
              "color_axis/ticks_font/bold" : False,
              "color_axis/ticks_font/italic" : False,

              "grid/maj_xenabled" : True,
              "grid/maj_yenabled" : True,
              "grid/maj_line/color" : "darkgray",
              "grid/maj_line/width" : 1,
              "grid/maj_line/style" : 'DotLine',
              "grid/min_xenabled" : True,
              "grid/min_yenabled" : True,
              "grid/min_line/color" : "#eaeaea",
              "grid/min_line/width" : 1,
              "grid/min_line/style" : 'DotLine',
              
              "marker/curve/symbol/marker" : 'Rect',
              "marker/curve/symbol/edgecolor" : "blue",
              "marker/curve/symbol/facecolor" : "cyan",
              "marker/curve/symbol/alpha" : .8,
              "marker/curve/symbol/size" : 7,
              "marker/curve/text/font/size" : 8,
              "marker/curve/text/font/family" : "default",
              "marker/curve/text/font/bold" : False,
              "marker/curve/text/font/italic" : False,
              "marker/curve/text/textcolor" : "black",
              "marker/curve/text/background_color" : "#ffffff",
              "marker/curve/text/background_alpha" : 0.8,
              "marker/curve/pen/style" : "SolidLine",
              "marker/curve/pen/color" : "black",
              "marker/curve/pen/width" : 0,
              "marker/curve/linestyle" : 0,
              "marker/curve/spacing" : 7,

              "marker/cross/symbol/marker" : 'Cross',
              "marker/cross/symbol/edgecolor" : "black",
              "marker/cross/symbol/facecolor" : "red",
              "marker/cross/symbol/alpha" : 1.,
              "marker/cross/symbol/size" : 8,
              "marker/cross/text/font/family" : "default",
              "marker/cross/text/font/size" : 8,
              "marker/cross/text/font/bold" : False,
              "marker/cross/text/font/italic" : False,
              "marker/cross/text/textcolor" : "black",
              "marker/cross/text/background_color" : "#ffffff",
              "marker/cross/text/background_alpha" : 0.8,
              "marker/cross/pen/style" : "DashLine",
              "marker/cross/pen/color" : "yellow",
              "marker/cross/pen/width" : 1,
              "marker/cross/linestyle" : 3,
              "marker/cross/spacing" : 7,

              "marker/selectpoint/symbol/marker" : 'Rect',
              "marker/selectpoint/symbol/edgecolor" : "blue",
              "marker/selectpoint/symbol/facecolor" : "cyan",
              "marker/selectpoint/symbol/alpha" : .8,
              "marker/selectpoint/symbol/size" : 7,
              "marker/selectpoint/text/font/size" : 8,
              "marker/selectpoint/text/font/family" : "default",
              "marker/selectpoint/text/font/bold" : False,
              "marker/selectpoint/text/font/italic" : False,
              "marker/selectpoint/text/textcolor" : "black",
              "marker/selectpoint/text/background_color" : "#ffffff",
              "marker/selectpoint/text/background_alpha" : 0.8,
              "marker/selectpoint/pen/style" : "SolidLine",
              "marker/selectpoint/pen/color" : "black",
              "marker/selectpoint/pen/width" : 0,
              "marker/selectpoint/linestyle" : 0,
              "marker/selectpoint/spacing" : 7,

              "marker/cross_section/symbol/marker" : 'Cross',
              "marker/cross_section/symbol/edgecolor" : "cyan",
              "marker/cross_section/symbol/facecolor" : "cyan",
              "marker/cross_section/symbol/alpha" : .8,
              "marker/cross_section/symbol/size" : 7,
              "marker/cross_section/text/font/size" : 8,
              "marker/cross_section/text/font/family" : "default",
              "marker/cross_section/text/font/bold" : False,
              "marker/cross_section/text/font/italic" : False,
              "marker/cross_section/text/textcolor" : "black",
              "marker/cross_section/text/background_color" : "#ffffff",
              "marker/cross_section/text/background_alpha" : 0.8,
              "marker/cross_section/pen/style" : "DashLine",
              "marker/cross_section/pen/color" : "cyan",
              "marker/cross_section/pen/width" : 1,
              "marker/cross_section/linestyle" : 3,
              "marker/cross_section/spacing" : 7,

              "shape/drag/line/style" : 'SolidLine',
              "shape/drag/line/color" : "#ffff00",
              "shape/drag/line/width" : 1,
              "shape/drag/fill/style" : "SolidPattern",
              "shape/drag/fill/color" : "white",
              "shape/drag/fill/alpha" : 0.1,              
              "shape/drag/symbol/marker" : 'Rect',
              "shape/drag/symbol/size" : 3,
              "shape/drag/symbol/edgecolor" : "#ffff00",
              "shape/drag/symbol/facecolor" : "#ffff00",
              "shape/drag/symbol/alpha" : 1.,
              "shape/drag/sel_line/style" : 'SolidLine',
              "shape/drag/sel_line/color" : "#00ff00",
              "shape/drag/sel_line/width" : 1,
              "shape/drag/sel_fill/style" : "SolidPattern",
              "shape/drag/sel_fill/color" : "white",
              "shape/drag/sel_fill/alpha" : 0.1,              
              "shape/drag/sel_symbol/marker" : 'Rect',
              "shape/drag/sel_symbol/size" : 9,
              "shape/drag/sel_symbol/edgecolor" : "#00aa00",
              "shape/drag/sel_symbol/facecolor" : "#00ff00",
              "shape/drag/sel_symbol/alpha" : .7,

              "shape/imageborder/line/style" : 'NoPen',
              "shape/imageborder/line/color" : "gray",
              "shape/imageborder/line/width" : 0,
              "shape/imageborder/fill/style" : "NoBrush",
              "shape/imageborder/fill/color" : "black",
              "shape/imageborder/fill/alpha" : 0.0,              
              "shape/imageborder/fill/angle" : 0.0,
              "shape/imageborder/fill/sx" : 1.0,
              "shape/imageborder/fill/sy" : 1.0,
              "shape/imageborder/symbol/marker" : 'NoSymbol',
              "shape/imageborder/symbol/size" : 7,
              "shape/imageborder/symbol/edgecolor" : "gray",
              "shape/imageborder/symbol/facecolor" : "black",
              "shape/imageborder/symbol/alpha" : .3,
              "shape/imageborder/sel_line/style" : 'SolidLine',
              "shape/imageborder/sel_line/color" : "gray",
              "shape/imageborder/sel_line/width" : 3,
              "shape/imageborder/sel_symbol/marker" : 'Rect',
              "shape/imageborder/sel_symbol/size" : 7,
              "shape/imageborder/sel_symbol/edgecolor" : "gray",
              "shape/imageborder/sel_symbol/facecolor" : "black",
              "shape/imageborder/sel_symbol/alpha" : .8,
              "shape/imageborder/sel_fill/style" : "NoBrush",
              "shape/imageborder/sel_fill/color" : "gray",
              "shape/imageborder/sel_fill/alpha" : 0.5,
              "shape/imageborder/sel_fill/angle" : 0.0,
              "shape/imageborder/sel_fill/sx" : 1.0,
              "shape/imageborder/sel_fill/sy" : 1.0,

              "shape/imagefilter/line/style" : 'SolidLine',
              "shape/imagefilter/line/color" : "#ffff00",
              "shape/imagefilter/line/width" : 1,
              "shape/imagefilter/sel_line/style" : 'SolidLine',
              "shape/imagefilter/sel_line/color" : "#00ffff",
              "shape/imagefilter/sel_line/width" : 2,
              "shape/imagefilter/fill/style" : "NoBrush",
              "shape/imagefilter/fill/color" : "white",
              "shape/imagefilter/fill/alpha" : 0.0,
              "shape/imagefilter/sel_fill/style" : "SolidPattern",
              "shape/imagefilter/sel_fill/color" : "white",
              "shape/imagefilter/sel_fill/alpha" : 0.2,
              "shape/imagefilter/symbol/marker" : 'Rect',
              "shape/imagefilter/symbol/size" : 3,
              "shape/imagefilter/symbol/edgecolor" : "#ffff00",
              "shape/imagefilter/symbol/facecolor" : "#ffff00",
              "shape/imagefilter/symbol/alpha" : 1.,
              "shape/imagefilter/sel_symbol/marker" : 'Ellipse',
              "shape/imagefilter/sel_symbol/size" : 7,
              "shape/imagefilter/sel_symbol/edgecolor" : "#0000ff",
              "shape/imagefilter/sel_symbol/facecolor" : "#00ffff",
              "shape/imagefilter/sel_symbol/alpha" : .8,

              "shape/rectzoom/line/style" : 'SolidLine',
              "shape/rectzoom/line/color" : "#bbbbbb",
              "shape/rectzoom/line/width" : 2,
              # not used -- start
              "shape/rectzoom/sel_line/style" : 'SolidLine',
              "shape/rectzoom/sel_line/color" : "green",
              "shape/rectzoom/sel_line/width" : 2,
              # not used -- end
              "shape/rectzoom/fill/color" : "yellow",
              "shape/rectzoom/fill/style" : "SolidPattern",
              "shape/rectzoom/fill/alpha" : 0.1,
              # not used -- start
              "shape/rectzoom/symbol/marker" : 'NoSymbol',
              "shape/rectzoom/symbol/size" : 0,
              "shape/rectzoom/symbol/edgecolor" : "black",
              "shape/rectzoom/symbol/facecolor" : "yellow",
              "shape/rectzoom/symbol/alpha" : 1.,
              "shape/rectzoom/sel_symbol/marker" : 'Rect',
              "shape/rectzoom/sel_symbol/size" : 5,
              "shape/rectzoom/sel_symbol/edgecolor" : "black",
              "shape/rectzoom/sel_symbol/facecolor" : "yellow",
              "shape/rectzoom/sel_symbol/alpha" : 1.,
              # not used -- end

              "shape/axes/border/line/style" : 'SolidLine',
              "shape/axes/border/line/color" : "magenta",
              "shape/axes/border/line/width" : 1,
              "shape/axes/border/sel_line/style" : 'SolidLine',
              "shape/axes/border/sel_line/color" : "magenta",
              "shape/axes/border/sel_line/width" : 2,
              "shape/axes/border/fill/style" : "NoBrush",
              "shape/axes/border/fill/color" : "magenta",
              "shape/axes/border/fill/alpha" : 0.0,
              "shape/axes/border/sel_fill/style" : "SolidPattern",
              "shape/axes/border/sel_fill/color" : "magenta",
              "shape/axes/border/sel_fill/alpha" : 0.3,
              "shape/axes/border/symbol/marker" : 'NoSymbol',
              "shape/axes/border/symbol/size" : 0,
              "shape/axes/border/symbol/edgecolor" : "black",
              "shape/axes/border/symbol/facecolor" : "yellow",
              "shape/axes/border/symbol/alpha" : 1.,
              "shape/axes/border/sel_symbol/marker" : 'NoSymbol',
              "shape/axes/border/sel_symbol/size" : 5,
              "shape/axes/border/sel_symbol/edgecolor" : "black",
              "shape/axes/border/sel_symbol/facecolor" : "yellow",
              "shape/axes/border/sel_symbol/alpha" : 1.,
              "shape/axes/arrow_size" : 8,
              "shape/axes/arrow_angle" : 30,
              "shape/axes/xarrow_pen/style" : 'SolidLine',
              "shape/axes/xarrow_pen/color" : "red",
              "shape/axes/xarrow_pen/width" : 1,
              "shape/axes/xarrow_brush/color" : "red",
              "shape/axes/xarrow_brush/alpha" : 0.2,
              "shape/axes/yarrow_pen/style" : 'SolidLine',
              "shape/axes/yarrow_pen/color" : "green",
              "shape/axes/yarrow_pen/width" : 1,
              "shape/axes/yarrow_brush/color" : "green",
              "shape/axes/yarrow_brush/alpha" : 0.2,

              "shape/cross_section/line/style" : 'DotLine',
              "shape/cross_section/line/color" : "#ff5555",
              "shape/cross_section/line/width" : 1,
              "shape/cross_section/fill/style" : "SolidPattern",
              "shape/cross_section/fill/color" : "white",
              "shape/cross_section/fill/alpha" : 0.1,              
              "shape/cross_section/symbol/marker" : 'Diamond',
              "shape/cross_section/symbol/size" : 7,
              "shape/cross_section/symbol/edgecolor" : "#ff5555",
              "shape/cross_section/symbol/facecolor" : "#ff5555",
              "shape/cross_section/symbol/alpha" : .6,
              "shape/cross_section/sel_line/style" : 'DotLine',
              "shape/cross_section/sel_line/color" : "#ff0000",
              "shape/cross_section/sel_line/width" : 1,
              "shape/cross_section/sel_fill/style" : "SolidPattern",
              "shape/cross_section/sel_fill/color" : "white",
              "shape/cross_section/sel_fill/alpha" : 0.1,              
              "shape/cross_section/sel_symbol/marker" : 'Diamond',
              "shape/cross_section/sel_symbol/size" : 9,
              "shape/cross_section/sel_symbol/edgecolor" : "#aa0000",
              "shape/cross_section/sel_symbol/facecolor" : "#ff0000",
              "shape/cross_section/sel_symbol/alpha" : .7,

              "shape/point/line/style" : 'SolidLine',
              "shape/point/line/color" : "#ffff00",
              "shape/point/line/width" : 1,
              "shape/point/sel_line/style" : 'SolidLine',
              "shape/point/sel_line/color" : "#00ff00",
              "shape/point/sel_line/width" : 1,
              "shape/point/fill/style" : "NoBrush",
              "shape/point/sel_fill/style" : "NoBrush",
              "shape/point/symbol/marker" : 'XCross',
              "shape/point/symbol/size" : 9,
              "shape/point/symbol/edgecolor" : "#ffff00",
              "shape/point/symbol/facecolor" : "#ffff00",
              "shape/point/symbol/alpha" : 1.,
              "shape/point/sel_symbol/marker" : 'XCross',
              "shape/point/sel_symbol/size" : 12,
              "shape/point/sel_symbol/edgecolor" : "#00aa00",
              "shape/point/sel_symbol/facecolor" : "#00ff00",
              "shape/point/sel_symbol/alpha" : .7,

              "shape/segment/line/style" : 'SolidLine',
              "shape/segment/line/color" : "#ffff00",
              "shape/segment/line/width" : 1,
              "shape/segment/sel_line/style" : 'SolidLine',
              "shape/segment/sel_line/color" : "#00ff00",
              "shape/segment/sel_line/width" : 1,
              "shape/segment/fill/style" : "NoBrush",
              "shape/segment/sel_fill/style" : "NoBrush",
              "shape/segment/symbol/marker" : 'XCross',
              "shape/segment/symbol/size" : 9,
              "shape/segment/symbol/edgecolor" : "#ffff00",
              "shape/segment/symbol/facecolor" : "#ffff00",
              "shape/segment/symbol/alpha" : 1.,
              "shape/segment/sel_symbol/marker" : 'XCross',
              "shape/segment/sel_symbol/size" : 12,
              "shape/segment/sel_symbol/edgecolor" : "#00aa00",
              "shape/segment/sel_symbol/facecolor" : "#00ff00",
              "shape/segment/sel_symbol/alpha" : .7,

              "shape/label/symbol/marker" : "NoSymbol",
              "shape/label/symbol/size" : 0,
              "shape/label/symbol/edgecolor" : "white",
              "shape/label/symbol/facecolor" : "white",
              "shape/label/border/style" : "SolidLine",
              "shape/label/border/color" : "#cbcbcb",
              "shape/label/border/width" : 0,
              "shape/label/font/size" : 8,
              "shape/label/font/family": "default",
              "shape/label/font/bold" : False,
              "shape/label/font/italic" : False,
              "shape/label/color" : "white",
              "shape/label/bgcolor" : "black",
              "shape/label/bgalpha" : 0.25,
              "shape/label/abspos" : False,
              "shape/label/move_anchor" : True,

              "label/symbol/marker" : "NoSymbol",
              "label/symbol/size" : 0,
              "label/symbol/edgecolor" : "white",
              "label/symbol/facecolor" : "white",
              "label/border/style" : "SolidLine",
              "label/border/color" : "#cbcbcb",
              "label/border/width" : 1,
              "label/font/size" : 9,
              "label/font/family": "default",
              "label/font/bold" : False,
              "label/font/italic" : False,
              "label/color" : "black",
              "label/bgcolor" : "white",
              "label/bgalpha" : 0.8,
              "label/anchor" : "TL",
              "label/xc" : 0,
              "label/yc" : 0,
              "label/abspos" : True,
              "label/absg" : "TR",
              "label/xg" : 0.0,
              "label/yg" : 0.0,

              # info_label: used in builder.make.computation for example
              "info_label/symbol/marker" : "NoSymbol",
              "info_label/symbol/size" : 0,
              "info_label/symbol/edgecolor" : "white",
              "info_label/symbol/facecolor" : "white",
              "info_label/border/style" : "SolidLine",
              "info_label/border/color" : "#cbcbcb",
              "info_label/border/width" : 1,
              "info_label/font/size" : 9,
              "info_label/font/family": "default",
              "info_label/font/bold" : False,
              "info_label/font/italic" : False,
              "info_label/color" : "black",
              "info_label/bgcolor" : "white",
              "info_label/bgalpha" : 0.8,
              "info_label/anchor" : "TL",
              "info_label/xc" : 0,
              "info_label/yc" : 0,
              "info_label/abspos" : True,
              "info_label/absg" : "TR",
              "info_label/xg" : 0.0,
              "info_label/yg" : 0.0,

              "legend/border/style" : "SolidLine",
              "legend/border/color" : "#cbcbcb",
              "legend/border/width" : 1,
              "legend/font/size" : 8,
              "legend/font/family": "default",
              "legend/font/bold" : False,
              "legend/font/italic" : False,
              "legend/color" : "black",
              "legend/bgcolor" : "white",
              "legend/bgalpha" : 0.8,
              "legend/anchor" : "TR",
              "legend/xc" : 0,
              "legend/yc" : 0,
              "legend/abspos" : True,
              "legend/absg" : "TR",
              "legend/xg" : 0.0,
              "legend/yg" : 0.0,
              },
              
            'histogram' :
             {
              "antialiasing" : False,
              
              "title/font/size" : 11,
              "title/font/bold" : False,
              "label/font/size" : 9,
              "label/font/bold" : False,

              "curve/line/style" : 'NoPen',
              "curve/line/color" : "green",
              "curve/line/width" : 1,
              "curve/symbol/marker" : "NoSymbol",
              "curve/symbol/size" : 0,
              "curve/symbol/edgecolor" : "white",
              "curve/symbol/facecolor" : "black",
              "curve/symbol/alpha" : 1.,
              "curve/shade" : .85,
              "curve/fitted" : False,
              "curve/curvestyle" : "Steps",
              "curve/label" : "",

              "range/line/style" : 'SolidLine',
              "range/line/color" : "#ff9393",
              "range/line/width" : 1,
              "range/sel_line/style" : 'SolidLine',
              "range/sel_line/color" : "red",
              "range/sel_line/width" : 2,
              "range/fill" : "red",
              "range/shade" : 0.15,
              "range/symbol/marker" : "NoSymbol",
              "range/symbol/size" : 5,
              "range/symbol/edgecolor" : "black",
              "range/symbol/facecolor" : "yellow",
              "range/symbol/alpha" : 1.,
              "range/sel_symbol/marker" : "Ellipse",
              "range/sel_symbol/size" : 9,
              "range/sel_symbol/edgecolor" : "white",
              "range/sel_symbol/facecolor" : "red",
              "range/sel_symbol/alpha" : .9,
              "range/multi/color" : "#806060",

              # Default parameters for plot axes
              "axis/title" : "",
              "axis/color" : "black",
              "axis/title_font/size" : 7,
              "axis/title_font/family" : "default",
              "axis/title_font/bold" : False,
              "axis/title_font/italic" : False,
              "axis/ticks_font/size" : 7,
              "axis/ticks_font/family" : "default",
              "axis/ticks_font/bold" : False,
              "axis/ticks_font/italic" : False,

              "grid/background" : "#FFFFFF",
              "grid/maj_xenabled" : True,
              "grid/maj_yenabled" : True,
              "grid/maj_line/color" : "darkgray",
              "grid/maj_line/width" : 1,
              "grid/maj_line/style" : 'DotLine',
              "grid/min_xenabled" : True,
              "grid/min_yenabled" : False,
              "grid/min_line/color" : "#eaeaea",
              "grid/min_line/width" : 1,
              "grid/min_line/style" : 'DotLine',

              "marker/curve/symbol/marker" : 'Ellipse',
              "marker/curve/symbol/edgecolor" : "black",
              "marker/curve/symbol/facecolor" : "blue",
              "marker/curve/symbol/alpha" : .8,
              "marker/curve/symbol/size" : 8,
              "marker/curve/text/font/size" : 11,
              "marker/curve/text/font/family" : "default",
              "marker/curve/text/font/bold" : False,
              "marker/curve/text/font/italic" : False,
              "marker/curve/text/textcolor" : "darkBlue",
              "marker/curve/text/background_color" : "blue",
              "marker/curve/text/background_alpha" : 0.2,
              "marker/curve/pen/style" : "SolidLine",
              "marker/curve/pen/color" : "black",
              "marker/curve/pen/width" : 0,
              "marker/curve/linestyle" : 0,

              "marker/cross/symbol/marker" : 'Cross',
              "marker/cross/symbol/edgecolor" : "black",
              "marker/cross/symbol/facecolor" : "red",
              "marker/cross/symbol/alpha" : 1.,
              "marker/cross/symbol/size" : 8,
              "marker/cross/text/font/family" : "default",
              "marker/cross/text/font/size" : 11,
              "marker/cross/text/font/bold" : False,
              "marker/cross/text/font/italic" : False,
              "marker/cross/text/textcolor" : "darkBlue",
              "marker/cross/text/background_color" : "blue",
              "marker/cross/text/background_alpha" : 0.2,
              "marker/cross/pen/style" : "SolidLine",
              "marker/cross/pen/color" : "black",
              "marker/cross/pen/width" : 1,
              "marker/cross/linestyle" : 3,
              },
              
            'cross_section' :
             {
              "antialiasing" : False,
              
              "title/font/size" : 11,
              "title/font/bold" : False,
              "label/font/size" : 9,
              "label/font/bold" : False,

              "curve/line/style" : 'SolidLine',
              "curve/line/color" : "blue",
              "curve/line/width" : 1,
              "curve/symbol/marker" : "NoSymbol",
              "curve/symbol/size" : 0,
              "curve/symbol/edgecolor" : "white",
              "curve/symbol/facecolor" : "black",
              "curve/symbol/alpha" : 1.,
              "curve/shade" : 0.,
              "curve/fitted" : False,
              "curve/label" : "",

              "range/line/style" : 'SolidLine',
              "range/line/color" : "#ff9393",
              "range/line/width" : 1,
              "range/sel_line/style" : 'SolidLine',
              "range/sel_line/color" : "red",
              "range/sel_line/width" : 2,
              "range/fill" : "red",
              "range/shade" : 0.15,
              "range/symbol/marker" : "NoSymbol",
              "range/symbol/size" : 5,
              "range/symbol/edgecolor" : "black",
              "range/symbol/facecolor" : "yellow",
              "range/symbol/alpha" : 1.,
              "range/sel_symbol/marker" : "Ellipse",
              "range/sel_symbol/size" : 9,
              "range/sel_symbol/edgecolor" : "white",
              "range/sel_symbol/facecolor" : "red",
              "range/sel_symbol/alpha" : .9,
              "range/multi/color" : "#806060",

              # Default parameters for plot axes
              "axis/title" : "",
              "axis/color" : "black",
              "axis/title_font/size" : 7,
              "axis/title_font/family" : "default",
              "axis/title_font/bold" : False,
              "axis/title_font/italic" : False,
              "axis/ticks_font/size" : 7,
              "axis/ticks_font/family" : "default",
              "axis/ticks_font/bold" : False,
              "axis/ticks_font/italic" : False,

              "grid/background" : "#FFFFFF",
              "grid/maj_xenabled" : True,
              "grid/maj_yenabled" : True,
              "grid/maj_line/color" : "darkgray",
              "grid/maj_line/width" : 1,
              "grid/maj_line/style" : 'DotLine',
              "grid/min_xenabled" : False,
              "grid/min_yenabled" : False,
              "grid/min_line/color" : "#eaeaea",
              "grid/min_line/width" : 1,
              "grid/min_line/style" : 'DotLine',

              "marker/curve/symbol/marker" : 'Ellipse',
              "marker/curve/symbol/edgecolor" : "black",
              "marker/curve/symbol/facecolor" : "blue",
              "marker/curve/symbol/alpha" : .8,
              "marker/curve/symbol/size" : 8,
              "marker/curve/text/font/size" : 11,
              "marker/curve/text/font/family" : "default",
              "marker/curve/text/font/bold" : False,
              "marker/curve/text/font/italic" : False,
              "marker/curve/text/textcolor" : "darkBlue",
              "marker/curve/text/background_color" : "blue",
              "marker/curve/text/background_alpha" : 0.2,
              "marker/curve/pen/style" : "SolidLine",
              "marker/curve/pen/color" : "black",
              "marker/curve/pen/width" : 0,
              "marker/curve/linestyle" : 0,

              "marker/cross/symbol/marker" : 'Cross',
              "marker/cross/symbol/edgecolor" : "black",
              "marker/cross/symbol/facecolor" : "red",
              "marker/cross/symbol/alpha" : 1.,
              "marker/cross/symbol/size" : 8,
              "marker/cross/text/font/family" : "default",
              "marker/cross/text/font/size" : 11,
              "marker/cross/text/font/bold" : False,
              "marker/cross/text/font/italic" : False,
              "marker/cross/text/textcolor" : "darkBlue",
              "marker/cross/text/background_color" : "blue",
              "marker/cross/text/background_alpha" : 0.2,
              "marker/cross/pen/style" : "SolidLine",
              "marker/cross/pen/color" : "black",
              "marker/cross/pen/width" : 1,
              "marker/cross/linestyle" : 3,
              },
              
            }

from guidata.config import CONF
CONF.update_defaults(DEFAULTS)
