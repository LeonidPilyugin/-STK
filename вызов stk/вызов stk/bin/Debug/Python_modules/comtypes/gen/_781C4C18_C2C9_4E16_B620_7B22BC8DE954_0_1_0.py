# -*- coding: mbcs -*-
typelib_path = 'D:\\STK\\bin\\AgUiApplication.tlb'
_lcid = 0 # change this if required
from ctypes import *
from comtypes import GUID
from comtypes import CoClass
import comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0
from ctypes import HRESULT
from comtypes import BSTR
from comtypes import helpstring
from comtypes import COMMETHOD
from comtypes import dispid
from comtypes.automation import IDispatch
from ctypes.wintypes import VARIANT_BOOL
import comtypes.gen._9B797FC6_9EF1_4779_9691_A85B091560A1_0_1_0
from comtypes import IUnknown
from comtypes import DISPMETHOD, DISPPROPERTY, helpstring
from comtypes.automation import VARIANT


class AgUiFileOpenExtCollection(CoClass):
    'Multiple file open collection.'
    _reg_clsid_ = GUID('{C9F806FD-174F-4DD0-92D1-19C7A2EC238B}')
    _idlflags_ = ['hidden', 'noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{781C4C18-C2C9-4E16-B620-7B22BC8DE954}', 1, 0)
class IAgUiFileOpenExtCollection(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Multiple file open collection.'
    _iid_ = GUID('{898D3614-D725-4B7B-BE49-E1DD888BEFB1}')
    _idlflags_ = ['dual', 'nonextensible', 'oleautomation']
AgUiFileOpenExtCollection._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IAgUiFileOpenExtCollection]

class _IAgUiFileOpenExt(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Access to file open dialog that allows multiple file specifications.'
    _iid_ = GUID('{BEEA5B8C-EC39-49BF-BD90-0FED41ACC952}')
    _idlflags_ = ['hidden', 'dual', 'nonextensible', 'oleautomation']
_IAgUiFileOpenExt._methods_ = [
    COMMETHOD([dispid(201), helpstring('Gets/sets the mulitple file open collection.'), 'propget'], HRESULT, 'FileName',
              ( ['out', 'retval'], POINTER(POINTER(IAgUiFileOpenExtCollection)), 'pVal' )),
    COMMETHOD([dispid(201), helpstring('Gets/sets the mulitple file open collection.'), 'propput'], HRESULT, 'FileName',
              ( ['in'], POINTER(IAgUiFileOpenExtCollection), 'pVal' )),
    COMMETHOD([dispid(202), helpstring('Gets/sets the file open dialog filter description.'), 'propget'], HRESULT, 'FilterDescription',
              ( ['out', 'retval'], POINTER(BSTR), 'pVal' )),
    COMMETHOD([dispid(202), helpstring('Gets/sets the file open dialog filter description.'), 'propput'], HRESULT, 'FilterDescription',
              ( ['in'], BSTR, 'pVal' )),
    COMMETHOD([dispid(203), helpstring('Gets/sets the file open dialog filter pattern.'), 'propget'], HRESULT, 'FilterPattern',
              ( ['out', 'retval'], POINTER(BSTR), 'pVal' )),
    COMMETHOD([dispid(203), helpstring('Gets/sets the file open dialog filter pattern.'), 'propput'], HRESULT, 'FilterPattern',
              ( ['in'], BSTR, 'pVal' )),
]
################################################################
## code template for _IAgUiFileOpenExt implementation
##class _IAgUiFileOpenExt_Impl(object):
##    def _get(self):
##        'Gets/sets the mulitple file open collection.'
##        #return pVal
##    def _set(self, pVal):
##        'Gets/sets the mulitple file open collection.'
##    FileName = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Gets/sets the file open dialog filter description.'
##        #return pVal
##    def _set(self, pVal):
##        'Gets/sets the file open dialog filter description.'
##    FilterDescription = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Gets/sets the file open dialog filter pattern.'
##        #return pVal
##    def _set(self, pVal):
##        'Gets/sets the file open dialog filter pattern.'
##    FilterPattern = property(_get, _set, doc = _set.__doc__)
##

class AgUiFileOpenExt(CoClass):
    'Access to file open dialog that allows multiple file specifications.'
    _reg_clsid_ = GUID('{EBFB7813-352C-43AD-AE7D-E18F23E77063}')
    _idlflags_ = ['hidden', 'noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{781C4C18-C2C9-4E16-B620-7B22BC8DE954}', 1, 0)
class IAgUiFileOpenExt(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    'Access to file open dialog that allows multiple file specifications.'
    _iid_ = GUID('{E9BCB21B-5D69-452B-9422-A78836AEDB95}')
    _idlflags_ = ['oleautomation']
AgUiFileOpenExt._com_interfaces_ = [_IAgUiFileOpenExt, IAgUiFileOpenExt]

class _IAgUiApplication(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Represents a root of the Application Model.'
    _iid_ = GUID('{8A71C052-B884-4D17-9B4C-D3CE26960FA4}')
    _idlflags_ = ['hidden', 'dual', 'nonextensible', 'oleautomation']
class IAgMRUCollection(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Provides information about most recently used (MRU) list.'
    _iid_ = GUID('{184F8527-EE7E-4D83-8387-4A2866CC734F}')
    _idlflags_ = ['dual', 'nonextensible', 'oleautomation']

# values for enumeration 'AgEOpenLogFileMode'
eOpenLogFileForWriting = 2
eOpenLogFileForAppending = 8
AgEOpenLogFileMode = c_int # enum

# values for enumeration 'AgEUiLogMsgType'
eUiLogMsgDebug = 0
eUiLogMsgInfo = 1
eUiLogMsgForceInfo = 2
eUiLogMsgWarning = 3
eUiLogMsgError = 4
eUiLogMsgAlarm = 4
AgEUiLogMsgType = c_int # enum
class IAgUiApplication(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    'IAgUiApplication represents a root of the Application Model.'
    _iid_ = GUID('{9A36E9B8-C995-40E4-8393-84AF79C20C3C}')
    _idlflags_ = ['oleautomation']
_IAgUiApplication._methods_ = [
    COMMETHOD([dispid(201), helpstring('Loads a personality by its name.')], HRESULT, 'LoadPersonality',
              ( ['in'], BSTR, 'PersName' )),
    COMMETHOD([dispid(202), helpstring('Returns a reference to the currently loaded personality.'), 'propget'], HRESULT, 'Personality',
              ( ['out', 'retval'], POINTER(POINTER(IDispatch)), 'pVal' )),
    COMMETHOD([dispid(203), helpstring('Gets/sets whether the main window is visible.'), 'propget'], HRESULT, 'Visible',
              ( ['out', 'retval'], POINTER(VARIANT_BOOL), 'pVal' )),
    COMMETHOD([dispid(203), helpstring('Gets/sets whether the main window is visible.'), 'propput'], HRESULT, 'Visible',
              ( ['in'], VARIANT_BOOL, 'pVal' )),
    COMMETHOD([dispid(204), helpstring('Gets/sets whether the application is user controlled.'), 'propget'], HRESULT, 'UserControl',
              ( ['out', 'retval'], POINTER(VARIANT_BOOL), 'pVal' )),
    COMMETHOD([dispid(204), helpstring('Gets/sets whether the application is user controlled.'), 'propput'], HRESULT, 'UserControl',
              ( ['in'], VARIANT_BOOL, 'pVal' )),
    COMMETHOD([dispid(205), helpstring('Returns a collection of windows.'), 'propget'], HRESULT, 'Windows',
              ( ['out', 'retval'], POINTER(POINTER(comtypes.gen._9B797FC6_9EF1_4779_9691_A85B091560A1_0_1_0.IAgUiWindowsCollection)), 'pVal' )),
    COMMETHOD([dispid(206), helpstring('Gets/sets a height of the main window.'), 'propget'], HRESULT, 'Height',
              ( ['out', 'retval'], POINTER(c_int), 'pVal' )),
    COMMETHOD([dispid(206), helpstring('Gets/sets a height of the main window.'), 'propput'], HRESULT, 'Height',
              ( ['in'], c_int, 'pVal' )),
    COMMETHOD([dispid(207), helpstring('Gets/sets a width of the main window.'), 'propget'], HRESULT, 'Width',
              ( ['out', 'retval'], POINTER(c_int), 'pVal' )),
    COMMETHOD([dispid(207), helpstring('Gets/sets a width of the main window.'), 'propput'], HRESULT, 'Width',
              ( ['in'], c_int, 'pVal' )),
    COMMETHOD([dispid(208), helpstring('Gets/sets a vertical coordinate of the main window.'), 'propget'], HRESULT, 'Left',
              ( ['out', 'retval'], POINTER(c_int), 'pVal' )),
    COMMETHOD([dispid(208), helpstring('Gets/sets a vertical coordinate of the main window.'), 'propput'], HRESULT, 'Left',
              ( ['in'], c_int, 'pVal' )),
    COMMETHOD([dispid(209), helpstring('Gets/sets a horizontal coordinate of the main window.'), 'propget'], HRESULT, 'Top',
              ( ['out', 'retval'], POINTER(c_int), 'pVal' )),
    COMMETHOD([dispid(209), helpstring('Gets/sets a horizontal coordinate of the main window.'), 'propput'], HRESULT, 'Top',
              ( ['in'], c_int, 'pVal' )),
    COMMETHOD([dispid(210), helpstring('Gets/sets the state of the main window.'), 'propget'], HRESULT, 'WindowState',
              ( ['out', 'retval'], POINTER(comtypes.gen._9B797FC6_9EF1_4779_9691_A85B091560A1_0_1_0.AgEWindowState), 'pVal' )),
    COMMETHOD([dispid(210), helpstring('Gets/sets the state of the main window.'), 'propput'], HRESULT, 'WindowState',
              ( ['in'], comtypes.gen._9B797FC6_9EF1_4779_9691_A85B091560A1_0_1_0.AgEWindowState, 'pVal' )),
    COMMETHOD([dispid(211), helpstring("Activates the application's main window.")], HRESULT, 'Activate'),
    COMMETHOD([dispid(212), helpstring('Returns a collection most recently used files.'), 'propget'], HRESULT, 'MRUList',
              ( ['out', 'retval'], POINTER(POINTER(IAgMRUCollection)), 'ppVal' )),
    COMMETHOD([dispid(213), helpstring('Brings up a common File Open dialog and returns the file name selected by the user. If the user canceled, returns an empty file name.')], HRESULT, 'FileOpenDialog',
              ( ['in'], BSTR, 'DefaultExt' ),
              ( ['in'], BSTR, 'Filter' ),
              ( ['in'], BSTR, 'InitialDir' ),
              ( ['out', 'retval'], POINTER(BSTR), 'pFileName' )),
    COMMETHOD([dispid(214), helpstring('Returns the complete path to the application, excluding the final separator and name of the application. Read-only String.'), 'propget'], HRESULT, 'Path',
              ( ['out', 'retval'], POINTER(BSTR), 'pVal' )),
    COMMETHOD([dispid(215), helpstring('Only works from local HTML pages and scripts')], HRESULT, 'CreateObject',
              ( ['in'], BSTR, 'ProgID' ),
              ( ['in', 'optional'], BSTR, 'RemoteServer', '' ),
              ( ['out', 'retval'], POINTER(POINTER(IUnknown)), 'ppObject' )),
    COMMETHOD([dispid(216), helpstring('Brings up a common File SaveAs dialog and returns the file name selected by the user. If the user canceled, returns an empty file name.')], HRESULT, 'FileSaveAsDialog',
              ( ['in'], BSTR, 'DefaultExt' ),
              ( ['in'], BSTR, 'Filter' ),
              ( ['in'], BSTR, 'InitialDir' ),
              ( ['out', 'retval'], POINTER(BSTR), 'pFileName' )),
    COMMETHOD([dispid(217), helpstring('Shuts down the application.')], HRESULT, 'Quit'),
    COMMETHOD([dispid(218), helpstring('Brings up a standard File Open Dialog and returns an object representing the selected file.')], HRESULT, 'FileOpenDialogExt',
              ( ['in'], VARIANT_BOOL, 'AllowMultiSelect' ),
              ( ['in'], BSTR, 'DefaultExt' ),
              ( ['in'], BSTR, 'Filter' ),
              ( ['in'], BSTR, 'InitialDir' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgUiFileOpenExt)), 'ppObject' )),
    COMMETHOD([dispid(219), helpstring('Returns an HWND handle associated with the application main window.'), 'propget'], HRESULT, 'HWND',
              ( ['out', 'retval'], POINTER(c_int), 'pVal' )),
    COMMETHOD([dispid(220), helpstring('Brings up the Directory Picker Dialog and returns a selected directory name.')], HRESULT, 'DirectoryPickerDialog',
              ( ['in'], BSTR, 'Title' ),
              ( ['in'], BSTR, 'InitialDir' ),
              ( ['out', 'retval'], POINTER(BSTR), 'pDirName' )),
    COMMETHOD([dispid(222), helpstring('Gets/Sets message-pending delay for server busy dialog (in milliseconds )'), 'propget'], HRESULT, 'MessagePendingDelay',
              ( ['out', 'retval'], POINTER(c_int), 'pVal' )),
    COMMETHOD([dispid(222), helpstring('Gets/Sets message-pending delay for server busy dialog (in milliseconds )'), 'propput'], HRESULT, 'MessagePendingDelay',
              ( ['in'], c_int, 'pVal' )),
    COMMETHOD([dispid(223), helpstring('Returns an new instance of the root object of the STK Object Model'), 'propget'], HRESULT, 'Personality2',
              ( ['out', 'retval'], POINTER(POINTER(IDispatch)), 'ppRetVal' )),
    COMMETHOD([dispid(224), helpstring('Specifies the current log file to be written to.')], HRESULT, 'OpenLogFile',
              ( ['in'], BSTR, 'LogFileName' ),
              ( ['in'], AgEOpenLogFileMode, 'LogFileMode' ),
              ( ['out', 'retval'], POINTER(VARIANT_BOOL), 'pVal' )),
    COMMETHOD([dispid(225), helpstring('Logs the Message specified.')], HRESULT, 'LogMsg',
              ( ['in'], AgEUiLogMsgType, 'MsgType' ),
              ( ['in'], BSTR, 'Msg' )),
    COMMETHOD([dispid(226), helpstring('Gets the current log files full path.'), 'propget'], HRESULT, 'LogFile',
              ( ['out', 'retval'], POINTER(BSTR), 'pLogFilePath' )),
    COMMETHOD([dispid(227), helpstring('Set to true to display certain alerts and messages. Otherwise false. The default value is True.'), 'propget'], HRESULT, 'DisplayAlerts',
              ( ['out', 'retval'], POINTER(VARIANT_BOOL), 'pRetVal' )),
    COMMETHOD([dispid(227), helpstring('Set to true to display certain alerts and messages. Otherwise false. The default value is True.'), 'propput'], HRESULT, 'DisplayAlerts',
              ( ['in'], VARIANT_BOOL, 'pRetVal' )),
    COMMETHOD([dispid(228), helpstring('Create a new instance of the application model root object.')], HRESULT, 'CreateApplication',
              ( ['out', 'retval'], POINTER(POINTER(IAgUiApplication)), 'ppRetVal' )),
    COMMETHOD([dispid(230), helpstring('Provide object model root for authorized business partners.')], HRESULT, 'GrantPartnerAccess',
              ( ['in'], BSTR, 'vendor' ),
              ( ['in'], BSTR, 'product' ),
              ( ['in'], BSTR, 'key' ),
              ( ['out', 'retval'], POINTER(POINTER(IDispatch)), 'ppRetVal' )),
    COMMETHOD([dispid(231), helpstring('Gets process id for the current instance.'), 'propget'], HRESULT, 'ProcessID',
              ( ['out', 'retval'], POINTER(c_int), 'pVal' )),
]
################################################################
## code template for _IAgUiApplication implementation
##class _IAgUiApplication_Impl(object):
##    def LoadPersonality(self, PersName):
##        'Loads a personality by its name.'
##        #return 
##
##    @property
##    def Personality(self):
##        'Returns a reference to the currently loaded personality.'
##        #return pVal
##
##    def _get(self):
##        'Gets/sets whether the main window is visible.'
##        #return pVal
##    def _set(self, pVal):
##        'Gets/sets whether the main window is visible.'
##    Visible = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Gets/sets whether the application is user controlled.'
##        #return pVal
##    def _set(self, pVal):
##        'Gets/sets whether the application is user controlled.'
##    UserControl = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Windows(self):
##        'Returns a collection of windows.'
##        #return pVal
##
##    def _get(self):
##        'Gets/sets a height of the main window.'
##        #return pVal
##    def _set(self, pVal):
##        'Gets/sets a height of the main window.'
##    Height = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Gets/sets a width of the main window.'
##        #return pVal
##    def _set(self, pVal):
##        'Gets/sets a width of the main window.'
##    Width = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Gets/sets a vertical coordinate of the main window.'
##        #return pVal
##    def _set(self, pVal):
##        'Gets/sets a vertical coordinate of the main window.'
##    Left = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Gets/sets a horizontal coordinate of the main window.'
##        #return pVal
##    def _set(self, pVal):
##        'Gets/sets a horizontal coordinate of the main window.'
##    Top = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Gets/sets the state of the main window.'
##        #return pVal
##    def _set(self, pVal):
##        'Gets/sets the state of the main window.'
##    WindowState = property(_get, _set, doc = _set.__doc__)
##
##    def Activate(self):
##        "Activates the application's main window."
##        #return 
##
##    @property
##    def MRUList(self):
##        'Returns a collection most recently used files.'
##        #return ppVal
##
##    def FileOpenDialog(self, DefaultExt, Filter, InitialDir):
##        'Brings up a common File Open dialog and returns the file name selected by the user. If the user canceled, returns an empty file name.'
##        #return pFileName
##
##    @property
##    def Path(self):
##        'Returns the complete path to the application, excluding the final separator and name of the application. Read-only String.'
##        #return pVal
##
##    def CreateObject(self, ProgID, RemoteServer):
##        'Only works from local HTML pages and scripts'
##        #return ppObject
##
##    def FileSaveAsDialog(self, DefaultExt, Filter, InitialDir):
##        'Brings up a common File SaveAs dialog and returns the file name selected by the user. If the user canceled, returns an empty file name.'
##        #return pFileName
##
##    def Quit(self):
##        'Shuts down the application.'
##        #return 
##
##    def FileOpenDialogExt(self, AllowMultiSelect, DefaultExt, Filter, InitialDir):
##        'Brings up a standard File Open Dialog and returns an object representing the selected file.'
##        #return ppObject
##
##    @property
##    def HWND(self):
##        'Returns an HWND handle associated with the application main window.'
##        #return pVal
##
##    def DirectoryPickerDialog(self, Title, InitialDir):
##        'Brings up the Directory Picker Dialog and returns a selected directory name.'
##        #return pDirName
##
##    def _get(self):
##        'Gets/Sets message-pending delay for server busy dialog (in milliseconds )'
##        #return pVal
##    def _set(self, pVal):
##        'Gets/Sets message-pending delay for server busy dialog (in milliseconds )'
##    MessagePendingDelay = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Personality2(self):
##        'Returns an new instance of the root object of the STK Object Model'
##        #return ppRetVal
##
##    def OpenLogFile(self, LogFileName, LogFileMode):
##        'Specifies the current log file to be written to.'
##        #return pVal
##
##    def LogMsg(self, MsgType, Msg):
##        'Logs the Message specified.'
##        #return 
##
##    @property
##    def LogFile(self):
##        'Gets the current log files full path.'
##        #return pLogFilePath
##
##    def _get(self):
##        'Set to true to display certain alerts and messages. Otherwise false. The default value is True.'
##        #return pRetVal
##    def _set(self, pRetVal):
##        'Set to true to display certain alerts and messages. Otherwise false. The default value is True.'
##    DisplayAlerts = property(_get, _set, doc = _set.__doc__)
##
##    def CreateApplication(self):
##        'Create a new instance of the application model root object.'
##        #return ppRetVal
##
##    def GrantPartnerAccess(self, vendor, product, key):
##        'Provide object model root for authorized business partners.'
##        #return ppRetVal
##
##    @property
##    def ProcessID(self):
##        'Gets process id for the current instance.'
##        #return pVal
##

class IAgUiApplicationEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Events raised by AgUiApplication coclass.'
    _iid_ = GUID('{84CD4AD7-3EED-4B2C-8E4D-1FF0D92D4CB2}')
    _idlflags_ = []
    _methods_ = []
IAgUiApplicationEvents._disp_methods_ = [
    DISPMETHOD([dispid(1), helpstring('Occurs upon the application shutdown.')], None, 'OnQuit'),
]
IAgUiFileOpenExt._methods_ = [
    COMMETHOD(['propget', helpstring('Gets/sets the mulitple file open collection.')], HRESULT, 'FileName',
              ( ['out', 'retval'], POINTER(POINTER(IAgUiFileOpenExtCollection)), 'pVal' )),
    COMMETHOD(['propput', helpstring('Gets/sets the mulitple file open collection.')], HRESULT, 'FileName',
              ( ['in'], POINTER(IAgUiFileOpenExtCollection), 'pVal' )),
    COMMETHOD(['propget', helpstring('Gets/sets the file open dialog filter description.')], HRESULT, 'FilterDescription',
              ( ['out', 'retval'], POINTER(BSTR), 'pVal' )),
    COMMETHOD(['propput', helpstring('Gets/sets the file open dialog filter description.')], HRESULT, 'FilterDescription',
              ( ['in'], BSTR, 'pVal' )),
    COMMETHOD(['propget', helpstring('Gets/sets the file open dialog filter pattern.')], HRESULT, 'FilterPattern',
              ( ['out', 'retval'], POINTER(BSTR), 'pVal' )),
    COMMETHOD(['propput', helpstring('Gets/sets the file open dialog filter pattern.')], HRESULT, 'FilterPattern',
              ( ['in'], BSTR, 'pVal' )),
]
################################################################
## code template for IAgUiFileOpenExt implementation
##class IAgUiFileOpenExt_Impl(object):
##    def _get(self):
##        'Gets/sets the mulitple file open collection.'
##        #return pVal
##    def _set(self, pVal):
##        'Gets/sets the mulitple file open collection.'
##    FileName = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Gets/sets the file open dialog filter description.'
##        #return pVal
##    def _set(self, pVal):
##        'Gets/sets the file open dialog filter description.'
##    FilterDescription = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Gets/sets the file open dialog filter pattern.'
##        #return pVal
##    def _set(self, pVal):
##        'Gets/sets the file open dialog filter pattern.'
##    FilterPattern = property(_get, _set, doc = _set.__doc__)
##

IAgUiFileOpenExtCollection._methods_ = [
    COMMETHOD([dispid(3), helpstring('Gets the total count of files in the collection.'), 'propget'], HRESULT, 'Count',
              ( ['out', 'retval'], POINTER(c_int), 'pVal' )),
    COMMETHOD([dispid(-4), helpstring('Enumerates through the file collection.'), 'propget'], HRESULT, '_NewEnum',
              ( ['out', 'retval'], POINTER(POINTER(IUnknown)), 'pVal' )),
    COMMETHOD([dispid(0), helpstring('Gets the file at the specified index.'), 'propget'], HRESULT, 'Item',
              ( ['in'], c_int, 'nIndex' ),
              ( ['out', 'retval'], POINTER(BSTR), 'pBSTR' )),
]
################################################################
## code template for IAgUiFileOpenExtCollection implementation
##class IAgUiFileOpenExtCollection_Impl(object):
##    @property
##    def Count(self):
##        'Gets the total count of files in the collection.'
##        #return pVal
##
##    @property
##    def _NewEnum(self):
##        'Enumerates through the file collection.'
##        #return pVal
##
##    @property
##    def Item(self, nIndex):
##        'Gets the file at the specified index.'
##        #return pBSTR
##

class AgMRUCollection(CoClass):
    'Provides information about most recently used (MRU) list.'
    _reg_clsid_ = GUID('{C342C66E-51DD-4527-90B4-0B059BC64D2B}')
    _idlflags_ = ['hidden', 'noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{781C4C18-C2C9-4E16-B620-7B22BC8DE954}', 1, 0)
AgMRUCollection._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IAgMRUCollection]

class AgUiApplication(CoClass):
    'A root object of the Application Model.'
    _reg_clsid_ = GUID('{3ED27D53-F604-4B0B-9255-EF255CCE3084}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{781C4C18-C2C9-4E16-B620-7B22BC8DE954}', 1, 0)
class IAgUiApplicationPartnerAccess(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    'Access to the application object model for business partners.'
    _iid_ = GUID('{B396C464-6B30-4E1E-B086-F983800C23FF}')
    _idlflags_ = ['oleautomation']
AgUiApplication._com_interfaces_ = [_IAgUiApplication, IAgUiApplication, IAgUiApplicationPartnerAccess]
AgUiApplication._outgoing_interfaces_ = [IAgUiApplicationEvents]

class Library(object):
    'AGI Ui Application 11'
    name = 'AgUiApplicationLib'
    _reg_typelib_ = ('{781C4C18-C2C9-4E16-B620-7B22BC8DE954}', 1, 0)

IAgMRUCollection._methods_ = [
    COMMETHOD([dispid(0), helpstring('Gets the MRU at the specified index.'), 'propget'], HRESULT, 'Item',
              ( ['in'], VARIANT, 'index' ),
              ( ['out', 'retval'], POINTER(BSTR), 'pVal' )),
    COMMETHOD([dispid(1), helpstring('Gets the total count of MRUs in the collection.'), 'propget'], HRESULT, 'Count',
              ( ['out', 'retval'], POINTER(c_int), 'pVal' )),
    COMMETHOD([dispid(-4), helpstring('Enumerates through the MRU collection.'), 'propget'], HRESULT, '_NewEnum',
              ( ['out', 'retval'], POINTER(POINTER(IUnknown)), 'ppVal' )),
]
################################################################
## code template for IAgMRUCollection implementation
##class IAgMRUCollection_Impl(object):
##    @property
##    def Item(self, index):
##        'Gets the MRU at the specified index.'
##        #return pVal
##
##    @property
##    def Count(self):
##        'Gets the total count of MRUs in the collection.'
##        #return pVal
##
##    @property
##    def _NewEnum(self):
##        'Enumerates through the MRU collection.'
##        #return ppVal
##

IAgUiApplication._methods_ = [
    COMMETHOD([helpstring('Loads a personality by its name.')], HRESULT, 'LoadPersonality',
              ( ['in'], BSTR, 'PersName' )),
    COMMETHOD(['propget', helpstring('Returns a reference to the currently loaded personality.')], HRESULT, 'Personality',
              ( ['out', 'retval'], POINTER(POINTER(IDispatch)), 'pVal' )),
    COMMETHOD(['propget', helpstring('Gets/sets whether the main window is visible.')], HRESULT, 'Visible',
              ( ['out', 'retval'], POINTER(VARIANT_BOOL), 'pVal' )),
    COMMETHOD(['propput', helpstring('Gets/sets whether the main window is visible.')], HRESULT, 'Visible',
              ( ['in'], VARIANT_BOOL, 'pVal' )),
    COMMETHOD(['propget', helpstring('Gets/sets whether the application is user controlled.')], HRESULT, 'UserControl',
              ( ['out', 'retval'], POINTER(VARIANT_BOOL), 'pVal' )),
    COMMETHOD(['propput', helpstring('Gets/sets whether the application is user controlled.')], HRESULT, 'UserControl',
              ( ['in'], VARIANT_BOOL, 'pVal' )),
    COMMETHOD(['propget', helpstring('Returns a collection of windows.')], HRESULT, 'Windows',
              ( ['out', 'retval'], POINTER(POINTER(comtypes.gen._9B797FC6_9EF1_4779_9691_A85B091560A1_0_1_0.IAgUiWindowsCollection)), 'pVal' )),
    COMMETHOD(['propget', helpstring('Gets/sets a height of the main window.')], HRESULT, 'Height',
              ( ['out', 'retval'], POINTER(c_int), 'pVal' )),
    COMMETHOD(['propput', helpstring('Gets/sets a height of the main window.')], HRESULT, 'Height',
              ( ['in'], c_int, 'pVal' )),
    COMMETHOD(['propget', helpstring('Gets/sets a width of the main window.')], HRESULT, 'Width',
              ( ['out', 'retval'], POINTER(c_int), 'pVal' )),
    COMMETHOD(['propput', helpstring('Gets/sets a width of the main window.')], HRESULT, 'Width',
              ( ['in'], c_int, 'pVal' )),
    COMMETHOD(['propget', helpstring('Gets/sets a vertical coordinate of the main window.')], HRESULT, 'Left',
              ( ['out', 'retval'], POINTER(c_int), 'pVal' )),
    COMMETHOD(['propput', helpstring('Gets/sets a vertical coordinate of the main window.')], HRESULT, 'Left',
              ( ['in'], c_int, 'pVal' )),
    COMMETHOD(['propget', helpstring('Gets/sets a horizontal coordinate of the main window.')], HRESULT, 'Top',
              ( ['out', 'retval'], POINTER(c_int), 'pVal' )),
    COMMETHOD(['propput', helpstring('Gets/sets a horizontal coordinate of the main window.')], HRESULT, 'Top',
              ( ['in'], c_int, 'pVal' )),
    COMMETHOD(['propget', helpstring('Gets/sets the state of the main window.')], HRESULT, 'WindowState',
              ( ['out', 'retval'], POINTER(comtypes.gen._9B797FC6_9EF1_4779_9691_A85B091560A1_0_1_0.AgEWindowState), 'pVal' )),
    COMMETHOD(['propput', helpstring('Gets/sets the state of the main window.')], HRESULT, 'WindowState',
              ( ['in'], comtypes.gen._9B797FC6_9EF1_4779_9691_A85B091560A1_0_1_0.AgEWindowState, 'pVal' )),
    COMMETHOD([helpstring("Activates the application's main window.")], HRESULT, 'Activate'),
    COMMETHOD(['propget', helpstring('Returns a collection most recently used files.')], HRESULT, 'MRUList',
              ( ['out', 'retval'], POINTER(POINTER(IAgMRUCollection)), 'ppVal' )),
    COMMETHOD([helpstring('Brings up a common File Open dialog and returns the file name selected by the user. If the user canceled, returns an empty file name.')], HRESULT, 'FileOpenDialog',
              ( ['in'], BSTR, 'DefaultExt' ),
              ( ['in'], BSTR, 'Filter' ),
              ( ['in'], BSTR, 'InitialDir' ),
              ( ['out', 'retval'], POINTER(BSTR), 'pFileName' )),
    COMMETHOD(['propget', helpstring('Returns the complete path to the application, excluding the final separator and name of the application. Read-only String.')], HRESULT, 'Path',
              ( ['out', 'retval'], POINTER(BSTR), 'pVal' )),
    COMMETHOD([helpstring('Only works from local HTML pages and scripts')], HRESULT, 'CreateObject',
              ( ['in'], BSTR, 'ProgID' ),
              ( ['in', 'optional'], BSTR, 'RemoteServer', '' ),
              ( ['out', 'retval'], POINTER(POINTER(IUnknown)), 'ppObject' )),
    COMMETHOD([helpstring('Brings up a common File SaveAs dialog and returns the file name selected by the user. If the user canceled, returns an empty file name.')], HRESULT, 'FileSaveAsDialog',
              ( ['in'], BSTR, 'DefaultExt' ),
              ( ['in'], BSTR, 'Filter' ),
              ( ['in'], BSTR, 'InitialDir' ),
              ( ['out', 'retval'], POINTER(BSTR), 'pFileName' )),
    COMMETHOD([helpstring('Shuts down the application.')], HRESULT, 'Quit'),
    COMMETHOD([helpstring('Brings up a standard File Open Dialog and returns an object representing the selected file.')], HRESULT, 'FileOpenDialogExt',
              ( ['in'], VARIANT_BOOL, 'AllowMultiSelect' ),
              ( ['in'], BSTR, 'DefaultExt' ),
              ( ['in'], BSTR, 'Filter' ),
              ( ['in'], BSTR, 'InitialDir' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgUiFileOpenExt)), 'ppObject' )),
    COMMETHOD(['propget', helpstring('Returns an HWND handle associated with the application main window.')], HRESULT, 'HWND',
              ( ['out', 'retval'], POINTER(c_int), 'pVal' )),
    COMMETHOD([helpstring('Brings up the Directory Picker Dialog and returns a selected directory name.')], HRESULT, 'DirectoryPickerDialog',
              ( ['in'], BSTR, 'Title' ),
              ( ['in'], BSTR, 'InitialDir' ),
              ( ['out', 'retval'], POINTER(BSTR), 'pDirName' )),
    COMMETHOD(['propget', helpstring('Gets/Sets message-pending delay for server busy dialog (in milliseconds )')], HRESULT, 'MessagePendingDelay',
              ( ['out', 'retval'], POINTER(c_int), 'pVal' )),
    COMMETHOD(['propput', helpstring('Gets/Sets message-pending delay for server busy dialog (in milliseconds )')], HRESULT, 'MessagePendingDelay',
              ( ['in'], c_int, 'pVal' )),
    COMMETHOD(['propget', helpstring('Returns an new instance of the root object of the STK Object Model')], HRESULT, 'Personality2',
              ( ['out', 'retval'], POINTER(POINTER(IDispatch)), 'ppRetVal' )),
    COMMETHOD([helpstring('Specifies the current log file to be written to.')], HRESULT, 'OpenLogFile',
              ( ['in'], BSTR, 'LogFileName' ),
              ( ['in'], AgEOpenLogFileMode, 'LogFileMode' ),
              ( ['out', 'retval'], POINTER(VARIANT_BOOL), 'pVal' )),
    COMMETHOD([helpstring('Logs the Message specified.')], HRESULT, 'LogMsg',
              ( ['in'], AgEUiLogMsgType, 'MsgType' ),
              ( ['in'], BSTR, 'Msg' )),
    COMMETHOD(['propget', helpstring('Gets the current log files full path.')], HRESULT, 'LogFile',
              ( ['out', 'retval'], POINTER(BSTR), 'pLogFilePath' )),
    COMMETHOD(['propget', helpstring('Set to true to display certain alerts and messages. Otherwise false. The default value is True.')], HRESULT, 'DisplayAlerts',
              ( ['out', 'retval'], POINTER(VARIANT_BOOL), 'pRetVal' )),
    COMMETHOD(['propput', helpstring('Set to true to display certain alerts and messages. Otherwise false. The default value is True.')], HRESULT, 'DisplayAlerts',
              ( ['in'], VARIANT_BOOL, 'pRetVal' )),
    COMMETHOD([helpstring('Create a new instance of the application model root object.')], HRESULT, 'CreateApplication',
              ( ['out', 'retval'], POINTER(POINTER(IAgUiApplication)), 'ppRetVal' )),
    COMMETHOD(['propget', helpstring('Gets process id for the current instance.')], HRESULT, 'ProcessID',
              ( ['out', 'retval'], POINTER(c_int), 'pVal' )),
]
################################################################
## code template for IAgUiApplication implementation
##class IAgUiApplication_Impl(object):
##    def LoadPersonality(self, PersName):
##        'Loads a personality by its name.'
##        #return 
##
##    @property
##    def Personality(self):
##        'Returns a reference to the currently loaded personality.'
##        #return pVal
##
##    def _get(self):
##        'Gets/sets whether the main window is visible.'
##        #return pVal
##    def _set(self, pVal):
##        'Gets/sets whether the main window is visible.'
##    Visible = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Gets/sets whether the application is user controlled.'
##        #return pVal
##    def _set(self, pVal):
##        'Gets/sets whether the application is user controlled.'
##    UserControl = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Windows(self):
##        'Returns a collection of windows.'
##        #return pVal
##
##    def _get(self):
##        'Gets/sets a height of the main window.'
##        #return pVal
##    def _set(self, pVal):
##        'Gets/sets a height of the main window.'
##    Height = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Gets/sets a width of the main window.'
##        #return pVal
##    def _set(self, pVal):
##        'Gets/sets a width of the main window.'
##    Width = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Gets/sets a vertical coordinate of the main window.'
##        #return pVal
##    def _set(self, pVal):
##        'Gets/sets a vertical coordinate of the main window.'
##    Left = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Gets/sets a horizontal coordinate of the main window.'
##        #return pVal
##    def _set(self, pVal):
##        'Gets/sets a horizontal coordinate of the main window.'
##    Top = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Gets/sets the state of the main window.'
##        #return pVal
##    def _set(self, pVal):
##        'Gets/sets the state of the main window.'
##    WindowState = property(_get, _set, doc = _set.__doc__)
##
##    def Activate(self):
##        "Activates the application's main window."
##        #return 
##
##    @property
##    def MRUList(self):
##        'Returns a collection most recently used files.'
##        #return ppVal
##
##    def FileOpenDialog(self, DefaultExt, Filter, InitialDir):
##        'Brings up a common File Open dialog and returns the file name selected by the user. If the user canceled, returns an empty file name.'
##        #return pFileName
##
##    @property
##    def Path(self):
##        'Returns the complete path to the application, excluding the final separator and name of the application. Read-only String.'
##        #return pVal
##
##    def CreateObject(self, ProgID, RemoteServer):
##        'Only works from local HTML pages and scripts'
##        #return ppObject
##
##    def FileSaveAsDialog(self, DefaultExt, Filter, InitialDir):
##        'Brings up a common File SaveAs dialog and returns the file name selected by the user. If the user canceled, returns an empty file name.'
##        #return pFileName
##
##    def Quit(self):
##        'Shuts down the application.'
##        #return 
##
##    def FileOpenDialogExt(self, AllowMultiSelect, DefaultExt, Filter, InitialDir):
##        'Brings up a standard File Open Dialog and returns an object representing the selected file.'
##        #return ppObject
##
##    @property
##    def HWND(self):
##        'Returns an HWND handle associated with the application main window.'
##        #return pVal
##
##    def DirectoryPickerDialog(self, Title, InitialDir):
##        'Brings up the Directory Picker Dialog and returns a selected directory name.'
##        #return pDirName
##
##    def _get(self):
##        'Gets/Sets message-pending delay for server busy dialog (in milliseconds )'
##        #return pVal
##    def _set(self, pVal):
##        'Gets/Sets message-pending delay for server busy dialog (in milliseconds )'
##    MessagePendingDelay = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Personality2(self):
##        'Returns an new instance of the root object of the STK Object Model'
##        #return ppRetVal
##
##    def OpenLogFile(self, LogFileName, LogFileMode):
##        'Specifies the current log file to be written to.'
##        #return pVal
##
##    def LogMsg(self, MsgType, Msg):
##        'Logs the Message specified.'
##        #return 
##
##    @property
##    def LogFile(self):
##        'Gets the current log files full path.'
##        #return pLogFilePath
##
##    def _get(self):
##        'Set to true to display certain alerts and messages. Otherwise false. The default value is True.'
##        #return pRetVal
##    def _set(self, pRetVal):
##        'Set to true to display certain alerts and messages. Otherwise false. The default value is True.'
##    DisplayAlerts = property(_get, _set, doc = _set.__doc__)
##
##    def CreateApplication(self):
##        'Create a new instance of the application model root object.'
##        #return ppRetVal
##
##    @property
##    def ProcessID(self):
##        'Gets process id for the current instance.'
##        #return pVal
##

IAgUiApplicationPartnerAccess._methods_ = [
    COMMETHOD([helpstring('Provide object model root for authorized business partners.')], HRESULT, 'GrantPartnerAccess',
              ( ['in'], BSTR, 'vendor' ),
              ( ['in'], BSTR, 'product' ),
              ( ['in'], BSTR, 'key' ),
              ( ['out', 'retval'], POINTER(POINTER(IDispatch)), 'ppRetVal' )),
]
################################################################
## code template for IAgUiApplicationPartnerAccess implementation
##class IAgUiApplicationPartnerAccess_Impl(object):
##    def GrantPartnerAccess(self, vendor, product, key):
##        'Provide object model root for authorized business partners.'
##        #return ppRetVal
##

__all__ = [ 'AgUiFileOpenExtCollection', 'AgUiApplication',
           'AgMRUCollection', 'IAgUiApplication', '_IAgUiApplication',
           'eUiLogMsgError', 'AgUiFileOpenExt', 'eUiLogMsgInfo',
           'eUiLogMsgWarning', 'IAgUiFileOpenExt',
           'IAgUiApplicationPartnerAccess', '_IAgUiFileOpenExt',
           'eUiLogMsgAlarm', 'IAgUiApplicationEvents',
           'eOpenLogFileForWriting', 'AgEUiLogMsgType',
           'eUiLogMsgDebug', 'eOpenLogFileForAppending',
           'IAgMRUCollection', 'AgEOpenLogFileMode',
           'eUiLogMsgForceInfo', 'IAgUiFileOpenExtCollection']
from comtypes import _check_version; _check_version('', 1491694984.000000)
