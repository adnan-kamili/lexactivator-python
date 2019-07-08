from ctypes import *
import os
import sys
import platform
import inspect
import subprocess
import ctypes
import ctypes.util


def UNCHECKED(type):
    if (hasattr(type, "_type_") and isinstance(type._type_, str)
            and type._type_ != "P"):
        return type
    else:
        return c_void_p


def is_os_64bit():
    return platform.machine().endswith('64')


def is_musl():
    if 'musl' in subprocess.check_output(['ldd', '--version']):
        return True
    return False


def get_library_path():
    compiler = 'gcc'
    arch = 'x86'
    if(is_os_64bit()):
        arch = 'x86_64'
    # Get the working directory of this file
    filename = inspect.getframeinfo(inspect.currentframe()).filename
    dir_path = os.path.dirname(os.path.abspath(filename))
    # dir_path = os.getcwd()
    if sys.platform == 'darwin':
        return os.path.join(dir_path, "libs/macos/"+arch+"/libLexActivator.dylib")
    elif sys.platform == 'linux':
        if(is_musl()):
            compiler = 'musl'
        return os.path.join(dir_path, "libs/linux/"+compiler+"/"+arch+"/libLexActivator.so")
    elif sys.platform == 'win32':
        return os.path.join(dir_path, "libs/win32/"+arch+"/LexActivator.dll")
    else:
        raise TypeError("Platform not supported!")


def load_library(path):
    if sys.platform == 'darwin':
        return ctypes.CDLL(path, ctypes.RTLD_GLOBAL)
    elif sys.platform == 'linux':
        return ctypes.cdll.LoadLibrary(path)
    elif sys.platform == 'win32':
        return ctypes.cdll.LoadLibrary(path)
    else:
        raise TypeError("Platform not supported!")


def get_char_type():
    if sys.platform == 'win32':
        return c_wchar_p
    else:
        return c_char_p


def get_ctype_string_buffer(size):
    if sys.platform == 'win32':
        return ctypes.create_unicode_buffer(size)
    else:
        return ctypes.create_string_buffer(size)


def get_ctype_string(input):
    if sys.platform == 'win32':
        return ctypes.c_wchar_p(input)
    else:
        return ctypes.c_char_p(input)


library = load_library(get_library_path())

# define types
CSTRTYPE = get_char_type()
STRTYPE = get_char_type()

CallbackType = CFUNCTYPE(UNCHECKED(None), c_uint32)


SetProductFile = library.SetProductFile
SetProductFile.argtypes = [CSTRTYPE]
SetProductFile.restype = c_int

SetProductData = library.SetProductData
SetProductData.argtypes = [CSTRTYPE]
SetProductData.restype = c_int

SetProductId = library.SetProductId
SetProductId.argtypes = [CSTRTYPE, c_uint32]
SetProductId.restype = c_int

SetLicenseKey = library.SetLicenseKey
SetLicenseKey.argtypes = [CSTRTYPE]
SetLicenseKey.restype = c_int

SetLicenseUserCredential = library.SetLicenseUserCredential
SetLicenseUserCredential.argtypes = [CSTRTYPE, CSTRTYPE]
SetLicenseUserCredential.restype = c_int

SetLicenseCallback = library.SetLicenseCallback
SetLicenseCallback.argtypes = [CallbackType]
SetLicenseCallback.restype = c_int

SetActivationMetadata = library.SetActivationMetadata
SetActivationMetadata.argtypes = [CSTRTYPE, CSTRTYPE]
SetActivationMetadata.restype = c_int

SetTrialActivationMetadata = library.SetTrialActivationMetadata
SetTrialActivationMetadata.argtypes = [CSTRTYPE, CSTRTYPE]
SetTrialActivationMetadata.restype = c_int

SetAppVersion = library.SetAppVersion
SetAppVersion.argtypes = [CSTRTYPE]
SetAppVersion.restype = c_int

SetNetworkProxy = library.SetNetworkProxy
SetNetworkProxy.argtypes = [CSTRTYPE]
SetNetworkProxy.restype = c_int

SetCryptlexHost = library.SetCryptlexHost
SetCryptlexHost.argtypes = [CSTRTYPE]
SetCryptlexHost.restype = c_int

GetProductMetadata = library.GetProductMetadata
GetProductMetadata.argtypes = [CSTRTYPE, STRTYPE, c_uint32]
GetProductMetadata.restype = c_int

GetLicenseMetadata = library.GetLicenseMetadata
GetLicenseMetadata.argtypes = [CSTRTYPE, STRTYPE, c_uint32]
GetLicenseMetadata.restype = c_int

GetLicenseMeterAttribute = library.GetLicenseMeterAttribute
GetLicenseMeterAttribute.argtypes = [
    CSTRTYPE, POINTER(c_uint32), POINTER(c_uint32)]
GetLicenseMeterAttribute.restype = c_int

GetLicenseKey = library.GetLicenseKey
GetLicenseKey.argtypes = [STRTYPE, c_uint32]
GetLicenseKey.restype = c_int

GetLicenseExpiryDate = library.GetLicenseExpiryDate
GetLicenseExpiryDate.argtypes = [POINTER(c_uint32)]
GetLicenseExpiryDate.restype = c_int

GetLicenseUserEmail = library.GetLicenseUserEmail
GetLicenseUserEmail.argtypes = [STRTYPE, c_uint32]
GetLicenseUserEmail.restype = c_int

GetLicenseUserName = library.GetLicenseUserName
GetLicenseUserName.argtypes = [STRTYPE, c_uint32]
GetLicenseUserName.restype = c_int

GetLicenseUserCompany = library.GetLicenseUserCompany
GetLicenseUserCompany.argtypes = [STRTYPE, c_uint32]
GetLicenseUserCompany.restype = c_int

GetLicenseUserMetadata = library.GetLicenseUserMetadata
GetLicenseUserMetadata.argtypes = [CSTRTYPE, STRTYPE, c_uint32]
GetLicenseUserMetadata.restype = c_int

GetLicenseType = library.GetLicenseType
GetLicenseType.argtypes = [STRTYPE, c_uint32]
GetLicenseType.restype = c_int

GetActivationMetadata = library.GetActivationMetadata
GetActivationMetadata.argtypes = [CSTRTYPE, STRTYPE, c_uint32]
GetActivationMetadata.restype = c_int

GetActivationMeterAttributeUses = library.GetActivationMeterAttributeUses
GetActivationMeterAttributeUses.argtypes = [CSTRTYPE, POINTER(c_uint32)]
GetActivationMeterAttributeUses.restype = c_int

GetServerSyncGracePeriodExpiryDate = library.GetServerSyncGracePeriodExpiryDate
GetServerSyncGracePeriodExpiryDate.argtypes = [POINTER(c_uint32)]
GetServerSyncGracePeriodExpiryDate.restype = c_int

GetTrialActivationMetadata = library.GetTrialActivationMetadata
GetTrialActivationMetadata.argtypes = [CSTRTYPE, STRTYPE, c_uint32]
GetTrialActivationMetadata.restype = c_int

GetTrialExpiryDate = library.GetTrialExpiryDate
GetTrialExpiryDate.argtypes = [POINTER(c_uint32)]
GetTrialExpiryDate.restype = c_int

GetTrialId = library.GetTrialId
GetTrialId.argtypes = [STRTYPE, c_uint32]
GetTrialId.restype = c_int

GetLocalTrialExpiryDate = library.GetLocalTrialExpiryDate
GetLocalTrialExpiryDate.argtypes = [POINTER(c_uint32)]
GetLocalTrialExpiryDate.restype = c_int

CheckForReleaseUpdate = library.CheckForReleaseUpdate
CheckForReleaseUpdate.argtypes = [CSTRTYPE, CSTRTYPE, CSTRTYPE, CallbackType]
CheckForReleaseUpdate.restype = c_int

ActivateLicense = library.ActivateLicense
ActivateLicense.argtypes = []
ActivateLicense.restype = c_int

ActivateLicenseOffline = library.ActivateLicenseOffline
ActivateLicenseOffline.argtypes = [CSTRTYPE]
ActivateLicenseOffline.restype = c_int

GenerateOfflineActivationRequest = library.GenerateOfflineActivationRequest
GenerateOfflineActivationRequest.argtypes = [CSTRTYPE]
GenerateOfflineActivationRequest.restype = c_int

DeactivateLicense = library.DeactivateLicense
DeactivateLicense.argtypes = []
DeactivateLicense.restype = c_int

GenerateOfflineDeactivationRequest = library.GenerateOfflineDeactivationRequest
GenerateOfflineDeactivationRequest.argtypes = [CSTRTYPE]
GenerateOfflineDeactivationRequest.restype = c_int

IsLicenseGenuine = library.IsLicenseGenuine
IsLicenseGenuine.argtypes = []
IsLicenseGenuine.restype = c_int

IsLicenseValid = library.IsLicenseValid
IsLicenseValid.argtypes = []
IsLicenseValid.restype = c_int

ActivateTrial = library.ActivateTrial
ActivateTrial.argtypes = []
ActivateTrial.restype = c_int

ActivateTrialOffline = library.ActivateTrialOffline
ActivateTrialOffline.argtypes = [CSTRTYPE]
ActivateTrialOffline.restype = c_int

GenerateOfflineTrialActivationRequest = library.GenerateOfflineTrialActivationRequest
GenerateOfflineTrialActivationRequest.argtypes = [CSTRTYPE]
GenerateOfflineTrialActivationRequest.restype = c_int

IsTrialGenuine = library.IsTrialGenuine
IsTrialGenuine.argtypes = []
IsTrialGenuine.restype = c_int

ActivateLocalTrial = library.ActivateLocalTrial
ActivateLocalTrial.argtypes = [c_uint32]
ActivateLocalTrial.restype = c_int

IsLocalTrialGenuine = library.IsLocalTrialGenuine
IsLocalTrialGenuine.argtypes = []
IsLocalTrialGenuine.restype = c_int

ExtendLocalTrial = library.ExtendLocalTrial
ExtendLocalTrial.argtypes = [c_uint32]
ExtendLocalTrial.restype = c_int

IncrementActivationMeterAttributeUses = library.IncrementActivationMeterAttributeUses
IncrementActivationMeterAttributeUses.argtypes = [CSTRTYPE, c_uint32]
IncrementActivationMeterAttributeUses.restype = c_int

DecrementActivationMeterAttributeUses = library.DecrementActivationMeterAttributeUses
DecrementActivationMeterAttributeUses.argtypes = [CSTRTYPE, c_uint32]
DecrementActivationMeterAttributeUses.restype = c_int

ResetActivationMeterAttributeUses = library.ResetActivationMeterAttributeUses
ResetActivationMeterAttributeUses.argtypes = [CSTRTYPE]
ResetActivationMeterAttributeUses.restype = c_int

Reset = library.Reset
Reset.argtypes = []
Reset.restype = c_int
