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


class ApplyInstanceSnapshotRequest(AbstractModel):
    """ApplyInstanceSnapshot request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _SnapshotId: Snapshot ID.
        :type SnapshotId: str
        """
        self._InstanceId = None
        self._SnapshotId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SnapshotId(self):
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SnapshotId = params.get("SnapshotId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyInstanceSnapshotResponse(AbstractModel):
    """ApplyInstanceSnapshot response structure.

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


class AssociateInstancesKeyPairsRequest(AbstractModel):
    """AssociateInstancesKeyPairs request structure.

    """

    def __init__(self):
        r"""
        :param _KeyIds: Key pair ID list. Each request can contain up to 100 key pairs.
        :type KeyIds: list of str
        :param _InstanceIds: Instance ID list. Each request can contain up to 100 instances at a time. You can get an instance ID from the `InstanceId` returned by the [DescribeInstances](https://intl.cloud.tencent.com/document/api/1207/47573?from_cn_redirect=1) API.
        :type InstanceIds: list of str
        """
        self._KeyIds = None
        self._InstanceIds = None

    @property
    def KeyIds(self):
        return self._KeyIds

    @KeyIds.setter
    def KeyIds(self, KeyIds):
        self._KeyIds = KeyIds

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._KeyIds = params.get("KeyIds")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateInstancesKeyPairsResponse(AbstractModel):
    """AssociateInstancesKeyPairs response structure.

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


class AttachCcnRequest(AbstractModel):
    """AttachCcn request structure.

    """

    def __init__(self):
        r"""
        :param _CcnId: CCN instance ID.
        :type CcnId: str
        """
        self._CcnId = None

    @property
    def CcnId(self):
        return self._CcnId

    @CcnId.setter
    def CcnId(self, CcnId):
        self._CcnId = CcnId


    def _deserialize(self, params):
        self._CcnId = params.get("CcnId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachCcnResponse(AbstractModel):
    """AttachCcn response structure.

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


class AttachDetail(AbstractModel):
    """Attachment information

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _AttachedDiskCount: Number of elastic cloud disks attached to the instance
        :type AttachedDiskCount: int
        :param _MaxAttachCount: Upper limit of attached elastic cloud disks
        :type MaxAttachCount: int
        """
        self._InstanceId = None
        self._AttachedDiskCount = None
        self._MaxAttachCount = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AttachedDiskCount(self):
        return self._AttachedDiskCount

    @AttachedDiskCount.setter
    def AttachedDiskCount(self, AttachedDiskCount):
        self._AttachedDiskCount = AttachedDiskCount

    @property
    def MaxAttachCount(self):
        return self._MaxAttachCount

    @MaxAttachCount.setter
    def MaxAttachCount(self, MaxAttachCount):
        self._MaxAttachCount = MaxAttachCount


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AttachedDiskCount = params.get("AttachedDiskCount")
        self._MaxAttachCount = params.get("MaxAttachCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachDisksRequest(AbstractModel):
    """AttachDisks request structure.

    """

    def __init__(self):
        r"""
        :param _DiskIds: List of cloud disk IDs.
        :type DiskIds: list of str
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _RenewFlag: Whether Auto-Renewal is enabled 
        :type RenewFlag: str
        """
        self._DiskIds = None
        self._InstanceId = None
        self._RenewFlag = None

    @property
    def DiskIds(self):
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag


    def _deserialize(self, params):
        self._DiskIds = params.get("DiskIds")
        self._InstanceId = params.get("InstanceId")
        self._RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachDisksResponse(AbstractModel):
    """AttachDisks response structure.

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


class Blueprint(AbstractModel):
    """Image information.

    """

    def __init__(self):
        r"""
        :param _BlueprintId: Image ID, which is the unique identifier of `Blueprint`.
        :type BlueprintId: str
        :param _DisplayTitle: Image title to be displayed.
        :type DisplayTitle: str
        :param _DisplayVersion: Image version to be displayed.
        :type DisplayVersion: str
        :param _Description: Image description information.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Description: str
        :param _OsName: OS name.
        :type OsName: str
        :param _Platform: OS type.
        :type Platform: str
        :param _PlatformType: OS type, such as LINUX_UNIX and WINDOWS.
        :type PlatformType: str
        :param _BlueprintType: Image type, such as APP_OS, PURE_OS, and PRIVATE.
        :type BlueprintType: str
        :param _ImageUrl: Image picture URL.
        :type ImageUrl: str
        :param _RequiredSystemDiskSize: System disk size required by image in GB.
        :type RequiredSystemDiskSize: int
        :param _BlueprintState: Image status.
        :type BlueprintState: str
        :param _CreatedTime: Creation time according to ISO 8601 standard. UTC time is used. 
Format: YYYY-MM-DDThh:mm:ssZ.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreatedTime: str
        :param _BlueprintName: Image name.
        :type BlueprintName: str
        :param _SupportAutomationTools: Whether the image supports automation tools.
        :type SupportAutomationTools: bool
        :param _RequiredMemorySize: Memory size required by image in GB.
        :type RequiredMemorySize: int
        :param _ImageId: ID of the Lighthouse image shared from a CVM image
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ImageId: str
        :param _CommunityUrl: URL of official website of the open-source project
        :type CommunityUrl: str
        :param _GuideUrl: Guide documentation URL
        :type GuideUrl: str
        :param _SceneIdSet: Array of IDs of scenes associated with an image
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type SceneIdSet: list of str
        :param _DockerVersion: Docker version.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type DockerVersion: str
        """
        self._BlueprintId = None
        self._DisplayTitle = None
        self._DisplayVersion = None
        self._Description = None
        self._OsName = None
        self._Platform = None
        self._PlatformType = None
        self._BlueprintType = None
        self._ImageUrl = None
        self._RequiredSystemDiskSize = None
        self._BlueprintState = None
        self._CreatedTime = None
        self._BlueprintName = None
        self._SupportAutomationTools = None
        self._RequiredMemorySize = None
        self._ImageId = None
        self._CommunityUrl = None
        self._GuideUrl = None
        self._SceneIdSet = None
        self._DockerVersion = None

    @property
    def BlueprintId(self):
        return self._BlueprintId

    @BlueprintId.setter
    def BlueprintId(self, BlueprintId):
        self._BlueprintId = BlueprintId

    @property
    def DisplayTitle(self):
        return self._DisplayTitle

    @DisplayTitle.setter
    def DisplayTitle(self, DisplayTitle):
        self._DisplayTitle = DisplayTitle

    @property
    def DisplayVersion(self):
        return self._DisplayVersion

    @DisplayVersion.setter
    def DisplayVersion(self, DisplayVersion):
        self._DisplayVersion = DisplayVersion

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def OsName(self):
        return self._OsName

    @OsName.setter
    def OsName(self, OsName):
        self._OsName = OsName

    @property
    def Platform(self):
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def PlatformType(self):
        return self._PlatformType

    @PlatformType.setter
    def PlatformType(self, PlatformType):
        self._PlatformType = PlatformType

    @property
    def BlueprintType(self):
        return self._BlueprintType

    @BlueprintType.setter
    def BlueprintType(self, BlueprintType):
        self._BlueprintType = BlueprintType

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def RequiredSystemDiskSize(self):
        return self._RequiredSystemDiskSize

    @RequiredSystemDiskSize.setter
    def RequiredSystemDiskSize(self, RequiredSystemDiskSize):
        self._RequiredSystemDiskSize = RequiredSystemDiskSize

    @property
    def BlueprintState(self):
        return self._BlueprintState

    @BlueprintState.setter
    def BlueprintState(self, BlueprintState):
        self._BlueprintState = BlueprintState

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def BlueprintName(self):
        return self._BlueprintName

    @BlueprintName.setter
    def BlueprintName(self, BlueprintName):
        self._BlueprintName = BlueprintName

    @property
    def SupportAutomationTools(self):
        return self._SupportAutomationTools

    @SupportAutomationTools.setter
    def SupportAutomationTools(self, SupportAutomationTools):
        self._SupportAutomationTools = SupportAutomationTools

    @property
    def RequiredMemorySize(self):
        return self._RequiredMemorySize

    @RequiredMemorySize.setter
    def RequiredMemorySize(self, RequiredMemorySize):
        self._RequiredMemorySize = RequiredMemorySize

    @property
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def CommunityUrl(self):
        return self._CommunityUrl

    @CommunityUrl.setter
    def CommunityUrl(self, CommunityUrl):
        self._CommunityUrl = CommunityUrl

    @property
    def GuideUrl(self):
        return self._GuideUrl

    @GuideUrl.setter
    def GuideUrl(self, GuideUrl):
        self._GuideUrl = GuideUrl

    @property
    def SceneIdSet(self):
        return self._SceneIdSet

    @SceneIdSet.setter
    def SceneIdSet(self, SceneIdSet):
        self._SceneIdSet = SceneIdSet

    @property
    def DockerVersion(self):
        return self._DockerVersion

    @DockerVersion.setter
    def DockerVersion(self, DockerVersion):
        self._DockerVersion = DockerVersion


    def _deserialize(self, params):
        self._BlueprintId = params.get("BlueprintId")
        self._DisplayTitle = params.get("DisplayTitle")
        self._DisplayVersion = params.get("DisplayVersion")
        self._Description = params.get("Description")
        self._OsName = params.get("OsName")
        self._Platform = params.get("Platform")
        self._PlatformType = params.get("PlatformType")
        self._BlueprintType = params.get("BlueprintType")
        self._ImageUrl = params.get("ImageUrl")
        self._RequiredSystemDiskSize = params.get("RequiredSystemDiskSize")
        self._BlueprintState = params.get("BlueprintState")
        self._CreatedTime = params.get("CreatedTime")
        self._BlueprintName = params.get("BlueprintName")
        self._SupportAutomationTools = params.get("SupportAutomationTools")
        self._RequiredMemorySize = params.get("RequiredMemorySize")
        self._ImageId = params.get("ImageId")
        self._CommunityUrl = params.get("CommunityUrl")
        self._GuideUrl = params.get("GuideUrl")
        self._SceneIdSet = params.get("SceneIdSet")
        self._DockerVersion = params.get("DockerVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BlueprintInstance(AbstractModel):
    """Image instance information.

    """

    def __init__(self):
        r"""
        :param _Blueprint: Image information.
        :type Blueprint: :class:`tencentcloud.lighthouse.v20200324.models.Blueprint`
        :param _SoftwareSet: Software list.
        :type SoftwareSet: list of Software
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        """
        self._Blueprint = None
        self._SoftwareSet = None
        self._InstanceId = None

    @property
    def Blueprint(self):
        return self._Blueprint

    @Blueprint.setter
    def Blueprint(self, Blueprint):
        self._Blueprint = Blueprint

    @property
    def SoftwareSet(self):
        return self._SoftwareSet

    @SoftwareSet.setter
    def SoftwareSet(self, SoftwareSet):
        self._SoftwareSet = SoftwareSet

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        if params.get("Blueprint") is not None:
            self._Blueprint = Blueprint()
            self._Blueprint._deserialize(params.get("Blueprint"))
        if params.get("SoftwareSet") is not None:
            self._SoftwareSet = []
            for item in params.get("SoftwareSet"):
                obj = Software()
                obj._deserialize(item)
                self._SoftwareSet.append(obj)
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BlueprintPrice(AbstractModel):
    """BlueprintPrice	Custom image price parameter.

    """

    def __init__(self):
        r"""
        :param _OriginalBlueprintPrice: Original image unit price in USD.
        :type OriginalBlueprintPrice: float
        :param _OriginalPrice: Original image total price in USD.
        :type OriginalPrice: float
        :param _Discount: Discount.
        :type Discount: int
        :param _DiscountPrice: Discounted image total price in USD.
        :type DiscountPrice: float
        """
        self._OriginalBlueprintPrice = None
        self._OriginalPrice = None
        self._Discount = None
        self._DiscountPrice = None

    @property
    def OriginalBlueprintPrice(self):
        return self._OriginalBlueprintPrice

    @OriginalBlueprintPrice.setter
    def OriginalBlueprintPrice(self, OriginalBlueprintPrice):
        self._OriginalBlueprintPrice = OriginalBlueprintPrice

    @property
    def OriginalPrice(self):
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def Discount(self):
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount

    @property
    def DiscountPrice(self):
        return self._DiscountPrice

    @DiscountPrice.setter
    def DiscountPrice(self, DiscountPrice):
        self._DiscountPrice = DiscountPrice


    def _deserialize(self, params):
        self._OriginalBlueprintPrice = params.get("OriginalBlueprintPrice")
        self._OriginalPrice = params.get("OriginalPrice")
        self._Discount = params.get("Discount")
        self._DiscountPrice = params.get("DiscountPrice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Bundle(AbstractModel):
    """Package information.

    """

    def __init__(self):
        r"""
        :param _BundleId: Package ID.
        :type BundleId: str
        :param _Memory: Memory size in GB.
        :type Memory: int
        :param _SystemDiskType: System disk type.
Valid values: 
<li> LOCAL_BASIC: local disk</li><li> LOCAL_SSD: local SSD disk</li><li> CLOUD_BASIC: HDD cloud disk</li><li> CLOUD_SSD: SSD cloud disk</li><li> CLOUD_PREMIUM: Premium Cloud Storage</li>
        :type SystemDiskType: str
        :param _SystemDiskSize: System disk size.
        :type SystemDiskSize: int
        :param _MonthlyTraffic: Monthly network traffic in Gb.
        :type MonthlyTraffic: int
        :param _SupportLinuxUnixPlatform: Whether Linux/Unix is supported.
        :type SupportLinuxUnixPlatform: bool
        :param _SupportWindowsPlatform: Whether Windows is supported.
        :type SupportWindowsPlatform: bool
        :param _Price: Current package unit price information.
        :type Price: :class:`tencentcloud.lighthouse.v20200324.models.Price`
        :param _CPU: Number of CPU cores.
        :type CPU: int
        :param _InternetMaxBandwidthOut: Peak bandwidth in Mbps.
        :type InternetMaxBandwidthOut: int
        :param _InternetChargeType: Network billing mode.
        :type InternetChargeType: str
        :param _BundleSalesState: Package sale status. Valid values: AVAILABLE, SOLD_OUT
        :type BundleSalesState: str
        :param _BundleType: Bundle type. 
Valid values: 
<li>STARTER_BUNDLE: Starter bundle</li>
<li>GENERAL_BUNDLE: General bundle</li>
<li>ENTERPRISE_BUNDLE: Enterprise bundle</li>
<li>STORAGE_BUNDLE: Storage-optimized bundle</li>
<li>EXCLUSIVE_BUNDLE: Dedicated bundle</li>
<li>HK_EXCLUSIVE_BUNDLE: Hong Kong-dedicated bundle </li>
<li>CAREFREE_BUNDLE: Lighthouse Care bundle</li>
<li>BEFAST_BUNDLE: BeFast bundle </li>
        :type BundleType: str
        :param _BundleTypeDescription: Bundle type description 
Note: This parameter may return null, indicating that no valid values can be obtained.
        :type BundleTypeDescription: str
        :param _BundleDisplayLabel: Package tag.
Valid values:
"ACTIVITY": promotional package
"NORMAL": regular package
"CAREFREE": carefree package
        :type BundleDisplayLabel: str
        """
        self._BundleId = None
        self._Memory = None
        self._SystemDiskType = None
        self._SystemDiskSize = None
        self._MonthlyTraffic = None
        self._SupportLinuxUnixPlatform = None
        self._SupportWindowsPlatform = None
        self._Price = None
        self._CPU = None
        self._InternetMaxBandwidthOut = None
        self._InternetChargeType = None
        self._BundleSalesState = None
        self._BundleType = None
        self._BundleTypeDescription = None
        self._BundleDisplayLabel = None

    @property
    def BundleId(self):
        return self._BundleId

    @BundleId.setter
    def BundleId(self, BundleId):
        self._BundleId = BundleId

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def SystemDiskType(self):
        return self._SystemDiskType

    @SystemDiskType.setter
    def SystemDiskType(self, SystemDiskType):
        self._SystemDiskType = SystemDiskType

    @property
    def SystemDiskSize(self):
        return self._SystemDiskSize

    @SystemDiskSize.setter
    def SystemDiskSize(self, SystemDiskSize):
        self._SystemDiskSize = SystemDiskSize

    @property
    def MonthlyTraffic(self):
        return self._MonthlyTraffic

    @MonthlyTraffic.setter
    def MonthlyTraffic(self, MonthlyTraffic):
        self._MonthlyTraffic = MonthlyTraffic

    @property
    def SupportLinuxUnixPlatform(self):
        return self._SupportLinuxUnixPlatform

    @SupportLinuxUnixPlatform.setter
    def SupportLinuxUnixPlatform(self, SupportLinuxUnixPlatform):
        self._SupportLinuxUnixPlatform = SupportLinuxUnixPlatform

    @property
    def SupportWindowsPlatform(self):
        return self._SupportWindowsPlatform

    @SupportWindowsPlatform.setter
    def SupportWindowsPlatform(self, SupportWindowsPlatform):
        self._SupportWindowsPlatform = SupportWindowsPlatform

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def CPU(self):
        return self._CPU

    @CPU.setter
    def CPU(self, CPU):
        self._CPU = CPU

    @property
    def InternetMaxBandwidthOut(self):
        return self._InternetMaxBandwidthOut

    @InternetMaxBandwidthOut.setter
    def InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):
        self._InternetMaxBandwidthOut = InternetMaxBandwidthOut

    @property
    def InternetChargeType(self):
        return self._InternetChargeType

    @InternetChargeType.setter
    def InternetChargeType(self, InternetChargeType):
        self._InternetChargeType = InternetChargeType

    @property
    def BundleSalesState(self):
        return self._BundleSalesState

    @BundleSalesState.setter
    def BundleSalesState(self, BundleSalesState):
        self._BundleSalesState = BundleSalesState

    @property
    def BundleType(self):
        return self._BundleType

    @BundleType.setter
    def BundleType(self, BundleType):
        self._BundleType = BundleType

    @property
    def BundleTypeDescription(self):
        return self._BundleTypeDescription

    @BundleTypeDescription.setter
    def BundleTypeDescription(self, BundleTypeDescription):
        self._BundleTypeDescription = BundleTypeDescription

    @property
    def BundleDisplayLabel(self):
        return self._BundleDisplayLabel

    @BundleDisplayLabel.setter
    def BundleDisplayLabel(self, BundleDisplayLabel):
        self._BundleDisplayLabel = BundleDisplayLabel


    def _deserialize(self, params):
        self._BundleId = params.get("BundleId")
        self._Memory = params.get("Memory")
        self._SystemDiskType = params.get("SystemDiskType")
        self._SystemDiskSize = params.get("SystemDiskSize")
        self._MonthlyTraffic = params.get("MonthlyTraffic")
        self._SupportLinuxUnixPlatform = params.get("SupportLinuxUnixPlatform")
        self._SupportWindowsPlatform = params.get("SupportWindowsPlatform")
        if params.get("Price") is not None:
            self._Price = Price()
            self._Price._deserialize(params.get("Price"))
        self._CPU = params.get("CPU")
        self._InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self._InternetChargeType = params.get("InternetChargeType")
        self._BundleSalesState = params.get("BundleSalesState")
        self._BundleType = params.get("BundleType")
        self._BundleTypeDescription = params.get("BundleTypeDescription")
        self._BundleDisplayLabel = params.get("BundleDisplayLabel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CcnAttachedInstance(AbstractModel):
    """List of instances associated with the CCN instance.

    """

    def __init__(self):
        r"""
        :param _CcnId: CCN instance ID.
        :type CcnId: str
        :param _CidrBlock: CIDR block of associated instance.
        :type CidrBlock: list of str
        :param _State: Associated instance status:

•  PENDING: applying
•  ACTIVE: connected
•  EXPIRED: expired
•  REJECTED: rejected
•  DELETED: deleted
•  FAILED: failed (it will be asynchronously unassociated after 2 hours)
•  ATTACHING: associating
•  DETACHING: unassociating
•  DETACHFAILED: failed to unassociate (it will be asynchronously unassociated after 2 hours)
        :type State: str
        :param _AttachedTime: Association time.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AttachedTime: str
        :param _Description: Remarks
        :type Description: str
        """
        self._CcnId = None
        self._CidrBlock = None
        self._State = None
        self._AttachedTime = None
        self._Description = None

    @property
    def CcnId(self):
        return self._CcnId

    @CcnId.setter
    def CcnId(self, CcnId):
        self._CcnId = CcnId

    @property
    def CidrBlock(self):
        return self._CidrBlock

    @CidrBlock.setter
    def CidrBlock(self, CidrBlock):
        self._CidrBlock = CidrBlock

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def AttachedTime(self):
        return self._AttachedTime

    @AttachedTime.setter
    def AttachedTime(self, AttachedTime):
        self._AttachedTime = AttachedTime

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._CcnId = params.get("CcnId")
        self._CidrBlock = params.get("CidrBlock")
        self._State = params.get("State")
        self._AttachedTime = params.get("AttachedTime")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContainerEnv(AbstractModel):
    """Container environment variable

    """

    def __init__(self):
        r"""
        :param _Key: Environment variable key
        :type Key: str
        :param _Value: Environment variable value
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBlueprintRequest(AbstractModel):
    """CreateBlueprint request structure.

    """

    def __init__(self):
        r"""
        :param _BlueprintName: Image name, which can contain up to 60 characters.
        :type BlueprintName: str
        :param _Description: Image description, which can contain up to 60 characters.
        :type Description: str
        :param _InstanceId: ID of the instance for which to make an image.
        :type InstanceId: str
        :param _ForcePowerOff: Whether to forcibly shut down the instance before creating the image 
Valid values: 
`True`: Shut down and instance first 
`False`: Create the image when the instance is running 
Default: `True` 
Note that if you create an image when the instance is running, there might be data loss.
        :type ForcePowerOff: bool
        """
        self._BlueprintName = None
        self._Description = None
        self._InstanceId = None
        self._ForcePowerOff = None

    @property
    def BlueprintName(self):
        return self._BlueprintName

    @BlueprintName.setter
    def BlueprintName(self, BlueprintName):
        self._BlueprintName = BlueprintName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ForcePowerOff(self):
        return self._ForcePowerOff

    @ForcePowerOff.setter
    def ForcePowerOff(self, ForcePowerOff):
        self._ForcePowerOff = ForcePowerOff


    def _deserialize(self, params):
        self._BlueprintName = params.get("BlueprintName")
        self._Description = params.get("Description")
        self._InstanceId = params.get("InstanceId")
        self._ForcePowerOff = params.get("ForcePowerOff")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBlueprintResponse(AbstractModel):
    """CreateBlueprint response structure.

    """

    def __init__(self):
        r"""
        :param _BlueprintId: Custom image ID.
        :type BlueprintId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BlueprintId = None
        self._RequestId = None

    @property
    def BlueprintId(self):
        return self._BlueprintId

    @BlueprintId.setter
    def BlueprintId(self, BlueprintId):
        self._BlueprintId = BlueprintId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BlueprintId = params.get("BlueprintId")
        self._RequestId = params.get("RequestId")


class CreateFirewallRulesRequest(AbstractModel):
    """CreateFirewallRules request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _FirewallRules: Firewall rule list.
        :type FirewallRules: list of FirewallRule
        :param _FirewallVersion: Current firewall version number. Every time you update the firewall rule version, it will be automatically increased by 1 to prevent the rule from expiring. If it is left empty, conflicts will not be considered.
        :type FirewallVersion: int
        """
        self._InstanceId = None
        self._FirewallRules = None
        self._FirewallVersion = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def FirewallRules(self):
        return self._FirewallRules

    @FirewallRules.setter
    def FirewallRules(self, FirewallRules):
        self._FirewallRules = FirewallRules

    @property
    def FirewallVersion(self):
        return self._FirewallVersion

    @FirewallVersion.setter
    def FirewallVersion(self, FirewallVersion):
        self._FirewallVersion = FirewallVersion


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("FirewallRules") is not None:
            self._FirewallRules = []
            for item in params.get("FirewallRules"):
                obj = FirewallRule()
                obj._deserialize(item)
                self._FirewallRules.append(obj)
        self._FirewallVersion = params.get("FirewallVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFirewallRulesResponse(AbstractModel):
    """CreateFirewallRules response structure.

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


class CreateInstanceSnapshotRequest(AbstractModel):
    """CreateInstanceSnapshot request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ID of the instance for which to create a snapshot.
        :type InstanceId: str
        :param _SnapshotName: Snapshot name, which can contain up to 60 characters.
        :type SnapshotName: str
        """
        self._InstanceId = None
        self._SnapshotName = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SnapshotName(self):
        return self._SnapshotName

    @SnapshotName.setter
    def SnapshotName(self, SnapshotName):
        self._SnapshotName = SnapshotName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SnapshotName = params.get("SnapshotName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstanceSnapshotResponse(AbstractModel):
    """CreateInstanceSnapshot response structure.

    """

    def __init__(self):
        r"""
        :param _SnapshotId: Snapshot ID.
        :type SnapshotId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SnapshotId = None
        self._RequestId = None

    @property
    def SnapshotId(self):
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SnapshotId = params.get("SnapshotId")
        self._RequestId = params.get("RequestId")


class CreateInstancesRequest(AbstractModel):
    """CreateInstances request structure.

    """

    def __init__(self):
        r"""
        :param _BundleId: Bundle ID. You can get it via the [DescribeBundles](https://intl.cloud.tencent.com/document/api/1207/47575?from_cn_redirect=1) API.
        :type BundleId: str
        :param _BlueprintId: Image ID. You can get it via the [DescribeBlueprints](https://intl.cloud.tencent.com/document/api/1207/47689?from_cn_redirect=1) API.
        :type BlueprintId: str
        :param _InstanceChargePrepaid: Monthly subscription information for the instance, including the purchase period, setting of auto-renewal, etc.
        :type InstanceChargePrepaid: :class:`tencentcloud.lighthouse.v20200324.models.InstanceChargePrepaid`
        :param _InstanceName: Instance display name.
        :type InstanceName: str
        :param _InstanceCount: Number of the instances to purchase. For monthly subscribed instances, the value can be 1 to 30. The default value is `1`. Note that this number can not exceed the remaining quota under the current account.
        :type InstanceCount: int
        :param _Zones: List of availability zones. A random AZ is selected by default.
        :type Zones: list of str
        :param _DryRun: Whether the request is a dry run only.
`true`: dry run only. The request will not create instance(s). A dry run can check whether all the required parameters are specified, whether the request format is right, whether the request exceeds service limits, and whether the specified CVMs are available.
If the dry run fails, the corresponding error code will be returned.
If the dry run succeeds, the RequestId will be returned.
`false` (default value): send a normal request and create instance(s) if all the requirements are met.
        :type DryRun: bool
        :param _ClientToken: A unique string supplied by the client to ensure that the request is idempotent. Its maximum length is 64 ASCII characters. If this parameter is not specified, the idem-potency of the request cannot be guaranteed.
        :type ClientToken: str
        :param _LoginConfiguration: Login password of the instance. It’s only available for Windows instances. If it’s not specified, it means that the user choose to set the login password after the instance creation.
        :type LoginConfiguration: :class:`tencentcloud.lighthouse.v20200324.models.LoginConfiguration`
        :param _Containers: Configuration of the containers to create
        :type Containers: list of DockerContainerConfiguration
        :param _AutoVoucher: Whether to use the vouchers automatically. It defaults to No.
        :type AutoVoucher: bool
        """
        self._BundleId = None
        self._BlueprintId = None
        self._InstanceChargePrepaid = None
        self._InstanceName = None
        self._InstanceCount = None
        self._Zones = None
        self._DryRun = None
        self._ClientToken = None
        self._LoginConfiguration = None
        self._Containers = None
        self._AutoVoucher = None

    @property
    def BundleId(self):
        return self._BundleId

    @BundleId.setter
    def BundleId(self, BundleId):
        self._BundleId = BundleId

    @property
    def BlueprintId(self):
        return self._BlueprintId

    @BlueprintId.setter
    def BlueprintId(self, BlueprintId):
        self._BlueprintId = BlueprintId

    @property
    def InstanceChargePrepaid(self):
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceCount(self):
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def Zones(self):
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def DryRun(self):
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def LoginConfiguration(self):
        return self._LoginConfiguration

    @LoginConfiguration.setter
    def LoginConfiguration(self, LoginConfiguration):
        self._LoginConfiguration = LoginConfiguration

    @property
    def Containers(self):
        return self._Containers

    @Containers.setter
    def Containers(self, Containers):
        self._Containers = Containers

    @property
    def AutoVoucher(self):
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher


    def _deserialize(self, params):
        self._BundleId = params.get("BundleId")
        self._BlueprintId = params.get("BlueprintId")
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self._InstanceName = params.get("InstanceName")
        self._InstanceCount = params.get("InstanceCount")
        self._Zones = params.get("Zones")
        self._DryRun = params.get("DryRun")
        self._ClientToken = params.get("ClientToken")
        if params.get("LoginConfiguration") is not None:
            self._LoginConfiguration = LoginConfiguration()
            self._LoginConfiguration._deserialize(params.get("LoginConfiguration"))
        if params.get("Containers") is not None:
            self._Containers = []
            for item in params.get("Containers"):
                obj = DockerContainerConfiguration()
                obj._deserialize(item)
                self._Containers.append(obj)
        self._AutoVoucher = params.get("AutoVoucher")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstancesResponse(AbstractModel):
    """CreateInstances response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIdSet: List of IDs created by using this API. The returning of IDs does not mean that the instances are created successfully.

You can call `DescribeInstances` API, and find the instance ID in the `InstancesSet` returned to check its status. If the `status` is `running`, the instance is created successfully.
        :type InstanceIdSet: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceIdSet = None
        self._RequestId = None

    @property
    def InstanceIdSet(self):
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceIdSet = params.get("InstanceIdSet")
        self._RequestId = params.get("RequestId")


class CreateKeyPairRequest(AbstractModel):
    """CreateKeyPair request structure.

    """

    def __init__(self):
        r"""
        :param _KeyName: Key pair name, which can contain up to 25 digits, letters, and underscores.
        :type KeyName: str
        """
        self._KeyName = None

    @property
    def KeyName(self):
        return self._KeyName

    @KeyName.setter
    def KeyName(self, KeyName):
        self._KeyName = KeyName


    def _deserialize(self, params):
        self._KeyName = params.get("KeyName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateKeyPairResponse(AbstractModel):
    """CreateKeyPair response structure.

    """

    def __init__(self):
        r"""
        :param _KeyPair: Key pair information.
        :type KeyPair: :class:`tencentcloud.lighthouse.v20200324.models.KeyPair`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._KeyPair = None
        self._RequestId = None

    @property
    def KeyPair(self):
        return self._KeyPair

    @KeyPair.setter
    def KeyPair(self, KeyPair):
        self._KeyPair = KeyPair

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("KeyPair") is not None:
            self._KeyPair = KeyPair()
            self._KeyPair._deserialize(params.get("KeyPair"))
        self._RequestId = params.get("RequestId")


class DataDiskPrice(AbstractModel):
    """Data disk price

    """

    def __init__(self):
        r"""
        :param _DiskId: Cloud disk ID.
        :type DiskId: str
        :param _OriginalDiskPrice: Cloud disk unit price.
        :type OriginalDiskPrice: float
        :param _OriginalPrice: Total price of cloud disk
        :type OriginalPrice: float
        :param _Discount: Discount.
        :type Discount: float
        :param _DiscountPrice: Discounted total price.
        :type DiscountPrice: float
        :param _InstanceId: ID of the instance to which the data disk is mounted.
Note: This field may return `null`, indicating that no valid value was found.
        :type InstanceId: str
        """
        self._DiskId = None
        self._OriginalDiskPrice = None
        self._OriginalPrice = None
        self._Discount = None
        self._DiscountPrice = None
        self._InstanceId = None

    @property
    def DiskId(self):
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def OriginalDiskPrice(self):
        return self._OriginalDiskPrice

    @OriginalDiskPrice.setter
    def OriginalDiskPrice(self, OriginalDiskPrice):
        self._OriginalDiskPrice = OriginalDiskPrice

    @property
    def OriginalPrice(self):
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def Discount(self):
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount

    @property
    def DiscountPrice(self):
        return self._DiscountPrice

    @DiscountPrice.setter
    def DiscountPrice(self, DiscountPrice):
        self._DiscountPrice = DiscountPrice

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._DiskId = params.get("DiskId")
        self._OriginalDiskPrice = params.get("OriginalDiskPrice")
        self._OriginalPrice = params.get("OriginalPrice")
        self._Discount = params.get("Discount")
        self._DiscountPrice = params.get("DiscountPrice")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBlueprintsRequest(AbstractModel):
    """DeleteBlueprints request structure.

    """

    def __init__(self):
        r"""
        :param _BlueprintIds: Image ID list, which can be obtained from the `BlueprintId` returned by the [DescribeBlueprints](https://intl.cloud.tencent.com/document/product/1207/47689?from_cn_redirect=1) API.
        :type BlueprintIds: list of str
        """
        self._BlueprintIds = None

    @property
    def BlueprintIds(self):
        return self._BlueprintIds

    @BlueprintIds.setter
    def BlueprintIds(self, BlueprintIds):
        self._BlueprintIds = BlueprintIds


    def _deserialize(self, params):
        self._BlueprintIds = params.get("BlueprintIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBlueprintsResponse(AbstractModel):
    """DeleteBlueprints response structure.

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


class DeleteFirewallRulesRequest(AbstractModel):
    """DeleteFirewallRules request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _FirewallRules: Firewall rule list.
        :type FirewallRules: list of FirewallRule
        :param _FirewallVersion: Current firewall version number. Every time you update the firewall rule version, it will be automatically increased by 1 to prevent the rule from expiring. If it is left empty, conflicts will not be considered.
        :type FirewallVersion: int
        """
        self._InstanceId = None
        self._FirewallRules = None
        self._FirewallVersion = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def FirewallRules(self):
        return self._FirewallRules

    @FirewallRules.setter
    def FirewallRules(self, FirewallRules):
        self._FirewallRules = FirewallRules

    @property
    def FirewallVersion(self):
        return self._FirewallVersion

    @FirewallVersion.setter
    def FirewallVersion(self, FirewallVersion):
        self._FirewallVersion = FirewallVersion


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("FirewallRules") is not None:
            self._FirewallRules = []
            for item in params.get("FirewallRules"):
                obj = FirewallRule()
                obj._deserialize(item)
                self._FirewallRules.append(obj)
        self._FirewallVersion = params.get("FirewallVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteFirewallRulesResponse(AbstractModel):
    """DeleteFirewallRules response structure.

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


class DeleteKeyPairsRequest(AbstractModel):
    """DeleteKeyPairs request structure.

    """

    def __init__(self):
        r"""
        :param _KeyIds: Key pair ID list. Each request can contain up to 10 key pairs.
        :type KeyIds: list of str
        """
        self._KeyIds = None

    @property
    def KeyIds(self):
        return self._KeyIds

    @KeyIds.setter
    def KeyIds(self, KeyIds):
        self._KeyIds = KeyIds


    def _deserialize(self, params):
        self._KeyIds = params.get("KeyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteKeyPairsResponse(AbstractModel):
    """DeleteKeyPairs response structure.

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


class DeleteSnapshotsRequest(AbstractModel):
    """DeleteSnapshots request structure.

    """

    def __init__(self):
        r"""
        :param _SnapshotIds: List of IDs of snapshots to be deleted, which can be queried through `DescribeSnapshots`.
        :type SnapshotIds: list of str
        """
        self._SnapshotIds = None

    @property
    def SnapshotIds(self):
        return self._SnapshotIds

    @SnapshotIds.setter
    def SnapshotIds(self, SnapshotIds):
        self._SnapshotIds = SnapshotIds


    def _deserialize(self, params):
        self._SnapshotIds = params.get("SnapshotIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSnapshotsResponse(AbstractModel):
    """DeleteSnapshots response structure.

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


class DeniedAction(AbstractModel):
    """Restricted operation.

    """

    def __init__(self):
        r"""
        :param _Action: Restricted operation name.
        :type Action: str
        :param _Code: Restricted operation message code.
        :type Code: str
        :param _Message: Restricted operation message.
        :type Message: str
        """
        self._Action = None
        self._Code = None
        self._Message = None

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._Action = params.get("Action")
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAllScenesRequest(AbstractModel):
    """DescribeAllScenes request structure.

    """

    def __init__(self):
        r"""
        :param _SceneIds: List of scene IDs
        :type SceneIds: list of str
        :param _Offset: Offset. Default value: 0
        :type Offset: int
        :param _Limit: Number of returned results. Default value: 20. Maximum value: 100
        :type Limit: int
        """
        self._SceneIds = None
        self._Offset = None
        self._Limit = None

    @property
    def SceneIds(self):
        return self._SceneIds

    @SceneIds.setter
    def SceneIds(self, SceneIds):
        self._SceneIds = SceneIds

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._SceneIds = params.get("SceneIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAllScenesResponse(AbstractModel):
    """DescribeAllScenes response structure.

    """

    def __init__(self):
        r"""
        :param _SceneInfoSet: List of scenes
        :type SceneInfoSet: list of SceneInfo
        :param _TotalCount: Total count of scenes
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SceneInfoSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def SceneInfoSet(self):
        return self._SceneInfoSet

    @SceneInfoSet.setter
    def SceneInfoSet(self, SceneInfoSet):
        self._SceneInfoSet = SceneInfoSet

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SceneInfoSet") is not None:
            self._SceneInfoSet = []
            for item in params.get("SceneInfoSet"):
                obj = SceneInfo()
                obj._deserialize(item)
                self._SceneInfoSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeBlueprintInstancesRequest(AbstractModel):
    """DescribeBlueprintInstances request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: Instance ID list, which currently can contain only one instance.
        :type InstanceIds: list of str
        """
        self._InstanceIds = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBlueprintInstancesResponse(AbstractModel):
    """DescribeBlueprintInstances response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible image instances.
        :type TotalCount: int
        :param _BlueprintInstanceSet: Image instance list information.
        :type BlueprintInstanceSet: list of BlueprintInstance
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._BlueprintInstanceSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def BlueprintInstanceSet(self):
        return self._BlueprintInstanceSet

    @BlueprintInstanceSet.setter
    def BlueprintInstanceSet(self, BlueprintInstanceSet):
        self._BlueprintInstanceSet = BlueprintInstanceSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("BlueprintInstanceSet") is not None:
            self._BlueprintInstanceSet = []
            for item in params.get("BlueprintInstanceSet"):
                obj = BlueprintInstance()
                obj._deserialize(item)
                self._BlueprintInstanceSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBlueprintsRequest(AbstractModel):
    """DescribeBlueprints request structure.

    """

    def __init__(self):
        r"""
        :param _BlueprintIds: Image ID list.
        :type BlueprintIds: list of str
        :param _Offset: Offset. Default value: 0. For more information on `Offset`, please see the relevant section in [Overview](https://intl.cloud.tencent.com/document/product/1207/47578?from_cn_redirect=1).
        :type Offset: int
        :param _Limit: Number of returned results. Default value: 20. Maximum value: 100. For more information on `Limit`, please see the relevant section in the API [Overview](https://intl.cloud.tencent.com/document/product/1207/47578?from_cn_redirect=1).
        :type Limit: int
        :param _Filters: Filter list.
<li>blueprint-id</li>Filter by the **image ID**.
Type: String
Required: no
<li>blueprint-type</li>Filter by the **image type**.
Valid values: `APP_OS` (application image), `PURE_OS` (system image), `DOCKER` (Docker container image), `PRIVATE` (custom image), `SHARED` (shared image)
Type: String
Required: no
<li>platform-type</li>Filter by the **image operating system**.
Valid values: `LINUX_UNIX` (Linux or Unix), `WINDOWS` (Windows)
Type: String
Required: no
<li>blueprint-name</li>Filter by the **image name**.
Type: String
Required: no
<li>blueprint-state</li>Filter by the **image status**.
Type: String
Required: no
<li>scene-id</li>Filter by the **scene ID**.
Type: String
Required: no

Each request can contain up to 10 `Filters`, each of which can contain up to 100 `Filter.Values`. `BlueprintIds` and `Filters` cannot be specified at the same time.
        :type Filters: list of Filter
        """
        self._BlueprintIds = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def BlueprintIds(self):
        return self._BlueprintIds

    @BlueprintIds.setter
    def BlueprintIds(self, BlueprintIds):
        self._BlueprintIds = BlueprintIds

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._BlueprintIds = params.get("BlueprintIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
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
        


class DescribeBlueprintsResponse(AbstractModel):
    """DescribeBlueprints response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible images.
        :type TotalCount: int
        :param _BlueprintSet: Image details list.
        :type BlueprintSet: list of Blueprint
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._BlueprintSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def BlueprintSet(self):
        return self._BlueprintSet

    @BlueprintSet.setter
    def BlueprintSet(self, BlueprintSet):
        self._BlueprintSet = BlueprintSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("BlueprintSet") is not None:
            self._BlueprintSet = []
            for item in params.get("BlueprintSet"):
                obj = Blueprint()
                obj._deserialize(item)
                self._BlueprintSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBundleDiscountRequest(AbstractModel):
    """DescribeBundleDiscount request structure.

    """

    def __init__(self):
        r"""
        :param _BundleId: Package ID.
        :type BundleId: str
        """
        self._BundleId = None

    @property
    def BundleId(self):
        return self._BundleId

    @BundleId.setter
    def BundleId(self, BundleId):
        self._BundleId = BundleId


    def _deserialize(self, params):
        self._BundleId = params.get("BundleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBundleDiscountResponse(AbstractModel):
    """DescribeBundleDiscount response structure.

    """

    def __init__(self):
        r"""
        :param _Currency: Currency: CNY, USD.
        :type Currency: str
        :param _DiscountDetail: Discount tier details. The information of each tier includes the duration, discounted quantity, total price, discounted price, and discount details (user discount, official website discount, or final discount).
        :type DiscountDetail: list of DiscountDetail
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Currency = None
        self._DiscountDetail = None
        self._RequestId = None

    @property
    def Currency(self):
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency

    @property
    def DiscountDetail(self):
        return self._DiscountDetail

    @DiscountDetail.setter
    def DiscountDetail(self, DiscountDetail):
        self._DiscountDetail = DiscountDetail

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Currency = params.get("Currency")
        if params.get("DiscountDetail") is not None:
            self._DiscountDetail = []
            for item in params.get("DiscountDetail"):
                obj = DiscountDetail()
                obj._deserialize(item)
                self._DiscountDetail.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBundlesRequest(AbstractModel):
    """DescribeBundles request structure.

    """

    def __init__(self):
        r"""
        :param _BundleIds: Package ID list.
        :type BundleIds: list of str
        :param _Offset: Offset. Default value: 0. For more information on `Offset`, please see the relevant section in [Overview](https://intl.cloud.tencent.com/document/product/1207/47578?from_cn_redirect=1).
        :type Offset: int
        :param _Limit: Number of returned results. Default value: 20. Maximum value: 100. For more information on `Limit`, please see the relevant section in the API [Overview](https://intl.cloud.tencent.com/document/product/1207/47578?from_cn_redirect=1).
        :type Limit: int
        :param _Filters: Filter list
<li>bundle-id</li>Filter by the **bundle ID**.
Type: String
Required: No
<li>support-platform-type</li>Filter by the **OS type**.
Valid values: `LINUX_UNIX` (Linux or Unix), `WINDOWS` (Windows)
Type: String
Required: No
<li>bundle-type</li>Filter by the **bundle type**.
Valid values: `GENERAL_BUNDLE` (General bundle), `STORAGE_BUNDLE` (Storage bundle), `ENTERPRISE_BUNDLE` (Enterprise bundle), `EXCLUSIVE_BUNDLE` (Dedicated bundle), `BEFAST_BUNDLE` (BeFast bundle)
Type: String
Required: No
<li>bundle-state</li>Filter by the **bundle status**.
Valid values: `ONLINE`, `OFFLINE`
Type: String
Required: No
Each request can contain up to 10 `Filters`, and up to 5 `Filter.Values` for each filter. You cannot specify both `BundleIds` and `Filters` at the same time.
        :type Filters: list of Filter
        :param _Zones: AZ list, which contains all AZs by default.
        :type Zones: list of str
        """
        self._BundleIds = None
        self._Offset = None
        self._Limit = None
        self._Filters = None
        self._Zones = None

    @property
    def BundleIds(self):
        return self._BundleIds

    @BundleIds.setter
    def BundleIds(self, BundleIds):
        self._BundleIds = BundleIds

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Zones(self):
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones


    def _deserialize(self, params):
        self._BundleIds = params.get("BundleIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Zones = params.get("Zones")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBundlesResponse(AbstractModel):
    """DescribeBundles response structure.

    """

    def __init__(self):
        r"""
        :param _BundleSet: List of package details.
        :type BundleSet: list of Bundle
        :param _TotalCount: Total number of eligible packages, which is used for pagination.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BundleSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def BundleSet(self):
        return self._BundleSet

    @BundleSet.setter
    def BundleSet(self, BundleSet):
        self._BundleSet = BundleSet

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("BundleSet") is not None:
            self._BundleSet = []
            for item in params.get("BundleSet"):
                obj = Bundle()
                obj._deserialize(item)
                self._BundleSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeCcnAttachedInstancesRequest(AbstractModel):
    """DescribeCcnAttachedInstances request structure.

    """


class DescribeCcnAttachedInstancesResponse(AbstractModel):
    """DescribeCcnAttachedInstances response structure.

    """

    def __init__(self):
        r"""
        :param _CcnAttachedInstanceSet: List of instances associated with the CCN instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CcnAttachedInstanceSet: list of CcnAttachedInstance
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CcnAttachedInstanceSet = None
        self._RequestId = None

    @property
    def CcnAttachedInstanceSet(self):
        return self._CcnAttachedInstanceSet

    @CcnAttachedInstanceSet.setter
    def CcnAttachedInstanceSet(self, CcnAttachedInstanceSet):
        self._CcnAttachedInstanceSet = CcnAttachedInstanceSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CcnAttachedInstanceSet") is not None:
            self._CcnAttachedInstanceSet = []
            for item in params.get("CcnAttachedInstanceSet"):
                obj = CcnAttachedInstance()
                obj._deserialize(item)
                self._CcnAttachedInstanceSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDiskConfigsRequest(AbstractModel):
    """DescribeDiskConfigs request structure.

    """

    def __init__(self):
        r"""
        :param _Filters: Filter list.
<li>zone</li>Filter by availability zone.
Type: String
Required: no
        :type Filters: list of Filter
        """
        self._Filters = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
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
        


class DescribeDiskConfigsResponse(AbstractModel):
    """DescribeDiskConfigs response structure.

    """

    def __init__(self):
        r"""
        :param _DiskConfigSet: List of cloud disk configurations.
        :type DiskConfigSet: list of DiskConfig
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DiskConfigSet = None
        self._RequestId = None

    @property
    def DiskConfigSet(self):
        return self._DiskConfigSet

    @DiskConfigSet.setter
    def DiskConfigSet(self, DiskConfigSet):
        self._DiskConfigSet = DiskConfigSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DiskConfigSet") is not None:
            self._DiskConfigSet = []
            for item in params.get("DiskConfigSet"):
                obj = DiskConfig()
                obj._deserialize(item)
                self._DiskConfigSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDiskDiscountRequest(AbstractModel):
    """DescribeDiskDiscount request structure.

    """

    def __init__(self):
        r"""
        :param _DiskType: Cloud disk type. Valid values: "CLOUD_PREMIUM".
        :type DiskType: str
        :param _DiskSize: Cloud disk size.
        :type DiskSize: int
        :param _DiskBackupQuota: Specify the quota of disk backups. No quota if it’s left empty. Only one quota is allowed.
        :type DiskBackupQuota: int
        """
        self._DiskType = None
        self._DiskSize = None
        self._DiskBackupQuota = None

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DiskBackupQuota(self):
        return self._DiskBackupQuota

    @DiskBackupQuota.setter
    def DiskBackupQuota(self, DiskBackupQuota):
        self._DiskBackupQuota = DiskBackupQuota


    def _deserialize(self, params):
        self._DiskType = params.get("DiskType")
        self._DiskSize = params.get("DiskSize")
        self._DiskBackupQuota = params.get("DiskBackupQuota")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDiskDiscountResponse(AbstractModel):
    """DescribeDiskDiscount response structure.

    """

    def __init__(self):
        r"""
        :param _Currency: Currency: CNY, USD.
        :type Currency: str
        :param _DiscountDetail: Discount tier details. The information of each tier includes the duration, discounted quantity, total price, discounted price, and discount details (user discount, official website discount, or final discount).
        :type DiscountDetail: list of DiscountDetail
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Currency = None
        self._DiscountDetail = None
        self._RequestId = None

    @property
    def Currency(self):
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency

    @property
    def DiscountDetail(self):
        return self._DiscountDetail

    @DiscountDetail.setter
    def DiscountDetail(self, DiscountDetail):
        self._DiscountDetail = DiscountDetail

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Currency = params.get("Currency")
        if params.get("DiscountDetail") is not None:
            self._DiscountDetail = []
            for item in params.get("DiscountDetail"):
                obj = DiscountDetail()
                obj._deserialize(item)
                self._DiscountDetail.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDisksDeniedActionsRequest(AbstractModel):
    """DescribeDisksDeniedActions request structure.

    """

    def __init__(self):
        r"""
        :param _DiskIds: List of cloud disk IDs.
        :type DiskIds: list of str
        """
        self._DiskIds = None

    @property
    def DiskIds(self):
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds


    def _deserialize(self, params):
        self._DiskIds = params.get("DiskIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDisksDeniedActionsResponse(AbstractModel):
    """DescribeDisksDeniedActions response structure.

    """

    def __init__(self):
        r"""
        :param _DiskDeniedActionSet: List of operation limits of cloud disks.
        :type DiskDeniedActionSet: list of DiskDeniedActions
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DiskDeniedActionSet = None
        self._RequestId = None

    @property
    def DiskDeniedActionSet(self):
        return self._DiskDeniedActionSet

    @DiskDeniedActionSet.setter
    def DiskDeniedActionSet(self, DiskDeniedActionSet):
        self._DiskDeniedActionSet = DiskDeniedActionSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DiskDeniedActionSet") is not None:
            self._DiskDeniedActionSet = []
            for item in params.get("DiskDeniedActionSet"):
                obj = DiskDeniedActions()
                obj._deserialize(item)
                self._DiskDeniedActionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDisksRequest(AbstractModel):
    """DescribeDisks request structure.

    """

    def __init__(self):
        r"""
        :param _DiskIds: List of cloud disk IDs.
        :type DiskIds: list of str
        :param _Filters: Filter list
disk-id
Filter by **cloud disk ID**.
Type: String
Required: No
instance-id
Filter by **instance ID**.
Type: String
Required: No
disk-name
Filter by **cloud disk name**.
Type: String
Required: No
zone
Filter by **availability zone**.
Type: String
Required: No
disk-usage
Filter by **cloud disk type**.
Type: String
Required: No
Values: `SYSTEM_DISK` and `DATA_DISK`
disk-state
Filter by **cloud disk status**.
Type: String
Required: No
Values: See `DiskState` in [Disk](https://intl.cloud.tencent.com/document/api/1207/47576?from_cn_redirect=1#Disk)
Each request can contain up to 10 `Filters` and 100 `Filter.Values`. `DiskIds` and `Filters` cannot be specified at the same time.
        :type Filters: list of Filter
        :param _Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _OrderField: The field by which the cloud disks are sorted. Valid values: "CREATED_TIME" (creation time), "EXPIRED_TIME" (expiration time), "DISK_SIZE" (size of cloud disks). Default value: "CREATED_TIME".
        :type OrderField: str
        :param _Order: Sorting order of the output cloud disks. Valid values: "ASC" (ascending order), "DESC" (descending order). Default value: "DESC".
        :type Order: str
        """
        self._DiskIds = None
        self._Filters = None
        self._Limit = None
        self._Offset = None
        self._OrderField = None
        self._Order = None

    @property
    def DiskIds(self):
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def OrderField(self):
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order


    def _deserialize(self, params):
        self._DiskIds = params.get("DiskIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._OrderField = params.get("OrderField")
        self._Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDisksResponse(AbstractModel):
    """DescribeDisks response structure.

    """

    def __init__(self):
        r"""
        :param _DiskSet: List of cloud disk information.
        :type DiskSet: list of Disk
        :param _TotalCount: Number of eligible cloud disks.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DiskSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def DiskSet(self):
        return self._DiskSet

    @DiskSet.setter
    def DiskSet(self, DiskSet):
        self._DiskSet = DiskSet

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DiskSet") is not None:
            self._DiskSet = []
            for item in params.get("DiskSet"):
                obj = Disk()
                obj._deserialize(item)
                self._DiskSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDisksReturnableRequest(AbstractModel):
    """DescribeDisksReturnable request structure.

    """

    def __init__(self):
        r"""
        :param _DiskIds: List of cloud disk IDs.
        :type DiskIds: list of str
        :param _Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        """
        self._DiskIds = None
        self._Limit = None
        self._Offset = None

    @property
    def DiskIds(self):
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._DiskIds = params.get("DiskIds")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDisksReturnableResponse(AbstractModel):
    """DescribeDisksReturnable response structure.

    """

    def __init__(self):
        r"""
        :param _DiskReturnableSet: List of returnable cloud disks.
        :type DiskReturnableSet: list of DiskReturnable
        :param _TotalCount: Number of eligible cloud disks.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DiskReturnableSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def DiskReturnableSet(self):
        return self._DiskReturnableSet

    @DiskReturnableSet.setter
    def DiskReturnableSet(self, DiskReturnableSet):
        self._DiskReturnableSet = DiskReturnableSet

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DiskReturnableSet") is not None:
            self._DiskReturnableSet = []
            for item in params.get("DiskReturnableSet"):
                obj = DiskReturnable()
                obj._deserialize(item)
                self._DiskReturnableSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeFirewallRulesRequest(AbstractModel):
    """DescribeFirewallRules request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFirewallRulesResponse(AbstractModel):
    """DescribeFirewallRules response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible firewall rules.
        :type TotalCount: int
        :param _FirewallRuleSet: Firewall rule details list.
        :type FirewallRuleSet: list of FirewallRuleInfo
        :param _FirewallVersion: Firewall version number.
        :type FirewallVersion: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._FirewallRuleSet = None
        self._FirewallVersion = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def FirewallRuleSet(self):
        return self._FirewallRuleSet

    @FirewallRuleSet.setter
    def FirewallRuleSet(self, FirewallRuleSet):
        self._FirewallRuleSet = FirewallRuleSet

    @property
    def FirewallVersion(self):
        return self._FirewallVersion

    @FirewallVersion.setter
    def FirewallVersion(self, FirewallVersion):
        self._FirewallVersion = FirewallVersion

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("FirewallRuleSet") is not None:
            self._FirewallRuleSet = []
            for item in params.get("FirewallRuleSet"):
                obj = FirewallRuleInfo()
                obj._deserialize(item)
                self._FirewallRuleSet.append(obj)
        self._FirewallVersion = params.get("FirewallVersion")
        self._RequestId = params.get("RequestId")


class DescribeFirewallRulesTemplateRequest(AbstractModel):
    """DescribeFirewallRulesTemplate request structure.

    """


class DescribeFirewallRulesTemplateResponse(AbstractModel):
    """DescribeFirewallRulesTemplate response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible firewall rules.
        :type TotalCount: int
        :param _FirewallRuleSet: Firewall rule details list.
        :type FirewallRuleSet: list of FirewallRuleInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._FirewallRuleSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def FirewallRuleSet(self):
        return self._FirewallRuleSet

    @FirewallRuleSet.setter
    def FirewallRuleSet(self, FirewallRuleSet):
        self._FirewallRuleSet = FirewallRuleSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("FirewallRuleSet") is not None:
            self._FirewallRuleSet = []
            for item in params.get("FirewallRuleSet"):
                obj = FirewallRuleInfo()
                obj._deserialize(item)
                self._FirewallRuleSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeGeneralResourceQuotasRequest(AbstractModel):
    """DescribeGeneralResourceQuotas request structure.

    """

    def __init__(self):
        r"""
        :param _ResourceNames: Resource name list. Values:
- `GENERAL_BUNDLE_INSTANCE`: General bundle
- `STORAGE_BUNDLE_INSTANCE`:  Storage bundle 
- `ENTERPRISE_BUNDLE_INSTANCE`: Enterprise bundle 
- `EXCLUSIVE_BUNDLE_INSTANCE`： Dedicated bundle
- `BEFAST_BUNDLE_INSTANCE`: BeFast bundle
- `USER_KEY_PAIR`: Key pair
- `SNAPSHOT`: Snapshot
- `BLUEPRINT`: Custom image
- `FREE_BLUEPRINT`: Free custom image
- `DATA_DISK`: Data disk
- `FIREWALL_RULE`: Firewall rules
        :type ResourceNames: list of str
        """
        self._ResourceNames = None

    @property
    def ResourceNames(self):
        return self._ResourceNames

    @ResourceNames.setter
    def ResourceNames(self, ResourceNames):
        self._ResourceNames = ResourceNames


    def _deserialize(self, params):
        self._ResourceNames = params.get("ResourceNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGeneralResourceQuotasResponse(AbstractModel):
    """DescribeGeneralResourceQuotas response structure.

    """

    def __init__(self):
        r"""
        :param _GeneralResourceQuotaSet: List of general resource quota details.
        :type GeneralResourceQuotaSet: list of GeneralResourceQuota
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._GeneralResourceQuotaSet = None
        self._RequestId = None

    @property
    def GeneralResourceQuotaSet(self):
        return self._GeneralResourceQuotaSet

    @GeneralResourceQuotaSet.setter
    def GeneralResourceQuotaSet(self, GeneralResourceQuotaSet):
        self._GeneralResourceQuotaSet = GeneralResourceQuotaSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("GeneralResourceQuotaSet") is not None:
            self._GeneralResourceQuotaSet = []
            for item in params.get("GeneralResourceQuotaSet"):
                obj = GeneralResourceQuota()
                obj._deserialize(item)
                self._GeneralResourceQuotaSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceLoginKeyPairAttributeRequest(AbstractModel):
    """DescribeInstanceLoginKeyPairAttribute request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceLoginKeyPairAttributeResponse(AbstractModel):
    """DescribeInstanceLoginKeyPairAttribute response structure.

    """

    def __init__(self):
        r"""
        :param _PermitLogin: Whether to allow login with the default key pair. Valid values: YES, NO.
        :type PermitLogin: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PermitLogin = None
        self._RequestId = None

    @property
    def PermitLogin(self):
        return self._PermitLogin

    @PermitLogin.setter
    def PermitLogin(self, PermitLogin):
        self._PermitLogin = PermitLogin

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PermitLogin = params.get("PermitLogin")
        self._RequestId = params.get("RequestId")


class DescribeInstanceVncUrlRequest(AbstractModel):
    """DescribeInstanceVncUrl request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID, which can be obtained from the `InstanceId` returned by the [DescribeInstances](https://intl.cloud.tencent.com/document/api/1207/47573?from_cn_redirect=1) API.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceVncUrlResponse(AbstractModel):
    """DescribeInstanceVncUrl response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceVncUrl: Instance VNC URL.
        :type InstanceVncUrl: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceVncUrl = None
        self._RequestId = None

    @property
    def InstanceVncUrl(self):
        return self._InstanceVncUrl

    @InstanceVncUrl.setter
    def InstanceVncUrl(self, InstanceVncUrl):
        self._InstanceVncUrl = InstanceVncUrl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceVncUrl = params.get("InstanceVncUrl")
        self._RequestId = params.get("RequestId")


class DescribeInstancesDeniedActionsRequest(AbstractModel):
    """DescribeInstancesDeniedActions request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: Instance ID list. Each request can contain up to 100 instances at a time. You can get an instance ID from the `InstanceId` returned by the [DescribeInstances](https://intl.cloud.tencent.com/document/api/1207/47573?from_cn_redirect=1) API.
        :type InstanceIds: list of str
        """
        self._InstanceIds = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesDeniedActionsResponse(AbstractModel):
    """DescribeInstancesDeniedActions response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceDeniedActionSet: List of instance operation limit details.
        :type InstanceDeniedActionSet: list of InstanceDeniedActions
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceDeniedActionSet = None
        self._RequestId = None

    @property
    def InstanceDeniedActionSet(self):
        return self._InstanceDeniedActionSet

    @InstanceDeniedActionSet.setter
    def InstanceDeniedActionSet(self, InstanceDeniedActionSet):
        self._InstanceDeniedActionSet = InstanceDeniedActionSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InstanceDeniedActionSet") is not None:
            self._InstanceDeniedActionSet = []
            for item in params.get("InstanceDeniedActionSet"):
                obj = InstanceDeniedActions()
                obj._deserialize(item)
                self._InstanceDeniedActionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstancesDiskNumRequest(AbstractModel):
    """DescribeInstancesDiskNum request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: List of instance IDs.
        :type InstanceIds: list of str
        """
        self._InstanceIds = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesDiskNumResponse(AbstractModel):
    """DescribeInstancesDiskNum response structure.

    """

    def __init__(self):
        r"""
        :param _AttachDetailSet: Information of all attached disks
        :type AttachDetailSet: list of AttachDetail
        :param _TotalCount: Number of attached cloud disks
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AttachDetailSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def AttachDetailSet(self):
        return self._AttachDetailSet

    @AttachDetailSet.setter
    def AttachDetailSet(self, AttachDetailSet):
        self._AttachDetailSet = AttachDetailSet

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AttachDetailSet") is not None:
            self._AttachDetailSet = []
            for item in params.get("AttachDetailSet"):
                obj = AttachDetail()
                obj._deserialize(item)
                self._AttachDetailSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: Instance ID list. Each request can contain up to 100 instances at a time.
        :type InstanceIds: list of str
        :param _Filters: Filter list. 
<li>instance-name</li>Filter by the **instance name**. 
Type: String 
Required: No 
<li>private-ip-address</li>Filter by the **private IP of instance primary ENI**. 
Type: String 
Required: No 
<li>public-ip-address</li>Filter by the **public IP of instance primary ENI**. 
Type: String 
Required: No 
<li>zone</li>Filter by the availability zone. 
Type: String 
Required: No 
<li>instance-state</li>Filter by the **instance status**. 
Type: String 
Required: No 
<li>tag-key</li>Filter by the **tag key**. 
Type: String 
Required: No 
<li>tag-value</li>Filter by the **tag value**. 
Type: String 
Required: No 
<li> tag:tag-key</li>Filter by tag key-value pair. The `tag-key` should be replaced with a specific tag key. 
Type: String 
Required: No 
Each request can contain up to 10 `Filters` and 100 `Filter.Values`. You cannot specify both `InstanceIds` and `Filters` at the same time.
        :type Filters: list of Filter
        :param _Offset: Offset. Default value: 0. For more information on `Offset`, please see the relevant section in [Overview](https://intl.cloud.tencent.com/document/product/1207/47578?from_cn_redirect=1).
        :type Offset: int
        :param _Limit: Number of returned results. Default value: 20. Maximum value: 100. For more information on `Limit`, please see the relevant section in the API [Overview](https://intl.cloud.tencent.com/document/product/1207/47578?from_cn_redirect=1).
        :type Limit: int
        """
        self._InstanceIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible instances.
        :type TotalCount: int
        :param _InstanceSet: List of instance details
        :type InstanceSet: list of Instance
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceSet(self):
        return self._InstanceSet

    @InstanceSet.setter
    def InstanceSet(self, InstanceSet):
        self._InstanceSet = InstanceSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("InstanceSet") is not None:
            self._InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = Instance()
                obj._deserialize(item)
                self._InstanceSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstancesReturnableRequest(AbstractModel):
    """DescribeInstancesReturnable request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: Instance ID list. Each request can contain up to 100 instances at a time. You can get an instance ID from the `InstanceId` returned by the [DescribeInstances](https://intl.cloud.tencent.com/document/api/1207/47573?from_cn_redirect=1) API.
        :type InstanceIds: list of str
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        """
        self._InstanceIds = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesReturnableResponse(AbstractModel):
    """DescribeInstancesReturnable response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible instances.
        :type TotalCount: int
        :param _InstanceReturnableSet: List of returnable instance details.
        :type InstanceReturnableSet: list of InstanceReturnable
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceReturnableSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceReturnableSet(self):
        return self._InstanceReturnableSet

    @InstanceReturnableSet.setter
    def InstanceReturnableSet(self, InstanceReturnableSet):
        self._InstanceReturnableSet = InstanceReturnableSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("InstanceReturnableSet") is not None:
            self._InstanceReturnableSet = []
            for item in params.get("InstanceReturnableSet"):
                obj = InstanceReturnable()
                obj._deserialize(item)
                self._InstanceReturnableSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstancesTrafficPackagesRequest(AbstractModel):
    """DescribeInstancesTrafficPackages request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: Instance ID list. Each request can contain up to 100 instances at a time. You can get an instance ID from the `InstanceId` returned by the [DescribeInstances](https://intl.cloud.tencent.com/document/api/1207/47573?from_cn_redirect=1) API.
        :type InstanceIds: list of str
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        """
        self._InstanceIds = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesTrafficPackagesResponse(AbstractModel):
    """DescribeInstancesTrafficPackages response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible instance traffic package details.
        :type TotalCount: int
        :param _InstanceTrafficPackageSet: List of instance traffic package details.
        :type InstanceTrafficPackageSet: list of InstanceTrafficPackage
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceTrafficPackageSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceTrafficPackageSet(self):
        return self._InstanceTrafficPackageSet

    @InstanceTrafficPackageSet.setter
    def InstanceTrafficPackageSet(self, InstanceTrafficPackageSet):
        self._InstanceTrafficPackageSet = InstanceTrafficPackageSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("InstanceTrafficPackageSet") is not None:
            self._InstanceTrafficPackageSet = []
            for item in params.get("InstanceTrafficPackageSet"):
                obj = InstanceTrafficPackage()
                obj._deserialize(item)
                self._InstanceTrafficPackageSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeKeyPairsRequest(AbstractModel):
    """DescribeKeyPairs request structure.

    """

    def __init__(self):
        r"""
        :param _KeyIds: Key pair ID list.
        :type KeyIds: list of str
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param _Filters: Filter list.
<li>key-id</li>Filter by **key pair ID**.
Type: String
Required: no
<li>key-name</li>Filter by the **key pair name**. Fuzzy match is supported.
Type: String
Required: no
Each request can contain up to 10 `Filters` and up to 5 `Filter.Values` for each filter. `KeyIds` and `Filters` cannot be specified at the same time.
        :type Filters: list of Filter
        """
        self._KeyIds = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def KeyIds(self):
        return self._KeyIds

    @KeyIds.setter
    def KeyIds(self, KeyIds):
        self._KeyIds = KeyIds

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._KeyIds = params.get("KeyIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
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
        


class DescribeKeyPairsResponse(AbstractModel):
    """DescribeKeyPairs response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible key pairs.
        :type TotalCount: int
        :param _KeyPairSet: List of key pair details.
        :type KeyPairSet: list of KeyPair
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._KeyPairSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def KeyPairSet(self):
        return self._KeyPairSet

    @KeyPairSet.setter
    def KeyPairSet(self, KeyPairSet):
        self._KeyPairSet = KeyPairSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("KeyPairSet") is not None:
            self._KeyPairSet = []
            for item in params.get("KeyPairSet"):
                obj = KeyPair()
                obj._deserialize(item)
                self._KeyPairSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeModifyInstanceBundlesRequest(AbstractModel):
    """DescribeModifyInstanceBundles request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _Filters: Filter list
<li>bundle-id</li>Filter by the **bundle ID**.
Type: String
Required: No
<li>support-platform-type</li>Filter by the **OS type**.
Valid values: `LINUX_UNIX` (Linux or Unix), `WINDOWS` (Windows)
Type: String
Required: No
<li>bundle-type</li>Filter by the **bundle type**.
Valid values: `GENERAL_BUNDLE` (General bundle), `STORAGE_BUNDLE` (Storage bundle), `ENTERPRISE_BUNDLE` (Enterprise bundle), `EXCLUSIVE_BUNDLE` (Dedicated bundle), `BEFAST_BUNDLE` (BeFast bundle)
Type: String
Required: No
<li>bundle-state</li>Filter by the **bundle status**.
Valid values: `ONLINE`, `OFFLINE`
Type: String
Required: No
Each request can contain up to 10 `Filters`, and each filter can have up to 5 `Filter.Values`.
        :type Filters: list of Filter
        :param _Offset: Offset. Default value: 0. For more information on `Offset`, please see the relevant section in [Overview](https://intl.cloud.tencent.com/document/product/1207/47578?from_cn_redirect=1).
        :type Offset: int
        :param _Limit: Number of returned results. Default value: 20. Maximum value: 100. For more information on `Limit`, please see the relevant section in the API [Overview](https://intl.cloud.tencent.com/document/product/1207/47578?from_cn_redirect=1).
        :type Limit: int
        """
        self._InstanceId = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeModifyInstanceBundlesResponse(AbstractModel):
    """DescribeModifyInstanceBundles response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of matched instances.
        :type TotalCount: int
        :param _ModifyBundleSet: New package details
        :type ModifyBundleSet: list of ModifyBundle
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._ModifyBundleSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ModifyBundleSet(self):
        return self._ModifyBundleSet

    @ModifyBundleSet.setter
    def ModifyBundleSet(self, ModifyBundleSet):
        self._ModifyBundleSet = ModifyBundleSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ModifyBundleSet") is not None:
            self._ModifyBundleSet = []
            for item in params.get("ModifyBundleSet"):
                obj = ModifyBundle()
                obj._deserialize(item)
                self._ModifyBundleSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRegionsRequest(AbstractModel):
    """DescribeRegions request structure.

    """


class DescribeRegionsResponse(AbstractModel):
    """DescribeRegions response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of regions.
        :type TotalCount: int
        :param _RegionSet: Region information list.
        :type RegionSet: list of RegionInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._RegionSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RegionSet(self):
        return self._RegionSet

    @RegionSet.setter
    def RegionSet(self, RegionSet):
        self._RegionSet = RegionSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("RegionSet") is not None:
            self._RegionSet = []
            for item in params.get("RegionSet"):
                obj = RegionInfo()
                obj._deserialize(item)
                self._RegionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeResetInstanceBlueprintsRequest(AbstractModel):
    """DescribeResetInstanceBlueprints request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Offset: Offset. Default value: 0. For more information on `Offset`, please see the relevant section in [Overview](https://intl.cloud.tencent.com/document/product/1207/47578?from_cn_redirect=1).
        :type Offset: int
        :param _Limit: Number of returned results. Default value: 20. Maximum value: 100. For more information on `Limit`, please see the relevant section in the API [Overview](https://intl.cloud.tencent.com/document/product/1207/47578?from_cn_redirect=1).
        :type Limit: int
        :param _Filters: Filter list
<li>blueprint-id</li>Filter by **image ID**.
Type: String
Required: no
<li>blueprint-type</li>Filter by **image type**.
Valid values: `APP_OS`: application image; `PURE_OS`: system image; `PRIVATE`: custom image
Type: String
Required: no
<li>platform-type</li>Filter by **image platform type**.
Valid values: `LINUX_UNIX`: Linux or Unix; `WINDOWS`: Windows
Type: String
Required: no
<li>blueprint-name</li>Filter by **image name**.
Type: String
Required: no
<li>blueprint-state</li>Filter by **image status**.
Type: String
Required: no

Each request can contain up to 10 `Filters` and 5 `Filter.Values`. `BlueprintIds` and `Filters` cannot be specified at the same time.
        :type Filters: list of Filter
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
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
        


class DescribeResetInstanceBlueprintsResponse(AbstractModel):
    """DescribeResetInstanceBlueprints response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible images.
        :type TotalCount: int
        :param _ResetInstanceBlueprintSet: Image reset information list
        :type ResetInstanceBlueprintSet: list of ResetInstanceBlueprint
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._ResetInstanceBlueprintSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ResetInstanceBlueprintSet(self):
        return self._ResetInstanceBlueprintSet

    @ResetInstanceBlueprintSet.setter
    def ResetInstanceBlueprintSet(self, ResetInstanceBlueprintSet):
        self._ResetInstanceBlueprintSet = ResetInstanceBlueprintSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ResetInstanceBlueprintSet") is not None:
            self._ResetInstanceBlueprintSet = []
            for item in params.get("ResetInstanceBlueprintSet"):
                obj = ResetInstanceBlueprint()
                obj._deserialize(item)
                self._ResetInstanceBlueprintSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeScenesRequest(AbstractModel):
    """DescribeScenes request structure.

    """

    def __init__(self):
        r"""
        :param _SceneIds: List of scene IDs
        :type SceneIds: list of str
        :param _Offset: Offset. Default value: 0
        :type Offset: int
        :param _Limit: Number of returned results. Default value: 20. Maximum value: 100
        :type Limit: int
        """
        self._SceneIds = None
        self._Offset = None
        self._Limit = None

    @property
    def SceneIds(self):
        return self._SceneIds

    @SceneIds.setter
    def SceneIds(self, SceneIds):
        self._SceneIds = SceneIds

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._SceneIds = params.get("SceneIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScenesResponse(AbstractModel):
    """DescribeScenes response structure.

    """

    def __init__(self):
        r"""
        :param _SceneSet: List of scenes
        :type SceneSet: list of Scene
        :param _TotalCount: Total number of scenes
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SceneSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def SceneSet(self):
        return self._SceneSet

    @SceneSet.setter
    def SceneSet(self, SceneSet):
        self._SceneSet = SceneSet

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SceneSet") is not None:
            self._SceneSet = []
            for item in params.get("SceneSet"):
                obj = Scene()
                obj._deserialize(item)
                self._SceneSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeSnapshotsDeniedActionsRequest(AbstractModel):
    """DescribeSnapshotsDeniedActions request structure.

    """

    def __init__(self):
        r"""
        :param _SnapshotIds: Snapshot ID list, which can be queried through `DescribeSnapshots`.
        :type SnapshotIds: list of str
        """
        self._SnapshotIds = None

    @property
    def SnapshotIds(self):
        return self._SnapshotIds

    @SnapshotIds.setter
    def SnapshotIds(self, SnapshotIds):
        self._SnapshotIds = SnapshotIds


    def _deserialize(self, params):
        self._SnapshotIds = params.get("SnapshotIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSnapshotsDeniedActionsResponse(AbstractModel):
    """DescribeSnapshotsDeniedActions response structure.

    """

    def __init__(self):
        r"""
        :param _SnapshotDeniedActionSet: List of snapshot operation limit details.
        :type SnapshotDeniedActionSet: list of SnapshotDeniedActions
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SnapshotDeniedActionSet = None
        self._RequestId = None

    @property
    def SnapshotDeniedActionSet(self):
        return self._SnapshotDeniedActionSet

    @SnapshotDeniedActionSet.setter
    def SnapshotDeniedActionSet(self, SnapshotDeniedActionSet):
        self._SnapshotDeniedActionSet = SnapshotDeniedActionSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SnapshotDeniedActionSet") is not None:
            self._SnapshotDeniedActionSet = []
            for item in params.get("SnapshotDeniedActionSet"):
                obj = SnapshotDeniedActions()
                obj._deserialize(item)
                self._SnapshotDeniedActionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSnapshotsRequest(AbstractModel):
    """DescribeSnapshots request structure.

    """

    def __init__(self):
        r"""
        :param _SnapshotIds: List of IDs of snapshots to be queried.
You cannot specify `SnapshotIds` and `Filters` at the same time.
        :type SnapshotIds: list of str
        :param _Filters: Filter list.
<li>snapshot-id</li>Filter by **snapshot ID**.
Type: String
Required: no
<li>disk-id</li>Filter by **disk ID**.
Type: String
Required: no
<li>snapshot-name</li>Filter by **snapshot name**.
Type: String
Required: no
<li>instance-id</li>Filter by **instance ID**.
Type: String
Required: no
Each request can contain up to 10 `Filters` and 5 `Filter.Values`. You cannot specify both `SnapshotIds` and `Filters` at the same time.
        :type Filters: list of Filter
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        """
        self._SnapshotIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def SnapshotIds(self):
        return self._SnapshotIds

    @SnapshotIds.setter
    def SnapshotIds(self, SnapshotIds):
        self._SnapshotIds = SnapshotIds

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._SnapshotIds = params.get("SnapshotIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSnapshotsResponse(AbstractModel):
    """DescribeSnapshots response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of snapshots.
        :type TotalCount: int
        :param _SnapshotSet: List of snapshot details.
        :type SnapshotSet: list of Snapshot
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._SnapshotSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SnapshotSet(self):
        return self._SnapshotSet

    @SnapshotSet.setter
    def SnapshotSet(self, SnapshotSet):
        self._SnapshotSet = SnapshotSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("SnapshotSet") is not None:
            self._SnapshotSet = []
            for item in params.get("SnapshotSet"):
                obj = Snapshot()
                obj._deserialize(item)
                self._SnapshotSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeZonesRequest(AbstractModel):
    """DescribeZones request structure.

    """

    def __init__(self):
        r"""
        :param _OrderField: Sorting field. Valid values:
<li>`ZONE`: Sort by the availability zone.
<li>`INSTANCE_DISPLAY_LABEL`: Sort by visibility labels (`HIDDEN`, `NORMAL` and `SELECTED`). Default: ['HIDDEN', 'NORMAL', 'SELECTED'].
The default value is `ZONE`.
        :type OrderField: str
        :param _Order: Specifies how availability zones are listed. Valid values:
<li>ASC: Ascending sort. 
<li>DESC: Descending sort.
The default value is `ASC`.
        :type Order: str
        """
        self._OrderField = None
        self._Order = None

    @property
    def OrderField(self):
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order


    def _deserialize(self, params):
        self._OrderField = params.get("OrderField")
        self._Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZonesResponse(AbstractModel):
    """DescribeZones response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of AZs
        :type TotalCount: int
        :param _ZoneInfoSet: List of AZ details
        :type ZoneInfoSet: list of ZoneInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._ZoneInfoSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ZoneInfoSet(self):
        return self._ZoneInfoSet

    @ZoneInfoSet.setter
    def ZoneInfoSet(self, ZoneInfoSet):
        self._ZoneInfoSet = ZoneInfoSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ZoneInfoSet") is not None:
            self._ZoneInfoSet = []
            for item in params.get("ZoneInfoSet"):
                obj = ZoneInfo()
                obj._deserialize(item)
                self._ZoneInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class DetachCcnRequest(AbstractModel):
    """DetachCcn request structure.

    """

    def __init__(self):
        r"""
        :param _CcnId: CCN instance ID.
        :type CcnId: str
        """
        self._CcnId = None

    @property
    def CcnId(self):
        return self._CcnId

    @CcnId.setter
    def CcnId(self, CcnId):
        self._CcnId = CcnId


    def _deserialize(self, params):
        self._CcnId = params.get("CcnId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachCcnResponse(AbstractModel):
    """DetachCcn response structure.

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


class DetachDisksRequest(AbstractModel):
    """DetachDisks request structure.

    """

    def __init__(self):
        r"""
        :param _DiskIds: List of cloud disk IDs.
        :type DiskIds: list of str
        """
        self._DiskIds = None

    @property
    def DiskIds(self):
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds


    def _deserialize(self, params):
        self._DiskIds = params.get("DiskIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachDisksResponse(AbstractModel):
    """DetachDisks response structure.

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


class DetailPrice(AbstractModel):
    """Billable items

    """

    def __init__(self):
        r"""
        :param _PriceName: Values: 
<li>"DiskSpace": Cloud disk space</li>
<li>"DiskBackupQuota": Cloud disk backups</li>
        :type PriceName: str
        :param _OriginUnitPrice: Official unit price of the billable item
        :type OriginUnitPrice: float
        :param _OriginalPrice: Official total price of the billable item
        :type OriginalPrice: float
        :param _Discount: Discount of the billable item
        :type Discount: float
        :param _DiscountPrice: Discounted total price of the billable item
        :type DiscountPrice: float
        """
        self._PriceName = None
        self._OriginUnitPrice = None
        self._OriginalPrice = None
        self._Discount = None
        self._DiscountPrice = None

    @property
    def PriceName(self):
        return self._PriceName

    @PriceName.setter
    def PriceName(self, PriceName):
        self._PriceName = PriceName

    @property
    def OriginUnitPrice(self):
        return self._OriginUnitPrice

    @OriginUnitPrice.setter
    def OriginUnitPrice(self, OriginUnitPrice):
        self._OriginUnitPrice = OriginUnitPrice

    @property
    def OriginalPrice(self):
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def Discount(self):
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount

    @property
    def DiscountPrice(self):
        return self._DiscountPrice

    @DiscountPrice.setter
    def DiscountPrice(self, DiscountPrice):
        self._DiscountPrice = DiscountPrice


    def _deserialize(self, params):
        self._PriceName = params.get("PriceName")
        self._OriginUnitPrice = params.get("OriginUnitPrice")
        self._OriginalPrice = params.get("OriginalPrice")
        self._Discount = params.get("Discount")
        self._DiscountPrice = params.get("DiscountPrice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateInstancesKeyPairsRequest(AbstractModel):
    """DisassociateInstancesKeyPairs request structure.

    """

    def __init__(self):
        r"""
        :param _KeyIds: Key pair ID list. Each request can contain up to 100 key pairs.
        :type KeyIds: list of str
        :param _InstanceIds: Instance ID list. Each request can contain up to 100 instances at a time. You can get an instance ID from the `InstanceId` returned by the [DescribeInstances](https://intl.cloud.tencent.com/document/api/1207/47573?from_cn_redirect=1) API.
        :type InstanceIds: list of str
        """
        self._KeyIds = None
        self._InstanceIds = None

    @property
    def KeyIds(self):
        return self._KeyIds

    @KeyIds.setter
    def KeyIds(self, KeyIds):
        self._KeyIds = KeyIds

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._KeyIds = params.get("KeyIds")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateInstancesKeyPairsResponse(AbstractModel):
    """DisassociateInstancesKeyPairs response structure.

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


class DiscountDetail(AbstractModel):
    """Package discount details (only returned for price query APIs called in the console).

    """

    def __init__(self):
        r"""
        :param _TimeSpan: Billing duration.
        :type TimeSpan: int
        :param _TimeUnit: Billing unit.
        :type TimeUnit: str
        :param _TotalCost: Total price.
        :type TotalCost: float
        :param _RealTotalCost: Discounted total price.
        :type RealTotalCost: float
        :param _Discount: Discount.
        :type Discount: int
        :param _PolicyDetail: Discount details.
        :type PolicyDetail: :class:`tencentcloud.lighthouse.v20200324.models.PolicyDetail`
        """
        self._TimeSpan = None
        self._TimeUnit = None
        self._TotalCost = None
        self._RealTotalCost = None
        self._Discount = None
        self._PolicyDetail = None

    @property
    def TimeSpan(self):
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def TimeUnit(self):
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def TotalCost(self):
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost

    @property
    def RealTotalCost(self):
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def Discount(self):
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount

    @property
    def PolicyDetail(self):
        return self._PolicyDetail

    @PolicyDetail.setter
    def PolicyDetail(self, PolicyDetail):
        self._PolicyDetail = PolicyDetail


    def _deserialize(self, params):
        self._TimeSpan = params.get("TimeSpan")
        self._TimeUnit = params.get("TimeUnit")
        self._TotalCost = params.get("TotalCost")
        self._RealTotalCost = params.get("RealTotalCost")
        self._Discount = params.get("Discount")
        if params.get("PolicyDetail") is not None:
            self._PolicyDetail = PolicyDetail()
            self._PolicyDetail._deserialize(params.get("PolicyDetail"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Disk(AbstractModel):
    """Disk information

    """

    def __init__(self):
        r"""
        :param _DiskId: Disk ID
        :type DiskId: str
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Zone: Availability zone
        :type Zone: str
        :param _DiskName: Disk name
        :type DiskName: str
        :param _DiskUsage: Disk type
        :type DiskUsage: str
        :param _DiskType: Disk media type
        :type DiskType: str
        :param _DiskChargeType: Disk payment type
        :type DiskChargeType: str
        :param _DiskSize: Disk size
        :type DiskSize: int
        :param _RenewFlag: Renewal flag
        :type RenewFlag: str
        :param _DiskState: Disk status. Values: 
<li>`PENDING`: Creating</li>
<li>`UNATTACHED`: Not attached</li>
<li>`ATTACHING`: Attaching</li>
<li>`ATTACHED`: Attached</li>
<li>`DETACHING`: Detaching</li>
<li>`SHUTDOWN`: Isolated</li>
<li>`CREATED_FAILED`: Failed to create</li>
<li>`TERMINATING`: Terminating</li>
<li>`DELETING`: Deleting</li>
<li>`FREEZING`: Freezing</li>
        :type DiskState: str
        :param _Attached: Whether the disk is attached to an instance
        :type Attached: bool
        :param _DeleteWithInstance: Whether to release the disk along with the instance
        :type DeleteWithInstance: bool
        :param _LatestOperation: Last operation
        :type LatestOperation: str
        :param _LatestOperationState: Last operation status
        :type LatestOperationState: str
        :param _LatestOperationRequestId: Last request ID
        :type LatestOperationRequestId: str
        :param _CreatedTime: Creation time according to ISO 8601 standard. UTC time is used. 
Format: YYYY-MM-DDThh:mm:ssZ.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type CreatedTime: str
        :param _ExpiredTime: Expiration time according to ISO 8601 standard. UTC time is used. 
Format: YYYY-MM-DDThh:mm:ssZ.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpiredTime: str
        :param _IsolatedTime: Isolation time according to ISO 8601 standard. UTC time is used. 
Format: YYYY-MM-DDThh:mm:ssZ.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsolatedTime: str
        :param _DiskBackupCount: Total disk backups
        :type DiskBackupCount: int
        :param _DiskBackupQuota: Disk backup quota
        :type DiskBackupQuota: int
        """
        self._DiskId = None
        self._InstanceId = None
        self._Zone = None
        self._DiskName = None
        self._DiskUsage = None
        self._DiskType = None
        self._DiskChargeType = None
        self._DiskSize = None
        self._RenewFlag = None
        self._DiskState = None
        self._Attached = None
        self._DeleteWithInstance = None
        self._LatestOperation = None
        self._LatestOperationState = None
        self._LatestOperationRequestId = None
        self._CreatedTime = None
        self._ExpiredTime = None
        self._IsolatedTime = None
        self._DiskBackupCount = None
        self._DiskBackupQuota = None

    @property
    def DiskId(self):
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def DiskName(self):
        return self._DiskName

    @DiskName.setter
    def DiskName(self, DiskName):
        self._DiskName = DiskName

    @property
    def DiskUsage(self):
        return self._DiskUsage

    @DiskUsage.setter
    def DiskUsage(self, DiskUsage):
        self._DiskUsage = DiskUsage

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskChargeType(self):
        return self._DiskChargeType

    @DiskChargeType.setter
    def DiskChargeType(self, DiskChargeType):
        self._DiskChargeType = DiskChargeType

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def DiskState(self):
        return self._DiskState

    @DiskState.setter
    def DiskState(self, DiskState):
        self._DiskState = DiskState

    @property
    def Attached(self):
        return self._Attached

    @Attached.setter
    def Attached(self, Attached):
        self._Attached = Attached

    @property
    def DeleteWithInstance(self):
        return self._DeleteWithInstance

    @DeleteWithInstance.setter
    def DeleteWithInstance(self, DeleteWithInstance):
        self._DeleteWithInstance = DeleteWithInstance

    @property
    def LatestOperation(self):
        return self._LatestOperation

    @LatestOperation.setter
    def LatestOperation(self, LatestOperation):
        self._LatestOperation = LatestOperation

    @property
    def LatestOperationState(self):
        return self._LatestOperationState

    @LatestOperationState.setter
    def LatestOperationState(self, LatestOperationState):
        self._LatestOperationState = LatestOperationState

    @property
    def LatestOperationRequestId(self):
        return self._LatestOperationRequestId

    @LatestOperationRequestId.setter
    def LatestOperationRequestId(self, LatestOperationRequestId):
        self._LatestOperationRequestId = LatestOperationRequestId

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ExpiredTime(self):
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def IsolatedTime(self):
        return self._IsolatedTime

    @IsolatedTime.setter
    def IsolatedTime(self, IsolatedTime):
        self._IsolatedTime = IsolatedTime

    @property
    def DiskBackupCount(self):
        return self._DiskBackupCount

    @DiskBackupCount.setter
    def DiskBackupCount(self, DiskBackupCount):
        self._DiskBackupCount = DiskBackupCount

    @property
    def DiskBackupQuota(self):
        return self._DiskBackupQuota

    @DiskBackupQuota.setter
    def DiskBackupQuota(self, DiskBackupQuota):
        self._DiskBackupQuota = DiskBackupQuota


    def _deserialize(self, params):
        self._DiskId = params.get("DiskId")
        self._InstanceId = params.get("InstanceId")
        self._Zone = params.get("Zone")
        self._DiskName = params.get("DiskName")
        self._DiskUsage = params.get("DiskUsage")
        self._DiskType = params.get("DiskType")
        self._DiskChargeType = params.get("DiskChargeType")
        self._DiskSize = params.get("DiskSize")
        self._RenewFlag = params.get("RenewFlag")
        self._DiskState = params.get("DiskState")
        self._Attached = params.get("Attached")
        self._DeleteWithInstance = params.get("DeleteWithInstance")
        self._LatestOperation = params.get("LatestOperation")
        self._LatestOperationState = params.get("LatestOperationState")
        self._LatestOperationRequestId = params.get("LatestOperationRequestId")
        self._CreatedTime = params.get("CreatedTime")
        self._ExpiredTime = params.get("ExpiredTime")
        self._IsolatedTime = params.get("IsolatedTime")
        self._DiskBackupCount = params.get("DiskBackupCount")
        self._DiskBackupQuota = params.get("DiskBackupQuota")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiskChargePrepaid(AbstractModel):
    """Parameter settings for the monthly subscribed cloud disk

    """

    def __init__(self):
        r"""
        :param _Period: Purchase duration.
        :type Period: int
        :param _RenewFlag: Whether Auto-Renewal is enabled 
        :type RenewFlag: str
        :param _TimeUnit: Purchase duration unit. Default value: "m" (month)
        :type TimeUnit: str
        """
        self._Period = None
        self._RenewFlag = None
        self._TimeUnit = None

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def TimeUnit(self):
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit


    def _deserialize(self, params):
        self._Period = params.get("Period")
        self._RenewFlag = params.get("RenewFlag")
        self._TimeUnit = params.get("TimeUnit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiskConfig(AbstractModel):
    """Cloud disk configuration

    """

    def __init__(self):
        r"""
        :param _Zone: Availability zone.
        :type Zone: str
        :param _DiskType: Cloud disk type.
        :type DiskType: str
        :param _DiskSalesState: Cloud disk sale status.
        :type DiskSalesState: str
        :param _MaxDiskSize: Maximum cloud disk size.
        :type MaxDiskSize: int
        :param _MinDiskSize: Minimum cloud disk size.
        :type MinDiskSize: int
        :param _DiskStepSize: Cloud disk increment.
        :type DiskStepSize: int
        """
        self._Zone = None
        self._DiskType = None
        self._DiskSalesState = None
        self._MaxDiskSize = None
        self._MinDiskSize = None
        self._DiskStepSize = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSalesState(self):
        return self._DiskSalesState

    @DiskSalesState.setter
    def DiskSalesState(self, DiskSalesState):
        self._DiskSalesState = DiskSalesState

    @property
    def MaxDiskSize(self):
        return self._MaxDiskSize

    @MaxDiskSize.setter
    def MaxDiskSize(self, MaxDiskSize):
        self._MaxDiskSize = MaxDiskSize

    @property
    def MinDiskSize(self):
        return self._MinDiskSize

    @MinDiskSize.setter
    def MinDiskSize(self, MinDiskSize):
        self._MinDiskSize = MinDiskSize

    @property
    def DiskStepSize(self):
        return self._DiskStepSize

    @DiskStepSize.setter
    def DiskStepSize(self, DiskStepSize):
        self._DiskStepSize = DiskStepSize


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._DiskType = params.get("DiskType")
        self._DiskSalesState = params.get("DiskSalesState")
        self._MaxDiskSize = params.get("MaxDiskSize")
        self._MinDiskSize = params.get("MinDiskSize")
        self._DiskStepSize = params.get("DiskStepSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiskDeniedActions(AbstractModel):
    """List of operation limits of disks.

    """

    def __init__(self):
        r"""
        :param _DiskId: Cloud disk ID.
        :type DiskId: str
        :param _DeniedActions: List of operation limits.
        :type DeniedActions: list of DeniedAction
        """
        self._DiskId = None
        self._DeniedActions = None

    @property
    def DiskId(self):
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def DeniedActions(self):
        return self._DeniedActions

    @DeniedActions.setter
    def DeniedActions(self, DeniedActions):
        self._DeniedActions = DeniedActions


    def _deserialize(self, params):
        self._DiskId = params.get("DiskId")
        if params.get("DeniedActions") is not None:
            self._DeniedActions = []
            for item in params.get("DeniedActions"):
                obj = DeniedAction()
                obj._deserialize(item)
                self._DeniedActions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiskPrice(AbstractModel):
    """Cloud disk price

    """

    def __init__(self):
        r"""
        :param _OriginalDiskPrice: Cloud disk unit price.
        :type OriginalDiskPrice: float
        :param _OriginalPrice: Total cloud disk price.
        :type OriginalPrice: float
        :param _Discount: Discount.
        :type Discount: float
        :param _DiscountPrice: Discounted total price.
        :type DiscountPrice: float
        :param _DetailPrices: Detailed billing items
        :type DetailPrices: list of DetailPrice
        """
        self._OriginalDiskPrice = None
        self._OriginalPrice = None
        self._Discount = None
        self._DiscountPrice = None
        self._DetailPrices = None

    @property
    def OriginalDiskPrice(self):
        return self._OriginalDiskPrice

    @OriginalDiskPrice.setter
    def OriginalDiskPrice(self, OriginalDiskPrice):
        self._OriginalDiskPrice = OriginalDiskPrice

    @property
    def OriginalPrice(self):
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def Discount(self):
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount

    @property
    def DiscountPrice(self):
        return self._DiscountPrice

    @DiscountPrice.setter
    def DiscountPrice(self, DiscountPrice):
        self._DiscountPrice = DiscountPrice

    @property
    def DetailPrices(self):
        return self._DetailPrices

    @DetailPrices.setter
    def DetailPrices(self, DetailPrices):
        self._DetailPrices = DetailPrices


    def _deserialize(self, params):
        self._OriginalDiskPrice = params.get("OriginalDiskPrice")
        self._OriginalPrice = params.get("OriginalPrice")
        self._Discount = params.get("Discount")
        self._DiscountPrice = params.get("DiscountPrice")
        if params.get("DetailPrices") is not None:
            self._DetailPrices = []
            for item in params.get("DetailPrices"):
                obj = DetailPrice()
                obj._deserialize(item)
                self._DetailPrices.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiskReturnable(AbstractModel):
    """Details of the returnable cloud disk

    """

    def __init__(self):
        r"""
        :param _DiskId: Cloud disk ID.
        :type DiskId: str
        :param _IsReturnable: Whether the cloud disk can be returned.
        :type IsReturnable: bool
        :param _ReturnFailCode: Error code of cloud disk return failure.
        :type ReturnFailCode: int
        :param _ReturnFailMessage: Error message of cloud disk return failure.
        :type ReturnFailMessage: str
        """
        self._DiskId = None
        self._IsReturnable = None
        self._ReturnFailCode = None
        self._ReturnFailMessage = None

    @property
    def DiskId(self):
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def IsReturnable(self):
        return self._IsReturnable

    @IsReturnable.setter
    def IsReturnable(self, IsReturnable):
        self._IsReturnable = IsReturnable

    @property
    def ReturnFailCode(self):
        return self._ReturnFailCode

    @ReturnFailCode.setter
    def ReturnFailCode(self, ReturnFailCode):
        self._ReturnFailCode = ReturnFailCode

    @property
    def ReturnFailMessage(self):
        return self._ReturnFailMessage

    @ReturnFailMessage.setter
    def ReturnFailMessage(self, ReturnFailMessage):
        self._ReturnFailMessage = ReturnFailMessage


    def _deserialize(self, params):
        self._DiskId = params.get("DiskId")
        self._IsReturnable = params.get("IsReturnable")
        self._ReturnFailCode = params.get("ReturnFailCode")
        self._ReturnFailMessage = params.get("ReturnFailMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DockerContainerConfiguration(AbstractModel):
    """Configuration used to create Docker containers

    """

    def __init__(self):
        r"""
        :param _ContainerImage: Container image address
        :type ContainerImage: str
        :param _ContainerName: Container name
        :type ContainerName: str
        :param _Envs: List of environment variables
        :type Envs: list of ContainerEnv
        :param _PublishPorts: List of mappings of container ports and host ports
        :type PublishPorts: list of DockerContainerPublishPort
        :param _Volumes: List of container mount volumes
        :type Volumes: list of DockerContainerVolume
        :param _Command: The command to run
        :type Command: str
        """
        self._ContainerImage = None
        self._ContainerName = None
        self._Envs = None
        self._PublishPorts = None
        self._Volumes = None
        self._Command = None

    @property
    def ContainerImage(self):
        return self._ContainerImage

    @ContainerImage.setter
    def ContainerImage(self, ContainerImage):
        self._ContainerImage = ContainerImage

    @property
    def ContainerName(self):
        return self._ContainerName

    @ContainerName.setter
    def ContainerName(self, ContainerName):
        self._ContainerName = ContainerName

    @property
    def Envs(self):
        return self._Envs

    @Envs.setter
    def Envs(self, Envs):
        self._Envs = Envs

    @property
    def PublishPorts(self):
        return self._PublishPorts

    @PublishPorts.setter
    def PublishPorts(self, PublishPorts):
        self._PublishPorts = PublishPorts

    @property
    def Volumes(self):
        return self._Volumes

    @Volumes.setter
    def Volumes(self, Volumes):
        self._Volumes = Volumes

    @property
    def Command(self):
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command


    def _deserialize(self, params):
        self._ContainerImage = params.get("ContainerImage")
        self._ContainerName = params.get("ContainerName")
        if params.get("Envs") is not None:
            self._Envs = []
            for item in params.get("Envs"):
                obj = ContainerEnv()
                obj._deserialize(item)
                self._Envs.append(obj)
        if params.get("PublishPorts") is not None:
            self._PublishPorts = []
            for item in params.get("PublishPorts"):
                obj = DockerContainerPublishPort()
                obj._deserialize(item)
                self._PublishPorts.append(obj)
        if params.get("Volumes") is not None:
            self._Volumes = []
            for item in params.get("Volumes"):
                obj = DockerContainerVolume()
                obj._deserialize(item)
                self._Volumes.append(obj)
        self._Command = params.get("Command")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DockerContainerPublishPort(AbstractModel):
    """Port mapping of the Docker container

    """

    def __init__(self):
        r"""
        :param _HostPort: Host port
        :type HostPort: int
        :param _ContainerPort: Container port
        :type ContainerPort: int
        :param _Ip: External IP. It defaults to 0.0.0.0.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Ip: str
        :param _Protocol: The protocol defaults to `tcp`. Valid values: `tcp`, `udp` and `sctp`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Protocol: str
        """
        self._HostPort = None
        self._ContainerPort = None
        self._Ip = None
        self._Protocol = None

    @property
    def HostPort(self):
        return self._HostPort

    @HostPort.setter
    def HostPort(self, HostPort):
        self._HostPort = HostPort

    @property
    def ContainerPort(self):
        return self._ContainerPort

    @ContainerPort.setter
    def ContainerPort(self, ContainerPort):
        self._ContainerPort = ContainerPort

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol


    def _deserialize(self, params):
        self._HostPort = params.get("HostPort")
        self._ContainerPort = params.get("ContainerPort")
        self._Ip = params.get("Ip")
        self._Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DockerContainerVolume(AbstractModel):
    """Docker container mount volume

    """

    def __init__(self):
        r"""
        :param _ContainerPath: Container path
        :type ContainerPath: str
        :param _HostPath: Host path
        :type HostPath: str
        """
        self._ContainerPath = None
        self._HostPath = None

    @property
    def ContainerPath(self):
        return self._ContainerPath

    @ContainerPath.setter
    def ContainerPath(self, ContainerPath):
        self._ContainerPath = ContainerPath

    @property
    def HostPath(self):
        return self._HostPath

    @HostPath.setter
    def HostPath(self, HostPath):
        self._HostPath = HostPath


    def _deserialize(self, params):
        self._ContainerPath = params.get("ContainerPath")
        self._HostPath = params.get("HostPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """>Key-Value pair filter for conditional filtering queries, such as filtering name
    > * If there are multiple `Filter` parameters, the relationship among them is the logical `AND`.
    > * If there are multiple `Values` for the same `Filter`, the relationship among the `Values` is the logical `OR`.
    >
    > Taking the `Filter` in the `DescribeInstances` API as an example, you can use the following filters to query the instance whose name (`instance-name`) is `test` ***and*** private IP (`private-ip-address`) is 10.10.10.10:
    ```
    Filters.0.Name=instance-name
    &Filters.0.Values.0=test
    &Filters.1.Name=private-ip-address
    &Filters.1.Values.0=10.10.10.10
    ```

    """

    def __init__(self):
        r"""
        :param _Name: Field to be filtered.
        :type Name: str
        :param _Values: Filter value of field.
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FirewallRule(AbstractModel):
    """Firewall rule information.

    """

    def __init__(self):
        r"""
        :param _Protocol: Protocol. Valid values: TCP, UDP, ICMP, ALL.
        :type Protocol: str
        :param _Port: Port. Valid values: ALL, one single port, multiple ports separated by commas, or port range indicated by a minus sign
        :type Port: str
        :param _CidrBlock: IP range or IP (mutually exclusive). Default value: 0.0.0.0/0, which indicates all sources.
        :type CidrBlock: str
        :param _Action: Valid values: ACCEPT, DROP. Default value: ACCEPT.
        :type Action: str
        :param _FirewallRuleDescription: Firewall rule description.
        :type FirewallRuleDescription: str
        """
        self._Protocol = None
        self._Port = None
        self._CidrBlock = None
        self._Action = None
        self._FirewallRuleDescription = None

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def CidrBlock(self):
        return self._CidrBlock

    @CidrBlock.setter
    def CidrBlock(self, CidrBlock):
        self._CidrBlock = CidrBlock

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def FirewallRuleDescription(self):
        return self._FirewallRuleDescription

    @FirewallRuleDescription.setter
    def FirewallRuleDescription(self, FirewallRuleDescription):
        self._FirewallRuleDescription = FirewallRuleDescription


    def _deserialize(self, params):
        self._Protocol = params.get("Protocol")
        self._Port = params.get("Port")
        self._CidrBlock = params.get("CidrBlock")
        self._Action = params.get("Action")
        self._FirewallRuleDescription = params.get("FirewallRuleDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FirewallRuleInfo(AbstractModel):
    """Firewall rule details.

    """

    def __init__(self):
        r"""
        :param _AppType: Application type. Valid values: custom, HTTP (80), HTTPS (443), Linux login (22), Windows login (3389), MySQL (3306), SQL Server (1433), all TCP ports, all UDP ports, Ping-ICMP, ALL.
        :type AppType: str
        :param _Protocol: Protocol. Valid values: TCP, UDP, ICMP, ALL.
        :type Protocol: str
        :param _Port: Port. Valid values: ALL, one single port, multiple ports separated by commas, or port range indicated by a minus sign
        :type Port: str
        :param _CidrBlock: IP range or IP (mutually exclusive). Default value: 0.0.0.0/0, which indicates all sources.
        :type CidrBlock: str
        :param _Action: Valid values: ACCEPT, DROP. Default value: ACCEPT.
        :type Action: str
        :param _FirewallRuleDescription: Firewall rule description.
        :type FirewallRuleDescription: str
        """
        self._AppType = None
        self._Protocol = None
        self._Port = None
        self._CidrBlock = None
        self._Action = None
        self._FirewallRuleDescription = None

    @property
    def AppType(self):
        return self._AppType

    @AppType.setter
    def AppType(self, AppType):
        self._AppType = AppType

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def CidrBlock(self):
        return self._CidrBlock

    @CidrBlock.setter
    def CidrBlock(self, CidrBlock):
        self._CidrBlock = CidrBlock

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def FirewallRuleDescription(self):
        return self._FirewallRuleDescription

    @FirewallRuleDescription.setter
    def FirewallRuleDescription(self, FirewallRuleDescription):
        self._FirewallRuleDescription = FirewallRuleDescription


    def _deserialize(self, params):
        self._AppType = params.get("AppType")
        self._Protocol = params.get("Protocol")
        self._Port = params.get("Port")
        self._CidrBlock = params.get("CidrBlock")
        self._Action = params.get("Action")
        self._FirewallRuleDescription = params.get("FirewallRuleDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GeneralResourceQuota(AbstractModel):
    """General resource quota information.


    """

    def __init__(self):
        r"""
        :param _ResourceName: Resource name.
        :type ResourceName: str
        :param _ResourceQuotaAvailable: Number of available resources.
        :type ResourceQuotaAvailable: int
        :param _ResourceQuotaTotal: Total number of resources.
        :type ResourceQuotaTotal: int
        """
        self._ResourceName = None
        self._ResourceQuotaAvailable = None
        self._ResourceQuotaTotal = None

    @property
    def ResourceName(self):
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def ResourceQuotaAvailable(self):
        return self._ResourceQuotaAvailable

    @ResourceQuotaAvailable.setter
    def ResourceQuotaAvailable(self, ResourceQuotaAvailable):
        self._ResourceQuotaAvailable = ResourceQuotaAvailable

    @property
    def ResourceQuotaTotal(self):
        return self._ResourceQuotaTotal

    @ResourceQuotaTotal.setter
    def ResourceQuotaTotal(self, ResourceQuotaTotal):
        self._ResourceQuotaTotal = ResourceQuotaTotal


    def _deserialize(self, params):
        self._ResourceName = params.get("ResourceName")
        self._ResourceQuotaAvailable = params.get("ResourceQuotaAvailable")
        self._ResourceQuotaTotal = params.get("ResourceQuotaTotal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportKeyPairRequest(AbstractModel):
    """ImportKeyPair request structure.

    """

    def __init__(self):
        r"""
        :param _KeyName: Key pair name, which can contain up to 25 digits, letters, and underscores.
        :type KeyName: str
        :param _PublicKey: Public key content of the key pair, which is in the OpenSSH RSA format.
        :type PublicKey: str
        """
        self._KeyName = None
        self._PublicKey = None

    @property
    def KeyName(self):
        return self._KeyName

    @KeyName.setter
    def KeyName(self, KeyName):
        self._KeyName = KeyName

    @property
    def PublicKey(self):
        return self._PublicKey

    @PublicKey.setter
    def PublicKey(self, PublicKey):
        self._PublicKey = PublicKey


    def _deserialize(self, params):
        self._KeyName = params.get("KeyName")
        self._PublicKey = params.get("PublicKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportKeyPairResponse(AbstractModel):
    """ImportKeyPair response structure.

    """

    def __init__(self):
        r"""
        :param _KeyId: Key pair ID.
        :type KeyId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._KeyId = None
        self._RequestId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._RequestId = params.get("RequestId")


class InquirePriceCreateBlueprintRequest(AbstractModel):
    """InquirePriceCreateBlueprint request structure.

    """

    def __init__(self):
        r"""
        :param _BlueprintCount: Number of custom images. Default value: 1.
        :type BlueprintCount: int
        """
        self._BlueprintCount = None

    @property
    def BlueprintCount(self):
        return self._BlueprintCount

    @BlueprintCount.setter
    def BlueprintCount(self, BlueprintCount):
        self._BlueprintCount = BlueprintCount


    def _deserialize(self, params):
        self._BlueprintCount = params.get("BlueprintCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceCreateBlueprintResponse(AbstractModel):
    """InquirePriceCreateBlueprint response structure.

    """

    def __init__(self):
        r"""
        :param _BlueprintPrice: Custom image price.
        :type BlueprintPrice: :class:`tencentcloud.lighthouse.v20200324.models.BlueprintPrice`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BlueprintPrice = None
        self._RequestId = None

    @property
    def BlueprintPrice(self):
        return self._BlueprintPrice

    @BlueprintPrice.setter
    def BlueprintPrice(self, BlueprintPrice):
        self._BlueprintPrice = BlueprintPrice

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("BlueprintPrice") is not None:
            self._BlueprintPrice = BlueprintPrice()
            self._BlueprintPrice._deserialize(params.get("BlueprintPrice"))
        self._RequestId = params.get("RequestId")


class InquirePriceCreateDisksRequest(AbstractModel):
    """InquirePriceCreateDisks request structure.

    """

    def __init__(self):
        r"""
        :param _DiskSize: Cloud disk size in GB.
        :type DiskSize: int
        :param _DiskType: Cloud disk media type. Valid values: "CLOUD_PREMIUM" (premium cloud storage), "CLOUD_SSD" (SSD cloud disk).
        :type DiskType: str
        :param _DiskChargePrepaid: Parameter settings for purchasing the monthly subscribed cloud disk.
        :type DiskChargePrepaid: :class:`tencentcloud.lighthouse.v20200324.models.DiskChargePrepaid`
        :param _DiskCount: Number of cloud disks. Default value: 1.
        :type DiskCount: int
        :param _DiskBackupQuota: Specify the quota of disk backups. No quota if it’s left empty. Only one quota is allowed.
        :type DiskBackupQuota: int
        """
        self._DiskSize = None
        self._DiskType = None
        self._DiskChargePrepaid = None
        self._DiskCount = None
        self._DiskBackupQuota = None

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskChargePrepaid(self):
        return self._DiskChargePrepaid

    @DiskChargePrepaid.setter
    def DiskChargePrepaid(self, DiskChargePrepaid):
        self._DiskChargePrepaid = DiskChargePrepaid

    @property
    def DiskCount(self):
        return self._DiskCount

    @DiskCount.setter
    def DiskCount(self, DiskCount):
        self._DiskCount = DiskCount

    @property
    def DiskBackupQuota(self):
        return self._DiskBackupQuota

    @DiskBackupQuota.setter
    def DiskBackupQuota(self, DiskBackupQuota):
        self._DiskBackupQuota = DiskBackupQuota


    def _deserialize(self, params):
        self._DiskSize = params.get("DiskSize")
        self._DiskType = params.get("DiskType")
        if params.get("DiskChargePrepaid") is not None:
            self._DiskChargePrepaid = DiskChargePrepaid()
            self._DiskChargePrepaid._deserialize(params.get("DiskChargePrepaid"))
        self._DiskCount = params.get("DiskCount")
        self._DiskBackupQuota = params.get("DiskBackupQuota")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceCreateDisksResponse(AbstractModel):
    """InquirePriceCreateDisks response structure.

    """

    def __init__(self):
        r"""
        :param _DiskPrice: Cloud disk price.
        :type DiskPrice: :class:`tencentcloud.lighthouse.v20200324.models.DiskPrice`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DiskPrice = None
        self._RequestId = None

    @property
    def DiskPrice(self):
        return self._DiskPrice

    @DiskPrice.setter
    def DiskPrice(self, DiskPrice):
        self._DiskPrice = DiskPrice

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DiskPrice") is not None:
            self._DiskPrice = DiskPrice()
            self._DiskPrice._deserialize(params.get("DiskPrice"))
        self._RequestId = params.get("RequestId")


class InquirePriceCreateInstancesRequest(AbstractModel):
    """InquirePriceCreateInstances request structure.

    """

    def __init__(self):
        r"""
        :param _BundleId: Instance package ID.
        :type BundleId: str
        :param _InstanceChargePrepaid: Parameter setting for prepaid mode. This parameter can specify the purchase period, whether to enable auto-renewal, and other attributes of the monthly subscribed instances.
        :type InstanceChargePrepaid: :class:`tencentcloud.lighthouse.v20200324.models.InstanceChargePrepaid`
        :param _InstanceCount: Number of instances to be created. Default value: 1.
        :type InstanceCount: int
        :param _BlueprintId: Application image ID, which is required if a paid application image is used and can be obtained from the `BlueprintId` returned by the [DescribeBlueprints](https://intl.cloud.tencent.com/document/product/1207/47689?from_cn_redirect=1) API.
        :type BlueprintId: str
        """
        self._BundleId = None
        self._InstanceChargePrepaid = None
        self._InstanceCount = None
        self._BlueprintId = None

    @property
    def BundleId(self):
        return self._BundleId

    @BundleId.setter
    def BundleId(self, BundleId):
        self._BundleId = BundleId

    @property
    def InstanceChargePrepaid(self):
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid

    @property
    def InstanceCount(self):
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def BlueprintId(self):
        return self._BlueprintId

    @BlueprintId.setter
    def BlueprintId(self, BlueprintId):
        self._BlueprintId = BlueprintId


    def _deserialize(self, params):
        self._BundleId = params.get("BundleId")
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self._InstanceCount = params.get("InstanceCount")
        self._BlueprintId = params.get("BlueprintId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceCreateInstancesResponse(AbstractModel):
    """InquirePriceCreateInstances response structure.

    """

    def __init__(self):
        r"""
        :param _Price: Price query information.
        :type Price: :class:`tencentcloud.lighthouse.v20200324.models.Price`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Price = None
        self._RequestId = None

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self._Price = Price()
            self._Price._deserialize(params.get("Price"))
        self._RequestId = params.get("RequestId")


class InquirePriceRenewDisksRequest(AbstractModel):
    """InquirePriceRenewDisks request structure.

    """

    def __init__(self):
        r"""
        :param _DiskIds: List of cloud disk IDs.
        :type DiskIds: list of str
        :param _RenewDiskChargePrepaid: Parameter settings for renewing the monthly subscribed cloud disk.
        :type RenewDiskChargePrepaid: :class:`tencentcloud.lighthouse.v20200324.models.RenewDiskChargePrepaid`
        """
        self._DiskIds = None
        self._RenewDiskChargePrepaid = None

    @property
    def DiskIds(self):
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds

    @property
    def RenewDiskChargePrepaid(self):
        return self._RenewDiskChargePrepaid

    @RenewDiskChargePrepaid.setter
    def RenewDiskChargePrepaid(self, RenewDiskChargePrepaid):
        self._RenewDiskChargePrepaid = RenewDiskChargePrepaid


    def _deserialize(self, params):
        self._DiskIds = params.get("DiskIds")
        if params.get("RenewDiskChargePrepaid") is not None:
            self._RenewDiskChargePrepaid = RenewDiskChargePrepaid()
            self._RenewDiskChargePrepaid._deserialize(params.get("RenewDiskChargePrepaid"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceRenewDisksResponse(AbstractModel):
    """InquirePriceRenewDisks response structure.

    """

    def __init__(self):
        r"""
        :param _DiskPrice: Cloud disk price.
        :type DiskPrice: :class:`tencentcloud.lighthouse.v20200324.models.DiskPrice`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DiskPrice = None
        self._RequestId = None

    @property
    def DiskPrice(self):
        return self._DiskPrice

    @DiskPrice.setter
    def DiskPrice(self, DiskPrice):
        self._DiskPrice = DiskPrice

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DiskPrice") is not None:
            self._DiskPrice = DiskPrice()
            self._DiskPrice._deserialize(params.get("DiskPrice"))
        self._RequestId = params.get("RequestId")


class InquirePriceRenewInstancesRequest(AbstractModel):
    """InquirePriceRenewInstances request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: IDs of the instances to be renewed. Each request can contain up to 50 instances at a time. You can get an instance ID from the `InstanceId` returned by the [DescribeInstances](https://intl.cloud.tencent.com/document/api/1207/47573?from_cn_redirect=1) API.
        :type InstanceIds: list of str
        :param _InstanceChargePrepaid: Parameter setting for prepaid mode. This parameter can specify the renewal period, whether to enable auto-renewal, and other attributes of the monthly subscribed instances.
        :type InstanceChargePrepaid: :class:`tencentcloud.lighthouse.v20200324.models.InstanceChargePrepaid`
        :param _RenewDataDisk: Whether to renew the data disk. Default: `false`.
        :type RenewDataDisk: bool
        :param _AlignInstanceExpiredTime: Whether to align the data disk expiration with the instance expiration time. Default: `false`.
        :type AlignInstanceExpiredTime: bool
        """
        self._InstanceIds = None
        self._InstanceChargePrepaid = None
        self._RenewDataDisk = None
        self._AlignInstanceExpiredTime = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def InstanceChargePrepaid(self):
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid

    @property
    def RenewDataDisk(self):
        return self._RenewDataDisk

    @RenewDataDisk.setter
    def RenewDataDisk(self, RenewDataDisk):
        self._RenewDataDisk = RenewDataDisk

    @property
    def AlignInstanceExpiredTime(self):
        return self._AlignInstanceExpiredTime

    @AlignInstanceExpiredTime.setter
    def AlignInstanceExpiredTime(self, AlignInstanceExpiredTime):
        self._AlignInstanceExpiredTime = AlignInstanceExpiredTime


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self._RenewDataDisk = params.get("RenewDataDisk")
        self._AlignInstanceExpiredTime = params.get("AlignInstanceExpiredTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceRenewInstancesResponse(AbstractModel):
    """InquirePriceRenewInstances response structure.

    """

    def __init__(self):
        r"""
        :param _Price: Price information. It defaults to the price information of the first instance in the list.
        :type Price: :class:`tencentcloud.lighthouse.v20200324.models.Price`
        :param _DataDiskPriceSet: List of data disk price information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DataDiskPriceSet: list of DataDiskPrice
        :param _InstancePriceDetailSet: Price list of the instances to be renewed.
Note: This field may return `null`, indicating that no valid value was found.
        :type InstancePriceDetailSet: list of InstancePriceDetail
        :param _TotalPrice: Total price
        :type TotalPrice: :class:`tencentcloud.lighthouse.v20200324.models.TotalPrice`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Price = None
        self._DataDiskPriceSet = None
        self._InstancePriceDetailSet = None
        self._TotalPrice = None
        self._RequestId = None

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def DataDiskPriceSet(self):
        return self._DataDiskPriceSet

    @DataDiskPriceSet.setter
    def DataDiskPriceSet(self, DataDiskPriceSet):
        self._DataDiskPriceSet = DataDiskPriceSet

    @property
    def InstancePriceDetailSet(self):
        return self._InstancePriceDetailSet

    @InstancePriceDetailSet.setter
    def InstancePriceDetailSet(self, InstancePriceDetailSet):
        self._InstancePriceDetailSet = InstancePriceDetailSet

    @property
    def TotalPrice(self):
        return self._TotalPrice

    @TotalPrice.setter
    def TotalPrice(self, TotalPrice):
        self._TotalPrice = TotalPrice

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self._Price = Price()
            self._Price._deserialize(params.get("Price"))
        if params.get("DataDiskPriceSet") is not None:
            self._DataDiskPriceSet = []
            for item in params.get("DataDiskPriceSet"):
                obj = DataDiskPrice()
                obj._deserialize(item)
                self._DataDiskPriceSet.append(obj)
        if params.get("InstancePriceDetailSet") is not None:
            self._InstancePriceDetailSet = []
            for item in params.get("InstancePriceDetailSet"):
                obj = InstancePriceDetail()
                obj._deserialize(item)
                self._InstancePriceDetailSet.append(obj)
        if params.get("TotalPrice") is not None:
            self._TotalPrice = TotalPrice()
            self._TotalPrice._deserialize(params.get("TotalPrice"))
        self._RequestId = params.get("RequestId")


class Instance(AbstractModel):
    """Instance information.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _BundleId: Package ID.
        :type BundleId: str
        :param _BlueprintId: Image ID.
        :type BlueprintId: str
        :param _CPU: Number of instance CPU cores.
        :type CPU: int
        :param _Memory: Instance memory capacity in GB.
        :type Memory: int
        :param _InstanceName: Instance name.
        :type InstanceName: str
        :param _InstanceChargeType: Instance billing mode. Valid values: 
PREPAID: prepaid (i.e., monthly subscription).
        :type InstanceChargeType: str
        :param _SystemDisk: Instance system disk information.
        :type SystemDisk: :class:`tencentcloud.lighthouse.v20200324.models.SystemDisk`
        :param _PrivateAddresses: Private IP of instance primary ENI. 
Note: this field may return null, indicating that no valid values can be obtained.
        :type PrivateAddresses: list of str
        :param _PublicAddresses: Public IP of instance primary ENI. 
Note: this field may return null, indicating that no valid values can be obtained.
        :type PublicAddresses: list of str
        :param _InternetAccessible: Instance bandwidth information.
        :type InternetAccessible: :class:`tencentcloud.lighthouse.v20200324.models.InternetAccessible`
        :param _RenewFlag: Auto-Renewal flag. Valid values: 
NOTIFY_AND_MANUAL_RENEW: notify upon expiration but do not renew automatically  
NOTIFY_AND_AUTO_RENEW: notify upon expiration and renew automatically.
        :type RenewFlag: str
        :param _LoginSettings: Instance login settings.
        :type LoginSettings: :class:`tencentcloud.lighthouse.v20200324.models.LoginSettings`
        :param _InstanceState: Instance status. Valid values: 
<li>PENDING: Creating</li><li>LAUNCH_FAILED: Failed to create</li><li>RUNNING: Running</li><li>STOPPED: Shut down</li><li>STARTING: Starting up</li><li>STOPPING: Shutting down</li><li>REBOOTING: Restarting</li><li>SHUTDOWN: Shutdown and to be terminated</li><li>TERMINATING: Terminating</li><li>DELETING: Deleting</li><li>FREEZING: Frozen</li><li>ENTER_RESCUE_MODE: Entering the rescue mode</li><li>RESCUE_MODE: Rescue mode</li><li>EXIT_RESCUE_MODE: Exiting from the rescue mode</li>
        :type InstanceState: str
        :param _Uuid: Globally unique ID of instance.
        :type Uuid: str
        :param _LatestOperation: Last instance operation, such as `StopInstances` and `ResetInstance`. Note: this field may return null, indicating that no valid values can be obtained.
        :type LatestOperation: str
        :param _LatestOperationState: Last instance operation status. Valid values: 
SUCCESS: operation succeeded 
OPERATING: the operation is being executed 
FAILED: operation failed 
Note: this field may return null, indicating that no valid values can be obtained.
        :type LatestOperationState: str
        :param _LatestOperationRequestId: Unique request ID for the last operation of the instance. 
Note: this field may return null, indicating that no valid values can be obtained.
        :type LatestOperationRequestId: str
        :param _IsolatedTime: Isolation time according to ISO 8601 standard. UTC time is used. 
Format: YYYY-MM-DDThh:mm:ssZ.
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsolatedTime: str
        :param _CreatedTime: Creation time according to ISO 8601 standard. UTC time is used. 
Format: YYYY-MM-DDThh:mm:ssZ.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreatedTime: str
        :param _ExpiredTime: Expiration time according to ISO 8601 standard. UTC time is used. 
Format: YYYY-MM-DDThh:mm:ssZ.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ExpiredTime: str
        :param _PlatformType: OS type, such as LINUX_UNIX and WINDOWS.
        :type PlatformType: str
        :param _Platform: OS type.
        :type Platform: str
        :param _OsName: OS name.
        :type OsName: str
        :param _Zone: AZ.
        :type Zone: str
        :param _Tags: The list of tags associated with the instance
        :type Tags: list of Tag
        :param _InstanceRestrictState: Obtain instance status
<li>NORMAL: The instance is normal</li><li>NETWORK_RESTRICT: The instance is blocked from the network.</li>
        :type InstanceRestrictState: str
        """
        self._InstanceId = None
        self._BundleId = None
        self._BlueprintId = None
        self._CPU = None
        self._Memory = None
        self._InstanceName = None
        self._InstanceChargeType = None
        self._SystemDisk = None
        self._PrivateAddresses = None
        self._PublicAddresses = None
        self._InternetAccessible = None
        self._RenewFlag = None
        self._LoginSettings = None
        self._InstanceState = None
        self._Uuid = None
        self._LatestOperation = None
        self._LatestOperationState = None
        self._LatestOperationRequestId = None
        self._IsolatedTime = None
        self._CreatedTime = None
        self._ExpiredTime = None
        self._PlatformType = None
        self._Platform = None
        self._OsName = None
        self._Zone = None
        self._Tags = None
        self._InstanceRestrictState = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BundleId(self):
        return self._BundleId

    @BundleId.setter
    def BundleId(self, BundleId):
        self._BundleId = BundleId

    @property
    def BlueprintId(self):
        return self._BlueprintId

    @BlueprintId.setter
    def BlueprintId(self, BlueprintId):
        self._BlueprintId = BlueprintId

    @property
    def CPU(self):
        return self._CPU

    @CPU.setter
    def CPU(self, CPU):
        self._CPU = CPU

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def SystemDisk(self):
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def PrivateAddresses(self):
        return self._PrivateAddresses

    @PrivateAddresses.setter
    def PrivateAddresses(self, PrivateAddresses):
        self._PrivateAddresses = PrivateAddresses

    @property
    def PublicAddresses(self):
        return self._PublicAddresses

    @PublicAddresses.setter
    def PublicAddresses(self, PublicAddresses):
        self._PublicAddresses = PublicAddresses

    @property
    def InternetAccessible(self):
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def LoginSettings(self):
        return self._LoginSettings

    @LoginSettings.setter
    def LoginSettings(self, LoginSettings):
        self._LoginSettings = LoginSettings

    @property
    def InstanceState(self):
        return self._InstanceState

    @InstanceState.setter
    def InstanceState(self, InstanceState):
        self._InstanceState = InstanceState

    @property
    def Uuid(self):
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def LatestOperation(self):
        return self._LatestOperation

    @LatestOperation.setter
    def LatestOperation(self, LatestOperation):
        self._LatestOperation = LatestOperation

    @property
    def LatestOperationState(self):
        return self._LatestOperationState

    @LatestOperationState.setter
    def LatestOperationState(self, LatestOperationState):
        self._LatestOperationState = LatestOperationState

    @property
    def LatestOperationRequestId(self):
        return self._LatestOperationRequestId

    @LatestOperationRequestId.setter
    def LatestOperationRequestId(self, LatestOperationRequestId):
        self._LatestOperationRequestId = LatestOperationRequestId

    @property
    def IsolatedTime(self):
        return self._IsolatedTime

    @IsolatedTime.setter
    def IsolatedTime(self, IsolatedTime):
        self._IsolatedTime = IsolatedTime

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ExpiredTime(self):
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def PlatformType(self):
        return self._PlatformType

    @PlatformType.setter
    def PlatformType(self, PlatformType):
        self._PlatformType = PlatformType

    @property
    def Platform(self):
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def OsName(self):
        return self._OsName

    @OsName.setter
    def OsName(self, OsName):
        self._OsName = OsName

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def InstanceRestrictState(self):
        return self._InstanceRestrictState

    @InstanceRestrictState.setter
    def InstanceRestrictState(self, InstanceRestrictState):
        self._InstanceRestrictState = InstanceRestrictState


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BundleId = params.get("BundleId")
        self._BlueprintId = params.get("BlueprintId")
        self._CPU = params.get("CPU")
        self._Memory = params.get("Memory")
        self._InstanceName = params.get("InstanceName")
        self._InstanceChargeType = params.get("InstanceChargeType")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = SystemDisk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        self._PrivateAddresses = params.get("PrivateAddresses")
        self._PublicAddresses = params.get("PublicAddresses")
        if params.get("InternetAccessible") is not None:
            self._InternetAccessible = InternetAccessible()
            self._InternetAccessible._deserialize(params.get("InternetAccessible"))
        self._RenewFlag = params.get("RenewFlag")
        if params.get("LoginSettings") is not None:
            self._LoginSettings = LoginSettings()
            self._LoginSettings._deserialize(params.get("LoginSettings"))
        self._InstanceState = params.get("InstanceState")
        self._Uuid = params.get("Uuid")
        self._LatestOperation = params.get("LatestOperation")
        self._LatestOperationState = params.get("LatestOperationState")
        self._LatestOperationRequestId = params.get("LatestOperationRequestId")
        self._IsolatedTime = params.get("IsolatedTime")
        self._CreatedTime = params.get("CreatedTime")
        self._ExpiredTime = params.get("ExpiredTime")
        self._PlatformType = params.get("PlatformType")
        self._Platform = params.get("Platform")
        self._OsName = params.get("OsName")
        self._Zone = params.get("Zone")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._InstanceRestrictState = params.get("InstanceRestrictState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceChargePrepaid(AbstractModel):
    """Instance billing mode

    """

    def __init__(self):
        r"""
        :param _Period: Subscription period in months. Valid values: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36, 48, 60.
        :type Period: int
        :param _RenewFlag: Auto-Renewal flag. Valid values: <br><li>NOTIFY_AND_AUTO_RENEW: notify upon expiration and renew automatically <br><li>NOTIFY_AND_MANUAL_RENEW: notify upon expiration but do not renew automatically. You need to manually renew <br><li>DISABLE_NOTIFY_AND_AUTO_RENEW: neither notify upon expiration nor renew automatically<br><br>Default value: NOTIFY_AND_MANUAL_RENEW. If this parameter is specified as `NOTIFY_AND_AUTO_RENEW`, the instance will be automatically renewed monthly if the account balance is sufficient.
        :type RenewFlag: str
        """
        self._Period = None
        self._RenewFlag = None

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag


    def _deserialize(self, params):
        self._Period = params.get("Period")
        self._RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceDeniedActions(AbstractModel):
    """List of instance operation limits.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param _DeniedActions: List of operation limits.
        :type DeniedActions: list of DeniedAction
        """
        self._InstanceId = None
        self._DeniedActions = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DeniedActions(self):
        return self._DeniedActions

    @DeniedActions.setter
    def DeniedActions(self, DeniedActions):
        self._DeniedActions = DeniedActions


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("DeniedActions") is not None:
            self._DeniedActions = []
            for item in params.get("DeniedActions"):
                obj = DeniedAction()
                obj._deserialize(item)
                self._DeniedActions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstancePrice(AbstractModel):
    """Price information of Lighthouse instances

    """

    def __init__(self):
        r"""
        :param _OriginalBundlePrice: Original package unit price.
        :type OriginalBundlePrice: float
        :param _OriginalPrice: Original price.
        :type OriginalPrice: float
        :param _Discount: Discount.
        :type Discount: int
        :param _DiscountPrice: Discounted price.
        :type DiscountPrice: float
        :param _Currency: Currency unit. Valid values: `CNY` and `USD`.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Currency: str
        """
        self._OriginalBundlePrice = None
        self._OriginalPrice = None
        self._Discount = None
        self._DiscountPrice = None
        self._Currency = None

    @property
    def OriginalBundlePrice(self):
        return self._OriginalBundlePrice

    @OriginalBundlePrice.setter
    def OriginalBundlePrice(self, OriginalBundlePrice):
        self._OriginalBundlePrice = OriginalBundlePrice

    @property
    def OriginalPrice(self):
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def Discount(self):
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount

    @property
    def DiscountPrice(self):
        return self._DiscountPrice

    @DiscountPrice.setter
    def DiscountPrice(self, DiscountPrice):
        self._DiscountPrice = DiscountPrice

    @property
    def Currency(self):
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency


    def _deserialize(self, params):
        self._OriginalBundlePrice = params.get("OriginalBundlePrice")
        self._OriginalPrice = params.get("OriginalPrice")
        self._Discount = params.get("Discount")
        self._DiscountPrice = params.get("DiscountPrice")
        self._Currency = params.get("Currency")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstancePriceDetail(AbstractModel):
    """Instance price details

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
Note: This field may return `null`, indicating that no valid value was found.
        :type InstanceId: str
        :param _InstancePrice: Price query information.
Note: This field may return `null`, indicating that no valid value was found.
        :type InstancePrice: :class:`tencentcloud.lighthouse.v20200324.models.InstancePrice`
        :param _DiscountDetail: Tiered-pricing details. The information of each tier includes the billable period, discount percentage, total price, discounted price, and discount details (`UserDiscount`, `CommonDiscount` and `FinalDiscount`).
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type DiscountDetail: list of DiscountDetail
        """
        self._InstanceId = None
        self._InstancePrice = None
        self._DiscountDetail = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstancePrice(self):
        return self._InstancePrice

    @InstancePrice.setter
    def InstancePrice(self, InstancePrice):
        self._InstancePrice = InstancePrice

    @property
    def DiscountDetail(self):
        return self._DiscountDetail

    @DiscountDetail.setter
    def DiscountDetail(self, DiscountDetail):
        self._DiscountDetail = DiscountDetail


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("InstancePrice") is not None:
            self._InstancePrice = InstancePrice()
            self._InstancePrice._deserialize(params.get("InstancePrice"))
        if params.get("DiscountDetail") is not None:
            self._DiscountDetail = []
            for item in params.get("DiscountDetail"):
                obj = DiscountDetail()
                obj._deserialize(item)
                self._DiscountDetail.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceReturnable(AbstractModel):
    """Whether the instance can be returned.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _IsReturnable: Whether the instance can be returned.
        :type IsReturnable: bool
        :param _ReturnFailCode: Error code of instance return failure.
        :type ReturnFailCode: int
        :param _ReturnFailMessage: Error message of instance return failure.
        :type ReturnFailMessage: str
        """
        self._InstanceId = None
        self._IsReturnable = None
        self._ReturnFailCode = None
        self._ReturnFailMessage = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def IsReturnable(self):
        return self._IsReturnable

    @IsReturnable.setter
    def IsReturnable(self, IsReturnable):
        self._IsReturnable = IsReturnable

    @property
    def ReturnFailCode(self):
        return self._ReturnFailCode

    @ReturnFailCode.setter
    def ReturnFailCode(self, ReturnFailCode):
        self._ReturnFailCode = ReturnFailCode

    @property
    def ReturnFailMessage(self):
        return self._ReturnFailMessage

    @ReturnFailMessage.setter
    def ReturnFailMessage(self, ReturnFailMessage):
        self._ReturnFailMessage = ReturnFailMessage


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._IsReturnable = params.get("IsReturnable")
        self._ReturnFailCode = params.get("ReturnFailCode")
        self._ReturnFailMessage = params.get("ReturnFailMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceTrafficPackage(AbstractModel):
    """Instance traffic package details

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _TrafficPackageSet: List of traffic package details.
        :type TrafficPackageSet: list of TrafficPackage
        """
        self._InstanceId = None
        self._TrafficPackageSet = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TrafficPackageSet(self):
        return self._TrafficPackageSet

    @TrafficPackageSet.setter
    def TrafficPackageSet(self, TrafficPackageSet):
        self._TrafficPackageSet = TrafficPackageSet


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("TrafficPackageSet") is not None:
            self._TrafficPackageSet = []
            for item in params.get("TrafficPackageSet"):
                obj = TrafficPackage()
                obj._deserialize(item)
                self._TrafficPackageSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InternetAccessible(AbstractModel):
    """This describes the internet accessibility of the instance created by a launch configuration and declares the internet usage billing method of the instance and the maximum bandwidth

    """

    def __init__(self):
        r"""
        :param _InternetChargeType: Network billing mode. Valid values:
<li>Bill by traffic package: TRAFFIC_POSTPAID_BY_HOUR</li>
<li>Bill by bandwidth: BANDWIDTH_POSTPAID_BY_HOUR</li>
        :type InternetChargeType: str
        :param _InternetMaxBandwidthOut: Public network outbound bandwidth cap in Mbps.
        :type InternetMaxBandwidthOut: int
        :param _PublicIpAssigned: Whether to assign a public IP.
        :type PublicIpAssigned: bool
        """
        self._InternetChargeType = None
        self._InternetMaxBandwidthOut = None
        self._PublicIpAssigned = None

    @property
    def InternetChargeType(self):
        return self._InternetChargeType

    @InternetChargeType.setter
    def InternetChargeType(self, InternetChargeType):
        self._InternetChargeType = InternetChargeType

    @property
    def InternetMaxBandwidthOut(self):
        return self._InternetMaxBandwidthOut

    @InternetMaxBandwidthOut.setter
    def InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):
        self._InternetMaxBandwidthOut = InternetMaxBandwidthOut

    @property
    def PublicIpAssigned(self):
        return self._PublicIpAssigned

    @PublicIpAssigned.setter
    def PublicIpAssigned(self, PublicIpAssigned):
        self._PublicIpAssigned = PublicIpAssigned


    def _deserialize(self, params):
        self._InternetChargeType = params.get("InternetChargeType")
        self._InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self._PublicIpAssigned = params.get("PublicIpAssigned")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateInstancesRequest(AbstractModel):
    """IsolateInstances request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: IDs of target instances. You can get the IDs from the `InstanceId` parameter returned by the `DescribeInstances` API. Up to 20 instances can be specified at the same time.
        :type InstanceIds: list of str
        :param _IsolateDataDisk: Whether to return data disks mounted on the instance together with the instance. Valid values: 
`TRUE`: Return the mounted data disks at the same time 
`FALSE`: Do not return the mounted data disks at the same time 
Default value: `TRUE`.
        :type IsolateDataDisk: bool
        """
        self._InstanceIds = None
        self._IsolateDataDisk = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def IsolateDataDisk(self):
        return self._IsolateDataDisk

    @IsolateDataDisk.setter
    def IsolateDataDisk(self, IsolateDataDisk):
        self._IsolateDataDisk = IsolateDataDisk


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._IsolateDataDisk = params.get("IsolateDataDisk")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateInstancesResponse(AbstractModel):
    """IsolateInstances response structure.

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


class KeyPair(AbstractModel):
    """Key pair information.

    """

    def __init__(self):
        r"""
        :param _KeyId: Key pair ID, which is the unique identifier of a key pair.
        :type KeyId: str
        :param _KeyName: Key pair name.
        :type KeyName: str
        :param _PublicKey: Public key (in plain text) of key pair.
        :type PublicKey: str
        :param _AssociatedInstanceIds: List of IDs of instances associated with the key pair.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AssociatedInstanceIds: list of str
        :param _CreatedTime: Creation time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreatedTime: str
        :param _PrivateKey: Private key of key pair.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PrivateKey: str
        """
        self._KeyId = None
        self._KeyName = None
        self._PublicKey = None
        self._AssociatedInstanceIds = None
        self._CreatedTime = None
        self._PrivateKey = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def KeyName(self):
        return self._KeyName

    @KeyName.setter
    def KeyName(self, KeyName):
        self._KeyName = KeyName

    @property
    def PublicKey(self):
        return self._PublicKey

    @PublicKey.setter
    def PublicKey(self, PublicKey):
        self._PublicKey = PublicKey

    @property
    def AssociatedInstanceIds(self):
        return self._AssociatedInstanceIds

    @AssociatedInstanceIds.setter
    def AssociatedInstanceIds(self, AssociatedInstanceIds):
        self._AssociatedInstanceIds = AssociatedInstanceIds

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def PrivateKey(self):
        return self._PrivateKey

    @PrivateKey.setter
    def PrivateKey(self, PrivateKey):
        self._PrivateKey = PrivateKey


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._KeyName = params.get("KeyName")
        self._PublicKey = params.get("PublicKey")
        self._AssociatedInstanceIds = params.get("AssociatedInstanceIds")
        self._CreatedTime = params.get("CreatedTime")
        self._PrivateKey = params.get("PrivateKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginConfiguration(AbstractModel):
    """Login password information

    """

    def __init__(self):
        r"""
        :param _AutoGeneratePassword: <li>`YES`: Random password. In this case, `Password` cannot be specified. </li>
<li>`No`: Custom. `Password` must be specified. </li>
        :type AutoGeneratePassword: str
        :param _Password: Instace login password.
For Windows instances, the password must contain 12 to 30 characters of the following types. It cannot start with “/” and cannot include the username.
<li>[a-z]</li>
<li>[A-Z]</li>
<li>[0-9]</li>
<li>[()`~!@#$%^&*-+=_|{}[]:;' <>,.?/]</li>
        :type Password: str
        """
        self._AutoGeneratePassword = None
        self._Password = None

    @property
    def AutoGeneratePassword(self):
        return self._AutoGeneratePassword

    @AutoGeneratePassword.setter
    def AutoGeneratePassword(self, AutoGeneratePassword):
        self._AutoGeneratePassword = AutoGeneratePassword

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password


    def _deserialize(self, params):
        self._AutoGeneratePassword = params.get("AutoGeneratePassword")
        self._Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginSettings(AbstractModel):
    """Describes login settings of an instance.

    """

    def __init__(self):
        r"""
        :param _KeyIds: Key ID list. After a key is associated, you can use it to access the instance. Note: this field may return [], indicating that no valid values can be obtained.
        :type KeyIds: list of str
        """
        self._KeyIds = None

    @property
    def KeyIds(self):
        return self._KeyIds

    @KeyIds.setter
    def KeyIds(self, KeyIds):
        self._KeyIds = KeyIds


    def _deserialize(self, params):
        self._KeyIds = params.get("KeyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBlueprintAttributeRequest(AbstractModel):
    """ModifyBlueprintAttribute request structure.

    """

    def __init__(self):
        r"""
        :param _BlueprintId: Image ID, which can be obtained from the `BlueprintId` returned by the [DescribeBlueprints](https://intl.cloud.tencent.com/document/product/1207/47689?from_cn_redirect=1) API.
        :type BlueprintId: str
        :param _BlueprintName: New image name, which can contain up to 60 characters.
        :type BlueprintName: str
        :param _Description: New image description, which can contain up to 60 characters.
        :type Description: str
        """
        self._BlueprintId = None
        self._BlueprintName = None
        self._Description = None

    @property
    def BlueprintId(self):
        return self._BlueprintId

    @BlueprintId.setter
    def BlueprintId(self, BlueprintId):
        self._BlueprintId = BlueprintId

    @property
    def BlueprintName(self):
        return self._BlueprintName

    @BlueprintName.setter
    def BlueprintName(self, BlueprintName):
        self._BlueprintName = BlueprintName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._BlueprintId = params.get("BlueprintId")
        self._BlueprintName = params.get("BlueprintName")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBlueprintAttributeResponse(AbstractModel):
    """ModifyBlueprintAttribute response structure.

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


class ModifyBundle(AbstractModel):
    """Changeable packages for the instance.

    """

    def __init__(self):
        r"""
        :param _ModifyPrice: Price difference that you need to pay for the new instance package after change.
        :type ModifyPrice: :class:`tencentcloud.lighthouse.v20200324.models.Price`
        :param _ModifyBundleState: Package change status. Valid values:
<li>SOLD_OUT: packages are sold out</li>
<li>AVAILABLE: packages can be changed</li>
<li>UNAVAILABLE: packages cannot be changed currently</li>
        :type ModifyBundleState: str
        :param _Bundle: Package information.
        :type Bundle: :class:`tencentcloud.lighthouse.v20200324.models.Bundle`
        :param _NotSupportModifyMessage: The reason of package changing failure. It’s empty if the package change status is `AVAILABLE`.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type NotSupportModifyMessage: str
        """
        self._ModifyPrice = None
        self._ModifyBundleState = None
        self._Bundle = None
        self._NotSupportModifyMessage = None

    @property
    def ModifyPrice(self):
        return self._ModifyPrice

    @ModifyPrice.setter
    def ModifyPrice(self, ModifyPrice):
        self._ModifyPrice = ModifyPrice

    @property
    def ModifyBundleState(self):
        return self._ModifyBundleState

    @ModifyBundleState.setter
    def ModifyBundleState(self, ModifyBundleState):
        self._ModifyBundleState = ModifyBundleState

    @property
    def Bundle(self):
        return self._Bundle

    @Bundle.setter
    def Bundle(self, Bundle):
        self._Bundle = Bundle

    @property
    def NotSupportModifyMessage(self):
        return self._NotSupportModifyMessage

    @NotSupportModifyMessage.setter
    def NotSupportModifyMessage(self, NotSupportModifyMessage):
        self._NotSupportModifyMessage = NotSupportModifyMessage


    def _deserialize(self, params):
        if params.get("ModifyPrice") is not None:
            self._ModifyPrice = Price()
            self._ModifyPrice._deserialize(params.get("ModifyPrice"))
        self._ModifyBundleState = params.get("ModifyBundleState")
        if params.get("Bundle") is not None:
            self._Bundle = Bundle()
            self._Bundle._deserialize(params.get("Bundle"))
        self._NotSupportModifyMessage = params.get("NotSupportModifyMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDisksAttributeRequest(AbstractModel):
    """ModifyDisksAttribute request structure.

    """

    def __init__(self):
        r"""
        :param _DiskIds: List of cloud disk IDs.
        :type DiskIds: list of str
        :param _DiskName: Cloud disk name.
        :type DiskName: str
        """
        self._DiskIds = None
        self._DiskName = None

    @property
    def DiskIds(self):
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds

    @property
    def DiskName(self):
        return self._DiskName

    @DiskName.setter
    def DiskName(self, DiskName):
        self._DiskName = DiskName


    def _deserialize(self, params):
        self._DiskIds = params.get("DiskIds")
        self._DiskName = params.get("DiskName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDisksAttributeResponse(AbstractModel):
    """ModifyDisksAttribute response structure.

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


class ModifyDisksRenewFlagRequest(AbstractModel):
    """ModifyDisksRenewFlag request structure.

    """

    def __init__(self):
        r"""
        :param _DiskIds: List of cloud disk IDs.
        :type DiskIds: list of str
        :param _RenewFlag: Whether Auto-Renewal is enabled 
        :type RenewFlag: str
        """
        self._DiskIds = None
        self._RenewFlag = None

    @property
    def DiskIds(self):
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag


    def _deserialize(self, params):
        self._DiskIds = params.get("DiskIds")
        self._RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDisksRenewFlagResponse(AbstractModel):
    """ModifyDisksRenewFlag response structure.

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


class ModifyFirewallRuleDescriptionRequest(AbstractModel):
    """ModifyFirewallRuleDescription request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _FirewallRule: Firewall rule.
        :type FirewallRule: :class:`tencentcloud.lighthouse.v20200324.models.FirewallRule`
        :param _FirewallVersion: Current firewall version number. Every time you update the firewall rule version, it will be automatically increased by 1 to prevent the rule from expiring. If it is left empty, conflicts will not be considered.
        :type FirewallVersion: int
        """
        self._InstanceId = None
        self._FirewallRule = None
        self._FirewallVersion = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def FirewallRule(self):
        return self._FirewallRule

    @FirewallRule.setter
    def FirewallRule(self, FirewallRule):
        self._FirewallRule = FirewallRule

    @property
    def FirewallVersion(self):
        return self._FirewallVersion

    @FirewallVersion.setter
    def FirewallVersion(self, FirewallVersion):
        self._FirewallVersion = FirewallVersion


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("FirewallRule") is not None:
            self._FirewallRule = FirewallRule()
            self._FirewallRule._deserialize(params.get("FirewallRule"))
        self._FirewallVersion = params.get("FirewallVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyFirewallRuleDescriptionResponse(AbstractModel):
    """ModifyFirewallRuleDescription response structure.

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


class ModifyFirewallRulesRequest(AbstractModel):
    """ModifyFirewallRules request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _FirewallRules: Firewall rule list.
        :type FirewallRules: list of FirewallRule
        :param _FirewallVersion: Current firewall version number. Every time you update the firewall rule version, it will be automatically increased by 1 to prevent the rule from expiring. If it is left empty, conflicts will not be considered.
        :type FirewallVersion: int
        """
        self._InstanceId = None
        self._FirewallRules = None
        self._FirewallVersion = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def FirewallRules(self):
        return self._FirewallRules

    @FirewallRules.setter
    def FirewallRules(self, FirewallRules):
        self._FirewallRules = FirewallRules

    @property
    def FirewallVersion(self):
        return self._FirewallVersion

    @FirewallVersion.setter
    def FirewallVersion(self, FirewallVersion):
        self._FirewallVersion = FirewallVersion


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("FirewallRules") is not None:
            self._FirewallRules = []
            for item in params.get("FirewallRules"):
                obj = FirewallRule()
                obj._deserialize(item)
                self._FirewallRules.append(obj)
        self._FirewallVersion = params.get("FirewallVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyFirewallRulesResponse(AbstractModel):
    """ModifyFirewallRules response structure.

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


class ModifyInstancesAttributeRequest(AbstractModel):
    """ModifyInstancesAttribute request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: Instance ID list. Each request can contain up to 100 instances at a time. You can get an instance ID from the `InstanceId` returned by the [DescribeInstances](https://intl.cloud.tencent.com/document/api/1207/47573?from_cn_redirect=1) API.
        :type InstanceIds: list of str
        :param _InstanceName: Instance name, which is customizable and can contain up to 60 characters.
        :type InstanceName: str
        """
        self._InstanceIds = None
        self._InstanceName = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._InstanceName = params.get("InstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstancesAttributeResponse(AbstractModel):
    """ModifyInstancesAttribute response structure.

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


class ModifyInstancesBundleRequest(AbstractModel):
    """ModifyInstancesBundle request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: IDs of target instances. You can get the IDs from the `InstanceId` parameter returned by the `DescribeInstances` API. Up to 15 instances can be specified at the same time.
        :type InstanceIds: list of str
        :param _BundleId: ID of bundles to change. You can get the IDs from the `BundleId` returned by the [DescribeBundles](https://intl.cloud.tencent.com/document/api/1207/47575?from_cn_redirect=1).
        :type BundleId: str
        :param _AutoVoucher: Whether to use existing vouchers under the current account automatically. Valid values: 
`true`: Deduct from existing vouchers automatically 
`false`: Do not deduct from existing vouchers automatically 
Default value: `false`.
        :type AutoVoucher: bool
        """
        self._InstanceIds = None
        self._BundleId = None
        self._AutoVoucher = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def BundleId(self):
        return self._BundleId

    @BundleId.setter
    def BundleId(self, BundleId):
        self._BundleId = BundleId

    @property
    def AutoVoucher(self):
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._BundleId = params.get("BundleId")
        self._AutoVoucher = params.get("AutoVoucher")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstancesBundleResponse(AbstractModel):
    """ModifyInstancesBundle response structure.

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


class ModifyInstancesLoginKeyPairAttributeRequest(AbstractModel):
    """ModifyInstancesLoginKeyPairAttribute request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: Instance ID list. Each request can contain up to 100 instances at a time.
        :type InstanceIds: list of str
        :param _PermitLogin: Whether to allow login with the default key pair. Valid values: YES: yes; NO: no.
        :type PermitLogin: str
        """
        self._InstanceIds = None
        self._PermitLogin = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def PermitLogin(self):
        return self._PermitLogin

    @PermitLogin.setter
    def PermitLogin(self, PermitLogin):
        self._PermitLogin = PermitLogin


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._PermitLogin = params.get("PermitLogin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstancesLoginKeyPairAttributeResponse(AbstractModel):
    """ModifyInstancesLoginKeyPairAttribute response structure.

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


class ModifyInstancesRenewFlagRequest(AbstractModel):
    """ModifyInstancesRenewFlag request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: Instance ID list. Each request can contain up to 100 instances at a time. You can get an instance ID from the `InstanceId` returned by the [DescribeInstances](https://intl.cloud.tencent.com/document/api/1207/47573?from_cn_redirect=1) API.
        :type InstanceIds: list of str
        :param _RenewFlag: Auto-Renewal flag. Valid values: <br><li>NOTIFY_AND_AUTO_RENEW: notify upon expiration and renew automatically <br><li>NOTIFY_AND_MANUAL_RENEW: notify upon expiration but do not renew automatically <br><li>DISABLE_NOTIFY_AND_MANUAL_RENEW: neither notify upon expiration nor renew automatically <br><br>If this parameter is specified as `NOTIFY_AND_AUTO_RENEW`, the instance will be automatically renewed monthly if the account balance is sufficient.
        :type RenewFlag: str
        """
        self._InstanceIds = None
        self._RenewFlag = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstancesRenewFlagResponse(AbstractModel):
    """ModifyInstancesRenewFlag response structure.

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


class ModifySnapshotAttributeRequest(AbstractModel):
    """ModifySnapshotAttribute request structure.

    """

    def __init__(self):
        r"""
        :param _SnapshotId: Snapshot ID, which can be queried through `DescribeSnapshots`.
        :type SnapshotId: str
        :param _SnapshotName: New snapshot name, which can contain up to 60 characters.
        :type SnapshotName: str
        """
        self._SnapshotId = None
        self._SnapshotName = None

    @property
    def SnapshotId(self):
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def SnapshotName(self):
        return self._SnapshotName

    @SnapshotName.setter
    def SnapshotName(self, SnapshotName):
        self._SnapshotName = SnapshotName


    def _deserialize(self, params):
        self._SnapshotId = params.get("SnapshotId")
        self._SnapshotName = params.get("SnapshotName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySnapshotAttributeResponse(AbstractModel):
    """ModifySnapshotAttribute response structure.

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


class PolicyDetail(AbstractModel):
    """Discount details.

    """

    def __init__(self):
        r"""
        :param _UserDiscount: User discount.
        :type UserDiscount: int
        :param _CommonDiscount: Public discount.
        :type CommonDiscount: int
        :param _FinalDiscount: Final discount.
        :type FinalDiscount: int
        :param _ActivityDiscount: Activity discount. The value `null` indicates no discount.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ActivityDiscount: float
        :param _DiscountType: Discount type.
Valid values: `user` (user discount), `common` (discount displayed on the official website), `activity` (activity discount), `null` (no discount).
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type DiscountType: str
        """
        self._UserDiscount = None
        self._CommonDiscount = None
        self._FinalDiscount = None
        self._ActivityDiscount = None
        self._DiscountType = None

    @property
    def UserDiscount(self):
        return self._UserDiscount

    @UserDiscount.setter
    def UserDiscount(self, UserDiscount):
        self._UserDiscount = UserDiscount

    @property
    def CommonDiscount(self):
        return self._CommonDiscount

    @CommonDiscount.setter
    def CommonDiscount(self, CommonDiscount):
        self._CommonDiscount = CommonDiscount

    @property
    def FinalDiscount(self):
        return self._FinalDiscount

    @FinalDiscount.setter
    def FinalDiscount(self, FinalDiscount):
        self._FinalDiscount = FinalDiscount

    @property
    def ActivityDiscount(self):
        return self._ActivityDiscount

    @ActivityDiscount.setter
    def ActivityDiscount(self, ActivityDiscount):
        self._ActivityDiscount = ActivityDiscount

    @property
    def DiscountType(self):
        return self._DiscountType

    @DiscountType.setter
    def DiscountType(self, DiscountType):
        self._DiscountType = DiscountType


    def _deserialize(self, params):
        self._UserDiscount = params.get("UserDiscount")
        self._CommonDiscount = params.get("CommonDiscount")
        self._FinalDiscount = params.get("FinalDiscount")
        self._ActivityDiscount = params.get("ActivityDiscount")
        self._DiscountType = params.get("DiscountType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Price(AbstractModel):
    """Price information

    """

    def __init__(self):
        r"""
        :param _InstancePrice: Instance price.
        :type InstancePrice: :class:`tencentcloud.lighthouse.v20200324.models.InstancePrice`
        """
        self._InstancePrice = None

    @property
    def InstancePrice(self):
        return self._InstancePrice

    @InstancePrice.setter
    def InstancePrice(self, InstancePrice):
        self._InstancePrice = InstancePrice


    def _deserialize(self, params):
        if params.get("InstancePrice") is not None:
            self._InstancePrice = InstancePrice()
            self._InstancePrice._deserialize(params.get("InstancePrice"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RebootInstancesRequest(AbstractModel):
    """RebootInstances request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: Instance ID list. Each request can contain up to 100 instances at a time. You can get an instance ID from the `InstanceId` returned by the [DescribeInstances](https://intl.cloud.tencent.com/document/api/1207/47573?from_cn_redirect=1) API.
        :type InstanceIds: list of str
        """
        self._InstanceIds = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RebootInstancesResponse(AbstractModel):
    """RebootInstances response structure.

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


class RegionInfo(AbstractModel):
    """Region information.

    """

    def __init__(self):
        r"""
        :param _Region: Region name, such as `ap-guangzhou`.
        :type Region: str
        :param _RegionName: Region description, such as South China (Guangzhou).
        :type RegionName: str
        :param _RegionState: Region availability status. Its value can only be `AVAILABLE`.
        :type RegionState: str
        :param _IsChinaMainland: Whether the region is in the Chinese mainland
        :type IsChinaMainland: bool
        """
        self._Region = None
        self._RegionName = None
        self._RegionState = None
        self._IsChinaMainland = None

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def RegionName(self):
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def RegionState(self):
        return self._RegionState

    @RegionState.setter
    def RegionState(self, RegionState):
        self._RegionState = RegionState

    @property
    def IsChinaMainland(self):
        return self._IsChinaMainland

    @IsChinaMainland.setter
    def IsChinaMainland(self, IsChinaMainland):
        self._IsChinaMainland = IsChinaMainland


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._RegionName = params.get("RegionName")
        self._RegionState = params.get("RegionState")
        self._IsChinaMainland = params.get("IsChinaMainland")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewDiskChargePrepaid(AbstractModel):
    """Parameter settings for renewing the monthly subscribed cloud disk

    """

    def __init__(self):
        r"""
        :param _Period: Purchase duration.
        :type Period: int
        :param _RenewFlag: Whether Auto-Renewal is enabled 
        :type RenewFlag: str
        :param _TimeUnit: Duration unit. Default value: "m" (month).
        :type TimeUnit: str
        :param _CurInstanceDeadline: Expiration time of the current instance.
        :type CurInstanceDeadline: str
        """
        self._Period = None
        self._RenewFlag = None
        self._TimeUnit = None
        self._CurInstanceDeadline = None

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def TimeUnit(self):
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def CurInstanceDeadline(self):
        return self._CurInstanceDeadline

    @CurInstanceDeadline.setter
    def CurInstanceDeadline(self, CurInstanceDeadline):
        self._CurInstanceDeadline = CurInstanceDeadline


    def _deserialize(self, params):
        self._Period = params.get("Period")
        self._RenewFlag = params.get("RenewFlag")
        self._TimeUnit = params.get("TimeUnit")
        self._CurInstanceDeadline = params.get("CurInstanceDeadline")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetAttachCcnRequest(AbstractModel):
    """ResetAttachCcn request structure.

    """

    def __init__(self):
        r"""
        :param _CcnId: CCN instance ID.
        :type CcnId: str
        """
        self._CcnId = None

    @property
    def CcnId(self):
        return self._CcnId

    @CcnId.setter
    def CcnId(self, CcnId):
        self._CcnId = CcnId


    def _deserialize(self, params):
        self._CcnId = params.get("CcnId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetAttachCcnResponse(AbstractModel):
    """ResetAttachCcn response structure.

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


class ResetInstanceBlueprint(AbstractModel):
    """Image reset information

    """

    def __init__(self):
        r"""
        :param _BlueprintInfo: Image details
        :type BlueprintInfo: :class:`tencentcloud.lighthouse.v20200324.models.Blueprint`
        :param _IsResettable: Whether the image can be reset as the target image
        :type IsResettable: bool
        :param _NonResettableMessage: Non-Resettable flag. If the image is resettable, it will be ""
        :type NonResettableMessage: str
        """
        self._BlueprintInfo = None
        self._IsResettable = None
        self._NonResettableMessage = None

    @property
    def BlueprintInfo(self):
        return self._BlueprintInfo

    @BlueprintInfo.setter
    def BlueprintInfo(self, BlueprintInfo):
        self._BlueprintInfo = BlueprintInfo

    @property
    def IsResettable(self):
        return self._IsResettable

    @IsResettable.setter
    def IsResettable(self, IsResettable):
        self._IsResettable = IsResettable

    @property
    def NonResettableMessage(self):
        return self._NonResettableMessage

    @NonResettableMessage.setter
    def NonResettableMessage(self, NonResettableMessage):
        self._NonResettableMessage = NonResettableMessage


    def _deserialize(self, params):
        if params.get("BlueprintInfo") is not None:
            self._BlueprintInfo = Blueprint()
            self._BlueprintInfo._deserialize(params.get("BlueprintInfo"))
        self._IsResettable = params.get("IsResettable")
        self._NonResettableMessage = params.get("NonResettableMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetInstanceRequest(AbstractModel):
    """ResetInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID, which can be obtained from the `InstanceId` returned by the [DescribeInstances](https://intl.cloud.tencent.com/document/api/1207/47573?from_cn_redirect=1) API.
        :type InstanceId: str
        :param _BlueprintId: Image ID, which can be obtained from the `BlueprintId` returned by the [DescribeBlueprints](https://intl.cloud.tencent.com/document/product/1207/47689?from_cn_redirect=1) API.
        :type BlueprintId: str
        """
        self._InstanceId = None
        self._BlueprintId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BlueprintId(self):
        return self._BlueprintId

    @BlueprintId.setter
    def BlueprintId(self, BlueprintId):
        self._BlueprintId = BlueprintId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BlueprintId = params.get("BlueprintId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetInstanceResponse(AbstractModel):
    """ResetInstance response structure.

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


class ResetInstancesPasswordRequest(AbstractModel):
    """ResetInstancesPassword request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: Instance ID list. Each request can contain up to 100 instances at a time.
        :type InstanceIds: list of str
        :param _Password: Login password of the instance(s). The password requirements vary among different operating systems:
The password of a `LINUX_UNIX` instance must contain 8–30 characters (above 12 characters preferably) in at least three of the following types and cannot begin with "/": <br><li>Lowercase letters: [a–z]<br><li>Uppercase letters: [A–Z]<br><li>Digits: 0–9<br><li>Special symbols: ()\`~!@#$%^&\*-+=\_|{}[]:;'<>,.?/</li>
The password of a `WINDOWS` instance must contain 12–30 characters in at least three of the following types and cannot begin with "/" or include the username: <br><li>Lowercase letters: [a–z]<br><li>Uppercase letters: [A–Z]<br><li>Digits: 0–9<br><li>Special symbols: ()\`~!@#$%^&\*-+=\_|{}[]:;' <>,.?/<br><li>If both `LINUX_UNIX` and `WINDOWS` instances exist, the requirements for password complexity of `WINDOWS` instances shall prevail.
        :type Password: str
        :param _UserName: OS username of the instance for which you want to reset the password, which can contain up to 64 characters.
        :type UserName: str
        """
        self._InstanceIds = None
        self._Password = None
        self._UserName = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

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


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._Password = params.get("Password")
        self._UserName = params.get("UserName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetInstancesPasswordResponse(AbstractModel):
    """ResetInstancesPassword response structure.

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


class Scene(AbstractModel):
    """Scene information

    """

    def __init__(self):
        r"""
        :param _SceneId: Scene ID
        :type SceneId: str
        :param _DisplayName: Display name of the scene
        :type DisplayName: str
        :param _Description: Scene description
        :type Description: str
        """
        self._SceneId = None
        self._DisplayName = None
        self._Description = None

    @property
    def SceneId(self):
        return self._SceneId

    @SceneId.setter
    def SceneId(self, SceneId):
        self._SceneId = SceneId

    @property
    def DisplayName(self):
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._SceneId = params.get("SceneId")
        self._DisplayName = params.get("DisplayName")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SceneInfo(AbstractModel):
    """Scene information

    """

    def __init__(self):
        r"""
        :param _SceneId: Scene ID
        :type SceneId: str
        :param _DisplayName: Display name of the scene
        :type DisplayName: str
        :param _Description: Scene description
        :type Description: str
        """
        self._SceneId = None
        self._DisplayName = None
        self._Description = None

    @property
    def SceneId(self):
        return self._SceneId

    @SceneId.setter
    def SceneId(self, SceneId):
        self._SceneId = SceneId

    @property
    def DisplayName(self):
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._SceneId = params.get("SceneId")
        self._DisplayName = params.get("DisplayName")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Snapshot(AbstractModel):
    """Snapshot information.

    """

    def __init__(self):
        r"""
        :param _SnapshotId: Snapshot ID.
        :type SnapshotId: str
        :param _DiskUsage: Type of the disk for which the snapshot is created. Valid values: <li>SYSTEM_DISK: system disk</li>
        :type DiskUsage: str
        :param _DiskId: ID of the disk for which the snapshot is created.
        :type DiskId: str
        :param _DiskSize: Size of the disk in GB for which the snapshot is created.
        :type DiskSize: int
        :param _SnapshotName: Snapshot name, which is a custom snapshot alias.
        :type SnapshotName: str
        :param _SnapshotState: Snapshot status. Valid values:
<li>NORMAL: normal </li>
<li>CREATING: creating</li>
<li>ROLLBACKING: rolling back</li>
        :type SnapshotState: str
        :param _Percent: Snapshot creation or rollback progress in percentage. After success, the value of this field will become 100.
        :type Percent: int
        :param _LatestOperation: Last snapshot operation. It is recorded only during snapshot creation and rollback.
Example values: CreateInstanceSnapshot, RollbackInstanceSnapshot.
Note: this field may return null, indicating that no valid values can be obtained.
        :type LatestOperation: str
        :param _LatestOperationState: Last snapshot operation status. It is recorded only during snapshot creation and rollback.
Valid values:
<li>SUCCESS: operation succeeded</li>
<li>OPERATING: the operation is being executed</li>
<li>FAILED: operation failed</li>
Note: this field may return null, indicating that no valid values can be obtained.
        :type LatestOperationState: str
        :param _LatestOperationRequestId: Unique request ID for the last snapshot operation. It is recorded only during snapshot creation and rollback.
Note: this field may return null, indicating that no valid values can be obtained.
        :type LatestOperationRequestId: str
        :param _CreatedTime: Snapshot creation time.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type CreatedTime: str
        """
        self._SnapshotId = None
        self._DiskUsage = None
        self._DiskId = None
        self._DiskSize = None
        self._SnapshotName = None
        self._SnapshotState = None
        self._Percent = None
        self._LatestOperation = None
        self._LatestOperationState = None
        self._LatestOperationRequestId = None
        self._CreatedTime = None

    @property
    def SnapshotId(self):
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def DiskUsage(self):
        return self._DiskUsage

    @DiskUsage.setter
    def DiskUsage(self, DiskUsage):
        self._DiskUsage = DiskUsage

    @property
    def DiskId(self):
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def SnapshotName(self):
        return self._SnapshotName

    @SnapshotName.setter
    def SnapshotName(self, SnapshotName):
        self._SnapshotName = SnapshotName

    @property
    def SnapshotState(self):
        return self._SnapshotState

    @SnapshotState.setter
    def SnapshotState(self, SnapshotState):
        self._SnapshotState = SnapshotState

    @property
    def Percent(self):
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent

    @property
    def LatestOperation(self):
        return self._LatestOperation

    @LatestOperation.setter
    def LatestOperation(self, LatestOperation):
        self._LatestOperation = LatestOperation

    @property
    def LatestOperationState(self):
        return self._LatestOperationState

    @LatestOperationState.setter
    def LatestOperationState(self, LatestOperationState):
        self._LatestOperationState = LatestOperationState

    @property
    def LatestOperationRequestId(self):
        return self._LatestOperationRequestId

    @LatestOperationRequestId.setter
    def LatestOperationRequestId(self, LatestOperationRequestId):
        self._LatestOperationRequestId = LatestOperationRequestId

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime


    def _deserialize(self, params):
        self._SnapshotId = params.get("SnapshotId")
        self._DiskUsage = params.get("DiskUsage")
        self._DiskId = params.get("DiskId")
        self._DiskSize = params.get("DiskSize")
        self._SnapshotName = params.get("SnapshotName")
        self._SnapshotState = params.get("SnapshotState")
        self._Percent = params.get("Percent")
        self._LatestOperation = params.get("LatestOperation")
        self._LatestOperationState = params.get("LatestOperationState")
        self._LatestOperationRequestId = params.get("LatestOperationRequestId")
        self._CreatedTime = params.get("CreatedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SnapshotDeniedActions(AbstractModel):
    """List of snapshot operation limits.

    """

    def __init__(self):
        r"""
        :param _SnapshotId: Snapshot ID.
        :type SnapshotId: str
        :param _DeniedActions: List of operation limits.
        :type DeniedActions: list of DeniedAction
        """
        self._SnapshotId = None
        self._DeniedActions = None

    @property
    def SnapshotId(self):
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def DeniedActions(self):
        return self._DeniedActions

    @DeniedActions.setter
    def DeniedActions(self, DeniedActions):
        self._DeniedActions = DeniedActions


    def _deserialize(self, params):
        self._SnapshotId = params.get("SnapshotId")
        if params.get("DeniedActions") is not None:
            self._DeniedActions = []
            for item in params.get("DeniedActions"):
                obj = DeniedAction()
                obj._deserialize(item)
                self._DeniedActions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Software(AbstractModel):
    """Image software information.

    """

    def __init__(self):
        r"""
        :param _Name: Software name.
        :type Name: str
        :param _Version: Software version.
        :type Version: str
        :param _ImageUrl: Software picture URL.
        :type ImageUrl: str
        :param _InstallDir: Software installation directory.
        :type InstallDir: str
        :param _DetailSet: List of software details.
        :type DetailSet: list of SoftwareDetail
        """
        self._Name = None
        self._Version = None
        self._ImageUrl = None
        self._InstallDir = None
        self._DetailSet = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def InstallDir(self):
        return self._InstallDir

    @InstallDir.setter
    def InstallDir(self, InstallDir):
        self._InstallDir = InstallDir

    @property
    def DetailSet(self):
        return self._DetailSet

    @DetailSet.setter
    def DetailSet(self, DetailSet):
        self._DetailSet = DetailSet


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Version = params.get("Version")
        self._ImageUrl = params.get("ImageUrl")
        self._InstallDir = params.get("InstallDir")
        if params.get("DetailSet") is not None:
            self._DetailSet = []
            for item in params.get("DetailSet"):
                obj = SoftwareDetail()
                obj._deserialize(item)
                self._DetailSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SoftwareDetail(AbstractModel):
    """Image software details.

    """

    def __init__(self):
        r"""
        :param _Key: Unique detail key
        :type Key: str
        :param _Title: Detail title.
        :type Title: str
        :param _Value: Detail value.
        :type Value: str
        """
        self._Key = None
        self._Title = None
        self._Value = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Title = params.get("Title")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartInstancesRequest(AbstractModel):
    """StartInstances request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: Instance ID list. Each request can contain up to 100 instances at a time. You can get an instance ID from the `InstanceId` returned by the [DescribeInstances](https://intl.cloud.tencent.com/document/api/1207/47573?from_cn_redirect=1) API.
        :type InstanceIds: list of str
        """
        self._InstanceIds = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartInstancesResponse(AbstractModel):
    """StartInstances response structure.

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


class StopInstancesRequest(AbstractModel):
    """StopInstances request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: Instance ID list. Each request can contain up to 100 instances at a time. You can get an instance ID from the `InstanceId` returned by the [DescribeInstances](https://intl.cloud.tencent.com/document/api/1207/47573?from_cn_redirect=1) API.
        :type InstanceIds: list of str
        """
        self._InstanceIds = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopInstancesResponse(AbstractModel):
    """StopInstances response structure.

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


class SystemDisk(AbstractModel):
    """Information on the block device where the operating system is installed, namely the system disk.

    """

    def __init__(self):
        r"""
        :param _DiskType: System disk type.
Valid values: 
<li> LOCAL_BASIC: local disk</li><li> LOCAL_SSD: local SSD disk</li><li> CLOUD_BASIC: HDD cloud disk</li><li> CLOUD_SSD: SSD cloud disk</li><li> CLOUD_PREMIUM: Premium Cloud Storage</li>
        :type DiskType: str
        :param _DiskSize: System disk size in GB.
        :type DiskSize: int
        :param _DiskId: System disk ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DiskId: str
        """
        self._DiskType = None
        self._DiskSize = None
        self._DiskId = None

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DiskId(self):
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId


    def _deserialize(self, params):
        self._DiskType = params.get("DiskType")
        self._DiskSize = params.get("DiskSize")
        self._DiskId = params.get("DiskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """Information on tags

    """

    def __init__(self):
        r"""
        :param _Key: Tag key
        :type Key: str
        :param _Value: Tag value
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateDisksRequest(AbstractModel):
    """TerminateDisks request structure.

    """

    def __init__(self):
        r"""
        :param _DiskIds: List of cloud disk IDs.
        :type DiskIds: list of str
        """
        self._DiskIds = None

    @property
    def DiskIds(self):
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds


    def _deserialize(self, params):
        self._DiskIds = params.get("DiskIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateDisksResponse(AbstractModel):
    """TerminateDisks response structure.

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


class TerminateInstancesRequest(AbstractModel):
    """TerminateInstances request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: Instance ID list, which can be obtained from the `InstanceId` returned by the [DescribeInstances](https://intl.cloud.tencent.com/document/api/1207/47573?from_cn_redirect=1) API.
        :type InstanceIds: list of str
        """
        self._InstanceIds = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateInstancesResponse(AbstractModel):
    """TerminateInstances response structure.

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


class TotalPrice(AbstractModel):
    """Total price information

    """

    def __init__(self):
        r"""
        :param _OriginalPrice: Total original price
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type OriginalPrice: float
        :param _DiscountPrice: Total discounted price
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type DiscountPrice: float
        """
        self._OriginalPrice = None
        self._DiscountPrice = None

    @property
    def OriginalPrice(self):
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def DiscountPrice(self):
        return self._DiscountPrice

    @DiscountPrice.setter
    def DiscountPrice(self, DiscountPrice):
        self._DiscountPrice = DiscountPrice


    def _deserialize(self, params):
        self._OriginalPrice = params.get("OriginalPrice")
        self._DiscountPrice = params.get("DiscountPrice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrafficPackage(AbstractModel):
    """Traffic package details.

    """

    def __init__(self):
        r"""
        :param _TrafficPackageId: Traffic package ID.
        :type TrafficPackageId: str
        :param _TrafficUsed: Used traffic in bytes during traffic package validity period.
        :type TrafficUsed: int
        :param _TrafficPackageTotal: Total traffic in bytes during traffic package validity period.
        :type TrafficPackageTotal: int
        :param _TrafficPackageRemaining: Remaining traffic in bytes during traffic package validity period.
        :type TrafficPackageRemaining: int
        :param _TrafficOverflow: Traffic exceeding package amount in bytes during traffic package validity period.
        :type TrafficOverflow: int
        :param _StartTime: Start time of traffic package validity period according to ISO 8601 standard. UTC time is used. 
Format: YYYY-MM-DDThh:mm:ssZ.
Note: this field may return null, indicating that no valid values can be obtained.
        :type StartTime: str
        :param _EndTime: End time of traffic package validity period according to ISO 8601 standard. UTC time is used. 
Format: YYYY-MM-DDThh:mm:ssZ.
Note: this field may return null, indicating that no valid values can be obtained.
        :type EndTime: str
        :param _Deadline: Traffic package expiration time according to ISO 8601 standard. UTC time is used. 
Format: YYYY-MM-DDThh:mm:ssZ.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Deadline: str
        :param _Status: Traffic package status:
<li>NETWORK_NORMAL: normal</li>
<li>OVERDUE_NETWORK_DISABLED: the network is disconnected due to overdue payments</li>
        :type Status: str
        """
        self._TrafficPackageId = None
        self._TrafficUsed = None
        self._TrafficPackageTotal = None
        self._TrafficPackageRemaining = None
        self._TrafficOverflow = None
        self._StartTime = None
        self._EndTime = None
        self._Deadline = None
        self._Status = None

    @property
    def TrafficPackageId(self):
        return self._TrafficPackageId

    @TrafficPackageId.setter
    def TrafficPackageId(self, TrafficPackageId):
        self._TrafficPackageId = TrafficPackageId

    @property
    def TrafficUsed(self):
        return self._TrafficUsed

    @TrafficUsed.setter
    def TrafficUsed(self, TrafficUsed):
        self._TrafficUsed = TrafficUsed

    @property
    def TrafficPackageTotal(self):
        return self._TrafficPackageTotal

    @TrafficPackageTotal.setter
    def TrafficPackageTotal(self, TrafficPackageTotal):
        self._TrafficPackageTotal = TrafficPackageTotal

    @property
    def TrafficPackageRemaining(self):
        return self._TrafficPackageRemaining

    @TrafficPackageRemaining.setter
    def TrafficPackageRemaining(self, TrafficPackageRemaining):
        self._TrafficPackageRemaining = TrafficPackageRemaining

    @property
    def TrafficOverflow(self):
        return self._TrafficOverflow

    @TrafficOverflow.setter
    def TrafficOverflow(self, TrafficOverflow):
        self._TrafficOverflow = TrafficOverflow

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
    def Deadline(self):
        return self._Deadline

    @Deadline.setter
    def Deadline(self, Deadline):
        self._Deadline = Deadline

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._TrafficPackageId = params.get("TrafficPackageId")
        self._TrafficUsed = params.get("TrafficUsed")
        self._TrafficPackageTotal = params.get("TrafficPackageTotal")
        self._TrafficPackageRemaining = params.get("TrafficPackageRemaining")
        self._TrafficOverflow = params.get("TrafficOverflow")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Deadline = params.get("Deadline")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneInfo(AbstractModel):
    """AZ details

    """

    def __init__(self):
        r"""
        :param _Zone: AZ
        :type Zone: str
        :param _ZoneName: Chinese name of AZ
        :type ZoneName: str
        :param _InstanceDisplayLabel: AZ tags on instance purchase page
        :type InstanceDisplayLabel: str
        """
        self._Zone = None
        self._ZoneName = None
        self._InstanceDisplayLabel = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ZoneName(self):
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def InstanceDisplayLabel(self):
        return self._InstanceDisplayLabel

    @InstanceDisplayLabel.setter
    def InstanceDisplayLabel(self, InstanceDisplayLabel):
        self._InstanceDisplayLabel = InstanceDisplayLabel


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._ZoneName = params.get("ZoneName")
        self._InstanceDisplayLabel = params.get("InstanceDisplayLabel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        