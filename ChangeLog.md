## Version 2.3.1 ##

### Bug fixes (since v2.3.0) ###

  * Fixed build failures occuring on non-Windows platforms ([Issue 54](https://code.google.com/p/guiqwt/issues/detail?id=54))
  * Fixed requirements in README and setup.py: guiqwt v2.3 requires guidata v1.6


---


## Version 2.3.0 ##

### New features (since v2.2.1) ###

  * Added support for Python 3: a single code source base compatible with both Python 2 and Python 3
  * `scaler` C++ extension: added alternative implementations of C99 features so that this extension is now compatible with Microsoft Visual C++ compiler (was only compatible with gcc)
  * Replaced all Fortran 77/90 extensions by Cython extensions:
    * Building `guiqwt` no longer requires a Fortran compiler (but only a C/C++ compiler for the C++ scaler extension and the C Cython extensions)
    * 2-D histogram items are drawn 3 times faster than before
    * The Mandelbrot example runs faster too

### Bug fixes (since v2.2.1) ###

  * `guiqwt.image_nanmin/_nanmax`: bug fixed when data is a numpy.ma.MaskedArray object
  * `guiqwt.styles`: using copy.deepcopy instead of copy.copy in `ItemParameters.get` to avoid side effects when using more than one instance of a DataSet object
  * `guiqwt.annotations`: fixed bug when showing an AnnotatedShape object on an empty plot (unit was None)
  * Fixed `PolygonShape` items pickle support (save\_items, restore\_items)


---


## Version 2.2.1 ##

### New features (since v2.2.0) ###

  * Added support for plot items serialization/deserialization to/from HDF5:
    * See `save_item`, `load_item`, `save_items` and `load_items` functions in `guiqwt.io`
    * io.save\_item/load\_item (HDF5): None can be saved/loaded instead of a real item
    * See `serialize` (save to) and `deserialize` (load from) methods in plot objects (save all items) or plot item objects
    * See the new test `loadsaveitems_hdf5.py`
  * builder/images: added option 'center\_on' to center image data on point of coordinates 'center\_on' (tuple)
  * Flip/Rotate widget/dialog: added method 'set\_parameters' to set default transform parameters
  * guiqwt.tools.SignalStatsTool.move: added X range to label
  * BaseCurveWidget/BaseImageWidget: added argument `curve_antialiasing` to switch on/off the curve antialiasing feature (this option may be passed to CurveWidget, CurveDialog, ImageWidget or ImageDialog through the `options` dictionary)
  * ([Issue 29](https://code.google.com/p/guiqwt/issues/detail?id=29)) Added test 'customize\_shape\_tool.py' to demonstrate how easy it is to customize a shape created with a tool like RectangleTool, EllipseTool, etc.
  * ([Issue 37](https://code.google.com/p/guiqwt/issues/detail?id=37)) Plot axis widget: added support for mouse double-click to set the axis range

### Possible API compatibility issues (since v2.2.0) ###

  * guiqwt now requires Python 2.6 (Python 2.5 support has been dropped)
  * `guiqwt.io` module: file type filters are now sorted depending on data types
    * `iohandler.load_filters` and `iohandler.save_filters` properties have been replaced by a method `iohandler.get_filters`:
      * iohandler.load\_filter --> iohandler.get\_filters('load')
      * iohandler.save\_filter --> iohandler.get\_filters('save')
  * guidata.hdf5io.HDF5Reader.read: argument 'dataset' was renamed to 'instance'
  * MaskedImageItem: masked\_areas attribute is now a list of MaskedArea objects (so that MaskedImageItem objects serialization is easier to implement)
  * Removed deprecated tools DuplicateCurveTool and DeleteCurveTool

### Bug fixes (since v2.2.0) ###

  * MaskedImageItem/bugfix: fixed rounding error when applying mask to item
  * io.imread: drastically reduced loading time with PIL.Image
  * RGB images support: fixed vertical orientation issue
  * Fixed memory leaks in selection tool, image/curve stats tools and contrast tool
  * Curve plot: setting axis scale of both X and Y axes at the same time was not working
  * [Issue 27](https://code.google.com/p/guiqwt/issues/detail?id=27): fixed FTBFS on kfreebsd due to Werror flag (patch from Frédéric Picca)
  * FreeFormTool/MultiLineTool: fixed warning when clicking the first two points if these two points are at the exact same position (happened only when creating such a shape on an empty canvas)
  * Fixed "Edit data..." tool: `oedit` function returns None when dialog is canceled or an array when it's validated (fixed "truth value" error)
  * ([Issue 32](https://code.google.com/p/guiqwt/issues/detail?id=32)) pyplot/better compatibility with Matplotlib: `plot` now accepts lists instead of NumPy arrays
  * ([Issue 33](https://code.google.com/p/guiqwt/issues/detail?id=33)) tools.LoadItemsTool: parent constructor was not called
  * ([Issue 36](https://code.google.com/p/guiqwt/issues/detail?id=36)) plot.PlotManager: fixed typo when setting the plot manager to `plot_id`


---


## Version 2.2.0 ##

### New features (since v2.1.6) ###

  * Added scaler module: resize function (using scaler C++ engine to resize images) which is incredibly faster than scipy.misc.imresize
  * `guiqwt.io` module was rewritten: new extensible I/O functions `imwrite`/`imread` (see section 'Possible API compatibility issues')
  * SelectTool:
    * added Undo/Redo actions (triggered by platform's standard key sequences)
    * "Select all" action is now triggered by platform's standard key sequence
  * Added 'get\_segment' test (analog to 'get\_point')
  * Interactive tools: added argument 'switch\_to\_default\_tool' (if True, when tool action is finished, plot manager will automatically switch to the default tool)
  * Added `label.!RangeInfo` object: showing !XRangeSelection shape informations (x, dx) in a label. See associated method 'range\_info\_label' in 'builder.make' singleton and unit test in 'tests/computations.py'.
  * Snapshot tool: added an option to apply (or not) the interpolation algorithm
  * `guiqwt.pyplot`: selecting default item type, hence allowing to use directly tools when there is only one curve/image without having to select it before
  * Added new guiqwt svg logo
  * Added new dialogs and widgets for manipulating (multiple) images:
    * Rotate&Crop dialog, widget and tool (+ test) for TrImageItem plot items
    * Flip&Rotate dialog and widget
  * `pyplot.imshow`: added interpolation option ('nearest', 'linear', 'antialiasing')
  * `io.imagefile_to_array`: added support for 16-bit Tiff with PhotoInterpretation=1
  * ResizeDialog: added option "keep original size" to bypass this dialog
  * RectangularActionTool: added option 'fix\_orientation' (default: False, but set to True for the SnapshotTool)

### Possible API compatibility issues (since v2.1.6) ###

  * `guiqwt.io` module was rewritten -- potential API breaks:
    * `imagefile_to_array` --> `imread`
    * `array_to_imagefile` --> `imwrite`
    * `array_to_dicomfile` --> `imwrite`
    * `IMAGE_LOAD_FILTERS` --> `iohandler.load_filters`
    * `IMAGE_SAVE_FILTERS` --> `iohandler.save_filters`
    * `set_dynamic_range_from_dtype` --> `scale_data_to_dtype`

  * Created `guiqwt.widgets` package to regroup ResizeDialog and RotateCropDialog/Widget
  * Moved module `guiqwt.fit` to `guiqwt.widgets` package

### Bug fixes (since v2.1.6) ###

  * `guiqwt.geometry` : fixed zero division error in `compute_angle` function
  * Fixed minimum value for histogram display
  * Fixed [Issue 16](https://code.google.com/p/guiqwt/issues/detail?id=16): use double precision for point baseclass
  * Fixed rounding error in image.assemble\_imageitems: concerns the snapshot tool, and the new rotate/crop dialog box (Rotate/Crop dialog: added a specific test checking if exported image is exactly identical to the original image when the cropping rectangle has the same size and position as the image below -- see rotatecrop.py test script).
  * scaler: linear interpolation was inactive on image edges (first/last col/row)
  * ImagePlot widget: fixed aspect ratio when showing the widget for the first time
  * Events/Hit test:
    * Plot item: fixed AttributeError with cursors (when clicking on the canvas with no current active item)
    * Curve item: avoid showing dividing by zero warning
  * tools.SnapshotTool:
    * now fixing ROI orientation to avoid the negative size issue
    * now handling out of memory errors for big images


---


## Version 2.1.6 ##

### Other changes (since v2.1.5) ###

  * guiqwt.pyplot.savefig:
    * added support for all image types supported by Qt (JPEG, TIFF, PNG, ...)
    * first argument (`fname`) may now be a file-like object (e.g. !StringIO)
  * guiqwt.baseplot/curve: added stepsize in `set_axis_limits` and removed from `set_axis_ticks`
  * guiqwt.image:
    * QuadGridItem: allow set\_data to update X,Y along with Z
    * new item PolygonMapItem: PolygonMapItem is intended to display maps i.e. items containing several hundreds of independent polygons
  * guiqwt.builder.make.error: added options 'errorbarwidth', 'errorbarcap', 'errorbarmode' and 'errorbaralpha' (avoid having to tweak the ErrorBarParam to customize these settings)
  * guiqwt.pyplot/pydicom: avoid the annoying warning message about the DICOM dictionnary revert
  * guiqwt.tools:
    * EditItemDataTool: new tool for editing displayed curve/image data using a GUI-based array editor (this feature requires the `spyderlib` library)

### Bug fixes (since v2.1.5) ###

  * ErrorBarCurveItem (error bar curves):
    * now handling NaNs uncertainties properly
    * handling runtime warnings that could end badly in draw method (example: transforming a zero in log scale)
  * Annotations/pickle bugfix: a !QString (instead of unicode) was pickled for annotation title, hence leading to compatiblity issues with PyQt API v2
  * guiqwt.io.array\_to\_dicomfile: fixed value representation error for smallest/largest pixel value parameters
  * guiqwt.resizedialog.is\_edit\_valid: fixed compatibility issue with PyQt API v2
  * Sift: upgraded deployment script for compatibility with guidata v1.4+
  * geometry.colvector: fixed major regression in coordinates calculations (significative impact on TrImageItem related features)


---


## Version 2.1.5 ##

### Other changes (since v2.1.4) ###

  * guiqwt.io: added function 'eliminate\_outliers' to cut image levels histogram (previously available only for display)
  * baseplot: added method 'copy\_to\_clipboard' + tools: added CopyToClipboardTool (copy canevas window to clipboard)


---


## Version 2.1.4 ##

Since this version, `guiqwt` is compatible with PyQt4 API #1 **and** API #2.
Please read carefully the coding guidelines which have been recently added to
the documentation.

### Bug fixes (since v2.1.3) ###

  * Sift/bugfix: difference/division operations were performed backwards (s001-s000 instead of s000-s001)
  * Sift: working directory is now changed after opening/saving signal/image
  * label.RangeComputation: fixed bug if compute function was returning more than one result and when X-range was empty (e.g. selection is outside curve X-axis values)
  * curve.CurvePlot: fixed pan/zoom erratic behavior for curves associated with log-scale axes
  * baseplot.BasePlot: now performing an autoscale after changing axis lin/log scale (set\_axis\_scale/set\_scales)
  * annotations.AnnotatedSegment/CRITICAL: fixed an error (introduced in v2.1.0) when computing segment length (returned length was twice lower than the real value)
  * image.XYImageItem (Contributor: Carlos Pascual): fixed bug when Y-axis array is of dimension Ni+1 (where Ni is the number of rows of the image pixel data array)
  * Fixed compatiblity issues with PyQt v4.4 (Contributor: Carlos Pascual)
  * (minor) Fixed label text (too long) of 2D-Histogram items background color in shown DataSet
  * guiqwt.io.array\_to\_dicomfile/bugfix: Smallest/LargestImagePixelValue fields had wrong type (str instead of int)
  * LabelTool: label was not moved as expected (default: now, label is **not** attached to canvas)
  * tools.ImageStatsTool/bugfix: image title was not shown
  * CurvePlot: autoscale for log scales / bugfix: handling zero values
  * tools.AxisScaleTool/bugfix: when updating its status, the tool was setting the axes scales even when not necessary, hence causing an autoscale since changeset 1159 (687e22074f8d)
  * ItemCenterTool was not working as expected when centering annotated shapes having a specific transform matrix
  * XYImageItem objects: re-added cross-section support (removed accidently)
  * Curve autoscale method (curve.CurvePlot/ErrorBarCurvePlot):
    * now handles non-finite values (NaNs and infs)
    * logarithmic scales: now excludes zero/negative values to avoid confusing the autoscale algorithm

### Possible API compatibility issues (since v2.1.3) ###

  * Moved functions from guiqwt.io to new module guiqwt.qthelpers: exec\_image\_save\_dialog, exec\_image\_open\_dialog, exec\_images\_open\_dialog
  * Markers:
    * label and constraint callbacks take now 2 arguments (the marker's coordinates) instead of 3
    * removed method 'move\_point\_to': use new method 'set\_pos' instead (takes two arguments: x, y)
  * Removed cursors introduced in v2.1.0:
    * These cursors have been replaced by shapes.Marker (i.e. objects derived from QwtPlotMarker)
    * Removed signals.SIG\_CURSOR\_MOVED, shapes.HorizontalCursor, shapes.VerticalCursor, annotations.AnnotatedHCursor, annotations.AnnotatedVCursor and associated builder methods (annotated\_vcursor, annotated\_hcursor)
    * Builder methods vcursor and hcursor were slightly changed (see tests/cursors.py to adapt your code)
    * Use markers instead of cursors (and SIG\_MARKER\_CHANGED instead of SIG\_CURSOR\_MOVED -- arguments are not identical, see signals.py):
      * base object: shapes.Marker
      * associated builder methods: marker, vcursor, hcursor, xcursor (see tests/cursors.py)
  * label.LabelItem: renamed method 'set\_position' to 'set\_pos' (consistency with shapes.PointShape, ...)
  * Annotations:
    * method `get_center` now returns coordinates **without** applying the transform matrix, i.e. in pure plot coordinates
    * the following methods were renamed to highlight the fact that the transform matrix is applied in those computations:
      * `get_center` was renamed to `get_tr_center`
      * `get_size` was renamed to `get_tr_size`
      * `get_angle` was renamed to `get_tr_angle`
      * `get_diameter` was renamed to `get_tr_diameter`
      * `get_length` was renamed to `get_tr_length`
  * Removed the following deprecated classes in `guiqwt.plot`:
    * CurvePlotWidget (renamed to CurveWidget)
    * CurvePlotDialog (renamed to CurveDialog)
    * ImagePlotWidget (renamed to ImageWidget)
    * ImagePlotDialog (renamed to ImageDialog)

### Other changes (since v2.1.3) ###

  * Added module qthelpers: image open/save dialog helpers (moved from guiqwt.io to avoid using GUIs in this module)
  * Annotation/default style: changed string formatting from '%d' to '%.1f'
  * baseplot.BasePlot.add\_item: when adding the same item twice, printing a warning message
  * Using new guidata.qt PyQt4->PySide transitional package
  * Sift: ROI extraction ("Crop"-->"ROI extraction" + added the same feature for signals), added "swap axes" operation for signals/images, added "normalize" processing for signals only
  * Sift: added linear calibration (signals: X/Y axes, images: Z axis)
  * Interactive tools: added signal SIG\_TOOL\_JOB\_FINISHED emitted when tool has finished its job + if SWITCH\_TO\_DEFAULT\_TOOL class attribute is True, switching to the default interactive tool
  * Buider: added cross cursor and marker constructors (builder.make.marker and builder.make.xcursor, see tests/cursors.py)
  * Added SignalStatsTool (standard curve tool) to show ymin, ymax, ymean, ... on a selected curve ROI
  * Sift: added support for curve data with error bars (I/O + operations + processing)
  * Added coding guidelines to the documentation
  * builder/make.computation/computation2d: added title option (defaults to object's (curve or image) label)
  * plot.CurvePlot, plot.CurveWidget: added keyword arguments 'xunit' and 'yunit' to set axes units (same syntax as labels)
  * plot.ImagePlot, plot.ImageWidget: added keyword arguments 'xunit', 'yunit' and 'zunit' to set axes units (same syntax as labels)
  * pyplot.imshow: added keyword argument 'mask' to support masked arrays display


---


## Version 2.1.3 ##

### Bug fixes (since v2.1.2) ###

  * tools.RectangularActionTool: removed unnecessary calls to setup\_shape\_appearance
  * tools.ImageStatsTool/CrossSectionTool.setup\_shape / bugfix: parent method was not called
  * Sift/bugfix: Spyder's internal shell was not parented -- this was causing issues with spyderlib v2.0.11
  * Cross section/auto refresh toggle button: do not refresh plot if disabling the auto refresh mode
  * (Fixes [Issue 14](https://code.google.com/p/guiqwt/issues/detail?id=14)) tools.CommandTool: docstring was translated from french
  * (Fixes [Issue 13](https://code.google.com/p/guiqwt/issues/detail?id=13)) Fixed precision/string formatting issue: switched from '%f' to '%g' (on-curve labels, ...)

### Possible API compatibility issues (since v2.1.2) ###

  * baseplot.BasePlot.get\_selected\_items: added argument 'z\_sorted' in first position (like in get\_items)

### Other changes (since v2.1.2) ###

  * added **this** changelog
  * baseplot/plot axes styles: added support for physical unit
  * annotations/attached label: added automatic axes unit support
  * annotations: added support for measurement relative uncertainty
  * fit/Fit param widgets: added suffix label + code cleaning
  * guiqwt.io/sift: open/save image dialog code refactoring
  * tools.ExportItemDataTool: added support for images
  * Added tool ItemCenterTool: center objects (rectangle, ellipse and their annotated counterparts)
  * Cross section panel: when a cross section shape has been removed, clearing cross section curve before removing it (notify other panels)
  * Cross sections/update\_plot: added option 'refresh' (default: True) --> we do not want to refresh the cross section panel systematically after registering a new shape
  * Annotations/annotationparam: added 'readonly' and 'private' options (bugfix: these parameters are now pickled correctly for shapes)


---


## Version 2.1.2 ##

### Bug fixes (since v2.1.1) ###

  * 1D Computations: now support error bar curves as well as simple curves
  * test\_line test: this test should have been excluded from test list + it should be possible to import it without executing it... fixed!

### Other changes (since v2.1.1) ###

  * guiqwt.fit: code cleaning / reimplementing FitParam.create\_widgets is now supported


---


## Version 2.1.1 ##

### Bug fixes (since v2.1.0) ###

  * Distributed source package: unwanted Sift build/dist files were eventually included in the package
  * setup.py: fixed sphinx ImportError issue when building autodoc from source package (not finding the just built extension module)
  * ErrorBarCurveItem/bugfix: did not support empty data
  * Cross section panel: do not compute cross section each time a plot item is added/deleted
  * annotations/Annotated cursor: couple of bugfixes + label color is changed when selecting/unselecting annotation
  * annotations/tools: code cleaning + minor bugfixes (styles were not applied as expected)
  * scaler.cpp/bugfix for float source images: values were converted to integers
  * Sift/arbitrary rotation: added option "reshape" (default: True)
  * Fix building the f90 extension on some systems
  * Curve plots: fixed autoscale behavior for logarithmic scales
  * fit/bugfix: when the fit params number was not a multiple of the layout column count, the last parameters were not shown

### Other changes (since v2.1.0) ###

  * shapes: added ObliqueRectangleShape
  * tools: added ObliqueRectangleTool and AnnotatedObliqueRectangleTool
  * Added averaged oblique cross section (panel and tools)
  * plot items/Refactoring: methods 'set\_selectable', 'set\_resizable', 'set\_movable' and 'set\_rotatable' are now mandatory for all plot items (not only the image items as before)
  * tools.ImageMaskTool/icon: more contrasted icon (in order to discriminate easily the disabled icon from the enabled one)
  * plot.PlotManager: added method 'get\_tool' (returns tool's instance from its class, if added to manager...)
  * tools / New ExportItemData tool: supports only curve items (for now)
  * tools.CrossSectionTool/AverageCrossSectionTool -- shape setup: added class attribute SHAPE\_TITLE + do not hide computations anymore
  * pyplot/Axes: added methods 'set\_xlim' and 'set\_ylim'
  * shapes.py/image.py: code refactoring/cleaning --> geometry.py
  * Rectangular shapes/annotations: added method get\_bounding\_rect\_coords
  * cross\_section.CrossSectionPlot: added attribute 'single\_source' / if True, only one image source is processed
  * Improve pcolor, refactor scaler sources
  * Handle Nan's quietly while computing lut min/max
  * Added basic function computation on hist2d
  * Allowed Histogram2DItems to have VOI, palettes and transparent backgrounds


---


## Version 2.1.0 ##

### Bug fixes (since v2.0.8) ###

  * cross\_section: CrossSectionWidget.update\_plot argument 'obj' was not optional as in CrossSectionPlot.update\_plot
  * Contrast adjustment panel: when setting range (i.e. possible change of image data), levels histogram was not updated
  * Tests: handling I/O errors occuring when user has no write permission on current directory
  * Image items: bugfixes in ImageItem (scale issues: replaced x0,y0,dx,dy by xmin,xmax,ymin,ymax) + added intermediate class RawImageItem (ImageItem without scale)
  * Image module: fixed pixel alignment issues (get\_closest\_indexes, ...)
  * TrImageParam: fixed wrong class inheritance
  * LegendBoxItem/bugfix: missing argument for include\_item
  * guiqwt.image.get\_filename: bugfix when filename is None
  * ErrorBarCurveItem.set\_data: now accepts None for both dx and dy (interface consistency with its parent class, CurveItem)
  * Image items/Align rectangular shape to image pixels/bugfix: this feature was not working for scaled images (ImageItem, MaskImageItem, ...)
  * guiqwt.curve/image: improved autoscale method (now works with curves plotted on two different Y-axes)
  * guiqwt.image: fixed issues related to empty filename/data when pickling/unpickling items
  * OpenFileTool: now remembers the previously browsed directory
  * Fixed PyQt >=v4.8 compatibility issue: PyQt is less permissive with signal string syntax (PyQt\_PyObject is mandatory for passing a Python/C++ object)
  * guiqwt.fit: fixed rounding error due to slider's non-continuous behaviour
  * guiqwt.label/bugfix: text label was reset to '' when redrawn
  * guiqwt.fit: bugfixes when using logscale
  * guiqwt.io.array\_to\_imagefile/text files: format is now '%d' for integer data types
  * (Fixes [Issue 7](https://code.google.com/p/guiqwt/issues/detail?id=7)) guifit: standard fit boundary excludes rightmost value
  * guiqwt/curve.py: added workaround to avoid division by zero when clicking between curves
  * guiqwt/io.py-array\_to\_dicomfile: fixed ambiguous VR for PixelData when changing DICOM data (forced to 'OB')
  * Bugfix: recent versions of PyQt don't like the QApplication reference to be stored in modules (why is that?!)
  * Annotation/get\_infos: fixed unicode error occuring with py2exe distribution only

### Possible API compatibility issues (since v2.0.8) ###

  * Panel interface: added mandatory method 'configure\_panel' which is called just before adding the very first tool to the manager
  * baseplot: renamed guiqwt.baseplot.EnhancedQwtPlot to BasePlot

### Other changes (since v2.0.8) ###

  * Cross sections/apply lut option turned on: now clipping data between 0 and LUT\_MAX (0-1023), as it is done for displayed data
  * Added RGBImageItem
  * Scaler extension: added support for boolean arrays (e.g. for showing masks)
  * Added DeleteItemTool (add an entry "Remove" in plot item context menu)
  * Plot items/introduced notion of "private items": new item methods: (is\_private, set\_private), new plot methods: (get\_private\_items, get\_public\_items)
  * BaseImageItem.get\_closest\_indexes (+code refactoring): added argument 'corner' -> see new method 'get\_closest\_index\_rect'
  * Shapes/Annotations: code cleaning/refactoring + implemented 'get\_rect' method for EllipseShape
  * Tools deriving from InteractiveTool: added arguments 'title', 'icon' and 'tip' to customize the tool's action
  * MaskedImageItem: added ImageMaskTool to edit image's mask interactively
  * ShapeParam: added attributes "private" and "readonly"
  * interfaces.IBasePlotItem: added argument 'ctrl=None' to 'move\_local\_point\_to' (ctrl is True when 'Ctrl' button is pressed)
  * Ellipse/Circle shapes: when pressing 'Ctrl' button while resizing the shape, its center position will remain unchanged
  * guiqwt.plot: added classes CurveWindow/ImageWindow (derived from QMainWindow)
  * Added transitional package guiqwt.transitional (regroup all Qwt5 import statements)
  * BasePlot: added class attributes AXIS\_IDS, AXIS\_NAMES (removed AXES)
  * BasePlot: added methods 'set\_axis\_limits' and 'get\_axis\_limits'
  * BasePlot: added method 'set\_axis\_ticks' to set axis major tick step size or maximum number of major ticks and maximum of minor ticks
  * Cross section panels: added interface to handle the cross section curve data when updated
  * Panel widgets are now dockable
  * guiqwt.fit: code cleaning/refactoring + added FitWidget (similar to FitDialog but inherits directly from QWidget)
  * guiqwt.fit: fit params may now be changed as often as needed (the param widgets are reconstructed then)
  * guiqwt.fit: replaced set\_fit\_func and set\_fit\_params by set\_fit\_data (non sense to be setting one without the other)
  * Added vertical/horizontal cursor plot items (+ tools + cursor info label): see builder.make.vcursor, hcursor and info\_cursor
  * Cross section panel: added button "auto refresh" (enabled by default) (e.g. may be disabled for large images)
  * Added signal SIG\_MASK\_CHANGED, emitted by plot when an image mask has changed
  * guiqwt.fit.FitWidget/FitDialog: now working with no fit param
  * guiqwt.signals.SIG\_ITEM\_REMOVED is now emitted by plot when an item is removed from the item list panel (as before) or using the delete item tool (new)
  * Cross section plot: added tool 'DeleteItemTool'
  * guiqwt.builder/scaled image items (ImageItem, RGBImageItem, ...): added option 'pixel\_size' (alternative to xdata and ydata)
  * guiqwt.fit: added option 'param\_cols' to regroup N fit parameters on each row
  * SnapshotTool: added options to add images together (instead of the default replace behavior) + bugfixes
  * Renamed signal\_app.py to sift.py (Sifia -> Sift)
  * Sift: added support for image processing
  * Image levels histogram (contrast panel): replaced the 'remove first bin' feature by an intelligent Y-axis scaling
  * guifit: reorganized layout to gain some space + added option 'size\_offset' to change param label's size
  * guiqwt.plot.CurveDialog: added attribute 'button\_box' (reference to the QDialogButtonBox instance)
  * guiqwt.io: added open/save filedialog filters 'IMAGE\_LOAD\_FILTERS' (types supported by 'imagefile\_to\_array') and 'IMAGE\_SAVE\_FILTERS' (types supported by 'array\_to\_imagefile')
  * guiqwt.io: added support for "I;16B" images
  * Sift/added image operations (+ various bugfixes/enhancements): resize and rotate (90°, -90°, H/V flipping, arbritrarily rotation)
  * Sift: added run scripts + py2exe setup script + icon
  * PanelWidget: added class attributes PANEL\_TITLE and PANEL\_ICON
  * guiqwt.cross\_section.CrossSectionItem: added method 'process\_curve\_data' (called when cross section data has changed instead of calling 'set\_data' directly)
  * Tools: added 'toolbar\_id' argument to all tools deriving from CommandTool
  * setup.py: removed the hard-coded -msse2 compile flag --> added extra options --sse2 and --sse3 as a replacement
  * Added ImageStatsTool: show statistics on selected image item's rectangular area
  * builder/images: added option 'interpolation' for all image item types (default=linear)
  * builder/images: added option 'eliminate\_outliers' for some image item types (default=None)
  * Sift: added image cropping and flat-field correction features
  * Sift: added average operation + threshold/clip features to image processing menu
  * ImageMaskTool: now emits SIG\_APPLIED\_MASK\_TOOL when mask is applied from defined shapes + other API details
  * Sift: added support for DICOM metadata (shown as a dictionnary in a GUI-based editor)
  * Sift: new embedded Python console with a proxy to manipulate signal/image data directly!
