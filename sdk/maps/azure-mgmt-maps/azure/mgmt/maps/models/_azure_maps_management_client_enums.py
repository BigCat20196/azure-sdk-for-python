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

from enum import Enum


class Name(str, Enum):

    s0 = "S0"
    s1 = "S1"
    g2 = "G2"


class Kind(str, Enum):

    gen1 = "Gen1"
    gen2 = "Gen2"


class CreatedByType(str, Enum):

    user = "User"
    application = "Application"
    managed_identity = "ManagedIdentity"
    key = "Key"


class KeyType(str, Enum):

    primary = "primary"
    secondary = "secondary"