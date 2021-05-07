# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class ConfidentialLedgerError(msrest.serialization.Model):
    """An error response from Confidential Ledger.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar error: An error response from Confidential Ledger.
    :vartype error:
     ~azure.confidentialledger._generated/_generated_identity.v0_1_preview.models.ConfidentialLedgerErrorBody
    """

    _validation = {
        'error': {'readonly': True},
    }

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ConfidentialLedgerErrorBody'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ConfidentialLedgerError, self).__init__(**kwargs)
        self.error = None


class ConfidentialLedgerErrorBody(msrest.serialization.Model):
    """An error response from Confidential Ledger.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: The error code.
    :vartype code: str
    :ivar message: The error message.
    :vartype message: str
    :ivar inner_error: An error response from Confidential Ledger.
    :vartype inner_error:
     ~azure.confidentialledger._generated/_generated_identity.v0_1_preview.models.ConfidentialLedgerErrorBody
    """

    _validation = {
        'code': {'readonly': True},
        'message': {'readonly': True},
        'inner_error': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'inner_error': {'key': 'innererror', 'type': 'ConfidentialLedgerErrorBody'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ConfidentialLedgerErrorBody, self).__init__(**kwargs)
        self.code = None
        self.message = None
        self.inner_error = None


class LedgerIdentityInformation(msrest.serialization.Model):
    """Contains the information about a Confidential Ledger.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar ledger_id: Id for the ledger.
    :vartype ledger_id: str
    :param ledger_tls_certificate: Required. PEM-encoded certificate used for TLS by the
     Confidential Ledger.
    :type ledger_tls_certificate: str
    """

    _validation = {
        'ledger_id': {'readonly': True},
        'ledger_tls_certificate': {'required': True},
    }

    _attribute_map = {
        'ledger_id': {'key': 'ledgerId', 'type': 'str'},
        'ledger_tls_certificate': {'key': 'ledgerTlsCertificate', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        ledger_tls_certificate: str,
        **kwargs
    ):
        super(LedgerIdentityInformation, self).__init__(**kwargs)
        self.ledger_id = None
        self.ledger_tls_certificate = ledger_tls_certificate