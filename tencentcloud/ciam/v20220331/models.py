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


class CreateApiImportUserJobRequest(AbstractModel):
    """CreateApiImportUserJob request structure.

    """

    def __init__(self):
        r"""
        :param _UserStoreId: User directory ID
        :type UserStoreId: str
        :param _DataFlowUserCreateList: Imported user data
        :type DataFlowUserCreateList: list of ImportUser
        """
        self._UserStoreId = None
        self._DataFlowUserCreateList = None

    @property
    def UserStoreId(self):
        return self._UserStoreId

    @UserStoreId.setter
    def UserStoreId(self, UserStoreId):
        self._UserStoreId = UserStoreId

    @property
    def DataFlowUserCreateList(self):
        return self._DataFlowUserCreateList

    @DataFlowUserCreateList.setter
    def DataFlowUserCreateList(self, DataFlowUserCreateList):
        self._DataFlowUserCreateList = DataFlowUserCreateList


    def _deserialize(self, params):
        self._UserStoreId = params.get("UserStoreId")
        if params.get("DataFlowUserCreateList") is not None:
            self._DataFlowUserCreateList = []
            for item in params.get("DataFlowUserCreateList"):
                obj = ImportUser()
                obj._deserialize(item)
                self._DataFlowUserCreateList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApiImportUserJobResponse(AbstractModel):
    """CreateApiImportUserJob response structure.

    """

    def __init__(self):
        r"""
        :param _Job: Data flow task
        :type Job: :class:`tencentcloud.ciam.v20220331.models.Job`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Job = None
        self._RequestId = None

    @property
    def Job(self):
        return self._Job

    @Job.setter
    def Job(self, Job):
        self._Job = Job

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Job") is not None:
            self._Job = Job()
            self._Job._deserialize(params.get("Job"))
        self._RequestId = params.get("RequestId")


class CreateFileExportUserJobRequest(AbstractModel):
    """CreateFileExportUserJob request structure.

    """

    def __init__(self):
        r"""
        :param _UserStoreId: User directory ID
        :type UserStoreId: str
        :param _Format: Exported data type

<li> **NDJSON** </li>  New-line Delimited JSON
<li> **CSV** </li>  Comma-Separated Values
        :type Format: str
        :param _Filters: Valid values of `Key`: `condition`, `userGroupId`.

<li> **condition** </li>	Values = Query condition, which can be user ID, username, mobile number, or email address.
<li> **userGroupId** </li>	Values = User group ID
        :type Filters: list of Filter
        :param _ExportPropertyMaps: Attributes and mapping names included in the exported user information. If this parameter is empty, all attributes will be included.
        :type ExportPropertyMaps: list of ExportPropertyMap
        """
        self._UserStoreId = None
        self._Format = None
        self._Filters = None
        self._ExportPropertyMaps = None

    @property
    def UserStoreId(self):
        return self._UserStoreId

    @UserStoreId.setter
    def UserStoreId(self, UserStoreId):
        self._UserStoreId = UserStoreId

    @property
    def Format(self):
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def ExportPropertyMaps(self):
        return self._ExportPropertyMaps

    @ExportPropertyMaps.setter
    def ExportPropertyMaps(self, ExportPropertyMaps):
        self._ExportPropertyMaps = ExportPropertyMaps


    def _deserialize(self, params):
        self._UserStoreId = params.get("UserStoreId")
        self._Format = params.get("Format")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("ExportPropertyMaps") is not None:
            self._ExportPropertyMaps = []
            for item in params.get("ExportPropertyMaps"):
                obj = ExportPropertyMap()
                obj._deserialize(item)
                self._ExportPropertyMaps.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFileExportUserJobResponse(AbstractModel):
    """CreateFileExportUserJob response structure.

    """

    def __init__(self):
        r"""
        :param _Job: Data flow task
        :type Job: :class:`tencentcloud.ciam.v20220331.models.Job`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Job = None
        self._RequestId = None

    @property
    def Job(self):
        return self._Job

    @Job.setter
    def Job(self, Job):
        self._Job = Job

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Job") is not None:
            self._Job = Job()
            self._Job._deserialize(params.get("Job"))
        self._RequestId = params.get("RequestId")


class CreateUserRequest(AbstractModel):
    """CreateUser request structure.

    """

    def __init__(self):
        r"""
        :param _UserStoreId: User directory ID
        :type UserStoreId: str
        :param _PhoneNumber: Mobile number
        :type PhoneNumber: str
        :param _Email: Email address
        :type Email: str
        :param _Password: Password
        :type Password: str
        :param _UserName: Username
        :type UserName: str
        :param _Nickname: Nickname
        :type Nickname: str
        :param _Address: Address
        :type Address: str
        :param _UserGroup: User group ID
        :type UserGroup: list of str
        :param _Birthdate: Date of birth
        :type Birthdate: int
        :param _CustomizationAttributes: Custom attribute
        :type CustomizationAttributes: list of MemberMap
        :param _IndexedAttribute1: Index field 1
        :type IndexedAttribute1: str
        :param _IndexedAttribute2: Index field 2
        :type IndexedAttribute2: str
        :param _IndexedAttribute3: Index field 3
        :type IndexedAttribute3: str
        :param _IndexedAttribute4: Index field 4
        :type IndexedAttribute4: str
        :param _IndexedAttribute5: Index field 5
        :type IndexedAttribute5: str
        """
        self._UserStoreId = None
        self._PhoneNumber = None
        self._Email = None
        self._Password = None
        self._UserName = None
        self._Nickname = None
        self._Address = None
        self._UserGroup = None
        self._Birthdate = None
        self._CustomizationAttributes = None
        self._IndexedAttribute1 = None
        self._IndexedAttribute2 = None
        self._IndexedAttribute3 = None
        self._IndexedAttribute4 = None
        self._IndexedAttribute5 = None

    @property
    def UserStoreId(self):
        return self._UserStoreId

    @UserStoreId.setter
    def UserStoreId(self, UserStoreId):
        self._UserStoreId = UserStoreId

    @property
    def PhoneNumber(self):
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Nickname(self):
        return self._Nickname

    @Nickname.setter
    def Nickname(self, Nickname):
        self._Nickname = Nickname

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def UserGroup(self):
        return self._UserGroup

    @UserGroup.setter
    def UserGroup(self, UserGroup):
        self._UserGroup = UserGroup

    @property
    def Birthdate(self):
        return self._Birthdate

    @Birthdate.setter
    def Birthdate(self, Birthdate):
        self._Birthdate = Birthdate

    @property
    def CustomizationAttributes(self):
        return self._CustomizationAttributes

    @CustomizationAttributes.setter
    def CustomizationAttributes(self, CustomizationAttributes):
        self._CustomizationAttributes = CustomizationAttributes

    @property
    def IndexedAttribute1(self):
        return self._IndexedAttribute1

    @IndexedAttribute1.setter
    def IndexedAttribute1(self, IndexedAttribute1):
        self._IndexedAttribute1 = IndexedAttribute1

    @property
    def IndexedAttribute2(self):
        return self._IndexedAttribute2

    @IndexedAttribute2.setter
    def IndexedAttribute2(self, IndexedAttribute2):
        self._IndexedAttribute2 = IndexedAttribute2

    @property
    def IndexedAttribute3(self):
        return self._IndexedAttribute3

    @IndexedAttribute3.setter
    def IndexedAttribute3(self, IndexedAttribute3):
        self._IndexedAttribute3 = IndexedAttribute3

    @property
    def IndexedAttribute4(self):
        return self._IndexedAttribute4

    @IndexedAttribute4.setter
    def IndexedAttribute4(self, IndexedAttribute4):
        self._IndexedAttribute4 = IndexedAttribute4

    @property
    def IndexedAttribute5(self):
        return self._IndexedAttribute5

    @IndexedAttribute5.setter
    def IndexedAttribute5(self, IndexedAttribute5):
        self._IndexedAttribute5 = IndexedAttribute5


    def _deserialize(self, params):
        self._UserStoreId = params.get("UserStoreId")
        self._PhoneNumber = params.get("PhoneNumber")
        self._Email = params.get("Email")
        self._Password = params.get("Password")
        self._UserName = params.get("UserName")
        self._Nickname = params.get("Nickname")
        self._Address = params.get("Address")
        self._UserGroup = params.get("UserGroup")
        self._Birthdate = params.get("Birthdate")
        if params.get("CustomizationAttributes") is not None:
            self._CustomizationAttributes = []
            for item in params.get("CustomizationAttributes"):
                obj = MemberMap()
                obj._deserialize(item)
                self._CustomizationAttributes.append(obj)
        self._IndexedAttribute1 = params.get("IndexedAttribute1")
        self._IndexedAttribute2 = params.get("IndexedAttribute2")
        self._IndexedAttribute3 = params.get("IndexedAttribute3")
        self._IndexedAttribute4 = params.get("IndexedAttribute4")
        self._IndexedAttribute5 = params.get("IndexedAttribute5")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUserResponse(AbstractModel):
    """CreateUser response structure.

    """

    def __init__(self):
        r"""
        :param _User: Information of the created user
Note: This field may return null, indicating that no valid values can be obtained.
        :type User: :class:`tencentcloud.ciam.v20220331.models.User`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._User = None
        self._RequestId = None

    @property
    def User(self):
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("User") is not None:
            self._User = User()
            self._User._deserialize(params.get("User"))
        self._RequestId = params.get("RequestId")


class DeleteUsersRequest(AbstractModel):
    """DeleteUsers request structure.

    """

    def __init__(self):
        r"""
        :param _UserStoreId: User directory ID
        :type UserStoreId: str
        :param _UserIds: Array of user IDs
        :type UserIds: list of str
        """
        self._UserStoreId = None
        self._UserIds = None

    @property
    def UserStoreId(self):
        return self._UserStoreId

    @UserStoreId.setter
    def UserStoreId(self, UserStoreId):
        self._UserStoreId = UserStoreId

    @property
    def UserIds(self):
        return self._UserIds

    @UserIds.setter
    def UserIds(self, UserIds):
        self._UserIds = UserIds


    def _deserialize(self, params):
        self._UserStoreId = params.get("UserStoreId")
        self._UserIds = params.get("UserIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUsersResponse(AbstractModel):
    """DeleteUsers response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeUserByIdRequest(AbstractModel):
    """DescribeUserById request structure.

    """

    def __init__(self):
        r"""
        :param _UserStoreId: User directory ID
        :type UserStoreId: str
        :param _UserId: User ID
        :type UserId: str
        :param _Original: Whether the content is passed through

<li> **false** </li>Default. The returned information is desensitized.
<li> **true** </li>Return the original content.
        :type Original: bool
        """
        self._UserStoreId = None
        self._UserId = None
        self._Original = None

    @property
    def UserStoreId(self):
        return self._UserStoreId

    @UserStoreId.setter
    def UserStoreId(self, UserStoreId):
        self._UserStoreId = UserStoreId

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Original(self):
        return self._Original

    @Original.setter
    def Original(self, Original):
        self._Original = Original


    def _deserialize(self, params):
        self._UserStoreId = params.get("UserStoreId")
        self._UserId = params.get("UserId")
        self._Original = params.get("Original")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserByIdResponse(AbstractModel):
    """DescribeUserById response structure.

    """

    def __init__(self):
        r"""
        :param _User: User information
Note: This field may return null, indicating that no valid values can be obtained.
        :type User: :class:`tencentcloud.ciam.v20220331.models.User`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._User = None
        self._RequestId = None

    @property
    def User(self):
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("User") is not None:
            self._User = User()
            self._User._deserialize(params.get("User"))
        self._RequestId = params.get("RequestId")


class DescribeUserRequest(AbstractModel):
    """DescribeUser request structure.

    """

    def __init__(self):
        r"""
        :param _UserStoreId: User directory ID
        :type UserStoreId: str
        :param _Pageable: Pagination data
        :type Pageable: :class:`tencentcloud.ciam.v20220331.models.Pageable`
        :param _Filters: Query condition (`propertycode` and `propertykey`)
        :type Filters: list of QueryUserFilter
        :param _Original: Whether the plaintext is returned
        :type Original: bool
        :param _Sort: Sorting configuration
        :type Sort: :class:`tencentcloud.ciam.v20220331.models.Sort`
        """
        self._UserStoreId = None
        self._Pageable = None
        self._Filters = None
        self._Original = None
        self._Sort = None

    @property
    def UserStoreId(self):
        return self._UserStoreId

    @UserStoreId.setter
    def UserStoreId(self, UserStoreId):
        self._UserStoreId = UserStoreId

    @property
    def Pageable(self):
        return self._Pageable

    @Pageable.setter
    def Pageable(self, Pageable):
        self._Pageable = Pageable

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Original(self):
        return self._Original

    @Original.setter
    def Original(self, Original):
        self._Original = Original

    @property
    def Sort(self):
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort


    def _deserialize(self, params):
        self._UserStoreId = params.get("UserStoreId")
        if params.get("Pageable") is not None:
            self._Pageable = Pageable()
            self._Pageable._deserialize(params.get("Pageable"))
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = QueryUserFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Original = params.get("Original")
        if params.get("Sort") is not None:
            self._Sort = Sort()
            self._Sort._deserialize(params.get("Sort"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserResponse(AbstractModel):
    """DescribeUser response structure.

    """

    def __init__(self):
        r"""
        :param _Total: The total number of returned results.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Total: int
        :param _Pageable: Pagination object
Note: this field may return null, indicating that no valid values can be obtained.
        :type Pageable: :class:`tencentcloud.ciam.v20220331.models.Pageable`
        :param _Content: User List
Note: this field may return null, indicating that no valid values can be obtained.
        :type Content: list of User
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._Pageable = None
        self._Content = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Pageable(self):
        return self._Pageable

    @Pageable.setter
    def Pageable(self, Pageable):
        self._Pageable = Pageable

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Pageable") is not None:
            self._Pageable = Pageable()
            self._Pageable._deserialize(params.get("Pageable"))
        if params.get("Content") is not None:
            self._Content = []
            for item in params.get("Content"):
                obj = User()
                obj._deserialize(item)
                self._Content.append(obj)
        self._RequestId = params.get("RequestId")


class ErrorDetails(AbstractModel):
    """Failure details

    """

    def __init__(self):
        r"""
        :param _UserId: User information
Note: This field may return null, indicating that no valid values can be obtained.
        :type UserId: str
        :param _Error: Failure cause
        :type Error: str
        """
        self._UserId = None
        self._Error = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Error(self):
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._Error = params.get("Error")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportPropertyMap(AbstractModel):
    """Exported attribute mapping

    """

    def __init__(self):
        r"""
        :param _UserPropertyCode: User attribute code
        :type UserPropertyCode: str
        :param _ColumnName: User attribute mapping name
        :type ColumnName: str
        """
        self._UserPropertyCode = None
        self._ColumnName = None

    @property
    def UserPropertyCode(self):
        return self._UserPropertyCode

    @UserPropertyCode.setter
    def UserPropertyCode(self, UserPropertyCode):
        self._UserPropertyCode = UserPropertyCode

    @property
    def ColumnName(self):
        return self._ColumnName

    @ColumnName.setter
    def ColumnName(self, ColumnName):
        self._ColumnName = ColumnName


    def _deserialize(self, params):
        self._UserPropertyCode = params.get("UserPropertyCode")
        self._ColumnName = params.get("ColumnName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FailedUsers(AbstractModel):
    """Failed user

    """

    def __init__(self):
        r"""
        :param _FailedUserIdentification: ID of the failed user
Note: This field may return null, indicating that no valid values can be obtained.
        :type FailedUserIdentification: str
        :param _FailedReason: Failure cause for user import
Note: This field may return null, indicating that no valid values can be obtained.
        :type FailedReason: str
        """
        self._FailedUserIdentification = None
        self._FailedReason = None

    @property
    def FailedUserIdentification(self):
        return self._FailedUserIdentification

    @FailedUserIdentification.setter
    def FailedUserIdentification(self, FailedUserIdentification):
        self._FailedUserIdentification = FailedUserIdentification

    @property
    def FailedReason(self):
        return self._FailedReason

    @FailedReason.setter
    def FailedReason(self, FailedReason):
        self._FailedReason = FailedReason


    def _deserialize(self, params):
        self._FailedUserIdentification = params.get("FailedUserIdentification")
        self._FailedReason = params.get("FailedReason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """Query condition

    """

    def __init__(self):
        r"""
        :param _Key: Key value
        :type Key: str
        :param _Values: Value
        :type Values: list of str
        :param _Logic: Logical value
        :type Logic: bool
        """
        self._Key = None
        self._Values = None
        self._Logic = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def Logic(self):
        return self._Logic

    @Logic.setter
    def Logic(self, Logic):
        self._Logic = Logic


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Values = params.get("Values")
        self._Logic = params.get("Logic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportUser(AbstractModel):
    """Imported user information
    1. One of the eight attributes of `UserName`, `PhoneNumber`, `Email`, `WechatOpenId`, `WechatUnionId`, `AlipayUserId`, `QqOpenId`, and `QqUnionId` must be included during import and comply with the regular expression rules for initializing custom attributes. The regular expressions for `UserName`, `PhoneNumber`, and `Email` can be queried in the custom attributes in the console.
    2. For password import, the imported password supports plaintext import, MD5 ciphertext import, SHA1 ciphertext import, and BCRYPT ciphertext import. This needs to be specified in the `PasswordEncryptTypeEnum` field.
    3. `IdentityVerified` and `IdentityVerificationMethod` can be imported.
    If `IdentityVerified` is `true`, `IdentityVerificationMethod` is required.
    If `IdentityVerificationMethod` is `nameAndIdCard`, `Name` and `ResidentIdentityCard` are required.
    If `IdentityVerificationMethod` is `nameIdCardAndPhone`, `Name`, `PhoneNumber`, and `ResidentIdentityCard` are required.

    """

    def __init__(self):
        r"""
        :param _UserName: Username
        :type UserName: str
        :param _PhoneNumber: Mobile number
        :type PhoneNumber: str
        :param _Email: Email address
        :type Email: str
        :param _ResidentIdentityCard: ID card number
        :type ResidentIdentityCard: str
        :param _Nickname: Nickname
        :type Nickname: str
        :param _Address: Address
        :type Address: str
        :param _UserGroup: User group ID
        :type UserGroup: list of str
        :param _QqOpenId: `qqOpenId` on QQ
        :type QqOpenId: str
        :param _QqUnionId: `qqUnionId` on QQ
        :type QqUnionId: str
        :param _WechatOpenId: `wechatOpenId` on WeChat
        :type WechatOpenId: str
        :param _WechatUnionId: `wechatUnionId` on WeChat
        :type WechatUnionId: str
        :param _AlipayUserId: `alipayUserId` on Alipay
        :type AlipayUserId: str
        :param _Description: Description
        :type Description: str
        :param _Birthdate: Date of birth
        :type Birthdate: str
        :param _Name: Name
        :type Name: str
        :param _Locale: Coordinate
        :type Locale: str
        :param _Gender: Gender. Valid values: `MALE`, `FEMALE`, `UNKNOWN`.
        :type Gender: str
        :param _IdentityVerificationMethod: Identity verification method
        :type IdentityVerificationMethod: str
        :param _IdentityVerified: Whether the identity is verified
        :type IdentityVerified: bool
        :param _Job: Job
        :type Job: str
        :param _Nationality: Country/Region
        :type Nationality: str
        :param _Zone: Time zone
        :type Zone: str
        :param _Password: Password ciphertext
        :type Password: str
        :param _CustomizationAttributes: Custom attribute
        :type CustomizationAttributes: list of MemberMap
        :param _Salt: Password salt
        :type Salt: :class:`tencentcloud.ciam.v20220331.models.Salt`
        :param _PasswordEncryptTypeEnum: Password encryption method. Valid values: `SHA1`, `BCRYPT`.
        :type PasswordEncryptTypeEnum: str
        :param _IndexedAttribute1: Index field 1
        :type IndexedAttribute1: str
        :param _IndexedAttribute2: Index field 2
        :type IndexedAttribute2: str
        :param _IndexedAttribute3: Index field 3
        :type IndexedAttribute3: str
        :param _IndexedAttribute4: Index field 4
        :type IndexedAttribute4: str
        :param _IndexedAttribute5: Index field 5
        :type IndexedAttribute5: str
        """
        self._UserName = None
        self._PhoneNumber = None
        self._Email = None
        self._ResidentIdentityCard = None
        self._Nickname = None
        self._Address = None
        self._UserGroup = None
        self._QqOpenId = None
        self._QqUnionId = None
        self._WechatOpenId = None
        self._WechatUnionId = None
        self._AlipayUserId = None
        self._Description = None
        self._Birthdate = None
        self._Name = None
        self._Locale = None
        self._Gender = None
        self._IdentityVerificationMethod = None
        self._IdentityVerified = None
        self._Job = None
        self._Nationality = None
        self._Zone = None
        self._Password = None
        self._CustomizationAttributes = None
        self._Salt = None
        self._PasswordEncryptTypeEnum = None
        self._IndexedAttribute1 = None
        self._IndexedAttribute2 = None
        self._IndexedAttribute3 = None
        self._IndexedAttribute4 = None
        self._IndexedAttribute5 = None

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def PhoneNumber(self):
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def ResidentIdentityCard(self):
        return self._ResidentIdentityCard

    @ResidentIdentityCard.setter
    def ResidentIdentityCard(self, ResidentIdentityCard):
        self._ResidentIdentityCard = ResidentIdentityCard

    @property
    def Nickname(self):
        return self._Nickname

    @Nickname.setter
    def Nickname(self, Nickname):
        self._Nickname = Nickname

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def UserGroup(self):
        return self._UserGroup

    @UserGroup.setter
    def UserGroup(self, UserGroup):
        self._UserGroup = UserGroup

    @property
    def QqOpenId(self):
        return self._QqOpenId

    @QqOpenId.setter
    def QqOpenId(self, QqOpenId):
        self._QqOpenId = QqOpenId

    @property
    def QqUnionId(self):
        return self._QqUnionId

    @QqUnionId.setter
    def QqUnionId(self, QqUnionId):
        self._QqUnionId = QqUnionId

    @property
    def WechatOpenId(self):
        return self._WechatOpenId

    @WechatOpenId.setter
    def WechatOpenId(self, WechatOpenId):
        self._WechatOpenId = WechatOpenId

    @property
    def WechatUnionId(self):
        return self._WechatUnionId

    @WechatUnionId.setter
    def WechatUnionId(self, WechatUnionId):
        self._WechatUnionId = WechatUnionId

    @property
    def AlipayUserId(self):
        return self._AlipayUserId

    @AlipayUserId.setter
    def AlipayUserId(self, AlipayUserId):
        self._AlipayUserId = AlipayUserId

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Birthdate(self):
        return self._Birthdate

    @Birthdate.setter
    def Birthdate(self, Birthdate):
        self._Birthdate = Birthdate

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Locale(self):
        return self._Locale

    @Locale.setter
    def Locale(self, Locale):
        self._Locale = Locale

    @property
    def Gender(self):
        return self._Gender

    @Gender.setter
    def Gender(self, Gender):
        self._Gender = Gender

    @property
    def IdentityVerificationMethod(self):
        return self._IdentityVerificationMethod

    @IdentityVerificationMethod.setter
    def IdentityVerificationMethod(self, IdentityVerificationMethod):
        self._IdentityVerificationMethod = IdentityVerificationMethod

    @property
    def IdentityVerified(self):
        return self._IdentityVerified

    @IdentityVerified.setter
    def IdentityVerified(self, IdentityVerified):
        self._IdentityVerified = IdentityVerified

    @property
    def Job(self):
        return self._Job

    @Job.setter
    def Job(self, Job):
        self._Job = Job

    @property
    def Nationality(self):
        return self._Nationality

    @Nationality.setter
    def Nationality(self, Nationality):
        self._Nationality = Nationality

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def CustomizationAttributes(self):
        return self._CustomizationAttributes

    @CustomizationAttributes.setter
    def CustomizationAttributes(self, CustomizationAttributes):
        self._CustomizationAttributes = CustomizationAttributes

    @property
    def Salt(self):
        return self._Salt

    @Salt.setter
    def Salt(self, Salt):
        self._Salt = Salt

    @property
    def PasswordEncryptTypeEnum(self):
        return self._PasswordEncryptTypeEnum

    @PasswordEncryptTypeEnum.setter
    def PasswordEncryptTypeEnum(self, PasswordEncryptTypeEnum):
        self._PasswordEncryptTypeEnum = PasswordEncryptTypeEnum

    @property
    def IndexedAttribute1(self):
        return self._IndexedAttribute1

    @IndexedAttribute1.setter
    def IndexedAttribute1(self, IndexedAttribute1):
        self._IndexedAttribute1 = IndexedAttribute1

    @property
    def IndexedAttribute2(self):
        return self._IndexedAttribute2

    @IndexedAttribute2.setter
    def IndexedAttribute2(self, IndexedAttribute2):
        self._IndexedAttribute2 = IndexedAttribute2

    @property
    def IndexedAttribute3(self):
        return self._IndexedAttribute3

    @IndexedAttribute3.setter
    def IndexedAttribute3(self, IndexedAttribute3):
        self._IndexedAttribute3 = IndexedAttribute3

    @property
    def IndexedAttribute4(self):
        return self._IndexedAttribute4

    @IndexedAttribute4.setter
    def IndexedAttribute4(self, IndexedAttribute4):
        self._IndexedAttribute4 = IndexedAttribute4

    @property
    def IndexedAttribute5(self):
        return self._IndexedAttribute5

    @IndexedAttribute5.setter
    def IndexedAttribute5(self, IndexedAttribute5):
        self._IndexedAttribute5 = IndexedAttribute5


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._PhoneNumber = params.get("PhoneNumber")
        self._Email = params.get("Email")
        self._ResidentIdentityCard = params.get("ResidentIdentityCard")
        self._Nickname = params.get("Nickname")
        self._Address = params.get("Address")
        self._UserGroup = params.get("UserGroup")
        self._QqOpenId = params.get("QqOpenId")
        self._QqUnionId = params.get("QqUnionId")
        self._WechatOpenId = params.get("WechatOpenId")
        self._WechatUnionId = params.get("WechatUnionId")
        self._AlipayUserId = params.get("AlipayUserId")
        self._Description = params.get("Description")
        self._Birthdate = params.get("Birthdate")
        self._Name = params.get("Name")
        self._Locale = params.get("Locale")
        self._Gender = params.get("Gender")
        self._IdentityVerificationMethod = params.get("IdentityVerificationMethod")
        self._IdentityVerified = params.get("IdentityVerified")
        self._Job = params.get("Job")
        self._Nationality = params.get("Nationality")
        self._Zone = params.get("Zone")
        self._Password = params.get("Password")
        if params.get("CustomizationAttributes") is not None:
            self._CustomizationAttributes = []
            for item in params.get("CustomizationAttributes"):
                obj = MemberMap()
                obj._deserialize(item)
                self._CustomizationAttributes.append(obj)
        if params.get("Salt") is not None:
            self._Salt = Salt()
            self._Salt._deserialize(params.get("Salt"))
        self._PasswordEncryptTypeEnum = params.get("PasswordEncryptTypeEnum")
        self._IndexedAttribute1 = params.get("IndexedAttribute1")
        self._IndexedAttribute2 = params.get("IndexedAttribute2")
        self._IndexedAttribute3 = params.get("IndexedAttribute3")
        self._IndexedAttribute4 = params.get("IndexedAttribute4")
        self._IndexedAttribute5 = params.get("IndexedAttribute5")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Job(AbstractModel):
    """Task details

    """

    def __init__(self):
        r"""
        :param _Id: Task ID
        :type Id: str
        :param _Status: Task status

<li> **PENDING** </li>  Pending
<li> **PROCESSING** </li>  Executing
<li> **COMPLETED** </li>  Completed
<li> **FAILED** </li>  Failed
        :type Status: str
        :param _Type: Task type

<li> **IMPORT_USER** </li>  User import
<li> **EXPORT_USER** </li>  User export
        :type Type: str
        :param _CreatedDate: Task creation time
        :type CreatedDate: int
        :param _Format: Data type of the task

<li> **NDJSON** </li>  New-line Delimited JSON
<li> **CSV** </li>  Comma-Separated Values
Note: this field may return null, indicating that no valid values can be obtained.
        :type Format: str
        :param _Location: Task result download address
Note: This field may return null, indicating that no valid values can be obtained.
        :type Location: str
        :param _ErrorDetails: Failure details
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorDetails: list of ErrorDetails
        :param _FailedUsers: Failed user
Note: This field may return null, indicating that no valid values can be obtained.
        :type FailedUsers: list of FailedUsers
        """
        self._Id = None
        self._Status = None
        self._Type = None
        self._CreatedDate = None
        self._Format = None
        self._Location = None
        self._ErrorDetails = None
        self._FailedUsers = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CreatedDate(self):
        return self._CreatedDate

    @CreatedDate.setter
    def CreatedDate(self, CreatedDate):
        self._CreatedDate = CreatedDate

    @property
    def Format(self):
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def ErrorDetails(self):
        return self._ErrorDetails

    @ErrorDetails.setter
    def ErrorDetails(self, ErrorDetails):
        self._ErrorDetails = ErrorDetails

    @property
    def FailedUsers(self):
        return self._FailedUsers

    @FailedUsers.setter
    def FailedUsers(self, FailedUsers):
        self._FailedUsers = FailedUsers


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Status = params.get("Status")
        self._Type = params.get("Type")
        self._CreatedDate = params.get("CreatedDate")
        self._Format = params.get("Format")
        self._Location = params.get("Location")
        if params.get("ErrorDetails") is not None:
            self._ErrorDetails = []
            for item in params.get("ErrorDetails"):
                obj = ErrorDetails()
                obj._deserialize(item)
                self._ErrorDetails.append(obj)
        if params.get("FailedUsers") is not None:
            self._FailedUsers = []
            for item in params.get("FailedUsers"):
                obj = FailedUsers()
                obj._deserialize(item)
                self._FailedUsers.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LinkAccountRequest(AbstractModel):
    """LinkAccount request structure.

    """

    def __init__(self):
        r"""
        :param _UserStoreId: User directory ID
        :type UserStoreId: str
        :param _PrimaryUserId: Primary user ID
        :type PrimaryUserId: str
        :param _SecondaryUserId: Secondary user ID
        :type SecondaryUserId: str
        :param _UserLinkedOnAttribute: Fusion attribute

<li> **PHONENUMBER** </li>	  Mobile number
<li> **EMAIL** </li>  Email
        :type UserLinkedOnAttribute: str
        """
        self._UserStoreId = None
        self._PrimaryUserId = None
        self._SecondaryUserId = None
        self._UserLinkedOnAttribute = None

    @property
    def UserStoreId(self):
        return self._UserStoreId

    @UserStoreId.setter
    def UserStoreId(self, UserStoreId):
        self._UserStoreId = UserStoreId

    @property
    def PrimaryUserId(self):
        return self._PrimaryUserId

    @PrimaryUserId.setter
    def PrimaryUserId(self, PrimaryUserId):
        self._PrimaryUserId = PrimaryUserId

    @property
    def SecondaryUserId(self):
        return self._SecondaryUserId

    @SecondaryUserId.setter
    def SecondaryUserId(self, SecondaryUserId):
        self._SecondaryUserId = SecondaryUserId

    @property
    def UserLinkedOnAttribute(self):
        return self._UserLinkedOnAttribute

    @UserLinkedOnAttribute.setter
    def UserLinkedOnAttribute(self, UserLinkedOnAttribute):
        self._UserLinkedOnAttribute = UserLinkedOnAttribute


    def _deserialize(self, params):
        self._UserStoreId = params.get("UserStoreId")
        self._PrimaryUserId = params.get("PrimaryUserId")
        self._SecondaryUserId = params.get("SecondaryUserId")
        self._UserLinkedOnAttribute = params.get("UserLinkedOnAttribute")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LinkAccountResponse(AbstractModel):
    """LinkAccount response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ListJobsRequest(AbstractModel):
    """ListJobs request structure.

    """

    def __init__(self):
        r"""
        :param _UserStoreId: User directory ID
        :type UserStoreId: str
        :param _JobIds: List of task IDs. If this parameter is empty, all tasks will be returned.
        :type JobIds: list of str
        """
        self._UserStoreId = None
        self._JobIds = None

    @property
    def UserStoreId(self):
        return self._UserStoreId

    @UserStoreId.setter
    def UserStoreId(self, UserStoreId):
        self._UserStoreId = UserStoreId

    @property
    def JobIds(self):
        return self._JobIds

    @JobIds.setter
    def JobIds(self, JobIds):
        self._JobIds = JobIds


    def _deserialize(self, params):
        self._UserStoreId = params.get("UserStoreId")
        self._JobIds = params.get("JobIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListJobsResponse(AbstractModel):
    """ListJobs response structure.

    """

    def __init__(self):
        r"""
        :param _JobSet: List of tasks
Note: This field may return null, indicating that no valid values can be obtained.
        :type JobSet: list of Job
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._JobSet = None
        self._RequestId = None

    @property
    def JobSet(self):
        return self._JobSet

    @JobSet.setter
    def JobSet(self, JobSet):
        self._JobSet = JobSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("JobSet") is not None:
            self._JobSet = []
            for item in params.get("JobSet"):
                obj = Job()
                obj._deserialize(item)
                self._JobSet.append(obj)
        self._RequestId = params.get("RequestId")


class ListLogMessageByConditionRequest(AbstractModel):
    """ListLogMessageByCondition request structure.

    """

    def __init__(self):
        r"""
        :param _UserStoreId: User pool ID
        :type UserStoreId: str
        :param _Pageable: Pagination data
        :type Pageable: :class:`tencentcloud.ciam.v20220331.models.Pageable`
        :param _StartTime: Start timestamp accurate to the millisecond
        :type StartTime: int
        :param _Filters: Valid values of `Key`: `events`.

<li> **events** </li>	Values can be one or multiple items in ["SIGNUP", "USER_UPDATE", "USER_DELETE", "USER_CREATE", "ACCOUNT_LINKING"].
        :type Filters: list of Filter
        """
        self._UserStoreId = None
        self._Pageable = None
        self._StartTime = None
        self._Filters = None

    @property
    def UserStoreId(self):
        return self._UserStoreId

    @UserStoreId.setter
    def UserStoreId(self, UserStoreId):
        self._UserStoreId = UserStoreId

    @property
    def Pageable(self):
        return self._Pageable

    @Pageable.setter
    def Pageable(self, Pageable):
        self._Pageable = Pageable

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._UserStoreId = params.get("UserStoreId")
        if params.get("Pageable") is not None:
            self._Pageable = Pageable()
            self._Pageable._deserialize(params.get("Pageable"))
        self._StartTime = params.get("StartTime")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListLogMessageByConditionResponse(AbstractModel):
    """ListLogMessageByCondition response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total number
        :type Total: int
        :param _Pageable: Pagination object
        :type Pageable: :class:`tencentcloud.ciam.v20220331.models.Pageable`
        :param _Content: List of logs
Note: This field may return null, indicating that no valid values can be obtained.
        :type Content: list of LogMessage
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._Pageable = None
        self._Content = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Pageable(self):
        return self._Pageable

    @Pageable.setter
    def Pageable(self, Pageable):
        self._Pageable = Pageable

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Pageable") is not None:
            self._Pageable = Pageable()
            self._Pageable._deserialize(params.get("Pageable"))
        if params.get("Content") is not None:
            self._Content = []
            for item in params.get("Content"):
                obj = LogMessage()
                obj._deserialize(item)
                self._Content.append(obj)
        self._RequestId = params.get("RequestId")


class ListUserByPropertyRequest(AbstractModel):
    """ListUserByProperty request structure.

    """

    def __init__(self):
        r"""
        :param _UserStoreId: User directory ID
        :type UserStoreId: str
        :param _PropertyCode: Query attribute

<li> **phoneNumber** </li>	  Mobile number
<li> **email** </li>  Email
        :type PropertyCode: str
        :param _PropertyValue: Attribute value
        :type PropertyValue: str
        :param _Original: Whether the content is passed through
        :type Original: bool
        """
        self._UserStoreId = None
        self._PropertyCode = None
        self._PropertyValue = None
        self._Original = None

    @property
    def UserStoreId(self):
        return self._UserStoreId

    @UserStoreId.setter
    def UserStoreId(self, UserStoreId):
        self._UserStoreId = UserStoreId

    @property
    def PropertyCode(self):
        return self._PropertyCode

    @PropertyCode.setter
    def PropertyCode(self, PropertyCode):
        self._PropertyCode = PropertyCode

    @property
    def PropertyValue(self):
        return self._PropertyValue

    @PropertyValue.setter
    def PropertyValue(self, PropertyValue):
        self._PropertyValue = PropertyValue

    @property
    def Original(self):
        return self._Original

    @Original.setter
    def Original(self, Original):
        self._Original = Original


    def _deserialize(self, params):
        self._UserStoreId = params.get("UserStoreId")
        self._PropertyCode = params.get("PropertyCode")
        self._PropertyValue = params.get("PropertyValue")
        self._Original = params.get("Original")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListUserByPropertyResponse(AbstractModel):
    """ListUserByProperty response structure.

    """

    def __init__(self):
        r"""
        :param _Users: List of users
Note: This field may return null, indicating that no valid values can be obtained.
        :type Users: list of User
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Users = None
        self._RequestId = None

    @property
    def Users(self):
        return self._Users

    @Users.setter
    def Users(self, Users):
        self._Users = Users

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Users") is not None:
            self._Users = []
            for item in params.get("Users"):
                obj = User()
                obj._deserialize(item)
                self._Users.append(obj)
        self._RequestId = params.get("RequestId")


class ListUserRequest(AbstractModel):
    """ListUser request structure.

    """

    def __init__(self):
        r"""
        :param _UserStoreId: User directory ID
        :type UserStoreId: str
        :param _Pageable: Pagination data
        :type Pageable: :class:`tencentcloud.ciam.v20220331.models.Pageable`
        :param _Filters: Valid values of `Key`: `condition`, `userGroupId`.

<li> **condition** </li>	Values = Query condition, which can be user ID, username, mobile number, or email address.
<li> **userGroupId** </li>	Values = User group ID
        :type Filters: list of Filter
        :param _Original: Whether the content is passed through
        :type Original: bool
        """
        self._UserStoreId = None
        self._Pageable = None
        self._Filters = None
        self._Original = None

    @property
    def UserStoreId(self):
        return self._UserStoreId

    @UserStoreId.setter
    def UserStoreId(self, UserStoreId):
        self._UserStoreId = UserStoreId

    @property
    def Pageable(self):
        return self._Pageable

    @Pageable.setter
    def Pageable(self, Pageable):
        self._Pageable = Pageable

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Original(self):
        return self._Original

    @Original.setter
    def Original(self, Original):
        self._Original = Original


    def _deserialize(self, params):
        self._UserStoreId = params.get("UserStoreId")
        if params.get("Pageable") is not None:
            self._Pageable = Pageable()
            self._Pageable._deserialize(params.get("Pageable"))
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Original = params.get("Original")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListUserResponse(AbstractModel):
    """ListUser response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total number
Note: This field may return null, indicating that no valid values can be obtained.
        :type Total: int
        :param _Pageable: Pagination object
Note: This field may return null, indicating that no valid values can be obtained.
        :type Pageable: :class:`tencentcloud.ciam.v20220331.models.Pageable`
        :param _Content: List of users
Note: This field may return null, indicating that no valid values can be obtained.
        :type Content: list of User
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._Pageable = None
        self._Content = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Pageable(self):
        return self._Pageable

    @Pageable.setter
    def Pageable(self, Pageable):
        self._Pageable = Pageable

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Pageable") is not None:
            self._Pageable = Pageable()
            self._Pageable._deserialize(params.get("Pageable"))
        if params.get("Content") is not None:
            self._Content = []
            for item in params.get("Content"):
                obj = User()
                obj._deserialize(item)
                self._Content.append(obj)
        self._RequestId = params.get("RequestId")


class LogMessage(AbstractModel):
    """Log details

    """

    def __init__(self):
        r"""
        :param _LogId: Log ID
        :type LogId: str
        :param _TenantId: Tenant ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type TenantId: str
        :param _UserStoreId: User pool ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type UserStoreId: str
        :param _EventCode: Event code
Note: This field may return null, indicating that no valid values can be obtained.
        :type EventCode: str
        :param _EventDate: Event timestamp in milliseconds
Note: This field may return null, indicating that no valid values can be obtained.
        :type EventDate: int
        :param _Description: Description
Note: This field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param _Participant: Event participant

<li> **TENANT** </li>  Tenant
<li> **USER** </li>  User
Note: This field may return null, indicating that no valid values can be obtained.
        :type Participant: str
        :param _ApplicationClientId: Application `clientId`
Note: This field may return null, indicating that no valid values can be obtained.
        :type ApplicationClientId: str
        :param _ApplicationName: Application name
Note: This field may return null, indicating that no valid values can be obtained.
        :type ApplicationName: str
        :param _AuthSourceId: Authentication source ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type AuthSourceId: str
        :param _AuthSourceName: Authentication source name
Note: This field may return null, indicating that no valid values can be obtained.
        :type AuthSourceName: str
        :param _AuthSourceType: Authentication source type
Note: This field may return null, indicating that no valid values can be obtained.
        :type AuthSourceType: str
        :param _AuthSourceCategory: Authentication source category
Note: This field may return null, indicating that no valid values can be obtained.
        :type AuthSourceCategory: str
        :param _Ip: IP address
Note: This field may return null, indicating that no valid values can be obtained.
        :type Ip: str
        :param _UserAgent: User agent
Note: This field may return null, indicating that no valid values can be obtained.
        :type UserAgent: str
        :param _UserId: User ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type UserId: str
        :param _Detail: Details
Note: This field may return null, indicating that no valid values can be obtained.
        :type Detail: str
        """
        self._LogId = None
        self._TenantId = None
        self._UserStoreId = None
        self._EventCode = None
        self._EventDate = None
        self._Description = None
        self._Participant = None
        self._ApplicationClientId = None
        self._ApplicationName = None
        self._AuthSourceId = None
        self._AuthSourceName = None
        self._AuthSourceType = None
        self._AuthSourceCategory = None
        self._Ip = None
        self._UserAgent = None
        self._UserId = None
        self._Detail = None

    @property
    def LogId(self):
        return self._LogId

    @LogId.setter
    def LogId(self, LogId):
        self._LogId = LogId

    @property
    def TenantId(self):
        return self._TenantId

    @TenantId.setter
    def TenantId(self, TenantId):
        self._TenantId = TenantId

    @property
    def UserStoreId(self):
        return self._UserStoreId

    @UserStoreId.setter
    def UserStoreId(self, UserStoreId):
        self._UserStoreId = UserStoreId

    @property
    def EventCode(self):
        return self._EventCode

    @EventCode.setter
    def EventCode(self, EventCode):
        self._EventCode = EventCode

    @property
    def EventDate(self):
        return self._EventDate

    @EventDate.setter
    def EventDate(self, EventDate):
        self._EventDate = EventDate

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Participant(self):
        return self._Participant

    @Participant.setter
    def Participant(self, Participant):
        self._Participant = Participant

    @property
    def ApplicationClientId(self):
        return self._ApplicationClientId

    @ApplicationClientId.setter
    def ApplicationClientId(self, ApplicationClientId):
        self._ApplicationClientId = ApplicationClientId

    @property
    def ApplicationName(self):
        return self._ApplicationName

    @ApplicationName.setter
    def ApplicationName(self, ApplicationName):
        self._ApplicationName = ApplicationName

    @property
    def AuthSourceId(self):
        return self._AuthSourceId

    @AuthSourceId.setter
    def AuthSourceId(self, AuthSourceId):
        self._AuthSourceId = AuthSourceId

    @property
    def AuthSourceName(self):
        return self._AuthSourceName

    @AuthSourceName.setter
    def AuthSourceName(self, AuthSourceName):
        self._AuthSourceName = AuthSourceName

    @property
    def AuthSourceType(self):
        return self._AuthSourceType

    @AuthSourceType.setter
    def AuthSourceType(self, AuthSourceType):
        self._AuthSourceType = AuthSourceType

    @property
    def AuthSourceCategory(self):
        return self._AuthSourceCategory

    @AuthSourceCategory.setter
    def AuthSourceCategory(self, AuthSourceCategory):
        self._AuthSourceCategory = AuthSourceCategory

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def UserAgent(self):
        return self._UserAgent

    @UserAgent.setter
    def UserAgent(self, UserAgent):
        self._UserAgent = UserAgent

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Detail(self):
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail


    def _deserialize(self, params):
        self._LogId = params.get("LogId")
        self._TenantId = params.get("TenantId")
        self._UserStoreId = params.get("UserStoreId")
        self._EventCode = params.get("EventCode")
        self._EventDate = params.get("EventDate")
        self._Description = params.get("Description")
        self._Participant = params.get("Participant")
        self._ApplicationClientId = params.get("ApplicationClientId")
        self._ApplicationName = params.get("ApplicationName")
        self._AuthSourceId = params.get("AuthSourceId")
        self._AuthSourceName = params.get("AuthSourceName")
        self._AuthSourceType = params.get("AuthSourceType")
        self._AuthSourceCategory = params.get("AuthSourceCategory")
        self._Ip = params.get("Ip")
        self._UserAgent = params.get("UserAgent")
        self._UserId = params.get("UserId")
        self._Detail = params.get("Detail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MemberMap(AbstractModel):
    """Map data type

    """

    def __init__(self):
        r"""
        :param _Name: Key
        :type Name: str
        :param _Value: Value
        :type Value: str
        :param _Type: Type
Note: This field may return null, indicating that no valid values can be obtained.
        :type Type: str
        """
        self._Name = None
        self._Value = None
        self._Type = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Pageable(AbstractModel):
    """Pagination object

    """

    def __init__(self):
        r"""
        :param _PageSize: Number of entries per page
        :type PageSize: int
        :param _PageNumber: Current page number
        :type PageNumber: int
        """
        self._PageSize = None
        self._PageNumber = None

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber


    def _deserialize(self, params):
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryUserFilter(AbstractModel):
    """Conditions to query the user information

    """

    def __init__(self):
        r"""
        :param _PropertyKey: Property key
        :type PropertyKey: str
        :param _PropertyValue: Property value
        :type PropertyValue: str
        :param _Logic: Logic value. `True` or `False`
        :type Logic: bool
        :param _OperateLogic: Operator. Values: `>`, `<`, `=`, `>=`, `<=`, `!=` and `between`. 
        :type OperateLogic: str
        """
        self._PropertyKey = None
        self._PropertyValue = None
        self._Logic = None
        self._OperateLogic = None

    @property
    def PropertyKey(self):
        return self._PropertyKey

    @PropertyKey.setter
    def PropertyKey(self, PropertyKey):
        self._PropertyKey = PropertyKey

    @property
    def PropertyValue(self):
        return self._PropertyValue

    @PropertyValue.setter
    def PropertyValue(self, PropertyValue):
        self._PropertyValue = PropertyValue

    @property
    def Logic(self):
        return self._Logic

    @Logic.setter
    def Logic(self, Logic):
        self._Logic = Logic

    @property
    def OperateLogic(self):
        return self._OperateLogic

    @OperateLogic.setter
    def OperateLogic(self, OperateLogic):
        self._OperateLogic = OperateLogic


    def _deserialize(self, params):
        self._PropertyKey = params.get("PropertyKey")
        self._PropertyValue = params.get("PropertyValue")
        self._Logic = params.get("Logic")
        self._OperateLogic = params.get("OperateLogic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetPasswordRequest(AbstractModel):
    """ResetPassword request structure.

    """

    def __init__(self):
        r"""
        :param _UserId: User ID
        :type UserId: str
        :param _UserStoreId: User directory ID
        :type UserStoreId: str
        """
        self._UserId = None
        self._UserStoreId = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserStoreId(self):
        return self._UserStoreId

    @UserStoreId.setter
    def UserStoreId(self, UserStoreId):
        self._UserStoreId = UserStoreId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._UserStoreId = params.get("UserStoreId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetPasswordResponse(AbstractModel):
    """ResetPassword response structure.

    """

    def __init__(self):
        r"""
        :param _Password: User password after reset
        :type Password: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Password = None
        self._RequestId = None

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Password = params.get("Password")
        self._RequestId = params.get("RequestId")


class Salt(AbstractModel):
    """Password salt

    """

    def __init__(self):
        r"""
        :param _SaltValue: Salt value
        :type SaltValue: str
        :param _SaltLocation: Salt value location
        :type SaltLocation: :class:`tencentcloud.ciam.v20220331.models.SaltLocation`
        """
        self._SaltValue = None
        self._SaltLocation = None

    @property
    def SaltValue(self):
        return self._SaltValue

    @SaltValue.setter
    def SaltValue(self, SaltValue):
        self._SaltValue = SaltValue

    @property
    def SaltLocation(self):
        return self._SaltLocation

    @SaltLocation.setter
    def SaltLocation(self, SaltLocation):
        self._SaltLocation = SaltLocation


    def _deserialize(self, params):
        self._SaltValue = params.get("SaltValue")
        if params.get("SaltLocation") is not None:
            self._SaltLocation = SaltLocation()
            self._SaltLocation._deserialize(params.get("SaltLocation"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SaltLocation(AbstractModel):
    """Salt location

    """

    def __init__(self):
        r"""
        :param _SaltLocationTypeEnum: Password salt type. Valid values: `HEAD`, `TAIL`, `OTHER`.
        :type SaltLocationTypeEnum: str
        :param _SaltLocationRule: Salting rule
        :type SaltLocationRule: :class:`tencentcloud.ciam.v20220331.models.SaltLocationRule`
        """
        self._SaltLocationTypeEnum = None
        self._SaltLocationRule = None

    @property
    def SaltLocationTypeEnum(self):
        return self._SaltLocationTypeEnum

    @SaltLocationTypeEnum.setter
    def SaltLocationTypeEnum(self, SaltLocationTypeEnum):
        self._SaltLocationTypeEnum = SaltLocationTypeEnum

    @property
    def SaltLocationRule(self):
        return self._SaltLocationRule

    @SaltLocationRule.setter
    def SaltLocationRule(self, SaltLocationRule):
        self._SaltLocationRule = SaltLocationRule


    def _deserialize(self, params):
        self._SaltLocationTypeEnum = params.get("SaltLocationTypeEnum")
        if params.get("SaltLocationRule") is not None:
            self._SaltLocationRule = SaltLocationRule()
            self._SaltLocationRule._deserialize(params.get("SaltLocationRule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SaltLocationRule(AbstractModel):
    """Salt location rule

    """

    def __init__(self):
        r"""
        :param _Regex: Expression
        :type Regex: str
        """
        self._Regex = None

    @property
    def Regex(self):
        return self._Regex

    @Regex.setter
    def Regex(self, Regex):
        self._Regex = Regex


    def _deserialize(self, params):
        self._Regex = params.get("Regex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetPasswordRequest(AbstractModel):
    """SetPassword request structure.

    """

    def __init__(self):
        r"""
        :param _UserStoreId: User directory ID
        :type UserStoreId: str
        :param _UserId: User ID
        :type UserId: str
        :param _Password: Password
        :type Password: str
        """
        self._UserStoreId = None
        self._UserId = None
        self._Password = None

    @property
    def UserStoreId(self):
        return self._UserStoreId

    @UserStoreId.setter
    def UserStoreId(self, UserStoreId):
        self._UserStoreId = UserStoreId

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password


    def _deserialize(self, params):
        self._UserStoreId = params.get("UserStoreId")
        self._UserId = params.get("UserId")
        self._Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetPasswordResponse(AbstractModel):
    """SetPassword response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Sort(AbstractModel):
    """Sorting of the result of user query

    """

    def __init__(self):
        r"""
        :param _PropertyKey: Key for sorting. See custom attributes
        :type PropertyKey: str
        :param _Order: `ASC` or `DESC`
        :type Order: str
        """
        self._PropertyKey = None
        self._Order = None

    @property
    def PropertyKey(self):
        return self._PropertyKey

    @PropertyKey.setter
    def PropertyKey(self, PropertyKey):
        self._PropertyKey = PropertyKey

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order


    def _deserialize(self, params):
        self._PropertyKey = params.get("PropertyKey")
        self._Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateUserRequest(AbstractModel):
    """UpdateUser request structure.

    """

    def __init__(self):
        r"""
        :param _UserId: User ID
        :type UserId: str
        :param _UserStoreId: User directory ID
        :type UserStoreId: str
        :param _UserName: Username
        :type UserName: str
        :param _PhoneNumber: Mobile number
        :type PhoneNumber: str
        :param _Email: Email address
        :type Email: str
        :param _Nickname: Nickname
        :type Nickname: str
        :param _Address: Address
        :type Address: str
        :param _UserGroup: User group
        :type UserGroup: list of str
        :param _Birthdate: Date of birth
        :type Birthdate: int
        :param _CustomizationAttributes: Custom attribute
        :type CustomizationAttributes: list of MemberMap
        :param _IndexedAttribute1: Index field 1
        :type IndexedAttribute1: str
        :param _IndexedAttribute2: Index field 2
        :type IndexedAttribute2: str
        :param _IndexedAttribute3: Index field 3
        :type IndexedAttribute3: str
        :param _IndexedAttribute4: Index field 4
        :type IndexedAttribute4: str
        :param _IndexedAttribute5: Index field 5
        :type IndexedAttribute5: str
        """
        self._UserId = None
        self._UserStoreId = None
        self._UserName = None
        self._PhoneNumber = None
        self._Email = None
        self._Nickname = None
        self._Address = None
        self._UserGroup = None
        self._Birthdate = None
        self._CustomizationAttributes = None
        self._IndexedAttribute1 = None
        self._IndexedAttribute2 = None
        self._IndexedAttribute3 = None
        self._IndexedAttribute4 = None
        self._IndexedAttribute5 = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserStoreId(self):
        return self._UserStoreId

    @UserStoreId.setter
    def UserStoreId(self, UserStoreId):
        self._UserStoreId = UserStoreId

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def PhoneNumber(self):
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def Nickname(self):
        return self._Nickname

    @Nickname.setter
    def Nickname(self, Nickname):
        self._Nickname = Nickname

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def UserGroup(self):
        return self._UserGroup

    @UserGroup.setter
    def UserGroup(self, UserGroup):
        self._UserGroup = UserGroup

    @property
    def Birthdate(self):
        return self._Birthdate

    @Birthdate.setter
    def Birthdate(self, Birthdate):
        self._Birthdate = Birthdate

    @property
    def CustomizationAttributes(self):
        return self._CustomizationAttributes

    @CustomizationAttributes.setter
    def CustomizationAttributes(self, CustomizationAttributes):
        self._CustomizationAttributes = CustomizationAttributes

    @property
    def IndexedAttribute1(self):
        return self._IndexedAttribute1

    @IndexedAttribute1.setter
    def IndexedAttribute1(self, IndexedAttribute1):
        self._IndexedAttribute1 = IndexedAttribute1

    @property
    def IndexedAttribute2(self):
        return self._IndexedAttribute2

    @IndexedAttribute2.setter
    def IndexedAttribute2(self, IndexedAttribute2):
        self._IndexedAttribute2 = IndexedAttribute2

    @property
    def IndexedAttribute3(self):
        return self._IndexedAttribute3

    @IndexedAttribute3.setter
    def IndexedAttribute3(self, IndexedAttribute3):
        self._IndexedAttribute3 = IndexedAttribute3

    @property
    def IndexedAttribute4(self):
        return self._IndexedAttribute4

    @IndexedAttribute4.setter
    def IndexedAttribute4(self, IndexedAttribute4):
        self._IndexedAttribute4 = IndexedAttribute4

    @property
    def IndexedAttribute5(self):
        return self._IndexedAttribute5

    @IndexedAttribute5.setter
    def IndexedAttribute5(self, IndexedAttribute5):
        self._IndexedAttribute5 = IndexedAttribute5


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._UserStoreId = params.get("UserStoreId")
        self._UserName = params.get("UserName")
        self._PhoneNumber = params.get("PhoneNumber")
        self._Email = params.get("Email")
        self._Nickname = params.get("Nickname")
        self._Address = params.get("Address")
        self._UserGroup = params.get("UserGroup")
        self._Birthdate = params.get("Birthdate")
        if params.get("CustomizationAttributes") is not None:
            self._CustomizationAttributes = []
            for item in params.get("CustomizationAttributes"):
                obj = MemberMap()
                obj._deserialize(item)
                self._CustomizationAttributes.append(obj)
        self._IndexedAttribute1 = params.get("IndexedAttribute1")
        self._IndexedAttribute2 = params.get("IndexedAttribute2")
        self._IndexedAttribute3 = params.get("IndexedAttribute3")
        self._IndexedAttribute4 = params.get("IndexedAttribute4")
        self._IndexedAttribute5 = params.get("IndexedAttribute5")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateUserResponse(AbstractModel):
    """UpdateUser response structure.

    """

    def __init__(self):
        r"""
        :param _User: User information after update
Note: This field may return null, indicating that no valid values can be obtained.
        :type User: :class:`tencentcloud.ciam.v20220331.models.User`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._User = None
        self._RequestId = None

    @property
    def User(self):
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("User") is not None:
            self._User = User()
            self._User._deserialize(params.get("User"))
        self._RequestId = params.get("RequestId")


class UpdateUserStatusRequest(AbstractModel):
    """UpdateUserStatus request structure.

    """

    def __init__(self):
        r"""
        :param _UserStoreId: User directory ID
        :type UserStoreId: str
        :param _UserId: User ID
        :type UserId: str
        :param _Status: User status

<li> **NORMAL** </li>	  Normal
<li> **LOCK** </li>  Locked
<li> **FREEZE** </li>	  Frozen
        :type Status: str
        """
        self._UserStoreId = None
        self._UserId = None
        self._Status = None

    @property
    def UserStoreId(self):
        return self._UserStoreId

    @UserStoreId.setter
    def UserStoreId(self, UserStoreId):
        self._UserStoreId = UserStoreId

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._UserStoreId = params.get("UserStoreId")
        self._UserId = params.get("UserId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateUserStatusResponse(AbstractModel):
    """UpdateUserStatus response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class User(AbstractModel):
    """User information

    """

    def __init__(self):
        r"""
        :param _UserId: User ID
        :type UserId: str
        :param _UserName: Username
Note: This field may return null, indicating that no valid values can be obtained.
        :type UserName: str
        :param _PhoneNumber: Mobile number
Note: This field may return null, indicating that no valid values can be obtained.
        :type PhoneNumber: str
        :param _Email: Email address
Note: This field may return null, indicating that no valid values can be obtained.
        :type Email: str
        :param _LastSignOn: Last login time
Note: This field may return null, indicating that no valid values can be obtained.
        :type LastSignOn: int
        :param _CreatedDate: Creation time
        :type CreatedDate: int
        :param _Status: Status
        :type Status: str
        :param _UserDataSourceEnum: User source
        :type UserDataSourceEnum: str
        :param _Nickname: Nickname
Note: This field may return null, indicating that no valid values can be obtained.
        :type Nickname: str
        :param _Address: Address
Note: This field may return null, indicating that no valid values can be obtained.
        :type Address: str
        :param _Birthdate: Date of birth
Note: This field may return null, indicating that no valid values can be obtained.
        :type Birthdate: int
        :param _UserGroups: User group ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type UserGroups: list of str
        :param _LastModifiedDate: Last modified time
Note: This field may return null, indicating that no valid values can be obtained.
        :type LastModifiedDate: int
        :param _CustomAttributes: Custom attribute
Note: This field may return null, indicating that no valid values can be obtained.
        :type CustomAttributes: list of MemberMap
        :param _ResidentIdentityCard: ID card number
Note: This field may return null, indicating that no valid values can be obtained.
        :type ResidentIdentityCard: str
        :param _QqOpenId: `OpenId` on QQ
Note: This field may return null, indicating that no valid values can be obtained.
        :type QqOpenId: str
        :param _QqUnionId: `UnionId` on QQ
Note: This field may return null, indicating that no valid values can be obtained.
        :type QqUnionId: str
        :param _WechatOpenId: `WechatOpenId` on WeChat
Note: This field may return null, indicating that no valid values can be obtained.
        :type WechatOpenId: str
        :param _WechatUnionId: `WechatUnionId` on WeChat
Note: This field may return null, indicating that no valid values can be obtained.
        :type WechatUnionId: str
        :param _AlipayUserId: `AlipayUserId` on Alipay
Note: This field may return null, indicating that no valid values can be obtained.
        :type AlipayUserId: str
        :param _Description: Description
Note: This field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param _Name: Name
Note: This field may return null, indicating that no valid values can be obtained.
        :type Name: str
        :param _Locale: Coordinate
Note: This field may return null, indicating that no valid values can be obtained.
        :type Locale: str
        :param _Gender: Gender
Note: This field may return null, indicating that no valid values can be obtained.
        :type Gender: str
        :param _IdentityVerificationMethod: Identity verification method
Note: This field may return null, indicating that no valid values can be obtained.
        :type IdentityVerificationMethod: str
        :param _IdentityVerified: Whether the identity is verified
Note: This field may return null, indicating that no valid values can be obtained.
        :type IdentityVerified: bool
        :param _Job: Job
Note: This field may return null, indicating that no valid values can be obtained.
        :type Job: str
        :param _Nationality: Country/Region
Note: This field may return null, indicating that no valid values can be obtained.
        :type Nationality: str
        :param _Primary: Whether the account is the primary account (after account merge, this parameter is `true` for primary accounts and `false` for secondary account).
Note: This field may return null, indicating that no valid values can be obtained.
        :type Primary: bool
        :param _Zone: Time zone
Note: This field may return null, indicating that no valid values can be obtained.
        :type Zone: str
        :param _AlreadyFirstLogin: Whether the account has ever logged in.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AlreadyFirstLogin: bool
        :param _TenantId: Tenant ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type TenantId: str
        :param _UserStoreId: User directory ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type UserStoreId: str
        :param _Version: Version
Note: This field may return null, indicating that no valid values can be obtained.
        :type Version: int
        :param _LockType: Lock type (locked by admin or locked by login policy)
Note: This field may return null, indicating that no valid values can be obtained.
        :type LockType: str
        :param _LockTime: Lock time
Note: This field may return null, indicating that no valid values can be obtained.
        :type LockTime: int
        :param _IndexedAttribute1: Index field 1
Note: this field may return null, indicating that no valid values can be obtained.
        :type IndexedAttribute1: str
        :param _IndexedAttribute2: Index field 2
Note: this field may return null, indicating that no valid values can be obtained.
        :type IndexedAttribute2: str
        :param _IndexedAttribute3: Index field 3
Note: this field may return null, indicating that no valid values can be obtained.
        :type IndexedAttribute3: str
        :param _IndexedAttribute4: Index field 4
Note: this field may return null, indicating that no valid values can be obtained.
        :type IndexedAttribute4: str
        :param _IndexedAttribute5: Index field 5
Note: this field may return null, indicating that no valid values can be obtained.
        :type IndexedAttribute5: str
        """
        self._UserId = None
        self._UserName = None
        self._PhoneNumber = None
        self._Email = None
        self._LastSignOn = None
        self._CreatedDate = None
        self._Status = None
        self._UserDataSourceEnum = None
        self._Nickname = None
        self._Address = None
        self._Birthdate = None
        self._UserGroups = None
        self._LastModifiedDate = None
        self._CustomAttributes = None
        self._ResidentIdentityCard = None
        self._QqOpenId = None
        self._QqUnionId = None
        self._WechatOpenId = None
        self._WechatUnionId = None
        self._AlipayUserId = None
        self._Description = None
        self._Name = None
        self._Locale = None
        self._Gender = None
        self._IdentityVerificationMethod = None
        self._IdentityVerified = None
        self._Job = None
        self._Nationality = None
        self._Primary = None
        self._Zone = None
        self._AlreadyFirstLogin = None
        self._TenantId = None
        self._UserStoreId = None
        self._Version = None
        self._LockType = None
        self._LockTime = None
        self._IndexedAttribute1 = None
        self._IndexedAttribute2 = None
        self._IndexedAttribute3 = None
        self._IndexedAttribute4 = None
        self._IndexedAttribute5 = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def PhoneNumber(self):
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def LastSignOn(self):
        return self._LastSignOn

    @LastSignOn.setter
    def LastSignOn(self, LastSignOn):
        self._LastSignOn = LastSignOn

    @property
    def CreatedDate(self):
        return self._CreatedDate

    @CreatedDate.setter
    def CreatedDate(self, CreatedDate):
        self._CreatedDate = CreatedDate

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def UserDataSourceEnum(self):
        return self._UserDataSourceEnum

    @UserDataSourceEnum.setter
    def UserDataSourceEnum(self, UserDataSourceEnum):
        self._UserDataSourceEnum = UserDataSourceEnum

    @property
    def Nickname(self):
        return self._Nickname

    @Nickname.setter
    def Nickname(self, Nickname):
        self._Nickname = Nickname

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def Birthdate(self):
        return self._Birthdate

    @Birthdate.setter
    def Birthdate(self, Birthdate):
        self._Birthdate = Birthdate

    @property
    def UserGroups(self):
        return self._UserGroups

    @UserGroups.setter
    def UserGroups(self, UserGroups):
        self._UserGroups = UserGroups

    @property
    def LastModifiedDate(self):
        return self._LastModifiedDate

    @LastModifiedDate.setter
    def LastModifiedDate(self, LastModifiedDate):
        self._LastModifiedDate = LastModifiedDate

    @property
    def CustomAttributes(self):
        return self._CustomAttributes

    @CustomAttributes.setter
    def CustomAttributes(self, CustomAttributes):
        self._CustomAttributes = CustomAttributes

    @property
    def ResidentIdentityCard(self):
        return self._ResidentIdentityCard

    @ResidentIdentityCard.setter
    def ResidentIdentityCard(self, ResidentIdentityCard):
        self._ResidentIdentityCard = ResidentIdentityCard

    @property
    def QqOpenId(self):
        return self._QqOpenId

    @QqOpenId.setter
    def QqOpenId(self, QqOpenId):
        self._QqOpenId = QqOpenId

    @property
    def QqUnionId(self):
        return self._QqUnionId

    @QqUnionId.setter
    def QqUnionId(self, QqUnionId):
        self._QqUnionId = QqUnionId

    @property
    def WechatOpenId(self):
        return self._WechatOpenId

    @WechatOpenId.setter
    def WechatOpenId(self, WechatOpenId):
        self._WechatOpenId = WechatOpenId

    @property
    def WechatUnionId(self):
        return self._WechatUnionId

    @WechatUnionId.setter
    def WechatUnionId(self, WechatUnionId):
        self._WechatUnionId = WechatUnionId

    @property
    def AlipayUserId(self):
        return self._AlipayUserId

    @AlipayUserId.setter
    def AlipayUserId(self, AlipayUserId):
        self._AlipayUserId = AlipayUserId

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Locale(self):
        return self._Locale

    @Locale.setter
    def Locale(self, Locale):
        self._Locale = Locale

    @property
    def Gender(self):
        return self._Gender

    @Gender.setter
    def Gender(self, Gender):
        self._Gender = Gender

    @property
    def IdentityVerificationMethod(self):
        return self._IdentityVerificationMethod

    @IdentityVerificationMethod.setter
    def IdentityVerificationMethod(self, IdentityVerificationMethod):
        self._IdentityVerificationMethod = IdentityVerificationMethod

    @property
    def IdentityVerified(self):
        return self._IdentityVerified

    @IdentityVerified.setter
    def IdentityVerified(self, IdentityVerified):
        self._IdentityVerified = IdentityVerified

    @property
    def Job(self):
        return self._Job

    @Job.setter
    def Job(self, Job):
        self._Job = Job

    @property
    def Nationality(self):
        return self._Nationality

    @Nationality.setter
    def Nationality(self, Nationality):
        self._Nationality = Nationality

    @property
    def Primary(self):
        return self._Primary

    @Primary.setter
    def Primary(self, Primary):
        self._Primary = Primary

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def AlreadyFirstLogin(self):
        return self._AlreadyFirstLogin

    @AlreadyFirstLogin.setter
    def AlreadyFirstLogin(self, AlreadyFirstLogin):
        self._AlreadyFirstLogin = AlreadyFirstLogin

    @property
    def TenantId(self):
        return self._TenantId

    @TenantId.setter
    def TenantId(self, TenantId):
        self._TenantId = TenantId

    @property
    def UserStoreId(self):
        return self._UserStoreId

    @UserStoreId.setter
    def UserStoreId(self, UserStoreId):
        self._UserStoreId = UserStoreId

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def LockType(self):
        return self._LockType

    @LockType.setter
    def LockType(self, LockType):
        self._LockType = LockType

    @property
    def LockTime(self):
        return self._LockTime

    @LockTime.setter
    def LockTime(self, LockTime):
        self._LockTime = LockTime

    @property
    def IndexedAttribute1(self):
        return self._IndexedAttribute1

    @IndexedAttribute1.setter
    def IndexedAttribute1(self, IndexedAttribute1):
        self._IndexedAttribute1 = IndexedAttribute1

    @property
    def IndexedAttribute2(self):
        return self._IndexedAttribute2

    @IndexedAttribute2.setter
    def IndexedAttribute2(self, IndexedAttribute2):
        self._IndexedAttribute2 = IndexedAttribute2

    @property
    def IndexedAttribute3(self):
        return self._IndexedAttribute3

    @IndexedAttribute3.setter
    def IndexedAttribute3(self, IndexedAttribute3):
        self._IndexedAttribute3 = IndexedAttribute3

    @property
    def IndexedAttribute4(self):
        return self._IndexedAttribute4

    @IndexedAttribute4.setter
    def IndexedAttribute4(self, IndexedAttribute4):
        self._IndexedAttribute4 = IndexedAttribute4

    @property
    def IndexedAttribute5(self):
        return self._IndexedAttribute5

    @IndexedAttribute5.setter
    def IndexedAttribute5(self, IndexedAttribute5):
        self._IndexedAttribute5 = IndexedAttribute5


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._UserName = params.get("UserName")
        self._PhoneNumber = params.get("PhoneNumber")
        self._Email = params.get("Email")
        self._LastSignOn = params.get("LastSignOn")
        self._CreatedDate = params.get("CreatedDate")
        self._Status = params.get("Status")
        self._UserDataSourceEnum = params.get("UserDataSourceEnum")
        self._Nickname = params.get("Nickname")
        self._Address = params.get("Address")
        self._Birthdate = params.get("Birthdate")
        self._UserGroups = params.get("UserGroups")
        self._LastModifiedDate = params.get("LastModifiedDate")
        if params.get("CustomAttributes") is not None:
            self._CustomAttributes = []
            for item in params.get("CustomAttributes"):
                obj = MemberMap()
                obj._deserialize(item)
                self._CustomAttributes.append(obj)
        self._ResidentIdentityCard = params.get("ResidentIdentityCard")
        self._QqOpenId = params.get("QqOpenId")
        self._QqUnionId = params.get("QqUnionId")
        self._WechatOpenId = params.get("WechatOpenId")
        self._WechatUnionId = params.get("WechatUnionId")
        self._AlipayUserId = params.get("AlipayUserId")
        self._Description = params.get("Description")
        self._Name = params.get("Name")
        self._Locale = params.get("Locale")
        self._Gender = params.get("Gender")
        self._IdentityVerificationMethod = params.get("IdentityVerificationMethod")
        self._IdentityVerified = params.get("IdentityVerified")
        self._Job = params.get("Job")
        self._Nationality = params.get("Nationality")
        self._Primary = params.get("Primary")
        self._Zone = params.get("Zone")
        self._AlreadyFirstLogin = params.get("AlreadyFirstLogin")
        self._TenantId = params.get("TenantId")
        self._UserStoreId = params.get("UserStoreId")
        self._Version = params.get("Version")
        self._LockType = params.get("LockType")
        self._LockTime = params.get("LockTime")
        self._IndexedAttribute1 = params.get("IndexedAttribute1")
        self._IndexedAttribute2 = params.get("IndexedAttribute2")
        self._IndexedAttribute3 = params.get("IndexedAttribute3")
        self._IndexedAttribute4 = params.get("IndexedAttribute4")
        self._IndexedAttribute5 = params.get("IndexedAttribute5")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        