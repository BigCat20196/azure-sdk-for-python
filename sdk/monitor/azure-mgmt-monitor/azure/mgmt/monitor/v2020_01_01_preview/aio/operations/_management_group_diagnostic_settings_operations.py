# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Optional, TypeVar

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._management_group_diagnostic_settings_operations import build_create_or_update_request, build_delete_request, build_get_request, build_list_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class ManagementGroupDiagnosticSettingsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~$(python-base-namespace).v2020_01_01_preview.aio.MonitorManagementClient`'s
        :attr:`management_group_diagnostic_settings` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")


    @distributed_trace_async
    async def get(
        self,
        management_group_id: str,
        name: str,
        **kwargs: Any
    ) -> _models.ManagementGroupDiagnosticSettingsResource:
        """Gets the active management group diagnostic settings for the specified resource.

        :param management_group_id: The management group id.
        :type management_group_id: str
        :param name: The name of the diagnostic setting.
        :type name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ManagementGroupDiagnosticSettingsResource, or the result of cls(response)
        :rtype:
         ~$(python-base-namespace).v2020_01_01_preview.models.ManagementGroupDiagnosticSettingsResource
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2020-01-01-preview"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.ManagementGroupDiagnosticSettingsResource]

        
        request = build_get_request(
            management_group_id=management_group_id,
            name=name,
            api_version=api_version,
            template_url=self.get.metadata['url'],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ManagementGroupDiagnosticSettingsResource', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': "/providers/microsoft.management/managementGroups/{managementGroupId}/providers/microsoft.insights/diagnosticSettings/{name}"}  # type: ignore


    @distributed_trace_async
    async def create_or_update(
        self,
        management_group_id: str,
        name: str,
        parameters: _models.ManagementGroupDiagnosticSettingsResource,
        **kwargs: Any
    ) -> _models.ManagementGroupDiagnosticSettingsResource:
        """Creates or updates management group diagnostic settings for the specified resource.

        :param management_group_id: The management group id.
        :type management_group_id: str
        :param name: The name of the diagnostic setting.
        :type name: str
        :param parameters: Parameters supplied to the operation.
        :type parameters:
         ~$(python-base-namespace).v2020_01_01_preview.models.ManagementGroupDiagnosticSettingsResource
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ManagementGroupDiagnosticSettingsResource, or the result of cls(response)
        :rtype:
         ~$(python-base-namespace).v2020_01_01_preview.models.ManagementGroupDiagnosticSettingsResource
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2020-01-01-preview"))  # type: str
        content_type = kwargs.pop('content_type', _headers.pop('Content-Type', "application/json"))  # type: Optional[str]
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.ManagementGroupDiagnosticSettingsResource]

        _json = self._serialize.body(parameters, 'ManagementGroupDiagnosticSettingsResource')

        request = build_create_or_update_request(
            management_group_id=management_group_id,
            name=name,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self.create_or_update.metadata['url'],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ManagementGroupDiagnosticSettingsResource', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_or_update.metadata = {'url': "/providers/microsoft.management/managementGroups/{managementGroupId}/providers/microsoft.insights/diagnosticSettings/{name}"}  # type: ignore


    @distributed_trace_async
    async def delete(  # pylint: disable=inconsistent-return-statements
        self,
        management_group_id: str,
        name: str,
        **kwargs: Any
    ) -> None:
        """Deletes existing management group diagnostic settings for the specified resource.

        :param management_group_id: The management group id.
        :type management_group_id: str
        :param name: The name of the diagnostic setting.
        :type name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2020-01-01-preview"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[None]

        
        request = build_delete_request(
            management_group_id=management_group_id,
            name=name,
            api_version=api_version,
            template_url=self.delete.metadata['url'],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {'url': "/providers/microsoft.management/managementGroups/{managementGroupId}/providers/microsoft.insights/diagnosticSettings/{name}"}  # type: ignore


    @distributed_trace
    def list(
        self,
        management_group_id: str,
        **kwargs: Any
    ) -> AsyncIterable[_models.ManagementGroupDiagnosticSettingsResourceCollection]:
        """Gets the active management group diagnostic settings list for the specified management group.

        :param management_group_id: The management group id.
        :type management_group_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either
         ManagementGroupDiagnosticSettingsResourceCollection or the result of cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~$(python-base-namespace).v2020_01_01_preview.models.ManagementGroupDiagnosticSettingsResourceCollection]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2020-01-01-preview"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.ManagementGroupDiagnosticSettingsResourceCollection]

        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_request(
                    management_group_id=management_group_id,
                    api_version=api_version,
                    template_url=self.list.metadata['url'],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                
                request = build_list_request(
                    management_group_id=management_group_id,
                    api_version=api_version,
                    template_url=next_link,
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("ManagementGroupDiagnosticSettingsResourceCollection", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': "/providers/microsoft.management/managementGroups/{managementGroupId}/providers/microsoft.insights/diagnosticSettings"}  # type: ignore
