# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.mgmt.core.exceptions import ARMErrorFormat
from msrest import Serializer

from .. import models as _models
from .._vendor import _convert_request, _format_url_section

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Optional, TypeVar
    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False
# fmt: off

def build_get_request(
    vault_name,  # type: str
    resource_group_name,  # type: str
    subscription_id,  # type: str
    fabric_name,  # type: str
    container_name,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = "2021-10-01"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}')
    path_format_arguments = {
        "vaultName": _SERIALIZER.url("vault_name", vault_name, 'str'),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "fabricName": _SERIALIZER.url("fabric_name", fabric_name, 'str'),
        "containerName": _SERIALIZER.url("container_name", container_name, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_register_request(
    vault_name,  # type: str
    resource_group_name,  # type: str
    subscription_id,  # type: str
    fabric_name,  # type: str
    container_name,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    api_version = "2021-10-01"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}')
    path_format_arguments = {
        "vaultName": _SERIALIZER.url("vault_name", vault_name, 'str'),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "fabricName": _SERIALIZER.url("fabric_name", fabric_name, 'str'),
        "containerName": _SERIALIZER.url("container_name", container_name, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_unregister_request(
    vault_name,  # type: str
    resource_group_name,  # type: str
    subscription_id,  # type: str
    fabric_name,  # type: str
    container_name,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = "2021-10-01"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}')
    path_format_arguments = {
        "vaultName": _SERIALIZER.url("vault_name", vault_name, 'str'),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "fabricName": _SERIALIZER.url("fabric_name", fabric_name, 'str'),
        "containerName": _SERIALIZER.url("container_name", container_name, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="DELETE",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_inquire_request(
    vault_name,  # type: str
    resource_group_name,  # type: str
    subscription_id,  # type: str
    fabric_name,  # type: str
    container_name,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    filter = kwargs.pop('filter', None)  # type: Optional[str]

    api_version = "2021-10-01"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}/inquire')
    path_format_arguments = {
        "vaultName": _SERIALIZER.url("vault_name", vault_name, 'str'),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "fabricName": _SERIALIZER.url("fabric_name", fabric_name, 'str'),
        "containerName": _SERIALIZER.url("container_name", container_name, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')
    if filter is not None:
        query_parameters['$filter'] = _SERIALIZER.query("filter", filter, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_refresh_request(
    vault_name,  # type: str
    resource_group_name,  # type: str
    subscription_id,  # type: str
    fabric_name,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    filter = kwargs.pop('filter', None)  # type: Optional[str]

    api_version = "2021-10-01"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/refreshContainers')
    path_format_arguments = {
        "vaultName": _SERIALIZER.url("vault_name", vault_name, 'str'),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "fabricName": _SERIALIZER.url("fabric_name", fabric_name, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')
    if filter is not None:
        query_parameters['$filter'] = _SERIALIZER.query("filter", filter, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )

# fmt: on
class ProtectionContainersOperations(object):
    """ProtectionContainersOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.recoveryservicesbackup.activestamp.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def get(
        self,
        vault_name,  # type: str
        resource_group_name,  # type: str
        fabric_name,  # type: str
        container_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.ProtectionContainerResource"
        """Gets details of the specific container registered to your Recovery Services Vault.

        :param vault_name: The name of the recovery services vault.
        :type vault_name: str
        :param resource_group_name: The name of the resource group where the recovery services vault is
         present.
        :type resource_group_name: str
        :param fabric_name: Name of the fabric where the container belongs.
        :type fabric_name: str
        :param container_name: Name of the container whose details need to be fetched.
        :type container_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ProtectionContainerResource, or the result of cls(response)
        :rtype: ~azure.mgmt.recoveryservicesbackup.activestamp.models.ProtectionContainerResource
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ProtectionContainerResource"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_request(
            vault_name=vault_name,
            resource_group_name=resource_group_name,
            subscription_id=self._config.subscription_id,
            fabric_name=fabric_name,
            container_name=container_name,
            template_url=self.get.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ProtectionContainerResource', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}'}  # type: ignore


    @distributed_trace
    def register(
        self,
        vault_name,  # type: str
        resource_group_name,  # type: str
        fabric_name,  # type: str
        container_name,  # type: str
        parameters,  # type: "_models.ProtectionContainerResource"
        **kwargs  # type: Any
    ):
        # type: (...) -> Optional["_models.ProtectionContainerResource"]
        """Registers the container with Recovery Services vault.
        This is an asynchronous operation. To track the operation status, use location header to call
        get latest status of
        the operation.

        :param vault_name: The name of the recovery services vault.
        :type vault_name: str
        :param resource_group_name: The name of the resource group where the recovery services vault is
         present.
        :type resource_group_name: str
        :param fabric_name: Fabric name associated with the container.
        :type fabric_name: str
        :param container_name: Name of the container to be registered.
        :type container_name: str
        :param parameters: Request body for operation.
        :type parameters:
         ~azure.mgmt.recoveryservicesbackup.activestamp.models.ProtectionContainerResource
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ProtectionContainerResource, or the result of cls(response)
        :rtype: ~azure.mgmt.recoveryservicesbackup.activestamp.models.ProtectionContainerResource or
         None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[Optional["_models.ProtectionContainerResource"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(parameters, 'ProtectionContainerResource')

        request = build_register_request(
            vault_name=vault_name,
            resource_group_name=resource_group_name,
            subscription_id=self._config.subscription_id,
            fabric_name=fabric_name,
            container_name=container_name,
            content_type=content_type,
            json=_json,
            template_url=self.register.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('ProtectionContainerResource', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    register.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}'}  # type: ignore


    @distributed_trace
    def unregister(
        self,
        vault_name,  # type: str
        resource_group_name,  # type: str
        fabric_name,  # type: str
        container_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Unregisters the given container from your Recovery Services Vault. This is an asynchronous
        operation. To determine
        whether the backend service has finished processing the request, call Get Container Operation
        Result API.

        :param vault_name: The name of the recovery services vault.
        :type vault_name: str
        :param resource_group_name: The name of the resource group where the recovery services vault is
         present.
        :type resource_group_name: str
        :param fabric_name: Name of the fabric where the container belongs.
        :type fabric_name: str
        :param container_name: Name of the container which needs to be unregistered from the Recovery
         Services Vault.
        :type container_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_unregister_request(
            vault_name=vault_name,
            resource_group_name=resource_group_name,
            subscription_id=self._config.subscription_id,
            fabric_name=fabric_name,
            container_name=container_name,
            template_url=self.unregister.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    unregister.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}'}  # type: ignore


    @distributed_trace
    def inquire(
        self,
        vault_name,  # type: str
        resource_group_name,  # type: str
        fabric_name,  # type: str
        container_name,  # type: str
        filter=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Inquires all the protectable items under the given container.

        This is an async operation and the results should be tracked using location header or
        Azure-async-url.

        :param vault_name: The name of the recovery services vault.
        :type vault_name: str
        :param resource_group_name: The name of the resource group where the recovery services vault is
         present.
        :type resource_group_name: str
        :param fabric_name: Fabric Name associated with the container.
        :type fabric_name: str
        :param container_name: Name of the container in which inquiry needs to be triggered.
        :type container_name: str
        :param filter: OData filter options.
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_inquire_request(
            vault_name=vault_name,
            resource_group_name=resource_group_name,
            subscription_id=self._config.subscription_id,
            fabric_name=fabric_name,
            container_name=container_name,
            filter=filter,
            template_url=self.inquire.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    inquire.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}/inquire'}  # type: ignore


    @distributed_trace
    def refresh(
        self,
        vault_name,  # type: str
        resource_group_name,  # type: str
        fabric_name,  # type: str
        filter=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Discovers all the containers in the subscription that can be backed up to Recovery Services
        Vault. This is an
        asynchronous operation. To know the status of the operation, call GetRefreshOperationResult
        API.

        :param vault_name: The name of the recovery services vault.
        :type vault_name: str
        :param resource_group_name: The name of the resource group where the recovery services vault is
         present.
        :type resource_group_name: str
        :param fabric_name: Fabric name associated the container.
        :type fabric_name: str
        :param filter: OData filter options.
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_refresh_request(
            vault_name=vault_name,
            resource_group_name=resource_group_name,
            subscription_id=self._config.subscription_id,
            fabric_name=fabric_name,
            filter=filter,
            template_url=self.refresh.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    refresh.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/refreshContainers'}  # type: ignore

