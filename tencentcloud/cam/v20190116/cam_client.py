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
from tencentcloud.cam.v20190116 import models


class CamClient(AbstractClient):
    _apiVersion = '2019-01-16'
    _endpoint = 'cam.tencentcloudapi.com'
    _service = 'cam'


    def AddUser(self, request):
        """This API is used to add sub-users.

        :param request: Request instance for AddUser.
        :type request: :class:`tencentcloud.cam.v20190116.models.AddUserRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.AddUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddUser", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddUserResponse()
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


    def AddUserToGroup(self, request):
        """This API is used to add users to a user group.

        :param request: Request instance for AddUserToGroup.
        :type request: :class:`tencentcloud.cam.v20190116.models.AddUserToGroupRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.AddUserToGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddUserToGroup", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddUserToGroupResponse()
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


    def AttachGroupPolicy(self, request):
        """This API (AttachGroupPolicy) is used to associate a policy with a user group.

        :param request: Request instance for AttachGroupPolicy.
        :type request: :class:`tencentcloud.cam.v20190116.models.AttachGroupPolicyRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.AttachGroupPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AttachGroupPolicy", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AttachGroupPolicyResponse()
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


    def AttachRolePolicy(self, request):
        """This API (AttachRolePolicy) is used to associate a policy with a role.

        :param request: Request instance for AttachRolePolicy.
        :type request: :class:`tencentcloud.cam.v20190116.models.AttachRolePolicyRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.AttachRolePolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AttachRolePolicy", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AttachRolePolicyResponse()
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


    def AttachUserPolicy(self, request):
        """This API (AttachUserPolicy) is used to associates a policy with a user.

        :param request: Request instance for AttachUserPolicy.
        :type request: :class:`tencentcloud.cam.v20190116.models.AttachUserPolicyRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.AttachUserPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AttachUserPolicy", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AttachUserPolicyResponse()
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


    def ConsumeCustomMFAToken(self, request):
        """This API is used to verify a custom multi-factor Token.

        :param request: Request instance for ConsumeCustomMFAToken.
        :type request: :class:`tencentcloud.cam.v20190116.models.ConsumeCustomMFATokenRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.ConsumeCustomMFATokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ConsumeCustomMFAToken", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ConsumeCustomMFATokenResponse()
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


    def CreateGroup(self, request):
        """This API is used to create a user group.

        :param request: Request instance for CreateGroup.
        :type request: :class:`tencentcloud.cam.v20190116.models.CreateGroupRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.CreateGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateGroup", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateGroupResponse()
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


    def CreateOIDCConfig(self, request):
        """This API is used to create role OIDC configurations.

        :param request: Request instance for CreateOIDCConfig.
        :type request: :class:`tencentcloud.cam.v20190116.models.CreateOIDCConfigRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.CreateOIDCConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOIDCConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateOIDCConfigResponse()
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


    def CreatePolicy(self, request):
        """This API (CreatePolicy) is used to create a policy.

        :param request: Request instance for CreatePolicy.
        :type request: :class:`tencentcloud.cam.v20190116.models.CreatePolicyRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.CreatePolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePolicy", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePolicyResponse()
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


    def CreatePolicyVersion(self, request):
        """This API is used to add a policy version. After creating a policy version, you can easily change the policy by changing the policy version.

        :param request: Request instance for CreatePolicyVersion.
        :type request: :class:`tencentcloud.cam.v20190116.models.CreatePolicyVersionRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.CreatePolicyVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePolicyVersion", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePolicyVersionResponse()
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


    def CreateRole(self, request):
        """This API (CreateRole) is used to create a role.

        :param request: Request instance for CreateRole.
        :type request: :class:`tencentcloud.cam.v20190116.models.CreateRoleRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.CreateRoleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRole", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateRoleResponse()
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


    def CreateSAMLProvider(self, request):
        """This API is used to create a SAML identity provider.

        :param request: Request instance for CreateSAMLProvider.
        :type request: :class:`tencentcloud.cam.v20190116.models.CreateSAMLProviderRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.CreateSAMLProviderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSAMLProvider", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSAMLProviderResponse()
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


    def CreateServiceLinkedRole(self, request):
        """This API is used to create a service-linked role.

        :param request: Request instance for CreateServiceLinkedRole.
        :type request: :class:`tencentcloud.cam.v20190116.models.CreateServiceLinkedRoleRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.CreateServiceLinkedRoleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateServiceLinkedRole", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateServiceLinkedRoleResponse()
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


    def CreateUserOIDCConfig(self, request):
        """This API is used to create a user OIDC configuration. Only one user OIDC IdP can be created, and the user SAML SSO IdP will be automatically disabled after it is created.

        :param request: Request instance for CreateUserOIDCConfig.
        :type request: :class:`tencentcloud.cam.v20190116.models.CreateUserOIDCConfigRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.CreateUserOIDCConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateUserOIDCConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateUserOIDCConfigResponse()
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


    def CreateUserSAMLConfig(self, request):
        """This API is used to create user SAML configurations.

        :param request: Request instance for CreateUserSAMLConfig.
        :type request: :class:`tencentcloud.cam.v20190116.models.CreateUserSAMLConfigRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.CreateUserSAMLConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateUserSAMLConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateUserSAMLConfigResponse()
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


    def DeleteGroup(self, request):
        """This API is used to delete a user group.

        :param request: Request instance for DeleteGroup.
        :type request: :class:`tencentcloud.cam.v20190116.models.DeleteGroupRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.DeleteGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteGroup", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteGroupResponse()
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


    def DeleteOIDCConfig(self, request):
        """This API is used to delete OIDC IdPs.

        :param request: Request instance for DeleteOIDCConfig.
        :type request: :class:`tencentcloud.cam.v20190116.models.DeleteOIDCConfigRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.DeleteOIDCConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteOIDCConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteOIDCConfigResponse()
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


    def DeletePolicy(self, request):
        """This API (DeletePolicy) is used to delete a policy.

        :param request: Request instance for DeletePolicy.
        :type request: :class:`tencentcloud.cam.v20190116.models.DeletePolicyRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.DeletePolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePolicy", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeletePolicyResponse()
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


    def DeletePolicyVersion(self, request):
        """This API is used to delete a policy version of a policy.

        :param request: Request instance for DeletePolicyVersion.
        :type request: :class:`tencentcloud.cam.v20190116.models.DeletePolicyVersionRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.DeletePolicyVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePolicyVersion", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeletePolicyVersionResponse()
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


    def DeleteRole(self, request):
        """This API (DeleteRole) is used to delete a specified role.

        :param request: Request instance for DeleteRole.
        :type request: :class:`tencentcloud.cam.v20190116.models.DeleteRoleRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.DeleteRoleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRole", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteRoleResponse()
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


    def DeleteRolePermissionsBoundary(self, request):
        """This API is used to delete a role permission boundary.

        :param request: Request instance for DeleteRolePermissionsBoundary.
        :type request: :class:`tencentcloud.cam.v20190116.models.DeleteRolePermissionsBoundaryRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.DeleteRolePermissionsBoundaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRolePermissionsBoundary", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteRolePermissionsBoundaryResponse()
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


    def DeleteSAMLProvider(self, request):
        """This API is used to delete a SAML identity provider.

        :param request: Request instance for DeleteSAMLProvider.
        :type request: :class:`tencentcloud.cam.v20190116.models.DeleteSAMLProviderRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.DeleteSAMLProviderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSAMLProvider", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteSAMLProviderResponse()
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


    def DeleteServiceLinkedRole(self, request):
        """This API is used to delete a service-linked role.

        :param request: Request instance for DeleteServiceLinkedRole.
        :type request: :class:`tencentcloud.cam.v20190116.models.DeleteServiceLinkedRoleRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.DeleteServiceLinkedRoleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteServiceLinkedRole", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteServiceLinkedRoleResponse()
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


    def DeleteUser(self, request):
        """This API is used to delete a sub-user.

        :param request: Request instance for DeleteUser.
        :type request: :class:`tencentcloud.cam.v20190116.models.DeleteUserRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.DeleteUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteUser", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteUserResponse()
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


    def DeleteUserPermissionsBoundary(self, request):
        """This API is used to delete a user permission boundary.

        :param request: Request instance for DeleteUserPermissionsBoundary.
        :type request: :class:`tencentcloud.cam.v20190116.models.DeleteUserPermissionsBoundaryRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.DeleteUserPermissionsBoundaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteUserPermissionsBoundary", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteUserPermissionsBoundaryResponse()
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


    def DescribeOIDCConfig(self, request):
        """This API is used to query role OIDC configurations.

        :param request: Request instance for DescribeOIDCConfig.
        :type request: :class:`tencentcloud.cam.v20190116.models.DescribeOIDCConfigRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.DescribeOIDCConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOIDCConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeOIDCConfigResponse()
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


    def DescribeRoleList(self, request):
        """This API (DescribeRoleList) is used to get the role list under the account.

        :param request: Request instance for DescribeRoleList.
        :type request: :class:`tencentcloud.cam.v20190116.models.DescribeRoleListRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.DescribeRoleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRoleList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRoleListResponse()
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


    def DescribeSafeAuthFlagColl(self, request):
        """This API is used to query security settings.

        :param request: Request instance for DescribeSafeAuthFlagColl.
        :type request: :class:`tencentcloud.cam.v20190116.models.DescribeSafeAuthFlagCollRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.DescribeSafeAuthFlagCollResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSafeAuthFlagColl", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSafeAuthFlagCollResponse()
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


    def DescribeSafeAuthFlagIntl(self, request):
        """This API is used to query security settings.

        :param request: Request instance for DescribeSafeAuthFlagIntl.
        :type request: :class:`tencentcloud.cam.v20190116.models.DescribeSafeAuthFlagIntlRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.DescribeSafeAuthFlagIntlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSafeAuthFlagIntl", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSafeAuthFlagIntlResponse()
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


    def DescribeSubAccounts(self, request):
        """This API is used to query sub-users through the sub-user UIN list.

        :param request: Request instance for DescribeSubAccounts.
        :type request: :class:`tencentcloud.cam.v20190116.models.DescribeSubAccountsRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.DescribeSubAccountsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSubAccounts", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSubAccountsResponse()
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


    def DescribeUserOIDCConfig(self, request):
        """This API is used to query the user OIDC configuration.

        :param request: Request instance for DescribeUserOIDCConfig.
        :type request: :class:`tencentcloud.cam.v20190116.models.DescribeUserOIDCConfigRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.DescribeUserOIDCConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserOIDCConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUserOIDCConfigResponse()
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


    def DescribeUserSAMLConfig(self, request):
        """This API is used to query user SAML configurations.

        :param request: Request instance for DescribeUserSAMLConfig.
        :type request: :class:`tencentcloud.cam.v20190116.models.DescribeUserSAMLConfigRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.DescribeUserSAMLConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserSAMLConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUserSAMLConfigResponse()
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


    def DetachGroupPolicy(self, request):
        """This API (DetachGroupPolicy) is used to unassociate a policy and a user group.

        :param request: Request instance for DetachGroupPolicy.
        :type request: :class:`tencentcloud.cam.v20190116.models.DetachGroupPolicyRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.DetachGroupPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DetachGroupPolicy", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetachGroupPolicyResponse()
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


    def DetachRolePolicy(self, request):
        """This API (DetachRolePolicy) is used to unassociate a policy and a role.

        :param request: Request instance for DetachRolePolicy.
        :type request: :class:`tencentcloud.cam.v20190116.models.DetachRolePolicyRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.DetachRolePolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DetachRolePolicy", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetachRolePolicyResponse()
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


    def DetachUserPolicy(self, request):
        """This API (DetachUserPolicy) is used to unassociate a policy and a user.

        :param request: Request instance for DetachUserPolicy.
        :type request: :class:`tencentcloud.cam.v20190116.models.DetachUserPolicyRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.DetachUserPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DetachUserPolicy", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetachUserPolicyResponse()
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


    def DisableUserSSO(self, request):
        """This API is used to disable user SSO.

        :param request: Request instance for DisableUserSSO.
        :type request: :class:`tencentcloud.cam.v20190116.models.DisableUserSSORequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.DisableUserSSOResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableUserSSO", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisableUserSSOResponse()
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


    def GetAccountSummary(self, request):
        """This API is used to query account summary.

        :param request: Request instance for GetAccountSummary.
        :type request: :class:`tencentcloud.cam.v20190116.models.GetAccountSummaryRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.GetAccountSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetAccountSummary", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetAccountSummaryResponse()
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


    def GetCustomMFATokenInfo(self, request):
        """This API is used to get information associated with a custom multi-factor Token

        :param request: Request instance for GetCustomMFATokenInfo.
        :type request: :class:`tencentcloud.cam.v20190116.models.GetCustomMFATokenInfoRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.GetCustomMFATokenInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetCustomMFATokenInfo", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetCustomMFATokenInfoResponse()
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


    def GetGroup(self, request):
        """This API is used to query user group details.

        :param request: Request instance for GetGroup.
        :type request: :class:`tencentcloud.cam.v20190116.models.GetGroupRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.GetGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetGroup", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetGroupResponse()
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


    def GetPolicy(self, request):
        """This API (GetPolicy) is used to query and view policy details.

        :param request: Request instance for GetPolicy.
        :type request: :class:`tencentcloud.cam.v20190116.models.GetPolicyRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.GetPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetPolicy", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetPolicyResponse()
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


    def GetPolicyVersion(self, request):
        """This API is used to query policy version details.

        :param request: Request instance for GetPolicyVersion.
        :type request: :class:`tencentcloud.cam.v20190116.models.GetPolicyVersionRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.GetPolicyVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetPolicyVersion", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetPolicyVersionResponse()
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


    def GetRole(self, request):
        """This API (GetRole) is used to get the details of a specified role.

        :param request: Request instance for GetRole.
        :type request: :class:`tencentcloud.cam.v20190116.models.GetRoleRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.GetRoleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetRole", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetRoleResponse()
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


    def GetSAMLProvider(self, request):
        """This API is used to query SAML identity provider details.

        :param request: Request instance for GetSAMLProvider.
        :type request: :class:`tencentcloud.cam.v20190116.models.GetSAMLProviderRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.GetSAMLProviderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetSAMLProvider", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetSAMLProviderResponse()
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


    def GetSecurityLastUsed(self, request):
        """This API is used to get a key’s recent usage details.

        :param request: Request instance for GetSecurityLastUsed.
        :type request: :class:`tencentcloud.cam.v20190116.models.GetSecurityLastUsedRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.GetSecurityLastUsedResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetSecurityLastUsed", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetSecurityLastUsedResponse()
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


    def GetServiceLinkedRoleDeletionStatus(self, request):
        """This API is used to get the status of the service-linked role deletion based on the `TaskId`

        :param request: Request instance for GetServiceLinkedRoleDeletionStatus.
        :type request: :class:`tencentcloud.cam.v20190116.models.GetServiceLinkedRoleDeletionStatusRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.GetServiceLinkedRoleDeletionStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetServiceLinkedRoleDeletionStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetServiceLinkedRoleDeletionStatusResponse()
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


    def GetUser(self, request):
        """This API is used to query sub-users.

        :param request: Request instance for GetUser.
        :type request: :class:`tencentcloud.cam.v20190116.models.GetUserRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.GetUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetUser", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetUserResponse()
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


    def GetUserAppId(self, request):
        """This API is used to get the user AppId.

        :param request: Request instance for GetUserAppId.
        :type request: :class:`tencentcloud.cam.v20190116.models.GetUserAppIdRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.GetUserAppIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetUserAppId", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetUserAppIdResponse()
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


    def ListAccessKeys(self, request):
        """This API is used to list the access keys associated with a specified CAM user.

        :param request: Request instance for ListAccessKeys.
        :type request: :class:`tencentcloud.cam.v20190116.models.ListAccessKeysRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.ListAccessKeysResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAccessKeys", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListAccessKeysResponse()
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


    def ListAttachedGroupPolicies(self, request):
        """This API (ListAttachedGroupPolicies) is used to query the list of policies associated with a user group.

        :param request: Request instance for ListAttachedGroupPolicies.
        :type request: :class:`tencentcloud.cam.v20190116.models.ListAttachedGroupPoliciesRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.ListAttachedGroupPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAttachedGroupPolicies", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListAttachedGroupPoliciesResponse()
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


    def ListAttachedRolePolicies(self, request):
        """This API (ListAttachedRolePolicies) is used to obtain the list of the policies associated with a role.

        :param request: Request instance for ListAttachedRolePolicies.
        :type request: :class:`tencentcloud.cam.v20190116.models.ListAttachedRolePoliciesRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.ListAttachedRolePoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAttachedRolePolicies", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListAttachedRolePoliciesResponse()
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


    def ListAttachedUserAllPolicies(self, request):
        """This API is used to list policies associated with the user (including those inherited from the user group).

        :param request: Request instance for ListAttachedUserAllPolicies.
        :type request: :class:`tencentcloud.cam.v20190116.models.ListAttachedUserAllPoliciesRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.ListAttachedUserAllPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAttachedUserAllPolicies", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListAttachedUserAllPoliciesResponse()
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


    def ListAttachedUserPolicies(self, request):
        """This API (ListAttachedUserPolicies) is used to query the list of policies associated with a sub-account.

        :param request: Request instance for ListAttachedUserPolicies.
        :type request: :class:`tencentcloud.cam.v20190116.models.ListAttachedUserPoliciesRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.ListAttachedUserPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAttachedUserPolicies", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListAttachedUserPoliciesResponse()
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


    def ListCollaborators(self, request):
        """This API is used to get the collaborator list.

        :param request: Request instance for ListCollaborators.
        :type request: :class:`tencentcloud.cam.v20190116.models.ListCollaboratorsRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.ListCollaboratorsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListCollaborators", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListCollaboratorsResponse()
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


    def ListEntitiesForPolicy(self, request):
        """This API (ListEntitiesForPolicy) is used to query the list of entities associated with a policy.

        :param request: Request instance for ListEntitiesForPolicy.
        :type request: :class:`tencentcloud.cam.v20190116.models.ListEntitiesForPolicyRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.ListEntitiesForPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListEntitiesForPolicy", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListEntitiesForPolicyResponse()
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


    def ListGroups(self, request):
        """This API is used to query the list of user groups.

        :param request: Request instance for ListGroups.
        :type request: :class:`tencentcloud.cam.v20190116.models.ListGroupsRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.ListGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListGroups", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListGroupsResponse()
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


    def ListGroupsForUser(self, request):
        """This API is used to list user groups associated with a user.

        :param request: Request instance for ListGroupsForUser.
        :type request: :class:`tencentcloud.cam.v20190116.models.ListGroupsForUserRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.ListGroupsForUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListGroupsForUser", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListGroupsForUserResponse()
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


    def ListPolicies(self, request):
        """This API is used to query the policy list.

        :param request: Request instance for ListPolicies.
        :type request: :class:`tencentcloud.cam.v20190116.models.ListPoliciesRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.ListPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListPolicies", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListPoliciesResponse()
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


    def ListPolicyVersions(self, request):
        """This API is used to get the list of policy versions.

        :param request: Request instance for ListPolicyVersions.
        :type request: :class:`tencentcloud.cam.v20190116.models.ListPolicyVersionsRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.ListPolicyVersionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListPolicyVersions", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListPolicyVersionsResponse()
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


    def ListSAMLProviders(self, request):
        """This API is used to query the list of SAML identity providers.

        :param request: Request instance for ListSAMLProviders.
        :type request: :class:`tencentcloud.cam.v20190116.models.ListSAMLProvidersRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.ListSAMLProvidersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListSAMLProviders", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListSAMLProvidersResponse()
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


    def ListUsers(self, request):
        """This API is used to pull sub-users.

        :param request: Request instance for ListUsers.
        :type request: :class:`tencentcloud.cam.v20190116.models.ListUsersRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.ListUsersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListUsers", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListUsersResponse()
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


    def ListUsersForGroup(self, request):
        """This API is used to query the list of users associated with a user group.

        :param request: Request instance for ListUsersForGroup.
        :type request: :class:`tencentcloud.cam.v20190116.models.ListUsersForGroupRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.ListUsersForGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListUsersForGroup", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListUsersForGroupResponse()
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


    def PutRolePermissionsBoundary(self, request):
        """This API is used to set a role permission boundary.

        :param request: Request instance for PutRolePermissionsBoundary.
        :type request: :class:`tencentcloud.cam.v20190116.models.PutRolePermissionsBoundaryRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.PutRolePermissionsBoundaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PutRolePermissionsBoundary", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PutRolePermissionsBoundaryResponse()
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


    def PutUserPermissionsBoundary(self, request):
        """This API is used to set a user permission boundary.

        :param request: Request instance for PutUserPermissionsBoundary.
        :type request: :class:`tencentcloud.cam.v20190116.models.PutUserPermissionsBoundaryRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.PutUserPermissionsBoundaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PutUserPermissionsBoundary", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PutUserPermissionsBoundaryResponse()
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


    def RemoveUserFromGroup(self, request):
        """This API is used to delete users from a user group.

        :param request: Request instance for RemoveUserFromGroup.
        :type request: :class:`tencentcloud.cam.v20190116.models.RemoveUserFromGroupRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.RemoveUserFromGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveUserFromGroup", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RemoveUserFromGroupResponse()
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


    def SetDefaultPolicyVersion(self, request):
        """This API is used to set the operative policy version.

        :param request: Request instance for SetDefaultPolicyVersion.
        :type request: :class:`tencentcloud.cam.v20190116.models.SetDefaultPolicyVersionRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.SetDefaultPolicyVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetDefaultPolicyVersion", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetDefaultPolicyVersionResponse()
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


    def SetMfaFlag(self, request):
        """This API is used to set account verification for login and sensitive operations for sub-users.

        :param request: Request instance for SetMfaFlag.
        :type request: :class:`tencentcloud.cam.v20190116.models.SetMfaFlagRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.SetMfaFlagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetMfaFlag", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetMfaFlagResponse()
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


    def UpdateAssumeRolePolicy(self, request):
        """This API (UpdateAssumeRolePolicy) is used to modify the trust policy of a role.

        :param request: Request instance for UpdateAssumeRolePolicy.
        :type request: :class:`tencentcloud.cam.v20190116.models.UpdateAssumeRolePolicyRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.UpdateAssumeRolePolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateAssumeRolePolicy", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateAssumeRolePolicyResponse()
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


    def UpdateGroup(self, request):
        """This API is used to update a user group.

        :param request: Request instance for UpdateGroup.
        :type request: :class:`tencentcloud.cam.v20190116.models.UpdateGroupRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.UpdateGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateGroup", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateGroupResponse()
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


    def UpdateOIDCConfig(self, request):
        """This API is used to modify role OIDC configurations.

        :param request: Request instance for UpdateOIDCConfig.
        :type request: :class:`tencentcloud.cam.v20190116.models.UpdateOIDCConfigRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.UpdateOIDCConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateOIDCConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateOIDCConfigResponse()
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


    def UpdatePolicy(self, request):
        """This API is used to update a policy.
        This API will update the default version of an existing policy instead of creating a new one. If no policy exists, a default version will be created.

        :param request: Request instance for UpdatePolicy.
        :type request: :class:`tencentcloud.cam.v20190116.models.UpdatePolicyRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.UpdatePolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdatePolicy", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdatePolicyResponse()
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


    def UpdateRoleConsoleLogin(self, request):
        """This API is used to modify a role's login permissions.

        :param request: Request instance for UpdateRoleConsoleLogin.
        :type request: :class:`tencentcloud.cam.v20190116.models.UpdateRoleConsoleLoginRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.UpdateRoleConsoleLoginResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateRoleConsoleLogin", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateRoleConsoleLoginResponse()
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


    def UpdateRoleDescription(self, request):
        """This API (UpdateRoleDescription) is used to modify the description of a role.

        :param request: Request instance for UpdateRoleDescription.
        :type request: :class:`tencentcloud.cam.v20190116.models.UpdateRoleDescriptionRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.UpdateRoleDescriptionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateRoleDescription", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateRoleDescriptionResponse()
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


    def UpdateSAMLProvider(self, request):
        """This API is used to update SAML identity provider information.

        :param request: Request instance for UpdateSAMLProvider.
        :type request: :class:`tencentcloud.cam.v20190116.models.UpdateSAMLProviderRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.UpdateSAMLProviderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateSAMLProvider", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateSAMLProviderResponse()
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


    def UpdateUser(self, request):
        """This API is used to update a sub-user.

        :param request: Request instance for UpdateUser.
        :type request: :class:`tencentcloud.cam.v20190116.models.UpdateUserRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.UpdateUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateUser", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateUserResponse()
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


    def UpdateUserOIDCConfig(self, request):
        """This API is used to modify the user OIDC configuration.

        :param request: Request instance for UpdateUserOIDCConfig.
        :type request: :class:`tencentcloud.cam.v20190116.models.UpdateUserOIDCConfigRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.UpdateUserOIDCConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateUserOIDCConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateUserOIDCConfigResponse()
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


    def UpdateUserSAMLConfig(self, request):
        """This API is used to modify user SAML configurations.

        :param request: Request instance for UpdateUserSAMLConfig.
        :type request: :class:`tencentcloud.cam.v20190116.models.UpdateUserSAMLConfigRequest`
        :rtype: :class:`tencentcloud.cam.v20190116.models.UpdateUserSAMLConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateUserSAMLConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateUserSAMLConfigResponse()
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