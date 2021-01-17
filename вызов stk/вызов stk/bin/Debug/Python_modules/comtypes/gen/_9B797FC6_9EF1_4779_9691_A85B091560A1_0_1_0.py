# -*- coding: mbcs -*-
typelib_path = 'D:\\STK\\bin\\AgUiCore.dll'
_lcid = 0 # change this if required
from ctypes import *
import comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0
from comtypes import GUID
from comtypes import BSTR
from ctypes import HRESULT
from ctypes.wintypes import VARIANT_BOOL
from comtypes import IUnknown
from comtypes import helpstring
from comtypes import COMMETHOD
from comtypes import dispid
from comtypes import CoClass
from comtypes.automation import VARIANT


class Library(object):
    'AGI Ui Core 11'
    name = 'AgUiCoreLib'
    _reg_typelib_ = ('{9B797FC6-9EF1-4779-9691-A85B091560A1}', 1, 0)

class IAgUiWindow(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    'Represents a window abstraction. Provides methods and properties to manipulate the position and the state of the window.'
    _iid_ = GUID('{05F59555-F74C-48B2-AAB4-1E6C58D7AEB7}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'AgEWindowState'
eWindowStateMaximized = 1
eWindowStateMinimized = 2
eWindowStateNormal = 3
AgEWindowState = c_int # enum

# values for enumeration 'AgEDockStyle'
eDockStyleIntegrated = 1
eDockStyleDockedLeft = 2
eDockStyleDockedRight = 3
eDockStyleDockedTop = 4
eDockStyleDockedBottom = 5
eDockStyleFloating = 6
AgEDockStyle = c_int # enum
class IAgUiToolbarCollection(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    "Provides methods and properties to obtain a window's toolbars."
    _iid_ = GUID('{62AA135B-4F2F-45DE-94A6-31BB0984AD28}')
    _idlflags_ = ['dual', 'nonextensible', 'oleautomation']

# values for enumeration 'AgEWindowService'
eWindowService2DWindow = 1
eWindowService3DWindow = 2
AgEWindowService = c_int # enum
IAgUiWindow._methods_ = [
    COMMETHOD(['propget', helpstring('The window caption. Can only be set within UI plugins for the non unique windows they own.')], HRESULT, 'Caption',
              ( ['out', 'retval'], POINTER(BSTR), 'pVal' )),
    COMMETHOD(['propput', helpstring('The window caption. Can only be set within UI plugins for the non unique windows they own.')], HRESULT, 'Caption',
              ( ['in'], BSTR, 'pVal' )),
    COMMETHOD([helpstring('Activates the window.')], HRESULT, 'Activate'),
    COMMETHOD(['propget', helpstring('The window state.')], HRESULT, 'WindowState',
              ( ['out', 'retval'], POINTER(AgEWindowState), 'pVal' )),
    COMMETHOD(['propput', helpstring('The window state.')], HRESULT, 'WindowState',
              ( ['in'], AgEWindowState, 'pVal' )),
    COMMETHOD([helpstring('Closes the window.')], HRESULT, 'Close'),
    COMMETHOD(['propget', helpstring('The window height.')], HRESULT, 'Height',
              ( ['out', 'retval'], POINTER(c_int), 'pVal' )),
    COMMETHOD(['propput', helpstring('The window height.')], HRESULT, 'Height',
              ( ['in'], c_int, 'pVal' )),
    COMMETHOD(['propget', helpstring('The window width.')], HRESULT, 'Width',
              ( ['out', 'retval'], POINTER(c_int), 'pVal' )),
    COMMETHOD(['propput', helpstring('The window width.')], HRESULT, 'Width',
              ( ['in'], c_int, 'pVal' )),
    COMMETHOD(['propget', helpstring('The window horizontal position.')], HRESULT, 'Left',
              ( ['out', 'retval'], POINTER(c_int), 'pVal' )),
    COMMETHOD(['propput', helpstring('The window horizontal position.')], HRESULT, 'Left',
              ( ['in'], c_int, 'pVal' )),
    COMMETHOD(['propget', helpstring('The window vertical position')], HRESULT, 'Top',
              ( ['out', 'retval'], POINTER(c_int), 'pVal' )),
    COMMETHOD(['propput', helpstring('The window vertical position')], HRESULT, 'Top',
              ( ['in'], c_int, 'pVal' )),
    COMMETHOD(['propget', helpstring('The window docking style.')], HRESULT, 'DockStyle',
              ( ['out', 'retval'], POINTER(AgEDockStyle), 'pVal' )),
    COMMETHOD(['propput', helpstring('The window docking style.')], HRESULT, 'DockStyle',
              ( ['in'], AgEDockStyle, 'pVal' )),
    COMMETHOD(['propget', helpstring('Whether to close the window when the application workbook is loaded/closed.')], HRESULT, 'NoWBClose',
              ( ['out', 'retval'], POINTER(VARIANT_BOOL), 'pVal' )),
    COMMETHOD(['propput', helpstring('Whether to close the window when the application workbook is loaded/closed.')], HRESULT, 'NoWBClose',
              ( ['in'], VARIANT_BOOL, 'pVal' )),
    COMMETHOD(['propget', helpstring("The window's pinned state.")], HRESULT, 'UnPinned',
              ( ['out', 'retval'], POINTER(VARIANT_BOOL), 'pVal' )),
    COMMETHOD(['propput', helpstring("The window's pinned state.")], HRESULT, 'UnPinned',
              ( ['in'], VARIANT_BOOL, 'pVal' )),
    COMMETHOD(['propget', helpstring('Returns whether the window supports pinning.')], HRESULT, 'SupportsPinning',
              ( ['out', 'retval'], POINTER(VARIANT_BOOL), 'pVal' )),
    COMMETHOD(['propget', helpstring("Returns the window's toolbar collection.")], HRESULT, 'Toolbars',
              ( ['out', 'retval'], POINTER(POINTER(IAgUiToolbarCollection)), 'ppVal' )),
    COMMETHOD([helpstring('Returns a service object that can be accessed at runtime. The method returns null if no service object is associated with the specified symbolic name.')], HRESULT, 'GetServiceByName',
              ( ['in'], BSTR, 'Name' ),
              ( ['out', 'retval'], POINTER(POINTER(IUnknown)), 'ppRetVal' )),
    COMMETHOD([helpstring('Returns a service object that can be accessed at runtime. The method returns null if no service object is associated with the specified service type.')], HRESULT, 'GetServiceByType',
              ( ['in'], AgEWindowService, 'ServiceType' ),
              ( ['out', 'retval'], POINTER(POINTER(IUnknown)), 'ppRetVal' )),
]
################################################################
## code template for IAgUiWindow implementation
##class IAgUiWindow_Impl(object):
##    def _get(self):
##        'The window caption. Can only be set within UI plugins for the non unique windows they own.'
##        #return pVal
##    def _set(self, pVal):
##        'The window caption. Can only be set within UI plugins for the non unique windows they own.'
##    Caption = property(_get, _set, doc = _set.__doc__)
##
##    def Activate(self):
##        'Activates the window.'
##        #return 
##
##    def _get(self):
##        'The window state.'
##        #return pVal
##    def _set(self, pVal):
##        'The window state.'
##    WindowState = property(_get, _set, doc = _set.__doc__)
##
##    def Close(self):
##        'Closes the window.'
##        #return 
##
##    def _get(self):
##        'The window height.'
##        #return pVal
##    def _set(self, pVal):
##        'The window height.'
##    Height = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'The window width.'
##        #return pVal
##    def _set(self, pVal):
##        'The window width.'
##    Width = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'The window horizontal position.'
##        #return pVal
##    def _set(self, pVal):
##        'The window horizontal position.'
##    Left = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'The window vertical position'
##        #return pVal
##    def _set(self, pVal):
##        'The window vertical position'
##    Top = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'The window docking style.'
##        #return pVal
##    def _set(self, pVal):
##        'The window docking style.'
##    DockStyle = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Whether to close the window when the application workbook is loaded/closed.'
##        #return pVal
##    def _set(self, pVal):
##        'Whether to close the window when the application workbook is loaded/closed.'
##    NoWBClose = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        "The window's pinned state."
##        #return pVal
##    def _set(self, pVal):
##        "The window's pinned state."
##    UnPinned = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def SupportsPinning(self):
##        'Returns whether the window supports pinning.'
##        #return pVal
##
##    @property
##    def Toolbars(self):
##        "Returns the window's toolbar collection."
##        #return ppVal
##
##    def GetServiceByName(self, Name):
##        'Returns a service object that can be accessed at runtime. The method returns null if no service object is associated with the specified symbolic name.'
##        #return ppRetVal
##
##    def GetServiceByType(self, ServiceType):
##        'Returns a service object that can be accessed at runtime. The method returns null if no service object is associated with the specified service type.'
##        #return ppRetVal
##

class AgUiWindow(CoClass):
    'Represents a window abstraction. Provides methods and properties to manipulate the position and the state of the window.'
    _reg_clsid_ = GUID('{180D29FA-766B-4DB5-9043-3C50B23A30AB}')
    _idlflags_ = ['hidden', 'noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{9B797FC6-9EF1-4779-9691-A85B091560A1}', 1, 0)
class _IAgUiWindow(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Represents a window abstraction. Provides methods and properties to manipulate the position and the state of the window.'
    _iid_ = GUID('{7BA21513-B774-4B68-8517-462C365641DD}')
    _idlflags_ = ['hidden', 'dual', 'nonextensible', 'oleautomation']
AgUiWindow._com_interfaces_ = [_IAgUiWindow, IAgUiWindow]

class IAgUiWindowsCollection(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    "Provides methods and properties to manage the application's windows."
    _iid_ = GUID('{4DD6FB87-C329-41A5-A359-8A9C03569635}')
    _idlflags_ = ['dual', 'nonextensible', 'oleautomation']

# values for enumeration 'AgEArrangeStyle'
eArrangeStyleCascade = 1
eArrangeStyleTiledHorizontal = 2
eArrangeStyleTiledVertical = 3
AgEArrangeStyle = c_int # enum
IAgUiWindowsCollection._methods_ = [
    COMMETHOD([dispid(0), helpstring('Retrieves a window object.'), 'propget'], HRESULT, 'Item',
              ( ['in'], VARIANT, 'IndexOrCaption' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgUiWindow)), 'pVal' )),
    COMMETHOD([dispid(1), helpstring('Returns a total number of window objects in the collection.'), 'propget'], HRESULT, 'Count',
              ( ['out', 'retval'], POINTER(c_int), 'pVal' )),
    COMMETHOD([dispid(2), helpstring('Arranges the application windows using the specified style.')], HRESULT, 'Arrange',
              ( ['in'], AgEArrangeStyle, 'ArrangeStyle' )),
    COMMETHOD([dispid(3), helpstring('Creates a new window. The bstrPluginID is a COM ProgID associated with an STK plugin.')], HRESULT, 'Add',
              ( ['in'], BSTR, 'PluginID' ),
              ( ['in'], VARIANT, 'InitData' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgUiWindow)), 'pNewWin' )),
    COMMETHOD([dispid(-4), helpstring('Enumerates the windows in the collection.'), 'propget'], HRESULT, '_NewEnum',
              ( ['out', 'retval'], POINTER(POINTER(IUnknown)), 'ppVal' )),
]
################################################################
## code template for IAgUiWindowsCollection implementation
##class IAgUiWindowsCollection_Impl(object):
##    @property
##    def Item(self, IndexOrCaption):
##        'Retrieves a window object.'
##        #return pVal
##
##    @property
##    def Count(self):
##        'Returns a total number of window objects in the collection.'
##        #return pVal
##
##    def Arrange(self, ArrangeStyle):
##        'Arranges the application windows using the specified style.'
##        #return 
##
##    def Add(self, PluginID, InitData):
##        'Creates a new window. The bstrPluginID is a COM ProgID associated with an STK plugin.'
##        #return pNewWin
##
##    @property
##    def _NewEnum(self):
##        'Enumerates the windows in the collection.'
##        #return ppVal
##

class IAgUiWindowGlobeObject(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    'Represents a 3D (Globe) window. Provides methods and properties to access the 3D window properties.'
    _iid_ = GUID('{B958EDBD-0569-4596-A253-BD90328844D0}')
    _idlflags_ = ['oleautomation']
IAgUiWindowGlobeObject._methods_ = [
    COMMETHOD(['propget', helpstring('A unique identifier associated with the window that can be used with Connect to control the 3D globe.')], HRESULT, 'SceneID',
              ( ['out', 'retval'], POINTER(c_int), 'pRetVal' )),
]
################################################################
## code template for IAgUiWindowGlobeObject implementation
##class IAgUiWindowGlobeObject_Impl(object):
##    @property
##    def SceneID(self):
##        'A unique identifier associated with the window that can be used with Connect to control the 3D globe.'
##        #return pRetVal
##

class _IAgUiWindowGlobeObject(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Represents a 3D (Globe) window. Provides methods and properties to access the 3D window properties.'
    _iid_ = GUID('{40B06213-8A37-40D3-A289-BF9D248FDD54}')
    _idlflags_ = ['hidden', 'dual', 'nonextensible', 'oleautomation']
_IAgUiWindowGlobeObject._methods_ = [
    COMMETHOD([dispid(201), helpstring('A unique identifier associated with the window that can be used with Connect to control the 3D globe.'), 'propget'], HRESULT, 'SceneID',
              ( ['out', 'retval'], POINTER(c_int), 'pRetVal' )),
]
################################################################
## code template for _IAgUiWindowGlobeObject implementation
##class _IAgUiWindowGlobeObject_Impl(object):
##    @property
##    def SceneID(self):
##        'A unique identifier associated with the window that can be used with Connect to control the 3D globe.'
##        #return pRetVal
##

class AgUiWindowGlobeObject(CoClass):
    'Provides methods and properties to manipulate the 3D globe.'
    _reg_clsid_ = GUID('{268F62AD-2AFA-4E5E-8B59-B3DA4A5D3E79}')
    _idlflags_ = ['hidden', 'noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{9B797FC6-9EF1-4779-9691-A85B091560A1}', 1, 0)
AgUiWindowGlobeObject._com_interfaces_ = [_IAgUiWindowGlobeObject, IAgUiWindowGlobeObject]

class IAgUiToolbar(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    'Provides methods and properties to control a toolbar.'
    _iid_ = GUID('{69C72C16-36F2-42D4-A183-6879BB5B8070}')
    _idlflags_ = ['oleautomation']
IAgUiToolbarCollection._methods_ = [
    COMMETHOD([dispid(0), helpstring('Retrieves a toolbar object.'), 'propget'], HRESULT, 'Item',
              ( ['in'], VARIANT, 'IndexOrCaption' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgUiToolbar)), 'pVal' )),
    COMMETHOD([dispid(1), helpstring('Returns a total number of toolbars in the collection.'), 'propget'], HRESULT, 'Count',
              ( ['out', 'retval'], POINTER(c_int), 'pVal' )),
    COMMETHOD([dispid(-4), helpstring('Enumerates the toolbars in the collection.'), 'propget'], HRESULT, '_NewEnum',
              ( ['out', 'retval'], POINTER(POINTER(IUnknown)), 'ppVal' )),
    COMMETHOD([dispid(2), helpstring('Returns a toolbar object with the specified toolbar identifier. The identifier is a unique number assigned to a toolbar object.')], HRESULT, 'GetToolbarByID',
              ( ['in'], c_int, 'ID' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgUiToolbar)), 'pVal' )),
]
################################################################
## code template for IAgUiToolbarCollection implementation
##class IAgUiToolbarCollection_Impl(object):
##    @property
##    def Item(self, IndexOrCaption):
##        'Retrieves a toolbar object.'
##        #return pVal
##
##    @property
##    def Count(self):
##        'Returns a total number of toolbars in the collection.'
##        #return pVal
##
##    @property
##    def _NewEnum(self):
##        'Enumerates the toolbars in the collection.'
##        #return ppVal
##
##    def GetToolbarByID(self, ID):
##        'Returns a toolbar object with the specified toolbar identifier. The identifier is a unique number assigned to a toolbar object.'
##        #return pVal
##

class AgUiToolbar(CoClass):
    'Represents a toolbar abstraction. Provides methods and properties to manipulate the position and the state of the toolbar.'
    _reg_clsid_ = GUID('{89FD3D93-3E4B-47C5-9A35-A425BC684E40}')
    _idlflags_ = ['hidden', 'noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{9B797FC6-9EF1-4779-9691-A85B091560A1}', 1, 0)
class _IAgUiToolbar(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Provides methods and properties to control a toolbar.'
    _iid_ = GUID('{0859D6D9-472D-44FB-80B6-0A0CC5119E91}')
    _idlflags_ = ['hidden', 'dual', 'nonextensible', 'oleautomation']
AgUiToolbar._com_interfaces_ = [_IAgUiToolbar, IAgUiToolbar]


# values for enumeration 'AgEFloatState'
eFloatStateFloated = 1
eFloatStateDocked = 2
AgEFloatState = c_int # enum
_IAgUiToolbar._methods_ = [
    COMMETHOD([dispid(1), helpstring('The toolbar identity.'), 'propget'], HRESULT, 'ID',
              ( ['out', 'retval'], POINTER(c_int), 'pVal' )),
    COMMETHOD([dispid(2), helpstring('The toolbar caption.'), 'propget'], HRESULT, 'Caption',
              ( ['out', 'retval'], POINTER(BSTR), 'pVal' )),
    COMMETHOD([dispid(3), helpstring('The toolbar visibility.'), 'propget'], HRESULT, 'Visible',
              ( ['out', 'retval'], POINTER(VARIANT_BOOL), 'pVal' )),
    COMMETHOD([dispid(3), helpstring('The toolbar visibility.'), 'propput'], HRESULT, 'Visible',
              ( ['in'], VARIANT_BOOL, 'pVal' )),
    COMMETHOD([dispid(4), helpstring('The toolbar float state.'), 'propget'], HRESULT, 'FloatState',
              ( ['out', 'retval'], POINTER(AgEFloatState), 'pVal' )),
    COMMETHOD([dispid(4), helpstring('The toolbar float state.'), 'propput'], HRESULT, 'FloatState',
              ( ['in'], AgEFloatState, 'pVal' )),
]
################################################################
## code template for _IAgUiToolbar implementation
##class _IAgUiToolbar_Impl(object):
##    @property
##    def ID(self):
##        'The toolbar identity.'
##        #return pVal
##
##    @property
##    def Caption(self):
##        'The toolbar caption.'
##        #return pVal
##
##    def _get(self):
##        'The toolbar visibility.'
##        #return pVal
##    def _set(self, pVal):
##        'The toolbar visibility.'
##    Visible = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'The toolbar float state.'
##        #return pVal
##    def _set(self, pVal):
##        'The toolbar float state.'
##    FloatState = property(_get, _set, doc = _set.__doc__)
##

class AgUiWindowsCollection(CoClass):
    'Provides methods and properties to manage the windows.'
    _reg_clsid_ = GUID('{15DD57C3-4512-4711-B7C5-DCD9B9EB8809}')
    _idlflags_ = ['hidden', 'noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{9B797FC6-9EF1-4779-9691-A85B091560A1}', 1, 0)
AgUiWindowsCollection._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IAgUiWindowsCollection]

class AgUiToolbarCollection(CoClass):
    'Provides methods and properties to manage the toolbars.'
    _reg_clsid_ = GUID('{F7239EFC-9609-41BF-AB06-E17574F98F60}')
    _idlflags_ = ['hidden', 'noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{9B797FC6-9EF1-4779-9691-A85B091560A1}', 1, 0)
AgUiToolbarCollection._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IAgUiToolbarCollection]

class AgUiWindowMapObject(CoClass):
    'Provides methods and properties to manipulate the 2D map.'
    _reg_clsid_ = GUID('{52968DE1-9E70-44E9-ADFB-A47FF2E0046E}')
    _idlflags_ = ['hidden', 'noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{9B797FC6-9EF1-4779-9691-A85B091560A1}', 1, 0)
class _IAgUiWindowMapObject(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Represents a 2D (Map) window. Provides methods and properties to access the 2D window properties.'
    _iid_ = GUID('{5FD247F7-F520-464A-9937-028D8384FBC3}')
    _idlflags_ = ['hidden', 'dual', 'nonextensible', 'oleautomation']
class IAgUiWindowMapObject(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    'Represents a 2D (Map) window. Provides methods and properties to access the 2D window properties.'
    _iid_ = GUID('{A94C0929-7448-4E9E-BEB8-8F7A8F252D0D}')
    _idlflags_ = ['oleautomation']
AgUiWindowMapObject._com_interfaces_ = [_IAgUiWindowMapObject, IAgUiWindowMapObject]

_IAgUiWindowMapObject._methods_ = [
    COMMETHOD([dispid(201), helpstring('A unique identifier associated with the window that can be used with Connect to control the 2D map.'), 'propget'], HRESULT, 'MapID',
              ( ['out', 'retval'], POINTER(c_int), 'pRetVal' )),
]
################################################################
## code template for _IAgUiWindowMapObject implementation
##class _IAgUiWindowMapObject_Impl(object):
##    @property
##    def MapID(self):
##        'A unique identifier associated with the window that can be used with Connect to control the 2D map.'
##        #return pRetVal
##

IAgUiWindowMapObject._methods_ = [
    COMMETHOD(['propget', helpstring('A unique identifier associated with the window that can be used with Connect to control the 2D map.')], HRESULT, 'MapID',
              ( ['out', 'retval'], POINTER(c_int), 'pRetVal' )),
]
################################################################
## code template for IAgUiWindowMapObject implementation
##class IAgUiWindowMapObject_Impl(object):
##    @property
##    def MapID(self):
##        'A unique identifier associated with the window that can be used with Connect to control the 2D map.'
##        #return pRetVal
##

_IAgUiWindow._methods_ = [
    COMMETHOD([dispid(201), helpstring('The window caption. Can only be set within UI plugins for the non unique windows they own.'), 'propget'], HRESULT, 'Caption',
              ( ['out', 'retval'], POINTER(BSTR), 'pVal' )),
    COMMETHOD([dispid(201), helpstring('The window caption. Can only be set within UI plugins for the non unique windows they own.'), 'propput'], HRESULT, 'Caption',
              ( ['in'], BSTR, 'pVal' )),
    COMMETHOD([dispid(202), helpstring('Activates the window.')], HRESULT, 'Activate'),
    COMMETHOD([dispid(203), helpstring('The window state.'), 'propget'], HRESULT, 'WindowState',
              ( ['out', 'retval'], POINTER(AgEWindowState), 'pVal' )),
    COMMETHOD([dispid(203), helpstring('The window state.'), 'propput'], HRESULT, 'WindowState',
              ( ['in'], AgEWindowState, 'pVal' )),
    COMMETHOD([dispid(204), helpstring('Closes the window.')], HRESULT, 'Close'),
    COMMETHOD([dispid(205), helpstring('The window height.'), 'propget'], HRESULT, 'Height',
              ( ['out', 'retval'], POINTER(c_int), 'pVal' )),
    COMMETHOD([dispid(205), helpstring('The window height.'), 'propput'], HRESULT, 'Height',
              ( ['in'], c_int, 'pVal' )),
    COMMETHOD([dispid(206), helpstring('The window width.'), 'propget'], HRESULT, 'Width',
              ( ['out', 'retval'], POINTER(c_int), 'pVal' )),
    COMMETHOD([dispid(206), helpstring('The window width.'), 'propput'], HRESULT, 'Width',
              ( ['in'], c_int, 'pVal' )),
    COMMETHOD([dispid(207), helpstring('The window horizontal position.'), 'propget'], HRESULT, 'Left',
              ( ['out', 'retval'], POINTER(c_int), 'pVal' )),
    COMMETHOD([dispid(207), helpstring('The window horizontal position.'), 'propput'], HRESULT, 'Left',
              ( ['in'], c_int, 'pVal' )),
    COMMETHOD([dispid(208), helpstring('The window vertical position.'), 'propget'], HRESULT, 'Top',
              ( ['out', 'retval'], POINTER(c_int), 'pVal' )),
    COMMETHOD([dispid(208), helpstring('The window vertical position.'), 'propput'], HRESULT, 'Top',
              ( ['in'], c_int, 'pVal' )),
    COMMETHOD([dispid(209), helpstring('The window docking style.'), 'propget'], HRESULT, 'DockStyle',
              ( ['out', 'retval'], POINTER(AgEDockStyle), 'pVal' )),
    COMMETHOD([dispid(209), helpstring('The window docking style.'), 'propput'], HRESULT, 'DockStyle',
              ( ['in'], AgEDockStyle, 'pVal' )),
    COMMETHOD([dispid(210), helpstring('Whether to close the window when the application workbook is loaded/closed.'), 'propget'], HRESULT, 'NoWBClose',
              ( ['out', 'retval'], POINTER(VARIANT_BOOL), 'pVal' )),
    COMMETHOD([dispid(210), helpstring('Whether to close the window when the application workbook is loaded/closed.'), 'propput'], HRESULT, 'NoWBClose',
              ( ['in'], VARIANT_BOOL, 'pVal' )),
    COMMETHOD([dispid(211), helpstring("The window's pinned state."), 'propget'], HRESULT, 'UnPinned',
              ( ['out', 'retval'], POINTER(VARIANT_BOOL), 'pVal' )),
    COMMETHOD([dispid(211), helpstring("The window's pinned state."), 'propput'], HRESULT, 'UnPinned',
              ( ['in'], VARIANT_BOOL, 'pVal' )),
    COMMETHOD([dispid(212), helpstring('Returns whether the window supports pinning.'), 'propget'], HRESULT, 'SupportsPinning',
              ( ['out', 'retval'], POINTER(VARIANT_BOOL), 'pVal' )),
    COMMETHOD([dispid(213), helpstring("Returns the window's toolbar collection."), 'propget'], HRESULT, 'Toolbars',
              ( ['out', 'retval'], POINTER(POINTER(IAgUiToolbarCollection)), 'ppVal' )),
    COMMETHOD([dispid(214), helpstring('Returns a service object that can be accessed at runtime. The method returns null if no service object is associated with the specified symbolic name.')], HRESULT, 'GetServiceByName',
              ( ['in'], BSTR, 'Name' ),
              ( ['out', 'retval'], POINTER(POINTER(IUnknown)), 'ppRetVal' )),
    COMMETHOD([dispid(215), helpstring('Returns a service object that can be accessed at runtime. The method returns null if no service object is associated with the specified service type.')], HRESULT, 'GetServiceByType',
              ( ['in'], AgEWindowService, 'ServiceType' ),
              ( ['out', 'retval'], POINTER(POINTER(IUnknown)), 'ppRetVal' )),
]
################################################################
## code template for _IAgUiWindow implementation
##class _IAgUiWindow_Impl(object):
##    def _get(self):
##        'The window caption. Can only be set within UI plugins for the non unique windows they own.'
##        #return pVal
##    def _set(self, pVal):
##        'The window caption. Can only be set within UI plugins for the non unique windows they own.'
##    Caption = property(_get, _set, doc = _set.__doc__)
##
##    def Activate(self):
##        'Activates the window.'
##        #return 
##
##    def _get(self):
##        'The window state.'
##        #return pVal
##    def _set(self, pVal):
##        'The window state.'
##    WindowState = property(_get, _set, doc = _set.__doc__)
##
##    def Close(self):
##        'Closes the window.'
##        #return 
##
##    def _get(self):
##        'The window height.'
##        #return pVal
##    def _set(self, pVal):
##        'The window height.'
##    Height = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'The window width.'
##        #return pVal
##    def _set(self, pVal):
##        'The window width.'
##    Width = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'The window horizontal position.'
##        #return pVal
##    def _set(self, pVal):
##        'The window horizontal position.'
##    Left = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'The window vertical position.'
##        #return pVal
##    def _set(self, pVal):
##        'The window vertical position.'
##    Top = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'The window docking style.'
##        #return pVal
##    def _set(self, pVal):
##        'The window docking style.'
##    DockStyle = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Whether to close the window when the application workbook is loaded/closed.'
##        #return pVal
##    def _set(self, pVal):
##        'Whether to close the window when the application workbook is loaded/closed.'
##    NoWBClose = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        "The window's pinned state."
##        #return pVal
##    def _set(self, pVal):
##        "The window's pinned state."
##    UnPinned = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def SupportsPinning(self):
##        'Returns whether the window supports pinning.'
##        #return pVal
##
##    @property
##    def Toolbars(self):
##        "Returns the window's toolbar collection."
##        #return ppVal
##
##    def GetServiceByName(self, Name):
##        'Returns a service object that can be accessed at runtime. The method returns null if no service object is associated with the specified symbolic name.'
##        #return ppRetVal
##
##    def GetServiceByType(self, ServiceType):
##        'Returns a service object that can be accessed at runtime. The method returns null if no service object is associated with the specified service type.'
##        #return ppRetVal
##

IAgUiToolbar._methods_ = [
    COMMETHOD(['propget', helpstring('The identity.')], HRESULT, 'ID',
              ( ['out', 'retval'], POINTER(c_int), 'pVal' )),
    COMMETHOD(['propget', helpstring('The caption.')], HRESULT, 'Caption',
              ( ['out', 'retval'], POINTER(BSTR), 'pVal' )),
    COMMETHOD(['propget', helpstring('The visibility.')], HRESULT, 'Visible',
              ( ['out', 'retval'], POINTER(VARIANT_BOOL), 'pVal' )),
    COMMETHOD(['propput', helpstring('The visibility.')], HRESULT, 'Visible',
              ( ['in'], VARIANT_BOOL, 'pVal' )),
    COMMETHOD(['propget', helpstring('The float state.')], HRESULT, 'FloatState',
              ( ['out', 'retval'], POINTER(AgEFloatState), 'pVal' )),
    COMMETHOD(['propput', helpstring('The float state.')], HRESULT, 'FloatState',
              ( ['in'], AgEFloatState, 'pVal' )),
]
################################################################
## code template for IAgUiToolbar implementation
##class IAgUiToolbar_Impl(object):
##    @property
##    def ID(self):
##        'The identity.'
##        #return pVal
##
##    @property
##    def Caption(self):
##        'The caption.'
##        #return pVal
##
##    def _get(self):
##        'The visibility.'
##        #return pVal
##    def _set(self, pVal):
##        'The visibility.'
##    Visible = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'The float state.'
##        #return pVal
##    def _set(self, pVal):
##        'The float state.'
##    FloatState = property(_get, _set, doc = _set.__doc__)
##

__all__ = [ '_IAgUiWindowMapObject', 'IAgUiWindowGlobeObject',
           '_IAgUiWindowGlobeObject', '_IAgUiWindow',
           'eWindowStateMinimized', 'eDockStyleFloating',
           'AgUiToolbar', 'eWindowStateNormal', 'IAgUiToolbar',
           'AgEFloatState', 'AgUiWindowMapObject',
           'IAgUiWindowMapObject', 'AgUiWindow',
           'eDockStyleDockedTop', 'IAgUiWindowsCollection',
           'eFloatStateDocked', 'IAgUiToolbarCollection',
           'AgEArrangeStyle', 'eDockStyleDockedRight',
           'AgEWindowService', 'AgUiWindowsCollection',
           'eDockStyleIntegrated', 'AgUiWindowGlobeObject',
           '_IAgUiToolbar', 'AgEWindowState', 'eArrangeStyleCascade',
           'eFloatStateFloated', 'eWindowService3DWindow',
           'eArrangeStyleTiledVertical', 'eDockStyleDockedLeft',
           'eArrangeStyleTiledHorizontal', 'eDockStyleDockedBottom',
           'IAgUiWindow', 'eWindowStateMaximized', 'AgEDockStyle',
           'eWindowService2DWindow', 'AgUiToolbarCollection']
from comtypes import _check_version; _check_version('', 1491698328.000000)
