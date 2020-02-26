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

from msrest.serialization import Model


class DataLakeStorageAccountDetails(Model):
    """Details of the data lake storage account associated with the workspace.

    :param account_url: Account URL
    :type account_url: str
    :param filesystem: Filesystem name
    :type filesystem: str
    """

    _attribute_map = {
        'account_url': {'key': 'accountUrl', 'type': 'str'},
        'filesystem': {'key': 'filesystem', 'type': 'str'},
    }

    def __init__(self, *, account_url: str=None, filesystem: str=None, **kwargs) -> None:
        super(DataLakeStorageAccountDetails, self).__init__(**kwargs)
        self.account_url = account_url
        self.filesystem = filesystem
