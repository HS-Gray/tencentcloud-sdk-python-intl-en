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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class AccessKey(AbstractModel):
    """Access key list

    """

    def __init__(self):
        """
        :param AccessKeyId: Access key ID\n        :type AccessKeyId: str\n        :param Status: Key status. Valid values: Active (activated), Inactive (not activated)\n        :type Status: str\n        :param CreateTime: Creation time\n        :type CreateTime: str\n        """
        self.AccessKeyId = None
        self.Status = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.AccessKeyId = params.get("AccessKeyId")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddUserRequest(AbstractModel):
    """AddUser request structure.

    """

    def __init__(self):
        """
        :param Name: Sub-user username\n        :type Name: str\n        :param Remark: Sub-user remarks\n        :type Remark: str\n        :param ConsoleLogin: Whether or not the sub-user is allowed to log in to the console. 0: No; 1: Yes.\n        :type ConsoleLogin: int\n        :param UseApi: Whether or not to generate keys for sub-users. 0: No; 1: Yes.\n        :type UseApi: int\n        :param Password: Sub-user's console login password. If no password rules have been set, the password must have a minimum of 8 characters containing uppercase letters, lowercase letters, digits, and special characters by default. This parameter will be valid only when the sub-user is allowed to log in to the console. If it is not specified and console login is allowed, the system will automatically generate a random 32-character password that contains uppercase letters, lowercase letters, digits, and special characters.\n        :type Password: str\n        :param NeedResetPassword: If the sub-user needs to reset their password when they next log in to the console. 0: No; 1: Yes.\n        :type NeedResetPassword: int\n        :param PhoneNum: Mobile number\n        :type PhoneNum: str\n        :param CountryCode: Country/Area Code\n        :type CountryCode: str\n        :param Email: Email\n        :type Email: str\n        """
        self.Name = None
        self.Remark = None
        self.ConsoleLogin = None
        self.UseApi = None
        self.Password = None
        self.NeedResetPassword = None
        self.PhoneNum = None
        self.CountryCode = None
        self.Email = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Remark = params.get("Remark")
        self.ConsoleLogin = params.get("ConsoleLogin")
        self.UseApi = params.get("UseApi")
        self.Password = params.get("Password")
        self.NeedResetPassword = params.get("NeedResetPassword")
        self.PhoneNum = params.get("PhoneNum")
        self.CountryCode = params.get("CountryCode")
        self.Email = params.get("Email")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddUserResponse(AbstractModel):
    """AddUser response structure.

    """

    def __init__(self):
        """
        :param Uin: Sub-user UIN\n        :type Uin: int\n        :param Name: Sub-user username\n        :type Name: str\n        :param Password: If the combination of input parameters indicates that a random password should be generated, the generated password is returned\n        :type Password: str\n        :param SecretId: Sub-user's key ID\n        :type SecretId: str\n        :param SecretKey: Sub-user's secret key\n        :type SecretKey: str\n        :param Uid: Sub-user UID\n        :type Uid: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Uin = None
        self.Name = None
        self.Password = None
        self.SecretId = None
        self.SecretKey = None
        self.Uid = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.Name = params.get("Name")
        self.Password = params.get("Password")
        self.SecretId = params.get("SecretId")
        self.SecretKey = params.get("SecretKey")
        self.Uid = params.get("Uid")
        self.RequestId = params.get("RequestId")


class AddUserToGroupRequest(AbstractModel):
    """AddUserToGroup request structure.

    """

    def __init__(self):
        """
        :param Info: How sub-user UIDs are associated with the ID of the user group they are added to.\n        :type Info: list of GroupIdOfUidInfo\n        """
        self.Info = None


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self.Info = []
            for item in params.get("Info"):
                obj = GroupIdOfUidInfo()
                obj._deserialize(item)
                self.Info.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddUserToGroupResponse(AbstractModel):
    """AddUserToGroup response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AttachEntityOfPolicy(AbstractModel):
    """The entity associated with the policy

    """

    def __init__(self):
        """
        :param Id: Entity ID\n        :type Id: str\n        :param Name: Entity Name
Note: This field may return null, indicating that no valid value was found.\n        :type Name: str\n        :param Uin: Entity UIN
Note: This field may return null, indicating that no valid value was found.\n        :type Uin: int\n        :param RelatedType: Type of entity association. 1: Associate by users; 2: Associate by User Groups\n        :type RelatedType: int\n        :param AttachmentTime: Policy association time
Note: this field may return `null`, indicating that no valid value was found.\n        :type AttachmentTime: str\n        """
        self.Id = None
        self.Name = None
        self.Uin = None
        self.RelatedType = None
        self.AttachmentTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Uin = params.get("Uin")
        self.RelatedType = params.get("RelatedType")
        self.AttachmentTime = params.get("AttachmentTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachGroupPolicyRequest(AbstractModel):
    """AttachGroupPolicy request structure.

    """

    def __init__(self):
        """
        :param PolicyId: Policy ID\n        :type PolicyId: int\n        :param AttachGroupId: User Group ID\n        :type AttachGroupId: int\n        """
        self.PolicyId = None
        self.AttachGroupId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.AttachGroupId = params.get("AttachGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachGroupPolicyResponse(AbstractModel):
    """AttachGroupPolicy response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AttachPolicyInfo(AbstractModel):
    """Associated policy

    """

    def __init__(self):
        """
        :param PolicyId: Policy ID\n        :type PolicyId: int\n        :param PolicyName: Policy name
Note: This field may return null, indicating that no valid value was found.\n        :type PolicyName: str\n        :param AddTime: Time created
Note: This field may return null, indicating that no valid value was found.\n        :type AddTime: str\n        :param CreateMode: How the policy was created: 1: Via console; 2: Via syntax
Note: This field may return null, indicating that no valid value was found.\n        :type CreateMode: int\n        :param PolicyType: Valid values: `user` and `QCS`
Note: This field may return null, indicating that no valid value was found.\n        :type PolicyType: str\n        :param Remark: Policy remarks\n        :type Remark: str\n        :param OperateOwnerUin: Root account of the operator associating the policy
Note: this field may return null, indicating that no valid values can be obtained.\n        :type OperateOwnerUin: str\n        :param OperateUin: The ID of the account associating the policy. If `UinType` is 0, this indicates that this is a sub-account `UIN`. If `UinType` is 1, this indicates this is a role ID\n        :type OperateUin: str\n        :param OperateUinType: If `UinType` is 0, `OperateUin` indicates that this is a sub-account `UIN`. If `UinType` is 1, `OperateUin` indicates that this is a role ID\n        :type OperateUinType: int\n        :param Deactived: Queries if the policy has been deactivated
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Deactived: int\n        :param DeactivedDetail: List of deprecated products
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DeactivedDetail: list of str\n        """
        self.PolicyId = None
        self.PolicyName = None
        self.AddTime = None
        self.CreateMode = None
        self.PolicyType = None
        self.Remark = None
        self.OperateOwnerUin = None
        self.OperateUin = None
        self.OperateUinType = None
        self.Deactived = None
        self.DeactivedDetail = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.PolicyName = params.get("PolicyName")
        self.AddTime = params.get("AddTime")
        self.CreateMode = params.get("CreateMode")
        self.PolicyType = params.get("PolicyType")
        self.Remark = params.get("Remark")
        self.OperateOwnerUin = params.get("OperateOwnerUin")
        self.OperateUin = params.get("OperateUin")
        self.OperateUinType = params.get("OperateUinType")
        self.Deactived = params.get("Deactived")
        self.DeactivedDetail = params.get("DeactivedDetail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachRolePolicyRequest(AbstractModel):
    """AttachRolePolicy request structure.

    """

    def __init__(self):
        """
        :param PolicyId: Policy ID. Either `PolicyId` or `PolicyName` must be entered\n        :type PolicyId: int\n        :param AttachRoleId: Role ID, used to specify a role. Input either `AttachRoleId` or `AttachRoleName`\n        :type AttachRoleId: str\n        :param AttachRoleName: Role name, used to specify a role. Input either `AttachRoleId` or `AttachRoleName`\n        :type AttachRoleName: str\n        :param PolicyName: Policy name. Either `PolicyId` or `PolicyName` must be entered\n        :type PolicyName: str\n        """
        self.PolicyId = None
        self.AttachRoleId = None
        self.AttachRoleName = None
        self.PolicyName = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.AttachRoleId = params.get("AttachRoleId")
        self.AttachRoleName = params.get("AttachRoleName")
        self.PolicyName = params.get("PolicyName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachRolePolicyResponse(AbstractModel):
    """AttachRolePolicy response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AttachUserPolicyRequest(AbstractModel):
    """AttachUserPolicy request structure.

    """

    def __init__(self):
        """
        :param PolicyId: Policy ID\n        :type PolicyId: int\n        :param AttachUin: Sub-account UIN\n        :type AttachUin: int\n        """
        self.PolicyId = None
        self.AttachUin = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.AttachUin = params.get("AttachUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachUserPolicyResponse(AbstractModel):
    """AttachUserPolicy response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AttachedPolicyOfRole(AbstractModel):
    """Policy associated with the role

    """

    def __init__(self):
        """
        :param PolicyId: Policy ID\n        :type PolicyId: int\n        :param PolicyName: Policy name\n        :type PolicyName: str\n        :param AddTime: Time of association\n        :type AddTime: str\n        :param PolicyType: Policy type. `User` indicates custom policy; `QCS` indicates preset policy
Note: This field may return null, indicating that no valid value was found.\n        :type PolicyType: str\n        :param CreateMode: Policy creation method. 1: indicates the policy was created based on product function or item permission; other values indicate the policy was created based on the policy syntax\n        :type CreateMode: int\n        :param Deactived: Whether the product has been deprecated (0: no; 1: yes)
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Deactived: int\n        :param DeactivedDetail: List of deprecated products
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DeactivedDetail: list of str\n        :param Description: Policy description
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Description: str\n        """
        self.PolicyId = None
        self.PolicyName = None
        self.AddTime = None
        self.PolicyType = None
        self.CreateMode = None
        self.Deactived = None
        self.DeactivedDetail = None
        self.Description = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.PolicyName = params.get("PolicyName")
        self.AddTime = params.get("AddTime")
        self.PolicyType = params.get("PolicyType")
        self.CreateMode = params.get("CreateMode")
        self.Deactived = params.get("Deactived")
        self.DeactivedDetail = params.get("DeactivedDetail")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumeCustomMFATokenRequest(AbstractModel):
    """ConsumeCustomMFAToken request structure.

    """

    def __init__(self):
        """
        :param MFAToken: Custom multi-factor verification Token\n        :type MFAToken: str\n        """
        self.MFAToken = None


    def _deserialize(self, params):
        self.MFAToken = params.get("MFAToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumeCustomMFATokenResponse(AbstractModel):
    """ConsumeCustomMFAToken response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateGroupRequest(AbstractModel):
    """CreateGroup request structure.

    """

    def __init__(self):
        """
        :param GroupName: User Group name\n        :type GroupName: str\n        :param Remark: User Group description\n        :type Remark: str\n        """
        self.GroupName = None
        self.Remark = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGroupResponse(AbstractModel):
    """CreateGroup response structure.

    """

    def __init__(self):
        """
        :param GroupId: User Group ID\n        :type GroupId: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.GroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.RequestId = params.get("RequestId")


class CreatePolicyRequest(AbstractModel):
    """CreatePolicy request structure.

    """

    def __init__(self):
        """
        :param PolicyName: Policy name\n        :type PolicyName: str\n        :param PolicyDocument: Policy document, such as `{"version":"2.0","statement":[{"action":"name/sts:AssumeRole","effect":"allow","principal":{"service":["cloudaudit.cloud.tencent.com","cls.cloud.tencent.com"]}}]}`, where `principal` is used to specify the resources that the role is authorized to access. For more information on this parameter, please see the `RoleInfo` output parameter of the [GetRole](https://intl.cloud.tencent.com/document/product/598/36221?from_cn_redirect=1) API\n        :type PolicyDocument: str\n        :param Description: Policy description\n        :type Description: str\n        """
        self.PolicyName = None
        self.PolicyDocument = None
        self.Description = None


    def _deserialize(self, params):
        self.PolicyName = params.get("PolicyName")
        self.PolicyDocument = params.get("PolicyDocument")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePolicyResponse(AbstractModel):
    """CreatePolicy response structure.

    """

    def __init__(self):
        """
        :param PolicyId: ID of newly added policy\n        :type PolicyId: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.PolicyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.RequestId = params.get("RequestId")


class CreatePolicyVersionRequest(AbstractModel):
    """CreatePolicyVersion request structure.

    """

    def __init__(self):
        """
        :param PolicyId: Policy ID\n        :type PolicyId: int\n        :param PolicyDocument: The policy document to use as the content for the new version\n        :type PolicyDocument: str\n        :param SetAsDefault: Specifies whether to set this version as the default version\n        :type SetAsDefault: bool\n        """
        self.PolicyId = None
        self.PolicyDocument = None
        self.SetAsDefault = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.PolicyDocument = params.get("PolicyDocument")
        self.SetAsDefault = params.get("SetAsDefault")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePolicyVersionResponse(AbstractModel):
    """CreatePolicyVersion response structure.

    """

    def __init__(self):
        """
        :param VersionId: Policy version ID
Note: this field may return null, indicating that no valid values can be obtained.\n        :type VersionId: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.VersionId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.VersionId = params.get("VersionId")
        self.RequestId = params.get("RequestId")


class CreateRoleRequest(AbstractModel):
    """CreateRole request structure.

    """

    def __init__(self):
        """
        :param RoleName: Role name\n        :type RoleName: str\n        :param PolicyDocument: Policy document\n        :type PolicyDocument: str\n        :param Description: Role description\n        :type Description: str\n        :param ConsoleLogin: Whether login is allowed. 1: yes, 0: no\n        :type ConsoleLogin: int\n        :param SessionDuration: The maximum validity period of the temporary key for creating a role (range: 0-43200)\n        :type SessionDuration: int\n        """
        self.RoleName = None
        self.PolicyDocument = None
        self.Description = None
        self.ConsoleLogin = None
        self.SessionDuration = None


    def _deserialize(self, params):
        self.RoleName = params.get("RoleName")
        self.PolicyDocument = params.get("PolicyDocument")
        self.Description = params.get("Description")
        self.ConsoleLogin = params.get("ConsoleLogin")
        self.SessionDuration = params.get("SessionDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRoleResponse(AbstractModel):
    """CreateRole response structure.

    """

    def __init__(self):
        """
        :param RoleId: Role ID
Note: This field may return null, indicating that no valid value was found.\n        :type RoleId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RoleId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RoleId = params.get("RoleId")
        self.RequestId = params.get("RequestId")


class CreateSAMLProviderRequest(AbstractModel):
    """CreateSAMLProvider request structure.

    """

    def __init__(self):
        """
        :param Name: SAML identity provider name\n        :type Name: str\n        :param Description: SAML identity provider description\n        :type Description: str\n        :param SAMLMetadataDocument: SAML identity provider metadata document (Base64)\n        :type SAMLMetadataDocument: str\n        """
        self.Name = None
        self.Description = None
        self.SAMLMetadataDocument = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.SAMLMetadataDocument = params.get("SAMLMetadataDocument")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSAMLProviderResponse(AbstractModel):
    """CreateSAMLProvider response structure.

    """

    def __init__(self):
        """
        :param ProviderArn: SAML identity provider resource descriptor\n        :type ProviderArn: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.ProviderArn = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProviderArn = params.get("ProviderArn")
        self.RequestId = params.get("RequestId")


class CreateServiceLinkedRoleRequest(AbstractModel):
    """CreateServiceLinkedRole request structure.

    """

    def __init__(self):
        """
        :param QCSServiceName: Authorized service, i.e., Tencent Cloud service entity with this role attached.\n        :type QCSServiceName: list of str\n        :param CustomSuffix: Custom suffix. A string you provide, which is combined with the service-provided prefix to form the complete role name.\n        :type CustomSuffix: str\n        :param Description: Role description.\n        :type Description: str\n        """
        self.QCSServiceName = None
        self.CustomSuffix = None
        self.Description = None


    def _deserialize(self, params):
        self.QCSServiceName = params.get("QCSServiceName")
        self.CustomSuffix = params.get("CustomSuffix")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateServiceLinkedRoleResponse(AbstractModel):
    """CreateServiceLinkedRole response structure.

    """

    def __init__(self):
        """
        :param RoleId: Role ID\n        :type RoleId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RoleId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RoleId = params.get("RoleId")
        self.RequestId = params.get("RequestId")


class DeleteGroupRequest(AbstractModel):
    """DeleteGroup request structure.

    """

    def __init__(self):
        """
        :param GroupId: User Group ID\n        :type GroupId: int\n        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteGroupResponse(AbstractModel):
    """DeleteGroup response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeletePolicyRequest(AbstractModel):
    """DeletePolicy request structure.

    """

    def __init__(self):
        """
        :param PolicyId: Array. Array elements are policy IDs. Policies can be deleted in a batch\n        :type PolicyId: list of int non-negative\n        """
        self.PolicyId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePolicyResponse(AbstractModel):
    """DeletePolicy response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeletePolicyVersionRequest(AbstractModel):
    """DeletePolicyVersion request structure.

    """

    def __init__(self):
        """
        :param PolicyId: Policy ID\n        :type PolicyId: int\n        :param VersionId: Policy version ID\n        :type VersionId: list of int non-negative\n        """
        self.PolicyId = None
        self.VersionId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.VersionId = params.get("VersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePolicyVersionResponse(AbstractModel):
    """DeletePolicyVersion response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRolePermissionsBoundaryRequest(AbstractModel):
    """DeleteRolePermissionsBoundary request structure.

    """

    def __init__(self):
        """
        :param RoleId: Role ID (either it or the role name must be entered)\n        :type RoleId: str\n        :param RoleName: Role name (either it or the role ID must be entered)\n        :type RoleName: str\n        """
        self.RoleId = None
        self.RoleName = None


    def _deserialize(self, params):
        self.RoleId = params.get("RoleId")
        self.RoleName = params.get("RoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRolePermissionsBoundaryResponse(AbstractModel):
    """DeleteRolePermissionsBoundary response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRoleRequest(AbstractModel):
    """DeleteRole request structure.

    """

    def __init__(self):
        """
        :param RoleId: Role ID, used to specify a role. Input either `RoleId` or `RoleName`\n        :type RoleId: str\n        :param RoleName: Role name, used to specify a role. Input either `RoleId` or `RoleName`\n        :type RoleName: str\n        """
        self.RoleId = None
        self.RoleName = None


    def _deserialize(self, params):
        self.RoleId = params.get("RoleId")
        self.RoleName = params.get("RoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRoleResponse(AbstractModel):
    """DeleteRole response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSAMLProviderRequest(AbstractModel):
    """DeleteSAMLProvider request structure.

    """

    def __init__(self):
        """
        :param Name: SAML identity provider name\n        :type Name: str\n        """
        self.Name = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSAMLProviderResponse(AbstractModel):
    """DeleteSAMLProvider response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteServiceLinkedRoleRequest(AbstractModel):
    """DeleteServiceLinkedRole request structure.

    """

    def __init__(self):
        """
        :param RoleName: Name of the service-linked role to be deleted.\n        :type RoleName: str\n        """
        self.RoleName = None


    def _deserialize(self, params):
        self.RoleName = params.get("RoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteServiceLinkedRoleResponse(AbstractModel):
    """DeleteServiceLinkedRole response structure.

    """

    def __init__(self):
        """
        :param DeletionTaskId: Deletion task identifier, which can be used to check the status of a service-linked role deletion.\n        :type DeletionTaskId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.DeletionTaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DeletionTaskId = params.get("DeletionTaskId")
        self.RequestId = params.get("RequestId")


class DeleteUserPermissionsBoundaryRequest(AbstractModel):
    """DeleteUserPermissionsBoundary request structure.

    """

    def __init__(self):
        """
        :param TargetUin: Sub-account `Uin`\n        :type TargetUin: int\n        """
        self.TargetUin = None


    def _deserialize(self, params):
        self.TargetUin = params.get("TargetUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUserPermissionsBoundaryResponse(AbstractModel):
    """DeleteUserPermissionsBoundary response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteUserRequest(AbstractModel):
    """DeleteUser request structure.

    """

    def __init__(self):
        """
        :param Name: Sub-user username\n        :type Name: str\n        :param Force: Whether to forcibly delete the sub-user. The default input parameter is `0`. `0`: do not delete the user if the user has undeleted API keys; `1`: first delete the API keys then delete the user if the user has undeleted API keys. To delete API keys, you need to have cam:DeleteApiKey permission, which enables you to delete both enabled and disabled API keys. If you do not have this permission, you will not be able to delete API keys and the user.\n        :type Force: int\n        """
        self.Name = None
        self.Force = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Force = params.get("Force")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUserResponse(AbstractModel):
    """DeleteUser response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeRoleListRequest(AbstractModel):
    """DescribeRoleList request structure.

    """

    def __init__(self):
        """
        :param Page: Page number, beginning from 1\n        :type Page: int\n        :param Rp: Number of lines per page, no greater than 200\n        :type Rp: int\n        """
        self.Page = None
        self.Rp = None


    def _deserialize(self, params):
        self.Page = params.get("Page")
        self.Rp = params.get("Rp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRoleListResponse(AbstractModel):
    """DescribeRoleList response structure.

    """

    def __init__(self):
        """
        :param List: Role details list
Note: This field may return null, indicating that no valid value was found.\n        :type List: list of RoleInfo\n        :param TotalNum: Total number of roles\n        :type TotalNum: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.List = None
        self.TotalNum = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = RoleInfo()
                obj._deserialize(item)
                self.List.append(obj)
        self.TotalNum = params.get("TotalNum")
        self.RequestId = params.get("RequestId")


class DescribeSafeAuthFlagCollRequest(AbstractModel):
    """DescribeSafeAuthFlagColl request structure.

    """

    def __init__(self):
        """
        :param SubUin: Sub-account\n        :type SubUin: int\n        """
        self.SubUin = None


    def _deserialize(self, params):
        self.SubUin = params.get("SubUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSafeAuthFlagCollResponse(AbstractModel):
    """DescribeSafeAuthFlagColl response structure.

    """

    def __init__(self):
        """
        :param LoginFlag: Login protection settings\n        :type LoginFlag: :class:`tencentcloud.cam.v20190116.models.LoginActionFlag`\n        :param ActionFlag: Sensitive operation protection settings\n        :type ActionFlag: :class:`tencentcloud.cam.v20190116.models.LoginActionFlag`\n        :param OffsiteFlag: Suspicious login location protection settings\n        :type OffsiteFlag: :class:`tencentcloud.cam.v20190116.models.OffsiteFlag`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.LoginFlag = None
        self.ActionFlag = None
        self.OffsiteFlag = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LoginFlag") is not None:
            self.LoginFlag = LoginActionFlag()
            self.LoginFlag._deserialize(params.get("LoginFlag"))
        if params.get("ActionFlag") is not None:
            self.ActionFlag = LoginActionFlag()
            self.ActionFlag._deserialize(params.get("ActionFlag"))
        if params.get("OffsiteFlag") is not None:
            self.OffsiteFlag = OffsiteFlag()
            self.OffsiteFlag._deserialize(params.get("OffsiteFlag"))
        self.RequestId = params.get("RequestId")


class DescribeSafeAuthFlagIntlRequest(AbstractModel):
    """DescribeSafeAuthFlagIntl request structure.

    """


class DescribeSafeAuthFlagIntlResponse(AbstractModel):
    """DescribeSafeAuthFlagIntl response structure.

    """

    def __init__(self):
        """
        :param LoginFlag: Login protection settings\n        :type LoginFlag: :class:`tencentcloud.cam.v20190116.models.LoginActionFlagIntl`\n        :param ActionFlag: Sensitive operation protection settings\n        :type ActionFlag: :class:`tencentcloud.cam.v20190116.models.LoginActionFlagIntl`\n        :param OffsiteFlag: Suspicious login location protection settings\n        :type OffsiteFlag: :class:`tencentcloud.cam.v20190116.models.OffsiteFlag`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.LoginFlag = None
        self.ActionFlag = None
        self.OffsiteFlag = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LoginFlag") is not None:
            self.LoginFlag = LoginActionFlagIntl()
            self.LoginFlag._deserialize(params.get("LoginFlag"))
        if params.get("ActionFlag") is not None:
            self.ActionFlag = LoginActionFlagIntl()
            self.ActionFlag._deserialize(params.get("ActionFlag"))
        if params.get("OffsiteFlag") is not None:
            self.OffsiteFlag = OffsiteFlag()
            self.OffsiteFlag._deserialize(params.get("OffsiteFlag"))
        self.RequestId = params.get("RequestId")


class DescribeSafeAuthFlagRequest(AbstractModel):
    """DescribeSafeAuthFlag request structure.

    """


class DescribeSafeAuthFlagResponse(AbstractModel):
    """DescribeSafeAuthFlag response structure.

    """

    def __init__(self):
        """
        :param LoginFlag: Login protection settings\n        :type LoginFlag: :class:`tencentcloud.cam.v20190116.models.LoginActionFlag`\n        :param ActionFlag: Sensitive operation protection settings\n        :type ActionFlag: :class:`tencentcloud.cam.v20190116.models.LoginActionFlag`\n        :param OffsiteFlag: Suspicious login location protection settings\n        :type OffsiteFlag: :class:`tencentcloud.cam.v20190116.models.OffsiteFlag`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.LoginFlag = None
        self.ActionFlag = None
        self.OffsiteFlag = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LoginFlag") is not None:
            self.LoginFlag = LoginActionFlag()
            self.LoginFlag._deserialize(params.get("LoginFlag"))
        if params.get("ActionFlag") is not None:
            self.ActionFlag = LoginActionFlag()
            self.ActionFlag._deserialize(params.get("ActionFlag"))
        if params.get("OffsiteFlag") is not None:
            self.OffsiteFlag = OffsiteFlag()
            self.OffsiteFlag._deserialize(params.get("OffsiteFlag"))
        self.RequestId = params.get("RequestId")


class DescribeSubAccountsRequest(AbstractModel):
    """DescribeSubAccounts request structure.

    """

    def __init__(self):
        """
        :param FilterSubAccountUin: List of sub-user UINs. Up to 50 UINs are supported.\n        :type FilterSubAccountUin: list of int non-negative\n        """
        self.FilterSubAccountUin = None


    def _deserialize(self, params):
        self.FilterSubAccountUin = params.get("FilterSubAccountUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSubAccountsResponse(AbstractModel):
    """DescribeSubAccounts response structure.

    """

    def __init__(self):
        """
        :param SubAccounts: Sub-user list\n        :type SubAccounts: list of SubAccountUser\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.SubAccounts = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SubAccounts") is not None:
            self.SubAccounts = []
            for item in params.get("SubAccounts"):
                obj = SubAccountUser()
                obj._deserialize(item)
                self.SubAccounts.append(obj)
        self.RequestId = params.get("RequestId")


class DetachGroupPolicyRequest(AbstractModel):
    """DetachGroupPolicy request structure.

    """

    def __init__(self):
        """
        :param PolicyId: Policy ID\n        :type PolicyId: int\n        :param DetachGroupId: User Group ID\n        :type DetachGroupId: int\n        """
        self.PolicyId = None
        self.DetachGroupId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.DetachGroupId = params.get("DetachGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachGroupPolicyResponse(AbstractModel):
    """DetachGroupPolicy response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DetachRolePolicyRequest(AbstractModel):
    """DetachRolePolicy request structure.

    """

    def __init__(self):
        """
        :param PolicyId: Policy ID. Either `PolicyId` or `PolicyName` must be entered\n        :type PolicyId: int\n        :param DetachRoleId: Role ID, used to specify a role. Input either `AttachRoleId` or `AttachRoleName`\n        :type DetachRoleId: str\n        :param DetachRoleName: Role name, used to specify a role. Input either `AttachRoleId` or `AttachRoleName`\n        :type DetachRoleName: str\n        :param PolicyName: Policy name. Either `PolicyId` or `PolicyName` must be entered\n        :type PolicyName: str\n        """
        self.PolicyId = None
        self.DetachRoleId = None
        self.DetachRoleName = None
        self.PolicyName = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.DetachRoleId = params.get("DetachRoleId")
        self.DetachRoleName = params.get("DetachRoleName")
        self.PolicyName = params.get("PolicyName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachRolePolicyResponse(AbstractModel):
    """DetachRolePolicy response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DetachUserPolicyRequest(AbstractModel):
    """DetachUserPolicy request structure.

    """

    def __init__(self):
        """
        :param PolicyId: Policy ID\n        :type PolicyId: int\n        :param DetachUin: Sub-account UIN\n        :type DetachUin: int\n        """
        self.PolicyId = None
        self.DetachUin = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.DetachUin = params.get("DetachUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachUserPolicyResponse(AbstractModel):
    """DetachUserPolicy response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class GetAccountSummaryRequest(AbstractModel):
    """GetAccountSummary request structure.

    """


class GetAccountSummaryResponse(AbstractModel):
    """GetAccountSummary response structure.

    """

    def __init__(self):
        """
        :param Policies: Number of policies\n        :type Policies: int\n        :param Roles: Number of roles\n        :type Roles: int\n        :param Idps: Number of identity providers\n        :type Idps: int\n        :param User: Number of sub-accounts\n        :type User: int\n        :param Group: Number of groups\n        :type Group: int\n        :param Member: Total number of grouped users\n        :type Member: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Policies = None
        self.Roles = None
        self.Idps = None
        self.User = None
        self.Group = None
        self.Member = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Policies = params.get("Policies")
        self.Roles = params.get("Roles")
        self.Idps = params.get("Idps")
        self.User = params.get("User")
        self.Group = params.get("Group")
        self.Member = params.get("Member")
        self.RequestId = params.get("RequestId")


class GetCustomMFATokenInfoRequest(AbstractModel):
    """GetCustomMFATokenInfo request structure.

    """

    def __init__(self):
        """
        :param MFAToken: Custom multi-factor verification Token\n        :type MFAToken: str\n        """
        self.MFAToken = None


    def _deserialize(self, params):
        self.MFAToken = params.get("MFAToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetCustomMFATokenInfoResponse(AbstractModel):
    """GetCustomMFATokenInfo response structure.

    """

    def __init__(self):
        """
        :param Uin: Account ID corresponding to the custom multi-factor verification Token\n        :type Uin: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Uin = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.RequestId = params.get("RequestId")


class GetGroupRequest(AbstractModel):
    """GetGroup request structure.

    """

    def __init__(self):
        """
        :param GroupId: User Group ID\n        :type GroupId: int\n        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetGroupResponse(AbstractModel):
    """GetGroup response structure.

    """

    def __init__(self):
        """
        :param GroupId: User Group ID\n        :type GroupId: int\n        :param GroupName: User Group name\n        :type GroupName: str\n        :param GroupNum: Number of members in the User Group\n        :type GroupNum: int\n        :param Remark: User Group description\n        :type Remark: str\n        :param CreateTime: Time User Group created\n        :type CreateTime: str\n        :param UserInfo: User Group member information\n        :type UserInfo: list of GroupMemberInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.GroupId = None
        self.GroupName = None
        self.GroupNum = None
        self.Remark = None
        self.CreateTime = None
        self.UserInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.GroupNum = params.get("GroupNum")
        self.Remark = params.get("Remark")
        self.CreateTime = params.get("CreateTime")
        if params.get("UserInfo") is not None:
            self.UserInfo = []
            for item in params.get("UserInfo"):
                obj = GroupMemberInfo()
                obj._deserialize(item)
                self.UserInfo.append(obj)
        self.RequestId = params.get("RequestId")


class GetPolicyRequest(AbstractModel):
    """GetPolicy request structure.

    """

    def __init__(self):
        """
        :param PolicyId: Policy ID\n        :type PolicyId: int\n        """
        self.PolicyId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetPolicyResponse(AbstractModel):
    """GetPolicy response structure.

    """

    def __init__(self):
        """
        :param PolicyName: Policy name
Note: This field may return null, indicating that no valid value was found.\n        :type PolicyName: str\n        :param Description: Policy description
Note: This field may return null, indicating that no valid value was found.\n        :type Description: str\n        :param Type: 1: Custom policy; 2: Preset policy
Note: This field may return null, indicating that no valid value was found.\n        :type Type: int\n        :param AddTime: Time created
Note: This field may return null, indicating that no valid value was found.\n        :type AddTime: str\n        :param UpdateTime: Time of latest update
Note: This field may return null, indicating that no valid value was found.\n        :type UpdateTime: str\n        :param PolicyDocument: Policy document
Note: This field may return null, indicating that no valid value was found.\n        :type PolicyDocument: str\n        :param PresetAlias: Remarks
Note: this field may return null, indicating that no valid values can be obtained.\n        :type PresetAlias: str\n        :param IsServiceLinkedRolePolicy: Whether it is a service-linked policy
Note: this field may return null, indicating that no valid values can be obtained.\n        :type IsServiceLinkedRolePolicy: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.PolicyName = None
        self.Description = None
        self.Type = None
        self.AddTime = None
        self.UpdateTime = None
        self.PolicyDocument = None
        self.PresetAlias = None
        self.IsServiceLinkedRolePolicy = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PolicyName = params.get("PolicyName")
        self.Description = params.get("Description")
        self.Type = params.get("Type")
        self.AddTime = params.get("AddTime")
        self.UpdateTime = params.get("UpdateTime")
        self.PolicyDocument = params.get("PolicyDocument")
        self.PresetAlias = params.get("PresetAlias")
        self.IsServiceLinkedRolePolicy = params.get("IsServiceLinkedRolePolicy")
        self.RequestId = params.get("RequestId")


class GetPolicyVersionRequest(AbstractModel):
    """GetPolicyVersion request structure.

    """

    def __init__(self):
        """
        :param PolicyId: Policy ID\n        :type PolicyId: int\n        :param VersionId: Policy version ID\n        :type VersionId: int\n        """
        self.PolicyId = None
        self.VersionId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.VersionId = params.get("VersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetPolicyVersionResponse(AbstractModel):
    """GetPolicyVersion response structure.

    """

    def __init__(self):
        """
        :param PolicyVersion: Policy version details
Note: this field may return null, indicating that no valid values can be obtained.\n        :type PolicyVersion: :class:`tencentcloud.cam.v20190116.models.PolicyVersionDetail`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.PolicyVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PolicyVersion") is not None:
            self.PolicyVersion = PolicyVersionDetail()
            self.PolicyVersion._deserialize(params.get("PolicyVersion"))
        self.RequestId = params.get("RequestId")


class GetRoleRequest(AbstractModel):
    """GetRole request structure.

    """

    def __init__(self):
        """
        :param RoleId: Role ID, used to specify role. Input either `RoleId` or `RoleName`\n        :type RoleId: str\n        :param RoleName: Role name, used to specify role. Input either `RoleId` or `RoleName`\n        :type RoleName: str\n        """
        self.RoleId = None
        self.RoleName = None


    def _deserialize(self, params):
        self.RoleId = params.get("RoleId")
        self.RoleName = params.get("RoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRoleResponse(AbstractModel):
    """GetRole response structure.

    """

    def __init__(self):
        """
        :param RoleInfo: Role details\n        :type RoleInfo: :class:`tencentcloud.cam.v20190116.models.RoleInfo`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RoleInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RoleInfo") is not None:
            self.RoleInfo = RoleInfo()
            self.RoleInfo._deserialize(params.get("RoleInfo"))
        self.RequestId = params.get("RequestId")


class GetSAMLProviderRequest(AbstractModel):
    """GetSAMLProvider request structure.

    """

    def __init__(self):
        """
        :param Name: SAML identity provider name\n        :type Name: str\n        """
        self.Name = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetSAMLProviderResponse(AbstractModel):
    """GetSAMLProvider response structure.

    """

    def __init__(self):
        """
        :param Name: SAML identity provider name\n        :type Name: str\n        :param Description: SAML identity provider description\n        :type Description: str\n        :param CreateTime: Time SAML identity provider created\n        :type CreateTime: str\n        :param ModifyTime: Time SAML identity provider last modified\n        :type ModifyTime: str\n        :param SAMLMetadata: SAML identity provider metadata document\n        :type SAMLMetadata: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Name = None
        self.Description = None
        self.CreateTime = None
        self.ModifyTime = None
        self.SAMLMetadata = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.CreateTime = params.get("CreateTime")
        self.ModifyTime = params.get("ModifyTime")
        self.SAMLMetadata = params.get("SAMLMetadata")
        self.RequestId = params.get("RequestId")


class GetSecurityLastUsedRequest(AbstractModel):
    """GetSecurityLastUsed request structure.

    """

    def __init__(self):
        """
        :param SecretIdList: A parameter used to query the key ID list.\n        :type SecretIdList: list of str\n        """
        self.SecretIdList = None


    def _deserialize(self, params):
        self.SecretIdList = params.get("SecretIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetSecurityLastUsedResponse(AbstractModel):
    """GetSecurityLastUsed response structure.

    """

    def __init__(self):
        """
        :param SecretIdLastUsedRows: List of key ID’s recent usage records.\n        :type SecretIdLastUsedRows: list of SecretIdLastUsed\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.SecretIdLastUsedRows = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SecretIdLastUsedRows") is not None:
            self.SecretIdLastUsedRows = []
            for item in params.get("SecretIdLastUsedRows"):
                obj = SecretIdLastUsed()
                obj._deserialize(item)
                self.SecretIdLastUsedRows.append(obj)
        self.RequestId = params.get("RequestId")


class GetServiceLinkedRoleDeletionStatusRequest(AbstractModel):
    """GetServiceLinkedRoleDeletionStatus request structure.

    """

    def __init__(self):
        """
        :param DeletionTaskId: Deletion task ID\n        :type DeletionTaskId: str\n        """
        self.DeletionTaskId = None


    def _deserialize(self, params):
        self.DeletionTaskId = params.get("DeletionTaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetServiceLinkedRoleDeletionStatusResponse(AbstractModel):
    """GetServiceLinkedRoleDeletionStatus response structure.

    """

    def __init__(self):
        """
        :param Status: Status: NOT_STARTED, IN_PROGRESS, SUCCEEDED, FAILED\n        :type Status: str\n        :param Reason: Reasons why the deletion failed.\n        :type Reason: str\n        :param ServiceType: Service type
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ServiceType: str\n        :param ServiceName: Service name
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ServiceName: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Status = None
        self.Reason = None
        self.ServiceType = None
        self.ServiceName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Reason = params.get("Reason")
        self.ServiceType = params.get("ServiceType")
        self.ServiceName = params.get("ServiceName")
        self.RequestId = params.get("RequestId")


class GetUserRequest(AbstractModel):
    """GetUser request structure.

    """

    def __init__(self):
        """
        :param Name: Sub-user username\n        :type Name: str\n        """
        self.Name = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetUserResponse(AbstractModel):
    """GetUser response structure.

    """

    def __init__(self):
        """
        :param Uin: Sub-user UIN\n        :type Uin: int\n        :param Name: Sub-user username\n        :type Name: str\n        :param Uid: Sub-user UID\n        :type Uid: int\n        :param Remark: Sub-user remarks\n        :type Remark: str\n        :param ConsoleLogin: If sub-user can log in to the Console\n        :type ConsoleLogin: int\n        :param PhoneNum: Mobile number\n        :type PhoneNum: str\n        :param CountryCode: Country/Area code\n        :type CountryCode: str\n        :param Email: Email\n        :type Email: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Uin = None
        self.Name = None
        self.Uid = None
        self.Remark = None
        self.ConsoleLogin = None
        self.PhoneNum = None
        self.CountryCode = None
        self.Email = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.Name = params.get("Name")
        self.Uid = params.get("Uid")
        self.Remark = params.get("Remark")
        self.ConsoleLogin = params.get("ConsoleLogin")
        self.PhoneNum = params.get("PhoneNum")
        self.CountryCode = params.get("CountryCode")
        self.Email = params.get("Email")
        self.RequestId = params.get("RequestId")


class GroupIdOfUidInfo(AbstractModel):
    """Information on the association between a sub-user and a User Group

    """

    def __init__(self):
        """
        :param Uid: Sub-user UID\n        :type Uid: int\n        :param GroupId: User Group ID\n        :type GroupId: int\n        """
        self.Uid = None
        self.GroupId = None


    def _deserialize(self, params):
        self.Uid = params.get("Uid")
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupInfo(AbstractModel):
    """User Group information

    """

    def __init__(self):
        """
        :param GroupId: User group ID\n        :type GroupId: int\n        :param GroupName: User Group name\n        :type GroupName: str\n        :param CreateTime: Time User Group created\n        :type CreateTime: str\n        :param Remark: User Group description\n        :type Remark: str\n        """
        self.GroupId = None
        self.GroupName = None
        self.CreateTime = None
        self.Remark = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.CreateTime = params.get("CreateTime")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupMemberInfo(AbstractModel):
    """User Group user information

    """

    def __init__(self):
        """
        :param Uid: Sub-user UID\n        :type Uid: int\n        :param Uin: Sub-user UIN\n        :type Uin: int\n        :param Name: Sub-user name\n        :type Name: str\n        :param PhoneNum: Mobile number\n        :type PhoneNum: str\n        :param CountryCode: Mobile number country/area code\n        :type CountryCode: str\n        :param PhoneFlag: If mobile number has been verified\n        :type PhoneFlag: int\n        :param Email: Email address\n        :type Email: str\n        :param EmailFlag: If email has been verified\n        :type EmailFlag: int\n        :param UserType: User type\n        :type UserType: int\n        :param CreateTime: Time policy created\n        :type CreateTime: str\n        :param IsReceiverOwner: If the user is the main message recipient\n        :type IsReceiverOwner: int\n        """
        self.Uid = None
        self.Uin = None
        self.Name = None
        self.PhoneNum = None
        self.CountryCode = None
        self.PhoneFlag = None
        self.Email = None
        self.EmailFlag = None
        self.UserType = None
        self.CreateTime = None
        self.IsReceiverOwner = None


    def _deserialize(self, params):
        self.Uid = params.get("Uid")
        self.Uin = params.get("Uin")
        self.Name = params.get("Name")
        self.PhoneNum = params.get("PhoneNum")
        self.CountryCode = params.get("CountryCode")
        self.PhoneFlag = params.get("PhoneFlag")
        self.Email = params.get("Email")
        self.EmailFlag = params.get("EmailFlag")
        self.UserType = params.get("UserType")
        self.CreateTime = params.get("CreateTime")
        self.IsReceiverOwner = params.get("IsReceiverOwner")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAccessKeysRequest(AbstractModel):
    """ListAccessKeys request structure.

    """

    def __init__(self):
        """
        :param TargetUin: `UIN` of the specified user. If this parameter is left empty, access keys of the current user will be listed by default\n        :type TargetUin: int\n        """
        self.TargetUin = None


    def _deserialize(self, params):
        self.TargetUin = params.get("TargetUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAccessKeysResponse(AbstractModel):
    """ListAccessKeys response structure.

    """

    def __init__(self):
        """
        :param AccessKeys: Access key list
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AccessKeys: list of AccessKey\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.AccessKeys = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AccessKeys") is not None:
            self.AccessKeys = []
            for item in params.get("AccessKeys"):
                obj = AccessKey()
                obj._deserialize(item)
                self.AccessKeys.append(obj)
        self.RequestId = params.get("RequestId")


class ListAttachedGroupPoliciesRequest(AbstractModel):
    """ListAttachedGroupPolicies request structure.

    """

    def __init__(self):
        """
        :param TargetGroupId: User group ID\n        :type TargetGroupId: int\n        :param Page: Page number, which starts from 1. Default is 1\n        :type Page: int\n        :param Rp: Number of entries per page; 20 by default\n        :type Rp: int\n        """
        self.TargetGroupId = None
        self.Page = None
        self.Rp = None


    def _deserialize(self, params):
        self.TargetGroupId = params.get("TargetGroupId")
        self.Page = params.get("Page")
        self.Rp = params.get("Rp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAttachedGroupPoliciesResponse(AbstractModel):
    """ListAttachedGroupPolicies response structure.

    """

    def __init__(self):
        """
        :param TotalNum: Total number of policies\n        :type TotalNum: int\n        :param List: Policy list\n        :type List: list of AttachPolicyInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalNum = None
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalNum = params.get("TotalNum")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = AttachPolicyInfo()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class ListAttachedRolePoliciesRequest(AbstractModel):
    """ListAttachedRolePolicies request structure.

    """

    def __init__(self):
        """
        :param Page: Page number, beginning from 1\n        :type Page: int\n        :param Rp: Number of lines per page, no more than 200\n        :type Rp: int\n        :param RoleId: Role ID, used to specify a role. Input either `RoleId` or `RoleName`\n        :type RoleId: str\n        :param RoleName: Role name, used to specify a role. Input either `RoleId` or `RoleName`\n        :type RoleName: str\n        :param PolicyType: Filter according to policy type. `User` indicates querying custom policies only. `QCS` indicates querying preset policies only\n        :type PolicyType: str\n        """
        self.Page = None
        self.Rp = None
        self.RoleId = None
        self.RoleName = None
        self.PolicyType = None


    def _deserialize(self, params):
        self.Page = params.get("Page")
        self.Rp = params.get("Rp")
        self.RoleId = params.get("RoleId")
        self.RoleName = params.get("RoleName")
        self.PolicyType = params.get("PolicyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAttachedRolePoliciesResponse(AbstractModel):
    """ListAttachedRolePolicies response structure.

    """

    def __init__(self):
        """
        :param List: List of policies associated with the role\n        :type List: list of AttachedPolicyOfRole\n        :param TotalNum: Total number of policies associated with the role\n        :type TotalNum: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.List = None
        self.TotalNum = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = AttachedPolicyOfRole()
                obj._deserialize(item)
                self.List.append(obj)
        self.TotalNum = params.get("TotalNum")
        self.RequestId = params.get("RequestId")


class ListAttachedUserPoliciesRequest(AbstractModel):
    """ListAttachedUserPolicies request structure.

    """

    def __init__(self):
        """
        :param TargetUin: Sub-account UIN\n        :type TargetUin: int\n        :param Page: Page number, which starts from 1. Default is 1\n        :type Page: int\n        :param Rp: Number of entries per page; 20 by default\n        :type Rp: int\n        """
        self.TargetUin = None
        self.Page = None
        self.Rp = None


    def _deserialize(self, params):
        self.TargetUin = params.get("TargetUin")
        self.Page = params.get("Page")
        self.Rp = params.get("Rp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAttachedUserPoliciesResponse(AbstractModel):
    """ListAttachedUserPolicies response structure.

    """

    def __init__(self):
        """
        :param TotalNum: Total number of policies\n        :type TotalNum: int\n        :param List: Policy list\n        :type List: list of AttachPolicyInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalNum = None
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalNum = params.get("TotalNum")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = AttachPolicyInfo()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class ListCollaboratorsRequest(AbstractModel):
    """ListCollaborators request structure.

    """

    def __init__(self):
        """
        :param Limit: Number of entries per page. Default value: 20\n        :type Limit: int\n        :param Offset: Pagination start value. Default value: 0\n        :type Offset: int\n        """
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListCollaboratorsResponse(AbstractModel):
    """ListCollaborators response structure.

    """

    def __init__(self):
        """
        :param TotalNum: Total number\n        :type TotalNum: int\n        :param Data: Collaborator information\n        :type Data: list of SubAccountInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalNum = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalNum = params.get("TotalNum")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SubAccountInfo()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class ListEntitiesForPolicyRequest(AbstractModel):
    """ListEntitiesForPolicy request structure.

    """

    def __init__(self):
        """
        :param PolicyId: Policy ID\n        :type PolicyId: int\n        :param Page: Page number, which starts from 1. Default is 1\n        :type Page: int\n        :param Rp: Number of entries per page; 20 by default\n        :type Rp: int\n        :param EntityFilter: Valid values: `All`, `User`, `Group`, and `Role`. `All` means all entity types will be returned; `User` means only sub-accounts will be returned; `Group` means only User Groups will be returned; `Role` means only roles will be returned. `All` is the default value.\n        :type EntityFilter: str\n        """
        self.PolicyId = None
        self.Page = None
        self.Rp = None
        self.EntityFilter = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.Page = params.get("Page")
        self.Rp = params.get("Rp")
        self.EntityFilter = params.get("EntityFilter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListEntitiesForPolicyResponse(AbstractModel):
    """ListEntitiesForPolicy response structure.

    """

    def __init__(self):
        """
        :param TotalNum: Number of entities
Note: This field may return null, indicating that no valid value was found.\n        :type TotalNum: int\n        :param List: Entity list
Note: This field may return null, indicating that no valid value was found.\n        :type List: list of AttachEntityOfPolicy\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalNum = None
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalNum = params.get("TotalNum")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = AttachEntityOfPolicy()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class ListGroupsForUserRequest(AbstractModel):
    """ListGroupsForUser request structure.

    """

    def __init__(self):
        """
        :param Uid: Sub-user UID\n        :type Uid: int\n        :param Rp: Number of entries per page; default is 20\n        :type Rp: int\n        :param Page: Page number; default is 1\n        :type Page: int\n        :param SubUin: Sub-account UIN\n        :type SubUin: int\n        """
        self.Uid = None
        self.Rp = None
        self.Page = None
        self.SubUin = None


    def _deserialize(self, params):
        self.Uid = params.get("Uid")
        self.Rp = params.get("Rp")
        self.Page = params.get("Page")
        self.SubUin = params.get("SubUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListGroupsForUserResponse(AbstractModel):
    """ListGroupsForUser response structure.

    """

    def __init__(self):
        """
        :param TotalNum: Total number of User Groups to which the sub-user has been added\n        :type TotalNum: int\n        :param GroupInfo: User Group information\n        :type GroupInfo: list of GroupInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalNum = None
        self.GroupInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalNum = params.get("TotalNum")
        if params.get("GroupInfo") is not None:
            self.GroupInfo = []
            for item in params.get("GroupInfo"):
                obj = GroupInfo()
                obj._deserialize(item)
                self.GroupInfo.append(obj)
        self.RequestId = params.get("RequestId")


class ListGroupsRequest(AbstractModel):
    """ListGroups request structure.

    """

    def __init__(self):
        """
        :param Page: Page number; default is 1\n        :type Page: int\n        :param Rp: Number of entries per page; default is 20\n        :type Rp: int\n        :param Keyword: Filter by User Group name\n        :type Keyword: str\n        """
        self.Page = None
        self.Rp = None
        self.Keyword = None


    def _deserialize(self, params):
        self.Page = params.get("Page")
        self.Rp = params.get("Rp")
        self.Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListGroupsResponse(AbstractModel):
    """ListGroups response structure.

    """

    def __init__(self):
        """
        :param TotalNum: Total number of User Groups\n        :type TotalNum: int\n        :param GroupInfo: User group information array\n        :type GroupInfo: list of GroupInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalNum = None
        self.GroupInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalNum = params.get("TotalNum")
        if params.get("GroupInfo") is not None:
            self.GroupInfo = []
            for item in params.get("GroupInfo"):
                obj = GroupInfo()
                obj._deserialize(item)
                self.GroupInfo.append(obj)
        self.RequestId = params.get("RequestId")


class ListPoliciesRequest(AbstractModel):
    """ListPolicies request structure.

    """

    def __init__(self):
        """
        :param Rp: Number of entries per page: must be greater than 0 and no greater than 200. Default is 20\n        :type Rp: int\n        :param Page: Page number. Starts from 1 and cannot be greater than 200. Default is 1\n        :type Page: int\n        :param Scope: Valid values: `All`, `QCS`, and `Local`. `All` means all policies will be returned; `QCS` means only preset policies will be returned; `Local` means only custom policies will be returned. `All` is the default value\n        :type Scope: str\n        :param Keyword: Filter by policy name\n        :type Keyword: str\n        """
        self.Rp = None
        self.Page = None
        self.Scope = None
        self.Keyword = None


    def _deserialize(self, params):
        self.Rp = params.get("Rp")
        self.Page = params.get("Page")
        self.Scope = params.get("Scope")
        self.Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListPoliciesResponse(AbstractModel):
    """ListPolicies response structure.

    """

    def __init__(self):
        """
        :param TotalNum: Total number of policies\n        :type TotalNum: int\n        :param List: Policy array. Each array contains fields including `policyId`, `policyName`, `addTime`, `type`, `description`, and `createMode`. 
policyId: policy ID 
policyName: policy name
addTime: policy creation time
type: 1: custom policy, 2: preset policy 
description: policy description 
createMode: 1 indicates a policy created based on business permissions, while other values indicate that the policy syntax can be viewed and the policy can be updated using the policy syntax
Attachments: number of associated users
ServiceType: the product the policy is associated with
IsAttached: this value should not be null when querying if a marked entity has been associated with a policy. 0 indicates that no policy has been associated, and 1 indicates that a policy has been associated\n        :type List: list of StrategyInfo\n        :param ServiceTypeList: Reserved field
Note: This field may return null, indicating that no valid value was found.\n        :type ServiceTypeList: list of str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalNum = None
        self.List = None
        self.ServiceTypeList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalNum = params.get("TotalNum")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = StrategyInfo()
                obj._deserialize(item)
                self.List.append(obj)
        self.ServiceTypeList = params.get("ServiceTypeList")
        self.RequestId = params.get("RequestId")


class ListPolicyVersionsRequest(AbstractModel):
    """ListPolicyVersions request structure.

    """

    def __init__(self):
        """
        :param PolicyId: Policy ID\n        :type PolicyId: int\n        """
        self.PolicyId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListPolicyVersionsResponse(AbstractModel):
    """ListPolicyVersions response structure.

    """

    def __init__(self):
        """
        :param Versions: Policy version list
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Versions: list of PolicyVersionItem\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Versions = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Versions") is not None:
            self.Versions = []
            for item in params.get("Versions"):
                obj = PolicyVersionItem()
                obj._deserialize(item)
                self.Versions.append(obj)
        self.RequestId = params.get("RequestId")


class ListSAMLProvidersRequest(AbstractModel):
    """ListSAMLProviders request structure.

    """


class ListSAMLProvidersResponse(AbstractModel):
    """ListSAMLProviders response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of SAML identity providers\n        :type TotalCount: int\n        :param SAMLProviderSet: List of SAML identity providers\n        :type SAMLProviderSet: list of SAMLProviderInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.SAMLProviderSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("SAMLProviderSet") is not None:
            self.SAMLProviderSet = []
            for item in params.get("SAMLProviderSet"):
                obj = SAMLProviderInfo()
                obj._deserialize(item)
                self.SAMLProviderSet.append(obj)
        self.RequestId = params.get("RequestId")


class ListUsersForGroupRequest(AbstractModel):
    """ListUsersForGroup request structure.

    """

    def __init__(self):
        """
        :param GroupId: User group ID\n        :type GroupId: int\n        :param Page: Page number; default is 1\n        :type Page: int\n        :param Rp: Number of entries per page; default is 20\n        :type Rp: int\n        """
        self.GroupId = None
        self.Page = None
        self.Rp = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.Page = params.get("Page")
        self.Rp = params.get("Rp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListUsersForGroupResponse(AbstractModel):
    """ListUsersForGroup response structure.

    """

    def __init__(self):
        """
        :param TotalNum: Total number of users associated with the User Group\n        :type TotalNum: int\n        :param UserInfo: Sub-user information\n        :type UserInfo: list of GroupMemberInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalNum = None
        self.UserInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalNum = params.get("TotalNum")
        if params.get("UserInfo") is not None:
            self.UserInfo = []
            for item in params.get("UserInfo"):
                obj = GroupMemberInfo()
                obj._deserialize(item)
                self.UserInfo.append(obj)
        self.RequestId = params.get("RequestId")


class ListUsersRequest(AbstractModel):
    """ListUsers request structure.

    """


class ListUsersResponse(AbstractModel):
    """ListUsers response structure.

    """

    def __init__(self):
        """
        :param Data: Sub-user information\n        :type Data: list of SubAccountInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SubAccountInfo()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class LoginActionFlag(AbstractModel):
    """Login and sensitive operation flag

    """

    def __init__(self):
        """
        :param Phone: Phone\n        :type Phone: int\n        :param Token: Hard token\n        :type Token: int\n        :param Stoken: Soft token\n        :type Stoken: int\n        :param Wechat: WeChat\n        :type Wechat: int\n        :param Custom: Custom\n        :type Custom: int\n        """
        self.Phone = None
        self.Token = None
        self.Stoken = None
        self.Wechat = None
        self.Custom = None


    def _deserialize(self, params):
        self.Phone = params.get("Phone")
        self.Token = params.get("Token")
        self.Stoken = params.get("Stoken")
        self.Wechat = params.get("Wechat")
        self.Custom = params.get("Custom")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginActionFlagIntl(AbstractModel):
    """Login and sensitive operation flag

    """

    def __init__(self):
        """
        :param Phone: Mobile number\n        :type Phone: int\n        :param Token: Hard token\n        :type Token: int\n        :param Stoken: Soft token\n        :type Stoken: int\n        :param Wechat: WeChat\n        :type Wechat: int\n        :param Custom: Custom\n        :type Custom: int\n        :param Mail: Email\n        :type Mail: int\n        """
        self.Phone = None
        self.Token = None
        self.Stoken = None
        self.Wechat = None
        self.Custom = None
        self.Mail = None


    def _deserialize(self, params):
        self.Phone = params.get("Phone")
        self.Token = params.get("Token")
        self.Stoken = params.get("Stoken")
        self.Wechat = params.get("Wechat")
        self.Custom = params.get("Custom")
        self.Mail = params.get("Mail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginActionMfaFlag(AbstractModel):
    """Login and sensitive operation flag

    """

    def __init__(self):
        """
        :param Phone: Mobile phone\n        :type Phone: int\n        :param Stoken: Soft token\n        :type Stoken: int\n        :param Wechat: WeChat\n        :type Wechat: int\n        """
        self.Phone = None
        self.Stoken = None
        self.Wechat = None


    def _deserialize(self, params):
        self.Phone = params.get("Phone")
        self.Stoken = params.get("Stoken")
        self.Wechat = params.get("Wechat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OffsiteFlag(AbstractModel):
    """Suspicious login location settings

    """

    def __init__(self):
        """
        :param VerifyFlag: Verification flag\n        :type VerifyFlag: int\n        :param NotifyPhone: Phone notification\n        :type NotifyPhone: int\n        :param NotifyEmail: Email notification\n        :type NotifyEmail: int\n        :param NotifyWechat: WeChat notification\n        :type NotifyWechat: int\n        :param Tips: Alert\n        :type Tips: int\n        """
        self.VerifyFlag = None
        self.NotifyPhone = None
        self.NotifyEmail = None
        self.NotifyWechat = None
        self.Tips = None


    def _deserialize(self, params):
        self.VerifyFlag = params.get("VerifyFlag")
        self.NotifyPhone = params.get("NotifyPhone")
        self.NotifyEmail = params.get("NotifyEmail")
        self.NotifyWechat = params.get("NotifyWechat")
        self.Tips = params.get("Tips")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PolicyVersionDetail(AbstractModel):
    """Policy version details

    """

    def __init__(self):
        """
        :param VersionId: Policy version ID
Note: this field may return null, indicating that no valid values can be obtained.\n        :type VersionId: int\n        :param CreateDate: Policy version creation time
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CreateDate: str\n        :param IsDefaultVersion: Whether it is the operative version. 0: no, 1: yes
Note: this field may return null, indicating that no valid values can be obtained.\n        :type IsDefaultVersion: int\n        :param Document: Policy syntax text
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Document: str\n        """
        self.VersionId = None
        self.CreateDate = None
        self.IsDefaultVersion = None
        self.Document = None


    def _deserialize(self, params):
        self.VersionId = params.get("VersionId")
        self.CreateDate = params.get("CreateDate")
        self.IsDefaultVersion = params.get("IsDefaultVersion")
        self.Document = params.get("Document")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PolicyVersionItem(AbstractModel):
    """Policy version list element structure

    """

    def __init__(self):
        """
        :param VersionId: Policy version ID
Note: this field may return null, indicating that no valid values can be obtained.\n        :type VersionId: int\n        :param CreateDate: Policy version creation time
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CreateDate: str\n        :param IsDefaultVersion: Whether it is the operative version. 0: no, 1: yes
Note: this field may return null, indicating that no valid values can be obtained.\n        :type IsDefaultVersion: int\n        """
        self.VersionId = None
        self.CreateDate = None
        self.IsDefaultVersion = None


    def _deserialize(self, params):
        self.VersionId = params.get("VersionId")
        self.CreateDate = params.get("CreateDate")
        self.IsDefaultVersion = params.get("IsDefaultVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutRolePermissionsBoundaryRequest(AbstractModel):
    """PutRolePermissionsBoundary request structure.

    """

    def __init__(self):
        """
        :param PolicyId: Policy ID\n        :type PolicyId: int\n        :param RoleId: Role ID (either it or the role name must be entered)\n        :type RoleId: str\n        :param RoleName: Role name (either it or the role ID must be entered)\n        :type RoleName: str\n        """
        self.PolicyId = None
        self.RoleId = None
        self.RoleName = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.RoleId = params.get("RoleId")
        self.RoleName = params.get("RoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutRolePermissionsBoundaryResponse(AbstractModel):
    """PutRolePermissionsBoundary response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class PutUserPermissionsBoundaryRequest(AbstractModel):
    """PutUserPermissionsBoundary request structure.

    """

    def __init__(self):
        """
        :param TargetUin: Sub-account `Uin`\n        :type TargetUin: int\n        :param PolicyId: Policy ID\n        :type PolicyId: int\n        """
        self.TargetUin = None
        self.PolicyId = None


    def _deserialize(self, params):
        self.TargetUin = params.get("TargetUin")
        self.PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutUserPermissionsBoundaryResponse(AbstractModel):
    """PutUserPermissionsBoundary response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RemoveUserFromGroupRequest(AbstractModel):
    """RemoveUserFromGroup request structure.

    """

    def __init__(self):
        """
        :param Info: The UID of the user to be deleted and an array corresponding to the User Group IDs\n        :type Info: list of GroupIdOfUidInfo\n        """
        self.Info = None


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self.Info = []
            for item in params.get("Info"):
                obj = GroupIdOfUidInfo()
                obj._deserialize(item)
                self.Info.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveUserFromGroupResponse(AbstractModel):
    """RemoveUserFromGroup response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RoleInfo(AbstractModel):
    """Role details

    """

    def __init__(self):
        """
        :param RoleId: Role ID\n        :type RoleId: str\n        :param RoleName: Role name\n        :type RoleName: str\n        :param PolicyDocument: Role policy document\n        :type PolicyDocument: str\n        :param Description: Role description\n        :type Description: str\n        :param AddTime: Time role created\n        :type AddTime: str\n        :param UpdateTime: Time role last updated\n        :type UpdateTime: str\n        :param ConsoleLogin: If login is allowed for the role\n        :type ConsoleLogin: int\n        :param RoleType: User role. Valid values: `user`, `system`, `service_linked`
Note: this field may return null, indicating that no valid values can be obtained.\n        :type RoleType: str\n        :param SessionDuration: Valid period
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SessionDuration: int\n        :param DeletionTaskId: Task identifier for deleting a service-linked role 
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DeletionTaskId: str\n        """
        self.RoleId = None
        self.RoleName = None
        self.PolicyDocument = None
        self.Description = None
        self.AddTime = None
        self.UpdateTime = None
        self.ConsoleLogin = None
        self.RoleType = None
        self.SessionDuration = None
        self.DeletionTaskId = None


    def _deserialize(self, params):
        self.RoleId = params.get("RoleId")
        self.RoleName = params.get("RoleName")
        self.PolicyDocument = params.get("PolicyDocument")
        self.Description = params.get("Description")
        self.AddTime = params.get("AddTime")
        self.UpdateTime = params.get("UpdateTime")
        self.ConsoleLogin = params.get("ConsoleLogin")
        self.RoleType = params.get("RoleType")
        self.SessionDuration = params.get("SessionDuration")
        self.DeletionTaskId = params.get("DeletionTaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SAMLProviderInfo(AbstractModel):
    """SAML identity provider

    """

    def __init__(self):
        """
        :param Name: SAML identity provider name\n        :type Name: str\n        :param Description: SAML identity provider description\n        :type Description: str\n        :param CreateTime: Time SAML identity provider created\n        :type CreateTime: str\n        :param ModifyTime: Time SAML identity provider last modified\n        :type ModifyTime: str\n        """
        self.Name = None
        self.Description = None
        self.CreateTime = None
        self.ModifyTime = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.CreateTime = params.get("CreateTime")
        self.ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecretIdLastUsed(AbstractModel):
    """The last time the key was used.

    """

    def __init__(self):
        """
        :param SecretId: Key ID.\n        :type SecretId: str\n        :param LastUsedDate: The date when the key ID was last used (the value is obtained one day later).
Note: this field may return `null`, indicating that no valid value can be obtained.\n        :type LastUsedDate: str\n        """
        self.SecretId = None
        self.LastUsedDate = None


    def _deserialize(self, params):
        self.SecretId = params.get("SecretId")
        self.LastUsedDate = params.get("LastUsedDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetDefaultPolicyVersionRequest(AbstractModel):
    """SetDefaultPolicyVersion request structure.

    """

    def __init__(self):
        """
        :param PolicyId: Policy ID\n        :type PolicyId: int\n        :param VersionId: Policy version ID\n        :type VersionId: int\n        """
        self.PolicyId = None
        self.VersionId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.VersionId = params.get("VersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetDefaultPolicyVersionResponse(AbstractModel):
    """SetDefaultPolicyVersion response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SetMfaFlagRequest(AbstractModel):
    """SetMfaFlag request structure.

    """

    def __init__(self):
        """
        :param OpUin: Sets user UIN\n        :type OpUin: int\n        :param LoginFlag: Sets login protection\n        :type LoginFlag: :class:`tencentcloud.cam.v20190116.models.LoginActionMfaFlag`\n        :param ActionFlag: Sets operation protection\n        :type ActionFlag: :class:`tencentcloud.cam.v20190116.models.LoginActionMfaFlag`\n        """
        self.OpUin = None
        self.LoginFlag = None
        self.ActionFlag = None


    def _deserialize(self, params):
        self.OpUin = params.get("OpUin")
        if params.get("LoginFlag") is not None:
            self.LoginFlag = LoginActionMfaFlag()
            self.LoginFlag._deserialize(params.get("LoginFlag"))
        if params.get("ActionFlag") is not None:
            self.ActionFlag = LoginActionMfaFlag()
            self.ActionFlag._deserialize(params.get("ActionFlag"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetMfaFlagResponse(AbstractModel):
    """SetMfaFlag response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StrategyInfo(AbstractModel):
    """Policy information

    """

    def __init__(self):
        """
        :param PolicyId: Policy ID\n        :type PolicyId: int\n        :param PolicyName: Policy name\n        :type PolicyName: str\n        :param AddTime: Time policy created
Note: This field may return null, indicating that no valid value was found.\n        :type AddTime: str\n        :param Type: Policy type. 1: Custom policy; 2: Preset policy\n        :type Type: int\n        :param Description: Policy description
Note: This field may return null, indicating that no valid value was found.\n        :type Description: str\n        :param CreateMode: How the policy was created: 1: Via console; 2: Via syntax\n        :type CreateMode: int\n        :param Attachments: Number of associated users\n        :type Attachments: int\n        :param ServiceType: Product associated with the policy
Note: This field may return null, indicating that no valid value was found.\n        :type ServiceType: str\n        :param IsAttached: This value should not be null when querying whether a marked entity has been associated with a policy. 0 indicates that no policy has been associated, while 1 indicates that a policy has been associated\n        :type IsAttached: int\n        :param Deactived: Queries if the policy has been deactivated
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Deactived: int\n        :param DeactivedDetail: List of deprecated products
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DeactivedDetail: list of str\n        :param IsServiceLinkedPolicy: The deletion task identifier used to check the deletion status of the service-linked role
Note: this field may return null, indicating that no valid values can be obtained.\n        :type IsServiceLinkedPolicy: int\n        :param AttachEntityCount: The number of entities associated with the policy.
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type AttachEntityCount: int\n        :param AttachEntityBoundaryCount: The number of entities associated with the permission boundary.
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type AttachEntityBoundaryCount: int\n        :param UpdateTime: The last edited time.
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type UpdateTime: str\n        """
        self.PolicyId = None
        self.PolicyName = None
        self.AddTime = None
        self.Type = None
        self.Description = None
        self.CreateMode = None
        self.Attachments = None
        self.ServiceType = None
        self.IsAttached = None
        self.Deactived = None
        self.DeactivedDetail = None
        self.IsServiceLinkedPolicy = None
        self.AttachEntityCount = None
        self.AttachEntityBoundaryCount = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.PolicyName = params.get("PolicyName")
        self.AddTime = params.get("AddTime")
        self.Type = params.get("Type")
        self.Description = params.get("Description")
        self.CreateMode = params.get("CreateMode")
        self.Attachments = params.get("Attachments")
        self.ServiceType = params.get("ServiceType")
        self.IsAttached = params.get("IsAttached")
        self.Deactived = params.get("Deactived")
        self.DeactivedDetail = params.get("DeactivedDetail")
        self.IsServiceLinkedPolicy = params.get("IsServiceLinkedPolicy")
        self.AttachEntityCount = params.get("AttachEntityCount")
        self.AttachEntityBoundaryCount = params.get("AttachEntityBoundaryCount")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubAccountInfo(AbstractModel):
    """Sub-user information

    """

    def __init__(self):
        """
        :param Uin: Sub-user user ID\n        :type Uin: int\n        :param Name: Sub-user username\n        :type Name: str\n        :param Uid: Sub-user UID\n        :type Uid: int\n        :param Remark: Sub-user remarks\n        :type Remark: str\n        :param ConsoleLogin: If sub-user can log in to the console\n        :type ConsoleLogin: int\n        :param PhoneNum: Mobile number\n        :type PhoneNum: str\n        :param CountryCode: Country/Area code\n        :type CountryCode: str\n        :param Email: Email\n        :type Email: str\n        :param CreateTime: Creation time
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type CreateTime: str\n        """
        self.Uin = None
        self.Name = None
        self.Uid = None
        self.Remark = None
        self.ConsoleLogin = None
        self.PhoneNum = None
        self.CountryCode = None
        self.Email = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.Name = params.get("Name")
        self.Uid = params.get("Uid")
        self.Remark = params.get("Remark")
        self.ConsoleLogin = params.get("ConsoleLogin")
        self.PhoneNum = params.get("PhoneNum")
        self.CountryCode = params.get("CountryCode")
        self.Email = params.get("Email")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubAccountUser(AbstractModel):
    """Sub-user information

    """

    def __init__(self):
        """
        :param Uin: Sub-user ID\n        :type Uin: int\n        :param Name: Sub-user name\n        :type Name: str\n        :param Uid: Sub-user UID\n        :type Uid: int\n        :param Remark: Sub-user remarks\n        :type Remark: str\n        :param CreateTime: Creation time
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CreateTime: str\n        :param UserType: User type (1: root account; 2: sub-user; 3: WeCom sub-user; 4: collaborator; 5: message recipient)\n        :type UserType: int\n        :param LastLoginIp: \n        :type LastLoginIp: str\n        :param LastLoginTime: \n        :type LastLoginTime: str\n        """
        self.Uin = None
        self.Name = None
        self.Uid = None
        self.Remark = None
        self.CreateTime = None
        self.UserType = None
        self.LastLoginIp = None
        self.LastLoginTime = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.Name = params.get("Name")
        self.Uid = params.get("Uid")
        self.Remark = params.get("Remark")
        self.CreateTime = params.get("CreateTime")
        self.UserType = params.get("UserType")
        self.LastLoginIp = params.get("LastLoginIp")
        self.LastLoginTime = params.get("LastLoginTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAssumeRolePolicyRequest(AbstractModel):
    """UpdateAssumeRolePolicy request structure.

    """

    def __init__(self):
        """
        :param PolicyDocument: Policy document\n        :type PolicyDocument: str\n        :param RoleId: Role ID, used to specify a role. Input either `RoleId` or `RoleName`\n        :type RoleId: str\n        :param RoleName: Role name, used to specify a role. Input either `RoleId` or `RoleName`\n        :type RoleName: str\n        """
        self.PolicyDocument = None
        self.RoleId = None
        self.RoleName = None


    def _deserialize(self, params):
        self.PolicyDocument = params.get("PolicyDocument")
        self.RoleId = params.get("RoleId")
        self.RoleName = params.get("RoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAssumeRolePolicyResponse(AbstractModel):
    """UpdateAssumeRolePolicy response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateGroupRequest(AbstractModel):
    """UpdateGroup request structure.

    """

    def __init__(self):
        """
        :param GroupId: User Group ID\n        :type GroupId: int\n        :param GroupName: User Group name\n        :type GroupName: str\n        :param Remark: User Group description\n        :type Remark: str\n        """
        self.GroupId = None
        self.GroupName = None
        self.Remark = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateGroupResponse(AbstractModel):
    """UpdateGroup response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdatePolicyRequest(AbstractModel):
    """UpdatePolicy request structure.

    """

    def __init__(self):
        """
        :param PolicyId: Policy ID. Either `PolicyId` or `PolicyName` must be entered\n        :type PolicyId: int\n        :param PolicyName: Policy name. Either `PolicyName` or `PolicyId` must be entered\n        :type PolicyName: str\n        :param Description: Policy description\n        :type Description: str\n        :param PolicyDocument: Policy documentation, for example: `{"version":"2.0","statement":[{"action":"name/sts:AssumeRole","effect":"allow","principal":{"service":["cloudaudit.cloud.tencent.com","cls.cloud.tencent.com"]}}]}`, where `principal` is used to specify the service that is authorized to use the role. For more information about this parameter, see **RoleInfo** under **Output Parameters** in the [GetRole](https://intl.cloud.tencent.com/document/product/598/36221?from_cn_redirect=1).\n        :type PolicyDocument: str\n        :param Alias: Preset policy remark\n        :type Alias: str\n        """
        self.PolicyId = None
        self.PolicyName = None
        self.Description = None
        self.PolicyDocument = None
        self.Alias = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.PolicyName = params.get("PolicyName")
        self.Description = params.get("Description")
        self.PolicyDocument = params.get("PolicyDocument")
        self.Alias = params.get("Alias")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdatePolicyResponse(AbstractModel):
    """UpdatePolicy response structure.

    """

    def __init__(self):
        """
        :param PolicyId: Policy ID, which will be returned only if the input parameter is `PolicyName`
Note: this field may return null, indicating that no valid values can be obtained.\n        :type PolicyId: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.PolicyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.RequestId = params.get("RequestId")


class UpdateRoleConsoleLoginRequest(AbstractModel):
    """UpdateRoleConsoleLogin request structure.

    """

    def __init__(self):
        """
        :param ConsoleLogin: Whether login is allowed. 1: yes, 0: no\n        :type ConsoleLogin: int\n        :param RoleId: Role ID\n        :type RoleId: int\n        :param RoleName: Role name\n        :type RoleName: str\n        """
        self.ConsoleLogin = None
        self.RoleId = None
        self.RoleName = None


    def _deserialize(self, params):
        self.ConsoleLogin = params.get("ConsoleLogin")
        self.RoleId = params.get("RoleId")
        self.RoleName = params.get("RoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRoleConsoleLoginResponse(AbstractModel):
    """UpdateRoleConsoleLogin response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateRoleDescriptionRequest(AbstractModel):
    """UpdateRoleDescription request structure.

    """

    def __init__(self):
        """
        :param Description: Role description\n        :type Description: str\n        :param RoleId: Role ID, used to specify a role. Input either `RoleId` or `RoleName`\n        :type RoleId: str\n        :param RoleName: Role name, used to specify a role. Input either `RoleId` or `RoleName`\n        :type RoleName: str\n        """
        self.Description = None
        self.RoleId = None
        self.RoleName = None


    def _deserialize(self, params):
        self.Description = params.get("Description")
        self.RoleId = params.get("RoleId")
        self.RoleName = params.get("RoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRoleDescriptionResponse(AbstractModel):
    """UpdateRoleDescription response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateSAMLProviderRequest(AbstractModel):
    """UpdateSAMLProvider request structure.

    """

    def __init__(self):
        """
        :param Name: SAML identity provider name\n        :type Name: str\n        :param Description: SAML identity provider description\n        :type Description: str\n        :param SAMLMetadataDocument: SAML identity provider metadata document (Base64)\n        :type SAMLMetadataDocument: str\n        """
        self.Name = None
        self.Description = None
        self.SAMLMetadataDocument = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.SAMLMetadataDocument = params.get("SAMLMetadataDocument")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateSAMLProviderResponse(AbstractModel):
    """UpdateSAMLProvider response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateUserRequest(AbstractModel):
    """UpdateUser request structure.

    """

    def __init__(self):
        """
        :param Name: Sub-user username\n        :type Name: str\n        :param Remark: Sub-user remarks\n        :type Remark: str\n        :param ConsoleLogin: Whether or not the sub-user is allowed to log in to the console. 0: No; 1: Yes.\n        :type ConsoleLogin: int\n        :param Password: Sub-user's console login password. If no password rules have been set, the password must have a minimum of 8 characters containing uppercase letters, lowercase letters, digits, and special characters by default. This parameter will be valid only when the sub-user is allowed to log in to the console. If it is not specified and console login is allowed, the system will automatically generate a random 32-character password that contains uppercase letters, lowercase letters, digits, and special characters.\n        :type Password: str\n        :param NeedResetPassword: If the sub-user needs to reset their password when they next log in to the console. 0: No; 1: Yes.\n        :type NeedResetPassword: int\n        :param PhoneNum: Mobile number\n        :type PhoneNum: str\n        :param CountryCode: Country/Area Code\n        :type CountryCode: str\n        :param Email: Email\n        :type Email: str\n        """
        self.Name = None
        self.Remark = None
        self.ConsoleLogin = None
        self.Password = None
        self.NeedResetPassword = None
        self.PhoneNum = None
        self.CountryCode = None
        self.Email = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Remark = params.get("Remark")
        self.ConsoleLogin = params.get("ConsoleLogin")
        self.Password = params.get("Password")
        self.NeedResetPassword = params.get("NeedResetPassword")
        self.PhoneNum = params.get("PhoneNum")
        self.CountryCode = params.get("CountryCode")
        self.Email = params.get("Email")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateUserResponse(AbstractModel):
    """UpdateUser response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")