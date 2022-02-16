# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Optional, TYPE_CHECKING

from azure.core.rest import HttpRequest, HttpResponse
from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

from . import models
from ._configuration import StorageManagementClientConfiguration
from .operations import BlobContainersOperations, BlobInventoryPoliciesOperations, BlobServicesOperations, EncryptionScopesOperations, FileServicesOperations, FileSharesOperations, ManagementPoliciesOperations, ObjectReplicationPoliciesOperations, Operations, PrivateEndpointConnectionsOperations, PrivateLinkResourcesOperations, QueueOperations, QueueServicesOperations, SkusOperations, StorageAccountsOperations, TableOperations, TableServicesOperations, UsagesOperations

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential

class StorageManagementClient:
    """The Azure Storage Management API.

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.storage.v2019_06_01.operations.Operations
    :ivar skus: SkusOperations operations
    :vartype skus: azure.mgmt.storage.v2019_06_01.operations.SkusOperations
    :ivar storage_accounts: StorageAccountsOperations operations
    :vartype storage_accounts: azure.mgmt.storage.v2019_06_01.operations.StorageAccountsOperations
    :ivar usages: UsagesOperations operations
    :vartype usages: azure.mgmt.storage.v2019_06_01.operations.UsagesOperations
    :ivar management_policies: ManagementPoliciesOperations operations
    :vartype management_policies:
     azure.mgmt.storage.v2019_06_01.operations.ManagementPoliciesOperations
    :ivar blob_inventory_policies: BlobInventoryPoliciesOperations operations
    :vartype blob_inventory_policies:
     azure.mgmt.storage.v2019_06_01.operations.BlobInventoryPoliciesOperations
    :ivar private_endpoint_connections: PrivateEndpointConnectionsOperations operations
    :vartype private_endpoint_connections:
     azure.mgmt.storage.v2019_06_01.operations.PrivateEndpointConnectionsOperations
    :ivar private_link_resources: PrivateLinkResourcesOperations operations
    :vartype private_link_resources:
     azure.mgmt.storage.v2019_06_01.operations.PrivateLinkResourcesOperations
    :ivar object_replication_policies: ObjectReplicationPoliciesOperations operations
    :vartype object_replication_policies:
     azure.mgmt.storage.v2019_06_01.operations.ObjectReplicationPoliciesOperations
    :ivar encryption_scopes: EncryptionScopesOperations operations
    :vartype encryption_scopes:
     azure.mgmt.storage.v2019_06_01.operations.EncryptionScopesOperations
    :ivar blob_services: BlobServicesOperations operations
    :vartype blob_services: azure.mgmt.storage.v2019_06_01.operations.BlobServicesOperations
    :ivar blob_containers: BlobContainersOperations operations
    :vartype blob_containers: azure.mgmt.storage.v2019_06_01.operations.BlobContainersOperations
    :ivar file_services: FileServicesOperations operations
    :vartype file_services: azure.mgmt.storage.v2019_06_01.operations.FileServicesOperations
    :ivar file_shares: FileSharesOperations operations
    :vartype file_shares: azure.mgmt.storage.v2019_06_01.operations.FileSharesOperations
    :ivar queue_services: QueueServicesOperations operations
    :vartype queue_services: azure.mgmt.storage.v2019_06_01.operations.QueueServicesOperations
    :ivar queue: QueueOperations operations
    :vartype queue: azure.mgmt.storage.v2019_06_01.operations.QueueOperations
    :ivar table_services: TableServicesOperations operations
    :vartype table_services: azure.mgmt.storage.v2019_06_01.operations.TableServicesOperations
    :ivar table: TableOperations operations
    :vartype table: azure.mgmt.storage.v2019_06_01.operations.TableOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param base_url: Service URL. Default value is 'https://management.azure.com'.
    :type base_url: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(
        self,
        credential: "TokenCredential",
        subscription_id: str,
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = StorageManagementClientConfiguration(credential=credential, subscription_id=subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.operations = Operations(self._client, self._config, self._serialize, self._deserialize)
        self.skus = SkusOperations(self._client, self._config, self._serialize, self._deserialize)
        self.storage_accounts = StorageAccountsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.usages = UsagesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.management_policies = ManagementPoliciesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.blob_inventory_policies = BlobInventoryPoliciesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.private_endpoint_connections = PrivateEndpointConnectionsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.private_link_resources = PrivateLinkResourcesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.object_replication_policies = ObjectReplicationPoliciesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.encryption_scopes = EncryptionScopesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.blob_services = BlobServicesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.blob_containers = BlobContainersOperations(self._client, self._config, self._serialize, self._deserialize)
        self.file_services = FileServicesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.file_shares = FileSharesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.queue_services = QueueServicesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.queue = QueueOperations(self._client, self._config, self._serialize, self._deserialize)
        self.table_services = TableServicesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.table = TableOperations(self._client, self._config, self._serialize, self._deserialize)


    def _send_request(
        self,
        request,  # type: HttpRequest
        **kwargs: Any
    ) -> HttpResponse:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client._send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/python/protocol/quickstart

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> StorageManagementClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
