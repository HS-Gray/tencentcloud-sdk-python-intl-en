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
from tencentcloud.eb.v20210416 import models


class EbClient(AbstractClient):
    _apiVersion = '2021-04-16'
    _endpoint = 'eb.tencentcloudapi.com'
    _service = 'eb'


    def CheckTransformation(self, request):
        """This API is used to test rules and data on the ETL configuration page.

        :param request: Request instance for CheckTransformation.
        :type request: :class:`tencentcloud.eb.v20210416.models.CheckTransformationRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.CheckTransformationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckTransformation", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CheckTransformationResponse()
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


    def CreateRule(self, request):
        """This API is used to create an event rule.

        :param request: Request instance for CreateRule.
        :type request: :class:`tencentcloud.eb.v20210416.models.CreateRuleRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.CreateRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRule", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateRuleResponse()
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


    def CreateTarget(self, request):
        """This API is used to create a delivery target.

        :param request: Request instance for CreateTarget.
        :type request: :class:`tencentcloud.eb.v20210416.models.CreateTargetRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.CreateTargetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTarget", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTargetResponse()
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


    def CreateTransformation(self, request):
        """This API is used to create a transformer.

        :param request: Request instance for CreateTransformation.
        :type request: :class:`tencentcloud.eb.v20210416.models.CreateTransformationRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.CreateTransformationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTransformation", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTransformationResponse()
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


    def DeleteConnection(self, request):
        """This API is used to delete an event connector.

        :param request: Request instance for DeleteConnection.
        :type request: :class:`tencentcloud.eb.v20210416.models.DeleteConnectionRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.DeleteConnectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteConnection", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteConnectionResponse()
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


    def DeleteEventBus(self, request):
        """This API is used to delete an event bus.

        :param request: Request instance for DeleteEventBus.
        :type request: :class:`tencentcloud.eb.v20210416.models.DeleteEventBusRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.DeleteEventBusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteEventBus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteEventBusResponse()
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


    def DeleteRule(self, request):
        """This API is used to delete an event rule.

        :param request: Request instance for DeleteRule.
        :type request: :class:`tencentcloud.eb.v20210416.models.DeleteRuleRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.DeleteRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRule", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteRuleResponse()
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


    def DeleteTarget(self, request):
        """This API is used to delete a delivery target.

        :param request: Request instance for DeleteTarget.
        :type request: :class:`tencentcloud.eb.v20210416.models.DeleteTargetRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.DeleteTargetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTarget", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteTargetResponse()
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


    def DeleteTransformation(self, request):
        """This API is used to delete a transformer.

        :param request: Request instance for DeleteTransformation.
        :type request: :class:`tencentcloud.eb.v20210416.models.DeleteTransformationRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.DeleteTransformationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTransformation", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteTransformationResponse()
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


    def GetRule(self, request):
        """This API is used to get the details of an event rule.

        :param request: Request instance for GetRule.
        :type request: :class:`tencentcloud.eb.v20210416.models.GetRuleRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.GetRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetRule", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetRuleResponse()
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


    def GetTransformation(self, request):
        """This API is used to get the details of a transformer.

        :param request: Request instance for GetTransformation.
        :type request: :class:`tencentcloud.eb.v20210416.models.GetTransformationRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.GetTransformationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetTransformation", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetTransformationResponse()
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


    def ListConnections(self, request):
        """This API is used to get the list of event connectors.

        :param request: Request instance for ListConnections.
        :type request: :class:`tencentcloud.eb.v20210416.models.ListConnectionsRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.ListConnectionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListConnections", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListConnectionsResponse()
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


    def ListEventBuses(self, request):
        """This API is used to get the list of event buses.

        :param request: Request instance for ListEventBuses.
        :type request: :class:`tencentcloud.eb.v20210416.models.ListEventBusesRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.ListEventBusesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListEventBuses", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListEventBusesResponse()
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


    def ListRules(self, request):
        """This API is used to get the list of event rules.

        :param request: Request instance for ListRules.
        :type request: :class:`tencentcloud.eb.v20210416.models.ListRulesRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.ListRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListRules", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListRulesResponse()
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


    def ListTargets(self, request):
        """This API is used to get the list delivery targets.

        :param request: Request instance for ListTargets.
        :type request: :class:`tencentcloud.eb.v20210416.models.ListTargetsRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.ListTargetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListTargets", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListTargetsResponse()
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


    def UpdateConnection(self, request):
        """This API is used to update an event connector.

        :param request: Request instance for UpdateConnection.
        :type request: :class:`tencentcloud.eb.v20210416.models.UpdateConnectionRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.UpdateConnectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateConnection", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateConnectionResponse()
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


    def UpdateRule(self, request):
        """This API is used to update an event rule.

        :param request: Request instance for UpdateRule.
        :type request: :class:`tencentcloud.eb.v20210416.models.UpdateRuleRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.UpdateRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateRule", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateRuleResponse()
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


    def UpdateTarget(self, request):
        """This API is used to update a delivery target.

        :param request: Request instance for UpdateTarget.
        :type request: :class:`tencentcloud.eb.v20210416.models.UpdateTargetRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.UpdateTargetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateTarget", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateTargetResponse()
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


    def UpdateTransformation(self, request):
        """This API is used to update a transformer.

        :param request: Request instance for UpdateTransformation.
        :type request: :class:`tencentcloud.eb.v20210416.models.UpdateTransformationRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.UpdateTransformationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateTransformation", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateTransformationResponse()
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