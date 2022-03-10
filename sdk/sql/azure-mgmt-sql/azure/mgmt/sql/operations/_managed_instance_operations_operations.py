# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, Iterable, Optional, TypeVar
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.mgmt.core.exceptions import ARMErrorFormat
from msrest import Serializer

from .. import models as _models
from .._vendor import _convert_request, _format_url_section
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

def build_list_by_managed_instance_request(
    resource_group_name: str,
    managed_instance_name: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2020-11-01-preview"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/operations')
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "managedInstanceName": _SERIALIZER.url("managed_instance_name", managed_instance_name, 'str'),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
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


def build_get_request(
    resource_group_name: str,
    managed_instance_name: str,
    operation_id: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2020-11-01-preview"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/operations/{operationId}')
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "managedInstanceName": _SERIALIZER.url("managed_instance_name", managed_instance_name, 'str'),
        "operationId": _SERIALIZER.url("operation_id", operation_id, 'str'),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
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


def build_cancel_request(
    resource_group_name: str,
    managed_instance_name: str,
    operation_id: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2020-11-01-preview"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/operations/{operationId}/cancel')
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "managedInstanceName": _SERIALIZER.url("managed_instance_name", managed_instance_name, 'str'),
        "operationId": _SERIALIZER.url("operation_id", operation_id, 'str'),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    return HttpRequest(
        method="POST",
        url=url,
        params=query_parameters,
        **kwargs
    )

class ManagedInstanceOperationsOperations(object):
    """ManagedInstanceOperationsOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.sql.models
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
    def list_by_managed_instance(
        self,
        resource_group_name: str,
        managed_instance_name: str,
        **kwargs: Any
    ) -> Iterable["_models.ManagedInstanceOperationListResult"]:
        """Gets a list of operations performed on the managed instance.

        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal.
        :type resource_group_name: str
        :param managed_instance_name: The name of the managed instance.
        :type managed_instance_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either ManagedInstanceOperationListResult or the result
         of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.sql.models.ManagedInstanceOperationListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ManagedInstanceOperationListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_by_managed_instance_request(
                    resource_group_name=resource_group_name,
                    managed_instance_name=managed_instance_name,
                    subscription_id=self._config.subscription_id,
                    template_url=self.list_by_managed_instance.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_by_managed_instance_request(
                    resource_group_name=resource_group_name,
                    managed_instance_name=managed_instance_name,
                    subscription_id=self._config.subscription_id,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("ManagedInstanceOperationListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response


        return ItemPaged(
            get_next, extract_data
        )
    list_by_managed_instance.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/operations'}  # type: ignore

    @distributed_trace
    def get(
        self,
        resource_group_name: str,
        managed_instance_name: str,
        operation_id: str,
        **kwargs: Any
    ) -> "_models.ManagedInstanceOperation":
        """Gets a management operation on a managed instance.

        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal.
        :type resource_group_name: str
        :param managed_instance_name: The name of the managed instance.
        :type managed_instance_name: str
        :param operation_id:
        :type operation_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ManagedInstanceOperation, or the result of cls(response)
        :rtype: ~azure.mgmt.sql.models.ManagedInstanceOperation
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ManagedInstanceOperation"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_request(
            resource_group_name=resource_group_name,
            managed_instance_name=managed_instance_name,
            operation_id=operation_id,
            subscription_id=self._config.subscription_id,
            template_url=self.get.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ManagedInstanceOperation', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/operations/{operationId}'}  # type: ignore


    @distributed_trace
    def cancel(
        self,
        resource_group_name: str,
        managed_instance_name: str,
        operation_id: str,
        **kwargs: Any
    ) -> None:
        """Cancels the asynchronous operation on the managed instance.

        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal.
        :type resource_group_name: str
        :param managed_instance_name: The name of the managed instance.
        :type managed_instance_name: str
        :param operation_id:
        :type operation_id: str
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

        
        request = build_cancel_request(
            resource_group_name=resource_group_name,
            managed_instance_name=managed_instance_name,
            operation_id=operation_id,
            subscription_id=self._config.subscription_id,
            template_url=self.cancel.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    cancel.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/operations/{operationId}/cancel'}  # type: ignore

