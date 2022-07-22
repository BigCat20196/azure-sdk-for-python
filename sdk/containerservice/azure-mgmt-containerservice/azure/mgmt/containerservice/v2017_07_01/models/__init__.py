# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import ContainerService
from ._models_py3 import ContainerServiceAgentPoolProfile
from ._models_py3 import ContainerServiceCustomProfile
from ._models_py3 import ContainerServiceDiagnosticsProfile
from ._models_py3 import ContainerServiceLinuxProfile
from ._models_py3 import ContainerServiceListResult
from ._models_py3 import ContainerServiceMasterProfile
from ._models_py3 import ContainerServiceOrchestratorProfile
from ._models_py3 import ContainerServicePrincipalProfile
from ._models_py3 import ContainerServiceSshConfiguration
from ._models_py3 import ContainerServiceSshPublicKey
from ._models_py3 import ContainerServiceVMDiagnostics
from ._models_py3 import ContainerServiceWindowsProfile
from ._models_py3 import KeyVaultSecretRef
from ._models_py3 import OrchestratorProfile
from ._models_py3 import OrchestratorVersionProfile
from ._models_py3 import OrchestratorVersionProfileListResult
from ._models_py3 import Resource


from ._container_service_client_enums import (
    ContainerServiceOrchestratorTypes,
    ContainerServiceStorageProfileTypes,
    ContainerServiceVMSizeTypes,
    Count,
    OSType,
)
from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk
__all__ = [
    'ContainerService',
    'ContainerServiceAgentPoolProfile',
    'ContainerServiceCustomProfile',
    'ContainerServiceDiagnosticsProfile',
    'ContainerServiceLinuxProfile',
    'ContainerServiceListResult',
    'ContainerServiceMasterProfile',
    'ContainerServiceOrchestratorProfile',
    'ContainerServicePrincipalProfile',
    'ContainerServiceSshConfiguration',
    'ContainerServiceSshPublicKey',
    'ContainerServiceVMDiagnostics',
    'ContainerServiceWindowsProfile',
    'KeyVaultSecretRef',
    'OrchestratorProfile',
    'OrchestratorVersionProfile',
    'OrchestratorVersionProfileListResult',
    'Resource',
    'ContainerServiceOrchestratorTypes',
    'ContainerServiceStorageProfileTypes',
    'ContainerServiceVMSizeTypes',
    'Count',
    'OSType',
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()