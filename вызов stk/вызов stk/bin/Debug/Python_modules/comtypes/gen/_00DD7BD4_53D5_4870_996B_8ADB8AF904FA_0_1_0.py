# -*- coding: mbcs -*-
typelib_path = 'D:\\STK\\bin\\AgStkUtil.dll'
_lcid = 0 # change this if required
from ctypes import *
from comtypes import GUID
from comtypes import CoClass
import comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0
from ctypes import HRESULT
from comtypes.automation import VARIANT
from comtypes.automation import _midlSAFEARRAY
from comtypes import helpstring
from comtypes import COMMETHOD
from comtypes import dispid
from comtypes import BSTR
from comtypes import IUnknown
from ctypes.wintypes import VARIANT_BOOL


class AgOrientationQuaternion(CoClass):
    'Quaternion orientation method.'
    _reg_clsid_ = GUID('{14A92724-ED96-4A4B-BF2F-DA2B08362C91}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{00DD7BD4-53D5-4870-996B-8ADB8AF904FA}', 1, 0)
class _IAgOrientationQuaternion(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'The hidden interface for IAgOrientationQuaternion'
    _iid_ = GUID('{9E4CD87C-5186-4546-86C1-CB841A3BD0BE}')
    _idlflags_ = ['hidden', 'dual', 'nonextensible', 'oleautomation']
class IAgOrientation(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    'Interface to set and retrieve the orientation method.'
    _iid_ = GUID('{672B5C2C-E494-44B4-A914-2877D59AC5A9}')
    _idlflags_ = ['oleautomation']
class IAgOrientationQuaternion(IAgOrientation):
    _case_insensitive_ = True
    'Interface for Quaternion orientation method.'
    _iid_ = GUID('{3C303D89-C28A-4A94-9017-8ABBD7AEC9C8}')
    _idlflags_ = ['oleautomation']
AgOrientationQuaternion._com_interfaces_ = [_IAgOrientationQuaternion, IAgOrientationQuaternion, IAgOrientation]

class AgUnitPrefsDim(CoClass):
    'Object that contains info on the Dimension.'
    _reg_clsid_ = GUID('{B7D85F32-055F-4945-BB26-18074FE998A9}')
    _idlflags_ = ['hidden', 'noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{00DD7BD4-53D5-4870-996B-8ADB8AF904FA}', 1, 0)
class _IAgUnitPrefsDim(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'The hidden IAgUnitPrefsDim interface.'
    _iid_ = GUID('{B7C3DA44-FD06-42EB-ADAD-FA952E68011B}')
    _idlflags_ = ['hidden', 'dual', 'nonextensible', 'oleautomation']
class IAgUnitPrefsDim(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    'Provides info on a Dimension from the global unit table.'
    _iid_ = GUID('{8A0E0AA9-F9A0-4732-A0A2-FA7393FE71B6}')
    _idlflags_ = ['oleautomation']
AgUnitPrefsDim._com_interfaces_ = [_IAgUnitPrefsDim, IAgUnitPrefsDim]

class IAgCartesian2Vector(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    'Represents a cartesian 2-D vector.'
    _iid_ = GUID('{222EF435-D824-4A2C-9953-1DCDC0FBCE44}')
    _idlflags_ = ['oleautomation']
IAgCartesian2Vector._methods_ = [
    COMMETHOD(['propget', helpstring('X coordinate')], HRESULT, 'X',
              ( ['out', 'retval'], POINTER(c_double), 'pRetVal' )),
    COMMETHOD(['propput', helpstring('X coordinate')], HRESULT, 'X',
              ( ['in'], c_double, 'pRetVal' )),
    COMMETHOD(['propget', helpstring('Y coordinate')], HRESULT, 'Y',
              ( ['out', 'retval'], POINTER(c_double), 'pRetVal' )),
    COMMETHOD(['propput', helpstring('Y coordinate')], HRESULT, 'Y',
              ( ['in'], c_double, 'pRetVal' )),
    COMMETHOD([helpstring('Returns cartesian vector')], HRESULT, 'Get',
              ( ['out'], POINTER(c_double), 'X' ),
              ( ['out'], POINTER(c_double), 'Y' )),
    COMMETHOD([helpstring('Sets cartesian vector')], HRESULT, 'Set',
              ( ['in'], c_double, 'X' ),
              ( ['in'], c_double, 'Y' )),
    COMMETHOD([helpstring('Returns coordinates as an array.')], HRESULT, 'ToArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
]
################################################################
## code template for IAgCartesian2Vector implementation
##class IAgCartesian2Vector_Impl(object):
##    def _get(self):
##        'X coordinate'
##        #return pRetVal
##    def _set(self, pRetVal):
##        'X coordinate'
##    X = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Y coordinate'
##        #return pRetVal
##    def _set(self, pRetVal):
##        'Y coordinate'
##    Y = property(_get, _set, doc = _set.__doc__)
##
##    def Get(self):
##        'Returns cartesian vector'
##        #return X, Y
##
##    def Set(self, X, Y):
##        'Sets cartesian vector'
##        #return 
##
##    def ToArray(self):
##        'Returns coordinates as an array.'
##        #return ppRetVal
##


# values for enumeration 'AgEExecMultiCmdResultAction'
eContinueOnError = 0
eStopOnError = 1
eExceptionOnError = 2
eIgnoreExecCmdResult = 32768
AgEExecMultiCmdResultAction = c_int # enum
class IAgOrientationAzEl(IAgOrientation):
    _case_insensitive_ = True
    'Interface for AzEl orientation method.'
    _iid_ = GUID('{F7E2943C-74D1-400F-98D4-505FBB83BCDC}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'AgEOrientationType'
eAzEl = 0
eEulerAngles = 1
eQuaternion = 2
eYPRAngles = 3
AgEOrientationType = c_int # enum

# values for enumeration 'AgEAzElAboutBoresight'
eAzElAboutBoresightHold = 0
eAzElAboutBoresightRotate = 1
AgEAzElAboutBoresight = c_int # enum

# values for enumeration 'AgEEulerOrientationSequence'
e121 = 0
e123 = 1
e131 = 2
e132 = 3
e212 = 4
e213 = 5
e231 = 6
e232 = 7
e312 = 8
e313 = 9
e321 = 10
e323 = 11
AgEEulerOrientationSequence = c_int # enum

# values for enumeration 'AgEYPRAnglesSequence'
ePRY = 0
ePYR = 1
eRPY = 2
eRYP = 3
eYPR = 4
eYRP = 5
AgEYPRAnglesSequence = c_int # enum
IAgOrientation._methods_ = [
    COMMETHOD([helpstring('Method to change the orientation method to the type specified.')], HRESULT, 'ConvertTo',
              ( ['in'], AgEOrientationType, 'Type' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgOrientation)), 'ppIAgOrientation' )),
    COMMETHOD(['propget', helpstring('Returns the orientation method currently being used.')], HRESULT, 'OrientationType',
              ( ['out', 'retval'], POINTER(AgEOrientationType), 'pType' )),
    COMMETHOD([helpstring('Assign a new orientation method.')], HRESULT, 'Assign',
              ( ['in'], POINTER(IAgOrientation), 'pOrientation' )),
    COMMETHOD([helpstring('Helper method to set orientation using the AzEl representation.')], HRESULT, 'AssignAzEl',
              ( ['in'], VARIANT, 'Azimuth' ),
              ( ['in'], VARIANT, 'Elevation' ),
              ( ['in'], AgEAzElAboutBoresight, 'AboutBoresight' )),
    COMMETHOD([helpstring('Helper method to set orientation using the Euler angles representation.')], HRESULT, 'AssignEulerAngles',
              ( ['in'], AgEEulerOrientationSequence, 'Sequence' ),
              ( ['in'], VARIANT, 'A' ),
              ( ['in'], VARIANT, 'B' ),
              ( ['in'], VARIANT, 'C' )),
    COMMETHOD([helpstring('Helper method to set orientation using the Quaternion representation.')], HRESULT, 'AssignQuaternion',
              ( ['in'], c_double, 'QX' ),
              ( ['in'], c_double, 'QY' ),
              ( ['in'], c_double, 'QZ' ),
              ( ['in'], c_double, 'QS' )),
    COMMETHOD([helpstring('Helper method to set orientation using the YPR angles representation.')], HRESULT, 'AssignYPRAngles',
              ( ['in'], AgEYPRAnglesSequence, 'Sequence' ),
              ( ['in'], VARIANT, 'Yaw' ),
              ( ['in'], VARIANT, 'Pitch' ),
              ( ['in'], VARIANT, 'Roll' )),
    COMMETHOD([helpstring('Helper method to get orientation using the AzEl representation.')], HRESULT, 'QueryAzEl',
              ( ['out'], POINTER(VARIANT), 'Azimuth' ),
              ( ['out'], POINTER(VARIANT), 'Elevation' ),
              ( ['out'], POINTER(AgEAzElAboutBoresight), 'AboutBoresight' )),
    COMMETHOD([helpstring('Helper method to get orientation using the Euler angles representation.')], HRESULT, 'QueryEulerAngles',
              ( ['in'], AgEEulerOrientationSequence, 'Sequence' ),
              ( ['out'], POINTER(VARIANT), 'A' ),
              ( ['out'], POINTER(VARIANT), 'B' ),
              ( ['out'], POINTER(VARIANT), 'C' )),
    COMMETHOD([helpstring('Helper method to get orientation using the Quaternion representation.')], HRESULT, 'QueryQuaternion',
              ( ['out'], POINTER(c_double), 'QX' ),
              ( ['out'], POINTER(c_double), 'QY' ),
              ( ['out'], POINTER(c_double), 'QZ' ),
              ( ['out'], POINTER(c_double), 'QS' )),
    COMMETHOD([helpstring('Helper method to get orientation using the YPR angles representation.')], HRESULT, 'QueryYPRAngles',
              ( ['in'], AgEYPRAnglesSequence, 'Sequence' ),
              ( ['out'], POINTER(VARIANT), 'Yaw' ),
              ( ['out'], POINTER(VARIANT), 'Pitch' ),
              ( ['out'], POINTER(VARIANT), 'Roll' )),
    COMMETHOD([helpstring('Returns the AzEl elements as an array.')], HRESULT, 'QueryAzElArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([helpstring('Returns the Euler elements as an array.')], HRESULT, 'QueryEulerAnglesArray',
              ( ['in'], AgEEulerOrientationSequence, 'Sequence' ),
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([helpstring('Returns the Quaternion elements as an array.')], HRESULT, 'QueryQuaternionArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([helpstring('Returns the YPR Angles elements as an array.')], HRESULT, 'QueryYPRAnglesArray',
              ( ['in'], AgEYPRAnglesSequence, 'Sequence' ),
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
]
################################################################
## code template for IAgOrientation implementation
##class IAgOrientation_Impl(object):
##    def ConvertTo(self, Type):
##        'Method to change the orientation method to the type specified.'
##        #return ppIAgOrientation
##
##    @property
##    def OrientationType(self):
##        'Returns the orientation method currently being used.'
##        #return pType
##
##    def Assign(self, pOrientation):
##        'Assign a new orientation method.'
##        #return 
##
##    def AssignAzEl(self, Azimuth, Elevation, AboutBoresight):
##        'Helper method to set orientation using the AzEl representation.'
##        #return 
##
##    def AssignEulerAngles(self, Sequence, A, B, C):
##        'Helper method to set orientation using the Euler angles representation.'
##        #return 
##
##    def AssignQuaternion(self, QX, QY, QZ, QS):
##        'Helper method to set orientation using the Quaternion representation.'
##        #return 
##
##    def AssignYPRAngles(self, Sequence, Yaw, Pitch, Roll):
##        'Helper method to set orientation using the YPR angles representation.'
##        #return 
##
##    def QueryAzEl(self):
##        'Helper method to get orientation using the AzEl representation.'
##        #return Azimuth, Elevation, AboutBoresight
##
##    def QueryEulerAngles(self, Sequence):
##        'Helper method to get orientation using the Euler angles representation.'
##        #return A, B, C
##
##    def QueryQuaternion(self):
##        'Helper method to get orientation using the Quaternion representation.'
##        #return QX, QY, QZ, QS
##
##    def QueryYPRAngles(self, Sequence):
##        'Helper method to get orientation using the YPR angles representation.'
##        #return Yaw, Pitch, Roll
##
##    def QueryAzElArray(self):
##        'Returns the AzEl elements as an array.'
##        #return ppRetVal
##
##    def QueryEulerAnglesArray(self, Sequence):
##        'Returns the Euler elements as an array.'
##        #return ppRetVal
##
##    def QueryQuaternionArray(self):
##        'Returns the Quaternion elements as an array.'
##        #return ppRetVal
##
##    def QueryYPRAnglesArray(self, Sequence):
##        'Returns the YPR Angles elements as an array.'
##        #return ppRetVal
##

IAgOrientationAzEl._methods_ = [
    COMMETHOD(['propget', helpstring('Measured in the XY plane of the parent reference frame about its Z axis in the right-handed sense for both vehicle-based sensors and facility-based sensors. Uses Angle Dimension.')], HRESULT, 'Azimuth',
              ( ['out', 'retval'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD(['propput', helpstring('Measured in the XY plane of the parent reference frame about its Z axis in the right-handed sense for both vehicle-based sensors and facility-based sensors. Uses Angle Dimension.')], HRESULT, 'Azimuth',
              ( ['in'], VARIANT, 'pVal' )),
    COMMETHOD(['propget', helpstring('Defined as the angle between the XY plane of the parent reference frame and the sensor or antenna boresight measured toward the positive Z axis. Uses Angle Dimension.')], HRESULT, 'Elevation',
              ( ['out', 'retval'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD(['propput', helpstring('Defined as the angle between the XY plane of the parent reference frame and the sensor or antenna boresight measured toward the positive Z axis. Uses Angle Dimension.')], HRESULT, 'Elevation',
              ( ['in'], VARIANT, 'pVal' )),
    COMMETHOD(['propget', helpstring("Determines orientation of the X and Y axes with respect to the parent's reference frame.")], HRESULT, 'AboutBoresight',
              ( ['out', 'retval'], POINTER(AgEAzElAboutBoresight), 'pVal' )),
    COMMETHOD(['propput', helpstring("Determines orientation of the X and Y axes with respect to the parent's reference frame.")], HRESULT, 'AboutBoresight',
              ( ['in'], AgEAzElAboutBoresight, 'pVal' )),
    COMMETHOD([helpstring('This property is deprecated. Use AssignAzEl instead.')], HRESULT, 'SetValues',
              ( ['in'], VARIANT, 'Azimuth' ),
              ( ['in'], VARIANT, 'Elevation' ),
              ( ['in'], AgEAzElAboutBoresight, 'AboutBoresight' )),
]
################################################################
## code template for IAgOrientationAzEl implementation
##class IAgOrientationAzEl_Impl(object):
##    def _get(self):
##        'Measured in the XY plane of the parent reference frame about its Z axis in the right-handed sense for both vehicle-based sensors and facility-based sensors. Uses Angle Dimension.'
##        #return pVal
##    def _set(self, pVal):
##        'Measured in the XY plane of the parent reference frame about its Z axis in the right-handed sense for both vehicle-based sensors and facility-based sensors. Uses Angle Dimension.'
##    Azimuth = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Defined as the angle between the XY plane of the parent reference frame and the sensor or antenna boresight measured toward the positive Z axis. Uses Angle Dimension.'
##        #return pVal
##    def _set(self, pVal):
##        'Defined as the angle between the XY plane of the parent reference frame and the sensor or antenna boresight measured toward the positive Z axis. Uses Angle Dimension.'
##    Elevation = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        "Determines orientation of the X and Y axes with respect to the parent's reference frame."
##        #return pVal
##    def _set(self, pVal):
##        "Determines orientation of the X and Y axes with respect to the parent's reference frame."
##    AboutBoresight = property(_get, _set, doc = _set.__doc__)
##
##    def SetValues(self, Azimuth, Elevation, AboutBoresight):
##        'This property is deprecated. Use AssignAzEl instead.'
##        #return 
##

class IAgPosition(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    'IAgPosition provides access to the position of the object'
    _iid_ = GUID('{98C86493-BD0A-431B-8033-3A4E0FA73967}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'AgEPositionType'
eCartesian = 0
eCylindrical = 1
eGeocentric = 2
eGeodetic = 3
eSpherical = 4
ePlanetocentric = 5
ePlanetodetic = 6
AgEPositionType = c_int # enum
IAgPosition._methods_ = [
    COMMETHOD([helpstring('Changes the position coordinates to type specified.')], HRESULT, 'ConvertTo',
              ( ['in'], AgEPositionType, 'Type' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgPosition)), 'ppIAgPosition' )),
    COMMETHOD(['propget', helpstring('Gets the type of position currently being used.')], HRESULT, 'PosType',
              ( ['out', 'retval'], POINTER(AgEPositionType), 'pType' )),
    COMMETHOD([helpstring('This assigns the coordinates into the system.')], HRESULT, 'Assign',
              ( ['in'], POINTER(IAgPosition), 'pPosition' )),
    COMMETHOD([helpstring('Helper method to assign the position using the Geocentric representation.')], HRESULT, 'AssignGeocentric',
              ( ['in'], VARIANT, 'Lat' ),
              ( ['in'], VARIANT, 'Lon' ),
              ( ['in'], c_double, 'Alt' )),
    COMMETHOD([helpstring('Helper method to assign the position using the Geodetic representation.')], HRESULT, 'AssignGeodetic',
              ( ['in'], VARIANT, 'Lat' ),
              ( ['in'], VARIANT, 'Lon' ),
              ( ['in'], c_double, 'Alt' )),
    COMMETHOD([helpstring('Helper method to assign the position using the Spherical representation')], HRESULT, 'AssignSpherical',
              ( ['in'], VARIANT, 'Lat' ),
              ( ['in'], VARIANT, 'Lon' ),
              ( ['in'], c_double, 'Radius' )),
    COMMETHOD([helpstring('Helper method to assign the position using the Cylindrical representation')], HRESULT, 'AssignCylindrical',
              ( ['in'], c_double, 'Radius' ),
              ( ['in'], c_double, 'Z' ),
              ( ['in'], VARIANT, 'Lon' )),
    COMMETHOD([helpstring('Helper method to assign the position using the Cartesian representation')], HRESULT, 'AssignCartesian',
              ( ['in'], c_double, 'X' ),
              ( ['in'], c_double, 'Y' ),
              ( ['in'], c_double, 'Z' )),
    COMMETHOD([helpstring('Helper method to assign the position using the Planetocentric representation')], HRESULT, 'AssignPlanetocentric',
              ( ['in'], VARIANT, 'Lat' ),
              ( ['in'], VARIANT, 'Lon' ),
              ( ['in'], c_double, 'Alt' )),
    COMMETHOD([helpstring('Helper method to assign the position using the Planetodetic representation')], HRESULT, 'AssignPlanetodetic',
              ( ['in'], VARIANT, 'Lat' ),
              ( ['in'], VARIANT, 'Lon' ),
              ( ['in'], c_double, 'Alt' )),
    COMMETHOD([helpstring('Helper method to get the position using the Planetocentric representation')], HRESULT, 'QueryPlanetocentric',
              ( ['out'], POINTER(VARIANT), 'Lat' ),
              ( ['out'], POINTER(VARIANT), 'Lon' ),
              ( ['out'], POINTER(c_double), 'Alt' )),
    COMMETHOD([helpstring('Helper method to get the position using the Planetodetic representation')], HRESULT, 'QueryPlanetodetic',
              ( ['out'], POINTER(VARIANT), 'Lat' ),
              ( ['out'], POINTER(VARIANT), 'Lon' ),
              ( ['out'], POINTER(c_double), 'Alt' )),
    COMMETHOD([helpstring('Helper method to get the position using the Spherical representation')], HRESULT, 'QuerySpherical',
              ( ['out'], POINTER(VARIANT), 'Lat' ),
              ( ['out'], POINTER(VARIANT), 'Lon' ),
              ( ['out'], POINTER(c_double), 'Radius' )),
    COMMETHOD([helpstring('Helper method to get the position using the Cylindrical representation')], HRESULT, 'QueryCylindrical',
              ( ['out'], POINTER(c_double), 'Radius' ),
              ( ['out'], POINTER(VARIANT), 'Lon' ),
              ( ['out'], POINTER(c_double), 'Z' )),
    COMMETHOD([helpstring('Helper method to get the position using the Cartesian representation')], HRESULT, 'QueryCartesian',
              ( ['out'], POINTER(c_double), 'X' ),
              ( ['out'], POINTER(c_double), 'Y' ),
              ( ['out'], POINTER(c_double), 'Z' )),
    COMMETHOD(['propget', helpstring('Gets the central body.')], HRESULT, 'CentralBodyName',
              ( ['out', 'retval'], POINTER(BSTR), 'pCBName' )),
    COMMETHOD([helpstring('Returns the Planetocentric elements as an array.')], HRESULT, 'QueryPlanetocentricArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([helpstring('Returns the Planetodetic elements as an array.')], HRESULT, 'QueryPlanetodeticArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([helpstring('Returns the Spherical elements as an array.')], HRESULT, 'QuerySphericalArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([helpstring('Returns the Cylindrical elements as an array.')], HRESULT, 'QueryCylindricalArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([helpstring('Returns the Cartesian elements as an array.')], HRESULT, 'QueryCartesianArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
]
################################################################
## code template for IAgPosition implementation
##class IAgPosition_Impl(object):
##    def ConvertTo(self, Type):
##        'Changes the position coordinates to type specified.'
##        #return ppIAgPosition
##
##    @property
##    def PosType(self):
##        'Gets the type of position currently being used.'
##        #return pType
##
##    def Assign(self, pPosition):
##        'This assigns the coordinates into the system.'
##        #return 
##
##    def AssignGeocentric(self, Lat, Lon, Alt):
##        'Helper method to assign the position using the Geocentric representation.'
##        #return 
##
##    def AssignGeodetic(self, Lat, Lon, Alt):
##        'Helper method to assign the position using the Geodetic representation.'
##        #return 
##
##    def AssignSpherical(self, Lat, Lon, Radius):
##        'Helper method to assign the position using the Spherical representation'
##        #return 
##
##    def AssignCylindrical(self, Radius, Z, Lon):
##        'Helper method to assign the position using the Cylindrical representation'
##        #return 
##
##    def AssignCartesian(self, X, Y, Z):
##        'Helper method to assign the position using the Cartesian representation'
##        #return 
##
##    def AssignPlanetocentric(self, Lat, Lon, Alt):
##        'Helper method to assign the position using the Planetocentric representation'
##        #return 
##
##    def AssignPlanetodetic(self, Lat, Lon, Alt):
##        'Helper method to assign the position using the Planetodetic representation'
##        #return 
##
##    def QueryPlanetocentric(self):
##        'Helper method to get the position using the Planetocentric representation'
##        #return Lat, Lon, Alt
##
##    def QueryPlanetodetic(self):
##        'Helper method to get the position using the Planetodetic representation'
##        #return Lat, Lon, Alt
##
##    def QuerySpherical(self):
##        'Helper method to get the position using the Spherical representation'
##        #return Lat, Lon, Radius
##
##    def QueryCylindrical(self):
##        'Helper method to get the position using the Cylindrical representation'
##        #return Radius, Lon, Z
##
##    def QueryCartesian(self):
##        'Helper method to get the position using the Cartesian representation'
##        #return X, Y, Z
##
##    @property
##    def CentralBodyName(self):
##        'Gets the central body.'
##        #return pCBName
##
##    def QueryPlanetocentricArray(self):
##        'Returns the Planetocentric elements as an array.'
##        #return ppRetVal
##
##    def QueryPlanetodeticArray(self):
##        'Returns the Planetodetic elements as an array.'
##        #return ppRetVal
##
##    def QuerySphericalArray(self):
##        'Returns the Spherical elements as an array.'
##        #return ppRetVal
##
##    def QueryCylindricalArray(self):
##        'Returns the Cylindrical elements as an array.'
##        #return ppRetVal
##
##    def QueryCartesianArray(self):
##        'Returns the Cartesian elements as an array.'
##        #return ppRetVal
##

class IAgUnitPrefsUnitCollection(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Provides access to the Unit collection.'
    _iid_ = GUID('{877F4DB9-79BB-43F7-A729-55B122B46768}')
    _idlflags_ = ['dual', 'nonextensible', 'oleautomation']
class IAgUnitPrefsUnit(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    'Provides info about a unit.'
    _iid_ = GUID('{087C2C8C-1CFC-4A71-A597-80E10952310A}')
    _idlflags_ = ['oleautomation']
_IAgUnitPrefsDim._methods_ = [
    COMMETHOD([dispid(201), helpstring('Returns the ID of the dimension.'), 'propget'], HRESULT, 'Id',
              ( ['out', 'retval'], POINTER(c_int), 'pId' )),
    COMMETHOD([dispid(202), helpstring("Returns the current Dimension's full name."), 'propget'], HRESULT, 'Name',
              ( ['out', 'retval'], POINTER(BSTR), 'pName' )),
    COMMETHOD([dispid(203), helpstring('Returns collection of Units.'), 'propget'], HRESULT, 'AvailableUnits',
              ( ['out', 'retval'], POINTER(POINTER(IAgUnitPrefsUnitCollection)), 'ppRetVal' )),
    COMMETHOD([dispid(204), helpstring('Returns the current unit for this dimension.'), 'propget'], HRESULT, 'CurrentUnit',
              ( ['out', 'retval'], POINTER(POINTER(IAgUnitPrefsUnit)), 'ppVal' )),
    COMMETHOD([dispid(205), helpstring('Sets the Unit for this simple dimension.')], HRESULT, 'SetCurrentUnit',
              ( ['in'], BSTR, 'UnitAbbrv' )),
]
################################################################
## code template for _IAgUnitPrefsDim implementation
##class _IAgUnitPrefsDim_Impl(object):
##    @property
##    def Id(self):
##        'Returns the ID of the dimension.'
##        #return pId
##
##    @property
##    def Name(self):
##        "Returns the current Dimension's full name."
##        #return pName
##
##    @property
##    def AvailableUnits(self):
##        'Returns collection of Units.'
##        #return ppRetVal
##
##    @property
##    def CurrentUnit(self):
##        'Returns the current unit for this dimension.'
##        #return ppVal
##
##    def SetCurrentUnit(self, UnitAbbrv):
##        'Sets the Unit for this simple dimension.'
##        #return 
##

class _IAgQuantity(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Provides helper methods for a quantity.'
    _iid_ = GUID('{F7289011-939C-4EAB-B743-4644A8ED1CDC}')
    _idlflags_ = ['hidden', 'dual', 'nonextensible', 'oleautomation']
class IAgQuantity(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    'Provides helper methods for a quantity.'
    _iid_ = GUID('{896B7C4F-D3D8-4472-ACD5-45F2C5D29742}')
    _idlflags_ = ['oleautomation']
_IAgQuantity._methods_ = [
    COMMETHOD([dispid(1), helpstring('Gets the name of the dimension'), 'propget'], HRESULT, 'Dimension',
              ( ['out', 'retval'], POINTER(BSTR), 'pDimName' )),
    COMMETHOD([dispid(2), helpstring('The current Unit abbreviation.'), 'propget'], HRESULT, 'Unit',
              ( ['out', 'retval'], POINTER(BSTR), 'pUnitAbbrv' )),
    COMMETHOD([dispid(3), helpstring('The current Unit abbreviation.')], HRESULT, 'ConvertToUnit',
              ( ['in'], BSTR, 'UnitAbbrv' )),
    COMMETHOD([dispid(4), helpstring('The current value. Changes depending on the current unit.'), 'propget'], HRESULT, 'Value',
              ( ['out', 'retval'], POINTER(c_double), 'pValue' )),
    COMMETHOD([dispid(4), helpstring('The current value. Changes depending on the current unit.'), 'propput'], HRESULT, 'Value',
              ( ['in'], c_double, 'pValue' )),
    COMMETHOD([dispid(5), helpstring('Adds the value from the IAgQuantity interface to this interface. Returns a new IAgQuantity. The dimensions must be similar.')], HRESULT, 'Add',
              ( ['in'], POINTER(IAgQuantity), 'Quantity' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgQuantity)), 'ppQuantity' )),
    COMMETHOD([dispid(6), helpstring('Subtracts the value from the IAgQuantity interface to this interface. Returns a new IAgQuantity. The dimensions must be similar.')], HRESULT, 'Subtract',
              ( ['in'], POINTER(IAgQuantity), 'Quantity' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgQuantity)), 'ppQuantity' )),
    COMMETHOD([dispid(7), helpstring('Multiplies the value from the IAgQuantity interface to this interface. Returns a new IAgQuantity. The dimensions must be similar.')], HRESULT, 'MultiplyQty',
              ( ['in'], POINTER(IAgQuantity), 'Quantity' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgQuantity)), 'ppQuantity' )),
    COMMETHOD([dispid(8), helpstring('Divides the value from the IAgQuantity interface to this interface. Returns a new IAgQuantity. The dimensions must be similar.')], HRESULT, 'DivideQty',
              ( ['in'], POINTER(IAgQuantity), 'Quantity' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgQuantity)), 'ppQuantity' )),
]
################################################################
## code template for _IAgQuantity implementation
##class _IAgQuantity_Impl(object):
##    @property
##    def Dimension(self):
##        'Gets the name of the dimension'
##        #return pDimName
##
##    @property
##    def Unit(self):
##        'The current Unit abbreviation.'
##        #return pUnitAbbrv
##
##    def ConvertToUnit(self, UnitAbbrv):
##        'The current Unit abbreviation.'
##        #return 
##
##    def _get(self):
##        'The current value. Changes depending on the current unit.'
##        #return pValue
##    def _set(self, pValue):
##        'The current value. Changes depending on the current unit.'
##    Value = property(_get, _set, doc = _set.__doc__)
##
##    def Add(self, Quantity):
##        'Adds the value from the IAgQuantity interface to this interface. Returns a new IAgQuantity. The dimensions must be similar.'
##        #return ppQuantity
##
##    def Subtract(self, Quantity):
##        'Subtracts the value from the IAgQuantity interface to this interface. Returns a new IAgQuantity. The dimensions must be similar.'
##        #return ppQuantity
##
##    def MultiplyQty(self, Quantity):
##        'Multiplies the value from the IAgQuantity interface to this interface. Returns a new IAgQuantity. The dimensions must be similar.'
##        #return ppQuantity
##
##    def DivideQty(self, Quantity):
##        'Divides the value from the IAgQuantity interface to this interface. Returns a new IAgQuantity. The dimensions must be similar.'
##        #return ppQuantity
##

class AgQuantity(CoClass):
    'Object that contains a quantity.'
    _reg_clsid_ = GUID('{DB42B23D-1EC7-4578-B9EA-A9DBD884AFF2}')
    _idlflags_ = ['hidden', 'noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{00DD7BD4-53D5-4870-996B-8ADB8AF904FA}', 1, 0)
AgQuantity._com_interfaces_ = [_IAgQuantity, IAgQuantity]

IAgOrientationQuaternion._methods_ = [
    COMMETHOD(['propget', helpstring('qx vector component. Dimensionless')], HRESULT, 'QX',
              ( ['out', 'retval'], POINTER(c_double), 'pVal' )),
    COMMETHOD(['propput', helpstring('qx vector component. Dimensionless')], HRESULT, 'QX',
              ( ['in'], c_double, 'pVal' )),
    COMMETHOD(['propget', helpstring('qy vector component. Dimensionless.')], HRESULT, 'QY',
              ( ['out', 'retval'], POINTER(c_double), 'pVal' )),
    COMMETHOD(['propput', helpstring('qy vector component. Dimensionless.')], HRESULT, 'QY',
              ( ['in'], c_double, 'pVal' )),
    COMMETHOD(['propget', helpstring('qz vector component. Dimensionless.')], HRESULT, 'QZ',
              ( ['out', 'retval'], POINTER(c_double), 'pVal' )),
    COMMETHOD(['propput', helpstring('qz vector component. Dimensionless.')], HRESULT, 'QZ',
              ( ['in'], c_double, 'pVal' )),
    COMMETHOD(['propget', helpstring('qs scalar component. Dimensionless.')], HRESULT, 'QS',
              ( ['out', 'retval'], POINTER(c_double), 'pVal' )),
    COMMETHOD(['propput', helpstring('qs scalar component. Dimensionless.')], HRESULT, 'QS',
              ( ['in'], c_double, 'pVal' )),
    COMMETHOD([helpstring('This property is deprecated. Use AssignQuaternion instead.')], HRESULT, 'SetValues',
              ( ['in'], c_double, 'QX' ),
              ( ['in'], c_double, 'QY' ),
              ( ['in'], c_double, 'QZ' ),
              ( ['in'], c_double, 'QS' )),
]
################################################################
## code template for IAgOrientationQuaternion implementation
##class IAgOrientationQuaternion_Impl(object):
##    def _get(self):
##        'qx vector component. Dimensionless'
##        #return pVal
##    def _set(self, pVal):
##        'qx vector component. Dimensionless'
##    QX = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'qy vector component. Dimensionless.'
##        #return pVal
##    def _set(self, pVal):
##        'qy vector component. Dimensionless.'
##    QY = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'qz vector component. Dimensionless.'
##        #return pVal
##    def _set(self, pVal):
##        'qz vector component. Dimensionless.'
##    QZ = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'qs scalar component. Dimensionless.'
##        #return pVal
##    def _set(self, pVal):
##        'qs scalar component. Dimensionless.'
##    QS = property(_get, _set, doc = _set.__doc__)
##
##    def SetValues(self, QX, QY, QZ, QS):
##        'This property is deprecated. Use AssignQuaternion instead.'
##        #return 
##

class AgOrientationYPRAngles(CoClass):
    'Yaw-Pitch Roll (YPR) Angles orientation system.'
    _reg_clsid_ = GUID('{714B0965-A228-4EE0-AF6D-CCA8782132A1}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{00DD7BD4-53D5-4870-996B-8ADB8AF904FA}', 1, 0)
class _IAgOrientationYPRAngles(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'The hidden interface for IAgOrientationYPRAngles'
    _iid_ = GUID('{44D175B2-F269-4AA9-A9F0-59DC11CA56D7}')
    _idlflags_ = ['hidden', 'dual', 'nonextensible', 'oleautomation']
class IAgOrientationYPRAngles(IAgOrientation):
    _case_insensitive_ = True
    'Interface for Yaw-Pitch Roll (YPR) Angles orientation system.'
    _iid_ = GUID('{0F54E29D-6864-468D-B1CD-1D12CE0ADD60}')
    _idlflags_ = ['oleautomation']
AgOrientationYPRAngles._com_interfaces_ = [_IAgOrientationYPRAngles, IAgOrientationYPRAngles, IAgOrientation]

class IAgExecMultiCmdResult(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Collection of objects returned by the ExecuteMultipleCommands.'
    _iid_ = GUID('{E3E18E06-94CF-4673-8C91-4689F20FD683}')
    _idlflags_ = ['hidden', 'dual', 'nonextensible', 'oleautomation']
class IAgExecCmdResult(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Collection of strings returned by the ExecuteCommand.'
    _iid_ = GUID('{D935A0A9-464B-456E-9014-4E9D15F6D719}')
    _idlflags_ = ['hidden', 'dual', 'nonextensible', 'oleautomation']
IAgExecMultiCmdResult._methods_ = [
    COMMETHOD([dispid(1), helpstring('Number of elements contained in the collection.'), 'propget'], HRESULT, 'Count',
              ( ['out', 'retval'], POINTER(c_int), 'pCount' )),
    COMMETHOD([dispid(0), helpstring('Gets the element at the specified index (0-based).'), 'propget'], HRESULT, 'Item',
              ( ['in'], c_int, 'Index' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgExecCmdResult)), 'pRetVal' )),
    COMMETHOD([dispid(-4), helpstring('Returns an object that can be used to iterate through all the objects in the collection.'), 'propget'], HRESULT, '_NewEnum',
              ( ['out', 'retval'], POINTER(POINTER(IUnknown)), 'ppEnum' )),
]
################################################################
## code template for IAgExecMultiCmdResult implementation
##class IAgExecMultiCmdResult_Impl(object):
##    @property
##    def Count(self):
##        'Number of elements contained in the collection.'
##        #return pCount
##
##    @property
##    def Item(self, Index):
##        'Gets the element at the specified index (0-based).'
##        #return pRetVal
##
##    @property
##    def _NewEnum(self):
##        'Returns an object that can be used to iterate through all the objects in the collection.'
##        #return ppEnum
##

class IAgDate(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    'Provides helper methods for a date.'
    _iid_ = GUID('{EC468355-7A84-4D43-A5A2-41E8F4890415}')
    _idlflags_ = ['oleautomation']
IAgDate._methods_ = [
    COMMETHOD([helpstring('Returns the value of the date given the unit.')], HRESULT, 'Format',
              ( ['in'], BSTR, 'Unit' ),
              ( ['out', 'retval'], POINTER(BSTR), 'pValue' )),
    COMMETHOD([helpstring('Sets this date with the given date value and unit type.')], HRESULT, 'SetDate',
              ( ['in'], BSTR, 'Unit' ),
              ( ['in'], BSTR, 'Value' )),
    COMMETHOD(['propget', helpstring('The current time in OLE DATE Format.')], HRESULT, 'OLEDate',
              ( ['out', 'retval'], POINTER(c_double), 'pDate' )),
    COMMETHOD(['propput', helpstring('The current time in OLE DATE Format.')], HRESULT, 'OLEDate',
              ( ['in'], c_double, 'pDate' )),
    COMMETHOD(['propget', helpstring('The Julian Day Number of the date of interest.')], HRESULT, 'WholeDays',
              ( ['out', 'retval'], POINTER(c_int), 'pVal' )),
    COMMETHOD(['propput', helpstring('The Julian Day Number of the date of interest.')], HRESULT, 'WholeDays',
              ( ['in'], c_int, 'pVal' )),
    COMMETHOD(['propget', helpstring('Contains values between 0.0 and 86400 with the exception of when the date is inside a leap second in which case the SecIntoDay can become as large as 86401.0')], HRESULT, 'SecIntoDay',
              ( ['out', 'retval'], POINTER(c_double), 'pVal' )),
    COMMETHOD(['propput', helpstring('Contains values between 0.0 and 86400 with the exception of when the date is inside a leap second in which case the SecIntoDay can become as large as 86401.0')], HRESULT, 'SecIntoDay',
              ( ['in'], c_double, 'pVal' )),
    COMMETHOD(['propget', helpstring('The UTC Day Number of the date of interest.')], HRESULT, 'WholeDaysUTC',
              ( ['out', 'retval'], POINTER(c_int), 'pVal' )),
    COMMETHOD(['propput', helpstring('The UTC Day Number of the date of interest.')], HRESULT, 'WholeDaysUTC',
              ( ['in'], c_int, 'pVal' )),
    COMMETHOD(['propget', helpstring('Contains values between 0.0 and 86400 with the exception of when the date is inside a leap second in which case the SecIntoDay can become as large as 86401.0')], HRESULT, 'SecIntoDayUTC',
              ( ['out', 'retval'], POINTER(c_double), 'pVal' )),
    COMMETHOD(['propput', helpstring('Contains values between 0.0 and 86400 with the exception of when the date is inside a leap second in which case the SecIntoDay can become as large as 86401.0')], HRESULT, 'SecIntoDayUTC',
              ( ['in'], c_double, 'pVal' )),
    COMMETHOD([helpstring('Adds the value in the given unit and returns a new date interface.')], HRESULT, 'Add',
              ( ['in'], BSTR, 'Unit' ),
              ( ['in'], c_double, 'Value' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgDate)), 'ppDate' )),
    COMMETHOD([helpstring('Subtracts the value in the given unit and returns a new date interface.')], HRESULT, 'Subtract',
              ( ['in'], BSTR, 'Unit' ),
              ( ['in'], c_double, 'Value' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgDate)), 'ppDate' )),
    COMMETHOD([helpstring('Subtracts the value from the IAgDate interface and returns an IAgQuantity.')], HRESULT, 'Span',
              ( ['in'], POINTER(IAgDate), 'Date' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgQuantity)), 'ppQuantity' )),
]
################################################################
## code template for IAgDate implementation
##class IAgDate_Impl(object):
##    def Format(self, Unit):
##        'Returns the value of the date given the unit.'
##        #return pValue
##
##    def SetDate(self, Unit, Value):
##        'Sets this date with the given date value and unit type.'
##        #return 
##
##    def _get(self):
##        'The current time in OLE DATE Format.'
##        #return pDate
##    def _set(self, pDate):
##        'The current time in OLE DATE Format.'
##    OLEDate = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'The Julian Day Number of the date of interest.'
##        #return pVal
##    def _set(self, pVal):
##        'The Julian Day Number of the date of interest.'
##    WholeDays = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Contains values between 0.0 and 86400 with the exception of when the date is inside a leap second in which case the SecIntoDay can become as large as 86401.0'
##        #return pVal
##    def _set(self, pVal):
##        'Contains values between 0.0 and 86400 with the exception of when the date is inside a leap second in which case the SecIntoDay can become as large as 86401.0'
##    SecIntoDay = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'The UTC Day Number of the date of interest.'
##        #return pVal
##    def _set(self, pVal):
##        'The UTC Day Number of the date of interest.'
##    WholeDaysUTC = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Contains values between 0.0 and 86400 with the exception of when the date is inside a leap second in which case the SecIntoDay can become as large as 86401.0'
##        #return pVal
##    def _set(self, pVal):
##        'Contains values between 0.0 and 86400 with the exception of when the date is inside a leap second in which case the SecIntoDay can become as large as 86401.0'
##    SecIntoDayUTC = property(_get, _set, doc = _set.__doc__)
##
##    def Add(self, Unit, Value):
##        'Adds the value in the given unit and returns a new date interface.'
##        #return ppDate
##
##    def Subtract(self, Unit, Value):
##        'Subtracts the value in the given unit and returns a new date interface.'
##        #return ppDate
##
##    def Span(self, Date):
##        'Subtracts the value from the IAgDate interface and returns an IAgQuantity.'
##        #return ppQuantity
##

_IAgOrientationQuaternion._methods_ = [
    COMMETHOD([dispid(201), helpstring('qx vector component. Dimensionless'), 'propget'], HRESULT, 'QX',
              ( ['out', 'retval'], POINTER(c_double), 'pVal' )),
    COMMETHOD([dispid(201), helpstring('qx vector component. Dimensionless'), 'propput'], HRESULT, 'QX',
              ( ['in'], c_double, 'pVal' )),
    COMMETHOD([dispid(202), helpstring('qy vector component. Dimensionless.'), 'propget'], HRESULT, 'QY',
              ( ['out', 'retval'], POINTER(c_double), 'pVal' )),
    COMMETHOD([dispid(202), helpstring('qy vector component. Dimensionless.'), 'propput'], HRESULT, 'QY',
              ( ['in'], c_double, 'pVal' )),
    COMMETHOD([dispid(203), helpstring('qz vector component. Dimensionless.'), 'propget'], HRESULT, 'QZ',
              ( ['out', 'retval'], POINTER(c_double), 'pVal' )),
    COMMETHOD([dispid(203), helpstring('qz vector component. Dimensionless.'), 'propput'], HRESULT, 'QZ',
              ( ['in'], c_double, 'pVal' )),
    COMMETHOD([dispid(204), helpstring('qs scalar component. Dimensionless.'), 'propget'], HRESULT, 'QS',
              ( ['out', 'retval'], POINTER(c_double), 'pVal' )),
    COMMETHOD([dispid(204), helpstring('qs scalar component. Dimensionless.'), 'propput'], HRESULT, 'QS',
              ( ['in'], c_double, 'pVal' )),
    COMMETHOD([dispid(205), helpstring('This property is deprecated. Use AssignQuaternion instead.')], HRESULT, 'SetValues',
              ( ['in'], c_double, 'QX' ),
              ( ['in'], c_double, 'QY' ),
              ( ['in'], c_double, 'QZ' ),
              ( ['in'], c_double, 'QS' )),
    COMMETHOD([dispid(401), helpstring('Method to change the orientation method to the type specified.')], HRESULT, 'ConvertTo',
              ( ['in'], AgEOrientationType, 'Type' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgOrientation)), 'ppIAgOrientation' )),
    COMMETHOD([dispid(402), helpstring('Returns the orientation method currently being used.'), 'propget'], HRESULT, 'OrientationType',
              ( ['out', 'retval'], POINTER(AgEOrientationType), 'pType' )),
    COMMETHOD([dispid(403), helpstring('Assign a new orientation method.')], HRESULT, 'Assign',
              ( ['in'], POINTER(IAgOrientation), 'pOrientation' )),
    COMMETHOD([dispid(404), helpstring('Helper method to set orientation using the AzEl representation.')], HRESULT, 'AssignAzEl',
              ( ['in'], VARIANT, 'Azimuth' ),
              ( ['in'], VARIANT, 'Elevation' ),
              ( ['in'], AgEAzElAboutBoresight, 'AboutBoresight' )),
    COMMETHOD([dispid(405), helpstring('Helper method to set orientation using the Euler angles representation.')], HRESULT, 'AssignEulerAngles',
              ( ['in'], AgEEulerOrientationSequence, 'Sequence' ),
              ( ['in'], VARIANT, 'A' ),
              ( ['in'], VARIANT, 'B' ),
              ( ['in'], VARIANT, 'C' )),
    COMMETHOD([dispid(406), helpstring('Helper method to set orientation using the Quaternion representation.')], HRESULT, 'AssignQuaternion',
              ( ['in'], c_double, 'QX' ),
              ( ['in'], c_double, 'QY' ),
              ( ['in'], c_double, 'QZ' ),
              ( ['in'], c_double, 'QS' )),
    COMMETHOD([dispid(407), helpstring('Helper method to set orientation using the YPR angles representation.')], HRESULT, 'AssignYPRAngles',
              ( ['in'], AgEYPRAnglesSequence, 'Sequence' ),
              ( ['in'], VARIANT, 'Yaw' ),
              ( ['in'], VARIANT, 'Pitch' ),
              ( ['in'], VARIANT, 'Roll' )),
    COMMETHOD([dispid(408), helpstring('Helper method to get orientation using the AzEl representation.')], HRESULT, 'QueryAzEl',
              ( ['out'], POINTER(VARIANT), 'Azimuth' ),
              ( ['out'], POINTER(VARIANT), 'Elevation' ),
              ( ['out'], POINTER(AgEAzElAboutBoresight), 'AboutBoresight' )),
    COMMETHOD([dispid(409), helpstring('Helper method to get orientation using the Euler angles representation.')], HRESULT, 'QueryEulerAngles',
              ( ['in'], AgEEulerOrientationSequence, 'Sequence' ),
              ( ['out'], POINTER(VARIANT), 'A' ),
              ( ['out'], POINTER(VARIANT), 'B' ),
              ( ['out'], POINTER(VARIANT), 'C' )),
    COMMETHOD([dispid(410), helpstring('Helper method to get orientation using the Quaternion representation.')], HRESULT, 'QueryQuaternion',
              ( ['out'], POINTER(c_double), 'QX' ),
              ( ['out'], POINTER(c_double), 'QY' ),
              ( ['out'], POINTER(c_double), 'QZ' ),
              ( ['out'], POINTER(c_double), 'QS' )),
    COMMETHOD([dispid(411), helpstring('Helper method to get orientation using the YPR angles representation.')], HRESULT, 'QueryYPRAngles',
              ( ['in'], AgEYPRAnglesSequence, 'Sequence' ),
              ( ['out'], POINTER(VARIANT), 'Yaw' ),
              ( ['out'], POINTER(VARIANT), 'Pitch' ),
              ( ['out'], POINTER(VARIANT), 'Roll' )),
    COMMETHOD([dispid(412), helpstring('Returns the AzEl elements as an array.')], HRESULT, 'QueryAzElArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(413), helpstring('Returns the Euler elements as an array.')], HRESULT, 'QueryEulerAnglesArray',
              ( ['in'], AgEEulerOrientationSequence, 'Sequence' ),
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(414), helpstring('Returns the Quaternion elements as an array.')], HRESULT, 'QueryQuaternionArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(415), helpstring('Returns the YPR Angles elements as an array.')], HRESULT, 'QueryYPRAnglesArray',
              ( ['in'], AgEYPRAnglesSequence, 'Sequence' ),
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
]
################################################################
## code template for _IAgOrientationQuaternion implementation
##class _IAgOrientationQuaternion_Impl(object):
##    def _get(self):
##        'qx vector component. Dimensionless'
##        #return pVal
##    def _set(self, pVal):
##        'qx vector component. Dimensionless'
##    QX = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'qy vector component. Dimensionless.'
##        #return pVal
##    def _set(self, pVal):
##        'qy vector component. Dimensionless.'
##    QY = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'qz vector component. Dimensionless.'
##        #return pVal
##    def _set(self, pVal):
##        'qz vector component. Dimensionless.'
##    QZ = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'qs scalar component. Dimensionless.'
##        #return pVal
##    def _set(self, pVal):
##        'qs scalar component. Dimensionless.'
##    QS = property(_get, _set, doc = _set.__doc__)
##
##    def SetValues(self, QX, QY, QZ, QS):
##        'This property is deprecated. Use AssignQuaternion instead.'
##        #return 
##
##    def ConvertTo(self, Type):
##        'Method to change the orientation method to the type specified.'
##        #return ppIAgOrientation
##
##    @property
##    def OrientationType(self):
##        'Returns the orientation method currently being used.'
##        #return pType
##
##    def Assign(self, pOrientation):
##        'Assign a new orientation method.'
##        #return 
##
##    def AssignAzEl(self, Azimuth, Elevation, AboutBoresight):
##        'Helper method to set orientation using the AzEl representation.'
##        #return 
##
##    def AssignEulerAngles(self, Sequence, A, B, C):
##        'Helper method to set orientation using the Euler angles representation.'
##        #return 
##
##    def AssignQuaternion(self, QX, QY, QZ, QS):
##        'Helper method to set orientation using the Quaternion representation.'
##        #return 
##
##    def AssignYPRAngles(self, Sequence, Yaw, Pitch, Roll):
##        'Helper method to set orientation using the YPR angles representation.'
##        #return 
##
##    def QueryAzEl(self):
##        'Helper method to get orientation using the AzEl representation.'
##        #return Azimuth, Elevation, AboutBoresight
##
##    def QueryEulerAngles(self, Sequence):
##        'Helper method to get orientation using the Euler angles representation.'
##        #return A, B, C
##
##    def QueryQuaternion(self):
##        'Helper method to get orientation using the Quaternion representation.'
##        #return QX, QY, QZ, QS
##
##    def QueryYPRAngles(self, Sequence):
##        'Helper method to get orientation using the YPR angles representation.'
##        #return Yaw, Pitch, Roll
##
##    def QueryAzElArray(self):
##        'Returns the AzEl elements as an array.'
##        #return ppRetVal
##
##    def QueryEulerAnglesArray(self, Sequence):
##        'Returns the Euler elements as an array.'
##        #return ppRetVal
##
##    def QueryQuaternionArray(self):
##        'Returns the Quaternion elements as an array.'
##        #return ppRetVal
##
##    def QueryYPRAnglesArray(self, Sequence):
##        'Returns the YPR Angles elements as an array.'
##        #return ppRetVal
##

class IAgCylindrical(IAgPosition):
    _case_insensitive_ = True
    'Cylindrical Position Type.'
    _iid_ = GUID('{66D88E7C-DFA4-4588-9F91-44C5C43D56DE}')
    _idlflags_ = ['oleautomation']
IAgCylindrical._methods_ = [
    COMMETHOD(['propget', helpstring('Dimension depends on context.')], HRESULT, 'Radius',
              ( ['out', 'retval'], POINTER(c_double), 'pVal' )),
    COMMETHOD(['propput', helpstring('Dimension depends on context.')], HRESULT, 'Radius',
              ( ['in'], c_double, 'pVal' )),
    COMMETHOD(['propget', helpstring('Uses Angle Dimension.')], HRESULT, 'Z',
              ( ['out', 'retval'], POINTER(c_double), 'pVal' )),
    COMMETHOD(['propput', helpstring('Uses Angle Dimension.')], HRESULT, 'Z',
              ( ['in'], c_double, 'pVal' )),
    COMMETHOD(['propget', helpstring('Dimension depends on context.')], HRESULT, 'Lon',
              ( ['out', 'retval'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD(['propput', helpstring('Dimension depends on context.')], HRESULT, 'Lon',
              ( ['in'], VARIANT, 'pVal' )),
    COMMETHOD([helpstring('This property is deprecated. Use AssignCylindrical instead.')], HRESULT, 'SetValues',
              ( ['in'], c_double, 'Radius' ),
              ( ['in'], c_double, 'Z' ),
              ( ['in'], VARIANT, 'Lon' )),
]
################################################################
## code template for IAgCylindrical implementation
##class IAgCylindrical_Impl(object):
##    def _get(self):
##        'Dimension depends on context.'
##        #return pVal
##    def _set(self, pVal):
##        'Dimension depends on context.'
##    Radius = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Uses Angle Dimension.'
##        #return pVal
##    def _set(self, pVal):
##        'Uses Angle Dimension.'
##    Z = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Dimension depends on context.'
##        #return pVal
##    def _set(self, pVal):
##        'Dimension depends on context.'
##    Lon = property(_get, _set, doc = _set.__doc__)
##
##    def SetValues(self, Radius, Z, Lon):
##        'This property is deprecated. Use AssignCylindrical instead.'
##        #return 
##

class AgPropertyInfoCollection(CoClass):
    'Property Infomation Collection coclass.'
    _reg_clsid_ = GUID('{2C3A4FA2-6F9D-42D8-9709-182E0E618D7F}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{00DD7BD4-53D5-4870-996B-8ADB8AF904FA}', 1, 0)
class IAgPropertyInfoCollection(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'The collection of properties.'
    _iid_ = GUID('{25E3F178-638F-462D-9857-C548CF7BBA80}')
    _idlflags_ = ['dual', 'nonextensible', 'oleautomation']
AgPropertyInfoCollection._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IAgPropertyInfoCollection]

_IAgOrientationYPRAngles._methods_ = [
    COMMETHOD([dispid(201), helpstring('YPR sequence. Must be set before Yaw,Pitch,Roll values. Otherwise the current Yaw,Pitch,Roll values will be converted to the Sequence specified.'), 'propget'], HRESULT, 'Sequence',
              ( ['out', 'retval'], POINTER(AgEYPRAnglesSequence), 'pVal' )),
    COMMETHOD([dispid(201), helpstring('YPR sequence. Must be set before Yaw,Pitch,Roll values. Otherwise the current Yaw,Pitch,Roll values will be converted to the Sequence specified.'), 'propput'], HRESULT, 'Sequence',
              ( ['in'], AgEYPRAnglesSequence, 'pVal' )),
    COMMETHOD([dispid(202), helpstring('Yaw angle. Uses Angle Dimension.'), 'propget'], HRESULT, 'Yaw',
              ( ['out', 'retval'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD([dispid(202), helpstring('Yaw angle. Uses Angle Dimension.'), 'propput'], HRESULT, 'Yaw',
              ( ['in'], VARIANT, 'pVal' )),
    COMMETHOD([dispid(203), helpstring('Pitch angle. Uses Angle Dimension.'), 'propget'], HRESULT, 'Pitch',
              ( ['out', 'retval'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD([dispid(203), helpstring('Pitch angle. Uses Angle Dimension.'), 'propput'], HRESULT, 'Pitch',
              ( ['in'], VARIANT, 'pVal' )),
    COMMETHOD([dispid(204), helpstring('Roll angle. Uses Angle Dimension.'), 'propget'], HRESULT, 'Roll',
              ( ['out', 'retval'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD([dispid(204), helpstring('Roll angle. Uses Angle Dimension.'), 'propput'], HRESULT, 'Roll',
              ( ['in'], VARIANT, 'pVal' )),
    COMMETHOD([dispid(205), helpstring('This property is deprecated. Use AssignYPRAngles instead.')], HRESULT, 'SetValues',
              ( ['in'], AgEYPRAnglesSequence, 'Sequence' ),
              ( ['in'], VARIANT, 'Yaw' ),
              ( ['in'], VARIANT, 'Pitch' ),
              ( ['in'], VARIANT, 'Roll' )),
    COMMETHOD([dispid(401), helpstring('Method to change the orientation method to the type specified.')], HRESULT, 'ConvertTo',
              ( ['in'], AgEOrientationType, 'Type' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgOrientation)), 'ppIAgOrientation' )),
    COMMETHOD([dispid(402), helpstring('Returns the orientation method currently being used.'), 'propget'], HRESULT, 'OrientationType',
              ( ['out', 'retval'], POINTER(AgEOrientationType), 'pType' )),
    COMMETHOD([dispid(403), helpstring('Assign a new orientation method.')], HRESULT, 'Assign',
              ( ['in'], POINTER(IAgOrientation), 'pOrientation' )),
    COMMETHOD([dispid(404), helpstring('Helper method to set orientation using the AzEl representation.')], HRESULT, 'AssignAzEl',
              ( ['in'], VARIANT, 'Azimuth' ),
              ( ['in'], VARIANT, 'Elevation' ),
              ( ['in'], AgEAzElAboutBoresight, 'AboutBoresight' )),
    COMMETHOD([dispid(405), helpstring('Helper method to set orientation using the Euler angles representation.')], HRESULT, 'AssignEulerAngles',
              ( ['in'], AgEEulerOrientationSequence, 'Sequence' ),
              ( ['in'], VARIANT, 'A' ),
              ( ['in'], VARIANT, 'B' ),
              ( ['in'], VARIANT, 'C' )),
    COMMETHOD([dispid(406), helpstring('Helper method to set orientation using the Quaternion representation.')], HRESULT, 'AssignQuaternion',
              ( ['in'], c_double, 'QX' ),
              ( ['in'], c_double, 'QY' ),
              ( ['in'], c_double, 'QZ' ),
              ( ['in'], c_double, 'QS' )),
    COMMETHOD([dispid(407), helpstring('Helper method to set orientation using the YPR angles representation.')], HRESULT, 'AssignYPRAngles',
              ( ['in'], AgEYPRAnglesSequence, 'Sequence' ),
              ( ['in'], VARIANT, 'Yaw' ),
              ( ['in'], VARIANT, 'Pitch' ),
              ( ['in'], VARIANT, 'Roll' )),
    COMMETHOD([dispid(408), helpstring('Helper method to get orientation using the AzEl representation.')], HRESULT, 'QueryAzEl',
              ( ['out'], POINTER(VARIANT), 'Azimuth' ),
              ( ['out'], POINTER(VARIANT), 'Elevation' ),
              ( ['out'], POINTER(AgEAzElAboutBoresight), 'AboutBoresight' )),
    COMMETHOD([dispid(409), helpstring('Helper method to get orientation using the Euler angles representation.')], HRESULT, 'QueryEulerAngles',
              ( ['in'], AgEEulerOrientationSequence, 'Sequence' ),
              ( ['out'], POINTER(VARIANT), 'A' ),
              ( ['out'], POINTER(VARIANT), 'B' ),
              ( ['out'], POINTER(VARIANT), 'C' )),
    COMMETHOD([dispid(410), helpstring('Helper method to get orientation using the Quaternion representation.')], HRESULT, 'QueryQuaternion',
              ( ['out'], POINTER(c_double), 'QX' ),
              ( ['out'], POINTER(c_double), 'QY' ),
              ( ['out'], POINTER(c_double), 'QZ' ),
              ( ['out'], POINTER(c_double), 'QS' )),
    COMMETHOD([dispid(411), helpstring('Helper method to get orientation using the YPR angles representation.')], HRESULT, 'QueryYPRAngles',
              ( ['in'], AgEYPRAnglesSequence, 'Sequence' ),
              ( ['out'], POINTER(VARIANT), 'Yaw' ),
              ( ['out'], POINTER(VARIANT), 'Pitch' ),
              ( ['out'], POINTER(VARIANT), 'Roll' )),
    COMMETHOD([dispid(412), helpstring('Returns the AzEl elements as an array.')], HRESULT, 'QueryAzElArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(413), helpstring('Returns the Euler elements as an array.')], HRESULT, 'QueryEulerAnglesArray',
              ( ['in'], AgEEulerOrientationSequence, 'Sequence' ),
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(414), helpstring('Returns the Quaternion elements as an array.')], HRESULT, 'QueryQuaternionArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(415), helpstring('Returns the YPR Angles elements as an array.')], HRESULT, 'QueryYPRAnglesArray',
              ( ['in'], AgEYPRAnglesSequence, 'Sequence' ),
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
]
################################################################
## code template for _IAgOrientationYPRAngles implementation
##class _IAgOrientationYPRAngles_Impl(object):
##    def _get(self):
##        'YPR sequence. Must be set before Yaw,Pitch,Roll values. Otherwise the current Yaw,Pitch,Roll values will be converted to the Sequence specified.'
##        #return pVal
##    def _set(self, pVal):
##        'YPR sequence. Must be set before Yaw,Pitch,Roll values. Otherwise the current Yaw,Pitch,Roll values will be converted to the Sequence specified.'
##    Sequence = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Yaw angle. Uses Angle Dimension.'
##        #return pVal
##    def _set(self, pVal):
##        'Yaw angle. Uses Angle Dimension.'
##    Yaw = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Pitch angle. Uses Angle Dimension.'
##        #return pVal
##    def _set(self, pVal):
##        'Pitch angle. Uses Angle Dimension.'
##    Pitch = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Roll angle. Uses Angle Dimension.'
##        #return pVal
##    def _set(self, pVal):
##        'Roll angle. Uses Angle Dimension.'
##    Roll = property(_get, _set, doc = _set.__doc__)
##
##    def SetValues(self, Sequence, Yaw, Pitch, Roll):
##        'This property is deprecated. Use AssignYPRAngles instead.'
##        #return 
##
##    def ConvertTo(self, Type):
##        'Method to change the orientation method to the type specified.'
##        #return ppIAgOrientation
##
##    @property
##    def OrientationType(self):
##        'Returns the orientation method currently being used.'
##        #return pType
##
##    def Assign(self, pOrientation):
##        'Assign a new orientation method.'
##        #return 
##
##    def AssignAzEl(self, Azimuth, Elevation, AboutBoresight):
##        'Helper method to set orientation using the AzEl representation.'
##        #return 
##
##    def AssignEulerAngles(self, Sequence, A, B, C):
##        'Helper method to set orientation using the Euler angles representation.'
##        #return 
##
##    def AssignQuaternion(self, QX, QY, QZ, QS):
##        'Helper method to set orientation using the Quaternion representation.'
##        #return 
##
##    def AssignYPRAngles(self, Sequence, Yaw, Pitch, Roll):
##        'Helper method to set orientation using the YPR angles representation.'
##        #return 
##
##    def QueryAzEl(self):
##        'Helper method to get orientation using the AzEl representation.'
##        #return Azimuth, Elevation, AboutBoresight
##
##    def QueryEulerAngles(self, Sequence):
##        'Helper method to get orientation using the Euler angles representation.'
##        #return A, B, C
##
##    def QueryQuaternion(self):
##        'Helper method to get orientation using the Quaternion representation.'
##        #return QX, QY, QZ, QS
##
##    def QueryYPRAngles(self, Sequence):
##        'Helper method to get orientation using the YPR angles representation.'
##        #return Yaw, Pitch, Roll
##
##    def QueryAzElArray(self):
##        'Returns the AzEl elements as an array.'
##        #return ppRetVal
##
##    def QueryEulerAnglesArray(self, Sequence):
##        'Returns the Euler elements as an array.'
##        #return ppRetVal
##
##    def QueryQuaternionArray(self):
##        'Returns the Quaternion elements as an array.'
##        #return ppRetVal
##
##    def QueryYPRAnglesArray(self, Sequence):
##        'Returns the YPR Angles elements as an array.'
##        #return ppRetVal
##


# values for enumeration 'AgEOrbitStateType'
eOrbitStateCartesian = 0
eOrbitStateClassical = 1
eOrbitStateEquinoctial = 2
eOrbitStateDelaunay = 3
eOrbitStateSpherical = 4
eOrbitStateMixedSpherical = 5
eOrbitStateGeodetic = 6
AgEOrbitStateType = c_int # enum
class AgOrientationEulerAngles(CoClass):
    'Euler Angles orientation method.'
    _reg_clsid_ = GUID('{60874E2E-71AA-436D-BA64-7665BBAD8A91}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{00DD7BD4-53D5-4870-996B-8ADB8AF904FA}', 1, 0)
class _IAgOrientationEulerAngles(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'The hidden interface for IAgOrientationEulerAngles'
    _iid_ = GUID('{7A137F20-75EA-4356-B9FB-216DC6E82F3B}')
    _idlflags_ = ['hidden', 'dual', 'nonextensible', 'oleautomation']
class IAgOrientationEulerAngles(IAgOrientation):
    _case_insensitive_ = True
    'Interface for Euler Angles orientation method.'
    _iid_ = GUID('{4010ADDB-6500-4A4A-80C6-2C856F3D02F6}')
    _idlflags_ = ['oleautomation']
AgOrientationEulerAngles._com_interfaces_ = [_IAgOrientationEulerAngles, IAgOrientationEulerAngles, IAgOrientation]

IAgOrientationYPRAngles._methods_ = [
    COMMETHOD(['propget', helpstring('YPR sequence. Must be set before Yaw,Pitch,Roll values. Otherwise the current Yaw,Pitch,Roll values will be converted to the Sequence specified.')], HRESULT, 'Sequence',
              ( ['out', 'retval'], POINTER(AgEYPRAnglesSequence), 'pVal' )),
    COMMETHOD(['propput', helpstring('YPR sequence. Must be set before Yaw,Pitch,Roll values. Otherwise the current Yaw,Pitch,Roll values will be converted to the Sequence specified.')], HRESULT, 'Sequence',
              ( ['in'], AgEYPRAnglesSequence, 'pVal' )),
    COMMETHOD(['propget', helpstring('Yaw angle. Uses Angle Dimension.')], HRESULT, 'Yaw',
              ( ['out', 'retval'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD(['propput', helpstring('Yaw angle. Uses Angle Dimension.')], HRESULT, 'Yaw',
              ( ['in'], VARIANT, 'pVal' )),
    COMMETHOD(['propget', helpstring('Pitch angle. Uses Angle Dimension.')], HRESULT, 'Pitch',
              ( ['out', 'retval'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD(['propput', helpstring('Pitch angle. Uses Angle Dimension.')], HRESULT, 'Pitch',
              ( ['in'], VARIANT, 'pVal' )),
    COMMETHOD(['propget', helpstring('Roll angle. Uses Angle Dimension.')], HRESULT, 'Roll',
              ( ['out', 'retval'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD(['propput', helpstring('Roll angle. Uses Angle Dimension.')], HRESULT, 'Roll',
              ( ['in'], VARIANT, 'pVal' )),
    COMMETHOD([helpstring('This property is deprecated. Use AssignYPRAngles instead.')], HRESULT, 'SetValues',
              ( ['in'], AgEYPRAnglesSequence, 'Sequence' ),
              ( ['in'], VARIANT, 'Yaw' ),
              ( ['in'], VARIANT, 'Pitch' ),
              ( ['in'], VARIANT, 'Roll' )),
]
################################################################
## code template for IAgOrientationYPRAngles implementation
##class IAgOrientationYPRAngles_Impl(object):
##    def _get(self):
##        'YPR sequence. Must be set before Yaw,Pitch,Roll values. Otherwise the current Yaw,Pitch,Roll values will be converted to the Sequence specified.'
##        #return pVal
##    def _set(self, pVal):
##        'YPR sequence. Must be set before Yaw,Pitch,Roll values. Otherwise the current Yaw,Pitch,Roll values will be converted to the Sequence specified.'
##    Sequence = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Yaw angle. Uses Angle Dimension.'
##        #return pVal
##    def _set(self, pVal):
##        'Yaw angle. Uses Angle Dimension.'
##    Yaw = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Pitch angle. Uses Angle Dimension.'
##        #return pVal
##    def _set(self, pVal):
##        'Pitch angle. Uses Angle Dimension.'
##    Pitch = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Roll angle. Uses Angle Dimension.'
##        #return pVal
##    def _set(self, pVal):
##        'Roll angle. Uses Angle Dimension.'
##    Roll = property(_get, _set, doc = _set.__doc__)
##
##    def SetValues(self, Sequence, Yaw, Pitch, Roll):
##        'This property is deprecated. Use AssignYPRAngles instead.'
##        #return 
##

class AgPropertyInfo(CoClass):
    'Property Infomation coclass.'
    _reg_clsid_ = GUID('{DDB3E429-10B9-45CE-9D23-E22CFC259C44}')
    _idlflags_ = ['hidden', 'noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{00DD7BD4-53D5-4870-996B-8ADB8AF904FA}', 1, 0)
class IAgPropertyInfo(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    'Property information.'
    _iid_ = GUID('{4C4DE223-5A1C-4427-B47F-9932787FAC00}')
    _idlflags_ = ['oleautomation']
class _IAgPropertyInfo(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'The property information hidden interface.'
    _iid_ = GUID('{42B062AE-DE52-46B6-9971-ABEACE018A22}')
    _idlflags_ = ['hidden', 'dual', 'nonextensible', 'oleautomation']
AgPropertyInfo._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IAgPropertyInfo, _IAgPropertyInfo]


# values for enumeration 'AgEPropertyInfoValueType'
ePropertyInfoValueTypeInt = 0
ePropertyInfoValueTypeReal = 1
ePropertyInfoValueTypeQuantity = 2
ePropertyInfoValueTypeDate = 3
ePropertyInfoValueTypeString = 4
ePropertyInfoValueTypeBool = 5
ePropertyInfoValueTypeInterface = 6
AgEPropertyInfoValueType = c_int # enum
IAgPropertyInfo._methods_ = [
    COMMETHOD(['propget', helpstring('The name of the property.')], HRESULT, 'Name',
              ( ['out', 'retval'], POINTER(BSTR), 'pVal' )),
    COMMETHOD(['propget', helpstring('The type of property.')], HRESULT, 'PropertyType',
              ( ['out', 'retval'], POINTER(AgEPropertyInfoValueType), 'pVal' )),
    COMMETHOD([helpstring('The value of the property. Use PropertyType to determine the type to cast to.')], HRESULT, 'GetValue',
              ( ['out', 'retval'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD([helpstring('The value of the property. Use PropertyType to determine the type to cast to.')], HRESULT, 'SetValue',
              ( ['in'], VARIANT, 'PropertyInfo' )),
    COMMETHOD(['propget', helpstring('Used to determine if the property has a minimum value.')], HRESULT, 'HasMin',
              ( ['out', 'retval'], POINTER(VARIANT_BOOL), 'pVal' )),
    COMMETHOD(['propget', helpstring('Used to determine if the property has a maximum value.')], HRESULT, 'HasMax',
              ( ['out', 'retval'], POINTER(VARIANT_BOOL), 'pVal' )),
    COMMETHOD(['propget', helpstring('The minimum value of this property. Use PropertyType to determine the type to cast to.')], HRESULT, 'Min',
              ( ['out', 'retval'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD(['propget', helpstring('The maximum value of this property. Use PropertyType to determine the type to cast to.')], HRESULT, 'Max',
              ( ['out', 'retval'], POINTER(VARIANT), 'pVal' )),
]
################################################################
## code template for IAgPropertyInfo implementation
##class IAgPropertyInfo_Impl(object):
##    @property
##    def Name(self):
##        'The name of the property.'
##        #return pVal
##
##    @property
##    def PropertyType(self):
##        'The type of property.'
##        #return pVal
##
##    def GetValue(self):
##        'The value of the property. Use PropertyType to determine the type to cast to.'
##        #return pVal
##
##    def SetValue(self, PropertyInfo):
##        'The value of the property. Use PropertyType to determine the type to cast to.'
##        #return 
##
##    @property
##    def HasMin(self):
##        'Used to determine if the property has a minimum value.'
##        #return pVal
##
##    @property
##    def HasMax(self):
##        'Used to determine if the property has a maximum value.'
##        #return pVal
##
##    @property
##    def Min(self):
##        'The minimum value of this property. Use PropertyType to determine the type to cast to.'
##        #return pVal
##
##    @property
##    def Max(self):
##        'The maximum value of this property. Use PropertyType to determine the type to cast to.'
##        #return pVal
##

class AgUnitPrefsDimCollection(CoClass):
    'Object that contains a collection of dimensions.'
    _reg_clsid_ = GUID('{C9E18A07-6566-4922-B0B2-C04502A740FB}')
    _idlflags_ = ['hidden', 'noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{00DD7BD4-53D5-4870-996B-8ADB8AF904FA}', 1, 0)
class IAgUnitPrefsDimCollection(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Provides accesses to the global unit table.'
    _iid_ = GUID('{36069A3D-9A9B-425E-B80B-B604AE70B239}')
    _idlflags_ = ['dual', 'nonextensible', 'oleautomation']
AgUnitPrefsDimCollection._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IAgUnitPrefsDimCollection]

class AgConversionUtility(CoClass):
    'Object that contains a unit conversion utility.'
    _reg_clsid_ = GUID('{73C19457-B614-49BC-ABCD-37795E4837FA}')
    _idlflags_ = ['hidden', 'noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{00DD7BD4-53D5-4870-996B-8ADB8AF904FA}', 1, 0)
class _IAgConversionUtility(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Provides conversion utilities.'
    _iid_ = GUID('{28DFEBD7-EF88-43B1-B3C8-6E2FB1B93641}')
    _idlflags_ = ['hidden', 'dual', 'nonextensible', 'oleautomation']
class IAgConversionUtility(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    'Provides conversion utilities.'
    _iid_ = GUID('{3207E23E-846E-466B-AD46-50BBB1AAF04C}')
    _idlflags_ = ['oleautomation']
AgConversionUtility._com_interfaces_ = [_IAgConversionUtility, IAgConversionUtility]

_IAgOrientationEulerAngles._methods_ = [
    COMMETHOD([dispid(201), helpstring('Euler rotation sequence. Must be set before A,B,C values. Otherwise the current A,B,C values will be converted to the Sequence specified.'), 'propget'], HRESULT, 'Sequence',
              ( ['out', 'retval'], POINTER(AgEEulerOrientationSequence), 'pVal' )),
    COMMETHOD([dispid(201), helpstring('Euler rotation sequence. Must be set before A,B,C values. Otherwise the current A,B,C values will be converted to the Sequence specified.'), 'propput'], HRESULT, 'Sequence',
              ( ['in'], AgEEulerOrientationSequence, 'pVal' )),
    COMMETHOD([dispid(202), helpstring('Euler A angle. Uses Angle Dimension.'), 'propget'], HRESULT, 'A',
              ( ['out', 'retval'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD([dispid(202), helpstring('Euler A angle. Uses Angle Dimension.'), 'propput'], HRESULT, 'A',
              ( ['in'], VARIANT, 'pVal' )),
    COMMETHOD([dispid(203), helpstring('Euler b angle. Uses Angle Dimension.'), 'propget'], HRESULT, 'B',
              ( ['out', 'retval'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD([dispid(203), helpstring('Euler b angle. Uses Angle Dimension.'), 'propput'], HRESULT, 'B',
              ( ['in'], VARIANT, 'pVal' )),
    COMMETHOD([dispid(204), helpstring('Euler C angle. Uses Angle Dimension.'), 'propget'], HRESULT, 'C',
              ( ['out', 'retval'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD([dispid(204), helpstring('Euler C angle. Uses Angle Dimension.'), 'propput'], HRESULT, 'C',
              ( ['in'], VARIANT, 'pVal' )),
    COMMETHOD([dispid(205), helpstring('This property is deprecated. Use AssignEulerAngles instead.')], HRESULT, 'SetValues',
              ( ['in'], AgEEulerOrientationSequence, 'Sequence' ),
              ( ['in'], VARIANT, 'A' ),
              ( ['in'], VARIANT, 'B' ),
              ( ['in'], VARIANT, 'C' )),
    COMMETHOD([dispid(401), helpstring('Method to change the orientation method to the type specified.')], HRESULT, 'ConvertTo',
              ( ['in'], AgEOrientationType, 'Type' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgOrientation)), 'ppIAgOrientation' )),
    COMMETHOD([dispid(402), helpstring('Returns the orientation method currently being used.'), 'propget'], HRESULT, 'OrientationType',
              ( ['out', 'retval'], POINTER(AgEOrientationType), 'pType' )),
    COMMETHOD([dispid(403), helpstring('Assign a new orientation method.')], HRESULT, 'Assign',
              ( ['in'], POINTER(IAgOrientation), 'pOrientation' )),
    COMMETHOD([dispid(404), helpstring('Helper method to set orientation using the AzEl representation.')], HRESULT, 'AssignAzEl',
              ( ['in'], VARIANT, 'Azimuth' ),
              ( ['in'], VARIANT, 'Elevation' ),
              ( ['in'], AgEAzElAboutBoresight, 'AboutBoresight' )),
    COMMETHOD([dispid(405), helpstring('Helper method to set orientation using the Euler angles representation.')], HRESULT, 'AssignEulerAngles',
              ( ['in'], AgEEulerOrientationSequence, 'Sequence' ),
              ( ['in'], VARIANT, 'A' ),
              ( ['in'], VARIANT, 'B' ),
              ( ['in'], VARIANT, 'C' )),
    COMMETHOD([dispid(406), helpstring('Helper method to set orientation using the Quaternion representation.')], HRESULT, 'AssignQuaternion',
              ( ['in'], c_double, 'QX' ),
              ( ['in'], c_double, 'QY' ),
              ( ['in'], c_double, 'QZ' ),
              ( ['in'], c_double, 'QS' )),
    COMMETHOD([dispid(407), helpstring('Helper method to set orientation using the YPR angles representation.')], HRESULT, 'AssignYPRAngles',
              ( ['in'], AgEYPRAnglesSequence, 'Sequence' ),
              ( ['in'], VARIANT, 'Yaw' ),
              ( ['in'], VARIANT, 'Pitch' ),
              ( ['in'], VARIANT, 'Roll' )),
    COMMETHOD([dispid(408), helpstring('Helper method to get orientation using the AzEl representation.')], HRESULT, 'QueryAzEl',
              ( ['out'], POINTER(VARIANT), 'Azimuth' ),
              ( ['out'], POINTER(VARIANT), 'Elevation' ),
              ( ['out'], POINTER(AgEAzElAboutBoresight), 'AboutBoresight' )),
    COMMETHOD([dispid(409), helpstring('Helper method to get orientation using the Euler angles representation.')], HRESULT, 'QueryEulerAngles',
              ( ['in'], AgEEulerOrientationSequence, 'Sequence' ),
              ( ['out'], POINTER(VARIANT), 'A' ),
              ( ['out'], POINTER(VARIANT), 'B' ),
              ( ['out'], POINTER(VARIANT), 'C' )),
    COMMETHOD([dispid(410), helpstring('Helper method to get orientation using the Quaternion representation.')], HRESULT, 'QueryQuaternion',
              ( ['out'], POINTER(c_double), 'QX' ),
              ( ['out'], POINTER(c_double), 'QY' ),
              ( ['out'], POINTER(c_double), 'QZ' ),
              ( ['out'], POINTER(c_double), 'QS' )),
    COMMETHOD([dispid(411), helpstring('Helper method to get orientation using the YPR angles representation.')], HRESULT, 'QueryYPRAngles',
              ( ['in'], AgEYPRAnglesSequence, 'Sequence' ),
              ( ['out'], POINTER(VARIANT), 'Yaw' ),
              ( ['out'], POINTER(VARIANT), 'Pitch' ),
              ( ['out'], POINTER(VARIANT), 'Roll' )),
    COMMETHOD([dispid(412), helpstring('Returns the AzEl elements as an array.')], HRESULT, 'QueryAzElArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(413), helpstring('Returns the Euler elements as an array.')], HRESULT, 'QueryEulerAnglesArray',
              ( ['in'], AgEEulerOrientationSequence, 'Sequence' ),
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(414), helpstring('Returns the Quaternion elements as an array.')], HRESULT, 'QueryQuaternionArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(415), helpstring('Returns the YPR Angles elements as an array.')], HRESULT, 'QueryYPRAnglesArray',
              ( ['in'], AgEYPRAnglesSequence, 'Sequence' ),
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
]
################################################################
## code template for _IAgOrientationEulerAngles implementation
##class _IAgOrientationEulerAngles_Impl(object):
##    def _get(self):
##        'Euler rotation sequence. Must be set before A,B,C values. Otherwise the current A,B,C values will be converted to the Sequence specified.'
##        #return pVal
##    def _set(self, pVal):
##        'Euler rotation sequence. Must be set before A,B,C values. Otherwise the current A,B,C values will be converted to the Sequence specified.'
##    Sequence = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Euler A angle. Uses Angle Dimension.'
##        #return pVal
##    def _set(self, pVal):
##        'Euler A angle. Uses Angle Dimension.'
##    A = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Euler b angle. Uses Angle Dimension.'
##        #return pVal
##    def _set(self, pVal):
##        'Euler b angle. Uses Angle Dimension.'
##    B = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Euler C angle. Uses Angle Dimension.'
##        #return pVal
##    def _set(self, pVal):
##        'Euler C angle. Uses Angle Dimension.'
##    C = property(_get, _set, doc = _set.__doc__)
##
##    def SetValues(self, Sequence, A, B, C):
##        'This property is deprecated. Use AssignEulerAngles instead.'
##        #return 
##
##    def ConvertTo(self, Type):
##        'Method to change the orientation method to the type specified.'
##        #return ppIAgOrientation
##
##    @property
##    def OrientationType(self):
##        'Returns the orientation method currently being used.'
##        #return pType
##
##    def Assign(self, pOrientation):
##        'Assign a new orientation method.'
##        #return 
##
##    def AssignAzEl(self, Azimuth, Elevation, AboutBoresight):
##        'Helper method to set orientation using the AzEl representation.'
##        #return 
##
##    def AssignEulerAngles(self, Sequence, A, B, C):
##        'Helper method to set orientation using the Euler angles representation.'
##        #return 
##
##    def AssignQuaternion(self, QX, QY, QZ, QS):
##        'Helper method to set orientation using the Quaternion representation.'
##        #return 
##
##    def AssignYPRAngles(self, Sequence, Yaw, Pitch, Roll):
##        'Helper method to set orientation using the YPR angles representation.'
##        #return 
##
##    def QueryAzEl(self):
##        'Helper method to get orientation using the AzEl representation.'
##        #return Azimuth, Elevation, AboutBoresight
##
##    def QueryEulerAngles(self, Sequence):
##        'Helper method to get orientation using the Euler angles representation.'
##        #return A, B, C
##
##    def QueryQuaternion(self):
##        'Helper method to get orientation using the Quaternion representation.'
##        #return QX, QY, QZ, QS
##
##    def QueryYPRAngles(self, Sequence):
##        'Helper method to get orientation using the YPR angles representation.'
##        #return Yaw, Pitch, Roll
##
##    def QueryAzElArray(self):
##        'Returns the AzEl elements as an array.'
##        #return ppRetVal
##
##    def QueryEulerAnglesArray(self, Sequence):
##        'Returns the Euler elements as an array.'
##        #return ppRetVal
##
##    def QueryQuaternionArray(self):
##        'Returns the Quaternion elements as an array.'
##        #return ppRetVal
##
##    def QueryYPRAnglesArray(self, Sequence):
##        'Returns the YPR Angles elements as an array.'
##        #return ppRetVal
##

class IAgDirection(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    'Interface to set and retrieve direction options for aligned and constrained vectors.'
    _iid_ = GUID('{46835020-0F55-4981-985F-63CC5743E7E8}')
    _idlflags_ = ['oleautomation']
class IAgOrbitState(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    'Interface to set and retrieve the coordinate type used to specify the orbit state.'
    _iid_ = GUID('{EB00CB53-7306-46E8-AD52-F8C8308E0B07}')
    _idlflags_ = ['oleautomation']
class IAgCartesian3Vector(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    'Represents a cartesian 3-D vector.'
    _iid_ = GUID('{878EF436-3CDC-48B8-B9E7-296F5EF89A97}')
    _idlflags_ = ['oleautomation']
_IAgConversionUtility._methods_ = [
    COMMETHOD([dispid(1), helpstring('Converts the specified quantity value from a given unit to another unit.')], HRESULT, 'ConvertQuantity',
              ( ['in'], BSTR, 'DimensionName' ),
              ( ['in'], BSTR, 'FromUnit' ),
              ( ['in'], BSTR, 'ToUnit' ),
              ( ['in'], c_double, 'Value' ),
              ( ['out', 'retval'], POINTER(c_double), 'pToValue' )),
    COMMETHOD([dispid(2), helpstring('Converts the specified date from a given unit to another unit.')], HRESULT, 'ConvertDate',
              ( ['in'], BSTR, 'FromUnit' ),
              ( ['in'], BSTR, 'ToUnit' ),
              ( ['in'], BSTR, 'FromValue' ),
              ( ['out', 'retval'], POINTER(BSTR), 'pToValue' )),
    COMMETHOD([dispid(3), helpstring('Converts the specified quantity values from a given unit to another unit.')], HRESULT, 'ConvertQuantityArray',
              ( ['in'], BSTR, 'DimensionName' ),
              ( ['in'], BSTR, 'FromUnit' ),
              ( ['in'], BSTR, 'ToUnit' ),
              ( ['in'], POINTER(_midlSAFEARRAY(VARIANT)), 'Values' ),
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppToValue' )),
    COMMETHOD([dispid(4), helpstring('Converts the specified dates from a given unit to another unit.')], HRESULT, 'ConvertDateArray',
              ( ['in'], BSTR, 'FromUnit' ),
              ( ['in'], BSTR, 'ToUnit' ),
              ( ['in'], POINTER(_midlSAFEARRAY(VARIANT)), 'FromValues' ),
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppToValues' )),
    COMMETHOD([dispid(5), helpstring('Creates an IAgQuantity interface with the given dimension, unit and value')], HRESULT, 'NewQuantity',
              ( ['in'], BSTR, 'Dimension' ),
              ( ['in'], BSTR, 'UnitAbbrv' ),
              ( ['in'], c_double, 'Value' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgQuantity)), 'ppQuantity' )),
    COMMETHOD([dispid(6), helpstring('Creates an IAgDate interface with the given unit and value')], HRESULT, 'NewDate',
              ( ['in'], BSTR, 'UnitAbbrv' ),
              ( ['in'], BSTR, 'Value' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgDate)), 'ppDate' )),
    COMMETHOD([dispid(7), helpstring("Creates an IAgPosition interface with earth as it's central body.")], HRESULT, 'NewPositionOnEarth',
              ( ['out', 'retval'], POINTER(POINTER(IAgPosition)), 'ppRetVal' )),
    COMMETHOD([dispid(8), helpstring('Converts the specified position values from a given position type to another position type.')], HRESULT, 'ConvertPositionArray',
              ( ['in'], AgEPositionType, 'PositionType' ),
              ( ['in'], POINTER(_midlSAFEARRAY(VARIANT)), 'PositionArray' ),
              ( ['in'], AgEPositionType, 'ConvertTo' ),
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppOutVal' )),
    COMMETHOD([dispid(9), helpstring('Creates an IAgDirection interface.')], HRESULT, 'NewDirection',
              ( ['out', 'retval'], POINTER(POINTER(IAgDirection)), 'ppRetVal' )),
    COMMETHOD([dispid(11), helpstring('Creates an IAgOrientation interface.')], HRESULT, 'NewOrientation',
              ( ['out', 'retval'], POINTER(POINTER(IAgOrientation)), 'ppRetVal' )),
    COMMETHOD([dispid(13), helpstring("Creates an IAgOrbitState interface with earth as it's central body.")], HRESULT, 'NewOrbitStateOnEarth',
              ( ['out', 'retval'], POINTER(POINTER(IAgOrbitState)), 'ppRetVal' )),
    COMMETHOD([dispid(15), helpstring('Creates an IAgPosition interface using the supplied central body.')], HRESULT, 'NewPositionOnCB',
              ( ['in'], BSTR, 'CentralBodyName' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgPosition)), 'ppRetVal' )),
    COMMETHOD([dispid(16), helpstring('Creates an IAgOrbitState interface using the supplied central body.')], HRESULT, 'NewOrbitStateOnCB',
              ( ['in'], BSTR, 'CentralBodyName' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgOrbitState)), 'ppRetVal' )),
    COMMETHOD([dispid(17), helpstring('Returns a Direction Cosine Matrix (DCM).')], HRESULT, 'QueryDirectionCosineMatrix',
              ( ['in'], POINTER(IAgOrientation), 'InputOrientation' ),
              ( ['out'], POINTER(POINTER(IAgCartesian3Vector)), 'pX' ),
              ( ['out'], POINTER(POINTER(IAgCartesian3Vector)), 'pY' ),
              ( ['out'], POINTER(POINTER(IAgCartesian3Vector)), 'pZ' )),
    COMMETHOD([dispid(18), helpstring('Returns a Direction Cosine Matrix (DCM) as an array.')], HRESULT, 'QueryDirectionCosineMatrixArray',
              ( ['in'], POINTER(IAgOrientation), 'InputOrientation' ),
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(19), helpstring('Creates a cartesian vector.')], HRESULT, 'NewCartesian3Vector',
              ( ['out', 'retval'], POINTER(POINTER(IAgCartesian3Vector)), 'ppRetVal' )),
    COMMETHOD([dispid(20), helpstring('Converts the direction to cartesian vector.')], HRESULT, 'NewCartesian3VectorFromDirection',
              ( ['in'], POINTER(IAgDirection), 'InputDirection' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgCartesian3Vector)), 'ppRetVal' )),
    COMMETHOD([dispid(21), helpstring('Converts the position to cartesian vector.')], HRESULT, 'NewCartesian3VectorFromPosition',
              ( ['in'], POINTER(IAgPosition), 'InputPosition' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgCartesian3Vector)), 'ppRetVal' )),
]
################################################################
## code template for _IAgConversionUtility implementation
##class _IAgConversionUtility_Impl(object):
##    def ConvertQuantity(self, DimensionName, FromUnit, ToUnit, Value):
##        'Converts the specified quantity value from a given unit to another unit.'
##        #return pToValue
##
##    def ConvertDate(self, FromUnit, ToUnit, FromValue):
##        'Converts the specified date from a given unit to another unit.'
##        #return pToValue
##
##    def ConvertQuantityArray(self, DimensionName, FromUnit, ToUnit, Values):
##        'Converts the specified quantity values from a given unit to another unit.'
##        #return ppToValue
##
##    def ConvertDateArray(self, FromUnit, ToUnit, FromValues):
##        'Converts the specified dates from a given unit to another unit.'
##        #return ppToValues
##
##    def NewQuantity(self, Dimension, UnitAbbrv, Value):
##        'Creates an IAgQuantity interface with the given dimension, unit and value'
##        #return ppQuantity
##
##    def NewDate(self, UnitAbbrv, Value):
##        'Creates an IAgDate interface with the given unit and value'
##        #return ppDate
##
##    def NewPositionOnEarth(self):
##        "Creates an IAgPosition interface with earth as it's central body."
##        #return ppRetVal
##
##    def ConvertPositionArray(self, PositionType, PositionArray, ConvertTo):
##        'Converts the specified position values from a given position type to another position type.'
##        #return ppOutVal
##
##    def NewDirection(self):
##        'Creates an IAgDirection interface.'
##        #return ppRetVal
##
##    def NewOrientation(self):
##        'Creates an IAgOrientation interface.'
##        #return ppRetVal
##
##    def NewOrbitStateOnEarth(self):
##        "Creates an IAgOrbitState interface with earth as it's central body."
##        #return ppRetVal
##
##    def NewPositionOnCB(self, CentralBodyName):
##        'Creates an IAgPosition interface using the supplied central body.'
##        #return ppRetVal
##
##    def NewOrbitStateOnCB(self, CentralBodyName):
##        'Creates an IAgOrbitState interface using the supplied central body.'
##        #return ppRetVal
##
##    def QueryDirectionCosineMatrix(self, InputOrientation):
##        'Returns a Direction Cosine Matrix (DCM).'
##        #return pX, pY, pZ
##
##    def QueryDirectionCosineMatrixArray(self, InputOrientation):
##        'Returns a Direction Cosine Matrix (DCM) as an array.'
##        #return ppRetVal
##
##    def NewCartesian3Vector(self):
##        'Creates a cartesian vector.'
##        #return ppRetVal
##
##    def NewCartesian3VectorFromDirection(self, InputDirection):
##        'Converts the direction to cartesian vector.'
##        #return ppRetVal
##
##    def NewCartesian3VectorFromPosition(self, InputPosition):
##        'Converts the position to cartesian vector.'
##        #return ppRetVal
##

IAgOrientationEulerAngles._methods_ = [
    COMMETHOD(['propget', helpstring('Euler rotation sequence. Must be set before A,B,C values. Otherwise the current A,B,C values will be converted to the Sequence specified.')], HRESULT, 'Sequence',
              ( ['out', 'retval'], POINTER(AgEEulerOrientationSequence), 'pVal' )),
    COMMETHOD(['propput', helpstring('Euler rotation sequence. Must be set before A,B,C values. Otherwise the current A,B,C values will be converted to the Sequence specified.')], HRESULT, 'Sequence',
              ( ['in'], AgEEulerOrientationSequence, 'pVal' )),
    COMMETHOD(['propget', helpstring('Euler A angle. Uses Angle Dimension.')], HRESULT, 'A',
              ( ['out', 'retval'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD(['propput', helpstring('Euler A angle. Uses Angle Dimension.')], HRESULT, 'A',
              ( ['in'], VARIANT, 'pVal' )),
    COMMETHOD(['propget', helpstring('Euler b angle. Uses Angle Dimension.')], HRESULT, 'B',
              ( ['out', 'retval'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD(['propput', helpstring('Euler b angle. Uses Angle Dimension.')], HRESULT, 'B',
              ( ['in'], VARIANT, 'pVal' )),
    COMMETHOD(['propget', helpstring('Euler C angle. Uses Angle Dimension.')], HRESULT, 'C',
              ( ['out', 'retval'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD(['propput', helpstring('Euler C angle. Uses Angle Dimension.')], HRESULT, 'C',
              ( ['in'], VARIANT, 'pVal' )),
    COMMETHOD([helpstring('This property is deprecated. Use AssignEulerAngles instead.')], HRESULT, 'SetValues',
              ( ['in'], AgEEulerOrientationSequence, 'Sequence' ),
              ( ['in'], VARIANT, 'A' ),
              ( ['in'], VARIANT, 'B' ),
              ( ['in'], VARIANT, 'C' )),
]
################################################################
## code template for IAgOrientationEulerAngles implementation
##class IAgOrientationEulerAngles_Impl(object):
##    def _get(self):
##        'Euler rotation sequence. Must be set before A,B,C values. Otherwise the current A,B,C values will be converted to the Sequence specified.'
##        #return pVal
##    def _set(self, pVal):
##        'Euler rotation sequence. Must be set before A,B,C values. Otherwise the current A,B,C values will be converted to the Sequence specified.'
##    Sequence = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Euler A angle. Uses Angle Dimension.'
##        #return pVal
##    def _set(self, pVal):
##        'Euler A angle. Uses Angle Dimension.'
##    A = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Euler b angle. Uses Angle Dimension.'
##        #return pVal
##    def _set(self, pVal):
##        'Euler b angle. Uses Angle Dimension.'
##    B = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Euler C angle. Uses Angle Dimension.'
##        #return pVal
##    def _set(self, pVal):
##        'Euler C angle. Uses Angle Dimension.'
##    C = property(_get, _set, doc = _set.__doc__)
##
##    def SetValues(self, Sequence, A, B, C):
##        'This property is deprecated. Use AssignEulerAngles instead.'
##        #return 
##

class _IAgDate(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Provides helper methods for a date.'
    _iid_ = GUID('{CF03B8BD-94E6-4EEA-9471-7D056A1FE168}')
    _idlflags_ = ['hidden', 'dual', 'nonextensible', 'oleautomation']
_IAgDate._methods_ = [
    COMMETHOD([dispid(1), helpstring('Returns the value of the date given the unit.')], HRESULT, 'Format',
              ( ['in'], BSTR, 'Unit' ),
              ( ['out', 'retval'], POINTER(BSTR), 'pValue' )),
    COMMETHOD([dispid(2), helpstring('Sets this date with the given date value and unit type.')], HRESULT, 'SetDate',
              ( ['in'], BSTR, 'Unit' ),
              ( ['in'], BSTR, 'Value' )),
    COMMETHOD([dispid(3), helpstring('The current time in OLE DATE Format.'), 'propget'], HRESULT, 'OLEDate',
              ( ['out', 'retval'], POINTER(c_double), 'pDate' )),
    COMMETHOD([dispid(3), helpstring('The current time in OLE DATE Format.'), 'propput'], HRESULT, 'OLEDate',
              ( ['in'], c_double, 'pDate' )),
    COMMETHOD([dispid(4), helpstring('The Julian Day Number of the date of interest.'), 'propget'], HRESULT, 'WholeDays',
              ( ['out', 'retval'], POINTER(c_int), 'pVal' )),
    COMMETHOD([dispid(4), helpstring('The Julian Day Number of the date of interest.'), 'propput'], HRESULT, 'WholeDays',
              ( ['in'], c_int, 'pVal' )),
    COMMETHOD([dispid(5), helpstring('Contains values between 0.0 and 86400 with the exception of when the date is inside a leap second in which case the SecIntoDay can become as large as 86401.0'), 'propget'], HRESULT, 'SecIntoDay',
              ( ['out', 'retval'], POINTER(c_double), 'pVal' )),
    COMMETHOD([dispid(5), helpstring('Contains values between 0.0 and 86400 with the exception of when the date is inside a leap second in which case the SecIntoDay can become as large as 86401.0'), 'propput'], HRESULT, 'SecIntoDay',
              ( ['in'], c_double, 'pVal' )),
    COMMETHOD([dispid(6), helpstring('The UTC Day Number of the date of interest.'), 'propget'], HRESULT, 'WholeDaysUTC',
              ( ['out', 'retval'], POINTER(c_int), 'pVal' )),
    COMMETHOD([dispid(6), helpstring('The UTC Day Number of the date of interest.'), 'propput'], HRESULT, 'WholeDaysUTC',
              ( ['in'], c_int, 'pVal' )),
    COMMETHOD([dispid(7), helpstring('Contains values between 0.0 and 86400 with the exception of when the date is inside a leap second in which case the SecIntoDay can become as large as 86401.0'), 'propget'], HRESULT, 'SecIntoDayUTC',
              ( ['out', 'retval'], POINTER(c_double), 'pVal' )),
    COMMETHOD([dispid(7), helpstring('Contains values between 0.0 and 86400 with the exception of when the date is inside a leap second in which case the SecIntoDay can become as large as 86401.0'), 'propput'], HRESULT, 'SecIntoDayUTC',
              ( ['in'], c_double, 'pVal' )),
    COMMETHOD([dispid(8), helpstring('Adds the value in the given unit and returns a new date interface.')], HRESULT, 'Add',
              ( ['in'], BSTR, 'Unit' ),
              ( ['in'], c_double, 'Value' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgDate)), 'ppDate' )),
    COMMETHOD([dispid(9), helpstring('Subtracts the value in the given unit and returns a new date interface.')], HRESULT, 'Subtract',
              ( ['in'], BSTR, 'Unit' ),
              ( ['in'], c_double, 'Value' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgDate)), 'ppDate' )),
    COMMETHOD([dispid(10), helpstring('Subtracts the value from the IAgDate interface and returns an IAgQuantity.')], HRESULT, 'Span',
              ( ['in'], POINTER(IAgDate), 'Date' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgQuantity)), 'ppQuantity' )),
]
################################################################
## code template for _IAgDate implementation
##class _IAgDate_Impl(object):
##    def Format(self, Unit):
##        'Returns the value of the date given the unit.'
##        #return pValue
##
##    def SetDate(self, Unit, Value):
##        'Sets this date with the given date value and unit type.'
##        #return 
##
##    def _get(self):
##        'The current time in OLE DATE Format.'
##        #return pDate
##    def _set(self, pDate):
##        'The current time in OLE DATE Format.'
##    OLEDate = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'The Julian Day Number of the date of interest.'
##        #return pVal
##    def _set(self, pVal):
##        'The Julian Day Number of the date of interest.'
##    WholeDays = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Contains values between 0.0 and 86400 with the exception of when the date is inside a leap second in which case the SecIntoDay can become as large as 86401.0'
##        #return pVal
##    def _set(self, pVal):
##        'Contains values between 0.0 and 86400 with the exception of when the date is inside a leap second in which case the SecIntoDay can become as large as 86401.0'
##    SecIntoDay = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'The UTC Day Number of the date of interest.'
##        #return pVal
##    def _set(self, pVal):
##        'The UTC Day Number of the date of interest.'
##    WholeDaysUTC = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Contains values between 0.0 and 86400 with the exception of when the date is inside a leap second in which case the SecIntoDay can become as large as 86401.0'
##        #return pVal
##    def _set(self, pVal):
##        'Contains values between 0.0 and 86400 with the exception of when the date is inside a leap second in which case the SecIntoDay can become as large as 86401.0'
##    SecIntoDayUTC = property(_get, _set, doc = _set.__doc__)
##
##    def Add(self, Unit, Value):
##        'Adds the value in the given unit and returns a new date interface.'
##        #return ppDate
##
##    def Subtract(self, Unit, Value):
##        'Subtracts the value in the given unit and returns a new date interface.'
##        #return ppDate
##
##    def Span(self, Date):
##        'Subtracts the value from the IAgDate interface and returns an IAgQuantity.'
##        #return ppQuantity
##

class IAgDirectionRADec(IAgDirection):
    _case_insensitive_ = True
    'Interface for Spherical direction (Right Ascension and Declination).'
    _iid_ = GUID('{79C99539-649F-4603-8ED1-EBB6A4E4616B}')
    _idlflags_ = ['oleautomation']

# values for enumeration 'AgEDirectionType'
eDirEuler = 0
eDirPR = 1
eDirRADec = 2
eDirXYZ = 3
AgEDirectionType = c_int # enum

# values for enumeration 'AgEEulerDirectionSequence'
e12 = 0
e21 = 1
e31 = 2
e32 = 3
AgEEulerDirectionSequence = c_int # enum

# values for enumeration 'AgEPRSequence'
ePR = 0
AgEPRSequence = c_int # enum
IAgDirection._methods_ = [
    COMMETHOD([helpstring('Method to changes the direction to the type specified.')], HRESULT, 'ConvertTo',
              ( ['in'], AgEDirectionType, 'Type' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgDirection)), 'ppIAgDirection' )),
    COMMETHOD(['propget', helpstring('Returns the type of direction currently being used.')], HRESULT, 'DirectionType',
              ( ['out', 'retval'], POINTER(AgEDirectionType), 'pType' )),
    COMMETHOD([helpstring('Assign a new direction.')], HRESULT, 'Assign',
              ( ['in'], POINTER(IAgDirection), 'pDirection' )),
    COMMETHOD([helpstring('Helper method to set direction using the Euler representation. Params B and C use Angle Dimension.')], HRESULT, 'AssignEuler',
              ( ['in'], VARIANT, 'B' ),
              ( ['in'], VARIANT, 'C' ),
              ( ['in'], AgEEulerDirectionSequence, 'Sequence' )),
    COMMETHOD([helpstring('Helper method to set direction using the Pitch Roll representation. Pitch and Roll use Angle Dimension.')], HRESULT, 'AssignPR',
              ( ['in'], VARIANT, 'Pitch' ),
              ( ['in'], VARIANT, 'Roll' )),
    COMMETHOD([helpstring('Helper method to set direction using the Right Ascension and Declination representation. Param Dec uses Latitude. Param RA uses Longitude.')], HRESULT, 'AssignRADec',
              ( ['in'], VARIANT, 'RA' ),
              ( ['in'], VARIANT, 'Dec' )),
    COMMETHOD([helpstring('Helper method to set direction using the Cartesian representation. Params X, Y and Z are dimensionless.')], HRESULT, 'AssignXYZ',
              ( ['in'], c_double, 'X' ),
              ( ['in'], c_double, 'Y' ),
              ( ['in'], c_double, 'Z' )),
    COMMETHOD([helpstring('Helper method to get direction using the Euler representation. Params B and C use Angle Dimension.')], HRESULT, 'QueryEuler',
              ( ['in'], AgEEulerDirectionSequence, 'Sequence' ),
              ( ['out'], POINTER(VARIANT), 'B' ),
              ( ['out'], POINTER(VARIANT), 'C' )),
    COMMETHOD([helpstring('Helper method to get direction using the Pitch Roll representation. Pitch and Roll use Angle Dimension.')], HRESULT, 'QueryPR',
              ( ['in'], AgEPRSequence, 'Sequence' ),
              ( ['out'], POINTER(VARIANT), 'Pitch' ),
              ( ['out'], POINTER(VARIANT), 'Roll' )),
    COMMETHOD([helpstring('Helper method to get direction using the Right Ascension and Declination representation. Param Dec uses Latitude. Param RA uses Longitude.')], HRESULT, 'QueryRADec',
              ( ['out'], POINTER(VARIANT), 'RA' ),
              ( ['out'], POINTER(VARIANT), 'Dec' )),
    COMMETHOD([helpstring('Helper method to get direction using the Cartesian representation. Params X, Y and Z are dimensionless.')], HRESULT, 'QueryXYZ',
              ( ['out'], POINTER(c_double), 'X' ),
              ( ['out'], POINTER(c_double), 'Y' ),
              ( ['out'], POINTER(c_double), 'Z' )),
    COMMETHOD([helpstring('Returns the Euler elements in an array.')], HRESULT, 'QueryEulerArray',
              ( ['in'], AgEEulerDirectionSequence, 'Sequence' ),
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([helpstring('Returns the PR elements in an array.')], HRESULT, 'QueryPRArray',
              ( ['in'], AgEPRSequence, 'Sequence' ),
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([helpstring('Returns the RADec elements in an array.')], HRESULT, 'QueryRADecArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([helpstring('Returns the XYZ elements in an array.')], HRESULT, 'QueryXYZArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
]
################################################################
## code template for IAgDirection implementation
##class IAgDirection_Impl(object):
##    def ConvertTo(self, Type):
##        'Method to changes the direction to the type specified.'
##        #return ppIAgDirection
##
##    @property
##    def DirectionType(self):
##        'Returns the type of direction currently being used.'
##        #return pType
##
##    def Assign(self, pDirection):
##        'Assign a new direction.'
##        #return 
##
##    def AssignEuler(self, B, C, Sequence):
##        'Helper method to set direction using the Euler representation. Params B and C use Angle Dimension.'
##        #return 
##
##    def AssignPR(self, Pitch, Roll):
##        'Helper method to set direction using the Pitch Roll representation. Pitch and Roll use Angle Dimension.'
##        #return 
##
##    def AssignRADec(self, RA, Dec):
##        'Helper method to set direction using the Right Ascension and Declination representation. Param Dec uses Latitude. Param RA uses Longitude.'
##        #return 
##
##    def AssignXYZ(self, X, Y, Z):
##        'Helper method to set direction using the Cartesian representation. Params X, Y and Z are dimensionless.'
##        #return 
##
##    def QueryEuler(self, Sequence):
##        'Helper method to get direction using the Euler representation. Params B and C use Angle Dimension.'
##        #return B, C
##
##    def QueryPR(self, Sequence):
##        'Helper method to get direction using the Pitch Roll representation. Pitch and Roll use Angle Dimension.'
##        #return Pitch, Roll
##
##    def QueryRADec(self):
##        'Helper method to get direction using the Right Ascension and Declination representation. Param Dec uses Latitude. Param RA uses Longitude.'
##        #return RA, Dec
##
##    def QueryXYZ(self):
##        'Helper method to get direction using the Cartesian representation. Params X, Y and Z are dimensionless.'
##        #return X, Y, Z
##
##    def QueryEulerArray(self, Sequence):
##        'Returns the Euler elements in an array.'
##        #return ppRetVal
##
##    def QueryPRArray(self, Sequence):
##        'Returns the PR elements in an array.'
##        #return ppRetVal
##
##    def QueryRADecArray(self):
##        'Returns the RADec elements in an array.'
##        #return ppRetVal
##
##    def QueryXYZArray(self):
##        'Returns the XYZ elements in an array.'
##        #return ppRetVal
##

IAgDirectionRADec._methods_ = [
    COMMETHOD(['propget', helpstring('Declination: angle above the x-y plane. Uses Latitude Dimension.')], HRESULT, 'Dec',
              ( ['out', 'retval'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD(['propput', helpstring('Declination: angle above the x-y plane. Uses Latitude Dimension.')], HRESULT, 'Dec',
              ( ['in'], VARIANT, 'pVal' )),
    COMMETHOD(['propget', helpstring('Right Ascension: angle in x-y plane from x towards y. Uses Longitude Dimension.')], HRESULT, 'RA',
              ( ['out', 'retval'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD(['propput', helpstring('Right Ascension: angle in x-y plane from x towards y. Uses Longitude Dimension.')], HRESULT, 'RA',
              ( ['in'], VARIANT, 'pVal' )),
    COMMETHOD([helpstring('This property is deprecated. Use AssignRADec instead.')], HRESULT, 'SetValues',
              ( ['in'], VARIANT, 'RA' ),
              ( ['in'], VARIANT, 'Dec' )),
    COMMETHOD(['propget', helpstring('A unitless value that represents magnitude.')], HRESULT, 'Magnitude',
              ( ['out', 'retval'], POINTER(c_double), 'pVal' )),
    COMMETHOD(['propput', helpstring('A unitless value that represents magnitude.')], HRESULT, 'Magnitude',
              ( ['in'], c_double, 'pVal' )),
]
################################################################
## code template for IAgDirectionRADec implementation
##class IAgDirectionRADec_Impl(object):
##    def _get(self):
##        'Declination: angle above the x-y plane. Uses Latitude Dimension.'
##        #return pVal
##    def _set(self, pVal):
##        'Declination: angle above the x-y plane. Uses Latitude Dimension.'
##    Dec = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Right Ascension: angle in x-y plane from x towards y. Uses Longitude Dimension.'
##        #return pVal
##    def _set(self, pVal):
##        'Right Ascension: angle in x-y plane from x towards y. Uses Longitude Dimension.'
##    RA = property(_get, _set, doc = _set.__doc__)
##
##    def SetValues(self, RA, Dec):
##        'This property is deprecated. Use AssignRADec instead.'
##        #return 
##
##    def _get(self):
##        'A unitless value that represents magnitude.'
##        #return pVal
##    def _set(self, pVal):
##        'A unitless value that represents magnitude.'
##    Magnitude = property(_get, _set, doc = _set.__doc__)
##

IAgUnitPrefsDimCollection._methods_ = [
    COMMETHOD([dispid(0), helpstring('Returns an IAgUnitPrefsDim given a Dimension name or an index.'), 'propget'], HRESULT, 'Item',
              ( ['in'], VARIANT, 'IndexOrName' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgUnitPrefsDim)), 'ppAgUnitPrefsDim' )),
    COMMETHOD([dispid(201), helpstring('Returns the number of items in the collection.'), 'propget'], HRESULT, 'Count',
              ( ['out', 'retval'], POINTER(c_int), 'pVal' )),
    COMMETHOD([dispid(202), helpstring('Returns the Current unit for a Dimension.')], HRESULT, 'SetCurrentUnit',
              ( ['in'], BSTR, 'Dimension' ),
              ( ['in'], BSTR, 'UnitAbbrv' )),
    COMMETHOD([dispid(203), helpstring('Returns the Current Unit for a Dimension.')], HRESULT, 'GetCurrentUnitAbbrv',
              ( ['in'], VARIANT, 'IndexOrDimName' ),
              ( ['out', 'retval'], POINTER(BSTR), 'pUnitAbbrv' )),
    COMMETHOD([dispid(204), helpstring('The MissionElapsedTime.'), 'propget'], HRESULT, 'MissionElapsedTime',
              ( ['out', 'retval'], POINTER(VARIANT), 'pMisElapTime' )),
    COMMETHOD([dispid(204), helpstring('The MissionElapsedTime.'), 'propput'], HRESULT, 'MissionElapsedTime',
              ( ['in'], VARIANT, 'pMisElapTime' )),
    COMMETHOD([dispid(205), helpstring('The JulianDateOffset.'), 'propget'], HRESULT, 'JulianDateOffset',
              ( ['out', 'retval'], POINTER(c_double), 'pJDateOffset' )),
    COMMETHOD([dispid(205), helpstring('The JulianDateOffset.'), 'propput'], HRESULT, 'JulianDateOffset',
              ( ['in'], c_double, 'pJDateOffset' )),
    COMMETHOD([dispid(-4), helpstring('Returns a collection of IAgUnitPrefsDim.'), 'propget'], HRESULT, '_NewEnum',
              ( ['out', 'retval'], POINTER(POINTER(IUnknown)), 'ppRetVal' )),
    COMMETHOD([dispid(206), helpstring('Resets the unitpreferences to the Default units')], HRESULT, 'ResetUnits'),
]
################################################################
## code template for IAgUnitPrefsDimCollection implementation
##class IAgUnitPrefsDimCollection_Impl(object):
##    @property
##    def Item(self, IndexOrName):
##        'Returns an IAgUnitPrefsDim given a Dimension name or an index.'
##        #return ppAgUnitPrefsDim
##
##    @property
##    def Count(self):
##        'Returns the number of items in the collection.'
##        #return pVal
##
##    def SetCurrentUnit(self, Dimension, UnitAbbrv):
##        'Returns the Current unit for a Dimension.'
##        #return 
##
##    def GetCurrentUnitAbbrv(self, IndexOrDimName):
##        'Returns the Current Unit for a Dimension.'
##        #return pUnitAbbrv
##
##    def _get(self):
##        'The MissionElapsedTime.'
##        #return pMisElapTime
##    def _set(self, pMisElapTime):
##        'The MissionElapsedTime.'
##    MissionElapsedTime = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'The JulianDateOffset.'
##        #return pJDateOffset
##    def _set(self, pJDateOffset):
##        'The JulianDateOffset.'
##    JulianDateOffset = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def _NewEnum(self):
##        'Returns a collection of IAgUnitPrefsDim.'
##        #return ppRetVal
##
##    def ResetUnits(self):
##        'Resets the unitpreferences to the Default units'
##        #return 
##

class AgDirection(CoClass):
    'Class defining direction options for aligned and constrained vectors.'
    _reg_clsid_ = GUID('{0653A707-4B46-4635-B5E4-E953834C3378}')
    _idlflags_ = ['hidden', 'noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{00DD7BD4-53D5-4870-996B-8ADB8AF904FA}', 1, 0)
class _IAgDirection(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'The hidden interface for IAgDirection'
    _iid_ = GUID('{898E251B-90AC-40A2-908F-62E2598B9EC9}')
    _idlflags_ = ['hidden', 'dual', 'nonextensible', 'oleautomation']
AgDirection._com_interfaces_ = [_IAgDirection, IAgDirection]


# values for enumeration 'AgECoordinateSystem'
eCoordinateSystemUnknown = -1
eCoordinateSystemAlignmentAtEpoch = 0
eCoordinateSystemB1950 = 1
eCoordinateSystemFixed = 2
eCoordinateSystemJ2000 = 3
eCoordinateSystemMeanOfDate = 4
eCoordinateSystemMeanOfEpoch = 5
eCoordinateSystemTEMEOfDate = 6
eCoordinateSystemTEMEOfEpoch = 7
eCoordinateSystemTrueOfDate = 8
eCoordinateSystemTrueOfEpoch = 9
eCoordinateSystemTrueOfRefDate = 10
eCoordinateSystemICRF = 11
eCoordinateSystemMeanEarth = 13
eCoordinateSystemFixedNoLibration = 14
eCoordinateSystemFixedIAU2003 = 15
eCoordinateSystemPrincipalAxes421 = 16
eCoordinateSystemPrincipalAxes403 = 17
eCoordinateSystemInertial = 18
eCoordinateSystemJ2000Ecliptic = 19
eCoordinateSystemTrueEclipticOfDate = 21
eCoordinateSystemPrincipalAxes430 = 22
AgECoordinateSystem = c_int # enum
_IAgDirection._methods_ = [
    COMMETHOD([dispid(201), helpstring('Method to changes the direction to the type specified.')], HRESULT, 'ConvertTo',
              ( ['in'], AgEDirectionType, 'Type' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgDirection)), 'ppRetVal' )),
    COMMETHOD([dispid(202), helpstring('Returns the type of direction currently being used.'), 'propget'], HRESULT, 'DirectionType',
              ( ['out', 'retval'], POINTER(AgEDirectionType), 'pType' )),
    COMMETHOD([dispid(203), helpstring('Assign a new direction.')], HRESULT, 'Assign',
              ( ['in'], POINTER(IAgDirection), 'pDirection' )),
    COMMETHOD([dispid(204), helpstring('Helper method to set direction using the Euler representation')], HRESULT, 'AssignEuler',
              ( ['in'], VARIANT, 'B' ),
              ( ['in'], VARIANT, 'C' ),
              ( ['in'], AgEEulerDirectionSequence, 'Sequence' )),
    COMMETHOD([dispid(205), helpstring('Helper method to set direction using the Pitch Roll representation')], HRESULT, 'AssignPR',
              ( ['in'], VARIANT, 'Pitch' ),
              ( ['in'], VARIANT, 'Roll' )),
    COMMETHOD([dispid(206), helpstring('Helper method to set direction using the Right Ascension and Declination representation')], HRESULT, 'AssignRADec',
              ( ['in'], VARIANT, 'RA' ),
              ( ['in'], VARIANT, 'Dec' )),
    COMMETHOD([dispid(207), helpstring('Helper method to set direction using the Cartesian representation')], HRESULT, 'AssignXYZ',
              ( ['in'], c_double, 'X' ),
              ( ['in'], c_double, 'Y' ),
              ( ['in'], c_double, 'Z' )),
    COMMETHOD([dispid(208), helpstring('Helper method to get direction using the Euler representation. Params B and C use Angle Dimension.')], HRESULT, 'QueryEuler',
              ( ['in'], AgEEulerDirectionSequence, 'Sequence' ),
              ( ['out'], POINTER(VARIANT), 'B' ),
              ( ['out'], POINTER(VARIANT), 'C' )),
    COMMETHOD([dispid(209), helpstring('Helper method to get direction using the Pitch Roll representation. Pitch and Roll use Angle Dimension.')], HRESULT, 'QueryPR',
              ( ['in'], AgEPRSequence, 'Sequence' ),
              ( ['out'], POINTER(VARIANT), 'Pitch' ),
              ( ['out'], POINTER(VARIANT), 'Roll' )),
    COMMETHOD([dispid(210), helpstring('Helper method to get direction using the Right Ascension and Declination representation. Param Dec uses Latitude. Param RA uses Longitude.')], HRESULT, 'QueryRADec',
              ( ['out'], POINTER(VARIANT), 'RA' ),
              ( ['out'], POINTER(VARIANT), 'Dec' )),
    COMMETHOD([dispid(211), helpstring('Helper method to get direction using the Cartesian representation. Params X, Y and Z are dimensionless.')], HRESULT, 'QueryXYZ',
              ( ['out'], POINTER(c_double), 'X' ),
              ( ['out'], POINTER(c_double), 'Y' ),
              ( ['out'], POINTER(c_double), 'Z' )),
    COMMETHOD([dispid(212), helpstring('Returns the Euler elements in an array.')], HRESULT, 'QueryEulerArray',
              ( ['in'], AgEEulerDirectionSequence, 'Sequence' ),
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(213), helpstring('Returns the PR elements in an array.')], HRESULT, 'QueryPRArray',
              ( ['in'], AgEPRSequence, 'Sequence' ),
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(214), helpstring('Returns the RADec elements in an array.')], HRESULT, 'QueryRADecArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(215), helpstring('Returns the XYZ elements in an array.')], HRESULT, 'QueryXYZArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
]
################################################################
## code template for _IAgDirection implementation
##class _IAgDirection_Impl(object):
##    def ConvertTo(self, Type):
##        'Method to changes the direction to the type specified.'
##        #return ppRetVal
##
##    @property
##    def DirectionType(self):
##        'Returns the type of direction currently being used.'
##        #return pType
##
##    def Assign(self, pDirection):
##        'Assign a new direction.'
##        #return 
##
##    def AssignEuler(self, B, C, Sequence):
##        'Helper method to set direction using the Euler representation'
##        #return 
##
##    def AssignPR(self, Pitch, Roll):
##        'Helper method to set direction using the Pitch Roll representation'
##        #return 
##
##    def AssignRADec(self, RA, Dec):
##        'Helper method to set direction using the Right Ascension and Declination representation'
##        #return 
##
##    def AssignXYZ(self, X, Y, Z):
##        'Helper method to set direction using the Cartesian representation'
##        #return 
##
##    def QueryEuler(self, Sequence):
##        'Helper method to get direction using the Euler representation. Params B and C use Angle Dimension.'
##        #return B, C
##
##    def QueryPR(self, Sequence):
##        'Helper method to get direction using the Pitch Roll representation. Pitch and Roll use Angle Dimension.'
##        #return Pitch, Roll
##
##    def QueryRADec(self):
##        'Helper method to get direction using the Right Ascension and Declination representation. Param Dec uses Latitude. Param RA uses Longitude.'
##        #return RA, Dec
##
##    def QueryXYZ(self):
##        'Helper method to get direction using the Cartesian representation. Params X, Y and Z are dimensionless.'
##        #return X, Y, Z
##
##    def QueryEulerArray(self, Sequence):
##        'Returns the Euler elements in an array.'
##        #return ppRetVal
##
##    def QueryPRArray(self, Sequence):
##        'Returns the PR elements in an array.'
##        #return ppRetVal
##
##    def QueryRADecArray(self):
##        'Returns the RADec elements in an array.'
##        #return ppRetVal
##
##    def QueryXYZArray(self):
##        'Returns the XYZ elements in an array.'
##        #return ppRetVal
##

class IAgDirectionEuler(IAgDirection):
    _case_insensitive_ = True
    'Interface for Euler direction sequence.'
    _iid_ = GUID('{2124D808-D63A-43D4-96C2-56ED861AFE53}')
    _idlflags_ = ['oleautomation']
IAgDirectionEuler._methods_ = [
    COMMETHOD(['propget', helpstring('Euler B angle. Uses Angle Dimension.')], HRESULT, 'B',
              ( ['out', 'retval'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD(['propput', helpstring('Euler B angle. Uses Angle Dimension.')], HRESULT, 'B',
              ( ['in'], VARIANT, 'pVal' )),
    COMMETHOD(['propget', helpstring('Euler C angle. Uses Angle Dimension.')], HRESULT, 'C',
              ( ['out', 'retval'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD(['propput', helpstring('Euler C angle. Uses Angle Dimension.')], HRESULT, 'C',
              ( ['in'], VARIANT, 'pVal' )),
    COMMETHOD(['propget', helpstring('Euler direction sequence.  Must be set before B,C values. Otherwise the B,C values will converted to the Sequence specified.')], HRESULT, 'Sequence',
              ( ['out', 'retval'], POINTER(AgEEulerDirectionSequence), 'pVal' )),
    COMMETHOD(['propput', helpstring('Euler direction sequence.  Must be set before B,C values. Otherwise the B,C values will converted to the Sequence specified.')], HRESULT, 'Sequence',
              ( ['in'], AgEEulerDirectionSequence, 'pVal' )),
    COMMETHOD([helpstring('This property is deprecated. Use AssignEuler instead.')], HRESULT, 'SetValues',
              ( ['in'], VARIANT, 'B' ),
              ( ['in'], VARIANT, 'C' ),
              ( ['in'], AgEEulerDirectionSequence, 'Sequence' )),
]
################################################################
## code template for IAgDirectionEuler implementation
##class IAgDirectionEuler_Impl(object):
##    def _get(self):
##        'Euler B angle. Uses Angle Dimension.'
##        #return pVal
##    def _set(self, pVal):
##        'Euler B angle. Uses Angle Dimension.'
##    B = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Euler C angle. Uses Angle Dimension.'
##        #return pVal
##    def _set(self, pVal):
##        'Euler C angle. Uses Angle Dimension.'
##    C = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Euler direction sequence.  Must be set before B,C values. Otherwise the B,C values will converted to the Sequence specified.'
##        #return pVal
##    def _set(self, pVal):
##        'Euler direction sequence.  Must be set before B,C values. Otherwise the B,C values will converted to the Sequence specified.'
##    Sequence = property(_get, _set, doc = _set.__doc__)
##
##    def SetValues(self, B, C, Sequence):
##        'This property is deprecated. Use AssignEuler instead.'
##        #return 
##

class AgPosition(CoClass):
    'The Position class.'
    _reg_clsid_ = GUID('{C20F8369-6C14-44D5-89F6-5DC524173687}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{00DD7BD4-53D5-4870-996B-8ADB8AF904FA}', 1, 0)
class _IAgPosition(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'IAgPosition provides access to the position of the object'
    _iid_ = GUID('{A7DCC4D2-F908-42C2-A0E7-A9853AEE01AB}')
    _idlflags_ = ['hidden', 'dual', 'nonextensible', 'oleautomation']
class IAgLocationData(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    'Base interface IAgLocationData. IAgPosition derives from this interface.'
    _iid_ = GUID('{6E86F9CA-0D23-4F20-AC30-BEBCFB07C679}')
    _idlflags_ = ['oleautomation']
AgPosition._com_interfaces_ = [_IAgPosition, IAgLocationData, IAgPosition]

_IAgPosition._methods_ = [
    COMMETHOD([dispid(201), helpstring('Changes the position coordinates to type specified.')], HRESULT, 'ConvertTo',
              ( ['in'], AgEPositionType, 'Type' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgPosition)), 'ppIAgPosition' )),
    COMMETHOD([dispid(202), helpstring('Gets the type of position currently being used.'), 'propget'], HRESULT, 'PosType',
              ( ['out', 'retval'], POINTER(AgEPositionType), 'pType' )),
    COMMETHOD([dispid(203), helpstring('This assigns the coordinates into the system.')], HRESULT, 'Assign',
              ( ['in'], POINTER(IAgPosition), 'pPosition' )),
    COMMETHOD([dispid(204), helpstring('Helper method to assign the position using the Geocentric representation.')], HRESULT, 'AssignGeocentric',
              ( ['in'], VARIANT, 'Lat' ),
              ( ['in'], VARIANT, 'Lon' ),
              ( ['in'], c_double, 'Alt' )),
    COMMETHOD([dispid(205), helpstring('Helper method to assign the position using the Geodetic representation.')], HRESULT, 'AssignGeodetic',
              ( ['in'], VARIANT, 'Lat' ),
              ( ['in'], VARIANT, 'Lon' ),
              ( ['in'], c_double, 'Alt' )),
    COMMETHOD([dispid(206), helpstring('Helper method to assign the position using the Spherical representation')], HRESULT, 'AssignSpherical',
              ( ['in'], VARIANT, 'Lat' ),
              ( ['in'], VARIANT, 'Lon' ),
              ( ['in'], c_double, 'Radius' )),
    COMMETHOD([dispid(207), helpstring('Helper method to assign the position using the Cylindrical representation')], HRESULT, 'AssignCylindrical',
              ( ['in'], c_double, 'Radius' ),
              ( ['in'], c_double, 'Z' ),
              ( ['in'], VARIANT, 'Lon' )),
    COMMETHOD([dispid(208), helpstring('Helper method to assign the position using the Cartesian representation')], HRESULT, 'AssignCartesian',
              ( ['in'], c_double, 'X' ),
              ( ['in'], c_double, 'Y' ),
              ( ['in'], c_double, 'Z' )),
    COMMETHOD([dispid(209), helpstring('Helper method to assign the position using the Planetocentric representation')], HRESULT, 'AssignPlanetocentric',
              ( ['in'], VARIANT, 'Lat' ),
              ( ['in'], VARIANT, 'Lon' ),
              ( ['in'], c_double, 'Alt' )),
    COMMETHOD([dispid(210), helpstring('Helper method to assign the position using the Planetodetic representation')], HRESULT, 'AssignPlanetodetic',
              ( ['in'], VARIANT, 'Lat' ),
              ( ['in'], VARIANT, 'Lon' ),
              ( ['in'], c_double, 'Alt' )),
    COMMETHOD([dispid(211), helpstring('Helper method to get the position using the Planetocentric representation')], HRESULT, 'QueryPlanetocentric',
              ( ['out'], POINTER(VARIANT), 'Lat' ),
              ( ['out'], POINTER(VARIANT), 'Lon' ),
              ( ['out'], POINTER(c_double), 'Alt' )),
    COMMETHOD([dispid(212), helpstring('Helper method to get the position using the Planetodetic representation')], HRESULT, 'QueryPlanetodetic',
              ( ['out'], POINTER(VARIANT), 'Lat' ),
              ( ['out'], POINTER(VARIANT), 'Lon' ),
              ( ['out'], POINTER(c_double), 'Alt' )),
    COMMETHOD([dispid(213), helpstring('Helper method to get the position using the Spherical representation')], HRESULT, 'QuerySpherical',
              ( ['out'], POINTER(VARIANT), 'Lat' ),
              ( ['out'], POINTER(VARIANT), 'Lon' ),
              ( ['out'], POINTER(c_double), 'Radius' )),
    COMMETHOD([dispid(214), helpstring('Helper method to get the position using the Cylindrical representation')], HRESULT, 'QueryCylindrical',
              ( ['out'], POINTER(c_double), 'Radius' ),
              ( ['out'], POINTER(VARIANT), 'Lon' ),
              ( ['out'], POINTER(c_double), 'Z' )),
    COMMETHOD([dispid(215), helpstring('Helper method to get the position using the Cartesian representation')], HRESULT, 'QueryCartesian',
              ( ['out'], POINTER(c_double), 'X' ),
              ( ['out'], POINTER(c_double), 'Y' ),
              ( ['out'], POINTER(c_double), 'Z' )),
    COMMETHOD([dispid(216), helpstring('Gets the central body.'), 'propget'], HRESULT, 'CentralBodyName',
              ( ['out', 'retval'], POINTER(BSTR), 'pCBName' )),
    COMMETHOD([dispid(217), helpstring('Returns the Planetocentric elements as an array.')], HRESULT, 'QueryPlanetocentricArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(218), helpstring('Returns the Planetodetic elements as an array.')], HRESULT, 'QueryPlanetodeticArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(219), helpstring('Returns the Spherical elements as an array.')], HRESULT, 'QuerySphericalArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(220), helpstring('Returns the Cylindrical elements as an array.')], HRESULT, 'QueryCylindricalArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(221), helpstring('Returns the Cartesian elements as an array.')], HRESULT, 'QueryCartesianArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
]
################################################################
## code template for _IAgPosition implementation
##class _IAgPosition_Impl(object):
##    def ConvertTo(self, Type):
##        'Changes the position coordinates to type specified.'
##        #return ppIAgPosition
##
##    @property
##    def PosType(self):
##        'Gets the type of position currently being used.'
##        #return pType
##
##    def Assign(self, pPosition):
##        'This assigns the coordinates into the system.'
##        #return 
##
##    def AssignGeocentric(self, Lat, Lon, Alt):
##        'Helper method to assign the position using the Geocentric representation.'
##        #return 
##
##    def AssignGeodetic(self, Lat, Lon, Alt):
##        'Helper method to assign the position using the Geodetic representation.'
##        #return 
##
##    def AssignSpherical(self, Lat, Lon, Radius):
##        'Helper method to assign the position using the Spherical representation'
##        #return 
##
##    def AssignCylindrical(self, Radius, Z, Lon):
##        'Helper method to assign the position using the Cylindrical representation'
##        #return 
##
##    def AssignCartesian(self, X, Y, Z):
##        'Helper method to assign the position using the Cartesian representation'
##        #return 
##
##    def AssignPlanetocentric(self, Lat, Lon, Alt):
##        'Helper method to assign the position using the Planetocentric representation'
##        #return 
##
##    def AssignPlanetodetic(self, Lat, Lon, Alt):
##        'Helper method to assign the position using the Planetodetic representation'
##        #return 
##
##    def QueryPlanetocentric(self):
##        'Helper method to get the position using the Planetocentric representation'
##        #return Lat, Lon, Alt
##
##    def QueryPlanetodetic(self):
##        'Helper method to get the position using the Planetodetic representation'
##        #return Lat, Lon, Alt
##
##    def QuerySpherical(self):
##        'Helper method to get the position using the Spherical representation'
##        #return Lat, Lon, Radius
##
##    def QueryCylindrical(self):
##        'Helper method to get the position using the Cylindrical representation'
##        #return Radius, Lon, Z
##
##    def QueryCartesian(self):
##        'Helper method to get the position using the Cartesian representation'
##        #return X, Y, Z
##
##    @property
##    def CentralBodyName(self):
##        'Gets the central body.'
##        #return pCBName
##
##    def QueryPlanetocentricArray(self):
##        'Returns the Planetocentric elements as an array.'
##        #return ppRetVal
##
##    def QueryPlanetodeticArray(self):
##        'Returns the Planetodetic elements as an array.'
##        #return ppRetVal
##
##    def QuerySphericalArray(self):
##        'Returns the Spherical elements as an array.'
##        #return ppRetVal
##
##    def QueryCylindricalArray(self):
##        'Returns the Cylindrical elements as an array.'
##        #return ppRetVal
##
##    def QueryCartesianArray(self):
##        'Returns the Cartesian elements as an array.'
##        #return ppRetVal
##

class _IAgCROrientationOffsetCart(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'The hidden interface for IAgOrientationOffsetCart'
    _iid_ = GUID('{BC2C3C74-2CC0-4D23-A9D1-57B7DB809550}')
    _idlflags_ = ['hidden', 'dual', 'nonextensible', 'oleautomation']
_IAgCROrientationOffsetCart._methods_ = [
    COMMETHOD([dispid(200), helpstring('X coordinate'), 'propget'], HRESULT, 'X',
              ( ['out', 'retval'], POINTER(c_double), 'pRetVal' )),
    COMMETHOD([dispid(200), helpstring('X coordinate'), 'propput'], HRESULT, 'X',
              ( ['in'], c_double, 'pRetVal' )),
    COMMETHOD([dispid(201), helpstring('Y coordinate'), 'propget'], HRESULT, 'Y',
              ( ['out', 'retval'], POINTER(c_double), 'pRetVal' )),
    COMMETHOD([dispid(201), helpstring('Y coordinate'), 'propput'], HRESULT, 'Y',
              ( ['in'], c_double, 'pRetVal' )),
    COMMETHOD([dispid(202), helpstring('Z coordinate'), 'propget'], HRESULT, 'Z',
              ( ['out', 'retval'], POINTER(c_double), 'pRetVal' )),
    COMMETHOD([dispid(202), helpstring('Z coordinate'), 'propput'], HRESULT, 'Z',
              ( ['in'], c_double, 'pRetVal' )),
    COMMETHOD([dispid(203), helpstring('Sets cartesian vector')], HRESULT, 'Set',
              ( ['in'], c_double, 'X' ),
              ( ['in'], c_double, 'Y' ),
              ( ['in'], c_double, 'Z' )),
    COMMETHOD([dispid(204), helpstring('Returns coordinates as an array.')], HRESULT, 'ToArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
]
################################################################
## code template for _IAgCROrientationOffsetCart implementation
##class _IAgCROrientationOffsetCart_Impl(object):
##    def _get(self):
##        'X coordinate'
##        #return pRetVal
##    def _set(self, pRetVal):
##        'X coordinate'
##    X = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Y coordinate'
##        #return pRetVal
##    def _set(self, pRetVal):
##        'Y coordinate'
##    Y = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Z coordinate'
##        #return pRetVal
##    def _set(self, pRetVal):
##        'Z coordinate'
##    Z = property(_get, _set, doc = _set.__doc__)
##
##    def Set(self, X, Y, Z):
##        'Sets cartesian vector'
##        #return 
##
##    def ToArray(self):
##        'Returns coordinates as an array.'
##        #return ppRetVal
##

class AgDate(CoClass):
    'Object that contains a date.'
    _reg_clsid_ = GUID('{8127B5C7-C3FF-4C8A-8512-4877E7B7F41E}')
    _idlflags_ = ['hidden', 'noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{00DD7BD4-53D5-4870-996B-8ADB8AF904FA}', 1, 0)
AgDate._com_interfaces_ = [_IAgDate, IAgDate]

class AgCROrientationOffsetCart(CoClass):
    'Orientation offset cartesian.'
    _reg_clsid_ = GUID('{EA42E642-A1E4-4250-ACE5-CDE816409D84}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{00DD7BD4-53D5-4870-996B-8ADB8AF904FA}', 1, 0)
AgCROrientationOffsetCart._com_interfaces_ = [_IAgCROrientationOffsetCart, IAgCartesian3Vector]

class AgDirectionPR(CoClass):
    'Pitch-Roll (PR) direction sequence.'
    _reg_clsid_ = GUID('{91AA8EA7-F5D5-4F46-A74F-E40D6E95BD72}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{00DD7BD4-53D5-4870-996B-8ADB8AF904FA}', 1, 0)
class _IAgDirectionPR(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'The hidden interface for IAgDirectionPR'
    _iid_ = GUID('{EE9887CA-2E1D-4BE7-A692-825D83ABC412}')
    _idlflags_ = ['hidden', 'dual', 'nonextensible', 'oleautomation']
class IAgDirectionPR(IAgDirection):
    _case_insensitive_ = True
    'Interface for Pitch-Roll (PR) direction sequence.'
    _iid_ = GUID('{B7461818-A389-4E6B-99EC-A77F0DBD41DE}')
    _idlflags_ = ['oleautomation']
AgDirectionPR._com_interfaces_ = [_IAgDirectionPR, IAgDirectionPR, IAgDirection]

_IAgDirectionPR._methods_ = [
    COMMETHOD([dispid(201), helpstring('Pitch angle. Uses Angle Dimension.'), 'propget'], HRESULT, 'Pitch',
              ( ['out', 'retval'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD([dispid(201), helpstring('Pitch angle. Uses Angle Dimension.'), 'propput'], HRESULT, 'Pitch',
              ( ['in'], VARIANT, 'pVal' )),
    COMMETHOD([dispid(202), helpstring('Roll angle. Uses Angle Dimension.'), 'propget'], HRESULT, 'Roll',
              ( ['out', 'retval'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD([dispid(202), helpstring('Roll angle. Uses Angle Dimension.'), 'propput'], HRESULT, 'Roll',
              ( ['in'], VARIANT, 'pVal' )),
    COMMETHOD([dispid(203), helpstring('PR direction sequence. Must be set before Pitch,Roll values. Otherwise the current Pitch,Roll values will be converted to the Sequence specified.'), 'propget'], HRESULT, 'Sequence',
              ( ['out', 'retval'], POINTER(AgEPRSequence), 'pVal' )),
    COMMETHOD([dispid(203), helpstring('PR direction sequence. Must be set before Pitch,Roll values. Otherwise the current Pitch,Roll values will be converted to the Sequence specified.'), 'propput'], HRESULT, 'Sequence',
              ( ['in'], AgEPRSequence, 'pVal' )),
    COMMETHOD([dispid(204), helpstring('This property is deprecated. Use AssignPR instead.')], HRESULT, 'SetValues',
              ( ['in'], VARIANT, 'Pitch' ),
              ( ['in'], VARIANT, 'Roll' )),
    COMMETHOD([dispid(401), helpstring('Method to changes the direction to the type specified.')], HRESULT, 'ConvertTo',
              ( ['in'], AgEDirectionType, 'Type' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgDirection)), 'ppIAgDirection' )),
    COMMETHOD([dispid(402), helpstring('Returns the type of direction currently being used.'), 'propget'], HRESULT, 'DirectionType',
              ( ['out', 'retval'], POINTER(AgEDirectionType), 'pType' )),
    COMMETHOD([dispid(403), helpstring('Assign a new direction.')], HRESULT, 'Assign',
              ( ['in'], POINTER(IAgDirection), 'pDirection' )),
    COMMETHOD([dispid(404), helpstring('Helper method to set direction using the Euler representation. Params B and C use Angle Dimension.')], HRESULT, 'AssignEuler',
              ( ['in'], VARIANT, 'B' ),
              ( ['in'], VARIANT, 'C' ),
              ( ['in'], AgEEulerDirectionSequence, 'Sequence' )),
    COMMETHOD([dispid(405), helpstring('Helper method to set direction using the Pitch Roll representation. Pitch and Roll use Angle Dimension.')], HRESULT, 'AssignPR',
              ( ['in'], VARIANT, 'Pitch' ),
              ( ['in'], VARIANT, 'Roll' )),
    COMMETHOD([dispid(406), helpstring('Helper method to set direction using the Right Ascension and Declination representation. Param Dec uses Latitude. Param RA uses Longitude.')], HRESULT, 'AssignRADec',
              ( ['in'], VARIANT, 'RA' ),
              ( ['in'], VARIANT, 'Dec' )),
    COMMETHOD([dispid(407), helpstring('Helper method to set direction using the Cartesian representation. Params X, Y and Z are dimensionless.')], HRESULT, 'AssignXYZ',
              ( ['in'], c_double, 'X' ),
              ( ['in'], c_double, 'Y' ),
              ( ['in'], c_double, 'Z' )),
    COMMETHOD([dispid(408), helpstring('Helper method to get direction using the Euler representation. Params B and C use Angle Dimension.')], HRESULT, 'QueryEuler',
              ( ['in'], AgEEulerDirectionSequence, 'Sequence' ),
              ( ['out'], POINTER(VARIANT), 'B' ),
              ( ['out'], POINTER(VARIANT), 'C' )),
    COMMETHOD([dispid(409), helpstring('Helper method to get direction using the Pitch Roll representation. Pitch and Roll use Angle Dimension.')], HRESULT, 'QueryPR',
              ( ['in'], AgEPRSequence, 'Sequence' ),
              ( ['out'], POINTER(VARIANT), 'Pitch' ),
              ( ['out'], POINTER(VARIANT), 'Roll' )),
    COMMETHOD([dispid(410), helpstring('Helper method to get direction using the Right Ascension and Declination representation. Param Dec uses Latitude. Param RA uses Longitude.')], HRESULT, 'QueryRADec',
              ( ['out'], POINTER(VARIANT), 'RA' ),
              ( ['out'], POINTER(VARIANT), 'Dec' )),
    COMMETHOD([dispid(411), helpstring('Helper method to get direction using the Cartesian representation. Params X, Y and Z are dimensionless.')], HRESULT, 'QueryXYZ',
              ( ['out'], POINTER(c_double), 'X' ),
              ( ['out'], POINTER(c_double), 'Y' ),
              ( ['out'], POINTER(c_double), 'Z' )),
    COMMETHOD([dispid(412), helpstring('Returns the Euler elements in an array.')], HRESULT, 'QueryEulerArray',
              ( ['in'], AgEEulerDirectionSequence, 'Sequence' ),
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(413), helpstring('Returns the PR elements in an array.')], HRESULT, 'QueryPRArray',
              ( ['in'], AgEPRSequence, 'Sequence' ),
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(414), helpstring('Returns the RADec elements in an array.')], HRESULT, 'QueryRADecArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(415), helpstring('Returns the XYZ elements in an array.')], HRESULT, 'QueryXYZArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
]
################################################################
## code template for _IAgDirectionPR implementation
##class _IAgDirectionPR_Impl(object):
##    def _get(self):
##        'Pitch angle. Uses Angle Dimension.'
##        #return pVal
##    def _set(self, pVal):
##        'Pitch angle. Uses Angle Dimension.'
##    Pitch = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Roll angle. Uses Angle Dimension.'
##        #return pVal
##    def _set(self, pVal):
##        'Roll angle. Uses Angle Dimension.'
##    Roll = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'PR direction sequence. Must be set before Pitch,Roll values. Otherwise the current Pitch,Roll values will be converted to the Sequence specified.'
##        #return pVal
##    def _set(self, pVal):
##        'PR direction sequence. Must be set before Pitch,Roll values. Otherwise the current Pitch,Roll values will be converted to the Sequence specified.'
##    Sequence = property(_get, _set, doc = _set.__doc__)
##
##    def SetValues(self, Pitch, Roll):
##        'This property is deprecated. Use AssignPR instead.'
##        #return 
##
##    def ConvertTo(self, Type):
##        'Method to changes the direction to the type specified.'
##        #return ppIAgDirection
##
##    @property
##    def DirectionType(self):
##        'Returns the type of direction currently being used.'
##        #return pType
##
##    def Assign(self, pDirection):
##        'Assign a new direction.'
##        #return 
##
##    def AssignEuler(self, B, C, Sequence):
##        'Helper method to set direction using the Euler representation. Params B and C use Angle Dimension.'
##        #return 
##
##    def AssignPR(self, Pitch, Roll):
##        'Helper method to set direction using the Pitch Roll representation. Pitch and Roll use Angle Dimension.'
##        #return 
##
##    def AssignRADec(self, RA, Dec):
##        'Helper method to set direction using the Right Ascension and Declination representation. Param Dec uses Latitude. Param RA uses Longitude.'
##        #return 
##
##    def AssignXYZ(self, X, Y, Z):
##        'Helper method to set direction using the Cartesian representation. Params X, Y and Z are dimensionless.'
##        #return 
##
##    def QueryEuler(self, Sequence):
##        'Helper method to get direction using the Euler representation. Params B and C use Angle Dimension.'
##        #return B, C
##
##    def QueryPR(self, Sequence):
##        'Helper method to get direction using the Pitch Roll representation. Pitch and Roll use Angle Dimension.'
##        #return Pitch, Roll
##
##    def QueryRADec(self):
##        'Helper method to get direction using the Right Ascension and Declination representation. Param Dec uses Latitude. Param RA uses Longitude.'
##        #return RA, Dec
##
##    def QueryXYZ(self):
##        'Helper method to get direction using the Cartesian representation. Params X, Y and Z are dimensionless.'
##        #return X, Y, Z
##
##    def QueryEulerArray(self, Sequence):
##        'Returns the Euler elements in an array.'
##        #return ppRetVal
##
##    def QueryPRArray(self, Sequence):
##        'Returns the PR elements in an array.'
##        #return ppRetVal
##
##    def QueryRADecArray(self):
##        'Returns the RADec elements in an array.'
##        #return ppRetVal
##
##    def QueryXYZArray(self):
##        'Returns the XYZ elements in an array.'
##        #return ppRetVal
##

class _IAgCROrientationYPRAngles(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'The hidden interface for IAgOrientationYPRAngles'
    _iid_ = GUID('{1443E1DB-9419-4433-BC7D-9FC7EE394733}')
    _idlflags_ = ['hidden', 'dual', 'nonextensible', 'oleautomation']
_IAgCROrientationYPRAngles._methods_ = [
    COMMETHOD([dispid(201), helpstring('YPR sequence. Must be set before Yaw,Pitch,Roll values. Otherwise the current Yaw,Pitch,Roll values will be converted to the Sequence specified.'), 'propget'], HRESULT, 'Sequence',
              ( ['out', 'retval'], POINTER(AgEYPRAnglesSequence), 'pVal' )),
    COMMETHOD([dispid(201), helpstring('YPR sequence. Must be set before Yaw,Pitch,Roll values. Otherwise the current Yaw,Pitch,Roll values will be converted to the Sequence specified.'), 'propput'], HRESULT, 'Sequence',
              ( ['in'], AgEYPRAnglesSequence, 'pVal' )),
    COMMETHOD([dispid(202), helpstring('Yaw angle. Uses Angle Dimension.'), 'propget'], HRESULT, 'Yaw',
              ( ['out', 'retval'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD([dispid(202), helpstring('Yaw angle. Uses Angle Dimension.'), 'propput'], HRESULT, 'Yaw',
              ( ['in'], VARIANT, 'pVal' )),
    COMMETHOD([dispid(203), helpstring('Pitch angle. Uses Angle Dimension.'), 'propget'], HRESULT, 'Pitch',
              ( ['out', 'retval'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD([dispid(203), helpstring('Pitch angle. Uses Angle Dimension.'), 'propput'], HRESULT, 'Pitch',
              ( ['in'], VARIANT, 'pVal' )),
    COMMETHOD([dispid(204), helpstring('Roll angle. Uses Angle Dimension.'), 'propget'], HRESULT, 'Roll',
              ( ['out', 'retval'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD([dispid(204), helpstring('Roll angle. Uses Angle Dimension.'), 'propput'], HRESULT, 'Roll',
              ( ['in'], VARIANT, 'pVal' )),
    COMMETHOD([dispid(205), helpstring('This property is deprecated. Use AssignYPRAngles instead.')], HRESULT, 'SetValues',
              ( ['in'], AgEYPRAnglesSequence, 'Sequence' ),
              ( ['in'], VARIANT, 'Yaw' ),
              ( ['in'], VARIANT, 'Pitch' ),
              ( ['in'], VARIANT, 'Roll' )),
    COMMETHOD([dispid(401), helpstring('Method to change the orientation method to the type specified.')], HRESULT, 'ConvertTo',
              ( ['in'], AgEOrientationType, 'Type' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgOrientation)), 'ppIAgOrientation' )),
    COMMETHOD([dispid(402), helpstring('Returns the orientation method currently being used.'), 'propget'], HRESULT, 'OrientationType',
              ( ['out', 'retval'], POINTER(AgEOrientationType), 'pType' )),
    COMMETHOD([dispid(403), helpstring('Assign a new orientation method.')], HRESULT, 'Assign',
              ( ['in'], POINTER(IAgOrientation), 'pOrientation' )),
    COMMETHOD([dispid(404), helpstring('Helper method to set orientation using the AzEl representation.')], HRESULT, 'AssignAzEl',
              ( ['in'], VARIANT, 'Azimuth' ),
              ( ['in'], VARIANT, 'Elevation' ),
              ( ['in'], AgEAzElAboutBoresight, 'AboutBoresight' )),
    COMMETHOD([dispid(405), helpstring('Helper method to set orientation using the Euler angles representation.')], HRESULT, 'AssignEulerAngles',
              ( ['in'], AgEEulerOrientationSequence, 'Sequence' ),
              ( ['in'], VARIANT, 'A' ),
              ( ['in'], VARIANT, 'B' ),
              ( ['in'], VARIANT, 'C' )),
    COMMETHOD([dispid(406), helpstring('Helper method to set orientation using the Quaternion representation.')], HRESULT, 'AssignQuaternion',
              ( ['in'], c_double, 'QX' ),
              ( ['in'], c_double, 'QY' ),
              ( ['in'], c_double, 'QZ' ),
              ( ['in'], c_double, 'QS' )),
    COMMETHOD([dispid(407), helpstring('Helper method to set orientation using the YPR angles representation.')], HRESULT, 'AssignYPRAngles',
              ( ['in'], AgEYPRAnglesSequence, 'Sequence' ),
              ( ['in'], VARIANT, 'Yaw' ),
              ( ['in'], VARIANT, 'Pitch' ),
              ( ['in'], VARIANT, 'Roll' )),
    COMMETHOD([dispid(408), helpstring('Helper method to get orientation using the AzEl representation.')], HRESULT, 'QueryAzEl',
              ( ['out'], POINTER(VARIANT), 'Azimuth' ),
              ( ['out'], POINTER(VARIANT), 'Elevation' ),
              ( ['out'], POINTER(AgEAzElAboutBoresight), 'AboutBoresight' )),
    COMMETHOD([dispid(409), helpstring('Helper method to get orientation using the Euler angles representation.')], HRESULT, 'QueryEulerAngles',
              ( ['in'], AgEEulerOrientationSequence, 'Sequence' ),
              ( ['out'], POINTER(VARIANT), 'A' ),
              ( ['out'], POINTER(VARIANT), 'B' ),
              ( ['out'], POINTER(VARIANT), 'C' )),
    COMMETHOD([dispid(410), helpstring('Helper method to get orientation using the Quaternion representation.')], HRESULT, 'QueryQuaternion',
              ( ['out'], POINTER(c_double), 'QX' ),
              ( ['out'], POINTER(c_double), 'QY' ),
              ( ['out'], POINTER(c_double), 'QZ' ),
              ( ['out'], POINTER(c_double), 'QS' )),
    COMMETHOD([dispid(411), helpstring('Helper method to get orientation using the YPR angles representation.')], HRESULT, 'QueryYPRAngles',
              ( ['in'], AgEYPRAnglesSequence, 'Sequence' ),
              ( ['out'], POINTER(VARIANT), 'Yaw' ),
              ( ['out'], POINTER(VARIANT), 'Pitch' ),
              ( ['out'], POINTER(VARIANT), 'Roll' )),
    COMMETHOD([dispid(412), helpstring('Returns the AzEl elements as an array.')], HRESULT, 'QueryAzElArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(413), helpstring('Returns the Euler elements as an array.')], HRESULT, 'QueryEulerAnglesArray',
              ( ['in'], AgEEulerOrientationSequence, 'Sequence' ),
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(414), helpstring('Returns the Quaternion elements as an array.')], HRESULT, 'QueryQuaternionArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(415), helpstring('Returns the YPR Angles elements as an array.')], HRESULT, 'QueryYPRAnglesArray',
              ( ['in'], AgEYPRAnglesSequence, 'Sequence' ),
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(416), helpstring('Gets or sets the location offset cartesian vector.'), 'propget'], HRESULT, 'PositionOffset',
              ( ['out', 'retval'], POINTER(POINTER(IAgCartesian3Vector)), 'ppRetVal' )),
]
################################################################
## code template for _IAgCROrientationYPRAngles implementation
##class _IAgCROrientationYPRAngles_Impl(object):
##    def _get(self):
##        'YPR sequence. Must be set before Yaw,Pitch,Roll values. Otherwise the current Yaw,Pitch,Roll values will be converted to the Sequence specified.'
##        #return pVal
##    def _set(self, pVal):
##        'YPR sequence. Must be set before Yaw,Pitch,Roll values. Otherwise the current Yaw,Pitch,Roll values will be converted to the Sequence specified.'
##    Sequence = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Yaw angle. Uses Angle Dimension.'
##        #return pVal
##    def _set(self, pVal):
##        'Yaw angle. Uses Angle Dimension.'
##    Yaw = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Pitch angle. Uses Angle Dimension.'
##        #return pVal
##    def _set(self, pVal):
##        'Pitch angle. Uses Angle Dimension.'
##    Pitch = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Roll angle. Uses Angle Dimension.'
##        #return pVal
##    def _set(self, pVal):
##        'Roll angle. Uses Angle Dimension.'
##    Roll = property(_get, _set, doc = _set.__doc__)
##
##    def SetValues(self, Sequence, Yaw, Pitch, Roll):
##        'This property is deprecated. Use AssignYPRAngles instead.'
##        #return 
##
##    def ConvertTo(self, Type):
##        'Method to change the orientation method to the type specified.'
##        #return ppIAgOrientation
##
##    @property
##    def OrientationType(self):
##        'Returns the orientation method currently being used.'
##        #return pType
##
##    def Assign(self, pOrientation):
##        'Assign a new orientation method.'
##        #return 
##
##    def AssignAzEl(self, Azimuth, Elevation, AboutBoresight):
##        'Helper method to set orientation using the AzEl representation.'
##        #return 
##
##    def AssignEulerAngles(self, Sequence, A, B, C):
##        'Helper method to set orientation using the Euler angles representation.'
##        #return 
##
##    def AssignQuaternion(self, QX, QY, QZ, QS):
##        'Helper method to set orientation using the Quaternion representation.'
##        #return 
##
##    def AssignYPRAngles(self, Sequence, Yaw, Pitch, Roll):
##        'Helper method to set orientation using the YPR angles representation.'
##        #return 
##
##    def QueryAzEl(self):
##        'Helper method to get orientation using the AzEl representation.'
##        #return Azimuth, Elevation, AboutBoresight
##
##    def QueryEulerAngles(self, Sequence):
##        'Helper method to get orientation using the Euler angles representation.'
##        #return A, B, C
##
##    def QueryQuaternion(self):
##        'Helper method to get orientation using the Quaternion representation.'
##        #return QX, QY, QZ, QS
##
##    def QueryYPRAngles(self, Sequence):
##        'Helper method to get orientation using the YPR angles representation.'
##        #return Yaw, Pitch, Roll
##
##    def QueryAzElArray(self):
##        'Returns the AzEl elements as an array.'
##        #return ppRetVal
##
##    def QueryEulerAnglesArray(self, Sequence):
##        'Returns the Euler elements as an array.'
##        #return ppRetVal
##
##    def QueryQuaternionArray(self):
##        'Returns the Quaternion elements as an array.'
##        #return ppRetVal
##
##    def QueryYPRAnglesArray(self, Sequence):
##        'Returns the YPR Angles elements as an array.'
##        #return ppRetVal
##
##    @property
##    def PositionOffset(self):
##        'Gets or sets the location offset cartesian vector.'
##        #return ppRetVal
##

class AgCROrientationYPRAngles(CoClass):
    'Yaw-Pitch Roll (YPR) Angles orientation system.'
    _reg_clsid_ = GUID('{2FCD1835-63EE-4D08-A5C3-D92EAEC915F2}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{00DD7BD4-53D5-4870-996B-8ADB8AF904FA}', 1, 0)
class IAgOrientationPositionOffset(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    'Interface for defining the orientation origin position offset relative to the parent object.'
    _iid_ = GUID('{B892E634-A18C-42DA-AF35-D1C92793A3DD}')
    _idlflags_ = ['oleautomation']
AgCROrientationYPRAngles._com_interfaces_ = [_IAgCROrientationYPRAngles, IAgOrientationYPRAngles, IAgOrientation, IAgOrientationPositionOffset]

IAgQuantity._methods_ = [
    COMMETHOD(['propget', helpstring('Gets the name of the dimension')], HRESULT, 'Dimension',
              ( ['out', 'retval'], POINTER(BSTR), 'pDimName' )),
    COMMETHOD(['propget', helpstring('The current Unit abbreviation.')], HRESULT, 'Unit',
              ( ['out', 'retval'], POINTER(BSTR), 'pUnitAbbrv' )),
    COMMETHOD([helpstring('Changes the value in this quantity to the specified unit.')], HRESULT, 'ConvertToUnit',
              ( ['in'], BSTR, 'UnitAbbrv' )),
    COMMETHOD(['propget', helpstring('The current value.')], HRESULT, 'Value',
              ( ['out', 'retval'], POINTER(c_double), 'pValue' )),
    COMMETHOD(['propput', helpstring('The current value.')], HRESULT, 'Value',
              ( ['in'], c_double, 'pValue' )),
    COMMETHOD([helpstring('Adds the value from the IAgQuantity interface to this interface. Returns a new IAgQuantity. The dimensions must be similar.')], HRESULT, 'Add',
              ( ['in'], POINTER(IAgQuantity), 'Quantity' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgQuantity)), 'ppQuantity' )),
    COMMETHOD([helpstring('Subtracts the value from the IAgQuantity interface to this interface. Returns a new IAgQuantity. The dimensions must be similar.')], HRESULT, 'Subtract',
              ( ['in'], POINTER(IAgQuantity), 'Quantity' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgQuantity)), 'ppQuantity' )),
    COMMETHOD([helpstring('Multiplies the value from the IAgQuantity interface to this interface. Returns a new IAgQuantity. The dimensions must be similar.')], HRESULT, 'MultiplyQty',
              ( ['in'], POINTER(IAgQuantity), 'Quantity' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgQuantity)), 'ppQuantity' )),
    COMMETHOD([helpstring('Divides the value from the IAgQuantity interface to this interface. The dimensions must be similar.')], HRESULT, 'DivideQty',
              ( ['in'], POINTER(IAgQuantity), 'Quantity' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgQuantity)), 'ppQuantity' )),
]
################################################################
## code template for IAgQuantity implementation
##class IAgQuantity_Impl(object):
##    @property
##    def Dimension(self):
##        'Gets the name of the dimension'
##        #return pDimName
##
##    @property
##    def Unit(self):
##        'The current Unit abbreviation.'
##        #return pUnitAbbrv
##
##    def ConvertToUnit(self, UnitAbbrv):
##        'Changes the value in this quantity to the specified unit.'
##        #return 
##
##    def _get(self):
##        'The current value.'
##        #return pValue
##    def _set(self, pValue):
##        'The current value.'
##    Value = property(_get, _set, doc = _set.__doc__)
##
##    def Add(self, Quantity):
##        'Adds the value from the IAgQuantity interface to this interface. Returns a new IAgQuantity. The dimensions must be similar.'
##        #return ppQuantity
##
##    def Subtract(self, Quantity):
##        'Subtracts the value from the IAgQuantity interface to this interface. Returns a new IAgQuantity. The dimensions must be similar.'
##        #return ppQuantity
##
##    def MultiplyQty(self, Quantity):
##        'Multiplies the value from the IAgQuantity interface to this interface. Returns a new IAgQuantity. The dimensions must be similar.'
##        #return ppQuantity
##
##    def DivideQty(self, Quantity):
##        'Divides the value from the IAgQuantity interface to this interface. The dimensions must be similar.'
##        #return ppQuantity
##

class _IAgDirectionEuler(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'The hidden interface for IAgDirectionEuler'
    _iid_ = GUID('{35C5FF47-87E1-4175-95EB-439CAB73BD9D}')
    _idlflags_ = ['hidden', 'dual', 'nonextensible', 'oleautomation']
_IAgDirectionEuler._methods_ = [
    COMMETHOD([dispid(201), helpstring('Euler B angle. Uses Angle Dimension.'), 'propget'], HRESULT, 'B',
              ( ['out', 'retval'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD([dispid(201), helpstring('Euler B angle. Uses Angle Dimension.'), 'propput'], HRESULT, 'B',
              ( ['in'], VARIANT, 'pVal' )),
    COMMETHOD([dispid(202), helpstring('Euler C angle. Uses Angle Dimension.'), 'propget'], HRESULT, 'C',
              ( ['out', 'retval'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD([dispid(202), helpstring('Euler C angle. Uses Angle Dimension.'), 'propput'], HRESULT, 'C',
              ( ['in'], VARIANT, 'pVal' )),
    COMMETHOD([dispid(203), helpstring('Euler direction sequence. Must be set before B,C values. Otherwise the B,C values will converted to the Sequence specified.'), 'propget'], HRESULT, 'Sequence',
              ( ['out', 'retval'], POINTER(AgEEulerDirectionSequence), 'pVal' )),
    COMMETHOD([dispid(203), helpstring('Euler direction sequence. Must be set before B,C values. Otherwise the B,C values will converted to the Sequence specified.'), 'propput'], HRESULT, 'Sequence',
              ( ['in'], AgEEulerDirectionSequence, 'pVal' )),
    COMMETHOD([dispid(204), helpstring('This property is deprecated. Use AssignEuler instead.')], HRESULT, 'SetValues',
              ( ['in'], VARIANT, 'B' ),
              ( ['in'], VARIANT, 'C' ),
              ( ['in'], AgEEulerDirectionSequence, 'Sequence' )),
    COMMETHOD([dispid(401), helpstring('Method to changes the direction to the type specified.')], HRESULT, 'ConvertTo',
              ( ['in'], AgEDirectionType, 'Type' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgDirection)), 'ppIAgDirection' )),
    COMMETHOD([dispid(402), helpstring('Returns the type of direction currently being used.'), 'propget'], HRESULT, 'DirectionType',
              ( ['out', 'retval'], POINTER(AgEDirectionType), 'pType' )),
    COMMETHOD([dispid(403), helpstring('Assign a new direction.')], HRESULT, 'Assign',
              ( ['in'], POINTER(IAgDirection), 'pDirection' )),
    COMMETHOD([dispid(404), helpstring('Helper method to set direction using the Euler representation. Params B and C use Angle Dimension.')], HRESULT, 'AssignEuler',
              ( ['in'], VARIANT, 'B' ),
              ( ['in'], VARIANT, 'C' ),
              ( ['in'], AgEEulerDirectionSequence, 'Sequence' )),
    COMMETHOD([dispid(405), helpstring('Helper method to set direction using the Pitch Roll representation. Pitch and Roll use Angle Dimension.')], HRESULT, 'AssignPR',
              ( ['in'], VARIANT, 'Pitch' ),
              ( ['in'], VARIANT, 'Roll' )),
    COMMETHOD([dispid(406), helpstring('Helper method to set direction using the Right Ascension and Declination representation. Param Dec uses Latitude. Param RA uses Longitude.')], HRESULT, 'AssignRADec',
              ( ['in'], VARIANT, 'RA' ),
              ( ['in'], VARIANT, 'Dec' )),
    COMMETHOD([dispid(407), helpstring('Helper method to set direction using the Cartesian representation. Params X, Y and Z are dimensionless.')], HRESULT, 'AssignXYZ',
              ( ['in'], c_double, 'X' ),
              ( ['in'], c_double, 'Y' ),
              ( ['in'], c_double, 'Z' )),
    COMMETHOD([dispid(408), helpstring('Helper method to get direction using the Euler representation. Params B and C use Angle Dimension.')], HRESULT, 'QueryEuler',
              ( ['in'], AgEEulerDirectionSequence, 'Sequence' ),
              ( ['out'], POINTER(VARIANT), 'B' ),
              ( ['out'], POINTER(VARIANT), 'C' )),
    COMMETHOD([dispid(409), helpstring('Helper method to get direction using the Pitch Roll representation. Pitch and Roll use Angle Dimension.')], HRESULT, 'QueryPR',
              ( ['in'], AgEPRSequence, 'Sequence' ),
              ( ['out'], POINTER(VARIANT), 'Pitch' ),
              ( ['out'], POINTER(VARIANT), 'Roll' )),
    COMMETHOD([dispid(410), helpstring('Helper method to get direction using the Right Ascension and Declination representation. Param Dec uses Latitude. Param RA uses Longitude.')], HRESULT, 'QueryRADec',
              ( ['out'], POINTER(VARIANT), 'RA' ),
              ( ['out'], POINTER(VARIANT), 'Dec' )),
    COMMETHOD([dispid(411), helpstring('Helper method to get direction using the Cartesian representation. Params X, Y and Z are dimensionless.')], HRESULT, 'QueryXYZ',
              ( ['out'], POINTER(c_double), 'X' ),
              ( ['out'], POINTER(c_double), 'Y' ),
              ( ['out'], POINTER(c_double), 'Z' )),
    COMMETHOD([dispid(412), helpstring('Returns the Euler elements in an array.')], HRESULT, 'QueryEulerArray',
              ( ['in'], AgEEulerDirectionSequence, 'Sequence' ),
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(413), helpstring('Returns the PR elements in an array.')], HRESULT, 'QueryPRArray',
              ( ['in'], AgEPRSequence, 'Sequence' ),
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(414), helpstring('Returns the RADec elements in an array.')], HRESULT, 'QueryRADecArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(415), helpstring('Returns the XYZ elements in an array.')], HRESULT, 'QueryXYZArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
]
################################################################
## code template for _IAgDirectionEuler implementation
##class _IAgDirectionEuler_Impl(object):
##    def _get(self):
##        'Euler B angle. Uses Angle Dimension.'
##        #return pVal
##    def _set(self, pVal):
##        'Euler B angle. Uses Angle Dimension.'
##    B = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Euler C angle. Uses Angle Dimension.'
##        #return pVal
##    def _set(self, pVal):
##        'Euler C angle. Uses Angle Dimension.'
##    C = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Euler direction sequence. Must be set before B,C values. Otherwise the B,C values will converted to the Sequence specified.'
##        #return pVal
##    def _set(self, pVal):
##        'Euler direction sequence. Must be set before B,C values. Otherwise the B,C values will converted to the Sequence specified.'
##    Sequence = property(_get, _set, doc = _set.__doc__)
##
##    def SetValues(self, B, C, Sequence):
##        'This property is deprecated. Use AssignEuler instead.'
##        #return 
##
##    def ConvertTo(self, Type):
##        'Method to changes the direction to the type specified.'
##        #return ppIAgDirection
##
##    @property
##    def DirectionType(self):
##        'Returns the type of direction currently being used.'
##        #return pType
##
##    def Assign(self, pDirection):
##        'Assign a new direction.'
##        #return 
##
##    def AssignEuler(self, B, C, Sequence):
##        'Helper method to set direction using the Euler representation. Params B and C use Angle Dimension.'
##        #return 
##
##    def AssignPR(self, Pitch, Roll):
##        'Helper method to set direction using the Pitch Roll representation. Pitch and Roll use Angle Dimension.'
##        #return 
##
##    def AssignRADec(self, RA, Dec):
##        'Helper method to set direction using the Right Ascension and Declination representation. Param Dec uses Latitude. Param RA uses Longitude.'
##        #return 
##
##    def AssignXYZ(self, X, Y, Z):
##        'Helper method to set direction using the Cartesian representation. Params X, Y and Z are dimensionless.'
##        #return 
##
##    def QueryEuler(self, Sequence):
##        'Helper method to get direction using the Euler representation. Params B and C use Angle Dimension.'
##        #return B, C
##
##    def QueryPR(self, Sequence):
##        'Helper method to get direction using the Pitch Roll representation. Pitch and Roll use Angle Dimension.'
##        #return Pitch, Roll
##
##    def QueryRADec(self):
##        'Helper method to get direction using the Right Ascension and Declination representation. Param Dec uses Latitude. Param RA uses Longitude.'
##        #return RA, Dec
##
##    def QueryXYZ(self):
##        'Helper method to get direction using the Cartesian representation. Params X, Y and Z are dimensionless.'
##        #return X, Y, Z
##
##    def QueryEulerArray(self, Sequence):
##        'Returns the Euler elements in an array.'
##        #return ppRetVal
##
##    def QueryPRArray(self, Sequence):
##        'Returns the PR elements in an array.'
##        #return ppRetVal
##
##    def QueryRADecArray(self):
##        'Returns the RADec elements in an array.'
##        #return ppRetVal
##
##    def QueryXYZArray(self):
##        'Returns the XYZ elements in an array.'
##        #return ppRetVal
##

class AgRuntimeTypeInfo(CoClass):
    'Runtime Type info coclass.'
    _reg_clsid_ = GUID('{95E84296-D519-44D5-AE58-C79ACEBD74E3}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{00DD7BD4-53D5-4870-996B-8ADB8AF904FA}', 1, 0)
class _IAgRuntimeTypeInfo(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'The component browser hidden interface.'
    _iid_ = GUID('{40815573-34A0-40D2-BF62-7537CB1302E6}')
    _idlflags_ = ['hidden', 'dual', 'nonextensible', 'oleautomation']
class IAgRuntimeTypeInfo(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    'Interface used to retrieve the properties at runtime.'
    _iid_ = GUID('{392131C9-C7DA-4E35-A95A-4C030CE31357}')
    _idlflags_ = ['oleautomation']
AgRuntimeTypeInfo._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, _IAgRuntimeTypeInfo, IAgRuntimeTypeInfo]

class AgDirectionEuler(CoClass):
    'Euler direction sequence.'
    _reg_clsid_ = GUID('{92BD6C6F-ACAE-4057-98D7-45EC4A0E733D}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{00DD7BD4-53D5-4870-996B-8ADB8AF904FA}', 1, 0)
AgDirectionEuler._com_interfaces_ = [_IAgDirectionEuler, IAgDirectionEuler, IAgDirection]

IAgPropertyInfoCollection._methods_ = [
    COMMETHOD([dispid(0), helpstring('Allows the user to iterate through the properties.'), 'propget'], HRESULT, 'Item',
              ( ['in'], VARIANT, 'IndexOrName' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgPropertyInfo)), 'ppVal' )),
    COMMETHOD([dispid(-4), helpstring('Enumerates through the properties.'), 'propget'], HRESULT, '_NewEnum',
              ( ['out', 'retval'], POINTER(POINTER(IUnknown)), 'ppVal' )),
    COMMETHOD([dispid(1), helpstring('The number of properties available.'), 'propget'], HRESULT, 'Count',
              ( ['out', 'retval'], POINTER(c_int), 'pVal' )),
]
################################################################
## code template for IAgPropertyInfoCollection implementation
##class IAgPropertyInfoCollection_Impl(object):
##    @property
##    def Item(self, IndexOrName):
##        'Allows the user to iterate through the properties.'
##        #return ppVal
##
##    @property
##    def _NewEnum(self):
##        'Enumerates through the properties.'
##        #return ppVal
##
##    @property
##    def Count(self):
##        'The number of properties available.'
##        #return pVal
##

_IAgRuntimeTypeInfo._methods_ = [
    COMMETHOD([dispid(1), helpstring('The collection of properties.'), 'propget'], HRESULT, 'Properties',
              ( ['out', 'retval'], POINTER(POINTER(IAgPropertyInfoCollection)), 'ppRetVal' )),
    COMMETHOD([dispid(2), helpstring('Determines if the interface is a collection.'), 'propget'], HRESULT, 'IsCollection',
              ( ['out', 'retval'], POINTER(VARIANT_BOOL), 'pVal' )),
    COMMETHOD([dispid(3), helpstring('If the interface is a collection, returns the collection count.'), 'propget'], HRESULT, 'Count',
              ( ['out', 'retval'], POINTER(c_int), 'pVal' )),
    COMMETHOD([dispid(4), helpstring('Returns the property of the collection at the given index.')], HRESULT, 'GetItem',
              ( ['in'], c_int, 'Index' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgPropertyInfo)), 'ppVal' )),
]
################################################################
## code template for _IAgRuntimeTypeInfo implementation
##class _IAgRuntimeTypeInfo_Impl(object):
##    @property
##    def Properties(self):
##        'The collection of properties.'
##        #return ppRetVal
##
##    @property
##    def IsCollection(self):
##        'Determines if the interface is a collection.'
##        #return pVal
##
##    @property
##    def Count(self):
##        'If the interface is a collection, returns the collection count.'
##        #return pVal
##
##    def GetItem(self, Index):
##        'Returns the property of the collection at the given index.'
##        #return ppVal
##

_IAgPropertyInfo._methods_ = [
    COMMETHOD([dispid(1), helpstring('The name of the property.'), 'propget'], HRESULT, 'Name',
              ( ['out', 'retval'], POINTER(BSTR), 'pVal' )),
    COMMETHOD([dispid(2), helpstring('The type of property.'), 'propget'], HRESULT, 'PropertyType',
              ( ['out', 'retval'], POINTER(AgEPropertyInfoValueType), 'pVal' )),
    COMMETHOD([dispid(3), helpstring('The value of the property. Use PropertyType to determine the type to cast to.')], HRESULT, 'GetValue',
              ( ['out', 'retval'], POINTER(VARIANT), 'pVVal' )),
    COMMETHOD([dispid(4), helpstring('The value of the property. Use PropertyType to determine the type to cast to.')], HRESULT, 'SetValue',
              ( ['in'], VARIANT, 'PropertyInfo' )),
    COMMETHOD([dispid(5), helpstring('Used to determine if the property has a minimum value.'), 'propget'], HRESULT, 'HasMin',
              ( ['out', 'retval'], POINTER(VARIANT_BOOL), 'pVal' )),
    COMMETHOD([dispid(6), helpstring('Used to determine if the property has a maximum value.'), 'propget'], HRESULT, 'HasMax',
              ( ['out', 'retval'], POINTER(VARIANT_BOOL), 'pVal' )),
    COMMETHOD([dispid(7), helpstring('The minimum value of this property. Use PropertyType to determine the type to cast to.'), 'propget'], HRESULT, 'Min',
              ( ['out', 'retval'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD([dispid(8), helpstring('The maximum value of this property. Use PropertyType to determine the type to cast to.'), 'propget'], HRESULT, 'Max',
              ( ['out', 'retval'], POINTER(VARIANT), 'pVal' )),
]
################################################################
## code template for _IAgPropertyInfo implementation
##class _IAgPropertyInfo_Impl(object):
##    @property
##    def Name(self):
##        'The name of the property.'
##        #return pVal
##
##    @property
##    def PropertyType(self):
##        'The type of property.'
##        #return pVal
##
##    def GetValue(self):
##        'The value of the property. Use PropertyType to determine the type to cast to.'
##        #return pVVal
##
##    def SetValue(self, PropertyInfo):
##        'The value of the property. Use PropertyType to determine the type to cast to.'
##        #return 
##
##    @property
##    def HasMin(self):
##        'Used to determine if the property has a minimum value.'
##        #return pVal
##
##    @property
##    def HasMax(self):
##        'Used to determine if the property has a maximum value.'
##        #return pVal
##
##    @property
##    def Min(self):
##        'The minimum value of this property. Use PropertyType to determine the type to cast to.'
##        #return pVal
##
##    @property
##    def Max(self):
##        'The maximum value of this property. Use PropertyType to determine the type to cast to.'
##        #return pVal
##

class IAgPlanetodetic(IAgPosition):
    _case_insensitive_ = True
    'IAgPlanetodetic sets the position using Planetodetic properties.'
    _iid_ = GUID('{4F49C748-FE5A-4B00-B47B-173E5F445411}')
    _idlflags_ = ['oleautomation']
IAgPlanetodetic._methods_ = [
    COMMETHOD(['propget', helpstring('Latitude. Uses Latitude Dimension.')], HRESULT, 'Lat',
              ( ['out', 'retval'], POINTER(VARIANT), 'pLat' )),
    COMMETHOD(['propput', helpstring('Latitude. Uses Latitude Dimension.')], HRESULT, 'Lat',
              ( ['in'], VARIANT, 'pLat' )),
    COMMETHOD(['propget', helpstring('Longitude. Uses Longitude Dimension.')], HRESULT, 'Lon',
              ( ['out', 'retval'], POINTER(VARIANT), 'pLon' )),
    COMMETHOD(['propput', helpstring('Longitude. Uses Longitude Dimension.')], HRESULT, 'Lon',
              ( ['in'], VARIANT, 'pLon' )),
    COMMETHOD(['propget', helpstring('Altitude. Dimension depends on context.')], HRESULT, 'Alt',
              ( ['out', 'retval'], POINTER(c_double), 'pAlt' )),
    COMMETHOD(['propput', helpstring('Altitude. Dimension depends on context.')], HRESULT, 'Alt',
              ( ['in'], c_double, 'pAlt' )),
]
################################################################
## code template for IAgPlanetodetic implementation
##class IAgPlanetodetic_Impl(object):
##    def _get(self):
##        'Latitude. Uses Latitude Dimension.'
##        #return pLat
##    def _set(self, pLat):
##        'Latitude. Uses Latitude Dimension.'
##    Lat = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Longitude. Uses Longitude Dimension.'
##        #return pLon
##    def _set(self, pLon):
##        'Longitude. Uses Longitude Dimension.'
##    Lon = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Altitude. Dimension depends on context.'
##        #return pAlt
##    def _set(self, pAlt):
##        'Altitude. Dimension depends on context.'
##    Alt = property(_get, _set, doc = _set.__doc__)
##

class _IAgPlanetodetic(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'IAgPlanetodetic sets the position using Planetodetic properties.'
    _iid_ = GUID('{E51C8DCB-6E1D-4D55-9807-47A7FB7C734F}')
    _idlflags_ = ['hidden', 'dual', 'nonextensible', 'oleautomation']
_IAgPlanetodetic._methods_ = [
    COMMETHOD([dispid(201), helpstring('Latitude. Uses Latitude Dimension.'), 'propget'], HRESULT, 'Lat',
              ( ['out', 'retval'], POINTER(VARIANT), 'pLat' )),
    COMMETHOD([dispid(201), helpstring('Latitude. Uses Latitude Dimension.'), 'propput'], HRESULT, 'Lat',
              ( ['in'], VARIANT, 'pLat' )),
    COMMETHOD([dispid(202), helpstring('Longitude. Uses Longitude Dimension.'), 'propget'], HRESULT, 'Lon',
              ( ['out', 'retval'], POINTER(VARIANT), 'pLon' )),
    COMMETHOD([dispid(202), helpstring('Longitude. Uses Longitude Dimension.'), 'propput'], HRESULT, 'Lon',
              ( ['in'], VARIANT, 'pLon' )),
    COMMETHOD([dispid(203), helpstring('Altitude. Dimension depends on context.'), 'propget'], HRESULT, 'Alt',
              ( ['out', 'retval'], POINTER(c_double), 'pAlt' )),
    COMMETHOD([dispid(203), helpstring('Altitude. Dimension depends on context.'), 'propput'], HRESULT, 'Alt',
              ( ['in'], c_double, 'pAlt' )),
    COMMETHOD([dispid(401), helpstring('Changes the position coordinates to type specified.')], HRESULT, 'ConvertTo',
              ( ['in'], AgEPositionType, 'Type' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgPosition)), 'ppIAgPosition' )),
    COMMETHOD([dispid(402), helpstring('Gets the type of position currently being used.'), 'propget'], HRESULT, 'PosType',
              ( ['out', 'retval'], POINTER(AgEPositionType), 'pType' )),
    COMMETHOD([dispid(403), helpstring('This assigns the coordinates into the system.')], HRESULT, 'Assign',
              ( ['in'], POINTER(IAgPosition), 'pPosition' )),
    COMMETHOD([dispid(404), helpstring('Helper method to assign the position using the Geocentric representation.')], HRESULT, 'AssignGeocentric',
              ( ['in'], VARIANT, 'Lat' ),
              ( ['in'], VARIANT, 'Lon' ),
              ( ['in'], c_double, 'Alt' )),
    COMMETHOD([dispid(405), helpstring('Helper method to assign the position using the Geodetic representation.')], HRESULT, 'AssignGeodetic',
              ( ['in'], VARIANT, 'Lat' ),
              ( ['in'], VARIANT, 'Lon' ),
              ( ['in'], c_double, 'Alt' )),
    COMMETHOD([dispid(406), helpstring('Helper method to assign the position using the Spherical representation')], HRESULT, 'AssignSpherical',
              ( ['in'], VARIANT, 'Lat' ),
              ( ['in'], VARIANT, 'Lon' ),
              ( ['in'], c_double, 'Radius' )),
    COMMETHOD([dispid(407), helpstring('Helper method to assign the position using the Cylindrical representation')], HRESULT, 'AssignCylindrical',
              ( ['in'], c_double, 'Radius' ),
              ( ['in'], c_double, 'Z' ),
              ( ['in'], VARIANT, 'Lon' )),
    COMMETHOD([dispid(408), helpstring('Helper method to assign the position using the Cartesian representation')], HRESULT, 'AssignCartesian',
              ( ['in'], c_double, 'X' ),
              ( ['in'], c_double, 'Y' ),
              ( ['in'], c_double, 'Z' )),
    COMMETHOD([dispid(409), helpstring('Helper method to assign the position using the Planetocentric representation')], HRESULT, 'AssignPlanetocentric',
              ( ['in'], VARIANT, 'Lat' ),
              ( ['in'], VARIANT, 'Lon' ),
              ( ['in'], c_double, 'Alt' )),
    COMMETHOD([dispid(410), helpstring('Helper method to assign the position using the Planetodetic representation')], HRESULT, 'AssignPlanetodetic',
              ( ['in'], VARIANT, 'Lat' ),
              ( ['in'], VARIANT, 'Lon' ),
              ( ['in'], c_double, 'Alt' )),
    COMMETHOD([dispid(411), helpstring('Helper method to get the position using the Planetocentric representation')], HRESULT, 'QueryPlanetocentric',
              ( ['out'], POINTER(VARIANT), 'Lat' ),
              ( ['out'], POINTER(VARIANT), 'Lon' ),
              ( ['out'], POINTER(c_double), 'Alt' )),
    COMMETHOD([dispid(412), helpstring('Helper method to get the position using the Planetodetic representation')], HRESULT, 'QueryPlanetodetic',
              ( ['out'], POINTER(VARIANT), 'Lat' ),
              ( ['out'], POINTER(VARIANT), 'Lon' ),
              ( ['out'], POINTER(c_double), 'Alt' )),
    COMMETHOD([dispid(413), helpstring('Helper method to get the position using the Spherical representation')], HRESULT, 'QuerySpherical',
              ( ['out'], POINTER(VARIANT), 'Lat' ),
              ( ['out'], POINTER(VARIANT), 'Lon' ),
              ( ['out'], POINTER(c_double), 'Radius' )),
    COMMETHOD([dispid(414), helpstring('Helper method to get the position using the Cylindrical representation')], HRESULT, 'QueryCylindrical',
              ( ['out'], POINTER(c_double), 'Radius' ),
              ( ['out'], POINTER(VARIANT), 'Lon' ),
              ( ['out'], POINTER(c_double), 'Z' )),
    COMMETHOD([dispid(415), helpstring('Helper method to get the position using the Cartesian representation')], HRESULT, 'QueryCartesian',
              ( ['out'], POINTER(c_double), 'X' ),
              ( ['out'], POINTER(c_double), 'Y' ),
              ( ['out'], POINTER(c_double), 'Z' )),
    COMMETHOD([dispid(416), helpstring('Gets the central body.'), 'propget'], HRESULT, 'CentralBodyName',
              ( ['out', 'retval'], POINTER(BSTR), 'pCBName' )),
    COMMETHOD([dispid(417), helpstring('Returns the Geocentric elements as an array.')], HRESULT, 'QueryPlanetocentricArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(418), helpstring('Returns the Geodetic elements as an array.')], HRESULT, 'QueryPlanetodeticArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(419), helpstring('Returns the Spherical elements as an array.')], HRESULT, 'QuerySphericalArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(420), helpstring('Returns the Cylindrical elements as an array.')], HRESULT, 'QueryCylindricalArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(421), helpstring('Returns the Cartesian elements as an array.')], HRESULT, 'QueryCartesianArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
]
################################################################
## code template for _IAgPlanetodetic implementation
##class _IAgPlanetodetic_Impl(object):
##    def _get(self):
##        'Latitude. Uses Latitude Dimension.'
##        #return pLat
##    def _set(self, pLat):
##        'Latitude. Uses Latitude Dimension.'
##    Lat = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Longitude. Uses Longitude Dimension.'
##        #return pLon
##    def _set(self, pLon):
##        'Longitude. Uses Longitude Dimension.'
##    Lon = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Altitude. Dimension depends on context.'
##        #return pAlt
##    def _set(self, pAlt):
##        'Altitude. Dimension depends on context.'
##    Alt = property(_get, _set, doc = _set.__doc__)
##
##    def ConvertTo(self, Type):
##        'Changes the position coordinates to type specified.'
##        #return ppIAgPosition
##
##    @property
##    def PosType(self):
##        'Gets the type of position currently being used.'
##        #return pType
##
##    def Assign(self, pPosition):
##        'This assigns the coordinates into the system.'
##        #return 
##
##    def AssignGeocentric(self, Lat, Lon, Alt):
##        'Helper method to assign the position using the Geocentric representation.'
##        #return 
##
##    def AssignGeodetic(self, Lat, Lon, Alt):
##        'Helper method to assign the position using the Geodetic representation.'
##        #return 
##
##    def AssignSpherical(self, Lat, Lon, Radius):
##        'Helper method to assign the position using the Spherical representation'
##        #return 
##
##    def AssignCylindrical(self, Radius, Z, Lon):
##        'Helper method to assign the position using the Cylindrical representation'
##        #return 
##
##    def AssignCartesian(self, X, Y, Z):
##        'Helper method to assign the position using the Cartesian representation'
##        #return 
##
##    def AssignPlanetocentric(self, Lat, Lon, Alt):
##        'Helper method to assign the position using the Planetocentric representation'
##        #return 
##
##    def AssignPlanetodetic(self, Lat, Lon, Alt):
##        'Helper method to assign the position using the Planetodetic representation'
##        #return 
##
##    def QueryPlanetocentric(self):
##        'Helper method to get the position using the Planetocentric representation'
##        #return Lat, Lon, Alt
##
##    def QueryPlanetodetic(self):
##        'Helper method to get the position using the Planetodetic representation'
##        #return Lat, Lon, Alt
##
##    def QuerySpherical(self):
##        'Helper method to get the position using the Spherical representation'
##        #return Lat, Lon, Radius
##
##    def QueryCylindrical(self):
##        'Helper method to get the position using the Cylindrical representation'
##        #return Radius, Lon, Z
##
##    def QueryCartesian(self):
##        'Helper method to get the position using the Cartesian representation'
##        #return X, Y, Z
##
##    @property
##    def CentralBodyName(self):
##        'Gets the central body.'
##        #return pCBName
##
##    def QueryPlanetocentricArray(self):
##        'Returns the Geocentric elements as an array.'
##        #return ppRetVal
##
##    def QueryPlanetodeticArray(self):
##        'Returns the Geodetic elements as an array.'
##        #return ppRetVal
##
##    def QuerySphericalArray(self):
##        'Returns the Spherical elements as an array.'
##        #return ppRetVal
##
##    def QueryCylindricalArray(self):
##        'Returns the Cylindrical elements as an array.'
##        #return ppRetVal
##
##    def QueryCartesianArray(self):
##        'Returns the Cartesian elements as an array.'
##        #return ppRetVal
##

IAgRuntimeTypeInfo._methods_ = [
    COMMETHOD(['propget', helpstring('The collection of properties.')], HRESULT, 'Properties',
              ( ['out', 'retval'], POINTER(POINTER(IAgPropertyInfoCollection)), 'ppRetVal' )),
    COMMETHOD(['propget', helpstring('Determines if the interface is a collection.')], HRESULT, 'IsCollection',
              ( ['out', 'retval'], POINTER(VARIANT_BOOL), 'pVal' )),
    COMMETHOD(['propget', helpstring('If the interface is a collection, returns the collection count.')], HRESULT, 'Count',
              ( ['out', 'retval'], POINTER(c_int), 'pVal' )),
    COMMETHOD([helpstring('Returns the property of the collection at the given index.')], HRESULT, 'GetItem',
              ( ['in'], c_int, 'Index' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgPropertyInfo)), 'ppVal' )),
]
################################################################
## code template for IAgRuntimeTypeInfo implementation
##class IAgRuntimeTypeInfo_Impl(object):
##    @property
##    def Properties(self):
##        'The collection of properties.'
##        #return ppRetVal
##
##    @property
##    def IsCollection(self):
##        'Determines if the interface is a collection.'
##        #return pVal
##
##    @property
##    def Count(self):
##        'If the interface is a collection, returns the collection count.'
##        #return pVal
##
##    def GetItem(self, Index):
##        'Returns the property of the collection at the given index.'
##        #return ppVal
##

class AgExecCmdResult(CoClass):
    'Collection of strings returned by the ExecuteCommand.'
    _reg_clsid_ = GUID('{8D198A08-0876-476E-ABF3-1C27BFEE3F07}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{00DD7BD4-53D5-4870-996B-8ADB8AF904FA}', 1, 0)
AgExecCmdResult._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch, IAgExecCmdResult]

class AgPlanetocentric(CoClass):
    'Class defining Planetocentric position.'
    _reg_clsid_ = GUID('{AF6F0F25-1F95-428A-A399-0681534BE091}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{00DD7BD4-53D5-4870-996B-8ADB8AF904FA}', 1, 0)
class _IAgPlanetocentric(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Planetocentric Position Type.'
    _iid_ = GUID('{301E4576-2ADF-474B-8439-C39310C6481A}')
    _idlflags_ = ['hidden', 'dual', 'nonextensible', 'oleautomation']
class IAgPlanetocentric(IAgPosition):
    _case_insensitive_ = True
    'Planetocentric Position Type.'
    _iid_ = GUID('{4DFE39F0-F1E9-49C1-B11A-0EE1C5795DF2}')
    _idlflags_ = ['oleautomation']
AgPlanetocentric._com_interfaces_ = [_IAgPlanetocentric, IAgPlanetocentric, IAgPosition]

class IAgSpherical(IAgPosition):
    _case_insensitive_ = True
    'Spherical Position Type.'
    _iid_ = GUID('{3843E85E-AEB6-433A-AE8D-8D981BB114E6}')
    _idlflags_ = ['oleautomation']
IAgSpherical._methods_ = [
    COMMETHOD(['propget', helpstring('Uses Latitude Dimension.')], HRESULT, 'Lat',
              ( ['out', 'retval'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD(['propput', helpstring('Uses Latitude Dimension.')], HRESULT, 'Lat',
              ( ['in'], VARIANT, 'pVal' )),
    COMMETHOD(['propget', helpstring('Uses Longitude Dimension.')], HRESULT, 'Lon',
              ( ['out', 'retval'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD(['propput', helpstring('Uses Longitude Dimension.')], HRESULT, 'Lon',
              ( ['in'], VARIANT, 'pVal' )),
    COMMETHOD(['propget', helpstring('Dimension depends on context.')], HRESULT, 'Radius',
              ( ['out', 'retval'], POINTER(c_double), 'pVal' )),
    COMMETHOD(['propput', helpstring('Dimension depends on context.')], HRESULT, 'Radius',
              ( ['in'], c_double, 'pVal' )),
    COMMETHOD([helpstring('This property is deprecated. Use AssignSpherical instead.')], HRESULT, 'SetValues',
              ( ['in'], VARIANT, 'Lat' ),
              ( ['in'], VARIANT, 'Lon' ),
              ( ['in'], c_double, 'Radius' )),
]
################################################################
## code template for IAgSpherical implementation
##class IAgSpherical_Impl(object):
##    def _get(self):
##        'Uses Latitude Dimension.'
##        #return pVal
##    def _set(self, pVal):
##        'Uses Latitude Dimension.'
##    Lat = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Uses Longitude Dimension.'
##        #return pVal
##    def _set(self, pVal):
##        'Uses Longitude Dimension.'
##    Lon = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Dimension depends on context.'
##        #return pVal
##    def _set(self, pVal):
##        'Dimension depends on context.'
##    Radius = property(_get, _set, doc = _set.__doc__)
##
##    def SetValues(self, Lat, Lon, Radius):
##        'This property is deprecated. Use AssignSpherical instead.'
##        #return 
##

IAgPlanetocentric._methods_ = [
    COMMETHOD(['propget', helpstring('Uses Latitude Dimension.')], HRESULT, 'Lat',
              ( ['out', 'retval'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD(['propput', helpstring('Uses Latitude Dimension.')], HRESULT, 'Lat',
              ( ['in'], VARIANT, 'pVal' )),
    COMMETHOD(['propget', helpstring('Uses Longitude Dimension.')], HRESULT, 'Lon',
              ( ['out', 'retval'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD(['propput', helpstring('Uses Longitude Dimension.')], HRESULT, 'Lon',
              ( ['in'], VARIANT, 'pVal' )),
    COMMETHOD(['propget', helpstring('Dimension depends on context.')], HRESULT, 'Alt',
              ( ['out', 'retval'], POINTER(c_double), 'pVal' )),
    COMMETHOD(['propput', helpstring('Dimension depends on context.')], HRESULT, 'Alt',
              ( ['in'], c_double, 'pVal' )),
]
################################################################
## code template for IAgPlanetocentric implementation
##class IAgPlanetocentric_Impl(object):
##    def _get(self):
##        'Uses Latitude Dimension.'
##        #return pVal
##    def _set(self, pVal):
##        'Uses Latitude Dimension.'
##    Lat = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Uses Longitude Dimension.'
##        #return pVal
##    def _set(self, pVal):
##        'Uses Longitude Dimension.'
##    Lon = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Dimension depends on context.'
##        #return pVal
##    def _set(self, pVal):
##        'Dimension depends on context.'
##    Alt = property(_get, _set, doc = _set.__doc__)
##

class AgExecMultiCmdResult(CoClass):
    'Collection of objects returned by the ExecuteMultipleCommands.'
    _reg_clsid_ = GUID('{5C09C4B6-2C7B-4A18-87FB-41422FBBB32B}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{00DD7BD4-53D5-4870-996B-8ADB8AF904FA}', 1, 0)
AgExecMultiCmdResult._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch, IAgExecMultiCmdResult]

_IAgPlanetocentric._methods_ = [
    COMMETHOD([dispid(201), helpstring('Uses Latitude Dimension.'), 'propget'], HRESULT, 'Lat',
              ( ['out', 'retval'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD([dispid(201), helpstring('Uses Latitude Dimension.'), 'propput'], HRESULT, 'Lat',
              ( ['in'], VARIANT, 'pVal' )),
    COMMETHOD([dispid(202), helpstring('Uses Longitude Dimension.'), 'propget'], HRESULT, 'Lon',
              ( ['out', 'retval'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD([dispid(202), helpstring('Uses Longitude Dimension.'), 'propput'], HRESULT, 'Lon',
              ( ['in'], VARIANT, 'pVal' )),
    COMMETHOD([dispid(203), helpstring('Dimension depends on context.'), 'propget'], HRESULT, 'Alt',
              ( ['out', 'retval'], POINTER(c_double), 'pVal' )),
    COMMETHOD([dispid(203), helpstring('Dimension depends on context.'), 'propput'], HRESULT, 'Alt',
              ( ['in'], c_double, 'pVal' )),
    COMMETHOD([dispid(401), helpstring('Changes the position coordinates to type specified.')], HRESULT, 'ConvertTo',
              ( ['in'], AgEPositionType, 'Type' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgPosition)), 'ppIAgPosition' )),
    COMMETHOD([dispid(402), helpstring('Gets the type of position currently being used.'), 'propget'], HRESULT, 'PosType',
              ( ['out', 'retval'], POINTER(AgEPositionType), 'pType' )),
    COMMETHOD([dispid(403), helpstring('This assigns the coordinates into the system.')], HRESULT, 'Assign',
              ( ['in'], POINTER(IAgPosition), 'pPosition' )),
    COMMETHOD([dispid(404), helpstring('Helper method to assign the position using the Geocentric representation.')], HRESULT, 'AssignGeocentric',
              ( ['in'], VARIANT, 'Lat' ),
              ( ['in'], VARIANT, 'Lon' ),
              ( ['in'], c_double, 'Alt' )),
    COMMETHOD([dispid(405), helpstring('Helper method to assign the position using the Geodetic representation.')], HRESULT, 'AssignGeodetic',
              ( ['in'], VARIANT, 'Lat' ),
              ( ['in'], VARIANT, 'Lon' ),
              ( ['in'], c_double, 'Alt' )),
    COMMETHOD([dispid(406), helpstring('Helper method to assign the position using the Spherical representation')], HRESULT, 'AssignSpherical',
              ( ['in'], VARIANT, 'Lat' ),
              ( ['in'], VARIANT, 'Lon' ),
              ( ['in'], c_double, 'Radius' )),
    COMMETHOD([dispid(407), helpstring('Helper method to assign the position using the Cylindrical representation')], HRESULT, 'AssignCylindrical',
              ( ['in'], c_double, 'Radius' ),
              ( ['in'], c_double, 'Z' ),
              ( ['in'], VARIANT, 'Lon' )),
    COMMETHOD([dispid(408), helpstring('Helper method to assign the position using the Cartesian representation')], HRESULT, 'AssignCartesian',
              ( ['in'], c_double, 'X' ),
              ( ['in'], c_double, 'Y' ),
              ( ['in'], c_double, 'Z' )),
    COMMETHOD([dispid(409), helpstring('Helper method to assign the position using the Planetocentric representation')], HRESULT, 'AssignPlanetocentric',
              ( ['in'], VARIANT, 'Lat' ),
              ( ['in'], VARIANT, 'Lon' ),
              ( ['in'], c_double, 'Alt' )),
    COMMETHOD([dispid(410), helpstring('Helper method to assign the position using the Planetodetic representation')], HRESULT, 'AssignPlanetodetic',
              ( ['in'], VARIANT, 'Lat' ),
              ( ['in'], VARIANT, 'Lon' ),
              ( ['in'], c_double, 'Alt' )),
    COMMETHOD([dispid(411), helpstring('Helper method to get the position using the Planetocentric representation')], HRESULT, 'QueryPlanetocentric',
              ( ['out'], POINTER(VARIANT), 'Lat' ),
              ( ['out'], POINTER(VARIANT), 'Lon' ),
              ( ['out'], POINTER(c_double), 'Alt' )),
    COMMETHOD([dispid(412), helpstring('Helper method to get the position using the Planetodetic representation')], HRESULT, 'QueryPlanetodetic',
              ( ['out'], POINTER(VARIANT), 'Lat' ),
              ( ['out'], POINTER(VARIANT), 'Lon' ),
              ( ['out'], POINTER(c_double), 'Alt' )),
    COMMETHOD([dispid(413), helpstring('Helper method to get the position using the Spherical representation')], HRESULT, 'QuerySpherical',
              ( ['out'], POINTER(VARIANT), 'Lat' ),
              ( ['out'], POINTER(VARIANT), 'Lon' ),
              ( ['out'], POINTER(c_double), 'Radius' )),
    COMMETHOD([dispid(414), helpstring('Helper method to get the position using the Cylindrical representation')], HRESULT, 'QueryCylindrical',
              ( ['out'], POINTER(c_double), 'Radius' ),
              ( ['out'], POINTER(VARIANT), 'Lon' ),
              ( ['out'], POINTER(c_double), 'Z' )),
    COMMETHOD([dispid(415), helpstring('Helper method to get the position using the Cartesian representation')], HRESULT, 'QueryCartesian',
              ( ['out'], POINTER(c_double), 'X' ),
              ( ['out'], POINTER(c_double), 'Y' ),
              ( ['out'], POINTER(c_double), 'Z' )),
    COMMETHOD([dispid(416), helpstring('Gets the central body.'), 'propget'], HRESULT, 'CentralBodyName',
              ( ['out', 'retval'], POINTER(BSTR), 'pCBName' )),
    COMMETHOD([dispid(417), helpstring('Returns the Planetocentric elements as an array.')], HRESULT, 'QueryPlanetocentricArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(418), helpstring('Returns the Planetodetic elements as an array.')], HRESULT, 'QueryPlanetodeticArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(419), helpstring('Returns the Spherical elements as an array.')], HRESULT, 'QuerySphericalArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(420), helpstring('Returns the Cylindrical elements as an array.')], HRESULT, 'QueryCylindricalArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(421), helpstring('Returns the Cartesian elements as an array.')], HRESULT, 'QueryCartesianArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
]
################################################################
## code template for _IAgPlanetocentric implementation
##class _IAgPlanetocentric_Impl(object):
##    def _get(self):
##        'Uses Latitude Dimension.'
##        #return pVal
##    def _set(self, pVal):
##        'Uses Latitude Dimension.'
##    Lat = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Uses Longitude Dimension.'
##        #return pVal
##    def _set(self, pVal):
##        'Uses Longitude Dimension.'
##    Lon = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Dimension depends on context.'
##        #return pVal
##    def _set(self, pVal):
##        'Dimension depends on context.'
##    Alt = property(_get, _set, doc = _set.__doc__)
##
##    def ConvertTo(self, Type):
##        'Changes the position coordinates to type specified.'
##        #return ppIAgPosition
##
##    @property
##    def PosType(self):
##        'Gets the type of position currently being used.'
##        #return pType
##
##    def Assign(self, pPosition):
##        'This assigns the coordinates into the system.'
##        #return 
##
##    def AssignGeocentric(self, Lat, Lon, Alt):
##        'Helper method to assign the position using the Geocentric representation.'
##        #return 
##
##    def AssignGeodetic(self, Lat, Lon, Alt):
##        'Helper method to assign the position using the Geodetic representation.'
##        #return 
##
##    def AssignSpherical(self, Lat, Lon, Radius):
##        'Helper method to assign the position using the Spherical representation'
##        #return 
##
##    def AssignCylindrical(self, Radius, Z, Lon):
##        'Helper method to assign the position using the Cylindrical representation'
##        #return 
##
##    def AssignCartesian(self, X, Y, Z):
##        'Helper method to assign the position using the Cartesian representation'
##        #return 
##
##    def AssignPlanetocentric(self, Lat, Lon, Alt):
##        'Helper method to assign the position using the Planetocentric representation'
##        #return 
##
##    def AssignPlanetodetic(self, Lat, Lon, Alt):
##        'Helper method to assign the position using the Planetodetic representation'
##        #return 
##
##    def QueryPlanetocentric(self):
##        'Helper method to get the position using the Planetocentric representation'
##        #return Lat, Lon, Alt
##
##    def QueryPlanetodetic(self):
##        'Helper method to get the position using the Planetodetic representation'
##        #return Lat, Lon, Alt
##
##    def QuerySpherical(self):
##        'Helper method to get the position using the Spherical representation'
##        #return Lat, Lon, Radius
##
##    def QueryCylindrical(self):
##        'Helper method to get the position using the Cylindrical representation'
##        #return Radius, Lon, Z
##
##    def QueryCartesian(self):
##        'Helper method to get the position using the Cartesian representation'
##        #return X, Y, Z
##
##    @property
##    def CentralBodyName(self):
##        'Gets the central body.'
##        #return pCBName
##
##    def QueryPlanetocentricArray(self):
##        'Returns the Planetocentric elements as an array.'
##        #return ppRetVal
##
##    def QueryPlanetodeticArray(self):
##        'Returns the Planetodetic elements as an array.'
##        #return ppRetVal
##
##    def QuerySphericalArray(self):
##        'Returns the Spherical elements as an array.'
##        #return ppRetVal
##
##    def QueryCylindricalArray(self):
##        'Returns the Cylindrical elements as an array.'
##        #return ppRetVal
##
##    def QueryCartesianArray(self):
##        'Returns the Cartesian elements as an array.'
##        #return ppRetVal
##

IAgExecCmdResult._methods_ = [
    COMMETHOD([dispid(1), helpstring('Number of elements contained in the collection.'), 'propget'], HRESULT, 'Count',
              ( ['out', 'retval'], POINTER(c_int), 'pCount' )),
    COMMETHOD([dispid(0), helpstring('Gets the element at the specified index (0-based).'), 'propget'], HRESULT, 'Item',
              ( ['in'], c_int, 'Index' ),
              ( ['out', 'retval'], POINTER(BSTR), 'pItem' )),
    COMMETHOD([dispid(-4), helpstring('Returns an object that can be used to iterate through all the strings in the collection.'), 'propget'], HRESULT, '_NewEnum',
              ( ['out', 'retval'], POINTER(POINTER(IUnknown)), 'ppEnum' )),
    COMMETHOD([dispid(4), helpstring('Return the elements within the specified range.')], HRESULT, 'Range',
              ( ['in'], c_int, 'StartIndex' ),
              ( ['in'], c_int, 'StopIndex' ),
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppVar' )),
    COMMETHOD([dispid(5), helpstring('Indicates whether the object contains valid results.'), 'propget'], HRESULT, 'IsSucceeded',
              ( ['out', 'retval'], POINTER(VARIANT_BOOL), 'pRetVal' )),
]
################################################################
## code template for IAgExecCmdResult implementation
##class IAgExecCmdResult_Impl(object):
##    @property
##    def Count(self):
##        'Number of elements contained in the collection.'
##        #return pCount
##
##    @property
##    def Item(self, Index):
##        'Gets the element at the specified index (0-based).'
##        #return pItem
##
##    @property
##    def _NewEnum(self):
##        'Returns an object that can be used to iterate through all the strings in the collection.'
##        #return ppEnum
##
##    def Range(self, StartIndex, StopIndex):
##        'Return the elements within the specified range.'
##        #return ppVar
##
##    @property
##    def IsSucceeded(self):
##        'Indicates whether the object contains valid results.'
##        #return pRetVal
##

IAgOrientationPositionOffset._methods_ = [
    COMMETHOD(['propget', helpstring('Gets or sets the position offset cartesian vector.')], HRESULT, 'PositionOffset',
              ( ['out', 'retval'], POINTER(POINTER(IAgCartesian3Vector)), 'ppRetVal' )),
]
################################################################
## code template for IAgOrientationPositionOffset implementation
##class IAgOrientationPositionOffset_Impl(object):
##    @property
##    def PositionOffset(self):
##        'Gets or sets the position offset cartesian vector.'
##        #return ppRetVal
##

class _IAgDirectionXYZ(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'The hidden interface for IAgDirectionXYZ'
    _iid_ = GUID('{09194A69-9BDF-4F94-8DD3-660F9AF9D8DB}')
    _idlflags_ = ['hidden', 'dual', 'nonextensible', 'oleautomation']
_IAgDirectionXYZ._methods_ = [
    COMMETHOD([dispid(201), helpstring('X component. Dimensionless'), 'propget'], HRESULT, 'X',
              ( ['out', 'retval'], POINTER(c_double), 'pVal' )),
    COMMETHOD([dispid(201), helpstring('X component. Dimensionless'), 'propput'], HRESULT, 'X',
              ( ['in'], c_double, 'pVal' )),
    COMMETHOD([dispid(202), helpstring('Y component. Dimensionless'), 'propget'], HRESULT, 'Y',
              ( ['out', 'retval'], POINTER(c_double), 'pVal' )),
    COMMETHOD([dispid(202), helpstring('Y component. Dimensionless'), 'propput'], HRESULT, 'Y',
              ( ['in'], c_double, 'pVal' )),
    COMMETHOD([dispid(203), helpstring('Z component. Dimensionless'), 'propget'], HRESULT, 'Z',
              ( ['out', 'retval'], POINTER(c_double), 'pVal' )),
    COMMETHOD([dispid(203), helpstring('Z component. Dimensionless'), 'propput'], HRESULT, 'Z',
              ( ['in'], c_double, 'pVal' )),
    COMMETHOD([dispid(204), helpstring('This property is deprecated. Use AssignXYZ instead.')], HRESULT, 'SetValues',
              ( ['in'], c_double, 'X' ),
              ( ['in'], c_double, 'Y' ),
              ( ['in'], c_double, 'Z' )),
    COMMETHOD([dispid(401), helpstring('Method to changes the direction to the type specified.')], HRESULT, 'ConvertTo',
              ( ['in'], AgEDirectionType, 'Type' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgDirection)), 'ppIAgDirection' )),
    COMMETHOD([dispid(402), helpstring('Returns the type of direction currently being used.'), 'propget'], HRESULT, 'DirectionType',
              ( ['out', 'retval'], POINTER(AgEDirectionType), 'pType' )),
    COMMETHOD([dispid(403), helpstring('Assign a new direction.')], HRESULT, 'Assign',
              ( ['in'], POINTER(IAgDirection), 'pDirection' )),
    COMMETHOD([dispid(404), helpstring('Helper method to set direction using the Euler representation. Params B and C use Angle Dimension.')], HRESULT, 'AssignEuler',
              ( ['in'], VARIANT, 'B' ),
              ( ['in'], VARIANT, 'C' ),
              ( ['in'], AgEEulerDirectionSequence, 'Sequence' )),
    COMMETHOD([dispid(405), helpstring('Helper method to set direction using the Pitch Roll representation. Pitch and Roll use Angle Dimension.')], HRESULT, 'AssignPR',
              ( ['in'], VARIANT, 'Pitch' ),
              ( ['in'], VARIANT, 'Roll' )),
    COMMETHOD([dispid(406), helpstring('Helper method to set direction using the Right Ascension and Declination representation. Param Dec uses Latitude. Param RA uses Longitude.')], HRESULT, 'AssignRADec',
              ( ['in'], VARIANT, 'RA' ),
              ( ['in'], VARIANT, 'Dec' )),
    COMMETHOD([dispid(407), helpstring('Helper method to set direction using the Cartesian representation. Params X, Y and Z are dimensionless.')], HRESULT, 'AssignXYZ',
              ( ['in'], c_double, 'X' ),
              ( ['in'], c_double, 'Y' ),
              ( ['in'], c_double, 'Z' )),
    COMMETHOD([dispid(408), helpstring('Helper method to get direction using the Euler representation. Params B and C use Angle Dimension.')], HRESULT, 'QueryEuler',
              ( ['in'], AgEEulerDirectionSequence, 'Sequence' ),
              ( ['out'], POINTER(VARIANT), 'B' ),
              ( ['out'], POINTER(VARIANT), 'C' )),
    COMMETHOD([dispid(409), helpstring('Helper method to get direction using the Pitch Roll representation. Pitch and Roll use Angle Dimension.')], HRESULT, 'QueryPR',
              ( ['in'], AgEPRSequence, 'Sequence' ),
              ( ['out'], POINTER(VARIANT), 'Pitch' ),
              ( ['out'], POINTER(VARIANT), 'Roll' )),
    COMMETHOD([dispid(410), helpstring('Helper method to get direction using the Right Ascension and Declination representation. Param Dec uses Latitude. Param RA uses Longitude.')], HRESULT, 'QueryRADec',
              ( ['out'], POINTER(VARIANT), 'RA' ),
              ( ['out'], POINTER(VARIANT), 'Dec' )),
    COMMETHOD([dispid(411), helpstring('Helper method to get direction using the Cartesian representation. Params X, Y and Z are dimensionless.')], HRESULT, 'QueryXYZ',
              ( ['out'], POINTER(c_double), 'X' ),
              ( ['out'], POINTER(c_double), 'Y' ),
              ( ['out'], POINTER(c_double), 'Z' )),
    COMMETHOD([dispid(412), helpstring('Returns the Euler elements in an array.')], HRESULT, 'QueryEulerArray',
              ( ['in'], AgEEulerDirectionSequence, 'Sequence' ),
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(413), helpstring('Returns the PR elements in an array.')], HRESULT, 'QueryPRArray',
              ( ['in'], AgEPRSequence, 'Sequence' ),
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(414), helpstring('Returns the RADec elements in an array.')], HRESULT, 'QueryRADecArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(415), helpstring('Returns the XYZ elements in an array.')], HRESULT, 'QueryXYZArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
]
################################################################
## code template for _IAgDirectionXYZ implementation
##class _IAgDirectionXYZ_Impl(object):
##    def _get(self):
##        'X component. Dimensionless'
##        #return pVal
##    def _set(self, pVal):
##        'X component. Dimensionless'
##    X = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Y component. Dimensionless'
##        #return pVal
##    def _set(self, pVal):
##        'Y component. Dimensionless'
##    Y = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Z component. Dimensionless'
##        #return pVal
##    def _set(self, pVal):
##        'Z component. Dimensionless'
##    Z = property(_get, _set, doc = _set.__doc__)
##
##    def SetValues(self, X, Y, Z):
##        'This property is deprecated. Use AssignXYZ instead.'
##        #return 
##
##    def ConvertTo(self, Type):
##        'Method to changes the direction to the type specified.'
##        #return ppIAgDirection
##
##    @property
##    def DirectionType(self):
##        'Returns the type of direction currently being used.'
##        #return pType
##
##    def Assign(self, pDirection):
##        'Assign a new direction.'
##        #return 
##
##    def AssignEuler(self, B, C, Sequence):
##        'Helper method to set direction using the Euler representation. Params B and C use Angle Dimension.'
##        #return 
##
##    def AssignPR(self, Pitch, Roll):
##        'Helper method to set direction using the Pitch Roll representation. Pitch and Roll use Angle Dimension.'
##        #return 
##
##    def AssignRADec(self, RA, Dec):
##        'Helper method to set direction using the Right Ascension and Declination representation. Param Dec uses Latitude. Param RA uses Longitude.'
##        #return 
##
##    def AssignXYZ(self, X, Y, Z):
##        'Helper method to set direction using the Cartesian representation. Params X, Y and Z are dimensionless.'
##        #return 
##
##    def QueryEuler(self, Sequence):
##        'Helper method to get direction using the Euler representation. Params B and C use Angle Dimension.'
##        #return B, C
##
##    def QueryPR(self, Sequence):
##        'Helper method to get direction using the Pitch Roll representation. Pitch and Roll use Angle Dimension.'
##        #return Pitch, Roll
##
##    def QueryRADec(self):
##        'Helper method to get direction using the Right Ascension and Declination representation. Param Dec uses Latitude. Param RA uses Longitude.'
##        #return RA, Dec
##
##    def QueryXYZ(self):
##        'Helper method to get direction using the Cartesian representation. Params X, Y and Z are dimensionless.'
##        #return X, Y, Z
##
##    def QueryEulerArray(self, Sequence):
##        'Returns the Euler elements in an array.'
##        #return ppRetVal
##
##    def QueryPRArray(self, Sequence):
##        'Returns the PR elements in an array.'
##        #return ppRetVal
##
##    def QueryRADecArray(self):
##        'Returns the RADec elements in an array.'
##        #return ppRetVal
##
##    def QueryXYZArray(self):
##        'Returns the XYZ elements in an array.'
##        #return ppRetVal
##

IAgCartesian3Vector._methods_ = [
    COMMETHOD(['propget', helpstring('X coordinate')], HRESULT, 'X',
              ( ['out', 'retval'], POINTER(c_double), 'pRetVal' )),
    COMMETHOD(['propput', helpstring('X coordinate')], HRESULT, 'X',
              ( ['in'], c_double, 'pRetVal' )),
    COMMETHOD(['propget', helpstring('Y coordinate')], HRESULT, 'Y',
              ( ['out', 'retval'], POINTER(c_double), 'pRetVal' )),
    COMMETHOD(['propput', helpstring('Y coordinate')], HRESULT, 'Y',
              ( ['in'], c_double, 'pRetVal' )),
    COMMETHOD(['propget', helpstring('Z coordinate')], HRESULT, 'Z',
              ( ['out', 'retval'], POINTER(c_double), 'pRetVal' )),
    COMMETHOD(['propput', helpstring('Z coordinate')], HRESULT, 'Z',
              ( ['in'], c_double, 'pRetVal' )),
    COMMETHOD([helpstring('Returns cartesian vector')], HRESULT, 'Get',
              ( ['out'], POINTER(c_double), 'X' ),
              ( ['out'], POINTER(c_double), 'Y' ),
              ( ['out'], POINTER(c_double), 'Z' )),
    COMMETHOD([helpstring('Sets cartesian vector')], HRESULT, 'Set',
              ( ['in'], c_double, 'X' ),
              ( ['in'], c_double, 'Y' ),
              ( ['in'], c_double, 'Z' )),
    COMMETHOD([helpstring('Returns coordinates as an array.')], HRESULT, 'ToArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
]
################################################################
## code template for IAgCartesian3Vector implementation
##class IAgCartesian3Vector_Impl(object):
##    def _get(self):
##        'X coordinate'
##        #return pRetVal
##    def _set(self, pRetVal):
##        'X coordinate'
##    X = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Y coordinate'
##        #return pRetVal
##    def _set(self, pRetVal):
##        'Y coordinate'
##    Y = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Z coordinate'
##        #return pRetVal
##    def _set(self, pRetVal):
##        'Z coordinate'
##    Z = property(_get, _set, doc = _set.__doc__)
##
##    def Get(self):
##        'Returns cartesian vector'
##        #return X, Y, Z
##
##    def Set(self, X, Y, Z):
##        'Sets cartesian vector'
##        #return 
##
##    def ToArray(self):
##        'Returns coordinates as an array.'
##        #return ppRetVal
##

class AgDirectionXYZ(CoClass):
    'Cartesian direction.'
    _reg_clsid_ = GUID('{4910BD98-3CC8-4F47-AE51-49367440C46C}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{00DD7BD4-53D5-4870-996B-8ADB8AF904FA}', 1, 0)
class IAgDirectionXYZ(IAgDirection):
    _case_insensitive_ = True
    'Interface for Cartesian direction.'
    _iid_ = GUID('{9E3D600A-8CCC-48E6-B035-2F01C2BEBA39}')
    _idlflags_ = ['oleautomation']
AgDirectionXYZ._com_interfaces_ = [_IAgDirectionXYZ, IAgDirectionXYZ, IAgDirection]

class _IAgCROrientationEulerAngles(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'The hidden interface for IAgOrientationEulerAngles'
    _iid_ = GUID('{D5AC1455-8B86-4577-A7A3-9151EFE277F3}')
    _idlflags_ = ['hidden', 'dual', 'nonextensible', 'oleautomation']
_IAgCROrientationEulerAngles._methods_ = [
    COMMETHOD([dispid(201), helpstring('Euler rotation sequence. Must be set before A,B,C values. Otherwise the current A,B,C values will be converted to the Sequence specified.'), 'propget'], HRESULT, 'Sequence',
              ( ['out', 'retval'], POINTER(AgEEulerOrientationSequence), 'pVal' )),
    COMMETHOD([dispid(201), helpstring('Euler rotation sequence. Must be set before A,B,C values. Otherwise the current A,B,C values will be converted to the Sequence specified.'), 'propput'], HRESULT, 'Sequence',
              ( ['in'], AgEEulerOrientationSequence, 'pVal' )),
    COMMETHOD([dispid(202), helpstring('Euler A angle. Uses Angle Dimension.'), 'propget'], HRESULT, 'A',
              ( ['out', 'retval'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD([dispid(202), helpstring('Euler A angle. Uses Angle Dimension.'), 'propput'], HRESULT, 'A',
              ( ['in'], VARIANT, 'pVal' )),
    COMMETHOD([dispid(203), helpstring('Euler b angle. Uses Angle Dimension.'), 'propget'], HRESULT, 'B',
              ( ['out', 'retval'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD([dispid(203), helpstring('Euler b angle. Uses Angle Dimension.'), 'propput'], HRESULT, 'B',
              ( ['in'], VARIANT, 'pVal' )),
    COMMETHOD([dispid(204), helpstring('Euler C angle. Uses Angle Dimension.'), 'propget'], HRESULT, 'C',
              ( ['out', 'retval'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD([dispid(204), helpstring('Euler C angle. Uses Angle Dimension.'), 'propput'], HRESULT, 'C',
              ( ['in'], VARIANT, 'pVal' )),
    COMMETHOD([dispid(205), helpstring('This property is deprecated. Use AssignEulerAngles instead.')], HRESULT, 'SetValues',
              ( ['in'], AgEEulerOrientationSequence, 'Sequence' ),
              ( ['in'], VARIANT, 'A' ),
              ( ['in'], VARIANT, 'B' ),
              ( ['in'], VARIANT, 'C' )),
    COMMETHOD([dispid(401), helpstring('Method to change the orientation method to the type specified.')], HRESULT, 'ConvertTo',
              ( ['in'], AgEOrientationType, 'Type' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgOrientation)), 'ppIAgOrientation' )),
    COMMETHOD([dispid(402), helpstring('Returns the orientation method currently being used.'), 'propget'], HRESULT, 'OrientationType',
              ( ['out', 'retval'], POINTER(AgEOrientationType), 'pType' )),
    COMMETHOD([dispid(403), helpstring('Assign a new orientation method.')], HRESULT, 'Assign',
              ( ['in'], POINTER(IAgOrientation), 'pOrientation' )),
    COMMETHOD([dispid(404), helpstring('Helper method to set orientation using the AzEl representation.')], HRESULT, 'AssignAzEl',
              ( ['in'], VARIANT, 'Azimuth' ),
              ( ['in'], VARIANT, 'Elevation' ),
              ( ['in'], AgEAzElAboutBoresight, 'AboutBoresight' )),
    COMMETHOD([dispid(405), helpstring('Helper method to set orientation using the Euler angles representation.')], HRESULT, 'AssignEulerAngles',
              ( ['in'], AgEEulerOrientationSequence, 'Sequence' ),
              ( ['in'], VARIANT, 'A' ),
              ( ['in'], VARIANT, 'B' ),
              ( ['in'], VARIANT, 'C' )),
    COMMETHOD([dispid(406), helpstring('Helper method to set orientation using the Quaternion representation.')], HRESULT, 'AssignQuaternion',
              ( ['in'], c_double, 'QX' ),
              ( ['in'], c_double, 'QY' ),
              ( ['in'], c_double, 'QZ' ),
              ( ['in'], c_double, 'QS' )),
    COMMETHOD([dispid(407), helpstring('Helper method to set orientation using the YPR angles representation.')], HRESULT, 'AssignYPRAngles',
              ( ['in'], AgEYPRAnglesSequence, 'Sequence' ),
              ( ['in'], VARIANT, 'Yaw' ),
              ( ['in'], VARIANT, 'Pitch' ),
              ( ['in'], VARIANT, 'Roll' )),
    COMMETHOD([dispid(408), helpstring('Helper method to get orientation using the AzEl representation.')], HRESULT, 'QueryAzEl',
              ( ['out'], POINTER(VARIANT), 'Azimuth' ),
              ( ['out'], POINTER(VARIANT), 'Elevation' ),
              ( ['out'], POINTER(AgEAzElAboutBoresight), 'AboutBoresight' )),
    COMMETHOD([dispid(409), helpstring('Helper method to get orientation using the Euler angles representation.')], HRESULT, 'QueryEulerAngles',
              ( ['in'], AgEEulerOrientationSequence, 'Sequence' ),
              ( ['out'], POINTER(VARIANT), 'A' ),
              ( ['out'], POINTER(VARIANT), 'B' ),
              ( ['out'], POINTER(VARIANT), 'C' )),
    COMMETHOD([dispid(410), helpstring('Helper method to get orientation using the Quaternion representation.')], HRESULT, 'QueryQuaternion',
              ( ['out'], POINTER(c_double), 'QX' ),
              ( ['out'], POINTER(c_double), 'QY' ),
              ( ['out'], POINTER(c_double), 'QZ' ),
              ( ['out'], POINTER(c_double), 'QS' )),
    COMMETHOD([dispid(411), helpstring('Helper method to get orientation using the YPR angles representation.')], HRESULT, 'QueryYPRAngles',
              ( ['in'], AgEYPRAnglesSequence, 'Sequence' ),
              ( ['out'], POINTER(VARIANT), 'Yaw' ),
              ( ['out'], POINTER(VARIANT), 'Pitch' ),
              ( ['out'], POINTER(VARIANT), 'Roll' )),
    COMMETHOD([dispid(412), helpstring('Returns the AzEl elements as an array.')], HRESULT, 'QueryAzElArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(413), helpstring('Returns the Euler elements as an array.')], HRESULT, 'QueryEulerAnglesArray',
              ( ['in'], AgEEulerOrientationSequence, 'Sequence' ),
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(414), helpstring('Returns the Quaternion elements as an array.')], HRESULT, 'QueryQuaternionArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(415), helpstring('Returns the YPR Angles elements as an array.')], HRESULT, 'QueryYPRAnglesArray',
              ( ['in'], AgEYPRAnglesSequence, 'Sequence' ),
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(416), helpstring('Gets or sets the location offset cartesian vector.'), 'propget'], HRESULT, 'PositionOffset',
              ( ['out', 'retval'], POINTER(POINTER(IAgCartesian3Vector)), 'ppRetVal' )),
]
################################################################
## code template for _IAgCROrientationEulerAngles implementation
##class _IAgCROrientationEulerAngles_Impl(object):
##    def _get(self):
##        'Euler rotation sequence. Must be set before A,B,C values. Otherwise the current A,B,C values will be converted to the Sequence specified.'
##        #return pVal
##    def _set(self, pVal):
##        'Euler rotation sequence. Must be set before A,B,C values. Otherwise the current A,B,C values will be converted to the Sequence specified.'
##    Sequence = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Euler A angle. Uses Angle Dimension.'
##        #return pVal
##    def _set(self, pVal):
##        'Euler A angle. Uses Angle Dimension.'
##    A = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Euler b angle. Uses Angle Dimension.'
##        #return pVal
##    def _set(self, pVal):
##        'Euler b angle. Uses Angle Dimension.'
##    B = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Euler C angle. Uses Angle Dimension.'
##        #return pVal
##    def _set(self, pVal):
##        'Euler C angle. Uses Angle Dimension.'
##    C = property(_get, _set, doc = _set.__doc__)
##
##    def SetValues(self, Sequence, A, B, C):
##        'This property is deprecated. Use AssignEulerAngles instead.'
##        #return 
##
##    def ConvertTo(self, Type):
##        'Method to change the orientation method to the type specified.'
##        #return ppIAgOrientation
##
##    @property
##    def OrientationType(self):
##        'Returns the orientation method currently being used.'
##        #return pType
##
##    def Assign(self, pOrientation):
##        'Assign a new orientation method.'
##        #return 
##
##    def AssignAzEl(self, Azimuth, Elevation, AboutBoresight):
##        'Helper method to set orientation using the AzEl representation.'
##        #return 
##
##    def AssignEulerAngles(self, Sequence, A, B, C):
##        'Helper method to set orientation using the Euler angles representation.'
##        #return 
##
##    def AssignQuaternion(self, QX, QY, QZ, QS):
##        'Helper method to set orientation using the Quaternion representation.'
##        #return 
##
##    def AssignYPRAngles(self, Sequence, Yaw, Pitch, Roll):
##        'Helper method to set orientation using the YPR angles representation.'
##        #return 
##
##    def QueryAzEl(self):
##        'Helper method to get orientation using the AzEl representation.'
##        #return Azimuth, Elevation, AboutBoresight
##
##    def QueryEulerAngles(self, Sequence):
##        'Helper method to get orientation using the Euler angles representation.'
##        #return A, B, C
##
##    def QueryQuaternion(self):
##        'Helper method to get orientation using the Quaternion representation.'
##        #return QX, QY, QZ, QS
##
##    def QueryYPRAngles(self, Sequence):
##        'Helper method to get orientation using the YPR angles representation.'
##        #return Yaw, Pitch, Roll
##
##    def QueryAzElArray(self):
##        'Returns the AzEl elements as an array.'
##        #return ppRetVal
##
##    def QueryEulerAnglesArray(self, Sequence):
##        'Returns the Euler elements as an array.'
##        #return ppRetVal
##
##    def QueryQuaternionArray(self):
##        'Returns the Quaternion elements as an array.'
##        #return ppRetVal
##
##    def QueryYPRAnglesArray(self, Sequence):
##        'Returns the YPR Angles elements as an array.'
##        #return ppRetVal
##
##    @property
##    def PositionOffset(self):
##        'Gets or sets the location offset cartesian vector.'
##        #return ppRetVal
##

class AgSpherical(CoClass):
    'Class defining spherical position.'
    _reg_clsid_ = GUID('{927F7836-769D-4FB7-9E29-3D045EC3B327}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{00DD7BD4-53D5-4870-996B-8ADB8AF904FA}', 1, 0)
class _IAgSpherical(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Spherical Position Type.'
    _iid_ = GUID('{3E466CBF-3602-4FE7-8375-8403F272E771}')
    _idlflags_ = ['hidden', 'dual', 'nonextensible', 'oleautomation']
AgSpherical._com_interfaces_ = [_IAgSpherical, IAgSpherical, IAgPosition]

class AgCROrientationEulerAngles(CoClass):
    'Euler Angles orientation method.'
    _reg_clsid_ = GUID('{82DB998B-9A3B-48B8-8FF6-1D6BC219CE66}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{00DD7BD4-53D5-4870-996B-8ADB8AF904FA}', 1, 0)
AgCROrientationEulerAngles._com_interfaces_ = [_IAgCROrientationEulerAngles, IAgOrientationEulerAngles, IAgOrientation, IAgOrientationPositionOffset]

IAgDirectionPR._methods_ = [
    COMMETHOD(['propget', helpstring('Pitch angle. Uses Angle Dimension.')], HRESULT, 'Pitch',
              ( ['out', 'retval'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD(['propput', helpstring('Pitch angle. Uses Angle Dimension.')], HRESULT, 'Pitch',
              ( ['in'], VARIANT, 'pVal' )),
    COMMETHOD(['propget', helpstring('Roll angle. Uses Angle Dimension.')], HRESULT, 'Roll',
              ( ['out', 'retval'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD(['propput', helpstring('Roll angle. Uses Angle Dimension.')], HRESULT, 'Roll',
              ( ['in'], VARIANT, 'pVal' )),
    COMMETHOD(['propget', helpstring('PR direction sequence. Must be set before Pitch,Roll values. Otherwise the current Pitch,Roll values will be converted to the Sequence specified.')], HRESULT, 'Sequence',
              ( ['out', 'retval'], POINTER(AgEPRSequence), 'pVal' )),
    COMMETHOD(['propput', helpstring('PR direction sequence. Must be set before Pitch,Roll values. Otherwise the current Pitch,Roll values will be converted to the Sequence specified.')], HRESULT, 'Sequence',
              ( ['in'], AgEPRSequence, 'pVal' )),
    COMMETHOD([helpstring('This property is deprecated. Use AssignPR instead.')], HRESULT, 'SetValues',
              ( ['in'], VARIANT, 'Pitch' ),
              ( ['in'], VARIANT, 'Roll' )),
]
################################################################
## code template for IAgDirectionPR implementation
##class IAgDirectionPR_Impl(object):
##    def _get(self):
##        'Pitch angle. Uses Angle Dimension.'
##        #return pVal
##    def _set(self, pVal):
##        'Pitch angle. Uses Angle Dimension.'
##    Pitch = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Roll angle. Uses Angle Dimension.'
##        #return pVal
##    def _set(self, pVal):
##        'Roll angle. Uses Angle Dimension.'
##    Roll = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'PR direction sequence. Must be set before Pitch,Roll values. Otherwise the current Pitch,Roll values will be converted to the Sequence specified.'
##        #return pVal
##    def _set(self, pVal):
##        'PR direction sequence. Must be set before Pitch,Roll values. Otherwise the current Pitch,Roll values will be converted to the Sequence specified.'
##    Sequence = property(_get, _set, doc = _set.__doc__)
##
##    def SetValues(self, Pitch, Roll):
##        'This property is deprecated. Use AssignPR instead.'
##        #return 
##

class _IAgCROrientationAzEl(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'The hidden interface for IAgOrientationAzEl'
    _iid_ = GUID('{1DA6141F-ED8B-460B-9C54-E91046F05DA8}')
    _idlflags_ = ['hidden', 'dual', 'nonextensible', 'oleautomation']
_IAgCROrientationAzEl._methods_ = [
    COMMETHOD([dispid(201), helpstring('Measured in the XY plane of the parent reference frame about its Z axis in the right-handed sense for both vehicle-based sensors and facility-based sensors. Uses Angle Dimension.'), 'propget'], HRESULT, 'Azimuth',
              ( ['out', 'retval'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD([dispid(201), helpstring('Measured in the XY plane of the parent reference frame about its Z axis in the right-handed sense for both vehicle-based sensors and facility-based sensors. Uses Angle Dimension.'), 'propput'], HRESULT, 'Azimuth',
              ( ['in'], VARIANT, 'pVal' )),
    COMMETHOD([dispid(202), helpstring('Defined as the angle between the XY plane of the parent reference frame and the sensor or antenna boresight measured toward the positive Z axis. Uses Angle Dimension.'), 'propget'], HRESULT, 'Elevation',
              ( ['out', 'retval'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD([dispid(202), helpstring('Defined as the angle between the XY plane of the parent reference frame and the sensor or antenna boresight measured toward the positive Z axis. Uses Angle Dimension.'), 'propput'], HRESULT, 'Elevation',
              ( ['in'], VARIANT, 'pVal' )),
    COMMETHOD([dispid(203), helpstring("Determines orientation of the X and Y axes with respect to the parent's reference frame."), 'propget'], HRESULT, 'AboutBoresight',
              ( ['out', 'retval'], POINTER(AgEAzElAboutBoresight), 'pVal' )),
    COMMETHOD([dispid(203), helpstring("Determines orientation of the X and Y axes with respect to the parent's reference frame."), 'propput'], HRESULT, 'AboutBoresight',
              ( ['in'], AgEAzElAboutBoresight, 'pVal' )),
    COMMETHOD([dispid(204), helpstring('This property is deprecated. Use AssignAzEl instead.')], HRESULT, 'SetValues',
              ( ['in'], VARIANT, 'Azimuth' ),
              ( ['in'], VARIANT, 'Elevation' ),
              ( ['in'], AgEAzElAboutBoresight, 'AboutBoresight' )),
    COMMETHOD([dispid(401), helpstring('Method to change the orientation method to the type specified.')], HRESULT, 'ConvertTo',
              ( ['in'], AgEOrientationType, 'Type' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgOrientation)), 'ppIAgOrientation' )),
    COMMETHOD([dispid(402), helpstring('Returns the orientation method currently being used.'), 'propget'], HRESULT, 'OrientationType',
              ( ['out', 'retval'], POINTER(AgEOrientationType), 'pType' )),
    COMMETHOD([dispid(403), helpstring('Assign a new orientation method.')], HRESULT, 'Assign',
              ( ['in'], POINTER(IAgOrientation), 'pOrientation' )),
    COMMETHOD([dispid(404), helpstring('Helper method to set orientation using the AzEl representation.')], HRESULT, 'AssignAzEl',
              ( ['in'], VARIANT, 'Azimuth' ),
              ( ['in'], VARIANT, 'Elevation' ),
              ( ['in'], AgEAzElAboutBoresight, 'AboutBoresight' )),
    COMMETHOD([dispid(405), helpstring('Helper method to set orientation using the Euler angles representation.')], HRESULT, 'AssignEulerAngles',
              ( ['in'], AgEEulerOrientationSequence, 'Sequence' ),
              ( ['in'], VARIANT, 'A' ),
              ( ['in'], VARIANT, 'B' ),
              ( ['in'], VARIANT, 'C' )),
    COMMETHOD([dispid(406), helpstring('Helper method to set orientation using the Quaternion representation.')], HRESULT, 'AssignQuaternion',
              ( ['in'], c_double, 'QX' ),
              ( ['in'], c_double, 'QY' ),
              ( ['in'], c_double, 'QZ' ),
              ( ['in'], c_double, 'QS' )),
    COMMETHOD([dispid(407), helpstring('Helper method to set orientation using the YPR angles representation.')], HRESULT, 'AssignYPRAngles',
              ( ['in'], AgEYPRAnglesSequence, 'Sequence' ),
              ( ['in'], VARIANT, 'Yaw' ),
              ( ['in'], VARIANT, 'Pitch' ),
              ( ['in'], VARIANT, 'Roll' )),
    COMMETHOD([dispid(408), helpstring('Helper method to get orientation using the AzEl representation.')], HRESULT, 'QueryAzEl',
              ( ['out'], POINTER(VARIANT), 'Azimuth' ),
              ( ['out'], POINTER(VARIANT), 'Elevation' ),
              ( ['out'], POINTER(AgEAzElAboutBoresight), 'AboutBoresight' )),
    COMMETHOD([dispid(409), helpstring('Helper method to get orientation using the Euler angles representation.')], HRESULT, 'QueryEulerAngles',
              ( ['in'], AgEEulerOrientationSequence, 'Sequence' ),
              ( ['out'], POINTER(VARIANT), 'A' ),
              ( ['out'], POINTER(VARIANT), 'B' ),
              ( ['out'], POINTER(VARIANT), 'C' )),
    COMMETHOD([dispid(410), helpstring('Helper method to get orientation using the Quaternion representation.')], HRESULT, 'QueryQuaternion',
              ( ['out'], POINTER(c_double), 'QX' ),
              ( ['out'], POINTER(c_double), 'QY' ),
              ( ['out'], POINTER(c_double), 'QZ' ),
              ( ['out'], POINTER(c_double), 'QS' )),
    COMMETHOD([dispid(411), helpstring('Helper method to get orientation using the YPR angles representation.')], HRESULT, 'QueryYPRAngles',
              ( ['in'], AgEYPRAnglesSequence, 'Sequence' ),
              ( ['out'], POINTER(VARIANT), 'Yaw' ),
              ( ['out'], POINTER(VARIANT), 'Pitch' ),
              ( ['out'], POINTER(VARIANT), 'Roll' )),
    COMMETHOD([dispid(412), helpstring('Returns the AzEl elements as an array.')], HRESULT, 'QueryAzElArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(413), helpstring('Returns the Euler elements as an array.')], HRESULT, 'QueryEulerAnglesArray',
              ( ['in'], AgEEulerOrientationSequence, 'Sequence' ),
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(414), helpstring('Returns the Quaternion elements as an array.')], HRESULT, 'QueryQuaternionArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(415), helpstring('Returns the YPR Angles elements as an array.')], HRESULT, 'QueryYPRAnglesArray',
              ( ['in'], AgEYPRAnglesSequence, 'Sequence' ),
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(416), helpstring('Gets or sets the location offset cartesian vector.'), 'propget'], HRESULT, 'PositionOffset',
              ( ['out', 'retval'], POINTER(POINTER(IAgCartesian3Vector)), 'ppRetVal' )),
]
################################################################
## code template for _IAgCROrientationAzEl implementation
##class _IAgCROrientationAzEl_Impl(object):
##    def _get(self):
##        'Measured in the XY plane of the parent reference frame about its Z axis in the right-handed sense for both vehicle-based sensors and facility-based sensors. Uses Angle Dimension.'
##        #return pVal
##    def _set(self, pVal):
##        'Measured in the XY plane of the parent reference frame about its Z axis in the right-handed sense for both vehicle-based sensors and facility-based sensors. Uses Angle Dimension.'
##    Azimuth = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Defined as the angle between the XY plane of the parent reference frame and the sensor or antenna boresight measured toward the positive Z axis. Uses Angle Dimension.'
##        #return pVal
##    def _set(self, pVal):
##        'Defined as the angle between the XY plane of the parent reference frame and the sensor or antenna boresight measured toward the positive Z axis. Uses Angle Dimension.'
##    Elevation = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        "Determines orientation of the X and Y axes with respect to the parent's reference frame."
##        #return pVal
##    def _set(self, pVal):
##        "Determines orientation of the X and Y axes with respect to the parent's reference frame."
##    AboutBoresight = property(_get, _set, doc = _set.__doc__)
##
##    def SetValues(self, Azimuth, Elevation, AboutBoresight):
##        'This property is deprecated. Use AssignAzEl instead.'
##        #return 
##
##    def ConvertTo(self, Type):
##        'Method to change the orientation method to the type specified.'
##        #return ppIAgOrientation
##
##    @property
##    def OrientationType(self):
##        'Returns the orientation method currently being used.'
##        #return pType
##
##    def Assign(self, pOrientation):
##        'Assign a new orientation method.'
##        #return 
##
##    def AssignAzEl(self, Azimuth, Elevation, AboutBoresight):
##        'Helper method to set orientation using the AzEl representation.'
##        #return 
##
##    def AssignEulerAngles(self, Sequence, A, B, C):
##        'Helper method to set orientation using the Euler angles representation.'
##        #return 
##
##    def AssignQuaternion(self, QX, QY, QZ, QS):
##        'Helper method to set orientation using the Quaternion representation.'
##        #return 
##
##    def AssignYPRAngles(self, Sequence, Yaw, Pitch, Roll):
##        'Helper method to set orientation using the YPR angles representation.'
##        #return 
##
##    def QueryAzEl(self):
##        'Helper method to get orientation using the AzEl representation.'
##        #return Azimuth, Elevation, AboutBoresight
##
##    def QueryEulerAngles(self, Sequence):
##        'Helper method to get orientation using the Euler angles representation.'
##        #return A, B, C
##
##    def QueryQuaternion(self):
##        'Helper method to get orientation using the Quaternion representation.'
##        #return QX, QY, QZ, QS
##
##    def QueryYPRAngles(self, Sequence):
##        'Helper method to get orientation using the YPR angles representation.'
##        #return Yaw, Pitch, Roll
##
##    def QueryAzElArray(self):
##        'Returns the AzEl elements as an array.'
##        #return ppRetVal
##
##    def QueryEulerAnglesArray(self, Sequence):
##        'Returns the Euler elements as an array.'
##        #return ppRetVal
##
##    def QueryQuaternionArray(self):
##        'Returns the Quaternion elements as an array.'
##        #return ppRetVal
##
##    def QueryYPRAnglesArray(self, Sequence):
##        'Returns the YPR Angles elements as an array.'
##        #return ppRetVal
##
##    @property
##    def PositionOffset(self):
##        'Gets or sets the location offset cartesian vector.'
##        #return ppRetVal
##

_IAgSpherical._methods_ = [
    COMMETHOD([dispid(201), helpstring('Uses Latitude Dimension.'), 'propget'], HRESULT, 'Lat',
              ( ['out', 'retval'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD([dispid(201), helpstring('Uses Latitude Dimension.'), 'propput'], HRESULT, 'Lat',
              ( ['in'], VARIANT, 'pVal' )),
    COMMETHOD([dispid(202), helpstring('Uses Longitude Dimension.'), 'propget'], HRESULT, 'Lon',
              ( ['out', 'retval'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD([dispid(202), helpstring('Uses Longitude Dimension.'), 'propput'], HRESULT, 'Lon',
              ( ['in'], VARIANT, 'pVal' )),
    COMMETHOD([dispid(203), helpstring('Dimension depends on context.'), 'propget'], HRESULT, 'Radius',
              ( ['out', 'retval'], POINTER(c_double), 'pVal' )),
    COMMETHOD([dispid(203), helpstring('Dimension depends on context.'), 'propput'], HRESULT, 'Radius',
              ( ['in'], c_double, 'pVal' )),
    COMMETHOD([dispid(204), helpstring('This property is deprecated. Use AssignSpherical instead.')], HRESULT, 'SetValues',
              ( ['in'], VARIANT, 'Lat' ),
              ( ['in'], VARIANT, 'Lon' ),
              ( ['in'], c_double, 'Radius' )),
    COMMETHOD([dispid(401), helpstring('Changes the position coordinates to type specified.')], HRESULT, 'ConvertTo',
              ( ['in'], AgEPositionType, 'Type' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgPosition)), 'ppIAgPosition' )),
    COMMETHOD([dispid(402), helpstring('Gets the type of position currently being used.'), 'propget'], HRESULT, 'PosType',
              ( ['out', 'retval'], POINTER(AgEPositionType), 'pType' )),
    COMMETHOD([dispid(403), helpstring('This assigns the coordinates into the system.')], HRESULT, 'Assign',
              ( ['in'], POINTER(IAgPosition), 'pPosition' )),
    COMMETHOD([dispid(404), helpstring('Helper method to assign the position using the Geocentric representation.')], HRESULT, 'AssignGeocentric',
              ( ['in'], VARIANT, 'Lat' ),
              ( ['in'], VARIANT, 'Lon' ),
              ( ['in'], c_double, 'Alt' )),
    COMMETHOD([dispid(405), helpstring('Helper method to assign the position using the Geodetic representation.')], HRESULT, 'AssignGeodetic',
              ( ['in'], VARIANT, 'Lat' ),
              ( ['in'], VARIANT, 'Lon' ),
              ( ['in'], c_double, 'Alt' )),
    COMMETHOD([dispid(406), helpstring('Helper method to assign the position using the Spherical representation')], HRESULT, 'AssignSpherical',
              ( ['in'], VARIANT, 'Lat' ),
              ( ['in'], VARIANT, 'Lon' ),
              ( ['in'], c_double, 'Radius' )),
    COMMETHOD([dispid(407), helpstring('Helper method to assign the position using the Cylindrical representation')], HRESULT, 'AssignCylindrical',
              ( ['in'], c_double, 'Radius' ),
              ( ['in'], c_double, 'Z' ),
              ( ['in'], VARIANT, 'Lon' )),
    COMMETHOD([dispid(408), helpstring('Helper method to assign the position using the Cartesian representation')], HRESULT, 'AssignCartesian',
              ( ['in'], c_double, 'X' ),
              ( ['in'], c_double, 'Y' ),
              ( ['in'], c_double, 'Z' )),
    COMMETHOD([dispid(409), helpstring('Helper method to assign the position using the Planetocentric representation')], HRESULT, 'AssignPlanetocentric',
              ( ['in'], VARIANT, 'Lat' ),
              ( ['in'], VARIANT, 'Lon' ),
              ( ['in'], c_double, 'Alt' )),
    COMMETHOD([dispid(410), helpstring('Helper method to assign the position using the Planetodetic representation')], HRESULT, 'AssignPlanetodetic',
              ( ['in'], VARIANT, 'Lat' ),
              ( ['in'], VARIANT, 'Lon' ),
              ( ['in'], c_double, 'Alt' )),
    COMMETHOD([dispid(411), helpstring('Helper method to get the position using the Planetocentric representation')], HRESULT, 'QueryPlanetocentric',
              ( ['out'], POINTER(VARIANT), 'Lat' ),
              ( ['out'], POINTER(VARIANT), 'Lon' ),
              ( ['out'], POINTER(c_double), 'Alt' )),
    COMMETHOD([dispid(412), helpstring('Helper method to get the position using the Planetodetic representation')], HRESULT, 'QueryPlanetodetic',
              ( ['out'], POINTER(VARIANT), 'Lat' ),
              ( ['out'], POINTER(VARIANT), 'Lon' ),
              ( ['out'], POINTER(c_double), 'Alt' )),
    COMMETHOD([dispid(413), helpstring('Helper method to get the position using the Spherical representation')], HRESULT, 'QuerySpherical',
              ( ['out'], POINTER(VARIANT), 'Lat' ),
              ( ['out'], POINTER(VARIANT), 'Lon' ),
              ( ['out'], POINTER(c_double), 'Radius' )),
    COMMETHOD([dispid(414), helpstring('Helper method to get the position using the Cylindrical representation')], HRESULT, 'QueryCylindrical',
              ( ['out'], POINTER(c_double), 'Radius' ),
              ( ['out'], POINTER(VARIANT), 'Lon' ),
              ( ['out'], POINTER(c_double), 'Z' )),
    COMMETHOD([dispid(415), helpstring('Helper method to get the position using the Cartesian representation')], HRESULT, 'QueryCartesian',
              ( ['out'], POINTER(c_double), 'X' ),
              ( ['out'], POINTER(c_double), 'Y' ),
              ( ['out'], POINTER(c_double), 'Z' )),
    COMMETHOD([dispid(416), helpstring('Gets the central body.'), 'propget'], HRESULT, 'CentralBodyName',
              ( ['out', 'retval'], POINTER(BSTR), 'pCBName' )),
    COMMETHOD([dispid(417), helpstring('Returns the Planetocentric elements as an array.')], HRESULT, 'QueryPlanetocentricArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(418), helpstring('Returns the Planetodetic elements as an array.')], HRESULT, 'QueryPlanetodeticArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(419), helpstring('Returns the Spherical elements as an array.')], HRESULT, 'QuerySphericalArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(420), helpstring('Returns the Cylindrical elements as an array.')], HRESULT, 'QueryCylindricalArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(421), helpstring('Returns the Cartesian elements as an array.')], HRESULT, 'QueryCartesianArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
]
################################################################
## code template for _IAgSpherical implementation
##class _IAgSpherical_Impl(object):
##    def _get(self):
##        'Uses Latitude Dimension.'
##        #return pVal
##    def _set(self, pVal):
##        'Uses Latitude Dimension.'
##    Lat = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Uses Longitude Dimension.'
##        #return pVal
##    def _set(self, pVal):
##        'Uses Longitude Dimension.'
##    Lon = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Dimension depends on context.'
##        #return pVal
##    def _set(self, pVal):
##        'Dimension depends on context.'
##    Radius = property(_get, _set, doc = _set.__doc__)
##
##    def SetValues(self, Lat, Lon, Radius):
##        'This property is deprecated. Use AssignSpherical instead.'
##        #return 
##
##    def ConvertTo(self, Type):
##        'Changes the position coordinates to type specified.'
##        #return ppIAgPosition
##
##    @property
##    def PosType(self):
##        'Gets the type of position currently being used.'
##        #return pType
##
##    def Assign(self, pPosition):
##        'This assigns the coordinates into the system.'
##        #return 
##
##    def AssignGeocentric(self, Lat, Lon, Alt):
##        'Helper method to assign the position using the Geocentric representation.'
##        #return 
##
##    def AssignGeodetic(self, Lat, Lon, Alt):
##        'Helper method to assign the position using the Geodetic representation.'
##        #return 
##
##    def AssignSpherical(self, Lat, Lon, Radius):
##        'Helper method to assign the position using the Spherical representation'
##        #return 
##
##    def AssignCylindrical(self, Radius, Z, Lon):
##        'Helper method to assign the position using the Cylindrical representation'
##        #return 
##
##    def AssignCartesian(self, X, Y, Z):
##        'Helper method to assign the position using the Cartesian representation'
##        #return 
##
##    def AssignPlanetocentric(self, Lat, Lon, Alt):
##        'Helper method to assign the position using the Planetocentric representation'
##        #return 
##
##    def AssignPlanetodetic(self, Lat, Lon, Alt):
##        'Helper method to assign the position using the Planetodetic representation'
##        #return 
##
##    def QueryPlanetocentric(self):
##        'Helper method to get the position using the Planetocentric representation'
##        #return Lat, Lon, Alt
##
##    def QueryPlanetodetic(self):
##        'Helper method to get the position using the Planetodetic representation'
##        #return Lat, Lon, Alt
##
##    def QuerySpherical(self):
##        'Helper method to get the position using the Spherical representation'
##        #return Lat, Lon, Radius
##
##    def QueryCylindrical(self):
##        'Helper method to get the position using the Cylindrical representation'
##        #return Radius, Lon, Z
##
##    def QueryCartesian(self):
##        'Helper method to get the position using the Cartesian representation'
##        #return X, Y, Z
##
##    @property
##    def CentralBodyName(self):
##        'Gets the central body.'
##        #return pCBName
##
##    def QueryPlanetocentricArray(self):
##        'Returns the Planetocentric elements as an array.'
##        #return ppRetVal
##
##    def QueryPlanetodeticArray(self):
##        'Returns the Planetodetic elements as an array.'
##        #return ppRetVal
##
##    def QuerySphericalArray(self):
##        'Returns the Spherical elements as an array.'
##        #return ppRetVal
##
##    def QueryCylindricalArray(self):
##        'Returns the Cylindrical elements as an array.'
##        #return ppRetVal
##
##    def QueryCartesianArray(self):
##        'Returns the Cartesian elements as an array.'
##        #return ppRetVal
##

class AgDoublesCollection(CoClass):
    'A collection of doubles.'
    _reg_clsid_ = GUID('{D266B02C-7030-45BE-9AC0-6481259CCEF9}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{00DD7BD4-53D5-4870-996B-8ADB8AF904FA}', 1, 0)
class IAgDoublesCollection(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Represents a collection of doubles.'
    _iid_ = GUID('{90D75563-26A7-4982-85E9-C3D04B27C552}')
    _idlflags_ = ['dual', 'nonextensible', 'oleautomation']
AgDoublesCollection._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IAgDoublesCollection]

class AgUnitPrefsUnitCollection(CoClass):
    'Object that contains a collection of IAgUnitPrefsUnit.'
    _reg_clsid_ = GUID('{42AED07E-6830-4B20-8CC9-898636F00348}')
    _idlflags_ = ['hidden', 'noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{00DD7BD4-53D5-4870-996B-8ADB8AF904FA}', 1, 0)
AgUnitPrefsUnitCollection._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown, IAgUnitPrefsUnitCollection]

IAgDirectionXYZ._methods_ = [
    COMMETHOD(['propget', helpstring('X component. Dimensionless')], HRESULT, 'X',
              ( ['out', 'retval'], POINTER(c_double), 'pVal' )),
    COMMETHOD(['propput', helpstring('X component. Dimensionless')], HRESULT, 'X',
              ( ['in'], c_double, 'pVal' )),
    COMMETHOD(['propget', helpstring('Y component. Dimensionless')], HRESULT, 'Y',
              ( ['out', 'retval'], POINTER(c_double), 'pVal' )),
    COMMETHOD(['propput', helpstring('Y component. Dimensionless')], HRESULT, 'Y',
              ( ['in'], c_double, 'pVal' )),
    COMMETHOD(['propget', helpstring('Z component. Dimensionless')], HRESULT, 'Z',
              ( ['out', 'retval'], POINTER(c_double), 'pVal' )),
    COMMETHOD(['propput', helpstring('Z component. Dimensionless')], HRESULT, 'Z',
              ( ['in'], c_double, 'pVal' )),
    COMMETHOD([helpstring('This property is deprecated. Use AssignXYZ instead.')], HRESULT, 'SetValues',
              ( ['in'], c_double, 'X' ),
              ( ['in'], c_double, 'Y' ),
              ( ['in'], c_double, 'Z' )),
]
################################################################
## code template for IAgDirectionXYZ implementation
##class IAgDirectionXYZ_Impl(object):
##    def _get(self):
##        'X component. Dimensionless'
##        #return pVal
##    def _set(self, pVal):
##        'X component. Dimensionless'
##    X = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Y component. Dimensionless'
##        #return pVal
##    def _set(self, pVal):
##        'Y component. Dimensionless'
##    Y = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Z component. Dimensionless'
##        #return pVal
##    def _set(self, pVal):
##        'Z component. Dimensionless'
##    Z = property(_get, _set, doc = _set.__doc__)
##
##    def SetValues(self, X, Y, Z):
##        'This property is deprecated. Use AssignXYZ instead.'
##        #return 
##

class _IAgCartesian3Vector(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'A hidden interface for IAgCartesian3Vector.'
    _iid_ = GUID('{8E8A17FF-2237-4541-83B6-3CFA7C3343CA}')
    _idlflags_ = ['hidden', 'dual', 'nonextensible', 'oleautomation']
_IAgCartesian3Vector._methods_ = [
    COMMETHOD([dispid(200), helpstring('X coordinate'), 'propget'], HRESULT, 'X',
              ( ['out', 'retval'], POINTER(c_double), 'pRetVal' )),
    COMMETHOD([dispid(200), helpstring('X coordinate'), 'propput'], HRESULT, 'X',
              ( ['in'], c_double, 'pRetVal' )),
    COMMETHOD([dispid(201), helpstring('Y coordinate'), 'propget'], HRESULT, 'Y',
              ( ['out', 'retval'], POINTER(c_double), 'pRetVal' )),
    COMMETHOD([dispid(201), helpstring('Y coordinate'), 'propput'], HRESULT, 'Y',
              ( ['in'], c_double, 'pRetVal' )),
    COMMETHOD([dispid(202), helpstring('Z coordinate'), 'propget'], HRESULT, 'Z',
              ( ['out', 'retval'], POINTER(c_double), 'pRetVal' )),
    COMMETHOD([dispid(202), helpstring('Z coordinate'), 'propput'], HRESULT, 'Z',
              ( ['in'], c_double, 'pRetVal' )),
    COMMETHOD([dispid(203), helpstring('Returns cartesian vector')], HRESULT, 'Get',
              ( ['out'], POINTER(c_double), 'X' ),
              ( ['out'], POINTER(c_double), 'Y' ),
              ( ['out'], POINTER(c_double), 'Z' )),
    COMMETHOD([dispid(204), helpstring('Sets cartesian vector')], HRESULT, 'Set',
              ( ['in'], c_double, 'X' ),
              ( ['in'], c_double, 'Y' ),
              ( ['in'], c_double, 'Z' )),
    COMMETHOD([dispid(205), helpstring('Returns coordinates as an array.')], HRESULT, 'ToArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
]
################################################################
## code template for _IAgCartesian3Vector implementation
##class _IAgCartesian3Vector_Impl(object):
##    def _get(self):
##        'X coordinate'
##        #return pRetVal
##    def _set(self, pRetVal):
##        'X coordinate'
##    X = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Y coordinate'
##        #return pRetVal
##    def _set(self, pRetVal):
##        'Y coordinate'
##    Y = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Z coordinate'
##        #return pRetVal
##    def _set(self, pRetVal):
##        'Z coordinate'
##    Z = property(_get, _set, doc = _set.__doc__)
##
##    def Get(self):
##        'Returns cartesian vector'
##        #return X, Y, Z
##
##    def Set(self, X, Y, Z):
##        'Sets cartesian vector'
##        #return 
##
##    def ToArray(self):
##        'Returns coordinates as an array.'
##        #return ppRetVal
##

class _IAgUnitPrefsUnit(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'The hidden IAgUnitPrefsUnit interface.'
    _iid_ = GUID('{1414F7A3-88ED-44BE-9A10-9EC2939110B4}')
    _idlflags_ = ['hidden', 'dual', 'nonextensible', 'oleautomation']
_IAgUnitPrefsUnit._methods_ = [
    COMMETHOD([dispid(201), helpstring('Returns the fullname of the unit.'), 'propget'], HRESULT, 'FullName',
              ( ['out', 'retval'], POINTER(BSTR), 'pName' )),
    COMMETHOD([dispid(202), helpstring('Returns the abbreviation of the unit.'), 'propget'], HRESULT, 'Abbrv',
              ( ['out', 'retval'], POINTER(BSTR), 'pAbbrv' )),
    COMMETHOD([dispid(203), helpstring('Returns the ID of the unit.'), 'propget'], HRESULT, 'Id',
              ( ['out', 'retval'], POINTER(c_int), 'pId' )),
    COMMETHOD([dispid(204), helpstring('Returns the Dimension for this unit.'), 'propget'], HRESULT, 'Dimension',
              ( ['out', 'retval'], POINTER(POINTER(IAgUnitPrefsDim)), 'ppUnitPrefsDim' )),
]
################################################################
## code template for _IAgUnitPrefsUnit implementation
##class _IAgUnitPrefsUnit_Impl(object):
##    @property
##    def FullName(self):
##        'Returns the fullname of the unit.'
##        #return pName
##
##    @property
##    def Abbrv(self):
##        'Returns the abbreviation of the unit.'
##        #return pAbbrv
##
##    @property
##    def Id(self):
##        'Returns the ID of the unit.'
##        #return pId
##
##    @property
##    def Dimension(self):
##        'Returns the Dimension for this unit.'
##        #return ppUnitPrefsDim
##

class AgCylindrical(CoClass):
    'Class defining cylindrical position.'
    _reg_clsid_ = GUID('{0C595F9B-4F85-41B7-A162-A85A4518302D}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{00DD7BD4-53D5-4870-996B-8ADB8AF904FA}', 1, 0)
class _IAgCylindrical(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Cylindrical Position Type.'
    _iid_ = GUID('{996BAFFA-0955-41A1-824A-7802F6BFB7AB}')
    _idlflags_ = ['hidden', 'dual', 'nonextensible', 'oleautomation']
AgCylindrical._com_interfaces_ = [_IAgCylindrical, IAgCylindrical, IAgPosition]

_IAgCylindrical._methods_ = [
    COMMETHOD([dispid(201), helpstring('Dimension depends on context.'), 'propget'], HRESULT, 'Radius',
              ( ['out', 'retval'], POINTER(c_double), 'pVal' )),
    COMMETHOD([dispid(201), helpstring('Dimension depends on context.'), 'propput'], HRESULT, 'Radius',
              ( ['in'], c_double, 'pVal' )),
    COMMETHOD([dispid(202), helpstring('Uses Angle Dimension.'), 'propget'], HRESULT, 'Z',
              ( ['out', 'retval'], POINTER(c_double), 'pVal' )),
    COMMETHOD([dispid(202), helpstring('Uses Angle Dimension.'), 'propput'], HRESULT, 'Z',
              ( ['in'], c_double, 'pVal' )),
    COMMETHOD([dispid(203), helpstring('Dimension depends on context.'), 'propget'], HRESULT, 'Lon',
              ( ['out', 'retval'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD([dispid(203), helpstring('Dimension depends on context.'), 'propput'], HRESULT, 'Lon',
              ( ['in'], VARIANT, 'pVal' )),
    COMMETHOD([dispid(204), helpstring('This property is deprecated. Use AssignCylindrical instead.')], HRESULT, 'SetValues',
              ( ['in'], c_double, 'Radius' ),
              ( ['in'], c_double, 'Z' ),
              ( ['in'], VARIANT, 'Lon' )),
    COMMETHOD([dispid(401), helpstring('Changes the position coordinates to type specified.')], HRESULT, 'ConvertTo',
              ( ['in'], AgEPositionType, 'Type' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgPosition)), 'ppIAgPosition' )),
    COMMETHOD([dispid(402), helpstring('Gets the type of position currently being used.'), 'propget'], HRESULT, 'PosType',
              ( ['out', 'retval'], POINTER(AgEPositionType), 'pType' )),
    COMMETHOD([dispid(403), helpstring('This assigns the coordinates into the system.')], HRESULT, 'Assign',
              ( ['in'], POINTER(IAgPosition), 'pPosition' )),
    COMMETHOD([dispid(404), helpstring('Helper method to assign the position using the Geocentric representation.')], HRESULT, 'AssignGeocentric',
              ( ['in'], VARIANT, 'Lat' ),
              ( ['in'], VARIANT, 'Lon' ),
              ( ['in'], c_double, 'Alt' )),
    COMMETHOD([dispid(405), helpstring('Helper method to assign the position using the Geodetic representation.')], HRESULT, 'AssignGeodetic',
              ( ['in'], VARIANT, 'Lat' ),
              ( ['in'], VARIANT, 'Lon' ),
              ( ['in'], c_double, 'Alt' )),
    COMMETHOD([dispid(406), helpstring('Helper method to assign the position using the Spherical representation')], HRESULT, 'AssignSpherical',
              ( ['in'], VARIANT, 'Lat' ),
              ( ['in'], VARIANT, 'Lon' ),
              ( ['in'], c_double, 'Radius' )),
    COMMETHOD([dispid(407), helpstring('Helper method to assign the position using the Cylindrical representation')], HRESULT, 'AssignCylindrical',
              ( ['in'], c_double, 'Radius' ),
              ( ['in'], c_double, 'Z' ),
              ( ['in'], VARIANT, 'Lon' )),
    COMMETHOD([dispid(408), helpstring('Helper method to assign the position using the Cartesian representation')], HRESULT, 'AssignCartesian',
              ( ['in'], c_double, 'X' ),
              ( ['in'], c_double, 'Y' ),
              ( ['in'], c_double, 'Z' )),
    COMMETHOD([dispid(409), helpstring('Helper method to assign the position using the Planetocentric representation')], HRESULT, 'AssignPlanetocentric',
              ( ['in'], VARIANT, 'Lat' ),
              ( ['in'], VARIANT, 'Lon' ),
              ( ['in'], c_double, 'Alt' )),
    COMMETHOD([dispid(410), helpstring('Helper method to assign the position using the Planetodetic representation')], HRESULT, 'AssignPlanetodetic',
              ( ['in'], VARIANT, 'Lat' ),
              ( ['in'], VARIANT, 'Lon' ),
              ( ['in'], c_double, 'Alt' )),
    COMMETHOD([dispid(411), helpstring('Helper method to get the position using the Planetocentric representation')], HRESULT, 'QueryPlanetocentric',
              ( ['out'], POINTER(VARIANT), 'Lat' ),
              ( ['out'], POINTER(VARIANT), 'Lon' ),
              ( ['out'], POINTER(c_double), 'Alt' )),
    COMMETHOD([dispid(412), helpstring('Helper method to get the position using the Planetodetic representation')], HRESULT, 'QueryPlanetodetic',
              ( ['out'], POINTER(VARIANT), 'Lat' ),
              ( ['out'], POINTER(VARIANT), 'Lon' ),
              ( ['out'], POINTER(c_double), 'Alt' )),
    COMMETHOD([dispid(413), helpstring('Helper method to get the position using the Spherical representation')], HRESULT, 'QuerySpherical',
              ( ['out'], POINTER(VARIANT), 'Lat' ),
              ( ['out'], POINTER(VARIANT), 'Lon' ),
              ( ['out'], POINTER(c_double), 'Radius' )),
    COMMETHOD([dispid(414), helpstring('Helper method to get the position using the Cylindrical representation')], HRESULT, 'QueryCylindrical',
              ( ['out'], POINTER(c_double), 'Radius' ),
              ( ['out'], POINTER(VARIANT), 'Lon' ),
              ( ['out'], POINTER(c_double), 'Z' )),
    COMMETHOD([dispid(415), helpstring('Helper method to get the position using the Cartesian representation')], HRESULT, 'QueryCartesian',
              ( ['out'], POINTER(c_double), 'X' ),
              ( ['out'], POINTER(c_double), 'Y' ),
              ( ['out'], POINTER(c_double), 'Z' )),
    COMMETHOD([dispid(416), helpstring('Gets the central body.'), 'propget'], HRESULT, 'CentralBodyName',
              ( ['out', 'retval'], POINTER(BSTR), 'pCBName' )),
    COMMETHOD([dispid(417), helpstring('Returns the Planetocentric elements as an array.')], HRESULT, 'QueryPlanetocentricArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(418), helpstring('Returns the Planetodetic elements as an array.')], HRESULT, 'QueryPlanetodeticArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(419), helpstring('Returns the Spherical elements as an array.')], HRESULT, 'QuerySphericalArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(420), helpstring('Returns the Cylindrical elements as an array.')], HRESULT, 'QueryCylindricalArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(421), helpstring('Returns the Cartesian elements as an array.')], HRESULT, 'QueryCartesianArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
]
################################################################
## code template for _IAgCylindrical implementation
##class _IAgCylindrical_Impl(object):
##    def _get(self):
##        'Dimension depends on context.'
##        #return pVal
##    def _set(self, pVal):
##        'Dimension depends on context.'
##    Radius = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Uses Angle Dimension.'
##        #return pVal
##    def _set(self, pVal):
##        'Uses Angle Dimension.'
##    Z = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Dimension depends on context.'
##        #return pVal
##    def _set(self, pVal):
##        'Dimension depends on context.'
##    Lon = property(_get, _set, doc = _set.__doc__)
##
##    def SetValues(self, Radius, Z, Lon):
##        'This property is deprecated. Use AssignCylindrical instead.'
##        #return 
##
##    def ConvertTo(self, Type):
##        'Changes the position coordinates to type specified.'
##        #return ppIAgPosition
##
##    @property
##    def PosType(self):
##        'Gets the type of position currently being used.'
##        #return pType
##
##    def Assign(self, pPosition):
##        'This assigns the coordinates into the system.'
##        #return 
##
##    def AssignGeocentric(self, Lat, Lon, Alt):
##        'Helper method to assign the position using the Geocentric representation.'
##        #return 
##
##    def AssignGeodetic(self, Lat, Lon, Alt):
##        'Helper method to assign the position using the Geodetic representation.'
##        #return 
##
##    def AssignSpherical(self, Lat, Lon, Radius):
##        'Helper method to assign the position using the Spherical representation'
##        #return 
##
##    def AssignCylindrical(self, Radius, Z, Lon):
##        'Helper method to assign the position using the Cylindrical representation'
##        #return 
##
##    def AssignCartesian(self, X, Y, Z):
##        'Helper method to assign the position using the Cartesian representation'
##        #return 
##
##    def AssignPlanetocentric(self, Lat, Lon, Alt):
##        'Helper method to assign the position using the Planetocentric representation'
##        #return 
##
##    def AssignPlanetodetic(self, Lat, Lon, Alt):
##        'Helper method to assign the position using the Planetodetic representation'
##        #return 
##
##    def QueryPlanetocentric(self):
##        'Helper method to get the position using the Planetocentric representation'
##        #return Lat, Lon, Alt
##
##    def QueryPlanetodetic(self):
##        'Helper method to get the position using the Planetodetic representation'
##        #return Lat, Lon, Alt
##
##    def QuerySpherical(self):
##        'Helper method to get the position using the Spherical representation'
##        #return Lat, Lon, Radius
##
##    def QueryCylindrical(self):
##        'Helper method to get the position using the Cylindrical representation'
##        #return Radius, Lon, Z
##
##    def QueryCartesian(self):
##        'Helper method to get the position using the Cartesian representation'
##        #return X, Y, Z
##
##    @property
##    def CentralBodyName(self):
##        'Gets the central body.'
##        #return pCBName
##
##    def QueryPlanetocentricArray(self):
##        'Returns the Planetocentric elements as an array.'
##        #return ppRetVal
##
##    def QueryPlanetodeticArray(self):
##        'Returns the Planetodetic elements as an array.'
##        #return ppRetVal
##
##    def QuerySphericalArray(self):
##        'Returns the Spherical elements as an array.'
##        #return ppRetVal
##
##    def QueryCylindricalArray(self):
##        'Returns the Cylindrical elements as an array.'
##        #return ppRetVal
##
##    def QueryCartesianArray(self):
##        'Returns the Cartesian elements as an array.'
##        #return ppRetVal
##

IAgDoublesCollection._methods_ = [
    COMMETHOD([dispid(0), helpstring('Returns a double at a specified position.'), 'propget'], HRESULT, 'Item',
              ( ['in'], c_int, 'Index' ),
              ( ['out', 'retval'], POINTER(c_double), 'pVal' )),
    COMMETHOD([dispid(201), helpstring('Returns the number of items in the collection.'), 'propget'], HRESULT, 'Count',
              ( ['out', 'retval'], POINTER(c_int), 'pVal' )),
    COMMETHOD([dispid(-4), helpstring('Returns a collection enumerator.'), 'propget'], HRESULT, '_NewEnum',
              ( ['out', 'retval'], POINTER(POINTER(IUnknown)), 'ppRetVal' )),
    COMMETHOD([dispid(202), helpstring('Add a value to the collection of doubles.')], HRESULT, 'Add',
              ( ['in'], c_double, 'Value' )),
    COMMETHOD([dispid(203), helpstring('Remove an element from the collection at a specified position.')], HRESULT, 'RemoveAt',
              ( ['in'], c_int, 'Index' )),
    COMMETHOD([dispid(205), helpstring('Clears the collection.')], HRESULT, 'RemoveAll'),
    COMMETHOD([dispid(206), helpstring('Returns an array of the elements in the collection')], HRESULT, 'ToArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(207), helpstring('Updates an element in the collection at a specified position.')], HRESULT, 'SetAt',
              ( ['in'], c_int, 'Index' ),
              ( ['in'], c_double, 'Value' )),
]
################################################################
## code template for IAgDoublesCollection implementation
##class IAgDoublesCollection_Impl(object):
##    @property
##    def Item(self, Index):
##        'Returns a double at a specified position.'
##        #return pVal
##
##    @property
##    def Count(self):
##        'Returns the number of items in the collection.'
##        #return pVal
##
##    @property
##    def _NewEnum(self):
##        'Returns a collection enumerator.'
##        #return ppRetVal
##
##    def Add(self, Value):
##        'Add a value to the collection of doubles.'
##        #return 
##
##    def RemoveAt(self, Index):
##        'Remove an element from the collection at a specified position.'
##        #return 
##
##    def RemoveAll(self):
##        'Clears the collection.'
##        #return 
##
##    def ToArray(self):
##        'Returns an array of the elements in the collection'
##        #return ppRetVal
##
##    def SetAt(self, Index, Value):
##        'Updates an element in the collection at a specified position.'
##        #return 
##

class AgCartesian3Vector(CoClass):
    'A 3-D cartesian vector.'
    _reg_clsid_ = GUID('{24E2567A-7785-4B8F-9D08-FD927E5AD85A}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{00DD7BD4-53D5-4870-996B-8ADB8AF904FA}', 1, 0)
AgCartesian3Vector._com_interfaces_ = [_IAgCartesian3Vector, IAgCartesian3Vector]

class AgUnitPrefsUnit(CoClass):
    'Object that contains info on the unit.'
    _reg_clsid_ = GUID('{05A8DB56-3475-4442-933C-5B1B66DEAD3A}')
    _idlflags_ = ['hidden', 'noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{00DD7BD4-53D5-4870-996B-8ADB8AF904FA}', 1, 0)
AgUnitPrefsUnit._com_interfaces_ = [_IAgUnitPrefsUnit, IAgUnitPrefsUnit]

class AgDirectionRADec(CoClass):
    'Spherical direction (Right Ascension and Declination).'
    _reg_clsid_ = GUID('{BCA34CA1-7A0B-4299-BA8B-EE8E177DFD98}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{00DD7BD4-53D5-4870-996B-8ADB8AF904FA}', 1, 0)
class _IAgDirectionRADec(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'The hidden interface for IAgDirectionRADec'
    _iid_ = GUID('{71D2F7A6-A509-4840-A3D6-15AD14F7B0F3}')
    _idlflags_ = ['hidden', 'dual', 'nonextensible', 'oleautomation']
AgDirectionRADec._com_interfaces_ = [_IAgDirectionRADec, IAgDirectionRADec, IAgDirection]

class _IAgOrientationAzEl(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'The hidden interface for IAgOrientationAzEl'
    _iid_ = GUID('{3D37AE5E-5D7C-429E-B14F-03B5A7594C69}')
    _idlflags_ = ['hidden', 'dual', 'nonextensible', 'oleautomation']
_IAgOrientationAzEl._methods_ = [
    COMMETHOD([dispid(201), helpstring('Measured in the XY plane of the parent reference frame about its Z axis in the right-handed sense for both vehicle-based sensors and facility-based sensors. Uses Angle Dimension.'), 'propget'], HRESULT, 'Azimuth',
              ( ['out', 'retval'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD([dispid(201), helpstring('Measured in the XY plane of the parent reference frame about its Z axis in the right-handed sense for both vehicle-based sensors and facility-based sensors. Uses Angle Dimension.'), 'propput'], HRESULT, 'Azimuth',
              ( ['in'], VARIANT, 'pVal' )),
    COMMETHOD([dispid(202), helpstring('Defined as the angle between the XY plane of the parent reference frame and the sensor or antenna boresight measured toward the positive Z axis. Uses Angle Dimension.'), 'propget'], HRESULT, 'Elevation',
              ( ['out', 'retval'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD([dispid(202), helpstring('Defined as the angle between the XY plane of the parent reference frame and the sensor or antenna boresight measured toward the positive Z axis. Uses Angle Dimension.'), 'propput'], HRESULT, 'Elevation',
              ( ['in'], VARIANT, 'pVal' )),
    COMMETHOD([dispid(203), helpstring("Determines orientation of the X and Y axes with respect to the parent's reference frame."), 'propget'], HRESULT, 'AboutBoresight',
              ( ['out', 'retval'], POINTER(AgEAzElAboutBoresight), 'pVal' )),
    COMMETHOD([dispid(203), helpstring("Determines orientation of the X and Y axes with respect to the parent's reference frame."), 'propput'], HRESULT, 'AboutBoresight',
              ( ['in'], AgEAzElAboutBoresight, 'pVal' )),
    COMMETHOD([dispid(204), helpstring('This property is deprecated. Use AssignAzEl instead.')], HRESULT, 'SetValues',
              ( ['in'], VARIANT, 'Azimuth' ),
              ( ['in'], VARIANT, 'Elevation' ),
              ( ['in'], AgEAzElAboutBoresight, 'AboutBoresight' )),
    COMMETHOD([dispid(401), helpstring('Method to change the orientation method to the type specified.')], HRESULT, 'ConvertTo',
              ( ['in'], AgEOrientationType, 'Type' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgOrientation)), 'ppIAgOrientation' )),
    COMMETHOD([dispid(402), helpstring('Returns the orientation method currently being used.'), 'propget'], HRESULT, 'OrientationType',
              ( ['out', 'retval'], POINTER(AgEOrientationType), 'pType' )),
    COMMETHOD([dispid(403), helpstring('Assign a new orientation method.')], HRESULT, 'Assign',
              ( ['in'], POINTER(IAgOrientation), 'pOrientation' )),
    COMMETHOD([dispid(404), helpstring('Helper method to set orientation using the AzEl representation.')], HRESULT, 'AssignAzEl',
              ( ['in'], VARIANT, 'Azimuth' ),
              ( ['in'], VARIANT, 'Elevation' ),
              ( ['in'], AgEAzElAboutBoresight, 'AboutBoresight' )),
    COMMETHOD([dispid(405), helpstring('Helper method to set orientation using the Euler angles representation.')], HRESULT, 'AssignEulerAngles',
              ( ['in'], AgEEulerOrientationSequence, 'Sequence' ),
              ( ['in'], VARIANT, 'A' ),
              ( ['in'], VARIANT, 'B' ),
              ( ['in'], VARIANT, 'C' )),
    COMMETHOD([dispid(406), helpstring('Helper method to set orientation using the Quaternion representation.')], HRESULT, 'AssignQuaternion',
              ( ['in'], c_double, 'QX' ),
              ( ['in'], c_double, 'QY' ),
              ( ['in'], c_double, 'QZ' ),
              ( ['in'], c_double, 'QS' )),
    COMMETHOD([dispid(407), helpstring('Helper method to set orientation using the YPR angles representation.')], HRESULT, 'AssignYPRAngles',
              ( ['in'], AgEYPRAnglesSequence, 'Sequence' ),
              ( ['in'], VARIANT, 'Yaw' ),
              ( ['in'], VARIANT, 'Pitch' ),
              ( ['in'], VARIANT, 'Roll' )),
    COMMETHOD([dispid(408), helpstring('Helper method to get orientation using the AzEl representation.')], HRESULT, 'QueryAzEl',
              ( ['out'], POINTER(VARIANT), 'Azimuth' ),
              ( ['out'], POINTER(VARIANT), 'Elevation' ),
              ( ['out'], POINTER(AgEAzElAboutBoresight), 'AboutBoresight' )),
    COMMETHOD([dispid(409), helpstring('Helper method to get orientation using the Euler angles representation.')], HRESULT, 'QueryEulerAngles',
              ( ['in'], AgEEulerOrientationSequence, 'Sequence' ),
              ( ['out'], POINTER(VARIANT), 'A' ),
              ( ['out'], POINTER(VARIANT), 'B' ),
              ( ['out'], POINTER(VARIANT), 'C' )),
    COMMETHOD([dispid(410), helpstring('Helper method to get orientation using the Quaternion representation.')], HRESULT, 'QueryQuaternion',
              ( ['out'], POINTER(c_double), 'QX' ),
              ( ['out'], POINTER(c_double), 'QY' ),
              ( ['out'], POINTER(c_double), 'QZ' ),
              ( ['out'], POINTER(c_double), 'QS' )),
    COMMETHOD([dispid(411), helpstring('Helper method to get orientation using the YPR angles representation.')], HRESULT, 'QueryYPRAngles',
              ( ['in'], AgEYPRAnglesSequence, 'Sequence' ),
              ( ['out'], POINTER(VARIANT), 'Yaw' ),
              ( ['out'], POINTER(VARIANT), 'Pitch' ),
              ( ['out'], POINTER(VARIANT), 'Roll' )),
    COMMETHOD([dispid(412), helpstring('Returns the AzEl elements as an array.')], HRESULT, 'QueryAzElArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(413), helpstring('Returns the Euler elements as an array.')], HRESULT, 'QueryEulerAnglesArray',
              ( ['in'], AgEEulerOrientationSequence, 'Sequence' ),
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(414), helpstring('Returns the Quaternion elements as an array.')], HRESULT, 'QueryQuaternionArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(415), helpstring('Returns the YPR Angles elements as an array.')], HRESULT, 'QueryYPRAnglesArray',
              ( ['in'], AgEYPRAnglesSequence, 'Sequence' ),
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
]
################################################################
## code template for _IAgOrientationAzEl implementation
##class _IAgOrientationAzEl_Impl(object):
##    def _get(self):
##        'Measured in the XY plane of the parent reference frame about its Z axis in the right-handed sense for both vehicle-based sensors and facility-based sensors. Uses Angle Dimension.'
##        #return pVal
##    def _set(self, pVal):
##        'Measured in the XY plane of the parent reference frame about its Z axis in the right-handed sense for both vehicle-based sensors and facility-based sensors. Uses Angle Dimension.'
##    Azimuth = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Defined as the angle between the XY plane of the parent reference frame and the sensor or antenna boresight measured toward the positive Z axis. Uses Angle Dimension.'
##        #return pVal
##    def _set(self, pVal):
##        'Defined as the angle between the XY plane of the parent reference frame and the sensor or antenna boresight measured toward the positive Z axis. Uses Angle Dimension.'
##    Elevation = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        "Determines orientation of the X and Y axes with respect to the parent's reference frame."
##        #return pVal
##    def _set(self, pVal):
##        "Determines orientation of the X and Y axes with respect to the parent's reference frame."
##    AboutBoresight = property(_get, _set, doc = _set.__doc__)
##
##    def SetValues(self, Azimuth, Elevation, AboutBoresight):
##        'This property is deprecated. Use AssignAzEl instead.'
##        #return 
##
##    def ConvertTo(self, Type):
##        'Method to change the orientation method to the type specified.'
##        #return ppIAgOrientation
##
##    @property
##    def OrientationType(self):
##        'Returns the orientation method currently being used.'
##        #return pType
##
##    def Assign(self, pOrientation):
##        'Assign a new orientation method.'
##        #return 
##
##    def AssignAzEl(self, Azimuth, Elevation, AboutBoresight):
##        'Helper method to set orientation using the AzEl representation.'
##        #return 
##
##    def AssignEulerAngles(self, Sequence, A, B, C):
##        'Helper method to set orientation using the Euler angles representation.'
##        #return 
##
##    def AssignQuaternion(self, QX, QY, QZ, QS):
##        'Helper method to set orientation using the Quaternion representation.'
##        #return 
##
##    def AssignYPRAngles(self, Sequence, Yaw, Pitch, Roll):
##        'Helper method to set orientation using the YPR angles representation.'
##        #return 
##
##    def QueryAzEl(self):
##        'Helper method to get orientation using the AzEl representation.'
##        #return Azimuth, Elevation, AboutBoresight
##
##    def QueryEulerAngles(self, Sequence):
##        'Helper method to get orientation using the Euler angles representation.'
##        #return A, B, C
##
##    def QueryQuaternion(self):
##        'Helper method to get orientation using the Quaternion representation.'
##        #return QX, QY, QZ, QS
##
##    def QueryYPRAngles(self, Sequence):
##        'Helper method to get orientation using the YPR angles representation.'
##        #return Yaw, Pitch, Roll
##
##    def QueryAzElArray(self):
##        'Returns the AzEl elements as an array.'
##        #return ppRetVal
##
##    def QueryEulerAnglesArray(self, Sequence):
##        'Returns the Euler elements as an array.'
##        #return ppRetVal
##
##    def QueryQuaternionArray(self):
##        'Returns the Quaternion elements as an array.'
##        #return ppRetVal
##
##    def QueryYPRAnglesArray(self, Sequence):
##        'Returns the YPR Angles elements as an array.'
##        #return ppRetVal
##

class AgCROrientationAzEl(CoClass):
    'AzEl orientation method.'
    _reg_clsid_ = GUID('{D9EF4E97-361B-4D0A-A9ED-20CB6637EF2E}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{00DD7BD4-53D5-4870-996B-8ADB8AF904FA}', 1, 0)
AgCROrientationAzEl._com_interfaces_ = [_IAgCROrientationAzEl, IAgOrientationAzEl, IAgOrientation, IAgOrientationPositionOffset]

_IAgDirectionRADec._methods_ = [
    COMMETHOD([dispid(201), helpstring('Declination: angle above the x-y plane. Uses Latitude Dimension.'), 'propget'], HRESULT, 'Dec',
              ( ['out', 'retval'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD([dispid(201), helpstring('Declination: angle above the x-y plane. Uses Latitude Dimension.'), 'propput'], HRESULT, 'Dec',
              ( ['in'], VARIANT, 'pVal' )),
    COMMETHOD([dispid(202), helpstring('Right Ascension: angle in x-y plane from x towards y. Uses Longitude Dimension.'), 'propget'], HRESULT, 'RA',
              ( ['out', 'retval'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD([dispid(202), helpstring('Right Ascension: angle in x-y plane from x towards y. Uses Longitude Dimension.'), 'propput'], HRESULT, 'RA',
              ( ['in'], VARIANT, 'pVal' )),
    COMMETHOD([dispid(203), helpstring('This property is deprecated. Use AssignRADec instead.')], HRESULT, 'SetValues',
              ( ['in'], VARIANT, 'RA' ),
              ( ['in'], VARIANT, 'Dec' )),
    COMMETHOD([dispid(401), helpstring('Method to changes the direction to the type specified.')], HRESULT, 'ConvertTo',
              ( ['in'], AgEDirectionType, 'Type' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgDirection)), 'ppIAgDirection' )),
    COMMETHOD([dispid(402), helpstring('Returns the type of direction currently being used.'), 'propget'], HRESULT, 'DirectionType',
              ( ['out', 'retval'], POINTER(AgEDirectionType), 'pType' )),
    COMMETHOD([dispid(403), helpstring('Assign a new direction.')], HRESULT, 'Assign',
              ( ['in'], POINTER(IAgDirection), 'pDirection' )),
    COMMETHOD([dispid(404), helpstring('Helper method to set direction using the Euler representation. Params B and C use Angle Dimension.')], HRESULT, 'AssignEuler',
              ( ['in'], VARIANT, 'B' ),
              ( ['in'], VARIANT, 'C' ),
              ( ['in'], AgEEulerDirectionSequence, 'Sequence' )),
    COMMETHOD([dispid(405), helpstring('Helper method to set direction using the Pitch Roll representation. Pitch and Roll use Angle Dimension.')], HRESULT, 'AssignPR',
              ( ['in'], VARIANT, 'Pitch' ),
              ( ['in'], VARIANT, 'Roll' )),
    COMMETHOD([dispid(406), helpstring('Helper method to set direction using the Right Ascension and Declination representation. Param Dec uses Latitude. Param RA uses Longitude.')], HRESULT, 'AssignRADec',
              ( ['in'], VARIANT, 'RA' ),
              ( ['in'], VARIANT, 'Dec' )),
    COMMETHOD([dispid(407), helpstring('Helper method to set direction using the Cartesian representation. Params X, Y and Z are dimensionless.')], HRESULT, 'AssignXYZ',
              ( ['in'], c_double, 'X' ),
              ( ['in'], c_double, 'Y' ),
              ( ['in'], c_double, 'Z' )),
    COMMETHOD([dispid(408), helpstring('Helper method to get direction using the Euler representation. Params B and C use Angle Dimension.')], HRESULT, 'QueryEuler',
              ( ['in'], AgEEulerDirectionSequence, 'Sequence' ),
              ( ['out'], POINTER(VARIANT), 'B' ),
              ( ['out'], POINTER(VARIANT), 'C' )),
    COMMETHOD([dispid(409), helpstring('Helper method to get direction using the Pitch Roll representation. Pitch and Roll use Angle Dimension.')], HRESULT, 'QueryPR',
              ( ['in'], AgEPRSequence, 'Sequence' ),
              ( ['out'], POINTER(VARIANT), 'Pitch' ),
              ( ['out'], POINTER(VARIANT), 'Roll' )),
    COMMETHOD([dispid(410), helpstring('Helper method to get direction using the Right Ascension and Declination representation. Param Dec uses Latitude. Param RA uses Longitude.')], HRESULT, 'QueryRADec',
              ( ['out'], POINTER(VARIANT), 'RA' ),
              ( ['out'], POINTER(VARIANT), 'Dec' )),
    COMMETHOD([dispid(411), helpstring('Helper method to get direction using the Cartesian representation. Params X, Y and Z are dimensionless.')], HRESULT, 'QueryXYZ',
              ( ['out'], POINTER(c_double), 'X' ),
              ( ['out'], POINTER(c_double), 'Y' ),
              ( ['out'], POINTER(c_double), 'Z' )),
    COMMETHOD([dispid(412), helpstring('Returns the Euler elements in an array.')], HRESULT, 'QueryEulerArray',
              ( ['in'], AgEEulerDirectionSequence, 'Sequence' ),
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(413), helpstring('Returns the PR elements in an array.')], HRESULT, 'QueryPRArray',
              ( ['in'], AgEPRSequence, 'Sequence' ),
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(414), helpstring('Returns the RADec elements in an array.')], HRESULT, 'QueryRADecArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(415), helpstring('Returns the XYZ elements in an array.')], HRESULT, 'QueryXYZArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(416), helpstring('A unitless value that represents magnitude.'), 'propget'], HRESULT, 'Magnitude',
              ( ['out', 'retval'], POINTER(c_double), 'pVal' )),
    COMMETHOD([dispid(416), helpstring('A unitless value that represents magnitude.'), 'propput'], HRESULT, 'Magnitude',
              ( ['in'], c_double, 'pVal' )),
]
################################################################
## code template for _IAgDirectionRADec implementation
##class _IAgDirectionRADec_Impl(object):
##    def _get(self):
##        'Declination: angle above the x-y plane. Uses Latitude Dimension.'
##        #return pVal
##    def _set(self, pVal):
##        'Declination: angle above the x-y plane. Uses Latitude Dimension.'
##    Dec = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Right Ascension: angle in x-y plane from x towards y. Uses Longitude Dimension.'
##        #return pVal
##    def _set(self, pVal):
##        'Right Ascension: angle in x-y plane from x towards y. Uses Longitude Dimension.'
##    RA = property(_get, _set, doc = _set.__doc__)
##
##    def SetValues(self, RA, Dec):
##        'This property is deprecated. Use AssignRADec instead.'
##        #return 
##
##    def ConvertTo(self, Type):
##        'Method to changes the direction to the type specified.'
##        #return ppIAgDirection
##
##    @property
##    def DirectionType(self):
##        'Returns the type of direction currently being used.'
##        #return pType
##
##    def Assign(self, pDirection):
##        'Assign a new direction.'
##        #return 
##
##    def AssignEuler(self, B, C, Sequence):
##        'Helper method to set direction using the Euler representation. Params B and C use Angle Dimension.'
##        #return 
##
##    def AssignPR(self, Pitch, Roll):
##        'Helper method to set direction using the Pitch Roll representation. Pitch and Roll use Angle Dimension.'
##        #return 
##
##    def AssignRADec(self, RA, Dec):
##        'Helper method to set direction using the Right Ascension and Declination representation. Param Dec uses Latitude. Param RA uses Longitude.'
##        #return 
##
##    def AssignXYZ(self, X, Y, Z):
##        'Helper method to set direction using the Cartesian representation. Params X, Y and Z are dimensionless.'
##        #return 
##
##    def QueryEuler(self, Sequence):
##        'Helper method to get direction using the Euler representation. Params B and C use Angle Dimension.'
##        #return B, C
##
##    def QueryPR(self, Sequence):
##        'Helper method to get direction using the Pitch Roll representation. Pitch and Roll use Angle Dimension.'
##        #return Pitch, Roll
##
##    def QueryRADec(self):
##        'Helper method to get direction using the Right Ascension and Declination representation. Param Dec uses Latitude. Param RA uses Longitude.'
##        #return RA, Dec
##
##    def QueryXYZ(self):
##        'Helper method to get direction using the Cartesian representation. Params X, Y and Z are dimensionless.'
##        #return X, Y, Z
##
##    def QueryEulerArray(self, Sequence):
##        'Returns the Euler elements in an array.'
##        #return ppRetVal
##
##    def QueryPRArray(self, Sequence):
##        'Returns the PR elements in an array.'
##        #return ppRetVal
##
##    def QueryRADecArray(self):
##        'Returns the RADec elements in an array.'
##        #return ppRetVal
##
##    def QueryXYZArray(self):
##        'Returns the XYZ elements in an array.'
##        #return ppRetVal
##
##    def _get(self):
##        'A unitless value that represents magnitude.'
##        #return pVal
##    def _set(self, pVal):
##        'A unitless value that represents magnitude.'
##    Magnitude = property(_get, _set, doc = _set.__doc__)
##

class AgOrientationAzEl(CoClass):
    'AzEl orientation method.'
    _reg_clsid_ = GUID('{C2D2A4ED-2A08-48B8-B479-6996EF33D8E3}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{00DD7BD4-53D5-4870-996B-8ADB8AF904FA}', 1, 0)
AgOrientationAzEl._com_interfaces_ = [_IAgOrientationAzEl, IAgOrientationAzEl, IAgOrientation]

IAgConversionUtility._methods_ = [
    COMMETHOD([helpstring('Converts the specified quantity value from a given unit to another unit.')], HRESULT, 'ConvertQuantity',
              ( ['in'], BSTR, 'DimensionName' ),
              ( ['in'], BSTR, 'FromUnit' ),
              ( ['in'], BSTR, 'ToUnit' ),
              ( ['in'], c_double, 'FromValue' ),
              ( ['out', 'retval'], POINTER(c_double), 'pToValue' )),
    COMMETHOD([helpstring('Converts the specified date from a given unit to another unit.')], HRESULT, 'ConvertDate',
              ( ['in'], BSTR, 'FromUnit' ),
              ( ['in'], BSTR, 'ToUnit' ),
              ( ['in'], BSTR, 'FromValue' ),
              ( ['out', 'retval'], POINTER(BSTR), 'pToValue' )),
    COMMETHOD([helpstring('Converts the specified quantity values from a given unit to another unit.')], HRESULT, 'ConvertQuantityArray',
              ( ['in'], BSTR, 'DimensionName' ),
              ( ['in'], BSTR, 'FromUnit' ),
              ( ['in'], BSTR, 'ToUnit' ),
              ( ['in'], POINTER(_midlSAFEARRAY(VARIANT)), 'QuantityValues' ),
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppConvertedQuantityValues' )),
    COMMETHOD([helpstring('Converts the specified dates from a given unit to another unit.')], HRESULT, 'ConvertDateArray',
              ( ['in'], BSTR, 'FromUnit' ),
              ( ['in'], BSTR, 'ToUnit' ),
              ( ['in'], POINTER(_midlSAFEARRAY(VARIANT)), 'FromValues' ),
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppConvertedDateValues' )),
    COMMETHOD([helpstring('Creates an IAgQuantity interface with the given dimension, unit and value')], HRESULT, 'NewQuantity',
              ( ['in'], BSTR, 'Dimension' ),
              ( ['in'], BSTR, 'UnitAbbrv' ),
              ( ['in'], c_double, 'Value' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgQuantity)), 'ppQuantity' )),
    COMMETHOD([helpstring('Creates an IAgDate interface with the given unit and value')], HRESULT, 'NewDate',
              ( ['in'], BSTR, 'UnitAbbrv' ),
              ( ['in'], BSTR, 'Value' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgDate)), 'ppDate' )),
    COMMETHOD([helpstring("Creates an IAgPosition interface with earth as it's central body.")], HRESULT, 'NewPositionOnEarth',
              ( ['out', 'retval'], POINTER(POINTER(IAgPosition)), 'ppRetVal' )),
    COMMETHOD([helpstring('Converts the specified position values from a given position type to another position type.')], HRESULT, 'ConvertPositionArray',
              ( ['in'], AgEPositionType, 'PositionType' ),
              ( ['in'], POINTER(_midlSAFEARRAY(VARIANT)), 'PositionArray' ),
              ( ['in'], AgEPositionType, 'ConvertTo' ),
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppOutVal' )),
    COMMETHOD([helpstring('Creates an IAgDirection interface.')], HRESULT, 'NewDirection',
              ( ['out', 'retval'], POINTER(POINTER(IAgDirection)), 'ppRetVal' )),
    COMMETHOD([helpstring('Creates an IAgOrientation interface.')], HRESULT, 'NewOrientation',
              ( ['out', 'retval'], POINTER(POINTER(IAgOrientation)), 'ppRetVal' )),
    COMMETHOD([helpstring("Creates an IAgOrbitState interface with earth as it's central body.")], HRESULT, 'NewOrbitStateOnEarth',
              ( ['out', 'retval'], POINTER(POINTER(IAgOrbitState)), 'ppRetVal' )),
    COMMETHOD([helpstring('Creates an IAgPosition interface using the supplied central body.')], HRESULT, 'NewPositionOnCB',
              ( ['in'], BSTR, 'CentralBodyName' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgPosition)), 'ppRetVal' )),
    COMMETHOD([helpstring('Creates an IAgOrbitState interface using the supplied central body.')], HRESULT, 'NewOrbitStateOnCB',
              ( ['in'], BSTR, 'CentralBodyName' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgOrbitState)), 'ppRetVal' )),
    COMMETHOD([helpstring('Returns a Direction Cosine Matrix (DCM).')], HRESULT, 'QueryDirectionCosineMatrix',
              ( ['in'], POINTER(IAgOrientation), 'InputOrientation' ),
              ( ['out'], POINTER(POINTER(IAgCartesian3Vector)), 'pX' ),
              ( ['out'], POINTER(POINTER(IAgCartesian3Vector)), 'pY' ),
              ( ['out'], POINTER(POINTER(IAgCartesian3Vector)), 'pZ' )),
    COMMETHOD([helpstring('Returns a Direction Cosine Matrix (DCM) as an array.')], HRESULT, 'QueryDirectionCosineMatrixArray',
              ( ['in'], POINTER(IAgOrientation), 'InputOrientation' ),
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([helpstring('Creates a cartesian vector.')], HRESULT, 'NewCartesian3Vector',
              ( ['out', 'retval'], POINTER(POINTER(IAgCartesian3Vector)), 'ppRetVal' )),
    COMMETHOD([helpstring('Converts the direction to cartesian vector.')], HRESULT, 'NewCartesian3VectorFromDirection',
              ( ['in'], POINTER(IAgDirection), 'InputDirection' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgCartesian3Vector)), 'ppRetVal' )),
    COMMETHOD([helpstring('Converts the position to cartesian vector.')], HRESULT, 'NewCartesian3VectorFromPosition',
              ( ['in'], POINTER(IAgPosition), 'InputPosition' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgCartesian3Vector)), 'ppRetVal' )),
]
################################################################
## code template for IAgConversionUtility implementation
##class IAgConversionUtility_Impl(object):
##    def ConvertQuantity(self, DimensionName, FromUnit, ToUnit, FromValue):
##        'Converts the specified quantity value from a given unit to another unit.'
##        #return pToValue
##
##    def ConvertDate(self, FromUnit, ToUnit, FromValue):
##        'Converts the specified date from a given unit to another unit.'
##        #return pToValue
##
##    def ConvertQuantityArray(self, DimensionName, FromUnit, ToUnit, QuantityValues):
##        'Converts the specified quantity values from a given unit to another unit.'
##        #return ppConvertedQuantityValues
##
##    def ConvertDateArray(self, FromUnit, ToUnit, FromValues):
##        'Converts the specified dates from a given unit to another unit.'
##        #return ppConvertedDateValues
##
##    def NewQuantity(self, Dimension, UnitAbbrv, Value):
##        'Creates an IAgQuantity interface with the given dimension, unit and value'
##        #return ppQuantity
##
##    def NewDate(self, UnitAbbrv, Value):
##        'Creates an IAgDate interface with the given unit and value'
##        #return ppDate
##
##    def NewPositionOnEarth(self):
##        "Creates an IAgPosition interface with earth as it's central body."
##        #return ppRetVal
##
##    def ConvertPositionArray(self, PositionType, PositionArray, ConvertTo):
##        'Converts the specified position values from a given position type to another position type.'
##        #return ppOutVal
##
##    def NewDirection(self):
##        'Creates an IAgDirection interface.'
##        #return ppRetVal
##
##    def NewOrientation(self):
##        'Creates an IAgOrientation interface.'
##        #return ppRetVal
##
##    def NewOrbitStateOnEarth(self):
##        "Creates an IAgOrbitState interface with earth as it's central body."
##        #return ppRetVal
##
##    def NewPositionOnCB(self, CentralBodyName):
##        'Creates an IAgPosition interface using the supplied central body.'
##        #return ppRetVal
##
##    def NewOrbitStateOnCB(self, CentralBodyName):
##        'Creates an IAgOrbitState interface using the supplied central body.'
##        #return ppRetVal
##
##    def QueryDirectionCosineMatrix(self, InputOrientation):
##        'Returns a Direction Cosine Matrix (DCM).'
##        #return pX, pY, pZ
##
##    def QueryDirectionCosineMatrixArray(self, InputOrientation):
##        'Returns a Direction Cosine Matrix (DCM) as an array.'
##        #return ppRetVal
##
##    def NewCartesian3Vector(self):
##        'Creates a cartesian vector.'
##        #return ppRetVal
##
##    def NewCartesian3VectorFromDirection(self, InputDirection):
##        'Converts the direction to cartesian vector.'
##        #return ppRetVal
##
##    def NewCartesian3VectorFromPosition(self, InputPosition):
##        'Converts the position to cartesian vector.'
##        #return ppRetVal
##

class IAgCartesian(IAgPosition):
    _case_insensitive_ = True
    'IAgCartesian Interface used to access a position using Cartesian Coordinates'
    _iid_ = GUID('{77B570BB-BBB5-4A5A-BF67-880AE0C55C0D}')
    _idlflags_ = ['oleautomation']
IAgCartesian._methods_ = [
    COMMETHOD(['propget', helpstring('Dimension depends on context.')], HRESULT, 'X',
              ( ['out', 'retval'], POINTER(c_double), 'pVal' )),
    COMMETHOD(['propput', helpstring('Dimension depends on context.')], HRESULT, 'X',
              ( ['in'], c_double, 'pVal' )),
    COMMETHOD(['propget', helpstring('Dimension depends on context.')], HRESULT, 'Y',
              ( ['out', 'retval'], POINTER(c_double), 'pVal' )),
    COMMETHOD(['propput', helpstring('Dimension depends on context.')], HRESULT, 'Y',
              ( ['in'], c_double, 'pVal' )),
    COMMETHOD(['propget', helpstring('Dimension depends on context.')], HRESULT, 'Z',
              ( ['out', 'retval'], POINTER(c_double), 'pVal' )),
    COMMETHOD(['propput', helpstring('Dimension depends on context.')], HRESULT, 'Z',
              ( ['in'], c_double, 'pVal' )),
    COMMETHOD([helpstring('This property is deprecated. Use AssignCartesian instead.')], HRESULT, 'SetValues',
              ( ['in'], c_double, 'X' ),
              ( ['in'], c_double, 'Y' ),
              ( ['in'], c_double, 'Z' )),
]
################################################################
## code template for IAgCartesian implementation
##class IAgCartesian_Impl(object):
##    def _get(self):
##        'Dimension depends on context.'
##        #return pVal
##    def _set(self, pVal):
##        'Dimension depends on context.'
##    X = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Dimension depends on context.'
##        #return pVal
##    def _set(self, pVal):
##        'Dimension depends on context.'
##    Y = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Dimension depends on context.'
##        #return pVal
##    def _set(self, pVal):
##        'Dimension depends on context.'
##    Z = property(_get, _set, doc = _set.__doc__)
##
##    def SetValues(self, X, Y, Z):
##        'This property is deprecated. Use AssignCartesian instead.'
##        #return 
##


# values for enumeration 'AgELineStyle'
eSolid = 0
eDashed = 1
eDotted = 2
eDotDashed = 3
eLongDashed = 4
eDashDotDotted = 5
eMDash = 6
eLDash = 7
eSDashDot = 8
eMDashDot = 9
eLDashDot = 10
eMSDash = 11
eLSDash = 12
eLMDash = 13
eLMSDash = 14
eDot = 15
eLongDash = 16
eSDash = 17
AgELineStyle = c_int # enum
IAgUnitPrefsDim._methods_ = [
    COMMETHOD(['propget', helpstring('Returns the ID of the dimension.')], HRESULT, 'Id',
              ( ['out', 'retval'], POINTER(c_int), 'pId' )),
    COMMETHOD(['propget', helpstring("Returns the current Dimension's full name.")], HRESULT, 'Name',
              ( ['out', 'retval'], POINTER(BSTR), 'pName' )),
    COMMETHOD(['propget', helpstring('Returns collection of Units.')], HRESULT, 'AvailableUnits',
              ( ['out', 'retval'], POINTER(POINTER(IAgUnitPrefsUnitCollection)), 'ppUnitPrefsUnitCollection' )),
    COMMETHOD(['propget', helpstring('Returns the current unit for this dimension.')], HRESULT, 'CurrentUnit',
              ( ['out', 'retval'], POINTER(POINTER(IAgUnitPrefsUnit)), 'ppUnitPrefsUnit' )),
    COMMETHOD([helpstring('Sets the Unit for this simple dimension.')], HRESULT, 'SetCurrentUnit',
              ( ['in'], BSTR, 'UnitAbbrv' )),
]
################################################################
## code template for IAgUnitPrefsDim implementation
##class IAgUnitPrefsDim_Impl(object):
##    @property
##    def Id(self):
##        'Returns the ID of the dimension.'
##        #return pId
##
##    @property
##    def Name(self):
##        "Returns the current Dimension's full name."
##        #return pName
##
##    @property
##    def AvailableUnits(self):
##        'Returns collection of Units.'
##        #return ppUnitPrefsUnitCollection
##
##    @property
##    def CurrentUnit(self):
##        'Returns the current unit for this dimension.'
##        #return ppUnitPrefsUnit
##
##    def SetCurrentUnit(self, UnitAbbrv):
##        'Sets the Unit for this simple dimension.'
##        #return 
##

class AgCartesian(CoClass):
    'Class used to access a position using Cartesian Coordinates.'
    _reg_clsid_ = GUID('{3C8F27C7-0D02-41DB-A9E6-A2BFE15B8B12}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{00DD7BD4-53D5-4870-996B-8ADB8AF904FA}', 1, 0)
class _IAgCartesian(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'IAgCartesian Interface used to access a position using Cartesian Coordinates'
    _iid_ = GUID('{E84D397A-F19D-4FEE-8781-84A617129932}')
    _idlflags_ = ['hidden', 'dual', 'nonextensible', 'oleautomation']
AgCartesian._com_interfaces_ = [_IAgCartesian, IAgCartesian, IAgPosition]

class Library(object):
    'AGI STK Util 11'
    name = 'STKUtil'
    _reg_typelib_ = ('{00DD7BD4-53D5-4870-996B-8ADB8AF904FA}', 1, 0)

class _IAgOrbitState(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'The hidden interface for IAgOrbitState'
    _iid_ = GUID('{11337044-5471-43AF-B254-A56E6187C4A3}')
    _idlflags_ = ['hidden', 'dual', 'nonextensible', 'oleautomation']
_IAgOrbitState._methods_ = [
    COMMETHOD([dispid(201), helpstring('Method to changes the coordinate type to the type specified.')], HRESULT, 'ConvertTo',
              ( ['in'], AgEOrbitStateType, 'Type' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgOrbitState)), 'ppRetVal' )),
    COMMETHOD([dispid(202), helpstring('Returns the coordinate type currently being used.'), 'propget'], HRESULT, 'OrbitStateType',
              ( ['out', 'retval'], POINTER(AgEOrbitStateType), 'pType' )),
    COMMETHOD([dispid(203), helpstring('Assign a new new coordinate type.')], HRESULT, 'Assign',
              ( ['in'], POINTER(IAgOrbitState), 'pOrbitState' )),
    COMMETHOD([dispid(204), helpstring('Helper method to assign a new orbit state using Classical representation')], HRESULT, 'AssignClassical',
              ( ['in'], AgECoordinateSystem, 'ECoordinateSystem' ),
              ( ['in'], c_double, 'SemiMajorAxis' ),
              ( ['in'], c_double, 'Eccentricity' ),
              ( ['in'], c_double, 'Inclination' ),
              ( ['in'], c_double, 'ArgOfPerigee' ),
              ( ['in'], c_double, 'RAAN' ),
              ( ['in'], c_double, 'MeanAnomaly' )),
    COMMETHOD([dispid(205), helpstring('Helper method to assign a new orbit state using Cartesian representation')], HRESULT, 'AssignCartesian',
              ( ['in'], AgECoordinateSystem, 'ECoordinateSystem' ),
              ( ['in'], c_double, 'XPosition' ),
              ( ['in'], c_double, 'YPosition' ),
              ( ['in'], c_double, 'ZPosition' ),
              ( ['in'], c_double, 'XVelocity' ),
              ( ['in'], c_double, 'YVelocity' ),
              ( ['in'], c_double, 'ZVelocity' )),
    COMMETHOD([dispid(206), helpstring('Helper method to assign a new orbit state using Geodetic representation')], HRESULT, 'AssignGeodetic',
              ( ['in'], AgECoordinateSystem, 'ECoordinateSystem' ),
              ( ['in'], c_double, 'Latitude' ),
              ( ['in'], c_double, 'Longitude' ),
              ( ['in'], c_double, 'Altitude' ),
              ( ['in'], c_double, 'LatitudeRate' ),
              ( ['in'], c_double, 'LongitudeRate' ),
              ( ['in'], c_double, 'AltitudeRate' )),
    COMMETHOD([dispid(207), helpstring('Helper method to assign a new orbit state using Equinoctial representation')], HRESULT, 'AssignEquinoctialPosigrade',
              ( ['in'], AgECoordinateSystem, 'ECoordinateSystem' ),
              ( ['in'], c_double, 'SemiMajorAxis' ),
              ( ['in'], c_double, 'H' ),
              ( ['in'], c_double, 'K' ),
              ( ['in'], c_double, 'P' ),
              ( ['in'], c_double, 'Q' ),
              ( ['in'], c_double, 'MeanLon' )),
    COMMETHOD([dispid(208), helpstring('Helper method to assign a new orbit state using Equinoctial representation')], HRESULT, 'AssignEquinoctialRetrograde',
              ( ['in'], AgECoordinateSystem, 'ECoordinateSystem' ),
              ( ['in'], c_double, 'SemiMajorAxis' ),
              ( ['in'], c_double, 'H' ),
              ( ['in'], c_double, 'K' ),
              ( ['in'], c_double, 'P' ),
              ( ['in'], c_double, 'Q' ),
              ( ['in'], c_double, 'MeanLon' )),
    COMMETHOD([dispid(209), helpstring('Helper method to assign a new orbit state using Mixed Spherical representation')], HRESULT, 'AssignMixedSpherical',
              ( ['in'], AgECoordinateSystem, 'ECoordinateSystem' ),
              ( ['in'], c_double, 'Latitude' ),
              ( ['in'], c_double, 'Longitude' ),
              ( ['in'], c_double, 'Altitude' ),
              ( ['in'], c_double, 'HorFlightPathAngle' ),
              ( ['in'], c_double, 'FlightPathAzimuth' ),
              ( ['in'], c_double, 'Velocity' )),
    COMMETHOD([dispid(210), helpstring('Helper method to assign a new orbit state using Spherical representation')], HRESULT, 'AssignSpherical',
              ( ['in'], AgECoordinateSystem, 'ECoordinateSystem' ),
              ( ['in'], c_double, 'RightAscension' ),
              ( ['in'], c_double, 'Declination' ),
              ( ['in'], c_double, 'Radius' ),
              ( ['in'], c_double, 'HorFlightPathAngle' ),
              ( ['in'], c_double, 'FlightPathAzimuth' ),
              ( ['in'], c_double, 'Velocity' )),
    COMMETHOD([dispid(211), helpstring('Gets the central body.'), 'propget'], HRESULT, 'CentralBodyName',
              ( ['out', 'retval'], POINTER(BSTR), 'pCBName' )),
    COMMETHOD([dispid(212), helpstring('The state epoch. Uses DateFormat Dimension.'), 'propget'], HRESULT, 'Epoch',
              ( ['out', 'retval'], POINTER(VARIANT), 'pRetVal' )),
    COMMETHOD([dispid(212), helpstring('The state epoch. Uses DateFormat Dimension.'), 'propput'], HRESULT, 'Epoch',
              ( ['in'], VARIANT, 'pRetVal' )),
]
################################################################
## code template for _IAgOrbitState implementation
##class _IAgOrbitState_Impl(object):
##    def ConvertTo(self, Type):
##        'Method to changes the coordinate type to the type specified.'
##        #return ppRetVal
##
##    @property
##    def OrbitStateType(self):
##        'Returns the coordinate type currently being used.'
##        #return pType
##
##    def Assign(self, pOrbitState):
##        'Assign a new new coordinate type.'
##        #return 
##
##    def AssignClassical(self, ECoordinateSystem, SemiMajorAxis, Eccentricity, Inclination, ArgOfPerigee, RAAN, MeanAnomaly):
##        'Helper method to assign a new orbit state using Classical representation'
##        #return 
##
##    def AssignCartesian(self, ECoordinateSystem, XPosition, YPosition, ZPosition, XVelocity, YVelocity, ZVelocity):
##        'Helper method to assign a new orbit state using Cartesian representation'
##        #return 
##
##    def AssignGeodetic(self, ECoordinateSystem, Latitude, Longitude, Altitude, LatitudeRate, LongitudeRate, AltitudeRate):
##        'Helper method to assign a new orbit state using Geodetic representation'
##        #return 
##
##    def AssignEquinoctialPosigrade(self, ECoordinateSystem, SemiMajorAxis, H, K, P, Q, MeanLon):
##        'Helper method to assign a new orbit state using Equinoctial representation'
##        #return 
##
##    def AssignEquinoctialRetrograde(self, ECoordinateSystem, SemiMajorAxis, H, K, P, Q, MeanLon):
##        'Helper method to assign a new orbit state using Equinoctial representation'
##        #return 
##
##    def AssignMixedSpherical(self, ECoordinateSystem, Latitude, Longitude, Altitude, HorFlightPathAngle, FlightPathAzimuth, Velocity):
##        'Helper method to assign a new orbit state using Mixed Spherical representation'
##        #return 
##
##    def AssignSpherical(self, ECoordinateSystem, RightAscension, Declination, Radius, HorFlightPathAngle, FlightPathAzimuth, Velocity):
##        'Helper method to assign a new orbit state using Spherical representation'
##        #return 
##
##    @property
##    def CentralBodyName(self):
##        'Gets the central body.'
##        #return pCBName
##
##    def _get(self):
##        'The state epoch. Uses DateFormat Dimension.'
##        #return pRetVal
##    def _set(self, pRetVal):
##        'The state epoch. Uses DateFormat Dimension.'
##    Epoch = property(_get, _set, doc = _set.__doc__)
##

class AgGeodetic(CoClass):
    'Class defining Geodetic position.'
    _reg_clsid_ = GUID('{4A6D507B-D6F0-4FCF-B973-3FAC07863335}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{00DD7BD4-53D5-4870-996B-8ADB8AF904FA}', 1, 0)
class _IAgGeodetic(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Sets the position using Geodetic properties.'
    _iid_ = GUID('{FE437A8A-ADA7-494C-8AB9-3127026E0654}')
    _idlflags_ = ['hidden', 'dual', 'nonextensible', 'oleautomation']
class IAgGeodetic(IAgPosition):
    _case_insensitive_ = True
    'IAgGeodetic sets the position using Geodetic properties.'
    _iid_ = GUID('{4EF60500-8A60-4E8D-AFF5-9AB9431F90E4}')
    _idlflags_ = ['oleautomation']
AgGeodetic._com_interfaces_ = [_IAgGeodetic, IAgGeodetic, IAgPosition]


# values for enumeration 'AgELogMsgDispID'
eLogMsgDispAll = -1
eLogMsgDispDefault = 0
eLogMsgDispMsgWin = 1
eLogMsgDispStatusBar = 2
AgELogMsgDispID = c_int # enum

# values for enumeration 'AgELogMsgType'
eLogMsgDebug = 0
eLogMsgInfo = 1
eLogMsgForceInfo = 2
eLogMsgWarning = 3
eLogMsgAlarm = 4
AgELogMsgType = c_int # enum
IAgLocationData._methods_ = [
]
################################################################
## code template for IAgLocationData implementation
##class IAgLocationData_Impl(object):

IAgGeodetic._methods_ = [
    COMMETHOD(['propget', helpstring('Latitude. Uses Latitude Dimension.')], HRESULT, 'Lat',
              ( ['out', 'retval'], POINTER(VARIANT), 'pLat' )),
    COMMETHOD(['propput', helpstring('Latitude. Uses Latitude Dimension.')], HRESULT, 'Lat',
              ( ['in'], VARIANT, 'pLat' )),
    COMMETHOD(['propget', helpstring('Longitude. Uses Longitude Dimension.')], HRESULT, 'Lon',
              ( ['out', 'retval'], POINTER(VARIANT), 'pLon' )),
    COMMETHOD(['propput', helpstring('Longitude. Uses Longitude Dimension.')], HRESULT, 'Lon',
              ( ['in'], VARIANT, 'pLon' )),
    COMMETHOD(['propget', helpstring('Altitude. Dimension depends on context.')], HRESULT, 'Alt',
              ( ['out', 'retval'], POINTER(c_double), 'pAlt' )),
    COMMETHOD(['propput', helpstring('Altitude. Dimension depends on context.')], HRESULT, 'Alt',
              ( ['in'], c_double, 'pAlt' )),
    COMMETHOD([helpstring('This property is deprecated. Use AssignGeodetic instead.')], HRESULT, 'SetValues',
              ( ['in'], VARIANT, 'Lat' ),
              ( ['in'], VARIANT, 'Lon' ),
              ( ['in'], c_double, 'Alt' )),
]
################################################################
## code template for IAgGeodetic implementation
##class IAgGeodetic_Impl(object):
##    def _get(self):
##        'Latitude. Uses Latitude Dimension.'
##        #return pLat
##    def _set(self, pLat):
##        'Latitude. Uses Latitude Dimension.'
##    Lat = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Longitude. Uses Longitude Dimension.'
##        #return pLon
##    def _set(self, pLon):
##        'Longitude. Uses Longitude Dimension.'
##    Lon = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Altitude. Dimension depends on context.'
##        #return pAlt
##    def _set(self, pAlt):
##        'Altitude. Dimension depends on context.'
##    Alt = property(_get, _set, doc = _set.__doc__)
##
##    def SetValues(self, Lat, Lon, Alt):
##        'This property is deprecated. Use AssignGeodetic instead.'
##        #return 
##

_IAgGeodetic._methods_ = [
    COMMETHOD([dispid(201), helpstring('Latitude. Uses Latitude Dimension.'), 'propget'], HRESULT, 'Lat',
              ( ['out', 'retval'], POINTER(VARIANT), 'pLat' )),
    COMMETHOD([dispid(201), helpstring('Latitude. Uses Latitude Dimension.'), 'propput'], HRESULT, 'Lat',
              ( ['in'], VARIANT, 'pLat' )),
    COMMETHOD([dispid(202), helpstring('Longitude. Uses Longitude Dimension.'), 'propget'], HRESULT, 'Lon',
              ( ['out', 'retval'], POINTER(VARIANT), 'pLon' )),
    COMMETHOD([dispid(202), helpstring('Longitude. Uses Longitude Dimension.'), 'propput'], HRESULT, 'Lon',
              ( ['in'], VARIANT, 'pLon' )),
    COMMETHOD([dispid(203), helpstring('Altitude. Dimension depends on context.'), 'propget'], HRESULT, 'Alt',
              ( ['out', 'retval'], POINTER(c_double), 'pAlt' )),
    COMMETHOD([dispid(203), helpstring('Altitude. Dimension depends on context.'), 'propput'], HRESULT, 'Alt',
              ( ['in'], c_double, 'pAlt' )),
    COMMETHOD([dispid(204), helpstring('This property is deprecated. Use AssignGeodetic instead.')], HRESULT, 'SetValues',
              ( ['in'], VARIANT, 'Lat' ),
              ( ['in'], VARIANT, 'Lon' ),
              ( ['in'], c_double, 'Alt' )),
    COMMETHOD([dispid(401), helpstring('Changes the position coordinates to type specified.')], HRESULT, 'ConvertTo',
              ( ['in'], AgEPositionType, 'Type' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgPosition)), 'ppIAgPosition' )),
    COMMETHOD([dispid(402), helpstring('Gets the type of position currently being used.'), 'propget'], HRESULT, 'PosType',
              ( ['out', 'retval'], POINTER(AgEPositionType), 'pType' )),
    COMMETHOD([dispid(403), helpstring('This assigns the coordinates into the system.')], HRESULT, 'Assign',
              ( ['in'], POINTER(IAgPosition), 'pPosition' )),
    COMMETHOD([dispid(404), helpstring('Helper method to assign the position using the Geocentric representation.')], HRESULT, 'AssignGeocentric',
              ( ['in'], VARIANT, 'Lat' ),
              ( ['in'], VARIANT, 'Lon' ),
              ( ['in'], c_double, 'Alt' )),
    COMMETHOD([dispid(405), helpstring('Helper method to assign the position using the Geodetic representation.')], HRESULT, 'AssignGeodetic',
              ( ['in'], VARIANT, 'Lat' ),
              ( ['in'], VARIANT, 'Lon' ),
              ( ['in'], c_double, 'Alt' )),
    COMMETHOD([dispid(406), helpstring('Helper method to assign the position using the Spherical representation')], HRESULT, 'AssignSpherical',
              ( ['in'], VARIANT, 'Lat' ),
              ( ['in'], VARIANT, 'Lon' ),
              ( ['in'], c_double, 'Radius' )),
    COMMETHOD([dispid(407), helpstring('Helper method to assign the position using the Cylindrical representation')], HRESULT, 'AssignCylindrical',
              ( ['in'], c_double, 'Radius' ),
              ( ['in'], c_double, 'Z' ),
              ( ['in'], VARIANT, 'Lon' )),
    COMMETHOD([dispid(408), helpstring('Helper method to assign the position using the Cartesian representation')], HRESULT, 'AssignCartesian',
              ( ['in'], c_double, 'X' ),
              ( ['in'], c_double, 'Y' ),
              ( ['in'], c_double, 'Z' )),
    COMMETHOD([dispid(409), helpstring('Helper method to assign the position using the Planetocentric representation')], HRESULT, 'AssignPlanetocentric',
              ( ['in'], VARIANT, 'Lat' ),
              ( ['in'], VARIANT, 'Lon' ),
              ( ['in'], c_double, 'Alt' )),
    COMMETHOD([dispid(410), helpstring('Helper method to assign the position using the Planetodetic representation')], HRESULT, 'AssignPlanetodetic',
              ( ['in'], VARIANT, 'Lat' ),
              ( ['in'], VARIANT, 'Lon' ),
              ( ['in'], c_double, 'Alt' )),
    COMMETHOD([dispid(411), helpstring('Helper method to get the position using the Planetocentric representation')], HRESULT, 'QueryPlanetocentric',
              ( ['out'], POINTER(VARIANT), 'Lat' ),
              ( ['out'], POINTER(VARIANT), 'Lon' ),
              ( ['out'], POINTER(c_double), 'Alt' )),
    COMMETHOD([dispid(412), helpstring('Helper method to get the position using the Planetodetic representation')], HRESULT, 'QueryPlanetodetic',
              ( ['out'], POINTER(VARIANT), 'Lat' ),
              ( ['out'], POINTER(VARIANT), 'Lon' ),
              ( ['out'], POINTER(c_double), 'Alt' )),
    COMMETHOD([dispid(413), helpstring('Helper method to get the position using the Spherical representation')], HRESULT, 'QuerySpherical',
              ( ['out'], POINTER(VARIANT), 'Lat' ),
              ( ['out'], POINTER(VARIANT), 'Lon' ),
              ( ['out'], POINTER(c_double), 'Radius' )),
    COMMETHOD([dispid(414), helpstring('Helper method to get the position using the Cylindrical representation')], HRESULT, 'QueryCylindrical',
              ( ['out'], POINTER(c_double), 'Radius' ),
              ( ['out'], POINTER(VARIANT), 'Lon' ),
              ( ['out'], POINTER(c_double), 'Z' )),
    COMMETHOD([dispid(415), helpstring('Helper method to get the position using the Cartesian representation')], HRESULT, 'QueryCartesian',
              ( ['out'], POINTER(c_double), 'X' ),
              ( ['out'], POINTER(c_double), 'Y' ),
              ( ['out'], POINTER(c_double), 'Z' )),
    COMMETHOD([dispid(416), helpstring('Gets the central body.'), 'propget'], HRESULT, 'CentralBodyName',
              ( ['out', 'retval'], POINTER(BSTR), 'pCBName' )),
    COMMETHOD([dispid(417), helpstring('Returns the Planetocentric elements as an array.')], HRESULT, 'QueryPlanetocentricArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(418), helpstring('Returns the Planetodetic elements as an array.')], HRESULT, 'QueryPlanetodeticArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(419), helpstring('Returns the Spherical elements as an array.')], HRESULT, 'QuerySphericalArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(420), helpstring('Returns the Cylindrical elements as an array.')], HRESULT, 'QueryCylindricalArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(421), helpstring('Returns the Cartesian elements as an array.')], HRESULT, 'QueryCartesianArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
]
################################################################
## code template for _IAgGeodetic implementation
##class _IAgGeodetic_Impl(object):
##    def _get(self):
##        'Latitude. Uses Latitude Dimension.'
##        #return pLat
##    def _set(self, pLat):
##        'Latitude. Uses Latitude Dimension.'
##    Lat = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Longitude. Uses Longitude Dimension.'
##        #return pLon
##    def _set(self, pLon):
##        'Longitude. Uses Longitude Dimension.'
##    Lon = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Altitude. Dimension depends on context.'
##        #return pAlt
##    def _set(self, pAlt):
##        'Altitude. Dimension depends on context.'
##    Alt = property(_get, _set, doc = _set.__doc__)
##
##    def SetValues(self, Lat, Lon, Alt):
##        'This property is deprecated. Use AssignGeodetic instead.'
##        #return 
##
##    def ConvertTo(self, Type):
##        'Changes the position coordinates to type specified.'
##        #return ppIAgPosition
##
##    @property
##    def PosType(self):
##        'Gets the type of position currently being used.'
##        #return pType
##
##    def Assign(self, pPosition):
##        'This assigns the coordinates into the system.'
##        #return 
##
##    def AssignGeocentric(self, Lat, Lon, Alt):
##        'Helper method to assign the position using the Geocentric representation.'
##        #return 
##
##    def AssignGeodetic(self, Lat, Lon, Alt):
##        'Helper method to assign the position using the Geodetic representation.'
##        #return 
##
##    def AssignSpherical(self, Lat, Lon, Radius):
##        'Helper method to assign the position using the Spherical representation'
##        #return 
##
##    def AssignCylindrical(self, Radius, Z, Lon):
##        'Helper method to assign the position using the Cylindrical representation'
##        #return 
##
##    def AssignCartesian(self, X, Y, Z):
##        'Helper method to assign the position using the Cartesian representation'
##        #return 
##
##    def AssignPlanetocentric(self, Lat, Lon, Alt):
##        'Helper method to assign the position using the Planetocentric representation'
##        #return 
##
##    def AssignPlanetodetic(self, Lat, Lon, Alt):
##        'Helper method to assign the position using the Planetodetic representation'
##        #return 
##
##    def QueryPlanetocentric(self):
##        'Helper method to get the position using the Planetocentric representation'
##        #return Lat, Lon, Alt
##
##    def QueryPlanetodetic(self):
##        'Helper method to get the position using the Planetodetic representation'
##        #return Lat, Lon, Alt
##
##    def QuerySpherical(self):
##        'Helper method to get the position using the Spherical representation'
##        #return Lat, Lon, Radius
##
##    def QueryCylindrical(self):
##        'Helper method to get the position using the Cylindrical representation'
##        #return Radius, Lon, Z
##
##    def QueryCartesian(self):
##        'Helper method to get the position using the Cartesian representation'
##        #return X, Y, Z
##
##    @property
##    def CentralBodyName(self):
##        'Gets the central body.'
##        #return pCBName
##
##    def QueryPlanetocentricArray(self):
##        'Returns the Planetocentric elements as an array.'
##        #return ppRetVal
##
##    def QueryPlanetodeticArray(self):
##        'Returns the Planetodetic elements as an array.'
##        #return ppRetVal
##
##    def QuerySphericalArray(self):
##        'Returns the Spherical elements as an array.'
##        #return ppRetVal
##
##    def QueryCylindricalArray(self):
##        'Returns the Cylindrical elements as an array.'
##        #return ppRetVal
##
##    def QueryCartesianArray(self):
##        'Returns the Cartesian elements as an array.'
##        #return ppRetVal
##


# values for enumeration 'AgEFillStyle'
eFillStyleSolid = 0
eFillStyleHorizontalStripe = 1
eFillStyleDiagonalStripe1 = 2
eFillStyleDiagonalStripe2 = 3
eFillStyleHatch = 4
eFillStyleDiagonalHatch = 5
eFillStyleScreen = 6
eFillStyleVerticalStripe = 7
AgEFillStyle = c_int # enum
IAgUnitPrefsUnit._methods_ = [
    COMMETHOD(['propget', helpstring('Returns the fullname of the unit.')], HRESULT, 'FullName',
              ( ['out', 'retval'], POINTER(BSTR), 'pName' )),
    COMMETHOD(['propget', helpstring('Returns the abbreviation of the unit.')], HRESULT, 'Abbrv',
              ( ['out', 'retval'], POINTER(BSTR), 'pAbbrv' )),
    COMMETHOD(['propget', helpstring('Returns the ID of the unit.')], HRESULT, 'Id',
              ( ['out', 'retval'], POINTER(c_int), 'pId' )),
    COMMETHOD(['propget', helpstring('Returns the Dimension for this unit.')], HRESULT, 'Dimension',
              ( ['out', 'retval'], POINTER(POINTER(IAgUnitPrefsDim)), 'ppUnitPrefsDim' )),
]
################################################################
## code template for IAgUnitPrefsUnit implementation
##class IAgUnitPrefsUnit_Impl(object):
##    @property
##    def FullName(self):
##        'Returns the fullname of the unit.'
##        #return pName
##
##    @property
##    def Abbrv(self):
##        'Returns the abbreviation of the unit.'
##        #return pAbbrv
##
##    @property
##    def Id(self):
##        'Returns the ID of the unit.'
##        #return pId
##
##    @property
##    def Dimension(self):
##        'Returns the Dimension for this unit.'
##        #return ppUnitPrefsDim
##

IAgUnitPrefsUnitCollection._methods_ = [
    COMMETHOD([dispid(0), helpstring('Returns the specific item in the collection given a unit identifier or an index.'), 'propget'], HRESULT, 'Item',
              ( ['in'], VARIANT, 'IndexOrName' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgUnitPrefsUnit)), 'ppUnitPrefsUnit' )),
    COMMETHOD([dispid(1), helpstring('Returns the number of items in the collection.'), 'propget'], HRESULT, 'Count',
              ( ['out', 'retval'], POINTER(c_int), 'pVal' )),
    COMMETHOD([dispid(-4), helpstring('Returns an enumeration of AgUnitPrefsUnit.'), 'propget'], HRESULT, '_NewEnum',
              ( ['out', 'retval'], POINTER(POINTER(IUnknown)), 'ppRetVal' )),
]
################################################################
## code template for IAgUnitPrefsUnitCollection implementation
##class IAgUnitPrefsUnitCollection_Impl(object):
##    @property
##    def Item(self, IndexOrName):
##        'Returns the specific item in the collection given a unit identifier or an index.'
##        #return ppUnitPrefsUnit
##
##    @property
##    def Count(self):
##        'Returns the number of items in the collection.'
##        #return pVal
##
##    @property
##    def _NewEnum(self):
##        'Returns an enumeration of AgUnitPrefsUnit.'
##        #return ppRetVal
##

class _IAgCartesian2Vector(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'A hidden interface for IAgCartesian2Vector.'
    _iid_ = GUID('{DCB88D22-81DB-4CD5-B343-3996EFD0821E}')
    _idlflags_ = ['hidden', 'dual', 'nonextensible', 'oleautomation']
_IAgCartesian2Vector._methods_ = [
    COMMETHOD([dispid(200), helpstring('X coordinate'), 'propget'], HRESULT, 'X',
              ( ['out', 'retval'], POINTER(c_double), 'pRetVal' )),
    COMMETHOD([dispid(200), helpstring('X coordinate'), 'propput'], HRESULT, 'X',
              ( ['in'], c_double, 'pRetVal' )),
    COMMETHOD([dispid(201), helpstring('Y coordinate'), 'propget'], HRESULT, 'Y',
              ( ['out', 'retval'], POINTER(c_double), 'pRetVal' )),
    COMMETHOD([dispid(201), helpstring('Y coordinate'), 'propput'], HRESULT, 'Y',
              ( ['in'], c_double, 'pRetVal' )),
    COMMETHOD([dispid(202), helpstring('Returns cartesian vector')], HRESULT, 'Get',
              ( ['out'], POINTER(c_double), 'X' ),
              ( ['out'], POINTER(c_double), 'Y' )),
    COMMETHOD([dispid(203), helpstring('Sets cartesian vector')], HRESULT, 'Set',
              ( ['in'], c_double, 'X' ),
              ( ['in'], c_double, 'Y' )),
    COMMETHOD([dispid(204), helpstring('Returns coordinates as an array.')], HRESULT, 'ToArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
]
################################################################
## code template for _IAgCartesian2Vector implementation
##class _IAgCartesian2Vector_Impl(object):
##    def _get(self):
##        'X coordinate'
##        #return pRetVal
##    def _set(self, pRetVal):
##        'X coordinate'
##    X = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Y coordinate'
##        #return pRetVal
##    def _set(self, pRetVal):
##        'Y coordinate'
##    Y = property(_get, _set, doc = _set.__doc__)
##
##    def Get(self):
##        'Returns cartesian vector'
##        #return X, Y
##
##    def Set(self, X, Y):
##        'Sets cartesian vector'
##        #return 
##
##    def ToArray(self):
##        'Returns coordinates as an array.'
##        #return ppRetVal
##

class AgCartesian2Vector(CoClass):
    'A 2-D cartesian vector.'
    _reg_clsid_ = GUID('{B17BA593-690C-4881-BC65-58F6E842F358}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{00DD7BD4-53D5-4870-996B-8ADB8AF904FA}', 1, 0)
AgCartesian2Vector._com_interfaces_ = [_IAgCartesian2Vector, IAgCartesian2Vector]

class IAgGeocentric(IAgPosition):
    _case_insensitive_ = True
    'Geocentric Position Type.'
    _iid_ = GUID('{3DB243A3-534F-4223-8C13-E53EB75CD4CE}')
    _idlflags_ = ['oleautomation']
IAgGeocentric._methods_ = [
    COMMETHOD(['propget', helpstring('Uses Latitude Dimension.')], HRESULT, 'Lat',
              ( ['out', 'retval'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD(['propput', helpstring('Uses Latitude Dimension.')], HRESULT, 'Lat',
              ( ['in'], VARIANT, 'pVal' )),
    COMMETHOD(['propget', helpstring('Uses Longitude Dimension.')], HRESULT, 'Lon',
              ( ['out', 'retval'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD(['propput', helpstring('Uses Longitude Dimension.')], HRESULT, 'Lon',
              ( ['in'], VARIANT, 'pVal' )),
    COMMETHOD(['propget', helpstring('Dimension depends on context.')], HRESULT, 'Alt',
              ( ['out', 'retval'], POINTER(c_double), 'pVal' )),
    COMMETHOD(['propput', helpstring('Dimension depends on context.')], HRESULT, 'Alt',
              ( ['in'], c_double, 'pVal' )),
    COMMETHOD([helpstring('This property is deprecated. Use AssignGeocentric instead.')], HRESULT, 'SetValues',
              ( ['in'], VARIANT, 'Lat' ),
              ( ['in'], VARIANT, 'Lon' ),
              ( ['in'], c_double, 'Alt' )),
]
################################################################
## code template for IAgGeocentric implementation
##class IAgGeocentric_Impl(object):
##    def _get(self):
##        'Uses Latitude Dimension.'
##        #return pVal
##    def _set(self, pVal):
##        'Uses Latitude Dimension.'
##    Lat = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Uses Longitude Dimension.'
##        #return pVal
##    def _set(self, pVal):
##        'Uses Longitude Dimension.'
##    Lon = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Dimension depends on context.'
##        #return pVal
##    def _set(self, pVal):
##        'Dimension depends on context.'
##    Alt = property(_get, _set, doc = _set.__doc__)
##
##    def SetValues(self, Lat, Lon, Alt):
##        'This property is deprecated. Use AssignGeocentric instead.'
##        #return 
##

class AgGeocentric(CoClass):
    'Class defining Geocentric position.'
    _reg_clsid_ = GUID('{2B723CBD-2A9A-4E33-A9B8-1C3468852F1B}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{00DD7BD4-53D5-4870-996B-8ADB8AF904FA}', 1, 0)
class _IAgGeocentric(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Geocentric Position Type.'
    _iid_ = GUID('{9A4C0236-81FC-442E-9FCD-8D957C4FA281}')
    _idlflags_ = ['hidden', 'dual', 'nonextensible', 'oleautomation']
AgGeocentric._com_interfaces_ = [_IAgGeocentric, IAgGeocentric, IAgPosition]

_IAgGeocentric._methods_ = [
    COMMETHOD([dispid(201), helpstring('Uses Latitude Dimension.'), 'propget'], HRESULT, 'Lat',
              ( ['out', 'retval'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD([dispid(201), helpstring('Uses Latitude Dimension.'), 'propput'], HRESULT, 'Lat',
              ( ['in'], VARIANT, 'pVal' )),
    COMMETHOD([dispid(202), helpstring('Uses Longitude Dimension.'), 'propget'], HRESULT, 'Lon',
              ( ['out', 'retval'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD([dispid(202), helpstring('Uses Longitude Dimension.'), 'propput'], HRESULT, 'Lon',
              ( ['in'], VARIANT, 'pVal' )),
    COMMETHOD([dispid(203), helpstring('Dimension depends on context.'), 'propget'], HRESULT, 'Alt',
              ( ['out', 'retval'], POINTER(c_double), 'pVal' )),
    COMMETHOD([dispid(203), helpstring('Dimension depends on context.'), 'propput'], HRESULT, 'Alt',
              ( ['in'], c_double, 'pVal' )),
    COMMETHOD([dispid(204), helpstring('This property is deprecated. Use AssignGeocentric instead.')], HRESULT, 'SetValues',
              ( ['in'], VARIANT, 'Lat' ),
              ( ['in'], VARIANT, 'Lon' ),
              ( ['in'], c_double, 'Alt' )),
    COMMETHOD([dispid(401), helpstring('Changes the position coordinates to type specified.')], HRESULT, 'ConvertTo',
              ( ['in'], AgEPositionType, 'Type' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgPosition)), 'ppIAgPosition' )),
    COMMETHOD([dispid(402), helpstring('Gets the type of position currently being used.'), 'propget'], HRESULT, 'PosType',
              ( ['out', 'retval'], POINTER(AgEPositionType), 'pType' )),
    COMMETHOD([dispid(403), helpstring('This assigns the coordinates into the system.')], HRESULT, 'Assign',
              ( ['in'], POINTER(IAgPosition), 'pPosition' )),
    COMMETHOD([dispid(404), helpstring('Helper method to assign the position using the Geocentric representation.')], HRESULT, 'AssignGeocentric',
              ( ['in'], VARIANT, 'Lat' ),
              ( ['in'], VARIANT, 'Lon' ),
              ( ['in'], c_double, 'Alt' )),
    COMMETHOD([dispid(405), helpstring('Helper method to assign the position using the Geodetic representation')], HRESULT, 'AssignGeodetic',
              ( ['in'], VARIANT, 'Lat' ),
              ( ['in'], VARIANT, 'Lon' ),
              ( ['in'], c_double, 'Alt' )),
    COMMETHOD([dispid(406), helpstring('Helper method to assign the position using the Spherical representation')], HRESULT, 'AssignSpherical',
              ( ['in'], VARIANT, 'Lat' ),
              ( ['in'], VARIANT, 'Lon' ),
              ( ['in'], c_double, 'Radius' )),
    COMMETHOD([dispid(407), helpstring('Helper method to assign the position using the Cylindrical representation')], HRESULT, 'AssignCylindrical',
              ( ['in'], c_double, 'Radius' ),
              ( ['in'], c_double, 'Z' ),
              ( ['in'], VARIANT, 'Lon' )),
    COMMETHOD([dispid(408), helpstring('Helper method to assign the position using the Cartesian representation')], HRESULT, 'AssignCartesian',
              ( ['in'], c_double, 'X' ),
              ( ['in'], c_double, 'Y' ),
              ( ['in'], c_double, 'Z' )),
    COMMETHOD([dispid(409), helpstring('Helper method to assign the position using the Planetocentric representation')], HRESULT, 'AssignPlanetocentric',
              ( ['in'], VARIANT, 'Lat' ),
              ( ['in'], VARIANT, 'Lon' ),
              ( ['in'], c_double, 'Alt' )),
    COMMETHOD([dispid(410), helpstring('Helper method to assign the position using the Planetodetic representation')], HRESULT, 'AssignPlanetodetic',
              ( ['in'], VARIANT, 'Lat' ),
              ( ['in'], VARIANT, 'Lon' ),
              ( ['in'], c_double, 'Alt' )),
    COMMETHOD([dispid(411), helpstring('Helper method to get the position using the Planetocentric representation')], HRESULT, 'QueryPlanetocentric',
              ( ['out'], POINTER(VARIANT), 'Lat' ),
              ( ['out'], POINTER(VARIANT), 'Lon' ),
              ( ['out'], POINTER(c_double), 'Alt' )),
    COMMETHOD([dispid(412), helpstring('Helper method to get the position using the Planetodetic representation')], HRESULT, 'QueryPlanetodetic',
              ( ['out'], POINTER(VARIANT), 'Lat' ),
              ( ['out'], POINTER(VARIANT), 'Lon' ),
              ( ['out'], POINTER(c_double), 'Alt' )),
    COMMETHOD([dispid(413), helpstring('Helper method to get the position using the Spherical representation')], HRESULT, 'QuerySpherical',
              ( ['out'], POINTER(VARIANT), 'Lat' ),
              ( ['out'], POINTER(VARIANT), 'Lon' ),
              ( ['out'], POINTER(c_double), 'Radius' )),
    COMMETHOD([dispid(414), helpstring('Helper method to get the position using the Cylindrical representation')], HRESULT, 'QueryCylindrical',
              ( ['out'], POINTER(c_double), 'Radius' ),
              ( ['out'], POINTER(VARIANT), 'Lon' ),
              ( ['out'], POINTER(c_double), 'Z' )),
    COMMETHOD([dispid(415), helpstring('Helper method to get the position using the Cartesian representation')], HRESULT, 'QueryCartesian',
              ( ['out'], POINTER(c_double), 'X' ),
              ( ['out'], POINTER(c_double), 'Y' ),
              ( ['out'], POINTER(c_double), 'Z' )),
    COMMETHOD([dispid(416), helpstring('Gets the central body.'), 'propget'], HRESULT, 'CentralBodyName',
              ( ['out', 'retval'], POINTER(BSTR), 'pCBName' )),
    COMMETHOD([dispid(417), helpstring('Returns the Planetocentric elements as an array.')], HRESULT, 'QueryPlanetocentricArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(418), helpstring('Returns the Planetodetic elements as an array.')], HRESULT, 'QueryPlanetodeticArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(419), helpstring('Returns the Spherical elements as an array.')], HRESULT, 'QuerySphericalArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(420), helpstring('Returns the Cylindrical elements as an array.')], HRESULT, 'QueryCylindricalArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(421), helpstring('Returns the Cartesian elements as an array.')], HRESULT, 'QueryCartesianArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
]
################################################################
## code template for _IAgGeocentric implementation
##class _IAgGeocentric_Impl(object):
##    def _get(self):
##        'Uses Latitude Dimension.'
##        #return pVal
##    def _set(self, pVal):
##        'Uses Latitude Dimension.'
##    Lat = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Uses Longitude Dimension.'
##        #return pVal
##    def _set(self, pVal):
##        'Uses Longitude Dimension.'
##    Lon = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Dimension depends on context.'
##        #return pVal
##    def _set(self, pVal):
##        'Dimension depends on context.'
##    Alt = property(_get, _set, doc = _set.__doc__)
##
##    def SetValues(self, Lat, Lon, Alt):
##        'This property is deprecated. Use AssignGeocentric instead.'
##        #return 
##
##    def ConvertTo(self, Type):
##        'Changes the position coordinates to type specified.'
##        #return ppIAgPosition
##
##    @property
##    def PosType(self):
##        'Gets the type of position currently being used.'
##        #return pType
##
##    def Assign(self, pPosition):
##        'This assigns the coordinates into the system.'
##        #return 
##
##    def AssignGeocentric(self, Lat, Lon, Alt):
##        'Helper method to assign the position using the Geocentric representation.'
##        #return 
##
##    def AssignGeodetic(self, Lat, Lon, Alt):
##        'Helper method to assign the position using the Geodetic representation'
##        #return 
##
##    def AssignSpherical(self, Lat, Lon, Radius):
##        'Helper method to assign the position using the Spherical representation'
##        #return 
##
##    def AssignCylindrical(self, Radius, Z, Lon):
##        'Helper method to assign the position using the Cylindrical representation'
##        #return 
##
##    def AssignCartesian(self, X, Y, Z):
##        'Helper method to assign the position using the Cartesian representation'
##        #return 
##
##    def AssignPlanetocentric(self, Lat, Lon, Alt):
##        'Helper method to assign the position using the Planetocentric representation'
##        #return 
##
##    def AssignPlanetodetic(self, Lat, Lon, Alt):
##        'Helper method to assign the position using the Planetodetic representation'
##        #return 
##
##    def QueryPlanetocentric(self):
##        'Helper method to get the position using the Planetocentric representation'
##        #return Lat, Lon, Alt
##
##    def QueryPlanetodetic(self):
##        'Helper method to get the position using the Planetodetic representation'
##        #return Lat, Lon, Alt
##
##    def QuerySpherical(self):
##        'Helper method to get the position using the Spherical representation'
##        #return Lat, Lon, Radius
##
##    def QueryCylindrical(self):
##        'Helper method to get the position using the Cylindrical representation'
##        #return Radius, Lon, Z
##
##    def QueryCartesian(self):
##        'Helper method to get the position using the Cartesian representation'
##        #return X, Y, Z
##
##    @property
##    def CentralBodyName(self):
##        'Gets the central body.'
##        #return pCBName
##
##    def QueryPlanetocentricArray(self):
##        'Returns the Planetocentric elements as an array.'
##        #return ppRetVal
##
##    def QueryPlanetodeticArray(self):
##        'Returns the Planetodetic elements as an array.'
##        #return ppRetVal
##
##    def QuerySphericalArray(self):
##        'Returns the Spherical elements as an array.'
##        #return ppRetVal
##
##    def QueryCylindricalArray(self):
##        'Returns the Cylindrical elements as an array.'
##        #return ppRetVal
##
##    def QueryCartesianArray(self):
##        'Returns the Cartesian elements as an array.'
##        #return ppRetVal
##

class _IAgOrientation(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'The hidden interface for IAgOrientation'
    _iid_ = GUID('{3B14008C-48DD-40A3-9A98-34877F9C1C07}')
    _idlflags_ = ['hidden', 'dual', 'nonextensible', 'oleautomation']
_IAgOrientation._methods_ = [
    COMMETHOD([dispid(201), helpstring('Method to change the orientation method to the type specified.')], HRESULT, 'ConvertTo',
              ( ['in'], AgEOrientationType, 'Type' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgOrientation)), 'ppRetVal' )),
    COMMETHOD([dispid(202), helpstring('Returns the orientation method currently being used.'), 'propget'], HRESULT, 'OrientationType',
              ( ['out', 'retval'], POINTER(AgEOrientationType), 'pType' )),
    COMMETHOD([dispid(203), helpstring('Assign a new orientation method.')], HRESULT, 'Assign',
              ( ['in'], POINTER(IAgOrientation), 'pOrientation' )),
    COMMETHOD([dispid(204), helpstring('Helper method to set orientation using the AzEl representation.')], HRESULT, 'AssignAzEl',
              ( ['in'], VARIANT, 'Azimuth' ),
              ( ['in'], VARIANT, 'Elevation' ),
              ( ['in'], AgEAzElAboutBoresight, 'AboutBoresight' )),
    COMMETHOD([dispid(205), helpstring('Helper method to set orientation using the Euler angles representation.')], HRESULT, 'AssignEulerAngles',
              ( ['in'], AgEEulerOrientationSequence, 'Sequence' ),
              ( ['in'], VARIANT, 'A' ),
              ( ['in'], VARIANT, 'B' ),
              ( ['in'], VARIANT, 'C' )),
    COMMETHOD([dispid(206), helpstring('Helper method to set orientation using the Quaternion representation.')], HRESULT, 'AssignQuaternion',
              ( ['in'], c_double, 'QX' ),
              ( ['in'], c_double, 'QY' ),
              ( ['in'], c_double, 'QZ' ),
              ( ['in'], c_double, 'QS' )),
    COMMETHOD([dispid(207), helpstring('Helper method to set orientation using the YPR angles representation.')], HRESULT, 'AssignYPRAngles',
              ( ['in'], AgEYPRAnglesSequence, 'Sequence' ),
              ( ['in'], VARIANT, 'Yaw' ),
              ( ['in'], VARIANT, 'Pitch' ),
              ( ['in'], VARIANT, 'Roll' )),
    COMMETHOD([dispid(208), helpstring('Helper method to get orientation using the AzEl representation.')], HRESULT, 'QueryAzEl',
              ( ['out'], POINTER(VARIANT), 'Azimuth' ),
              ( ['out'], POINTER(VARIANT), 'Elevation' ),
              ( ['out'], POINTER(AgEAzElAboutBoresight), 'AboutBoresight' )),
    COMMETHOD([dispid(209), helpstring('Helper method to get orientation using the Euler angles representation.')], HRESULT, 'QueryEulerAngles',
              ( ['in'], AgEEulerOrientationSequence, 'Sequence' ),
              ( ['out'], POINTER(VARIANT), 'A' ),
              ( ['out'], POINTER(VARIANT), 'B' ),
              ( ['out'], POINTER(VARIANT), 'C' )),
    COMMETHOD([dispid(210), helpstring('Helper method to get orientation using the Quaternion representation.')], HRESULT, 'QueryQuaternion',
              ( ['out'], POINTER(c_double), 'QX' ),
              ( ['out'], POINTER(c_double), 'QY' ),
              ( ['out'], POINTER(c_double), 'QZ' ),
              ( ['out'], POINTER(c_double), 'QS' )),
    COMMETHOD([dispid(211), helpstring('Helper method to get orientation using the YPR angles representation.')], HRESULT, 'QueryYPRAngles',
              ( ['in'], AgEYPRAnglesSequence, 'Sequence' ),
              ( ['out'], POINTER(VARIANT), 'Yaw' ),
              ( ['out'], POINTER(VARIANT), 'Pitch' ),
              ( ['out'], POINTER(VARIANT), 'Roll' )),
    COMMETHOD([dispid(212), helpstring('Returns the AzEl elements as an array.')], HRESULT, 'QueryAzElArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(213), helpstring('Returns the Euler elements as an array.')], HRESULT, 'QueryEulerAnglesArray',
              ( ['in'], AgEEulerOrientationSequence, 'Sequence' ),
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(214), helpstring('Returns the Quaternion elements as an array.')], HRESULT, 'QueryQuaternionArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(215), helpstring('Returns the YPR Angles elements as an array.')], HRESULT, 'QueryYPRAnglesArray',
              ( ['in'], AgEYPRAnglesSequence, 'Sequence' ),
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
]
################################################################
## code template for _IAgOrientation implementation
##class _IAgOrientation_Impl(object):
##    def ConvertTo(self, Type):
##        'Method to change the orientation method to the type specified.'
##        #return ppRetVal
##
##    @property
##    def OrientationType(self):
##        'Returns the orientation method currently being used.'
##        #return pType
##
##    def Assign(self, pOrientation):
##        'Assign a new orientation method.'
##        #return 
##
##    def AssignAzEl(self, Azimuth, Elevation, AboutBoresight):
##        'Helper method to set orientation using the AzEl representation.'
##        #return 
##
##    def AssignEulerAngles(self, Sequence, A, B, C):
##        'Helper method to set orientation using the Euler angles representation.'
##        #return 
##
##    def AssignQuaternion(self, QX, QY, QZ, QS):
##        'Helper method to set orientation using the Quaternion representation.'
##        #return 
##
##    def AssignYPRAngles(self, Sequence, Yaw, Pitch, Roll):
##        'Helper method to set orientation using the YPR angles representation.'
##        #return 
##
##    def QueryAzEl(self):
##        'Helper method to get orientation using the AzEl representation.'
##        #return Azimuth, Elevation, AboutBoresight
##
##    def QueryEulerAngles(self, Sequence):
##        'Helper method to get orientation using the Euler angles representation.'
##        #return A, B, C
##
##    def QueryQuaternion(self):
##        'Helper method to get orientation using the Quaternion representation.'
##        #return QX, QY, QZ, QS
##
##    def QueryYPRAngles(self, Sequence):
##        'Helper method to get orientation using the YPR angles representation.'
##        #return Yaw, Pitch, Roll
##
##    def QueryAzElArray(self):
##        'Returns the AzEl elements as an array.'
##        #return ppRetVal
##
##    def QueryEulerAnglesArray(self, Sequence):
##        'Returns the Euler elements as an array.'
##        #return ppRetVal
##
##    def QueryQuaternionArray(self):
##        'Returns the Quaternion elements as an array.'
##        #return ppRetVal
##
##    def QueryYPRAnglesArray(self, Sequence):
##        'Returns the YPR Angles elements as an array.'
##        #return ppRetVal
##

class AgOrientation(CoClass):
    'Class defining the orientation of an orbit.'
    _reg_clsid_ = GUID('{A3F1394D-B573-4974-A855-E3538DD4EDBF}')
    _idlflags_ = ['hidden', 'noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{00DD7BD4-53D5-4870-996B-8ADB8AF904FA}', 1, 0)
AgOrientation._com_interfaces_ = [_IAgOrientation, IAgOrientation]

class _IAgCROrientationQuaternion(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'The hidden interface for IAgOrientationQuaternion'
    _iid_ = GUID('{1EDB1BA4-4B95-492C-8E8D-3147E503BBB3}')
    _idlflags_ = ['hidden', 'dual', 'nonextensible', 'oleautomation']
_IAgCROrientationQuaternion._methods_ = [
    COMMETHOD([dispid(201), helpstring('qx vector component. Dimensionless'), 'propget'], HRESULT, 'QX',
              ( ['out', 'retval'], POINTER(c_double), 'pVal' )),
    COMMETHOD([dispid(201), helpstring('qx vector component. Dimensionless'), 'propput'], HRESULT, 'QX',
              ( ['in'], c_double, 'pVal' )),
    COMMETHOD([dispid(202), helpstring('qy vector component. Dimensionless.'), 'propget'], HRESULT, 'QY',
              ( ['out', 'retval'], POINTER(c_double), 'pVal' )),
    COMMETHOD([dispid(202), helpstring('qy vector component. Dimensionless.'), 'propput'], HRESULT, 'QY',
              ( ['in'], c_double, 'pVal' )),
    COMMETHOD([dispid(203), helpstring('qz vector component. Dimensionless.'), 'propget'], HRESULT, 'QZ',
              ( ['out', 'retval'], POINTER(c_double), 'pVal' )),
    COMMETHOD([dispid(203), helpstring('qz vector component. Dimensionless.'), 'propput'], HRESULT, 'QZ',
              ( ['in'], c_double, 'pVal' )),
    COMMETHOD([dispid(204), helpstring('qs scalar component. Dimensionless.'), 'propget'], HRESULT, 'QS',
              ( ['out', 'retval'], POINTER(c_double), 'pVal' )),
    COMMETHOD([dispid(204), helpstring('qs scalar component. Dimensionless.'), 'propput'], HRESULT, 'QS',
              ( ['in'], c_double, 'pVal' )),
    COMMETHOD([dispid(205), helpstring('This property is deprecated. Use AssignQuaternion instead.')], HRESULT, 'SetValues',
              ( ['in'], c_double, 'QX' ),
              ( ['in'], c_double, 'QY' ),
              ( ['in'], c_double, 'QZ' ),
              ( ['in'], c_double, 'QS' )),
    COMMETHOD([dispid(401), helpstring('Method to change the orientation method to the type specified.')], HRESULT, 'ConvertTo',
              ( ['in'], AgEOrientationType, 'Type' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgOrientation)), 'ppIAgOrientation' )),
    COMMETHOD([dispid(402), helpstring('Returns the orientation method currently being used.'), 'propget'], HRESULT, 'OrientationType',
              ( ['out', 'retval'], POINTER(AgEOrientationType), 'pType' )),
    COMMETHOD([dispid(403), helpstring('Assign a new orientation method.')], HRESULT, 'Assign',
              ( ['in'], POINTER(IAgOrientation), 'pOrientation' )),
    COMMETHOD([dispid(404), helpstring('Helper method to set orientation using the AzEl representation.')], HRESULT, 'AssignAzEl',
              ( ['in'], VARIANT, 'Azimuth' ),
              ( ['in'], VARIANT, 'Elevation' ),
              ( ['in'], AgEAzElAboutBoresight, 'AboutBoresight' )),
    COMMETHOD([dispid(405), helpstring('Helper method to set orientation using the Euler angles representation.')], HRESULT, 'AssignEulerAngles',
              ( ['in'], AgEEulerOrientationSequence, 'Sequence' ),
              ( ['in'], VARIANT, 'A' ),
              ( ['in'], VARIANT, 'B' ),
              ( ['in'], VARIANT, 'C' )),
    COMMETHOD([dispid(406), helpstring('Helper method to set orientation using the Quaternion representation.')], HRESULT, 'AssignQuaternion',
              ( ['in'], c_double, 'QX' ),
              ( ['in'], c_double, 'QY' ),
              ( ['in'], c_double, 'QZ' ),
              ( ['in'], c_double, 'QS' )),
    COMMETHOD([dispid(407), helpstring('Helper method to set orientation using the YPR angles representation.')], HRESULT, 'AssignYPRAngles',
              ( ['in'], AgEYPRAnglesSequence, 'Sequence' ),
              ( ['in'], VARIANT, 'Yaw' ),
              ( ['in'], VARIANT, 'Pitch' ),
              ( ['in'], VARIANT, 'Roll' )),
    COMMETHOD([dispid(408), helpstring('Helper method to get orientation using the AzEl representation.')], HRESULT, 'QueryAzEl',
              ( ['out'], POINTER(VARIANT), 'Azimuth' ),
              ( ['out'], POINTER(VARIANT), 'Elevation' ),
              ( ['out'], POINTER(AgEAzElAboutBoresight), 'AboutBoresight' )),
    COMMETHOD([dispid(409), helpstring('Helper method to get orientation using the Euler angles representation.')], HRESULT, 'QueryEulerAngles',
              ( ['in'], AgEEulerOrientationSequence, 'Sequence' ),
              ( ['out'], POINTER(VARIANT), 'A' ),
              ( ['out'], POINTER(VARIANT), 'B' ),
              ( ['out'], POINTER(VARIANT), 'C' )),
    COMMETHOD([dispid(410), helpstring('Helper method to get orientation using the Quaternion representation.')], HRESULT, 'QueryQuaternion',
              ( ['out'], POINTER(c_double), 'QX' ),
              ( ['out'], POINTER(c_double), 'QY' ),
              ( ['out'], POINTER(c_double), 'QZ' ),
              ( ['out'], POINTER(c_double), 'QS' )),
    COMMETHOD([dispid(411), helpstring('Helper method to get orientation using the YPR angles representation.')], HRESULT, 'QueryYPRAngles',
              ( ['in'], AgEYPRAnglesSequence, 'Sequence' ),
              ( ['out'], POINTER(VARIANT), 'Yaw' ),
              ( ['out'], POINTER(VARIANT), 'Pitch' ),
              ( ['out'], POINTER(VARIANT), 'Roll' )),
    COMMETHOD([dispid(412), helpstring('Returns the AzEl elements as an array.')], HRESULT, 'QueryAzElArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(413), helpstring('Returns the Euler elements as an array.')], HRESULT, 'QueryEulerAnglesArray',
              ( ['in'], AgEEulerOrientationSequence, 'Sequence' ),
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(414), helpstring('Returns the Quaternion elements as an array.')], HRESULT, 'QueryQuaternionArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(415), helpstring('Returns the YPR Angles elements as an array.')], HRESULT, 'QueryYPRAnglesArray',
              ( ['in'], AgEYPRAnglesSequence, 'Sequence' ),
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(416), helpstring('Gets or sets the location offset cartesian vector.'), 'propget'], HRESULT, 'PositionOffset',
              ( ['out', 'retval'], POINTER(POINTER(IAgCartesian3Vector)), 'ppRetVal' )),
]
################################################################
## code template for _IAgCROrientationQuaternion implementation
##class _IAgCROrientationQuaternion_Impl(object):
##    def _get(self):
##        'qx vector component. Dimensionless'
##        #return pVal
##    def _set(self, pVal):
##        'qx vector component. Dimensionless'
##    QX = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'qy vector component. Dimensionless.'
##        #return pVal
##    def _set(self, pVal):
##        'qy vector component. Dimensionless.'
##    QY = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'qz vector component. Dimensionless.'
##        #return pVal
##    def _set(self, pVal):
##        'qz vector component. Dimensionless.'
##    QZ = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'qs scalar component. Dimensionless.'
##        #return pVal
##    def _set(self, pVal):
##        'qs scalar component. Dimensionless.'
##    QS = property(_get, _set, doc = _set.__doc__)
##
##    def SetValues(self, QX, QY, QZ, QS):
##        'This property is deprecated. Use AssignQuaternion instead.'
##        #return 
##
##    def ConvertTo(self, Type):
##        'Method to change the orientation method to the type specified.'
##        #return ppIAgOrientation
##
##    @property
##    def OrientationType(self):
##        'Returns the orientation method currently being used.'
##        #return pType
##
##    def Assign(self, pOrientation):
##        'Assign a new orientation method.'
##        #return 
##
##    def AssignAzEl(self, Azimuth, Elevation, AboutBoresight):
##        'Helper method to set orientation using the AzEl representation.'
##        #return 
##
##    def AssignEulerAngles(self, Sequence, A, B, C):
##        'Helper method to set orientation using the Euler angles representation.'
##        #return 
##
##    def AssignQuaternion(self, QX, QY, QZ, QS):
##        'Helper method to set orientation using the Quaternion representation.'
##        #return 
##
##    def AssignYPRAngles(self, Sequence, Yaw, Pitch, Roll):
##        'Helper method to set orientation using the YPR angles representation.'
##        #return 
##
##    def QueryAzEl(self):
##        'Helper method to get orientation using the AzEl representation.'
##        #return Azimuth, Elevation, AboutBoresight
##
##    def QueryEulerAngles(self, Sequence):
##        'Helper method to get orientation using the Euler angles representation.'
##        #return A, B, C
##
##    def QueryQuaternion(self):
##        'Helper method to get orientation using the Quaternion representation.'
##        #return QX, QY, QZ, QS
##
##    def QueryYPRAngles(self, Sequence):
##        'Helper method to get orientation using the YPR angles representation.'
##        #return Yaw, Pitch, Roll
##
##    def QueryAzElArray(self):
##        'Returns the AzEl elements as an array.'
##        #return ppRetVal
##
##    def QueryEulerAnglesArray(self, Sequence):
##        'Returns the Euler elements as an array.'
##        #return ppRetVal
##
##    def QueryQuaternionArray(self):
##        'Returns the Quaternion elements as an array.'
##        #return ppRetVal
##
##    def QueryYPRAnglesArray(self, Sequence):
##        'Returns the YPR Angles elements as an array.'
##        #return ppRetVal
##
##    @property
##    def PositionOffset(self):
##        'Gets or sets the location offset cartesian vector.'
##        #return ppRetVal
##

class AgCROrientationQuaternion(CoClass):
    'Quaternion orientation method.'
    _reg_clsid_ = GUID('{066D9B48-0E24-4B56-9F25-07E60DDEA3E0}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{00DD7BD4-53D5-4870-996B-8ADB8AF904FA}', 1, 0)
AgCROrientationQuaternion._com_interfaces_ = [_IAgCROrientationQuaternion, IAgOrientationQuaternion, IAgOrientation, IAgOrientationPositionOffset]

IAgOrbitState._methods_ = [
    COMMETHOD([helpstring('Method to changes the coordinate type to the type specified.')], HRESULT, 'ConvertTo',
              ( ['in'], AgEOrbitStateType, 'Type' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgOrbitState)), 'ppIAgOrbitState' )),
    COMMETHOD(['propget', helpstring('Returns the coordinate type currently being used.')], HRESULT, 'OrbitStateType',
              ( ['out', 'retval'], POINTER(AgEOrbitStateType), 'pType' )),
    COMMETHOD([helpstring('Assign a new coordinate type.')], HRESULT, 'Assign',
              ( ['in'], POINTER(IAgOrbitState), 'pOrbitState' )),
    COMMETHOD([helpstring('Helper method to assign a new orbit state using Classical representation')], HRESULT, 'AssignClassical',
              ( ['in'], AgECoordinateSystem, 'ECoordinateSystem' ),
              ( ['in'], c_double, 'SemiMajorAxis' ),
              ( ['in'], c_double, 'Eccentricity' ),
              ( ['in'], c_double, 'Inclination' ),
              ( ['in'], c_double, 'ArgOfPerigee' ),
              ( ['in'], c_double, 'RAAN' ),
              ( ['in'], c_double, 'MeanAnomaly' )),
    COMMETHOD([helpstring('Helper method to assign a new orbit state using Cartesian representation')], HRESULT, 'AssignCartesian',
              ( ['in'], AgECoordinateSystem, 'ECoordinateSystem' ),
              ( ['in'], c_double, 'XPosition' ),
              ( ['in'], c_double, 'YPosition' ),
              ( ['in'], c_double, 'ZPosition' ),
              ( ['in'], c_double, 'XVelocity' ),
              ( ['in'], c_double, 'YVelocity' ),
              ( ['in'], c_double, 'ZVelocity' )),
    COMMETHOD([helpstring('Helper method to assign a new orbit state using Geodetic representation')], HRESULT, 'AssignGeodetic',
              ( ['in'], AgECoordinateSystem, 'ECoordinateSystem' ),
              ( ['in'], c_double, 'Latitude' ),
              ( ['in'], c_double, 'Longitude' ),
              ( ['in'], c_double, 'Altitude' ),
              ( ['in'], c_double, 'LatitudeRate' ),
              ( ['in'], c_double, 'LongitudeRate' ),
              ( ['in'], c_double, 'AltitudeRate' )),
    COMMETHOD([helpstring('Helper method to assign a new orbit state using Equinoctial representation')], HRESULT, 'AssignEquinoctialPosigrade',
              ( ['in'], AgECoordinateSystem, 'ECoordinateSystem' ),
              ( ['in'], c_double, 'SemiMajorAxis' ),
              ( ['in'], c_double, 'H' ),
              ( ['in'], c_double, 'K' ),
              ( ['in'], c_double, 'P' ),
              ( ['in'], c_double, 'Q' ),
              ( ['in'], c_double, 'MeanLon' )),
    COMMETHOD([helpstring('Helper method to assign a new orbit state using Equinoctial representation')], HRESULT, 'AssignEquinoctialRetrograde',
              ( ['in'], AgECoordinateSystem, 'ECoordinateSystem' ),
              ( ['in'], c_double, 'SemiMajorAxis' ),
              ( ['in'], c_double, 'H' ),
              ( ['in'], c_double, 'K' ),
              ( ['in'], c_double, 'P' ),
              ( ['in'], c_double, 'Q' ),
              ( ['in'], c_double, 'MeanLon' )),
    COMMETHOD([helpstring('Helper method to assign a new orbit state using Mixed Spherical representation')], HRESULT, 'AssignMixedSpherical',
              ( ['in'], AgECoordinateSystem, 'ECoordinateSystem' ),
              ( ['in'], c_double, 'Latitude' ),
              ( ['in'], c_double, 'Longitude' ),
              ( ['in'], c_double, 'Altitude' ),
              ( ['in'], c_double, 'HorFlightPathAngle' ),
              ( ['in'], c_double, 'FlightPathAzimuth' ),
              ( ['in'], c_double, 'Velocity' )),
    COMMETHOD([helpstring('Helper method to assign a new orbit state using Spherical representation')], HRESULT, 'AssignSpherical',
              ( ['in'], AgECoordinateSystem, 'ECoordinateSystem' ),
              ( ['in'], c_double, 'RightAscension' ),
              ( ['in'], c_double, 'Declination' ),
              ( ['in'], c_double, 'Radius' ),
              ( ['in'], c_double, 'HorFlightPathAngle' ),
              ( ['in'], c_double, 'FlightPathAzimuth' ),
              ( ['in'], c_double, 'Velocity' )),
    COMMETHOD(['propget', helpstring('Gets the central body.')], HRESULT, 'CentralBodyName',
              ( ['out', 'retval'], POINTER(BSTR), 'pCBName' )),
    COMMETHOD(['propget', helpstring('The state epoch')], HRESULT, 'Epoch',
              ( ['out', 'retval'], POINTER(VARIANT), 'pRetVal' )),
    COMMETHOD(['propput', helpstring('The state epoch')], HRESULT, 'Epoch',
              ( ['in'], VARIANT, 'pRetVal' )),
]
################################################################
## code template for IAgOrbitState implementation
##class IAgOrbitState_Impl(object):
##    def ConvertTo(self, Type):
##        'Method to changes the coordinate type to the type specified.'
##        #return ppIAgOrbitState
##
##    @property
##    def OrbitStateType(self):
##        'Returns the coordinate type currently being used.'
##        #return pType
##
##    def Assign(self, pOrbitState):
##        'Assign a new coordinate type.'
##        #return 
##
##    def AssignClassical(self, ECoordinateSystem, SemiMajorAxis, Eccentricity, Inclination, ArgOfPerigee, RAAN, MeanAnomaly):
##        'Helper method to assign a new orbit state using Classical representation'
##        #return 
##
##    def AssignCartesian(self, ECoordinateSystem, XPosition, YPosition, ZPosition, XVelocity, YVelocity, ZVelocity):
##        'Helper method to assign a new orbit state using Cartesian representation'
##        #return 
##
##    def AssignGeodetic(self, ECoordinateSystem, Latitude, Longitude, Altitude, LatitudeRate, LongitudeRate, AltitudeRate):
##        'Helper method to assign a new orbit state using Geodetic representation'
##        #return 
##
##    def AssignEquinoctialPosigrade(self, ECoordinateSystem, SemiMajorAxis, H, K, P, Q, MeanLon):
##        'Helper method to assign a new orbit state using Equinoctial representation'
##        #return 
##
##    def AssignEquinoctialRetrograde(self, ECoordinateSystem, SemiMajorAxis, H, K, P, Q, MeanLon):
##        'Helper method to assign a new orbit state using Equinoctial representation'
##        #return 
##
##    def AssignMixedSpherical(self, ECoordinateSystem, Latitude, Longitude, Altitude, HorFlightPathAngle, FlightPathAzimuth, Velocity):
##        'Helper method to assign a new orbit state using Mixed Spherical representation'
##        #return 
##
##    def AssignSpherical(self, ECoordinateSystem, RightAscension, Declination, Radius, HorFlightPathAngle, FlightPathAzimuth, Velocity):
##        'Helper method to assign a new orbit state using Spherical representation'
##        #return 
##
##    @property
##    def CentralBodyName(self):
##        'Gets the central body.'
##        #return pCBName
##
##    def _get(self):
##        'The state epoch'
##        #return pRetVal
##    def _set(self, pRetVal):
##        'The state epoch'
##    Epoch = property(_get, _set, doc = _set.__doc__)
##

class AgPlanetodetic(CoClass):
    'Class defining Planetodetic position.'
    _reg_clsid_ = GUID('{BC77E74E-6E37-4398-AEBD-1E905F04505C}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{00DD7BD4-53D5-4870-996B-8ADB8AF904FA}', 1, 0)
AgPlanetodetic._com_interfaces_ = [_IAgPlanetodetic, IAgPlanetodetic, IAgPosition]

_IAgCartesian._methods_ = [
    COMMETHOD([dispid(201), helpstring('Dimension depends on context.'), 'propget'], HRESULT, 'X',
              ( ['out', 'retval'], POINTER(c_double), 'pVal' )),
    COMMETHOD([dispid(201), helpstring('Dimension depends on context.'), 'propput'], HRESULT, 'X',
              ( ['in'], c_double, 'pVal' )),
    COMMETHOD([dispid(202), helpstring('Dimension depends on context.'), 'propget'], HRESULT, 'Y',
              ( ['out', 'retval'], POINTER(c_double), 'pVal' )),
    COMMETHOD([dispid(202), helpstring('Dimension depends on context.'), 'propput'], HRESULT, 'Y',
              ( ['in'], c_double, 'pVal' )),
    COMMETHOD([dispid(203), helpstring('Dimension depends on context.'), 'propget'], HRESULT, 'Z',
              ( ['out', 'retval'], POINTER(c_double), 'pVal' )),
    COMMETHOD([dispid(203), helpstring('Dimension depends on context.'), 'propput'], HRESULT, 'Z',
              ( ['in'], c_double, 'pVal' )),
    COMMETHOD([dispid(204), helpstring('This property is deprecated. Use AssignCartesian instead.')], HRESULT, 'SetValues',
              ( ['in'], c_double, 'X' ),
              ( ['in'], c_double, 'Y' ),
              ( ['in'], c_double, 'Z' )),
    COMMETHOD([dispid(401), helpstring('Changes the position coordinates to type specified.')], HRESULT, 'ConvertTo',
              ( ['in'], AgEPositionType, 'Type' ),
              ( ['out', 'retval'], POINTER(POINTER(IAgPosition)), 'ppIAgPosition' )),
    COMMETHOD([dispid(402), helpstring('Gets the type of position currently being used.'), 'propget'], HRESULT, 'PosType',
              ( ['out', 'retval'], POINTER(AgEPositionType), 'pType' )),
    COMMETHOD([dispid(403), helpstring('This assigns the coordinates into the system.')], HRESULT, 'Assign',
              ( ['in'], POINTER(IAgPosition), 'pPosition' )),
    COMMETHOD([dispid(404), helpstring('Helper method to assign the position using the Geocentric representation.')], HRESULT, 'AssignGeocentric',
              ( ['in'], VARIANT, 'Lat' ),
              ( ['in'], VARIANT, 'Lon' ),
              ( ['in'], c_double, 'Alt' )),
    COMMETHOD([dispid(405), helpstring('Helper method to assign the position using the Geodetic representation.')], HRESULT, 'AssignGeodetic',
              ( ['in'], VARIANT, 'Lat' ),
              ( ['in'], VARIANT, 'Lon' ),
              ( ['in'], c_double, 'Alt' )),
    COMMETHOD([dispid(406), helpstring('Helper method to assign the position using the Spherical representation')], HRESULT, 'AssignSpherical',
              ( ['in'], VARIANT, 'Lat' ),
              ( ['in'], VARIANT, 'Lon' ),
              ( ['in'], c_double, 'Radius' )),
    COMMETHOD([dispid(407), helpstring('Helper method to assign the position using the Cylindrical representation')], HRESULT, 'AssignCylindrical',
              ( ['in'], c_double, 'Radius' ),
              ( ['in'], c_double, 'Z' ),
              ( ['in'], VARIANT, 'Lon' )),
    COMMETHOD([dispid(408), helpstring('Helper method to assign the position using the Cartesian representation')], HRESULT, 'AssignCartesian',
              ( ['in'], c_double, 'X' ),
              ( ['in'], c_double, 'Y' ),
              ( ['in'], c_double, 'Z' )),
    COMMETHOD([dispid(409), helpstring('Helper method to assign the position using the Planetocentric representation')], HRESULT, 'AssignPlanetocentric',
              ( ['in'], VARIANT, 'Lat' ),
              ( ['in'], VARIANT, 'Lon' ),
              ( ['in'], c_double, 'Alt' )),
    COMMETHOD([dispid(410), helpstring('Helper method to assign the position using the Planetodetic representation')], HRESULT, 'AssignPlanetodetic',
              ( ['in'], VARIANT, 'Lat' ),
              ( ['in'], VARIANT, 'Lon' ),
              ( ['in'], c_double, 'Alt' )),
    COMMETHOD([dispid(411), helpstring('Helper method to get the position using the Planetocentric representation')], HRESULT, 'QueryPlanetocentric',
              ( ['out'], POINTER(VARIANT), 'Lat' ),
              ( ['out'], POINTER(VARIANT), 'Lon' ),
              ( ['out'], POINTER(c_double), 'Alt' )),
    COMMETHOD([dispid(412), helpstring('Helper method to get the position using the Planetodetic representation')], HRESULT, 'QueryPlanetodetic',
              ( ['out'], POINTER(VARIANT), 'Lat' ),
              ( ['out'], POINTER(VARIANT), 'Lon' ),
              ( ['out'], POINTER(c_double), 'Alt' )),
    COMMETHOD([dispid(413), helpstring('Helper method to get the position using the Spherical representation')], HRESULT, 'QuerySpherical',
              ( ['out'], POINTER(VARIANT), 'Lat' ),
              ( ['out'], POINTER(VARIANT), 'Lon' ),
              ( ['out'], POINTER(c_double), 'Radius' )),
    COMMETHOD([dispid(414), helpstring('Helper method to get the position using the Cylindrical representation')], HRESULT, 'QueryCylindrical',
              ( ['out'], POINTER(c_double), 'Radius' ),
              ( ['out'], POINTER(VARIANT), 'Lon' ),
              ( ['out'], POINTER(c_double), 'Z' )),
    COMMETHOD([dispid(415), helpstring('Helper method to get the position using the Cartesian representation')], HRESULT, 'QueryCartesian',
              ( ['out'], POINTER(c_double), 'X' ),
              ( ['out'], POINTER(c_double), 'Y' ),
              ( ['out'], POINTER(c_double), 'Z' )),
    COMMETHOD([dispid(416), helpstring('Gets the central body.'), 'propget'], HRESULT, 'CentralBodyName',
              ( ['out', 'retval'], POINTER(BSTR), 'pCBName' )),
    COMMETHOD([dispid(417), helpstring('Returns the Planetocentric elements as an array.')], HRESULT, 'QueryPlanetocentricArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(418), helpstring('Returns the Planetodetic elements as an array.')], HRESULT, 'QueryPlanetodeticArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(419), helpstring('Returns the Spherical elements as an array.')], HRESULT, 'QuerySphericalArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(420), helpstring('Returns the Cylindrical elements as an array.')], HRESULT, 'QueryCylindricalArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
    COMMETHOD([dispid(421), helpstring('Returns the Cartesian elements as an array.')], HRESULT, 'QueryCartesianArray',
              ( ['out', 'retval'], POINTER(_midlSAFEARRAY(VARIANT)), 'ppRetVal' )),
]
################################################################
## code template for _IAgCartesian implementation
##class _IAgCartesian_Impl(object):
##    def _get(self):
##        'Dimension depends on context.'
##        #return pVal
##    def _set(self, pVal):
##        'Dimension depends on context.'
##    X = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Dimension depends on context.'
##        #return pVal
##    def _set(self, pVal):
##        'Dimension depends on context.'
##    Y = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'Dimension depends on context.'
##        #return pVal
##    def _set(self, pVal):
##        'Dimension depends on context.'
##    Z = property(_get, _set, doc = _set.__doc__)
##
##    def SetValues(self, X, Y, Z):
##        'This property is deprecated. Use AssignCartesian instead.'
##        #return 
##
##    def ConvertTo(self, Type):
##        'Changes the position coordinates to type specified.'
##        #return ppIAgPosition
##
##    @property
##    def PosType(self):
##        'Gets the type of position currently being used.'
##        #return pType
##
##    def Assign(self, pPosition):
##        'This assigns the coordinates into the system.'
##        #return 
##
##    def AssignGeocentric(self, Lat, Lon, Alt):
##        'Helper method to assign the position using the Geocentric representation.'
##        #return 
##
##    def AssignGeodetic(self, Lat, Lon, Alt):
##        'Helper method to assign the position using the Geodetic representation.'
##        #return 
##
##    def AssignSpherical(self, Lat, Lon, Radius):
##        'Helper method to assign the position using the Spherical representation'
##        #return 
##
##    def AssignCylindrical(self, Radius, Z, Lon):
##        'Helper method to assign the position using the Cylindrical representation'
##        #return 
##
##    def AssignCartesian(self, X, Y, Z):
##        'Helper method to assign the position using the Cartesian representation'
##        #return 
##
##    def AssignPlanetocentric(self, Lat, Lon, Alt):
##        'Helper method to assign the position using the Planetocentric representation'
##        #return 
##
##    def AssignPlanetodetic(self, Lat, Lon, Alt):
##        'Helper method to assign the position using the Planetodetic representation'
##        #return 
##
##    def QueryPlanetocentric(self):
##        'Helper method to get the position using the Planetocentric representation'
##        #return Lat, Lon, Alt
##
##    def QueryPlanetodetic(self):
##        'Helper method to get the position using the Planetodetic representation'
##        #return Lat, Lon, Alt
##
##    def QuerySpherical(self):
##        'Helper method to get the position using the Spherical representation'
##        #return Lat, Lon, Radius
##
##    def QueryCylindrical(self):
##        'Helper method to get the position using the Cylindrical representation'
##        #return Radius, Lon, Z
##
##    def QueryCartesian(self):
##        'Helper method to get the position using the Cartesian representation'
##        #return X, Y, Z
##
##    @property
##    def CentralBodyName(self):
##        'Gets the central body.'
##        #return pCBName
##
##    def QueryPlanetocentricArray(self):
##        'Returns the Planetocentric elements as an array.'
##        #return ppRetVal
##
##    def QueryPlanetodeticArray(self):
##        'Returns the Planetodetic elements as an array.'
##        #return ppRetVal
##
##    def QuerySphericalArray(self):
##        'Returns the Spherical elements as an array.'
##        #return ppRetVal
##
##    def QueryCylindricalArray(self):
##        'Returns the Cylindrical elements as an array.'
##        #return ppRetVal
##
##    def QueryCartesianArray(self):
##        'Returns the Cartesian elements as an array.'
##        #return ppRetVal
##

__all__ = [ 'eDashDotDotted', '_IAgOrientation', 'ePYR',
           'eFillStyleDiagonalStripe1', 'IAgExecMultiCmdResult',
           'e232', 'AgECoordinateSystem', 'IAgPropertyInfo',
           'eCoordinateSystemB1950', 'eGeodetic',
           'IAgUnitPrefsUnitCollection', 'AgEDirectionType', 'eAzEl',
           'AgExecCmdResult', 'eFillStyleDiagonalStripe2',
           'eLogMsgForceInfo', 'eOrbitStateEquinoctial',
           'eCoordinateSystemTrueEclipticOfDate',
           'ePropertyInfoValueTypeQuantity',
           'eCoordinateSystemInertial', 'eOrbitStateCartesian',
           'e212', 'AgEEulerOrientationSequence', 'eLDashDot',
           'IAgPosition', '_IAgPropertyInfo', 'IAgOrientationAzEl',
           'e131', 'IAgDoublesCollection', 'IAgDirectionRADec',
           'e132', 'eRYP', 'eDot', 'eAzElAboutBoresightRotate',
           'eMDash', 'eOrbitStateMixedSpherical', 'eDirXYZ',
           'eMDashDot', 'IAgUnitPrefsDimCollection',
           '_IAgUnitPrefsUnit', 'eDotDashed', '_IAgSpherical',
           '_IAgGeodetic', 'AgEExecMultiCmdResultAction',
           'eSpherical', 'eCoordinateSystemFixedIAU2003',
           '_IAgCartesian3Vector', 'eQuaternion', 'eContinueOnError',
           'eLogMsgDispDefault', 'eYRP', 'IAgPlanetocentric',
           'IAgDirection', 'eLSDash', 'AgCROrientationQuaternion',
           'eLogMsgInfo', '_IAgDate', 'eSDashDot', 'AgOrientation',
           'IAgGeodetic', 'AgEOrbitStateType', 'IAgConversionUtility',
           'eLMSDash', 'e231', 'IAgCartesian', 'AgPropertyInfo',
           'eCoordinateSystemAlignmentAtEpoch', '_IAgUnitPrefsDim',
           'eCoordinateSystemTEMEOfEpoch', 'eOrbitStateSpherical',
           'IAgPlanetodetic', 'IAgOrientationPositionOffset',
           'eFillStyleDiagonalHatch', 'AgExecMultiCmdResult',
           'AgEPropertyInfoValueType', 'eCoordinateSystemJ2000',
           'eCylindrical', '_IAgOrientationQuaternion',
           'AgUnitPrefsUnit', 'AgELineStyle',
           'eCoordinateSystemMeanOfDate', 'AgEAzElAboutBoresight',
           'AgPropertyInfoCollection', 'AgDirectionEuler',
           'AgCartesian2Vector', 'e123', 'e313', 'eLDash',
           'AgPlanetodetic', 'IAgUnitPrefsUnit', 'AgRuntimeTypeInfo',
           'ePlanetocentric', 'IAgOrientationQuaternion', 'IAgDate',
           'eDirPR', 'IAgOrientationYPRAngles', 'eFillStyleHatch',
           'AgUnitPrefsDim', 'eOrbitStateGeodetic',
           '_IAgDirectionEuler', 'AgOrientationAzEl', 'IAgQuantity',
           'IAgOrbitState', 'eEulerAngles', 'IAgCylindrical',
           '_IAgCartesian', 'AgCylindrical', 'AgPlanetocentric',
           'AgDirectionXYZ', 'eLongDashed', 'AgConversionUtility',
           'AgDirection', 'IAgExecCmdResult', 'IAgUnitPrefsDim',
           '_IAgCROrientationQuaternion', '_IAgDirectionPR', 'e321',
           'AgDoublesCollection', '_IAgCROrientationOffsetCart',
           '_IAgPlanetodetic', 'ePRY', '_IAgConversionUtility',
           'AgOrientationEulerAngles', '_IAgCROrientationYPRAngles',
           'eAzElAboutBoresightHold', '_IAgCROrientationEulerAngles',
           'AgUnitPrefsUnitCollection', 'eSolid', 'eLogMsgWarning',
           'eCoordinateSystemMeanOfEpoch', '_IAgDirection',
           'AgCROrientationEulerAngles', '_IAgCartesian2Vector',
           'eExceptionOnError', 'eCoordinateSystemTEMEOfDate',
           'eDotted', '_IAgCylindrical', 'AgCartesian', 'eYPRAngles',
           'AgCROrientationAzEl', 'eCoordinateSystemFixed',
           'eCoordinateSystemMeanEarth', 'eRPY',
           'IAgPropertyInfoCollection', 'AgDate', 'e21',
           'eFillStyleSolid', 'ePropertyInfoValueTypeBool',
           'eCoordinateSystemFixedNoLibration', 'e213',
           'ePropertyInfoValueTypeString', 'ePR',
           'AgOrientationQuaternion', '_IAgRuntimeTypeInfo',
           'eLogMsgDispAll', 'IAgOrientationEulerAngles',
           'AgCROrientationOffsetCart',
           'eCoordinateSystemJ2000Ecliptic', '_IAgOrientationAzEl',
           'eCoordinateSystemICRF', 'ePropertyInfoValueTypeReal',
           'AgEFillStyle', '_IAgOrientationEulerAngles', 'eLMDash',
           'e312', 'ePropertyInfoValueTypeInt', 'eDirRADec',
           'eCoordinateSystemPrincipalAxes421',
           '_IAgCROrientationAzEl', 'ePropertyInfoValueTypeInterface',
           'eCoordinateSystemTrueOfRefDate', 'AgSpherical',
           'AgEOrientationType', 'e121', 'eLogMsgDebug',
           'eLogMsgDispMsgWin', 'eCoordinateSystemPrincipalAxes403',
           'IAgLocationData', 'eStopOnError',
           'eCoordinateSystemTrueOfDate', 'AgDirectionPR',
           'eLogMsgAlarm', '_IAgOrientationYPRAngles',
           'AgOrientationYPRAngles', 'e323', '_IAgDirectionRADec',
           '_IAgOrbitState', 'eLogMsgDispStatusBar',
           'eCoordinateSystemTrueOfEpoch', 'AgEYPRAnglesSequence',
           'AgPosition', 'AgCROrientationYPRAngles',
           'eFillStyleVerticalStripe', 'IAgRuntimeTypeInfo',
           'AgQuantity', 'IAgDirectionEuler', 'eGeocentric',
           'AgELogMsgDispID', '_IAgDirectionXYZ', 'eCartesian',
           'eMSDash', 'ePropertyInfoValueTypeDate',
           'IAgCartesian3Vector', 'AgEPRSequence', 'IAgDirectionXYZ',
           'AgGeodetic', 'eSDash', 'eYPR', 'eDashed',
           'eOrbitStateDelaunay', 'eLongDash', 'eFillStyleScreen',
           'IAgGeocentric', 'AgDirectionRADec', 'IAgCartesian2Vector',
           'e31', '_IAgQuantity', 'eCoordinateSystemPrincipalAxes430',
           'e32', 'ePlanetodetic', 'AgEEulerDirectionSequence',
           'eOrbitStateClassical', '_IAgPlanetocentric',
           'IAgDirectionPR', '_IAgPosition', 'IAgSpherical',
           'AgELogMsgType', 'eFillStyleHorizontalStripe', 'eDirEuler',
           'eIgnoreExecCmdResult', 'IAgOrientation', 'e12',
           'AgUnitPrefsDimCollection', 'AgGeocentric',
           'AgEPositionType', 'eCoordinateSystemUnknown',
           '_IAgGeocentric', 'AgCartesian3Vector']
from comtypes import _check_version; _check_version('', 1491698322.000000)
