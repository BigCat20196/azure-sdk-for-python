# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
from msrest import Serializer, Deserializer
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest


class SearchClientOperationsMixin(object):

    async def get_service_statistics(
        self,
        request_options: Optional["_models.RequestOptions"] = None,
        **kwargs
    ) -> "_models.ServiceStatistics":
        """Gets service level statistics for a search service.

        :param request_options: Parameter group.
        :type request_options: ~azure.search.documents.indexes.v2020_06_preview.models.RequestOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ServiceStatistics, or the result of cls(response)
        :rtype: ~azure.search.documents.indexes.v2020_06_preview.models.ServiceStatistics
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = self._get_api_version('get_service_statistics')
        if api_version == '2020-06-30':
            from ..v2020_06.aio.operations import SearchClientOperationsMixin as OperationClass
        elif api_version == '2020-06-30-Preview':
            from ..v2020_06_preview.aio.operations import SearchClientOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'get_service_statistics'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._serialize.client_side_validation = False
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return await mixin_instance.get_service_statistics(request_options, **kwargs)