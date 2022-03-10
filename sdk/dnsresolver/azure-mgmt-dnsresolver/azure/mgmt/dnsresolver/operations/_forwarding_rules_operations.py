# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, Iterable, Optional, TypeVar, Union
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
JSONType = Any
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

def build_create_or_update_request(
    subscription_id: str,
    resource_group_name: str,
    dns_forwarding_ruleset_name: str,
    forwarding_rule_name: str,
    *,
    json: JSONType = None,
    content: Any = None,
    if_match: Optional[str] = None,
    if_none_match: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    api_version = "2020-04-01-preview"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsForwardingRulesets/{dnsForwardingRulesetName}/forwardingRules/{forwardingRuleName}')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str', min_length=1),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
        "dnsForwardingRulesetName": _SERIALIZER.url("dns_forwarding_ruleset_name", dns_forwarding_ruleset_name, 'str'),
        "forwardingRuleName": _SERIALIZER.url("forwarding_rule_name", forwarding_rule_name, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if if_match is not None:
        header_parameters['If-Match'] = _SERIALIZER.header("if_match", if_match, 'str')
    if if_none_match is not None:
        header_parameters['If-None-Match'] = _SERIALIZER.header("if_none_match", if_none_match, 'str')
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        json=json,
        content=content,
        **kwargs
    )


def build_update_request(
    subscription_id: str,
    resource_group_name: str,
    dns_forwarding_ruleset_name: str,
    forwarding_rule_name: str,
    *,
    json: JSONType = None,
    content: Any = None,
    if_match: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    api_version = "2020-04-01-preview"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsForwardingRulesets/{dnsForwardingRulesetName}/forwardingRules/{forwardingRuleName}')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str', min_length=1),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
        "dnsForwardingRulesetName": _SERIALIZER.url("dns_forwarding_ruleset_name", dns_forwarding_ruleset_name, 'str'),
        "forwardingRuleName": _SERIALIZER.url("forwarding_rule_name", forwarding_rule_name, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if if_match is not None:
        header_parameters['If-Match'] = _SERIALIZER.header("if_match", if_match, 'str')
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PATCH",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        json=json,
        content=content,
        **kwargs
    )


def build_delete_request(
    subscription_id: str,
    resource_group_name: str,
    dns_forwarding_ruleset_name: str,
    forwarding_rule_name: str,
    *,
    if_match: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2020-04-01-preview"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsForwardingRulesets/{dnsForwardingRulesetName}/forwardingRules/{forwardingRuleName}')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str', min_length=1),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
        "dnsForwardingRulesetName": _SERIALIZER.url("dns_forwarding_ruleset_name", dns_forwarding_ruleset_name, 'str'),
        "forwardingRuleName": _SERIALIZER.url("forwarding_rule_name", forwarding_rule_name, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if if_match is not None:
        header_parameters['If-Match'] = _SERIALIZER.header("if_match", if_match, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="DELETE",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_get_request(
    subscription_id: str,
    resource_group_name: str,
    dns_forwarding_ruleset_name: str,
    forwarding_rule_name: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2020-04-01-preview"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsForwardingRulesets/{dnsForwardingRulesetName}/forwardingRules/{forwardingRuleName}')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str', min_length=1),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
        "dnsForwardingRulesetName": _SERIALIZER.url("dns_forwarding_ruleset_name", dns_forwarding_ruleset_name, 'str'),
        "forwardingRuleName": _SERIALIZER.url("forwarding_rule_name", forwarding_rule_name, 'str'),
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


def build_list_request(
    subscription_id: str,
    resource_group_name: str,
    dns_forwarding_ruleset_name: str,
    *,
    top: Optional[int] = None,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2020-04-01-preview"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsForwardingRulesets/{dnsForwardingRulesetName}/forwardingRules')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str', min_length=1),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
        "dnsForwardingRulesetName": _SERIALIZER.url("dns_forwarding_ruleset_name", dns_forwarding_ruleset_name, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')
    if top is not None:
        query_parameters['$top'] = _SERIALIZER.query("top", top, 'int')

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

class ForwardingRulesOperations(object):
    """ForwardingRulesOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~dns_resolver_management_client.models
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
    def create_or_update(
        self,
        resource_group_name: str,
        dns_forwarding_ruleset_name: str,
        forwarding_rule_name: str,
        parameters: "_models.ForwardingRule",
        if_match: Optional[str] = None,
        if_none_match: Optional[str] = None,
        **kwargs: Any
    ) -> "_models.ForwardingRule":
        """Creates or updates a forwarding rule in a DNS forwarding ruleset.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param dns_forwarding_ruleset_name: The name of the DNS forwarding ruleset.
        :type dns_forwarding_ruleset_name: str
        :param forwarding_rule_name: The name of the forwarding rule.
        :type forwarding_rule_name: str
        :param parameters: Parameters supplied to the CreateOrUpdate operation.
        :type parameters: ~dns_resolver_management_client.models.ForwardingRule
        :param if_match: ETag of the resource. Omit this value to always overwrite the current
         resource. Specify the last-seen ETag value to prevent accidentally overwriting any concurrent
         changes.
        :type if_match: str
        :param if_none_match: Set to '*' to allow a new resource to be created, but to prevent updating
         an existing resource. Other values will be ignored.
        :type if_none_match: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ForwardingRule, or the result of cls(response)
        :rtype: ~dns_resolver_management_client.models.ForwardingRule
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ForwardingRule"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(parameters, 'ForwardingRule')

        request = build_create_or_update_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            dns_forwarding_ruleset_name=dns_forwarding_ruleset_name,
            forwarding_rule_name=forwarding_rule_name,
            content_type=content_type,
            json=_json,
            if_match=if_match,
            if_none_match=if_none_match,
            template_url=self.create_or_update.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize('ForwardingRule', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('ForwardingRule', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsForwardingRulesets/{dnsForwardingRulesetName}/forwardingRules/{forwardingRuleName}'}  # type: ignore


    @distributed_trace
    def update(
        self,
        resource_group_name: str,
        dns_forwarding_ruleset_name: str,
        forwarding_rule_name: str,
        parameters: "_models.ForwardingRulePatch",
        if_match: Optional[str] = None,
        **kwargs: Any
    ) -> "_models.ForwardingRule":
        """Updates a forwarding rule in a DNS forwarding ruleset.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param dns_forwarding_ruleset_name: The name of the DNS forwarding ruleset.
        :type dns_forwarding_ruleset_name: str
        :param forwarding_rule_name: The name of the forwarding rule.
        :type forwarding_rule_name: str
        :param parameters: Parameters supplied to the Update operation.
        :type parameters: ~dns_resolver_management_client.models.ForwardingRulePatch
        :param if_match: ETag of the resource. Omit this value to always overwrite the current
         resource. Specify the last-seen ETag value to prevent accidentally overwriting any concurrent
         changes.
        :type if_match: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ForwardingRule, or the result of cls(response)
        :rtype: ~dns_resolver_management_client.models.ForwardingRule
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ForwardingRule"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(parameters, 'ForwardingRulePatch')

        request = build_update_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            dns_forwarding_ruleset_name=dns_forwarding_ruleset_name,
            forwarding_rule_name=forwarding_rule_name,
            content_type=content_type,
            json=_json,
            if_match=if_match,
            template_url=self.update.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ForwardingRule', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsForwardingRulesets/{dnsForwardingRulesetName}/forwardingRules/{forwardingRuleName}'}  # type: ignore


    @distributed_trace
    def delete(
        self,
        resource_group_name: str,
        dns_forwarding_ruleset_name: str,
        forwarding_rule_name: str,
        if_match: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """Deletes a forwarding rule in a DNS forwarding ruleset. WARNING: This operation cannot be
        undone.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param dns_forwarding_ruleset_name: The name of the DNS forwarding ruleset.
        :type dns_forwarding_ruleset_name: str
        :param forwarding_rule_name: The name of the forwarding rule.
        :type forwarding_rule_name: str
        :param if_match: ETag of the resource. Omit this value to always overwrite the current
         resource. Specify the last-seen ETag value to prevent accidentally overwriting any concurrent
         changes.
        :type if_match: str
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
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            dns_forwarding_ruleset_name=dns_forwarding_ruleset_name,
            forwarding_rule_name=forwarding_rule_name,
            if_match=if_match,
            template_url=self.delete.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsForwardingRulesets/{dnsForwardingRulesetName}/forwardingRules/{forwardingRuleName}'}  # type: ignore


    @distributed_trace
    def get(
        self,
        resource_group_name: str,
        dns_forwarding_ruleset_name: str,
        forwarding_rule_name: str,
        **kwargs: Any
    ) -> "_models.ForwardingRule":
        """Gets properties of a forwarding rule in a DNS forwarding ruleset.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param dns_forwarding_ruleset_name: The name of the DNS forwarding ruleset.
        :type dns_forwarding_ruleset_name: str
        :param forwarding_rule_name: The name of the forwarding rule.
        :type forwarding_rule_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ForwardingRule, or the result of cls(response)
        :rtype: ~dns_resolver_management_client.models.ForwardingRule
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ForwardingRule"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            dns_forwarding_ruleset_name=dns_forwarding_ruleset_name,
            forwarding_rule_name=forwarding_rule_name,
            template_url=self.get.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ForwardingRule', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsForwardingRulesets/{dnsForwardingRulesetName}/forwardingRules/{forwardingRuleName}'}  # type: ignore


    @distributed_trace
    def list(
        self,
        resource_group_name: str,
        dns_forwarding_ruleset_name: str,
        top: Optional[int] = None,
        **kwargs: Any
    ) -> Iterable["_models.ForwardingRuleListResult"]:
        """Lists forwarding rules in a DNS forwarding ruleset.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param dns_forwarding_ruleset_name: The name of the DNS forwarding ruleset.
        :type dns_forwarding_ruleset_name: str
        :param top: The maximum number of results to return. If not specified, returns up to 100
         results.
        :type top: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either ForwardingRuleListResult or the result of
         cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~dns_resolver_management_client.models.ForwardingRuleListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ForwardingRuleListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    dns_forwarding_ruleset_name=dns_forwarding_ruleset_name,
                    top=top,
                    template_url=self.list.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    dns_forwarding_ruleset_name=dns_forwarding_ruleset_name,
                    top=top,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("ForwardingRuleListResult", pipeline_response)
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
    list.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsForwardingRulesets/{dnsForwardingRulesetName}/forwardingRules'}  # type: ignore
