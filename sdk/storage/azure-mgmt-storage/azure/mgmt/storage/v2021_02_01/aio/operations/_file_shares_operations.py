# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, AsyncIterable, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._file_shares_operations import build_create_request, build_delete_request, build_get_request, build_list_request, build_restore_request, build_update_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class FileSharesOperations:
    """FileSharesOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.storage.v2021_02_01.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def list(
        self,
        resource_group_name: str,
        account_name: str,
        maxpagesize: Optional[str] = None,
        filter: Optional[str] = None,
        expand: Optional[Union[str, "_models.ListSharesExpand"]] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.FileShareItems"]:
        """Lists all shares.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only.
        :type account_name: str
        :param maxpagesize: Optional. Specified maximum number of shares that can be included in the
         list.
        :type maxpagesize: str
        :param filter: Optional. When specified, only share names starting with the filter will be
         listed.
        :type filter: str
        :param expand: Optional, used to expand the properties within share's properties.
        :type expand: str or ~azure.mgmt.storage.v2021_02_01.models.ListSharesExpand
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either FileShareItems or the result of cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.storage.v2021_02_01.models.FileShareItems]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.FileShareItems"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_request(
                    resource_group_name=resource_group_name,
                    account_name=account_name,
                    subscription_id=self._config.subscription_id,
                    maxpagesize=maxpagesize,
                    filter=filter,
                    expand=expand,
                    template_url=self.list.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_request(
                    resource_group_name=resource_group_name,
                    account_name=account_name,
                    subscription_id=self._config.subscription_id,
                    maxpagesize=maxpagesize,
                    filter=filter,
                    expand=expand,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("FileShareItems", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/fileServices/default/shares'}  # type: ignore

    @distributed_trace_async
    async def create(
        self,
        resource_group_name: str,
        account_name: str,
        share_name: str,
        file_share: "_models.FileShare",
        expand: Optional[Union[str, "_models.PutSharesExpand"]] = None,
        **kwargs: Any
    ) -> "_models.FileShare":
        """Creates a new share under the specified account as described by request body. The share
        resource includes metadata and properties for that share. It does not include a list of the
        files contained by the share.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only.
        :type account_name: str
        :param share_name: The name of the file share within the specified storage account. File share
         names must be between 3 and 63 characters in length and use numbers, lower-case letters and
         dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter
         or number.
        :type share_name: str
        :param file_share: Properties of the file share to create.
        :type file_share: ~azure.mgmt.storage.v2021_02_01.models.FileShare
        :param expand: Optional, used to create a snapshot.
        :type expand: str or ~azure.mgmt.storage.v2021_02_01.models.PutSharesExpand
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: FileShare, or the result of cls(response)
        :rtype: ~azure.mgmt.storage.v2021_02_01.models.FileShare
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.FileShare"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(file_share, 'FileShare')

        request = build_create_request(
            resource_group_name=resource_group_name,
            account_name=account_name,
            share_name=share_name,
            subscription_id=self._config.subscription_id,
            content_type=content_type,
            json=_json,
            expand=expand,
            template_url=self.create.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize('FileShare', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('FileShare', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/fileServices/default/shares/{shareName}'}  # type: ignore


    @distributed_trace_async
    async def update(
        self,
        resource_group_name: str,
        account_name: str,
        share_name: str,
        file_share: "_models.FileShare",
        **kwargs: Any
    ) -> "_models.FileShare":
        """Updates share properties as specified in request body. Properties not mentioned in the request
        will not be changed. Update fails if the specified share does not already exist.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only.
        :type account_name: str
        :param share_name: The name of the file share within the specified storage account. File share
         names must be between 3 and 63 characters in length and use numbers, lower-case letters and
         dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter
         or number.
        :type share_name: str
        :param file_share: Properties to update for the file share.
        :type file_share: ~azure.mgmt.storage.v2021_02_01.models.FileShare
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: FileShare, or the result of cls(response)
        :rtype: ~azure.mgmt.storage.v2021_02_01.models.FileShare
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.FileShare"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(file_share, 'FileShare')

        request = build_update_request(
            resource_group_name=resource_group_name,
            account_name=account_name,
            share_name=share_name,
            subscription_id=self._config.subscription_id,
            content_type=content_type,
            json=_json,
            template_url=self.update.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('FileShare', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/fileServices/default/shares/{shareName}'}  # type: ignore


    @distributed_trace_async
    async def get(
        self,
        resource_group_name: str,
        account_name: str,
        share_name: str,
        expand: Optional[str] = "stats",
        x_ms_snapshot: Optional[str] = None,
        **kwargs: Any
    ) -> "_models.FileShare":
        """Gets properties of a specified share.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only.
        :type account_name: str
        :param share_name: The name of the file share within the specified storage account. File share
         names must be between 3 and 63 characters in length and use numbers, lower-case letters and
         dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter
         or number.
        :type share_name: str
        :param expand: Optional, used to expand the properties within share's properties. The default
         value is "stats".
        :type expand: str
        :param x_ms_snapshot: Optional, used to retrieve properties of a snapshot.
        :type x_ms_snapshot: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: FileShare, or the result of cls(response)
        :rtype: ~azure.mgmt.storage.v2021_02_01.models.FileShare
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.FileShare"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_request(
            resource_group_name=resource_group_name,
            account_name=account_name,
            share_name=share_name,
            subscription_id=self._config.subscription_id,
            expand=expand,
            x_ms_snapshot=x_ms_snapshot,
            template_url=self.get.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('FileShare', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/fileServices/default/shares/{shareName}'}  # type: ignore


    @distributed_trace_async
    async def delete(
        self,
        resource_group_name: str,
        account_name: str,
        share_name: str,
        x_ms_snapshot: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """Deletes specified share under its account.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only.
        :type account_name: str
        :param share_name: The name of the file share within the specified storage account. File share
         names must be between 3 and 63 characters in length and use numbers, lower-case letters and
         dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter
         or number.
        :type share_name: str
        :param x_ms_snapshot: Optional, used to delete a snapshot.
        :type x_ms_snapshot: str
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

        
        request = build_delete_request(
            resource_group_name=resource_group_name,
            account_name=account_name,
            share_name=share_name,
            subscription_id=self._config.subscription_id,
            x_ms_snapshot=x_ms_snapshot,
            template_url=self.delete.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/fileServices/default/shares/{shareName}'}  # type: ignore


    @distributed_trace_async
    async def restore(
        self,
        resource_group_name: str,
        account_name: str,
        share_name: str,
        deleted_share: "_models.DeletedShare",
        **kwargs: Any
    ) -> None:
        """Restore a file share within a valid retention days if share soft delete is enabled.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only.
        :type account_name: str
        :param share_name: The name of the file share within the specified storage account. File share
         names must be between 3 and 63 characters in length and use numbers, lower-case letters and
         dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter
         or number.
        :type share_name: str
        :param deleted_share:
        :type deleted_share: ~azure.mgmt.storage.v2021_02_01.models.DeletedShare
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

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(deleted_share, 'DeletedShare')

        request = build_restore_request(
            resource_group_name=resource_group_name,
            account_name=account_name,
            share_name=share_name,
            subscription_id=self._config.subscription_id,
            content_type=content_type,
            json=_json,
            template_url=self.restore.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    restore.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/fileServices/default/shares/{shareName}/restore'}  # type: ignore

