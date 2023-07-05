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


class AddGroupMemberRequest(AbstractModel):
    """AddGroupMember request structure.

    """

    def __init__(self):
        r"""
        :param _GroupId: The group ID.
        :type GroupId: str
        :param _SdkAppId: The SDKAppID assigned by LCIC.
        :type SdkAppId: int
        :param _MemberIds: The users. Array length limit: 200.
        :type MemberIds: list of str
        """
        self._GroupId = None
        self._SdkAppId = None
        self._MemberIds = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def MemberIds(self):
        return self._MemberIds

    @MemberIds.setter
    def MemberIds(self, MemberIds):
        self._MemberIds = MemberIds


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._SdkAppId = params.get("SdkAppId")
        self._MemberIds = params.get("MemberIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddGroupMemberResponse(AbstractModel):
    """AddGroupMember response structure.

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


class AnswerInfo(AbstractModel):
    """The answer to a quiz question.

    """

    def __init__(self):
        r"""
        :param _Name: The username.
        :type Name: str
        :param _Answer: The answer. Bits are used to indicate the options chosen. For example, `0x1` indicates that option A is chosen; `0x11` indicates that A and B are chosen, and so on.
        :type Answer: int
        :param _CostTime: The time used.
        :type CostTime: int
        :param _UserId: The user ID.
        :type UserId: str
        :param _IsCorrect: Whether the answer is correct. `1`: Correct; `0`: Incorrect.
        :type IsCorrect: int
        """
        self._Name = None
        self._Answer = None
        self._CostTime = None
        self._UserId = None
        self._IsCorrect = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Answer(self):
        return self._Answer

    @Answer.setter
    def Answer(self, Answer):
        self._Answer = Answer

    @property
    def CostTime(self):
        return self._CostTime

    @CostTime.setter
    def CostTime(self, CostTime):
        self._CostTime = CostTime

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def IsCorrect(self):
        return self._IsCorrect

    @IsCorrect.setter
    def IsCorrect(self, IsCorrect):
        self._IsCorrect = IsCorrect


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Answer = params.get("Answer")
        self._CostTime = params.get("CostTime")
        self._UserId = params.get("UserId")
        self._IsCorrect = params.get("IsCorrect")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnswerStat(AbstractModel):
    """The statistics for each type of answer.

    """

    def __init__(self):
        r"""
        :param _Answer: The answer. Bits are used to indicate the options chosen. For example, `0x1` indicates that option A is chosen; `0x11` indicates that A and B are chosen, and so on.
        :type Answer: int
        :param _Count: The number of users that submitted the answer.
        :type Count: int
        """
        self._Answer = None
        self._Count = None

    @property
    def Answer(self):
        return self._Answer

    @Answer.setter
    def Answer(self, Answer):
        self._Answer = Answer

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._Answer = params.get("Answer")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppCustomContent(AbstractModel):
    """Custom application content
    Used by actions: SetAppCustomContent.

    """

    def __init__(self):
        r"""
        :param _Scene: Multiple scenarios can be set for an application.
        :type Scene: str
        :param _LogoUrl: Logo URL
        :type LogoUrl: str
        :param _HomeUrl: Homepage URL, which can be used for redirection
        :type HomeUrl: str
        :param _JsUrl: Custom JS URL
        :type JsUrl: str
        :param _CssUrl: Custom CSS URL
        :type CssUrl: str
        """
        self._Scene = None
        self._LogoUrl = None
        self._HomeUrl = None
        self._JsUrl = None
        self._CssUrl = None

    @property
    def Scene(self):
        return self._Scene

    @Scene.setter
    def Scene(self, Scene):
        self._Scene = Scene

    @property
    def LogoUrl(self):
        return self._LogoUrl

    @LogoUrl.setter
    def LogoUrl(self, LogoUrl):
        self._LogoUrl = LogoUrl

    @property
    def HomeUrl(self):
        return self._HomeUrl

    @HomeUrl.setter
    def HomeUrl(self, HomeUrl):
        self._HomeUrl = HomeUrl

    @property
    def JsUrl(self):
        return self._JsUrl

    @JsUrl.setter
    def JsUrl(self, JsUrl):
        self._JsUrl = JsUrl

    @property
    def CssUrl(self):
        return self._CssUrl

    @CssUrl.setter
    def CssUrl(self, CssUrl):
        self._CssUrl = CssUrl


    def _deserialize(self, params):
        self._Scene = params.get("Scene")
        self._LogoUrl = params.get("LogoUrl")
        self._HomeUrl = params.get("HomeUrl")
        self._JsUrl = params.get("JsUrl")
        self._CssUrl = params.get("CssUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackgroundPictureConfig(AbstractModel):
    """Background image settings.

    """

    def __init__(self):
        r"""
        :param _Url: The URL of the background image.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Url: str
        """
        self._Url = None

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchAddGroupMemberRequest(AbstractModel):
    """BatchAddGroupMember request structure.

    """

    def __init__(self):
        r"""
        :param _GroupIds: The target group IDs. Array length limit: 100.
        :type GroupIds: list of str
        :param _SdkAppId: The SDKAppID assigned by LCIC.
        :type SdkAppId: int
        :param _MemberIds: The users to add. Array length limit: 200.
        :type MemberIds: list of str
        """
        self._GroupIds = None
        self._SdkAppId = None
        self._MemberIds = None

    @property
    def GroupIds(self):
        return self._GroupIds

    @GroupIds.setter
    def GroupIds(self, GroupIds):
        self._GroupIds = GroupIds

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def MemberIds(self):
        return self._MemberIds

    @MemberIds.setter
    def MemberIds(self, MemberIds):
        self._MemberIds = MemberIds


    def _deserialize(self, params):
        self._GroupIds = params.get("GroupIds")
        self._SdkAppId = params.get("SdkAppId")
        self._MemberIds = params.get("MemberIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchAddGroupMemberResponse(AbstractModel):
    """BatchAddGroupMember response structure.

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


class BatchCreateGroupWithMembersRequest(AbstractModel):
    """BatchCreateGroupWithMembers request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: The SDKAppID assigned by LCIC.
        :type SdkAppId: int
        :param _GroupBaseInfos: The information of the groups to create. Array length limit: 256.
        :type GroupBaseInfos: list of GroupBaseInfo
        :param _MemberIds: The group members. Array length limit: 200.
        :type MemberIds: list of str
        """
        self._SdkAppId = None
        self._GroupBaseInfos = None
        self._MemberIds = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def GroupBaseInfos(self):
        return self._GroupBaseInfos

    @GroupBaseInfos.setter
    def GroupBaseInfos(self, GroupBaseInfos):
        self._GroupBaseInfos = GroupBaseInfos

    @property
    def MemberIds(self):
        return self._MemberIds

    @MemberIds.setter
    def MemberIds(self, MemberIds):
        self._MemberIds = MemberIds


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        if params.get("GroupBaseInfos") is not None:
            self._GroupBaseInfos = []
            for item in params.get("GroupBaseInfos"):
                obj = GroupBaseInfo()
                obj._deserialize(item)
                self._GroupBaseInfos.append(obj)
        self._MemberIds = params.get("MemberIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchCreateGroupWithMembersResponse(AbstractModel):
    """BatchCreateGroupWithMembers response structure.

    """

    def __init__(self):
        r"""
        :param _GroupIds: The IDs of the groups created, which are in the same order as the elements in the request parameter `GroupBaseInfos.N`.
        :type GroupIds: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._GroupIds = None
        self._RequestId = None

    @property
    def GroupIds(self):
        return self._GroupIds

    @GroupIds.setter
    def GroupIds(self, GroupIds):
        self._GroupIds = GroupIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._GroupIds = params.get("GroupIds")
        self._RequestId = params.get("RequestId")


class BatchCreateRoomRequest(AbstractModel):
    """BatchCreateRoom request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: The SDKAppID assigned by LCIC.
        :type SdkAppId: int
        :param _RoomInfos: The information of the rooms to create.
        :type RoomInfos: list of RoomInfo
        """
        self._SdkAppId = None
        self._RoomInfos = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomInfos(self):
        return self._RoomInfos

    @RoomInfos.setter
    def RoomInfos(self, RoomInfos):
        self._RoomInfos = RoomInfos


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        if params.get("RoomInfos") is not None:
            self._RoomInfos = []
            for item in params.get("RoomInfos"):
                obj = RoomInfo()
                obj._deserialize(item)
                self._RoomInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchCreateRoomResponse(AbstractModel):
    """BatchCreateRoom response structure.

    """

    def __init__(self):
        r"""
        :param _RoomIds: The IDs of the rooms created, which are in the same order as they are passed in.
        :type RoomIds: list of int non-negative
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RoomIds = None
        self._RequestId = None

    @property
    def RoomIds(self):
        return self._RoomIds

    @RoomIds.setter
    def RoomIds(self, RoomIds):
        self._RoomIds = RoomIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RoomIds = params.get("RoomIds")
        self._RequestId = params.get("RequestId")


class BatchDeleteGroupMemberRequest(AbstractModel):
    """BatchDeleteGroupMember request structure.

    """

    def __init__(self):
        r"""
        :param _GroupIds: The target group IDs. Array length limit: 100.
        :type GroupIds: list of str
        :param _SdkAppId: The SDKAppID assigned by LCIC.
        :type SdkAppId: int
        :param _MemberIds: The users to remove. Array length limit: 256.
        :type MemberIds: list of str
        """
        self._GroupIds = None
        self._SdkAppId = None
        self._MemberIds = None

    @property
    def GroupIds(self):
        return self._GroupIds

    @GroupIds.setter
    def GroupIds(self, GroupIds):
        self._GroupIds = GroupIds

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def MemberIds(self):
        return self._MemberIds

    @MemberIds.setter
    def MemberIds(self, MemberIds):
        self._MemberIds = MemberIds


    def _deserialize(self, params):
        self._GroupIds = params.get("GroupIds")
        self._SdkAppId = params.get("SdkAppId")
        self._MemberIds = params.get("MemberIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchDeleteGroupMemberResponse(AbstractModel):
    """BatchDeleteGroupMember response structure.

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


class BatchDeleteRecordRequest(AbstractModel):
    """BatchDeleteRecord request structure.

    """

    def __init__(self):
        r"""
        :param _RoomIds: The room IDs.
        :type RoomIds: list of int
        :param _SdkAppId: The SDKAppID assigned by LCIC.
        :type SdkAppId: int
        """
        self._RoomIds = None
        self._SdkAppId = None

    @property
    def RoomIds(self):
        return self._RoomIds

    @RoomIds.setter
    def RoomIds(self, RoomIds):
        self._RoomIds = RoomIds

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId


    def _deserialize(self, params):
        self._RoomIds = params.get("RoomIds")
        self._SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchDeleteRecordResponse(AbstractModel):
    """BatchDeleteRecord response structure.

    """

    def __init__(self):
        r"""
        :param _RoomIds: The IDs of the rooms whose recordings are deleted. Note: This field may return null, indicating that no valid values can be obtained.
        :type RoomIds: list of int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RoomIds = None
        self._RequestId = None

    @property
    def RoomIds(self):
        return self._RoomIds

    @RoomIds.setter
    def RoomIds(self, RoomIds):
        self._RoomIds = RoomIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RoomIds = params.get("RoomIds")
        self._RequestId = params.get("RequestId")


class BatchDescribeDocumentRequest(AbstractModel):
    """BatchDescribeDocument request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: The SDKAppID assigned by LCIC.
        :type SdkAppId: int
        :param _Page: The page to return records from. Pagination starts from 1.
        :type Page: int
        :param _Limit: The maximum number of records per page. The value of this parameter cannot exceed `1000`.
        :type Limit: int
        :param _Permission: The courseware access. [0]: The private courseware of the specified user (`Owner`) will be returned; [1]: The public courseware of the specified user will be returned; [0,1]: Both the private and public courseware of the specified user will be returned; [2]: The private courseware of the specified user and the public courseware of all users (including `Owner`) will be returned.
        :type Permission: list of int non-negative
        :param _Owner: The user ID of the courseware owner. If you do not specify this, the information of all courseware under the application will be returned.
        :type Owner: str
        :param _Keyword: The filename keyword.
        :type Keyword: str
        :param _DocumentId: The courseware IDs. Non-existent IDs will be ignored.
        :type DocumentId: list of str
        """
        self._SdkAppId = None
        self._Page = None
        self._Limit = None
        self._Permission = None
        self._Owner = None
        self._Keyword = None
        self._DocumentId = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Permission(self):
        return self._Permission

    @Permission.setter
    def Permission(self, Permission):
        self._Permission = Permission

    @property
    def Owner(self):
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def DocumentId(self):
        return self._DocumentId

    @DocumentId.setter
    def DocumentId(self, DocumentId):
        self._DocumentId = DocumentId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Page = params.get("Page")
        self._Limit = params.get("Limit")
        self._Permission = params.get("Permission")
        self._Owner = params.get("Owner")
        self._Keyword = params.get("Keyword")
        self._DocumentId = params.get("DocumentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchDescribeDocumentResponse(AbstractModel):
    """BatchDescribeDocument response structure.

    """

    def __init__(self):
        r"""
        :param _Total: The total number of records that meet the conditions.
        :type Total: int
        :param _Documents: The information of the courseware.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Documents: list of DocumentInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._Documents = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Documents(self):
        return self._Documents

    @Documents.setter
    def Documents(self, Documents):
        self._Documents = Documents

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Documents") is not None:
            self._Documents = []
            for item in params.get("Documents"):
                obj = DocumentInfo()
                obj._deserialize(item)
                self._Documents.append(obj)
        self._RequestId = params.get("RequestId")


class BatchRegisterRequest(AbstractModel):
    """BatchRegister request structure.

    """

    def __init__(self):
        r"""
        :param _Users: The information of the users to register.
        :type Users: list of BatchUserRequest
        """
        self._Users = None

    @property
    def Users(self):
        return self._Users

    @Users.setter
    def Users(self, Users):
        self._Users = Users


    def _deserialize(self, params):
        if params.get("Users") is not None:
            self._Users = []
            for item in params.get("Users"):
                obj = BatchUserRequest()
                obj._deserialize(item)
                self._Users.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchRegisterResponse(AbstractModel):
    """BatchRegister response structure.

    """

    def __init__(self):
        r"""
        :param _Users: The information of the successfully registered users. Note: This field may return null, indicating that no valid values can be obtained.
        :type Users: list of BatchUserInfo
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
                obj = BatchUserInfo()
                obj._deserialize(item)
                self._Users.append(obj)
        self._RequestId = params.get("RequestId")


class BatchUserInfo(AbstractModel):
    """The information of registered users.
    Used by actions: BatchRegister.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: The SDKAppID assigned by LCIC.

        :type SdkAppId: int
        :param _UserId: 
Note: This field may return null, indicating that no valid values can be obtained.
        :type UserId: str
        :param _OriginId: 
Note: This field may return null, indicating that no valid values can be obtained.
        :type OriginId: str
        """
        self._SdkAppId = None
        self._UserId = None
        self._OriginId = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def OriginId(self):
        return self._OriginId

    @OriginId.setter
    def OriginId(self, OriginId):
        self._OriginId = OriginId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._UserId = params.get("UserId")
        self._OriginId = params.get("OriginId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchUserRequest(AbstractModel):
    """The information of the users to register.
    Used by actions: BatchRegister.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: The SDKAppID assigned by LCIC.  Note: This field may return null, indicating that no valid values can be obtained.
        :type SdkAppId: int
        :param _Name: The username.  Note: This field may return null, indicating that no valid values can be obtained.
        :type Name: str
        :param _OriginId: The user’s ID in your system, which must be unique across the same application.  Note: This field may return null, indicating that no valid values can be obtained.
        :type OriginId: str
        :param _Avatar: The user’s profile photo.  Note: This field may return null, indicating that no valid values can be obtained.
        :type Avatar: str
        """
        self._SdkAppId = None
        self._Name = None
        self._OriginId = None
        self._Avatar = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def OriginId(self):
        return self._OriginId

    @OriginId.setter
    def OriginId(self, OriginId):
        self._OriginId = OriginId

    @property
    def Avatar(self):
        return self._Avatar

    @Avatar.setter
    def Avatar(self, Avatar):
        self._Avatar = Avatar


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Name = params.get("Name")
        self._OriginId = params.get("OriginId")
        self._Avatar = params.get("Avatar")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindDocumentToRoomRequest(AbstractModel):
    """BindDocumentToRoom request structure.

    """

    def __init__(self):
        r"""
        :param _RoomId: Room ID
        :type RoomId: int
        :param _DocumentId: Document ID
        :type DocumentId: str
        :param _BindType: Binding type. The default value is `0`. The backend passes through this parameter to clients so that the clients can implement business logic based on this parameter.
        :type BindType: int
        """
        self._RoomId = None
        self._DocumentId = None
        self._BindType = None

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def DocumentId(self):
        return self._DocumentId

    @DocumentId.setter
    def DocumentId(self, DocumentId):
        self._DocumentId = DocumentId

    @property
    def BindType(self):
        return self._BindType

    @BindType.setter
    def BindType(self, BindType):
        self._BindType = BindType


    def _deserialize(self, params):
        self._RoomId = params.get("RoomId")
        self._DocumentId = params.get("DocumentId")
        self._BindType = params.get("BindType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindDocumentToRoomResponse(AbstractModel):
    """BindDocumentToRoom response structure.

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


class CreateDocumentRequest(AbstractModel):
    """CreateDocument request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: LCIC SdkAppId
        :type SdkAppId: int
        :param _DocumentUrl: Document URL	
        :type DocumentUrl: str
        :param _DocumentName: Document name	
        :type DocumentName: str
        :param _Owner: Document owner ID	
        :type Owner: str
        :param _TranscodeType: Transcoding type. Valid values: `0`: No transcoding required (default); `1`: Documents that need to be transcoded: ppt, pptx, pdf, doc, docx; `2`: Videos that need to be transcoded: mp4, 3pg, mpeg, avi, flv, wmv, rm, h264, etc.; `2`: Audio that needs to be transcoded: mp3, wav, wma, aac, flac, opus
        :type TranscodeType: int
        :param _Permission: Permission. Valid values: `0`: Private document (default); `1`: Public document
        :type Permission: int
        :param _DocumentType: Document extension
        :type DocumentType: str
        :param _DocumentSize: Document size, in bytes
        :type DocumentSize: int
        """
        self._SdkAppId = None
        self._DocumentUrl = None
        self._DocumentName = None
        self._Owner = None
        self._TranscodeType = None
        self._Permission = None
        self._DocumentType = None
        self._DocumentSize = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def DocumentUrl(self):
        return self._DocumentUrl

    @DocumentUrl.setter
    def DocumentUrl(self, DocumentUrl):
        self._DocumentUrl = DocumentUrl

    @property
    def DocumentName(self):
        return self._DocumentName

    @DocumentName.setter
    def DocumentName(self, DocumentName):
        self._DocumentName = DocumentName

    @property
    def Owner(self):
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def TranscodeType(self):
        return self._TranscodeType

    @TranscodeType.setter
    def TranscodeType(self, TranscodeType):
        self._TranscodeType = TranscodeType

    @property
    def Permission(self):
        return self._Permission

    @Permission.setter
    def Permission(self, Permission):
        self._Permission = Permission

    @property
    def DocumentType(self):
        return self._DocumentType

    @DocumentType.setter
    def DocumentType(self, DocumentType):
        self._DocumentType = DocumentType

    @property
    def DocumentSize(self):
        return self._DocumentSize

    @DocumentSize.setter
    def DocumentSize(self, DocumentSize):
        self._DocumentSize = DocumentSize


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._DocumentUrl = params.get("DocumentUrl")
        self._DocumentName = params.get("DocumentName")
        self._Owner = params.get("Owner")
        self._TranscodeType = params.get("TranscodeType")
        self._Permission = params.get("Permission")
        self._DocumentType = params.get("DocumentType")
        self._DocumentSize = params.get("DocumentSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDocumentResponse(AbstractModel):
    """CreateDocument response structure.

    """

    def __init__(self):
        r"""
        :param _DocumentId: Document ID
        :type DocumentId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DocumentId = None
        self._RequestId = None

    @property
    def DocumentId(self):
        return self._DocumentId

    @DocumentId.setter
    def DocumentId(self, DocumentId):
        self._DocumentId = DocumentId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DocumentId = params.get("DocumentId")
        self._RequestId = params.get("RequestId")


class CreateGroupWithMembersRequest(AbstractModel):
    """CreateGroupWithMembers request structure.

    """

    def __init__(self):
        r"""
        :param _GroupName: The group name.
        :type GroupName: str
        :param _SdkAppId: The SDKAppID assigned by LCIC.
        :type SdkAppId: int
        :param _TeacherId: The user ID of the teacher.
        :type TeacherId: str
        :param _MemberIds: The group members. Array length limit: 200.
        :type MemberIds: list of str
        """
        self._GroupName = None
        self._SdkAppId = None
        self._TeacherId = None
        self._MemberIds = None

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TeacherId(self):
        return self._TeacherId

    @TeacherId.setter
    def TeacherId(self, TeacherId):
        self._TeacherId = TeacherId

    @property
    def MemberIds(self):
        return self._MemberIds

    @MemberIds.setter
    def MemberIds(self, MemberIds):
        self._MemberIds = MemberIds


    def _deserialize(self, params):
        self._GroupName = params.get("GroupName")
        self._SdkAppId = params.get("SdkAppId")
        self._TeacherId = params.get("TeacherId")
        self._MemberIds = params.get("MemberIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGroupWithMembersResponse(AbstractModel):
    """CreateGroupWithMembers response structure.

    """

    def __init__(self):
        r"""
        :param _GroupId: The ID of the successfully created group.
        :type GroupId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._GroupId = None
        self._RequestId = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._RequestId = params.get("RequestId")


class CreateGroupWithSubGroupRequest(AbstractModel):
    """CreateGroupWithSubGroup request structure.

    """

    def __init__(self):
        r"""
        :param _GroupName: The group name after merging.
        :type GroupName: str
        :param _SdkAppId: The SDKAppID assigned by LCIC.
        :type SdkAppId: int
        :param _SubGroupIds: The IDs of the groups to merge. Duplicate group IDs are not allowed. Array length limit: 40.
        :type SubGroupIds: list of str
        :param _TeacherId: The user ID of the teacher.
        :type TeacherId: str
        """
        self._GroupName = None
        self._SdkAppId = None
        self._SubGroupIds = None
        self._TeacherId = None

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def SubGroupIds(self):
        return self._SubGroupIds

    @SubGroupIds.setter
    def SubGroupIds(self, SubGroupIds):
        self._SubGroupIds = SubGroupIds

    @property
    def TeacherId(self):
        return self._TeacherId

    @TeacherId.setter
    def TeacherId(self, TeacherId):
        self._TeacherId = TeacherId


    def _deserialize(self, params):
        self._GroupName = params.get("GroupName")
        self._SdkAppId = params.get("SdkAppId")
        self._SubGroupIds = params.get("SubGroupIds")
        self._TeacherId = params.get("TeacherId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGroupWithSubGroupResponse(AbstractModel):
    """CreateGroupWithSubGroup response structure.

    """

    def __init__(self):
        r"""
        :param _GroupId: The ID of the merged group.
        :type GroupId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._GroupId = None
        self._RequestId = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._RequestId = params.get("RequestId")


class CreateRoomRequest(AbstractModel):
    """CreateRoom request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Room name
        :type Name: str
        :param _StartTime: Reserved room start time, in UNIX timestamp format
        :type StartTime: int
        :param _EndTime: Reserved room end time, in UNIX timestamp format
        :type EndTime: int
        :param _SdkAppId: LCIC SdkAppId
        :type SdkAppId: int
        :param _Resolution: 	Resolution. Valid values: 1: SD; 2: HD; 3: FHD
        :type Resolution: int
        :param _MaxMicNumber: Maximum number of mic-on users (excluding teachers). Value range: [0, 16]
        :type MaxMicNumber: int
        :param _SubType: The room subtype. Valid values: videodoc: Document + Video; video: Video only.
        :type SubType: str
        :param _TeacherId: The user ID of the teacher. User IDs are returned by the user registration APIs. The user specified will have teacher permissions in the room created.
        :type TeacherId: str
        :param _AutoMic: Whether to automatically turn the mic on when the user enters a room. Valid values: 0: No (default value); 1: Yes.
        :type AutoMic: int
        :param _TurnOffMic: Whether to disconnect communication after audio/video permissions are revoked. Valid values: `0` (default): Yes; `1`: No.
        :type TurnOffMic: int
        :param _AudioQuality: Whether to enable the high audio quality mode. Valid values: 0: No (default value); 1: Yes.
        :type AudioQuality: int
        :param _DisableRecord: Whether to disable auto recording. Valid values: 0: No (default); 1: Yes. If this parameter is 0, recording will start when the class starts and stops when the class ends.
        :type DisableRecord: int
        :param _Assistants: The user IDs of the teaching assistants. User IDs are returned by the user registration APIs. The users specified will have teaching assistant permissions in the room created.
        :type Assistants: list of str
        :param _RTCAudienceNumber: The number of RTC users.
        :type RTCAudienceNumber: int
        :param _AudienceType: The audience type.
        :type AudienceType: int
        :param _RecordLayout: Recording layout
        :type RecordLayout: int
        :param _GroupId: The ID of the group to bind. If you specify this parameter, only members of the group can enter this room.
        :type GroupId: str
        :param _EnableDirectControl: Whether the teacher/teaching assistant can control students' cameras/microphones without the students' consent. Valid values: 
`0` (default): No (consent required)
`1`: Yes (no consent required)
        :type EnableDirectControl: int
        """
        self._Name = None
        self._StartTime = None
        self._EndTime = None
        self._SdkAppId = None
        self._Resolution = None
        self._MaxMicNumber = None
        self._SubType = None
        self._TeacherId = None
        self._AutoMic = None
        self._TurnOffMic = None
        self._AudioQuality = None
        self._DisableRecord = None
        self._Assistants = None
        self._RTCAudienceNumber = None
        self._AudienceType = None
        self._RecordLayout = None
        self._GroupId = None
        self._EnableDirectControl = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Resolution(self):
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def MaxMicNumber(self):
        return self._MaxMicNumber

    @MaxMicNumber.setter
    def MaxMicNumber(self, MaxMicNumber):
        self._MaxMicNumber = MaxMicNumber

    @property
    def SubType(self):
        return self._SubType

    @SubType.setter
    def SubType(self, SubType):
        self._SubType = SubType

    @property
    def TeacherId(self):
        return self._TeacherId

    @TeacherId.setter
    def TeacherId(self, TeacherId):
        self._TeacherId = TeacherId

    @property
    def AutoMic(self):
        return self._AutoMic

    @AutoMic.setter
    def AutoMic(self, AutoMic):
        self._AutoMic = AutoMic

    @property
    def TurnOffMic(self):
        return self._TurnOffMic

    @TurnOffMic.setter
    def TurnOffMic(self, TurnOffMic):
        self._TurnOffMic = TurnOffMic

    @property
    def AudioQuality(self):
        return self._AudioQuality

    @AudioQuality.setter
    def AudioQuality(self, AudioQuality):
        self._AudioQuality = AudioQuality

    @property
    def DisableRecord(self):
        return self._DisableRecord

    @DisableRecord.setter
    def DisableRecord(self, DisableRecord):
        self._DisableRecord = DisableRecord

    @property
    def Assistants(self):
        return self._Assistants

    @Assistants.setter
    def Assistants(self, Assistants):
        self._Assistants = Assistants

    @property
    def RTCAudienceNumber(self):
        return self._RTCAudienceNumber

    @RTCAudienceNumber.setter
    def RTCAudienceNumber(self, RTCAudienceNumber):
        self._RTCAudienceNumber = RTCAudienceNumber

    @property
    def AudienceType(self):
        return self._AudienceType

    @AudienceType.setter
    def AudienceType(self, AudienceType):
        self._AudienceType = AudienceType

    @property
    def RecordLayout(self):
        return self._RecordLayout

    @RecordLayout.setter
    def RecordLayout(self, RecordLayout):
        self._RecordLayout = RecordLayout

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def EnableDirectControl(self):
        return self._EnableDirectControl

    @EnableDirectControl.setter
    def EnableDirectControl(self, EnableDirectControl):
        self._EnableDirectControl = EnableDirectControl


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._SdkAppId = params.get("SdkAppId")
        self._Resolution = params.get("Resolution")
        self._MaxMicNumber = params.get("MaxMicNumber")
        self._SubType = params.get("SubType")
        self._TeacherId = params.get("TeacherId")
        self._AutoMic = params.get("AutoMic")
        self._TurnOffMic = params.get("TurnOffMic")
        self._AudioQuality = params.get("AudioQuality")
        self._DisableRecord = params.get("DisableRecord")
        self._Assistants = params.get("Assistants")
        self._RTCAudienceNumber = params.get("RTCAudienceNumber")
        self._AudienceType = params.get("AudienceType")
        self._RecordLayout = params.get("RecordLayout")
        self._GroupId = params.get("GroupId")
        self._EnableDirectControl = params.get("EnableDirectControl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRoomResponse(AbstractModel):
    """CreateRoom response structure.

    """

    def __init__(self):
        r"""
        :param _RoomId: Room ID
        :type RoomId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RoomId = None
        self._RequestId = None

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RoomId = params.get("RoomId")
        self._RequestId = params.get("RequestId")


class CreateSupervisorRequest(AbstractModel):
    """CreateSupervisor request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: The application ID.
        :type SdkAppId: int
        :param _Users: The user IDs.
        :type Users: list of str
        """
        self._SdkAppId = None
        self._Users = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Users(self):
        return self._Users

    @Users.setter
    def Users(self, Users):
        self._Users = Users


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Users = params.get("Users")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSupervisorResponse(AbstractModel):
    """CreateSupervisor response structure.

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


class DeleteAppCustomContentRequest(AbstractModel):
    """DeleteAppCustomContent request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: The application ID.
        :type SdkAppId: int
        :param _Scenes: The custom elements (for which a scene has been configured) to delete. If this is empty, all custom elements will be deleted.
        :type Scenes: list of str
        """
        self._SdkAppId = None
        self._Scenes = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Scenes(self):
        return self._Scenes

    @Scenes.setter
    def Scenes(self, Scenes):
        self._Scenes = Scenes


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Scenes = params.get("Scenes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAppCustomContentResponse(AbstractModel):
    """DeleteAppCustomContent response structure.

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


class DeleteDocumentRequest(AbstractModel):
    """DeleteDocument request structure.

    """

    def __init__(self):
        r"""
        :param _DocumentId: The document ID.
        :type DocumentId: str
        """
        self._DocumentId = None

    @property
    def DocumentId(self):
        return self._DocumentId

    @DocumentId.setter
    def DocumentId(self, DocumentId):
        self._DocumentId = DocumentId


    def _deserialize(self, params):
        self._DocumentId = params.get("DocumentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDocumentResponse(AbstractModel):
    """DeleteDocument response structure.

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


class DeleteGroupMemberRequest(AbstractModel):
    """DeleteGroupMember request structure.

    """

    def __init__(self):
        r"""
        :param _GroupId: The group ID. You cannot remove members from a merged group.
        :type GroupId: str
        :param _SdkAppId: The SDKAppID assigned by LCIC.
        :type SdkAppId: int
        :param _MemberIds: The users. Array length limit: 200.
        :type MemberIds: list of str
        """
        self._GroupId = None
        self._SdkAppId = None
        self._MemberIds = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def MemberIds(self):
        return self._MemberIds

    @MemberIds.setter
    def MemberIds(self, MemberIds):
        self._MemberIds = MemberIds


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._SdkAppId = params.get("SdkAppId")
        self._MemberIds = params.get("MemberIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteGroupMemberResponse(AbstractModel):
    """DeleteGroupMember response structure.

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


class DeleteGroupRequest(AbstractModel):
    """DeleteGroup request structure.

    """

    def __init__(self):
        r"""
        :param _GroupIds: The IDs of the groups to delete.
        :type GroupIds: list of str
        :param _SdkAppId: The SDKAppID assigned by LCIC.
        :type SdkAppId: int
        """
        self._GroupIds = None
        self._SdkAppId = None

    @property
    def GroupIds(self):
        return self._GroupIds

    @GroupIds.setter
    def GroupIds(self, GroupIds):
        self._GroupIds = GroupIds

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId


    def _deserialize(self, params):
        self._GroupIds = params.get("GroupIds")
        self._SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteGroupResponse(AbstractModel):
    """DeleteGroup response structure.

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


class DeleteRecordRequest(AbstractModel):
    """DeleteRecord request structure.

    """

    def __init__(self):
        r"""
        :param _RoomId: The room ID.
        :type RoomId: int
        :param _SdkAppId: The SDKAppID assigned by LCIC.
        :type SdkAppId: int
        """
        self._RoomId = None
        self._SdkAppId = None

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId


    def _deserialize(self, params):
        self._RoomId = params.get("RoomId")
        self._SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRecordResponse(AbstractModel):
    """DeleteRecord response structure.

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


class DeleteRoomRequest(AbstractModel):
    """DeleteRoom request structure.

    """

    def __init__(self):
        r"""
        :param _RoomId: Room ID
        :type RoomId: int
        """
        self._RoomId = None

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId


    def _deserialize(self, params):
        self._RoomId = params.get("RoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRoomResponse(AbstractModel):
    """DeleteRoom response structure.

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


class DeleteSupervisorRequest(AbstractModel):
    """DeleteSupervisor request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: The application ID.
        :type SdkAppId: int
        :param _Users: The user IDs.
        :type Users: list of str
        """
        self._SdkAppId = None
        self._Users = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Users(self):
        return self._Users

    @Users.setter
    def Users(self, Users):
        self._Users = Users


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Users = params.get("Users")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSupervisorResponse(AbstractModel):
    """DeleteSupervisor response structure.

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


class DescribeAnswerListRequest(AbstractModel):
    """DescribeAnswerList request structure.

    """

    def __init__(self):
        r"""
        :param _QuestionId: The question ID.
        :type QuestionId: str
        :param _Page: 1
        :type Page: int
        :param _Limit: 100
        :type Limit: int
        """
        self._QuestionId = None
        self._Page = None
        self._Limit = None

    @property
    def QuestionId(self):
        return self._QuestionId

    @QuestionId.setter
    def QuestionId(self, QuestionId):
        self._QuestionId = QuestionId

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._QuestionId = params.get("QuestionId")
        self._Page = params.get("Page")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAnswerListResponse(AbstractModel):
    """DescribeAnswerList response structure.

    """

    def __init__(self):
        r"""
        :param _Total: The total number of answers.
        :type Total: int
        :param _AnswerInfo: A list of the answers.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AnswerInfo: list of AnswerInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._AnswerInfo = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def AnswerInfo(self):
        return self._AnswerInfo

    @AnswerInfo.setter
    def AnswerInfo(self, AnswerInfo):
        self._AnswerInfo = AnswerInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("AnswerInfo") is not None:
            self._AnswerInfo = []
            for item in params.get("AnswerInfo"):
                obj = AnswerInfo()
                obj._deserialize(item)
                self._AnswerInfo.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCurrentMemberListRequest(AbstractModel):
    """DescribeCurrentMemberList request structure.

    """

    def __init__(self):
        r"""
        :param _RoomId: The room ID.
        :type RoomId: int
        :param _Page: The page to return records from. Pagination starts from 1.
        :type Page: int
        :param _Limit: The maximum number of records per page. The value of this parameter cannot exceed 1000.
        :type Limit: int
        """
        self._RoomId = None
        self._Page = None
        self._Limit = None

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._RoomId = params.get("RoomId")
        self._Page = params.get("Page")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCurrentMemberListResponse(AbstractModel):
    """DescribeCurrentMemberList response structure.

    """

    def __init__(self):
        r"""
        :param _Total: The total number of records.
        :type Total: int
        :param _MemberRecords: The user list.
        :type MemberRecords: list of MemberRecord
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._MemberRecords = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def MemberRecords(self):
        return self._MemberRecords

    @MemberRecords.setter
    def MemberRecords(self, MemberRecords):
        self._MemberRecords = MemberRecords

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("MemberRecords") is not None:
            self._MemberRecords = []
            for item in params.get("MemberRecords"):
                obj = MemberRecord()
                obj._deserialize(item)
                self._MemberRecords.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDeveloperRequest(AbstractModel):
    """DescribeDeveloper request structure.

    """


class DescribeDeveloperResponse(AbstractModel):
    """DescribeDeveloper response structure.

    """

    def __init__(self):
        r"""
        :param _DeveloperId: The developer ID.
        :type DeveloperId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DeveloperId = None
        self._RequestId = None

    @property
    def DeveloperId(self):
        return self._DeveloperId

    @DeveloperId.setter
    def DeveloperId(self, DeveloperId):
        self._DeveloperId = DeveloperId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DeveloperId = params.get("DeveloperId")
        self._RequestId = params.get("RequestId")


class DescribeDocumentRequest(AbstractModel):
    """DescribeDocument request structure.

    """

    def __init__(self):
        r"""
        :param _DocumentId: The (unique) document ID.
        :type DocumentId: str
        """
        self._DocumentId = None

    @property
    def DocumentId(self):
        return self._DocumentId

    @DocumentId.setter
    def DocumentId(self, DocumentId):
        self._DocumentId = DocumentId


    def _deserialize(self, params):
        self._DocumentId = params.get("DocumentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDocumentResponse(AbstractModel):
    """DescribeDocument response structure.

    """

    def __init__(self):
        r"""
        :param _DocumentId: The document ID.
        :type DocumentId: str
        :param _DocumentUrl: The document’s original URL.
        :type DocumentUrl: str
        :param _DocumentName: The document title.
        :type DocumentName: str
        :param _Owner: The user ID of the document’s owner.
        :type Owner: str
        :param _SdkAppId: The application ID.
        :type SdkAppId: int
        :param _Permission: The document access type.
        :type Permission: int
        :param _TranscodeResult: The transcoding result. If the file is not transcoded, this parameter will be empty. If it is successfully transcoded, this parameter will be the URL of the transcoded file. If transcoding fails, this parameter will indicate the error code.
        :type TranscodeResult: str
        :param _TranscodeType: The transcoding type.
        :type TranscodeType: int
        :param _TranscodeProgress: The transcoding progress. Value range: 0-100.
        :type TranscodeProgress: int
        :param _TranscodeState: The transcoding status. 0: The file is not transcoded. 1: The file is being transcoded. 2: Transcoding failed. 3: Transcoding is successful.
        :type TranscodeState: int
        :param _TranscodeInfo: The error message for failed transcoding.
        :type TranscodeInfo: str
        :param _DocumentType: The document type.
        :type DocumentType: str
        :param _DocumentSize: The document size (bytes).
        :type DocumentSize: int
        :param _UpdateTime: The time (Unix timestamp) when the document was last updated.
        :type UpdateTime: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DocumentId = None
        self._DocumentUrl = None
        self._DocumentName = None
        self._Owner = None
        self._SdkAppId = None
        self._Permission = None
        self._TranscodeResult = None
        self._TranscodeType = None
        self._TranscodeProgress = None
        self._TranscodeState = None
        self._TranscodeInfo = None
        self._DocumentType = None
        self._DocumentSize = None
        self._UpdateTime = None
        self._RequestId = None

    @property
    def DocumentId(self):
        return self._DocumentId

    @DocumentId.setter
    def DocumentId(self, DocumentId):
        self._DocumentId = DocumentId

    @property
    def DocumentUrl(self):
        return self._DocumentUrl

    @DocumentUrl.setter
    def DocumentUrl(self, DocumentUrl):
        self._DocumentUrl = DocumentUrl

    @property
    def DocumentName(self):
        return self._DocumentName

    @DocumentName.setter
    def DocumentName(self, DocumentName):
        self._DocumentName = DocumentName

    @property
    def Owner(self):
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Permission(self):
        return self._Permission

    @Permission.setter
    def Permission(self, Permission):
        self._Permission = Permission

    @property
    def TranscodeResult(self):
        return self._TranscodeResult

    @TranscodeResult.setter
    def TranscodeResult(self, TranscodeResult):
        self._TranscodeResult = TranscodeResult

    @property
    def TranscodeType(self):
        return self._TranscodeType

    @TranscodeType.setter
    def TranscodeType(self, TranscodeType):
        self._TranscodeType = TranscodeType

    @property
    def TranscodeProgress(self):
        return self._TranscodeProgress

    @TranscodeProgress.setter
    def TranscodeProgress(self, TranscodeProgress):
        self._TranscodeProgress = TranscodeProgress

    @property
    def TranscodeState(self):
        return self._TranscodeState

    @TranscodeState.setter
    def TranscodeState(self, TranscodeState):
        self._TranscodeState = TranscodeState

    @property
    def TranscodeInfo(self):
        return self._TranscodeInfo

    @TranscodeInfo.setter
    def TranscodeInfo(self, TranscodeInfo):
        self._TranscodeInfo = TranscodeInfo

    @property
    def DocumentType(self):
        return self._DocumentType

    @DocumentType.setter
    def DocumentType(self, DocumentType):
        self._DocumentType = DocumentType

    @property
    def DocumentSize(self):
        return self._DocumentSize

    @DocumentSize.setter
    def DocumentSize(self, DocumentSize):
        self._DocumentSize = DocumentSize

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DocumentId = params.get("DocumentId")
        self._DocumentUrl = params.get("DocumentUrl")
        self._DocumentName = params.get("DocumentName")
        self._Owner = params.get("Owner")
        self._SdkAppId = params.get("SdkAppId")
        self._Permission = params.get("Permission")
        self._TranscodeResult = params.get("TranscodeResult")
        self._TranscodeType = params.get("TranscodeType")
        self._TranscodeProgress = params.get("TranscodeProgress")
        self._TranscodeState = params.get("TranscodeState")
        self._TranscodeInfo = params.get("TranscodeInfo")
        self._DocumentType = params.get("DocumentType")
        self._DocumentSize = params.get("DocumentSize")
        self._UpdateTime = params.get("UpdateTime")
        self._RequestId = params.get("RequestId")


class DescribeDocumentsByRoomRequest(AbstractModel):
    """DescribeDocumentsByRoom request structure.

    """

    def __init__(self):
        r"""
        :param _RoomId: The room ID.
        :type RoomId: int
        :param _SdkAppId: The SDKAppID assigned by LCIC.
        :type SdkAppId: int
        :param _Page: The page to return records from. Pagination starts from 1, which is also the default value of this parameter.
        :type Page: int
        :param _Limit: The maximum number of records to return per page. The maximum value can be 1000. The default value is 100.
        :type Limit: int
        :param _Permission: The document access type. [0]: The private documents of the owner. [1]: The public documents of the owner. [0,1]: The private and public documents of the owner. [2]: The private and public documents of all users (including the owner). Default value: [2].
        :type Permission: list of int non-negative
        :param _Owner: The user ID of the document owner. If you do not specify this, the information of all documents under the application will be returned.
        :type Owner: str
        """
        self._RoomId = None
        self._SdkAppId = None
        self._Page = None
        self._Limit = None
        self._Permission = None
        self._Owner = None

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Permission(self):
        return self._Permission

    @Permission.setter
    def Permission(self, Permission):
        self._Permission = Permission

    @property
    def Owner(self):
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner


    def _deserialize(self, params):
        self._RoomId = params.get("RoomId")
        self._SdkAppId = params.get("SdkAppId")
        self._Page = params.get("Page")
        self._Limit = params.get("Limit")
        self._Permission = params.get("Permission")
        self._Owner = params.get("Owner")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDocumentsByRoomResponse(AbstractModel):
    """DescribeDocumentsByRoom response structure.

    """

    def __init__(self):
        r"""
        :param _Documents: 
Note: This field may return null, indicating that no valid values can be obtained.
        :type Documents: list of DocumentInfo
        :param _Total: The total number of records that meet the conditions.
        :type Total: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Documents = None
        self._Total = None
        self._RequestId = None

    @property
    def Documents(self):
        return self._Documents

    @Documents.setter
    def Documents(self, Documents):
        self._Documents = Documents

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Documents") is not None:
            self._Documents = []
            for item in params.get("Documents"):
                obj = DocumentInfo()
                obj._deserialize(item)
                self._Documents.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeDocumentsRequest(AbstractModel):
    """DescribeDocuments request structure.

    """

    def __init__(self):
        r"""
        :param _SchoolId: The school ID.
        :type SchoolId: int
        :param _Page: The page to return records from. Pagination starts from 1.
        :type Page: int
        :param _Limit: The maximum number of records per page. The value of this parameter cannot exceed `1000`.
        :type Limit: int
        :param _Permission: The courseware access. [0]: The private courseware of the specified user (`Owner`) will be returned; [1]: The public courseware of the specified user will be returned; [0,1]: Both the private and public courseware of the specified user will be returned; [2]: The private courseware of the specified user and the public courseware of all users (including `Owner`) will be returned.
        :type Permission: list of int non-negative
        :param _Owner: The user ID of the courseware owner. If you do not specify this parameter, all courseware under the school ID will be returned.
        :type Owner: str
        :param _Keyword: The filename keyword.
        :type Keyword: str
        :param _DocumentId: The courseware IDs. Non-existent IDs will be ignored.
        :type DocumentId: list of str
        """
        self._SchoolId = None
        self._Page = None
        self._Limit = None
        self._Permission = None
        self._Owner = None
        self._Keyword = None
        self._DocumentId = None

    @property
    def SchoolId(self):
        return self._SchoolId

    @SchoolId.setter
    def SchoolId(self, SchoolId):
        self._SchoolId = SchoolId

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Permission(self):
        return self._Permission

    @Permission.setter
    def Permission(self, Permission):
        self._Permission = Permission

    @property
    def Owner(self):
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def DocumentId(self):
        return self._DocumentId

    @DocumentId.setter
    def DocumentId(self, DocumentId):
        self._DocumentId = DocumentId


    def _deserialize(self, params):
        self._SchoolId = params.get("SchoolId")
        self._Page = params.get("Page")
        self._Limit = params.get("Limit")
        self._Permission = params.get("Permission")
        self._Owner = params.get("Owner")
        self._Keyword = params.get("Keyword")
        self._DocumentId = params.get("DocumentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDocumentsResponse(AbstractModel):
    """DescribeDocuments response structure.

    """

    def __init__(self):
        r"""
        :param _Total: The total number of records that meet the conditions.
        :type Total: int
        :param _Documents: The information of the courseware.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Documents: list of DocumentInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._Documents = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Documents(self):
        return self._Documents

    @Documents.setter
    def Documents(self, Documents):
        self._Documents = Documents

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Documents") is not None:
            self._Documents = []
            for item in params.get("Documents"):
                obj = DocumentInfo()
                obj._deserialize(item)
                self._Documents.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeGroupListRequest(AbstractModel):
    """DescribeGroupList request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: The SDKAppID assigned by LCIC.
        :type SdkAppId: int
        :param _Page: The page to return records from. Pagination starts from 1.
        :type Page: int
        :param _Limit: The maximum number of records per page. The value of this parameter cannot exceed 1000 and is 20 by default.
        :type Limit: int
        :param _TeacherId: The user ID of the teacher, which is used as the filter. This parameter and MemberId are mutually exclusive. If both are specified, only this parameter will take effect.
        :type TeacherId: str
        :param _MemberId: The user ID of a member, which is used as the filter. This parameter and TeacherId are mutually exclusive.
        :type MemberId: str
        """
        self._SdkAppId = None
        self._Page = None
        self._Limit = None
        self._TeacherId = None
        self._MemberId = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def TeacherId(self):
        return self._TeacherId

    @TeacherId.setter
    def TeacherId(self, TeacherId):
        self._TeacherId = TeacherId

    @property
    def MemberId(self):
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Page = params.get("Page")
        self._Limit = params.get("Limit")
        self._TeacherId = params.get("TeacherId")
        self._MemberId = params.get("MemberId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGroupListResponse(AbstractModel):
    """DescribeGroupList response structure.

    """

    def __init__(self):
        r"""
        :param _Total: The total number of groups that meet the conditions.
        :type Total: int
        :param _GroupInfos: 
Note: This field may return null, indicating that no valid values can be obtained.
        :type GroupInfos: list of GroupInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._GroupInfos = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def GroupInfos(self):
        return self._GroupInfos

    @GroupInfos.setter
    def GroupInfos(self, GroupInfos):
        self._GroupInfos = GroupInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("GroupInfos") is not None:
            self._GroupInfos = []
            for item in params.get("GroupInfos"):
                obj = GroupInfo()
                obj._deserialize(item)
                self._GroupInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeGroupMemberListRequest(AbstractModel):
    """DescribeGroupMemberList request structure.

    """

    def __init__(self):
        r"""
        :param _GroupId: The group ID.
        :type GroupId: str
        :param _SdkAppId: The SDKAppID assigned by LCIC.
        :type SdkAppId: int
        :param _Page: The page to return records from. The default value is 1.
        :type Page: int
        :param _Limit: The maximum number of records per page. The value of this parameter cannot exceed 1000 and is 20 by default.
        :type Limit: int
        """
        self._GroupId = None
        self._SdkAppId = None
        self._Page = None
        self._Limit = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._SdkAppId = params.get("SdkAppId")
        self._Page = params.get("Page")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGroupMemberListResponse(AbstractModel):
    """DescribeGroupMemberList response structure.

    """

    def __init__(self):
        r"""
        :param _Total: The total number of records that meet the conditions.
        :type Total: int
        :param _MemberIds: 
Note: This field may return null, indicating that no valid values can be obtained.
        :type MemberIds: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._MemberIds = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def MemberIds(self):
        return self._MemberIds

    @MemberIds.setter
    def MemberIds(self, MemberIds):
        self._MemberIds = MemberIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        self._MemberIds = params.get("MemberIds")
        self._RequestId = params.get("RequestId")


class DescribeGroupRequest(AbstractModel):
    """DescribeGroup request structure.

    """

    def __init__(self):
        r"""
        :param _GroupId: The group ID.
        :type GroupId: str
        :param _SdkAppId: The SDKAppID assigned by LCIC.
        :type SdkAppId: int
        """
        self._GroupId = None
        self._SdkAppId = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGroupResponse(AbstractModel):
    """DescribeGroup response structure.

    """

    def __init__(self):
        r"""
        :param _GroupId: The group ID.
        :type GroupId: str
        :param _GroupName: The group name.
        :type GroupName: str
        :param _TeacherId: 
Note: This field may return null, indicating that no valid values can be obtained.
        :type TeacherId: str
        :param _GroupType: The group type. 0: Ordinary group. 1: Merged group. If the group queried is a merged group, the IDs of the sub-groups will be returned.
        :type GroupType: int
        :param _SubGroupIds: 
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubGroupIds: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._GroupId = None
        self._GroupName = None
        self._TeacherId = None
        self._GroupType = None
        self._SubGroupIds = None
        self._RequestId = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def TeacherId(self):
        return self._TeacherId

    @TeacherId.setter
    def TeacherId(self, TeacherId):
        self._TeacherId = TeacherId

    @property
    def GroupType(self):
        return self._GroupType

    @GroupType.setter
    def GroupType(self, GroupType):
        self._GroupType = GroupType

    @property
    def SubGroupIds(self):
        return self._SubGroupIds

    @SubGroupIds.setter
    def SubGroupIds(self, SubGroupIds):
        self._SubGroupIds = SubGroupIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._TeacherId = params.get("TeacherId")
        self._GroupType = params.get("GroupType")
        self._SubGroupIds = params.get("SubGroupIds")
        self._RequestId = params.get("RequestId")


class DescribeQuestionListRequest(AbstractModel):
    """DescribeQuestionList request structure.

    """

    def __init__(self):
        r"""
        :param _RoomId: The room ID.
        :type RoomId: int
        :param _Page: The page to return records from. Pagination starts from 1, which is also the default value of this parameter.
        :type Page: int
        :param _Limit: The page to return records from. Pagination starts from 1, which is also the default value of this parameter.
        :type Limit: int
        """
        self._RoomId = None
        self._Page = None
        self._Limit = None

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._RoomId = params.get("RoomId")
        self._Page = params.get("Page")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeQuestionListResponse(AbstractModel):
    """DescribeQuestionList response structure.

    """

    def __init__(self):
        r"""
        :param _Total: The total number of quiz questions.
        :type Total: int
        :param _QuestionInfo: A list of the questions.
Note: This field may return null, indicating that no valid values can be obtained.
        :type QuestionInfo: list of QuestionInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._QuestionInfo = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def QuestionInfo(self):
        return self._QuestionInfo

    @QuestionInfo.setter
    def QuestionInfo(self, QuestionInfo):
        self._QuestionInfo = QuestionInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("QuestionInfo") is not None:
            self._QuestionInfo = []
            for item in params.get("QuestionInfo"):
                obj = QuestionInfo()
                obj._deserialize(item)
                self._QuestionInfo.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRoomRequest(AbstractModel):
    """DescribeRoom request structure.

    """

    def __init__(self):
        r"""
        :param _RoomId: Room ID	
        :type RoomId: int
        """
        self._RoomId = None

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId


    def _deserialize(self, params):
        self._RoomId = params.get("RoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRoomResponse(AbstractModel):
    """DescribeRoom response structure.

    """

    def __init__(self):
        r"""
        :param _Name: Room name	
        :type Name: str
        :param _StartTime: Reserved room start time, in UNIX timestamp format	
        :type StartTime: int
        :param _EndTime: Reserved room end time, in UNIX timestamp format	
        :type EndTime: int
        :param _TeacherId: Teacher ID	
        :type TeacherId: str
        :param _SdkAppId: LCIC SdkAppId	
        :type SdkAppId: int
        :param _Resolution: Resolution. Valid values: 1: SD; 2: HD; 3: FHD
        :type Resolution: int
        :param _MaxMicNumber: Maximum number of mic-on users (excluding teachers). Value range: [0, 16]
        :type MaxMicNumber: int
        :param _AutoMic: Whether to automatically turn the mic on when the user enters a room. Valid values: 0: No (default value); 1: Yes.
        :type AutoMic: int
        :param _AudioQuality: Whether to enable the high audio quality mode. Valid values: 0: No (default value); 1: Yes.
        :type AudioQuality: int
        :param _SubType: The room subtype. Valid values: videodoc: Document + Video; video: Video only.
        :type SubType: str
        :param _DisableRecord: Whether to disable auto recording. Valid values: 0: No (default); 1: Yes. If this parameter is 0, recording will start when the class starts and stops when the class ends.
        :type DisableRecord: int
        :param _Assistants: Assistant ID list Note: This field may return null, indicating that no valid values can be obtained.
        :type Assistants: list of str
        :param _RecordUrl: Recording URL. This parameter exists only after a room is ended. Note: This field may return null, indicating that no valid values can be obtained.
        :type RecordUrl: str
        :param _Status: The class status. 0: The class has not started. 1: The class has started. 2: The class ended. 3: The class expired. Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: int
        :param _GroupId: Note: This field may return null, indicating that no valid values can be obtained.
        :type GroupId: str
        :param _EnableDirectControl: Whether the students' consent is required to control their cameras/microphones.
        :type EnableDirectControl: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Name = None
        self._StartTime = None
        self._EndTime = None
        self._TeacherId = None
        self._SdkAppId = None
        self._Resolution = None
        self._MaxMicNumber = None
        self._AutoMic = None
        self._AudioQuality = None
        self._SubType = None
        self._DisableRecord = None
        self._Assistants = None
        self._RecordUrl = None
        self._Status = None
        self._GroupId = None
        self._EnableDirectControl = None
        self._RequestId = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def TeacherId(self):
        return self._TeacherId

    @TeacherId.setter
    def TeacherId(self, TeacherId):
        self._TeacherId = TeacherId

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Resolution(self):
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def MaxMicNumber(self):
        return self._MaxMicNumber

    @MaxMicNumber.setter
    def MaxMicNumber(self, MaxMicNumber):
        self._MaxMicNumber = MaxMicNumber

    @property
    def AutoMic(self):
        return self._AutoMic

    @AutoMic.setter
    def AutoMic(self, AutoMic):
        self._AutoMic = AutoMic

    @property
    def AudioQuality(self):
        return self._AudioQuality

    @AudioQuality.setter
    def AudioQuality(self, AudioQuality):
        self._AudioQuality = AudioQuality

    @property
    def SubType(self):
        return self._SubType

    @SubType.setter
    def SubType(self, SubType):
        self._SubType = SubType

    @property
    def DisableRecord(self):
        return self._DisableRecord

    @DisableRecord.setter
    def DisableRecord(self, DisableRecord):
        self._DisableRecord = DisableRecord

    @property
    def Assistants(self):
        return self._Assistants

    @Assistants.setter
    def Assistants(self, Assistants):
        self._Assistants = Assistants

    @property
    def RecordUrl(self):
        return self._RecordUrl

    @RecordUrl.setter
    def RecordUrl(self, RecordUrl):
        self._RecordUrl = RecordUrl

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def EnableDirectControl(self):
        return self._EnableDirectControl

    @EnableDirectControl.setter
    def EnableDirectControl(self, EnableDirectControl):
        self._EnableDirectControl = EnableDirectControl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._TeacherId = params.get("TeacherId")
        self._SdkAppId = params.get("SdkAppId")
        self._Resolution = params.get("Resolution")
        self._MaxMicNumber = params.get("MaxMicNumber")
        self._AutoMic = params.get("AutoMic")
        self._AudioQuality = params.get("AudioQuality")
        self._SubType = params.get("SubType")
        self._DisableRecord = params.get("DisableRecord")
        self._Assistants = params.get("Assistants")
        self._RecordUrl = params.get("RecordUrl")
        self._Status = params.get("Status")
        self._GroupId = params.get("GroupId")
        self._EnableDirectControl = params.get("EnableDirectControl")
        self._RequestId = params.get("RequestId")


class DescribeRoomStatisticsRequest(AbstractModel):
    """DescribeRoomStatistics request structure.

    """

    def __init__(self):
        r"""
        :param _RoomId: Room ID
        :type RoomId: int
        :param _Page: Current page in pagination, which starts from 1.
        :type Page: int
        :param _Limit: Number of data entries to return per page. Maximum value: 1000
        :type Limit: int
        """
        self._RoomId = None
        self._Page = None
        self._Limit = None

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._RoomId = params.get("RoomId")
        self._Page = params.get("Page")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRoomStatisticsResponse(AbstractModel):
    """DescribeRoomStatistics response structure.

    """

    def __init__(self):
        r"""
        :param _PeakMemberNumber: Peak number of online members
        :type PeakMemberNumber: int
        :param _MemberNumber: Accumulated number of online members
        :type MemberNumber: int
        :param _Total: Total number of records, including members who entered the room and members who should attend the class but did not
        :type Total: int
        :param _MemberRecords: Member record list
        :type MemberRecords: list of MemberRecord
        :param _RealStartTime: The actual start time of the room, in Unix timestamp, accurate to seconds. Note: This field may return null, indicating that no valid values can be obtained.
        :type RealStartTime: int
        :param _RealEndTime: The actual end time of the room, in Unix timestamp, accurate to seconds. Note: This field may return null, indicating that no valid values can be obtained.
        :type RealEndTime: int
        :param _MessageCount: The total message count of the room.
        :type MessageCount: int
        :param _MicCount: The total number of mic-on students in the room.
        :type MicCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PeakMemberNumber = None
        self._MemberNumber = None
        self._Total = None
        self._MemberRecords = None
        self._RealStartTime = None
        self._RealEndTime = None
        self._MessageCount = None
        self._MicCount = None
        self._RequestId = None

    @property
    def PeakMemberNumber(self):
        return self._PeakMemberNumber

    @PeakMemberNumber.setter
    def PeakMemberNumber(self, PeakMemberNumber):
        self._PeakMemberNumber = PeakMemberNumber

    @property
    def MemberNumber(self):
        return self._MemberNumber

    @MemberNumber.setter
    def MemberNumber(self, MemberNumber):
        self._MemberNumber = MemberNumber

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def MemberRecords(self):
        return self._MemberRecords

    @MemberRecords.setter
    def MemberRecords(self, MemberRecords):
        self._MemberRecords = MemberRecords

    @property
    def RealStartTime(self):
        return self._RealStartTime

    @RealStartTime.setter
    def RealStartTime(self, RealStartTime):
        self._RealStartTime = RealStartTime

    @property
    def RealEndTime(self):
        return self._RealEndTime

    @RealEndTime.setter
    def RealEndTime(self, RealEndTime):
        self._RealEndTime = RealEndTime

    @property
    def MessageCount(self):
        return self._MessageCount

    @MessageCount.setter
    def MessageCount(self, MessageCount):
        self._MessageCount = MessageCount

    @property
    def MicCount(self):
        return self._MicCount

    @MicCount.setter
    def MicCount(self, MicCount):
        self._MicCount = MicCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PeakMemberNumber = params.get("PeakMemberNumber")
        self._MemberNumber = params.get("MemberNumber")
        self._Total = params.get("Total")
        if params.get("MemberRecords") is not None:
            self._MemberRecords = []
            for item in params.get("MemberRecords"):
                obj = MemberRecord()
                obj._deserialize(item)
                self._MemberRecords.append(obj)
        self._RealStartTime = params.get("RealStartTime")
        self._RealEndTime = params.get("RealEndTime")
        self._MessageCount = params.get("MessageCount")
        self._MicCount = params.get("MicCount")
        self._RequestId = params.get("RequestId")


class DescribeSdkAppIdUsersRequest(AbstractModel):
    """DescribeSdkAppIdUsers request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: The SDKAppID assigned by LCIC.
        :type SdkAppId: int
        :param _Page: The page to return records from. The default value is 1.
        :type Page: int
        :param _Limit: The maximum number of records to return per page. The default value is 20.
        :type Limit: int
        """
        self._SdkAppId = None
        self._Page = None
        self._Limit = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Page = params.get("Page")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSdkAppIdUsersResponse(AbstractModel):
    """DescribeSdkAppIdUsers response structure.

    """

    def __init__(self):
        r"""
        :param _Total: The total number of users.
        :type Total: int
        :param _Users: The information of the users. Note: This field may return null, indicating that no valid values can be obtained.
        :type Users: list of UserInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._Users = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        self._Total = params.get("Total")
        if params.get("Users") is not None:
            self._Users = []
            for item in params.get("Users"):
                obj = UserInfo()
                obj._deserialize(item)
                self._Users.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSupervisorsRequest(AbstractModel):
    """DescribeSupervisors request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: The SDKAppID assigned by LCIC.

        :type SdkAppId: int
        :param _Limit: The maximum number of records per page. The maximum value allowed is 100, and the default value is 20.
        :type Limit: int
        :param _Page: The page to return records from. Pagination starts from 1, which is also the default value of this parameter.
        :type Page: int
        """
        self._SdkAppId = None
        self._Limit = None
        self._Page = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Limit = params.get("Limit")
        self._Page = params.get("Page")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSupervisorsResponse(AbstractModel):
    """DescribeSupervisors response structure.

    """

    def __init__(self):
        r"""
        :param _Total: The total number of spectators.
        :type Total: int
        :param _Page: The current page number.
        :type Page: int
        :param _Limit: The number of records on the current page.
        :type Limit: int
        :param _UserIds: A list of the spectators.
        :type UserIds: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._Page = None
        self._Limit = None
        self._UserIds = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def UserIds(self):
        return self._UserIds

    @UserIds.setter
    def UserIds(self, UserIds):
        self._UserIds = UserIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        self._Page = params.get("Page")
        self._Limit = params.get("Limit")
        self._UserIds = params.get("UserIds")
        self._RequestId = params.get("RequestId")


class DescribeUserRequest(AbstractModel):
    """DescribeUser request structure.

    """

    def __init__(self):
        r"""
        :param _UserId: User ID	
        :type UserId: str
        """
        self._UserId = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
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
        :param _SdkAppId: The application ID.	
        :type SdkAppId: int
        :param _UserId: User ID	
        :type UserId: str
        :param _Name: Username	
        :type Name: str
        :param _Avatar: URL of user profile photo.	
        :type Avatar: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SdkAppId = None
        self._UserId = None
        self._Name = None
        self._Avatar = None
        self._RequestId = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Avatar(self):
        return self._Avatar

    @Avatar.setter
    def Avatar(self, Avatar):
        self._Avatar = Avatar

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._UserId = params.get("UserId")
        self._Name = params.get("Name")
        self._Avatar = params.get("Avatar")
        self._RequestId = params.get("RequestId")


class DocumentInfo(AbstractModel):
    """Document Information.
    Used by actions: DescribeDocumentsByRoom.

    """

    def __init__(self):
        r"""
        :param _DocumentId: The document ID. Note: This field may return null, indicating that no valid values can be obtained.
        :type DocumentId: str
        :param _DocumentUrl: The document’s original URL. Note: This field may return null, indicating that no valid values can be obtained.
        :type DocumentUrl: str
        :param _DocumentName: The document title. Note: This field may return null, indicating that no valid values can be obtained.
        :type DocumentName: str
        :param _Owner: The user ID of the document’s owner. Note: This field may return null, indicating that no valid values can be obtained.
        :type Owner: str
        :param _SdkAppId: The application ID. Note: This field may return null, indicating that no valid values can be obtained.
        :type SdkAppId: int
        :param _Permission: The document access type. 0: Private; 1: Public. Note: This field may return null, indicating that no valid values can be obtained.
        :type Permission: int
        :param _TranscodeResult: The transcoding result. If the file is not transcoded, this parameter will be empty. If it is successfully transcoded, this parameter will be the URL of the transcoded file. If transcoding fails, this parameter will indicate the error code. Note: This field may return null, indicating that no valid values can be obtained.
        :type TranscodeResult: str
        :param _TranscodeType: The transcoding type. Note: This field may return null, indicating that no valid values can be obtained.
        :type TranscodeType: int
        :param _TranscodeProgress: The transcoding progress. Value range: 0-100. Note: This field may return null, indicating that no valid values can be obtained.
        :type TranscodeProgress: int
        :param _TranscodeState: The transcoding status. 0: The file is not transcoded. 1: The file is being transcoded. 2: Transcoding failed. 3: Transcoding is successful. Note: This field may return null, indicating that no valid values can be obtained.
        :type TranscodeState: int
        :param _TranscodeInfo: The error message for failed transcoding. Note: This field may return null, indicating that no valid values can be obtained.
        :type TranscodeInfo: str
        :param _DocumentType: The document type. Note: This field may return null, indicating that no valid values can be obtained.
        :type DocumentType: str
        :param _DocumentSize: The document size (bytes). Note: This field may return null, indicating that no valid values can be obtained.
        :type DocumentSize: int
        :param _UpdateTime: The time (Unix timestamp) when the document was last updated. Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdateTime: int
        :param _Pages: The number of pages.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Pages: int
        :param _Width: The width. This parameter is valid only if static document transcoding is used.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Width: int
        :param _Height: The height. This parameter is valid only if static document transcoding is used.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Height: int
        :param _Cover: The thumbnail. Only transcoded courseware has thumbnails.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Cover: str
        """
        self._DocumentId = None
        self._DocumentUrl = None
        self._DocumentName = None
        self._Owner = None
        self._SdkAppId = None
        self._Permission = None
        self._TranscodeResult = None
        self._TranscodeType = None
        self._TranscodeProgress = None
        self._TranscodeState = None
        self._TranscodeInfo = None
        self._DocumentType = None
        self._DocumentSize = None
        self._UpdateTime = None
        self._Pages = None
        self._Width = None
        self._Height = None
        self._Cover = None

    @property
    def DocumentId(self):
        return self._DocumentId

    @DocumentId.setter
    def DocumentId(self, DocumentId):
        self._DocumentId = DocumentId

    @property
    def DocumentUrl(self):
        return self._DocumentUrl

    @DocumentUrl.setter
    def DocumentUrl(self, DocumentUrl):
        self._DocumentUrl = DocumentUrl

    @property
    def DocumentName(self):
        return self._DocumentName

    @DocumentName.setter
    def DocumentName(self, DocumentName):
        self._DocumentName = DocumentName

    @property
    def Owner(self):
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Permission(self):
        return self._Permission

    @Permission.setter
    def Permission(self, Permission):
        self._Permission = Permission

    @property
    def TranscodeResult(self):
        return self._TranscodeResult

    @TranscodeResult.setter
    def TranscodeResult(self, TranscodeResult):
        self._TranscodeResult = TranscodeResult

    @property
    def TranscodeType(self):
        return self._TranscodeType

    @TranscodeType.setter
    def TranscodeType(self, TranscodeType):
        self._TranscodeType = TranscodeType

    @property
    def TranscodeProgress(self):
        return self._TranscodeProgress

    @TranscodeProgress.setter
    def TranscodeProgress(self, TranscodeProgress):
        self._TranscodeProgress = TranscodeProgress

    @property
    def TranscodeState(self):
        return self._TranscodeState

    @TranscodeState.setter
    def TranscodeState(self, TranscodeState):
        self._TranscodeState = TranscodeState

    @property
    def TranscodeInfo(self):
        return self._TranscodeInfo

    @TranscodeInfo.setter
    def TranscodeInfo(self, TranscodeInfo):
        self._TranscodeInfo = TranscodeInfo

    @property
    def DocumentType(self):
        return self._DocumentType

    @DocumentType.setter
    def DocumentType(self, DocumentType):
        self._DocumentType = DocumentType

    @property
    def DocumentSize(self):
        return self._DocumentSize

    @DocumentSize.setter
    def DocumentSize(self, DocumentSize):
        self._DocumentSize = DocumentSize

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Pages(self):
        return self._Pages

    @Pages.setter
    def Pages(self, Pages):
        self._Pages = Pages

    @property
    def Width(self):
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Cover(self):
        return self._Cover

    @Cover.setter
    def Cover(self, Cover):
        self._Cover = Cover


    def _deserialize(self, params):
        self._DocumentId = params.get("DocumentId")
        self._DocumentUrl = params.get("DocumentUrl")
        self._DocumentName = params.get("DocumentName")
        self._Owner = params.get("Owner")
        self._SdkAppId = params.get("SdkAppId")
        self._Permission = params.get("Permission")
        self._TranscodeResult = params.get("TranscodeResult")
        self._TranscodeType = params.get("TranscodeType")
        self._TranscodeProgress = params.get("TranscodeProgress")
        self._TranscodeState = params.get("TranscodeState")
        self._TranscodeInfo = params.get("TranscodeInfo")
        self._DocumentType = params.get("DocumentType")
        self._DocumentSize = params.get("DocumentSize")
        self._UpdateTime = params.get("UpdateTime")
        self._Pages = params.get("Pages")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._Cover = params.get("Cover")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EndRoomRequest(AbstractModel):
    """EndRoom request structure.

    """

    def __init__(self):
        r"""
        :param _RoomId: The room ID.
        :type RoomId: int
        """
        self._RoomId = None

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId


    def _deserialize(self, params):
        self._RoomId = params.get("RoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EndRoomResponse(AbstractModel):
    """EndRoom response structure.

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


class EventDataInfo(AbstractModel):
    """The information of a room event.

    """

    def __init__(self):
        r"""
        :param _RoomId: The room ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RoomId: int
        :param _UserId: The ID of the user to whom the event occurred.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UserId: str
        """
        self._RoomId = None
        self._UserId = None

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._RoomId = params.get("RoomId")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EventInfo(AbstractModel):
    """The event information.

    """

    def __init__(self):
        r"""
        :param _Timestamp: The Unix timestamp (seconds) when the event occurred.
        :type Timestamp: int
        :param _EventType: The event type. Valid values: 
`RoomStart`: The class started. `RoomEnd`: The class ended. `MemberJoin`: A user joined. `MemberQuit`: A user left. `RecordFinish`: Recording is finished.
·Camera0n·: The camera is turned on.
`Camera0ff`: The camera is turned off.
`MicOn`: The mic is turned on.
`MicOff`: The mic is turned off.
`ScreenOn`: Screen sharing is enabled.
`ScreenOff`: Screen sharing is disabled.
`VisibleOn`: The page is visible.
`VisibleOff`: The page is invisible.
        :type EventType: str
        :param _EventData: The details of the event, including the room ID and the user to whom the event occurred.
Note: This field may return null, indicating that no valid values can be obtained.
        :type EventData: :class:`tencentcloud.lcic.v20220817.models.EventDataInfo`
        """
        self._Timestamp = None
        self._EventType = None
        self._EventData = None

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def EventType(self):
        return self._EventType

    @EventType.setter
    def EventType(self, EventType):
        self._EventType = EventType

    @property
    def EventData(self):
        return self._EventData

    @EventData.setter
    def EventData(self, EventData):
        self._EventData = EventData


    def _deserialize(self, params):
        self._Timestamp = params.get("Timestamp")
        self._EventType = params.get("EventType")
        if params.get("EventData") is not None:
            self._EventData = EventDataInfo()
            self._EventData._deserialize(params.get("EventData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRoomEventRequest(AbstractModel):
    """GetRoomEvent request structure.

    """

    def __init__(self):
        r"""
        :param _RoomId: The room ID.
        :type RoomId: int
        :param _SdkAppId: The application ID.
        :type SdkAppId: int
        :param _Page: The starting page. Pagination starts from 1. This parameter is valid only if `keyword` is empty.
        :type Page: int
        :param _Limit: The maximum number of records (up to 200) per page. This parameter is valid only if `keyword` is empty.
        :type Limit: int
        :param _Keyword: The type of events to query. Valid values:
`RoomStart`: The class started.
`RoomEnd`: The class ended.
`MemberJoin`: A user joined.
`MemberQuit`: A user left.
`RecordFinish`: Recording is finished.
        :type Keyword: str
        """
        self._RoomId = None
        self._SdkAppId = None
        self._Page = None
        self._Limit = None
        self._Keyword = None

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword


    def _deserialize(self, params):
        self._RoomId = params.get("RoomId")
        self._SdkAppId = params.get("SdkAppId")
        self._Page = params.get("Page")
        self._Limit = params.get("Limit")
        self._Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRoomEventResponse(AbstractModel):
    """GetRoomEvent response structure.

    """

    def __init__(self):
        r"""
        :param _Total: The total number of events for the room. The value of this parameter is not affected by `keyword`.
        :type Total: int
        :param _Events: The event details, including the type and time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Events: list of EventInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._Events = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Events(self):
        return self._Events

    @Events.setter
    def Events(self, Events):
        self._Events = Events

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Events") is not None:
            self._Events = []
            for item in params.get("Events"):
                obj = EventInfo()
                obj._deserialize(item)
                self._Events.append(obj)
        self._RequestId = params.get("RequestId")


class GetRoomMessageRequest(AbstractModel):
    """GetRoomMessage request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: The SDKAppID assigned by LCIC.
        :type SdkAppId: int
        :param _RoomId: The room ID.
        :type RoomId: int
        :param _Seq: The starting message sequence. Messages before this sequence will be returned (not including the message whose sequence is `seq`).
        :type Seq: int
        :param _Limit: The maximum number of messages to return. The value of this parameter cannot exceed the maximum message count allowed by your package.
        :type Limit: int
        """
        self._SdkAppId = None
        self._RoomId = None
        self._Seq = None
        self._Limit = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def Seq(self):
        return self._Seq

    @Seq.setter
    def Seq(self, Seq):
        self._Seq = Seq

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        self._Seq = params.get("Seq")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRoomMessageResponse(AbstractModel):
    """GetRoomMessage response structure.

    """

    def __init__(self):
        r"""
        :param _Messages: The message list.
        :type Messages: list of MessageList
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Messages = None
        self._RequestId = None

    @property
    def Messages(self):
        return self._Messages

    @Messages.setter
    def Messages(self, Messages):
        self._Messages = Messages

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Messages") is not None:
            self._Messages = []
            for item in params.get("Messages"):
                obj = MessageList()
                obj._deserialize(item)
                self._Messages.append(obj)
        self._RequestId = params.get("RequestId")


class GetRoomsRequest(AbstractModel):
    """GetRooms request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: The SDKAppID assigned by LCIC.

        :type SdkAppId: int
        :param _StartTime: The start time. The default start time is 30 minutes before the current time.
        :type StartTime: int
        :param _EndTime: The end time. The default end time is 30 minutes after the current time.
        :type EndTime: int
        :param _Page: The page to return records from. Pagination starts from 1.
        :type Page: int
        :param _Limit: The number of records per page. The default is 10.
        :type Limit: int
        """
        self._SdkAppId = None
        self._StartTime = None
        self._EndTime = None
        self._Page = None
        self._Limit = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Page = params.get("Page")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRoomsResponse(AbstractModel):
    """GetRooms response structure.

    """

    def __init__(self):
        r"""
        :param _Total: The total number of rooms.
        :type Total: int
        :param _Rooms: The room list.
        :type Rooms: list of RoomItem
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._Rooms = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Rooms(self):
        return self._Rooms

    @Rooms.setter
    def Rooms(self, Rooms):
        self._Rooms = Rooms

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Rooms") is not None:
            self._Rooms = []
            for item in params.get("Rooms"):
                obj = RoomItem()
                obj._deserialize(item)
                self._Rooms.append(obj)
        self._RequestId = params.get("RequestId")


class GetWatermarkRequest(AbstractModel):
    """GetWatermark request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: The SDKAppID assigned by LCIC.
        :type SdkAppId: int
        """
        self._SdkAppId = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetWatermarkResponse(AbstractModel):
    """GetWatermark response structure.

    """

    def __init__(self):
        r"""
        :param _TeacherLogo: The watermark settings for the teacher’s video. Note: This field may return null, indicating that no valid values can be obtained.
        :type TeacherLogo: :class:`tencentcloud.lcic.v20220817.models.WatermarkConfig`
        :param _BoardLogo: The watermark settings for the whiteboard. Note: This field may return null, indicating that no valid values can be obtained.
        :type BoardLogo: :class:`tencentcloud.lcic.v20220817.models.WatermarkConfig`
        :param _BackgroundPicture: The background image. Note: This field may return null, indicating that no valid values can be obtained.
        :type BackgroundPicture: :class:`tencentcloud.lcic.v20220817.models.BackgroundPictureConfig`
        :param _Text: The watermark text. Note: This field may return null, indicating that no valid values can be obtained.
        :type Text: :class:`tencentcloud.lcic.v20220817.models.TextMarkConfig`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TeacherLogo = None
        self._BoardLogo = None
        self._BackgroundPicture = None
        self._Text = None
        self._RequestId = None

    @property
    def TeacherLogo(self):
        return self._TeacherLogo

    @TeacherLogo.setter
    def TeacherLogo(self, TeacherLogo):
        self._TeacherLogo = TeacherLogo

    @property
    def BoardLogo(self):
        return self._BoardLogo

    @BoardLogo.setter
    def BoardLogo(self, BoardLogo):
        self._BoardLogo = BoardLogo

    @property
    def BackgroundPicture(self):
        return self._BackgroundPicture

    @BackgroundPicture.setter
    def BackgroundPicture(self, BackgroundPicture):
        self._BackgroundPicture = BackgroundPicture

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TeacherLogo") is not None:
            self._TeacherLogo = WatermarkConfig()
            self._TeacherLogo._deserialize(params.get("TeacherLogo"))
        if params.get("BoardLogo") is not None:
            self._BoardLogo = WatermarkConfig()
            self._BoardLogo._deserialize(params.get("BoardLogo"))
        if params.get("BackgroundPicture") is not None:
            self._BackgroundPicture = BackgroundPictureConfig()
            self._BackgroundPicture._deserialize(params.get("BackgroundPicture"))
        if params.get("Text") is not None:
            self._Text = TextMarkConfig()
            self._Text._deserialize(params.get("Text"))
        self._RequestId = params.get("RequestId")


class GroupBaseInfo(AbstractModel):
    """The information of the groups to create.
    Used by actions: BatchCreateGroupWithMembers.

    """

    def __init__(self):
        r"""
        :param _GroupName: The group names. Note: This field may return null, indicating that no valid values can be obtained.
        :type GroupName: str
        :param _TeacherId: The user ID of the teacher. Note: This field may return null, indicating that no valid values can be obtained.
        :type TeacherId: str
        """
        self._GroupName = None
        self._TeacherId = None

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def TeacherId(self):
        return self._TeacherId

    @TeacherId.setter
    def TeacherId(self, TeacherId):
        self._TeacherId = TeacherId


    def _deserialize(self, params):
        self._GroupName = params.get("GroupName")
        self._TeacherId = params.get("TeacherId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupInfo(AbstractModel):
    """The information of the groups queried.
    Used by actions: DescribeGroupList.

    """

    def __init__(self):
        r"""
        :param _GroupId: 
Note: This field may return null, indicating that no valid values can be obtained.
        :type GroupId: str
        :param _GroupName: 
Note: This field may return null, indicating that no valid values can be obtained.
        :type GroupName: str
        :param _TeacherId: 
Note: This field may return null, indicating that no valid values can be obtained.
        :type TeacherId: str
        :param _GroupType: 
Note: This field may return null, indicating that no valid values can be obtained.
        :type GroupType: int
        :param _SubGroupIds: 
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubGroupIds: str
        """
        self._GroupId = None
        self._GroupName = None
        self._TeacherId = None
        self._GroupType = None
        self._SubGroupIds = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def TeacherId(self):
        return self._TeacherId

    @TeacherId.setter
    def TeacherId(self, TeacherId):
        self._TeacherId = TeacherId

    @property
    def GroupType(self):
        return self._GroupType

    @GroupType.setter
    def GroupType(self, GroupType):
        self._GroupType = GroupType

    @property
    def SubGroupIds(self):
        return self._SubGroupIds

    @SubGroupIds.setter
    def SubGroupIds(self, SubGroupIds):
        self._SubGroupIds = SubGroupIds


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._TeacherId = params.get("TeacherId")
        self._GroupType = params.get("GroupType")
        self._SubGroupIds = params.get("SubGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KickUserFromRoomRequest(AbstractModel):
    """KickUserFromRoom request structure.

    """

    def __init__(self):
        r"""
        :param _RoomId: The room ID.
        :type RoomId: int
        :param _SdkAppId: The SDKAppID assigned by LCIC.
        :type SdkAppId: int
        :param _UserId: The ID of the user to be removed.
        :type UserId: str
        :param _KickType: The removal type: 
`1`: Keep the user out temporarily. The `Duration` parameter specifies the ban duration, during which the user is banned from entering the room. 
`2`: Remove the user permanently.
        :type KickType: int
        :param _Duration: The ban duration (seconds). This parameter is valid if `KickType` is `1`. The default value is `0`.
        :type Duration: int
        """
        self._RoomId = None
        self._SdkAppId = None
        self._UserId = None
        self._KickType = None
        self._Duration = None

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def KickType(self):
        return self._KickType

    @KickType.setter
    def KickType(self, KickType):
        self._KickType = KickType

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration


    def _deserialize(self, params):
        self._RoomId = params.get("RoomId")
        self._SdkAppId = params.get("SdkAppId")
        self._UserId = params.get("UserId")
        self._KickType = params.get("KickType")
        self._Duration = params.get("Duration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KickUserFromRoomResponse(AbstractModel):
    """KickUserFromRoom response structure.

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


class LoginOriginIdRequest(AbstractModel):
    """LoginOriginId request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: LCIC SdkAppId
        :type SdkAppId: int
        :param _OriginId: User's ID in the customer system, which should be unique under the same application
        :type OriginId: str
        """
        self._SdkAppId = None
        self._OriginId = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def OriginId(self):
        return self._OriginId

    @OriginId.setter
    def OriginId(self, OriginId):
        self._OriginId = OriginId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._OriginId = params.get("OriginId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginOriginIdResponse(AbstractModel):
    """LoginOriginId response structure.

    """

    def __init__(self):
        r"""
        :param _UserId: User ID
        :type UserId: str
        :param _Token: Login status token returned after successful login or registration. The token is valid for seven days.
        :type Token: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._UserId = None
        self._Token = None
        self._RequestId = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Token(self):
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._Token = params.get("Token")
        self._RequestId = params.get("RequestId")


class LoginUserRequest(AbstractModel):
    """LoginUser request structure.

    """

    def __init__(self):
        r"""
        :param _UserId: User ID obtained during registration
        :type UserId: str
        """
        self._UserId = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginUserResponse(AbstractModel):
    """LoginUser response structure.

    """

    def __init__(self):
        r"""
        :param _UserId: User ID
        :type UserId: str
        :param _Token: Login status token returned after successful login or registration. The token is valid for seven days.
        :type Token: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._UserId = None
        self._Token = None
        self._RequestId = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Token(self):
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._Token = params.get("Token")
        self._RequestId = params.get("RequestId")


class MemberRecord(AbstractModel):
    """Member record information
    Used by actions: DescribeCurrentMemberList, DescribeRoomStatistics.

    """

    def __init__(self):
        r"""
        :param _UserId: User ID
        :type UserId: str
        :param _UserName: Username
        :type UserName: str
        :param _PresentTime: Online duration, in seconds
        :type PresentTime: int
        :param _Camera: Whether the camera is enabled
        :type Camera: int
        :param _Mic: Whether the mic is enabled
        :type Mic: int
        :param _Silence: Whether the user is muted
        :type Silence: int
        :param _AnswerQuestions: Number of questions answered by the user
        :type AnswerQuestions: int
        :param _HandUps: Number of hand raising times
        :type HandUps: int
        :param _FirstJoinTimestamp: First time that the user entered the room, in UNIX timestamp format
        :type FirstJoinTimestamp: int
        :param _LastQuitTimestamp: Last time that the user left the room, in UNIX timestamp format
        :type LastQuitTimestamp: int
        :param _Rewords: Number of rewards received
        :type Rewords: int
        :param _IPAddress: The user’s IP address.
        :type IPAddress: str
        :param _Location: The user’s location.
        :type Location: str
        :param _Device: The user’s device type. 0: Unknown; 1: Windows; 2: macOS; 3: Android; 4: iOS; 5: Web; 6: Mobile webpage; 7: Weixin Mini Program.
        :type Device: int
        :param _PerMemberMicCount: The number of times a user turned their mic on.
        :type PerMemberMicCount: int
        :param _PerMemberMessageCount: The number of messages sent by a user.
        :type PerMemberMessageCount: int
        :param _Role: The user role. `0`: Student; `1`: Teacher; `2`: Teaching Assistant; `3`: Spectator.
        :type Role: int
        :param _GroupId: The class number.
        :type GroupId: str
        :param _SubGroupId: The sub-class number.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubGroupId: list of str
        :param _Stage: Whether the user is on the stage.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Stage: int
        """
        self._UserId = None
        self._UserName = None
        self._PresentTime = None
        self._Camera = None
        self._Mic = None
        self._Silence = None
        self._AnswerQuestions = None
        self._HandUps = None
        self._FirstJoinTimestamp = None
        self._LastQuitTimestamp = None
        self._Rewords = None
        self._IPAddress = None
        self._Location = None
        self._Device = None
        self._PerMemberMicCount = None
        self._PerMemberMessageCount = None
        self._Role = None
        self._GroupId = None
        self._SubGroupId = None
        self._Stage = None

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
    def PresentTime(self):
        return self._PresentTime

    @PresentTime.setter
    def PresentTime(self, PresentTime):
        self._PresentTime = PresentTime

    @property
    def Camera(self):
        return self._Camera

    @Camera.setter
    def Camera(self, Camera):
        self._Camera = Camera

    @property
    def Mic(self):
        return self._Mic

    @Mic.setter
    def Mic(self, Mic):
        self._Mic = Mic

    @property
    def Silence(self):
        return self._Silence

    @Silence.setter
    def Silence(self, Silence):
        self._Silence = Silence

    @property
    def AnswerQuestions(self):
        return self._AnswerQuestions

    @AnswerQuestions.setter
    def AnswerQuestions(self, AnswerQuestions):
        self._AnswerQuestions = AnswerQuestions

    @property
    def HandUps(self):
        return self._HandUps

    @HandUps.setter
    def HandUps(self, HandUps):
        self._HandUps = HandUps

    @property
    def FirstJoinTimestamp(self):
        return self._FirstJoinTimestamp

    @FirstJoinTimestamp.setter
    def FirstJoinTimestamp(self, FirstJoinTimestamp):
        self._FirstJoinTimestamp = FirstJoinTimestamp

    @property
    def LastQuitTimestamp(self):
        return self._LastQuitTimestamp

    @LastQuitTimestamp.setter
    def LastQuitTimestamp(self, LastQuitTimestamp):
        self._LastQuitTimestamp = LastQuitTimestamp

    @property
    def Rewords(self):
        return self._Rewords

    @Rewords.setter
    def Rewords(self, Rewords):
        self._Rewords = Rewords

    @property
    def IPAddress(self):
        return self._IPAddress

    @IPAddress.setter
    def IPAddress(self, IPAddress):
        self._IPAddress = IPAddress

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def Device(self):
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def PerMemberMicCount(self):
        return self._PerMemberMicCount

    @PerMemberMicCount.setter
    def PerMemberMicCount(self, PerMemberMicCount):
        self._PerMemberMicCount = PerMemberMicCount

    @property
    def PerMemberMessageCount(self):
        return self._PerMemberMessageCount

    @PerMemberMessageCount.setter
    def PerMemberMessageCount(self, PerMemberMessageCount):
        self._PerMemberMessageCount = PerMemberMessageCount

    @property
    def Role(self):
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def SubGroupId(self):
        return self._SubGroupId

    @SubGroupId.setter
    def SubGroupId(self, SubGroupId):
        self._SubGroupId = SubGroupId

    @property
    def Stage(self):
        return self._Stage

    @Stage.setter
    def Stage(self, Stage):
        self._Stage = Stage


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._UserName = params.get("UserName")
        self._PresentTime = params.get("PresentTime")
        self._Camera = params.get("Camera")
        self._Mic = params.get("Mic")
        self._Silence = params.get("Silence")
        self._AnswerQuestions = params.get("AnswerQuestions")
        self._HandUps = params.get("HandUps")
        self._FirstJoinTimestamp = params.get("FirstJoinTimestamp")
        self._LastQuitTimestamp = params.get("LastQuitTimestamp")
        self._Rewords = params.get("Rewords")
        self._IPAddress = params.get("IPAddress")
        self._Location = params.get("Location")
        self._Device = params.get("Device")
        self._PerMemberMicCount = params.get("PerMemberMicCount")
        self._PerMemberMessageCount = params.get("PerMemberMessageCount")
        self._Role = params.get("Role")
        self._GroupId = params.get("GroupId")
        self._SubGroupId = params.get("SubGroupId")
        self._Stage = params.get("Stage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MessageItem(AbstractModel):
    """The information of a message.

    """

    def __init__(self):
        r"""
        :param _MessageType: The message type. `0`: Text; `1`: Image.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MessageType: int
        :param _TextMessage: The text. This parameter is valid if `MessageType` is `0`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TextMessage: str
        :param _ImageMessage: The image URL. This parameter is valid if `MessageType` is `1`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ImageMessage: str
        """
        self._MessageType = None
        self._TextMessage = None
        self._ImageMessage = None

    @property
    def MessageType(self):
        return self._MessageType

    @MessageType.setter
    def MessageType(self, MessageType):
        self._MessageType = MessageType

    @property
    def TextMessage(self):
        return self._TextMessage

    @TextMessage.setter
    def TextMessage(self, TextMessage):
        self._TextMessage = TextMessage

    @property
    def ImageMessage(self):
        return self._ImageMessage

    @ImageMessage.setter
    def ImageMessage(self, ImageMessage):
        self._ImageMessage = ImageMessage


    def _deserialize(self, params):
        self._MessageType = params.get("MessageType")
        self._TextMessage = params.get("TextMessage")
        self._ImageMessage = params.get("ImageMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MessageList(AbstractModel):
    """The list of historical messages.

    """

    def __init__(self):
        r"""
        :param _Timestamp: The message timestamp.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Timestamp: int
        :param _FromAccount: The sender.
Note: This field may return null, indicating that no valid values can be obtained.
        :type FromAccount: str
        :param _Seq: The message sequence, which is unique across a class. The earlier a message is sent, the lower the sequence.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Seq: int
        :param _MessageBody: The message content.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MessageBody: list of MessageItem
        """
        self._Timestamp = None
        self._FromAccount = None
        self._Seq = None
        self._MessageBody = None

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def FromAccount(self):
        return self._FromAccount

    @FromAccount.setter
    def FromAccount(self, FromAccount):
        self._FromAccount = FromAccount

    @property
    def Seq(self):
        return self._Seq

    @Seq.setter
    def Seq(self, Seq):
        self._Seq = Seq

    @property
    def MessageBody(self):
        return self._MessageBody

    @MessageBody.setter
    def MessageBody(self, MessageBody):
        self._MessageBody = MessageBody


    def _deserialize(self, params):
        self._Timestamp = params.get("Timestamp")
        self._FromAccount = params.get("FromAccount")
        self._Seq = params.get("Seq")
        if params.get("MessageBody") is not None:
            self._MessageBody = []
            for item in params.get("MessageBody"):
                obj = MessageItem()
                obj._deserialize(item)
                self._MessageBody.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAppRequest(AbstractModel):
    """ModifyApp request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: LCIC SdkAppId
        :type SdkAppId: int
        :param _Callback: Callback URL. Currently, only port 80 and port 443 are supported.
        :type Callback: str
        :param _CallbackKey: The callback key.
        :type CallbackKey: str
        """
        self._SdkAppId = None
        self._Callback = None
        self._CallbackKey = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Callback(self):
        return self._Callback

    @Callback.setter
    def Callback(self, Callback):
        self._Callback = Callback

    @property
    def CallbackKey(self):
        return self._CallbackKey

    @CallbackKey.setter
    def CallbackKey(self, CallbackKey):
        self._CallbackKey = CallbackKey


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Callback = params.get("Callback")
        self._CallbackKey = params.get("CallbackKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAppResponse(AbstractModel):
    """ModifyApp response structure.

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


class ModifyGroupRequest(AbstractModel):
    """ModifyGroup request structure.

    """

    def __init__(self):
        r"""
        :param _GroupId: The ID of the group to modify.
        :type GroupId: str
        :param _SdkAppId: The SDKAppID assigned by LCIC.
        :type SdkAppId: int
        :param _TeacherId: The user ID of the teacher.
        :type TeacherId: str
        :param _GroupName: The new group name.
        :type GroupName: str
        """
        self._GroupId = None
        self._SdkAppId = None
        self._TeacherId = None
        self._GroupName = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TeacherId(self):
        return self._TeacherId

    @TeacherId.setter
    def TeacherId(self, TeacherId):
        self._TeacherId = TeacherId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._SdkAppId = params.get("SdkAppId")
        self._TeacherId = params.get("TeacherId")
        self._GroupName = params.get("GroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyGroupResponse(AbstractModel):
    """ModifyGroup response structure.

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


class ModifyRoomRequest(AbstractModel):
    """ModifyRoom request structure.

    """

    def __init__(self):
        r"""
        :param _RoomId: The room ID.
        :type RoomId: int
        :param _SdkAppId: The SDKAppID assigned by LCIC.
        :type SdkAppId: int
        :param _StartTime: The room start time (Unix timestamp).
        :type StartTime: int
        :param _EndTime: The room end time (Unix timestamp).
        :type EndTime: int
        :param _TeacherId: The user ID of the teacher. User IDs are returned by the user registration APIs.
        :type TeacherId: str
        :param _Name: The room name.
        :type Name: str
        :param _Resolution: The resolution. Valid values: 1: SD; 2: HD; 3: FHD.
        :type Resolution: int
        :param _MaxMicNumber: The maximum number of mic-on users (excluding the teacher). Value range: 0-16.
        :type MaxMicNumber: int
        :param _AutoMic: Whether to automatically turn the mic on when a user enters the room. Valid values: 0: No (default value); 1: Yes.
        :type AutoMic: int
        :param _AudioQuality: Whether to enable the high audio quality mode. Valid values: 0: No (default value); 1: Yes.
        :type AudioQuality: int
        :param _SubType: The room subtype. Valid values: videodoc: Document + Video; video: Video only; coteaching: Dual-teacher.
        :type SubType: str
        :param _DisableRecord: Whether to disable auto recording. Valid values: 0: No (default); 1: Yes. If this parameter is 0, recording will start when the class starts and stops when the class ends.
        :type DisableRecord: int
        :param _Assistants: The user IDs of the teacher assistants. User IDs are returned by the user registration APIs.
        :type Assistants: list of str
        :param _GroupId: The ID of the group to bind.
        :type GroupId: str
        :param _EnableDirectControl: Whether the students' consent is required to control their cameras/microphones.
        :type EnableDirectControl: int
        """
        self._RoomId = None
        self._SdkAppId = None
        self._StartTime = None
        self._EndTime = None
        self._TeacherId = None
        self._Name = None
        self._Resolution = None
        self._MaxMicNumber = None
        self._AutoMic = None
        self._AudioQuality = None
        self._SubType = None
        self._DisableRecord = None
        self._Assistants = None
        self._GroupId = None
        self._EnableDirectControl = None

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def TeacherId(self):
        return self._TeacherId

    @TeacherId.setter
    def TeacherId(self, TeacherId):
        self._TeacherId = TeacherId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Resolution(self):
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def MaxMicNumber(self):
        return self._MaxMicNumber

    @MaxMicNumber.setter
    def MaxMicNumber(self, MaxMicNumber):
        self._MaxMicNumber = MaxMicNumber

    @property
    def AutoMic(self):
        return self._AutoMic

    @AutoMic.setter
    def AutoMic(self, AutoMic):
        self._AutoMic = AutoMic

    @property
    def AudioQuality(self):
        return self._AudioQuality

    @AudioQuality.setter
    def AudioQuality(self, AudioQuality):
        self._AudioQuality = AudioQuality

    @property
    def SubType(self):
        return self._SubType

    @SubType.setter
    def SubType(self, SubType):
        self._SubType = SubType

    @property
    def DisableRecord(self):
        return self._DisableRecord

    @DisableRecord.setter
    def DisableRecord(self, DisableRecord):
        self._DisableRecord = DisableRecord

    @property
    def Assistants(self):
        return self._Assistants

    @Assistants.setter
    def Assistants(self, Assistants):
        self._Assistants = Assistants

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def EnableDirectControl(self):
        return self._EnableDirectControl

    @EnableDirectControl.setter
    def EnableDirectControl(self, EnableDirectControl):
        self._EnableDirectControl = EnableDirectControl


    def _deserialize(self, params):
        self._RoomId = params.get("RoomId")
        self._SdkAppId = params.get("SdkAppId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._TeacherId = params.get("TeacherId")
        self._Name = params.get("Name")
        self._Resolution = params.get("Resolution")
        self._MaxMicNumber = params.get("MaxMicNumber")
        self._AutoMic = params.get("AutoMic")
        self._AudioQuality = params.get("AudioQuality")
        self._SubType = params.get("SubType")
        self._DisableRecord = params.get("DisableRecord")
        self._Assistants = params.get("Assistants")
        self._GroupId = params.get("GroupId")
        self._EnableDirectControl = params.get("EnableDirectControl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRoomResponse(AbstractModel):
    """ModifyRoom response structure.

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


class ModifyUserProfileRequest(AbstractModel):
    """ModifyUserProfile request structure.

    """

    def __init__(self):
        r"""
        :param _UserId: The ID of the user whose profile will be modified.
        :type UserId: str
        :param _Nickname: The new username to use.
        :type Nickname: str
        :param _Avatar: The URL of the new profile photo.
        :type Avatar: str
        """
        self._UserId = None
        self._Nickname = None
        self._Avatar = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Nickname(self):
        return self._Nickname

    @Nickname.setter
    def Nickname(self, Nickname):
        self._Nickname = Nickname

    @property
    def Avatar(self):
        return self._Avatar

    @Avatar.setter
    def Avatar(self, Avatar):
        self._Avatar = Avatar


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._Nickname = params.get("Nickname")
        self._Avatar = params.get("Avatar")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUserProfileResponse(AbstractModel):
    """ModifyUserProfile response structure.

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


class QuestionInfo(AbstractModel):
    """A quiz question in a room.

    """

    def __init__(self):
        r"""
        :param _QuestionId: The question ID.
        :type QuestionId: str
        :param _QuestionContent: The question.
        :type QuestionContent: str
        :param _Duration: The time limit for the question. If you set this parameter to `0`, there will not be a time limit.
        :type Duration: int
        :param _CorrectAnswer: The correct answer. Bits are used to indicate the options that should be chosen. For example, `0x1` indicates option A; `0x11` indicates A and B, and so on.
        :type CorrectAnswer: int
        :param _AnswerStats: The statistics for each type of answer.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AnswerStats: list of AnswerStat
        """
        self._QuestionId = None
        self._QuestionContent = None
        self._Duration = None
        self._CorrectAnswer = None
        self._AnswerStats = None

    @property
    def QuestionId(self):
        return self._QuestionId

    @QuestionId.setter
    def QuestionId(self, QuestionId):
        self._QuestionId = QuestionId

    @property
    def QuestionContent(self):
        return self._QuestionContent

    @QuestionContent.setter
    def QuestionContent(self, QuestionContent):
        self._QuestionContent = QuestionContent

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def CorrectAnswer(self):
        return self._CorrectAnswer

    @CorrectAnswer.setter
    def CorrectAnswer(self, CorrectAnswer):
        self._CorrectAnswer = CorrectAnswer

    @property
    def AnswerStats(self):
        return self._AnswerStats

    @AnswerStats.setter
    def AnswerStats(self, AnswerStats):
        self._AnswerStats = AnswerStats


    def _deserialize(self, params):
        self._QuestionId = params.get("QuestionId")
        self._QuestionContent = params.get("QuestionContent")
        self._Duration = params.get("Duration")
        self._CorrectAnswer = params.get("CorrectAnswer")
        if params.get("AnswerStats") is not None:
            self._AnswerStats = []
            for item in params.get("AnswerStats"):
                obj = AnswerStat()
                obj._deserialize(item)
                self._AnswerStats.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterUserRequest(AbstractModel):
    """RegisterUser request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: LCIC SdkAppId	
        :type SdkAppId: int
        :param _Name: Username	
        :type Name: str
        :param _OriginId: User's ID in the customer system, which should be unique under the same application	
        :type OriginId: str
        :param _Avatar: User's profile photo	
        :type Avatar: str
        """
        self._SdkAppId = None
        self._Name = None
        self._OriginId = None
        self._Avatar = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def OriginId(self):
        return self._OriginId

    @OriginId.setter
    def OriginId(self, OriginId):
        self._OriginId = OriginId

    @property
    def Avatar(self):
        return self._Avatar

    @Avatar.setter
    def Avatar(self, Avatar):
        self._Avatar = Avatar


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Name = params.get("Name")
        self._OriginId = params.get("OriginId")
        self._Avatar = params.get("Avatar")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterUserResponse(AbstractModel):
    """RegisterUser response structure.

    """

    def __init__(self):
        r"""
        :param _UserId: User ID	
        :type UserId: str
        :param _Token: Login status token returned after successful login or registration. The token is valid for seven days.	
        :type Token: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._UserId = None
        self._Token = None
        self._RequestId = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Token(self):
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._Token = params.get("Token")
        self._RequestId = params.get("RequestId")


class RoomInfo(AbstractModel):
    """The information of the room to create.
    Used by actions: BatchCreateRoom.

    """

    def __init__(self):
        r"""
        :param _Name: The room name.
        :type Name: str
        :param _StartTime: The room start time (Unix timestamp).
        :type StartTime: int
        :param _EndTime: The room end time (Unix timestamp).
        :type EndTime: int
        :param _Resolution: The resolution. Valid values: `1`: SD; `2`: HD; `3`: FHD.
        :type Resolution: int
        :param _MaxMicNumber: The maximum number of mic-on users (excluding the teacher). Value range: 0-16.
        :type MaxMicNumber: int
        :param _SubType: The room subtype. Valid values: `videodoc`: Document + Video; `video`: Video only; `coteaching`: Dual-teacher.
        :type SubType: str
        :param _TeacherId: The user ID of the teacher. User IDs are returned by the user registration APIs.
        :type TeacherId: str
        :param _AutoMic: Whether to automatically turn the mic on when a user enters the room. Valid values: `0` (default): No; `1`: Yes.
        :type AutoMic: int
        :param _TurnOffMic: Whether to disconnect communication after audio/video permissions are revoked. Valid values: `0` (default): Yes; `1`: No.
        :type TurnOffMic: int
        :param _AudioQuality: Whether to enable the high audio quality mode. Valid values: `0` (default): No; `1`: Yes.
        :type AudioQuality: int
        :param _DisableRecord: Whether to disable auto recording. Valid values: `0` (default): No; `1`: Yes. If this parameter is `0`, recording will start when the class starts and stops when the class ends.
        :type DisableRecord: int
        :param _Assistants: The user IDs of the teacher assistants. User IDs are returned by the user registration APIs.
        :type Assistants: list of str
        :param _RTCAudienceNumber: The number of RTC users.
        :type RTCAudienceNumber: int
        :param _AudienceType: The audience type.
        :type AudienceType: int
        :param _RecordLayout: The recording layout.
        :type RecordLayout: int
        :param _GroupId: The ID of the group to bind. Note: This field may return null, indicating that no valid values can be obtained.
        :type GroupId: str
        :param _EnableDirectControl: Whether the students' consent is required to control their cameras/microphones.
        :type EnableDirectControl: int
        """
        self._Name = None
        self._StartTime = None
        self._EndTime = None
        self._Resolution = None
        self._MaxMicNumber = None
        self._SubType = None
        self._TeacherId = None
        self._AutoMic = None
        self._TurnOffMic = None
        self._AudioQuality = None
        self._DisableRecord = None
        self._Assistants = None
        self._RTCAudienceNumber = None
        self._AudienceType = None
        self._RecordLayout = None
        self._GroupId = None
        self._EnableDirectControl = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Resolution(self):
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def MaxMicNumber(self):
        return self._MaxMicNumber

    @MaxMicNumber.setter
    def MaxMicNumber(self, MaxMicNumber):
        self._MaxMicNumber = MaxMicNumber

    @property
    def SubType(self):
        return self._SubType

    @SubType.setter
    def SubType(self, SubType):
        self._SubType = SubType

    @property
    def TeacherId(self):
        return self._TeacherId

    @TeacherId.setter
    def TeacherId(self, TeacherId):
        self._TeacherId = TeacherId

    @property
    def AutoMic(self):
        return self._AutoMic

    @AutoMic.setter
    def AutoMic(self, AutoMic):
        self._AutoMic = AutoMic

    @property
    def TurnOffMic(self):
        return self._TurnOffMic

    @TurnOffMic.setter
    def TurnOffMic(self, TurnOffMic):
        self._TurnOffMic = TurnOffMic

    @property
    def AudioQuality(self):
        return self._AudioQuality

    @AudioQuality.setter
    def AudioQuality(self, AudioQuality):
        self._AudioQuality = AudioQuality

    @property
    def DisableRecord(self):
        return self._DisableRecord

    @DisableRecord.setter
    def DisableRecord(self, DisableRecord):
        self._DisableRecord = DisableRecord

    @property
    def Assistants(self):
        return self._Assistants

    @Assistants.setter
    def Assistants(self, Assistants):
        self._Assistants = Assistants

    @property
    def RTCAudienceNumber(self):
        return self._RTCAudienceNumber

    @RTCAudienceNumber.setter
    def RTCAudienceNumber(self, RTCAudienceNumber):
        self._RTCAudienceNumber = RTCAudienceNumber

    @property
    def AudienceType(self):
        return self._AudienceType

    @AudienceType.setter
    def AudienceType(self, AudienceType):
        self._AudienceType = AudienceType

    @property
    def RecordLayout(self):
        return self._RecordLayout

    @RecordLayout.setter
    def RecordLayout(self, RecordLayout):
        self._RecordLayout = RecordLayout

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def EnableDirectControl(self):
        return self._EnableDirectControl

    @EnableDirectControl.setter
    def EnableDirectControl(self, EnableDirectControl):
        self._EnableDirectControl = EnableDirectControl


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Resolution = params.get("Resolution")
        self._MaxMicNumber = params.get("MaxMicNumber")
        self._SubType = params.get("SubType")
        self._TeacherId = params.get("TeacherId")
        self._AutoMic = params.get("AutoMic")
        self._TurnOffMic = params.get("TurnOffMic")
        self._AudioQuality = params.get("AudioQuality")
        self._DisableRecord = params.get("DisableRecord")
        self._Assistants = params.get("Assistants")
        self._RTCAudienceNumber = params.get("RTCAudienceNumber")
        self._AudienceType = params.get("AudienceType")
        self._RecordLayout = params.get("RecordLayout")
        self._GroupId = params.get("GroupId")
        self._EnableDirectControl = params.get("EnableDirectControl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RoomItem(AbstractModel):
    """The room list.

    """

    def __init__(self):
        r"""
        :param _Name: The name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Name: str
        :param _RoomId: The room ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RoomId: int
        :param _Status: The room status. `0`: Not started; `1`: Started; `2`: Ended.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: int
        :param _StartTime: The scheduled start time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type StartTime: int
        :param _EndTime: The scheduled end time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type EndTime: int
        :param _RealStartTime: The actual start time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RealStartTime: int
        :param _RealEndTime: The actual end time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RealEndTime: int
        :param _Resolution: The resolution. `1`: SD.
`2`: HD
`3`: FHD
Note: This field may return null, indicating that no valid values can be obtained.
        :type Resolution: int
        :param _MaxRTCMember: The maximum number of mic-on users allowed.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MaxRTCMember: int
        :param _ReplayUrl: The URL of the room's recording. This parameter has been deprecated. Please use `RecordUrl` instead.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ReplayUrl: str
        :param _RecordUrl: The recording URL (HTTPS), which is generated only after a room ends.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RecordUrl: str
        :param _MaxMicNumber: The maximum number of users allowed (including teachers) in the room. The default value is `0`, which indicates that no limit is set. 
Note: This field may return null, indicating that no valid values can be obtained.
        :type MaxMicNumber: int
        :param _EnableDirectControl: Whether the students' consent is required to control their cameras/microphones.
Note: This field may return null, indicating that no valid value was found.
        :type EnableDirectControl: int
        """
        self._Name = None
        self._RoomId = None
        self._Status = None
        self._StartTime = None
        self._EndTime = None
        self._RealStartTime = None
        self._RealEndTime = None
        self._Resolution = None
        self._MaxRTCMember = None
        self._ReplayUrl = None
        self._RecordUrl = None
        self._MaxMicNumber = None
        self._EnableDirectControl = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def RealStartTime(self):
        return self._RealStartTime

    @RealStartTime.setter
    def RealStartTime(self, RealStartTime):
        self._RealStartTime = RealStartTime

    @property
    def RealEndTime(self):
        return self._RealEndTime

    @RealEndTime.setter
    def RealEndTime(self, RealEndTime):
        self._RealEndTime = RealEndTime

    @property
    def Resolution(self):
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def MaxRTCMember(self):
        return self._MaxRTCMember

    @MaxRTCMember.setter
    def MaxRTCMember(self, MaxRTCMember):
        self._MaxRTCMember = MaxRTCMember

    @property
    def ReplayUrl(self):
        return self._ReplayUrl

    @ReplayUrl.setter
    def ReplayUrl(self, ReplayUrl):
        self._ReplayUrl = ReplayUrl

    @property
    def RecordUrl(self):
        return self._RecordUrl

    @RecordUrl.setter
    def RecordUrl(self, RecordUrl):
        self._RecordUrl = RecordUrl

    @property
    def MaxMicNumber(self):
        return self._MaxMicNumber

    @MaxMicNumber.setter
    def MaxMicNumber(self, MaxMicNumber):
        self._MaxMicNumber = MaxMicNumber

    @property
    def EnableDirectControl(self):
        return self._EnableDirectControl

    @EnableDirectControl.setter
    def EnableDirectControl(self, EnableDirectControl):
        self._EnableDirectControl = EnableDirectControl


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._RoomId = params.get("RoomId")
        self._Status = params.get("Status")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._RealStartTime = params.get("RealStartTime")
        self._RealEndTime = params.get("RealEndTime")
        self._Resolution = params.get("Resolution")
        self._MaxRTCMember = params.get("MaxRTCMember")
        self._ReplayUrl = params.get("ReplayUrl")
        self._RecordUrl = params.get("RecordUrl")
        self._MaxMicNumber = params.get("MaxMicNumber")
        self._EnableDirectControl = params.get("EnableDirectControl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetAppCustomContentRequest(AbstractModel):
    """SetAppCustomContent request structure.

    """

    def __init__(self):
        r"""
        :param _CustomContent: Custom content
        :type CustomContent: list of AppCustomContent
        :param _SdkAppId: Application ID
        :type SdkAppId: int
        """
        self._CustomContent = None
        self._SdkAppId = None

    @property
    def CustomContent(self):
        return self._CustomContent

    @CustomContent.setter
    def CustomContent(self, CustomContent):
        self._CustomContent = CustomContent

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId


    def _deserialize(self, params):
        if params.get("CustomContent") is not None:
            self._CustomContent = []
            for item in params.get("CustomContent"):
                obj = AppCustomContent()
                obj._deserialize(item)
                self._CustomContent.append(obj)
        self._SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetAppCustomContentResponse(AbstractModel):
    """SetAppCustomContent response structure.

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


class SetWatermarkRequest(AbstractModel):
    """SetWatermark request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: The SDKAppID assigned by LCIC.
        :type SdkAppId: int
        :param _TeacherUrl: The URL of the watermark for the teacher’s video. If you pass in an empty string, the teacher’s video will not have a watermark.
        :type TeacherUrl: str
        :param _BoardUrl: The URL of the watermark for the whiteboard. If you pass in an empty string, the whiteboard video will not have a watermark.
        :type BoardUrl: str
        :param _VideoUrl: The image displayed when there is no video. If you pass in an empty string, no images will be displayed.
        :type VideoUrl: str
        :param _BoardW: The width of the whiteboard’s watermark, which is expressed as a percentage of the video width. The value range is 0-100, and the default value is 0.
        :type BoardW: float
        :param _BoardH: The height of the whiteboard’s watermark, which is expressed as a percentage of the video height. The value range is 0-100, and the default value is 0.
        :type BoardH: float
        :param _BoardX: The horizontal offset of the whiteboard’s watermark, which is expressed as a percentage of the video width. For example, 50 indicates that the watermark will appear in the middle horizontally. Value range: 0-100.
        :type BoardX: float
        :param _BoardY: The vertical offset of the whiteboard’s watermark, which is expressed as a percentage of the video width. For example, 50 indicates that the watermark will appear in the middle vertically. Value range: 0-100.
        :type BoardY: float
        :param _TeacherW: The width of the watermark for the teacher’s video, which is expressed as a percentage of the video width. The value range is 0-100, and the default value is 0.
        :type TeacherW: float
        :param _TeacherH: The height of the watermark for the teacher’s video, which is expressed as a percentage of the video height. The value range is 0-100, and the default value is 0.
        :type TeacherH: float
        :param _TeacherX: The horizontal offset of the watermark for the teacher’s video, which is expressed as a percentage of the video width. For example, 50 indicates that the watermark will appear in the middle horizontally. Value range: 0-100.
        :type TeacherX: float
        :param _TeacherY: The vertical offset of the watermark for the teacher’s video, which is expressed as a percentage of the video width. For example, 50 indicates that the watermark will appear in the middle vertically. Value range: 0-100.
        :type TeacherY: float
        :param _Text: The watermark text. If you pass in an empty string, there will be no text.
        :type Text: str
        :param _TextColor: The watermark text color.
        :type TextColor: str
        """
        self._SdkAppId = None
        self._TeacherUrl = None
        self._BoardUrl = None
        self._VideoUrl = None
        self._BoardW = None
        self._BoardH = None
        self._BoardX = None
        self._BoardY = None
        self._TeacherW = None
        self._TeacherH = None
        self._TeacherX = None
        self._TeacherY = None
        self._Text = None
        self._TextColor = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TeacherUrl(self):
        return self._TeacherUrl

    @TeacherUrl.setter
    def TeacherUrl(self, TeacherUrl):
        self._TeacherUrl = TeacherUrl

    @property
    def BoardUrl(self):
        return self._BoardUrl

    @BoardUrl.setter
    def BoardUrl(self, BoardUrl):
        self._BoardUrl = BoardUrl

    @property
    def VideoUrl(self):
        return self._VideoUrl

    @VideoUrl.setter
    def VideoUrl(self, VideoUrl):
        self._VideoUrl = VideoUrl

    @property
    def BoardW(self):
        return self._BoardW

    @BoardW.setter
    def BoardW(self, BoardW):
        self._BoardW = BoardW

    @property
    def BoardH(self):
        return self._BoardH

    @BoardH.setter
    def BoardH(self, BoardH):
        self._BoardH = BoardH

    @property
    def BoardX(self):
        return self._BoardX

    @BoardX.setter
    def BoardX(self, BoardX):
        self._BoardX = BoardX

    @property
    def BoardY(self):
        return self._BoardY

    @BoardY.setter
    def BoardY(self, BoardY):
        self._BoardY = BoardY

    @property
    def TeacherW(self):
        return self._TeacherW

    @TeacherW.setter
    def TeacherW(self, TeacherW):
        self._TeacherW = TeacherW

    @property
    def TeacherH(self):
        return self._TeacherH

    @TeacherH.setter
    def TeacherH(self, TeacherH):
        self._TeacherH = TeacherH

    @property
    def TeacherX(self):
        return self._TeacherX

    @TeacherX.setter
    def TeacherX(self, TeacherX):
        self._TeacherX = TeacherX

    @property
    def TeacherY(self):
        return self._TeacherY

    @TeacherY.setter
    def TeacherY(self, TeacherY):
        self._TeacherY = TeacherY

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def TextColor(self):
        return self._TextColor

    @TextColor.setter
    def TextColor(self, TextColor):
        self._TextColor = TextColor


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TeacherUrl = params.get("TeacherUrl")
        self._BoardUrl = params.get("BoardUrl")
        self._VideoUrl = params.get("VideoUrl")
        self._BoardW = params.get("BoardW")
        self._BoardH = params.get("BoardH")
        self._BoardX = params.get("BoardX")
        self._BoardY = params.get("BoardY")
        self._TeacherW = params.get("TeacherW")
        self._TeacherH = params.get("TeacherH")
        self._TeacherX = params.get("TeacherX")
        self._TeacherY = params.get("TeacherY")
        self._Text = params.get("Text")
        self._TextColor = params.get("TextColor")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetWatermarkResponse(AbstractModel):
    """SetWatermark response structure.

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


class StartRoomRequest(AbstractModel):
    """StartRoom request structure.

    """

    def __init__(self):
        r"""
        :param _RoomId: The room ID.
        :type RoomId: int
        """
        self._RoomId = None

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId


    def _deserialize(self, params):
        self._RoomId = params.get("RoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartRoomResponse(AbstractModel):
    """StartRoom response structure.

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


class TextMarkConfig(AbstractModel):
    """The watermark text.
    Used by actions: GetWatermark.

    """

    def __init__(self):
        r"""
        :param _Text: The watermark text. Note: This field may return null, indicating that no valid values can be obtained.
        :type Text: str
        :param _Color: The watermark text color. Note: This field may return null, indicating that no valid values can be obtained.
        :type Color: str
        """
        self._Text = None
        self._Color = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Color(self):
        return self._Color

    @Color.setter
    def Color(self, Color):
        self._Color = Color


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._Color = params.get("Color")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindDocumentFromRoomRequest(AbstractModel):
    """UnbindDocumentFromRoom request structure.

    """

    def __init__(self):
        r"""
        :param _RoomId: Room ID	
        :type RoomId: int
        :param _DocumentId: Document ID	
        :type DocumentId: str
        """
        self._RoomId = None
        self._DocumentId = None

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def DocumentId(self):
        return self._DocumentId

    @DocumentId.setter
    def DocumentId(self, DocumentId):
        self._DocumentId = DocumentId


    def _deserialize(self, params):
        self._RoomId = params.get("RoomId")
        self._DocumentId = params.get("DocumentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindDocumentFromRoomResponse(AbstractModel):
    """UnbindDocumentFromRoom response structure.

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


class UserInfo(AbstractModel):
    """The user information.
    Used by actions: DescribeSdkAppIdUsers.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 
Note: This field may return null, indicating that no valid values can be obtained.
        :type SdkAppId: int
        :param _UserId: 
Note: This field may return null, indicating that no valid values can be obtained.
        :type UserId: str
        :param _Name: 
Note: This field may return null, indicating that no valid values can be obtained.
        :type Name: str
        :param _Avatar: 
Note: This field may return null, indicating that no valid values can be obtained.
        :type Avatar: str
        """
        self._SdkAppId = None
        self._UserId = None
        self._Name = None
        self._Avatar = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Avatar(self):
        return self._Avatar

    @Avatar.setter
    def Avatar(self, Avatar):
        self._Avatar = Avatar


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._UserId = params.get("UserId")
        self._Name = params.get("Name")
        self._Avatar = params.get("Avatar")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WatermarkConfig(AbstractModel):
    """Watermark settings.
    Used by actions: GetWatermark.

    """

    def __init__(self):
        r"""
        :param _Url: The URL of the watermark image. Note: This field may return null, indicating that no valid values can be obtained.
        :type Url: str
        :param _Width: The watermark width, which is expressed as a percentage of the video width. Note: This field may return null, indicating that no valid values can be obtained.
        :type Width: float
        :param _Height: The watermark height, which is expressed as a percentage of the video height. Note: This field may return null, indicating that no valid values can be obtained.
        :type Height: float
        :param _LocationX: The horizontal offset of the watermark, which is expressed as a percentage of the video width. For example, 50 indicates that the watermark will appear in the middle horizontally. Value range: 0-100. Note: This field may return null, indicating that no valid values can be obtained.
        :type LocationX: float
        :param _LocationY: The vertical offset of the watermark, which is expressed as a percentage of the video width. For example, 50 indicates that the watermark will appear in the middle vertically. Value range: 0-100. Note: This field may return null, indicating that no valid values can be obtained.
        :type LocationY: float
        """
        self._Url = None
        self._Width = None
        self._Height = None
        self._LocationX = None
        self._LocationY = None

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Width(self):
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def LocationX(self):
        return self._LocationX

    @LocationX.setter
    def LocationX(self, LocationX):
        self._LocationX = LocationX

    @property
    def LocationY(self):
        return self._LocationY

    @LocationY.setter
    def LocationY(self, LocationY):
        self._LocationY = LocationY


    def _deserialize(self, params):
        self._Url = params.get("Url")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._LocationX = params.get("LocationX")
        self._LocationY = params.get("LocationY")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        