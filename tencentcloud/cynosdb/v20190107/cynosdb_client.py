# -*- coding: utf8 -*-
# Copyright (c) 2017-2021 THL A29 Limited, a Tencent company. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.cynosdb.v20190107 import models


class CynosdbClient(AbstractClient):
    _apiVersion = '2019-01-07'
    _endpoint = 'cynosdb.tencentcloudapi.com'
    _service = 'cynosdb'


    def ActivateInstance(self, request):
        """This API is used to remove the isolation of an instance to make it accessible again.

        :param request: Request instance for ActivateInstance.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ActivateInstanceRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ActivateInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ActivateInstance", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ActivateInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AddInstances(self, request):
        """This API is used to add an instance in a cluster.

        :param request: Request instance for AddInstances.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.AddInstancesRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.AddInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddInstances", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateAccounts(self, request):
        """This API is used to create an account.

        :param request: Request instance for CreateAccounts.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.CreateAccountsRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.CreateAccountsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAccounts", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAccountsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAccounts(self, request):
        """This API is used to query database management accounts.

        :param request: Request instance for DescribeAccounts.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeAccountsRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeAccountsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccounts", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccountsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBackupConfig(self, request):
        """This API is used to get the backup configuration information of the specified cluster, including the full backup time range and backup file retention period.

        :param request: Request instance for DescribeBackupConfig.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeBackupConfigRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeBackupConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBackupConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBackupList(self, request):
        """This API is used to query the list of backup files.

        :param request: Request instance for DescribeBackupList.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeBackupListRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeBackupListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBackupListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeClusterDetail(self, request):
        """This API is used to display cluster details.

        :param request: Request instance for DescribeClusterDetail.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeClusterDetailRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeClusterDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClusterDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeClusterInstanceGrps(self, request):
        """This API is used to query instance groups.

        :param request: Request instance for DescribeClusterInstanceGrps.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeClusterInstanceGrpsRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeClusterInstanceGrpsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterInstanceGrps", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClusterInstanceGrpsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeClusters(self, request):
        """This API is used to the list of clusters.

        :param request: Request instance for DescribeClusters.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeClustersRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeClustersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusters", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClustersResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDBSecurityGroups(self, request):
        """This API is used to query the security group information of an instance.

        :param request: Request instance for DescribeDBSecurityGroups.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeDBSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeDBSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBSecurityGroups", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBSecurityGroupsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeInstanceDetail(self, request):
        """This API is used to query instance details.

        :param request: Request instance for DescribeInstanceDetail.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeInstanceDetailRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeInstanceDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeInstanceSpecs(self, request):
        """This API is used to query instance specifications.

        :param request: Request instance for DescribeInstanceSpecs.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeInstanceSpecsRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeInstanceSpecsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceSpecs", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceSpecsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeInstances(self, request):
        """This API is used to query the list of instances.

        :param request: Request instance for DescribeInstances.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeInstancesRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstances", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeMaintainPeriod(self, request):
        """This API is used to query the instance maintenance window.

        :param request: Request instance for DescribeMaintainPeriod.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeMaintainPeriodRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeMaintainPeriodResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMaintainPeriod", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMaintainPeriodResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeProjectSecurityGroups(self, request):
        """This API is used to query the security group information of a project.

        :param request: Request instance for DescribeProjectSecurityGroups.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeProjectSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeProjectSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProjectSecurityGroups", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProjectSecurityGroupsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeResourcesByDealName(self, request):
        """This API is used to query the list of resources by billing order ID.

        :param request: Request instance for DescribeResourcesByDealName.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeResourcesByDealNameRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeResourcesByDealNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResourcesByDealName", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeResourcesByDealNameResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRollbackTimeRange(self, request):
        """This API is used to query the valid rollback time range for the specified cluster.

        :param request: Request instance for DescribeRollbackTimeRange.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeRollbackTimeRangeRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeRollbackTimeRangeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRollbackTimeRange", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRollbackTimeRangeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRollbackTimeValidity(self, request):
        """This API is used to query whether rollback is possible based on the specified time and cluster.

        :param request: Request instance for DescribeRollbackTimeValidity.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeRollbackTimeValidityRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeRollbackTimeValidityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRollbackTimeValidity", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRollbackTimeValidityResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def IsolateCluster(self, request):
        """This API is used to isolate a cluster.

        :param request: Request instance for IsolateCluster.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.IsolateClusterRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.IsolateClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IsolateCluster", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.IsolateClusterResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def IsolateInstance(self, request):
        """This API is used to isolate an instance.

        :param request: Request instance for IsolateInstance.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.IsolateInstanceRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.IsolateInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IsolateInstance", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.IsolateInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyBackupConfig(self, request):
        """This API is used to modify the backup configuration of the specified cluster.

        :param request: Request instance for ModifyBackupConfig.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyBackupConfigRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyBackupConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBackupConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyBackupConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyClusterName(self, request):
        """This API is used to modify cluster name.

        :param request: Request instance for ModifyClusterName.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyClusterNameRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyClusterNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyClusterName", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyClusterNameResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyClusterParam(self, request):
        """This API is used to modify the parameters of a cluster.

        :param request: Request instance for ModifyClusterParam.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyClusterParamRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyClusterParamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyClusterParam", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyClusterParamResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyDBInstanceSecurityGroups(self, request):
        """This API is used to modify the security groups bound to an instance.

        :param request: Request instance for ModifyDBInstanceSecurityGroups.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyDBInstanceSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyDBInstanceSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBInstanceSecurityGroups", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDBInstanceSecurityGroupsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyInstanceName(self, request):
        """This API is used to modify instance name.

        :param request: Request instance for ModifyInstanceName.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyInstanceNameRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyInstanceNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstanceName", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyInstanceNameResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyMaintainPeriodConfig(self, request):
        """This API is used to modify the maintenance time configuration.

        :param request: Request instance for ModifyMaintainPeriodConfig.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyMaintainPeriodConfigRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyMaintainPeriodConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMaintainPeriodConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyMaintainPeriodConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def OfflineCluster(self, request):
        """This API is used to deactivate a cluster.

        :param request: Request instance for OfflineCluster.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.OfflineClusterRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.OfflineClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OfflineCluster", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.OfflineClusterResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def OfflineInstance(self, request):
        """This API is used to deactivate an instance.

        :param request: Request instance for OfflineInstance.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.OfflineInstanceRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.OfflineInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OfflineInstance", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.OfflineInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def PauseServerless(self, request):
        """This API is used to pause a serverless cluster.

        :param request: Request instance for PauseServerless.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.PauseServerlessRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.PauseServerlessResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PauseServerless", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PauseServerlessResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ResumeServerless(self, request):
        """This API is used to resume a serverless cluster.

        :param request: Request instance for ResumeServerless.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ResumeServerlessRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ResumeServerlessResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResumeServerless", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResumeServerlessResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SetRenewFlag(self, request):
        """This API is used to set auto-renewal for an instance.

        :param request: Request instance for SetRenewFlag.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.SetRenewFlagRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.SetRenewFlagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetRenewFlag", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetRenewFlagResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpgradeInstance(self, request):
        """This API is used to upgrade an instance.

        :param request: Request instance for UpgradeInstance.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.UpgradeInstanceRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.UpgradeInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradeInstance", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpgradeInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)