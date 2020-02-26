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


class ExtendedLivySessionResponse(Model):
    """ExtendedLivySessionResponse.

    :param livy_info:
    :type livy_info: ~azure.synapse.models.LivySessionStateInformation
    :param name:
    :type name: str
    :param workspace_name:
    :type workspace_name: str
    :param spark_pool_name:
    :type spark_pool_name: str
    :param submitter_name:
    :type submitter_name: str
    :param submitter_id:
    :type submitter_id: str
    :param artifact_id:
    :type artifact_id: str
    :param job_type: Possible values include: 'SparkBatch', 'SparkSession'
    :type job_type: str or ~azure.synapse.models.JobType
    :param result: Possible values include: 'Uncertain', 'Succeeded',
     'Failed', 'Cancelled'
    :type result: str or ~azure.synapse.models.JobResult
    :param scheduler_info:
    :type scheduler_info: ~azure.synapse.models.SchedulerInformation
    :param plugin_info:
    :type plugin_info: ~azure.synapse.models.SparkServicePluginInformation
    :param error_info:
    :type error_info: list[~azure.synapse.models.ErrorInformation]
    :param tags:
    :type tags: dict[str, str]
    :param id:
    :type id: int
    :param app_id:
    :type app_id: str
    :param app_info:
    :type app_info: dict[str, str]
    :param state:
    :type state: str
    :param log:
    :type log: list[str]
    """

    _attribute_map = {
        'livy_info': {'key': 'livyInfo', 'type': 'LivySessionStateInformation'},
        'name': {'key': 'name', 'type': 'str'},
        'workspace_name': {'key': 'workspaceName', 'type': 'str'},
        'spark_pool_name': {'key': 'sparkPoolName', 'type': 'str'},
        'submitter_name': {'key': 'submitterName', 'type': 'str'},
        'submitter_id': {'key': 'submitterId', 'type': 'str'},
        'artifact_id': {'key': 'artifactId', 'type': 'str'},
        'job_type': {'key': 'jobType', 'type': 'str'},
        'result': {'key': 'result', 'type': 'str'},
        'scheduler_info': {'key': 'schedulerInfo', 'type': 'SchedulerInformation'},
        'plugin_info': {'key': 'pluginInfo', 'type': 'SparkServicePluginInformation'},
        'error_info': {'key': 'errorInfo', 'type': '[ErrorInformation]'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'id': {'key': 'id', 'type': 'int'},
        'app_id': {'key': 'appId', 'type': 'str'},
        'app_info': {'key': 'appInfo', 'type': '{str}'},
        'state': {'key': 'state', 'type': 'str'},
        'log': {'key': 'log', 'type': '[str]'},
    }

    def __init__(self, *, livy_info=None, name: str=None, workspace_name: str=None, spark_pool_name: str=None, submitter_name: str=None, submitter_id: str=None, artifact_id: str=None, job_type=None, result=None, scheduler_info=None, plugin_info=None, error_info=None, tags=None, id: int=None, app_id: str=None, app_info=None, state: str=None, log=None, **kwargs) -> None:
        super(ExtendedLivySessionResponse, self).__init__(**kwargs)
        self.livy_info = livy_info
        self.name = name
        self.workspace_name = workspace_name
        self.spark_pool_name = spark_pool_name
        self.submitter_name = submitter_name
        self.submitter_id = submitter_id
        self.artifact_id = artifact_id
        self.job_type = job_type
        self.result = result
        self.scheduler_info = scheduler_info
        self.plugin_info = plugin_info
        self.error_info = error_info
        self.tags = tags
        self.id = id
        self.app_id = app_id
        self.app_info = app_info
        self.state = state
        self.log = log
