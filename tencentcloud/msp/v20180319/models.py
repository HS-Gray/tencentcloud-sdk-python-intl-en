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


class DeregisterMigrationTaskRequest(AbstractModel):
    """DeregisterMigrationTask request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeregisterMigrationTaskResponse(AbstractModel):
    """DeregisterMigrationTask response structure.

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


class DescribeMigrationTaskRequest(AbstractModel):
    """DescribeMigrationTask request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID, such as msp-jitoh33n
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMigrationTaskResponse(AbstractModel):
    """DescribeMigrationTask response structure.

    """

    def __init__(self):
        r"""
        :param _TaskStatus: Migration details list
        :type TaskStatus: list of TaskStatus
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskStatus = None
        self._RequestId = None

    @property
    def TaskStatus(self):
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TaskStatus") is not None:
            self._TaskStatus = []
            for item in params.get("TaskStatus"):
                obj = TaskStatus()
                obj._deserialize(item)
                self._TaskStatus.append(obj)
        self._RequestId = params.get("RequestId")


class DstInfo(AbstractModel):
    """Migration destination information

    """

    def __init__(self):
        r"""
        :param _Region: Migration destination region
        :type Region: str
        :param _Ip: 
        :type Ip: str
        :param _Port: Migration destination port
        :type Port: str
        :param _InstanceId: Migration destination instance ID
        :type InstanceId: str
        """
        self._Region = None
        self._Ip = None
        self._Port = None
        self._InstanceId = None

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListMigrationProjectRequest(AbstractModel):
    """ListMigrationProject request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: The initial number of records, default value: 0
        :type Offset: int
        :param _Limit: The number of records returned, default value: 500
        :type Limit: int
        """
        self._Offset = None
        self._Limit = None

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
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListMigrationProjectResponse(AbstractModel):
    """ListMigrationProject response structure.

    """

    def __init__(self):
        r"""
        :param _Projects: Project list
        :type Projects: list of Project
        :param _TotalCount: Total number of projects
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Projects = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Projects(self):
        return self._Projects

    @Projects.setter
    def Projects(self, Projects):
        self._Projects = Projects

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
        if params.get("Projects") is not None:
            self._Projects = []
            for item in params.get("Projects"):
                obj = Project()
                obj._deserialize(item)
                self._Projects.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class ListMigrationTaskRequest(AbstractModel):
    """ListMigrationTask request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: The initial number of records, default value: 0
        :type Offset: int
        :param _Limit: Number of records, default value: 10
        :type Limit: int
        :param _ProjectId: Project ID, the default value is empty.
        :type ProjectId: int
        """
        self._Offset = None
        self._Limit = None
        self._ProjectId = None

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
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListMigrationTaskResponse(AbstractModel):
    """ListMigrationTask response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of records
        :type TotalCount: int
        :param _Tasks: Migration task list
        :type Tasks: list of Task
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Tasks = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Tasks(self):
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = Task()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._RequestId = params.get("RequestId")


class ModifyMigrationTaskBelongToProjectRequest(AbstractModel):
    """ModifyMigrationTaskBelongToProject request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID, such as msp-jitoh33n
        :type TaskId: str
        :param _ProjectId: Project ID, such as 10005
        :type ProjectId: int
        """
        self._TaskId = None
        self._ProjectId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMigrationTaskBelongToProjectResponse(AbstractModel):
    """ModifyMigrationTaskBelongToProject response structure.

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


class ModifyMigrationTaskStatusRequest(AbstractModel):
    """ModifyMigrationTaskStatus request structure.

    """

    def __init__(self):
        r"""
        :param _Status: Task status, valid values include `unstart` (migration has not started), `migrating` (migration in progress), `finish` (migration completed) or `fail` (migration failed).
        :type Status: str
        :param _TaskId: Task ID, such as msp-jitoh33n
        :type TaskId: str
        """
        self._Status = None
        self._TaskId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMigrationTaskStatusResponse(AbstractModel):
    """ModifyMigrationTaskStatus response structure.

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


class Project(AbstractModel):
    """List type

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID
        :type ProjectId: int
        :param _ProjectName: Project name
        :type ProjectName: str
        """
        self._ProjectId = None
        self._ProjectName = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ProjectName = params.get("ProjectName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterMigrationTaskRequest(AbstractModel):
    """RegisterMigrationTask request structure.

    """

    def __init__(self):
        r"""
        :param _TaskType: Task type, valid values include `database` (database migration), `file` (file migration) or `host` (host migration).
        :type TaskType: str
        :param _TaskName: Task name
        :type TaskName: str
        :param _ServiceSupplier: Service supplier name
        :type ServiceSupplier: str
        :param _CreateTime: Migration task creation time
        :type CreateTime: str
        :param _UpdateTime: Migration task update time
        :type UpdateTime: str
        :param _MigrateClass: Migration type, for example `mysql:mysql` in database migration means migration from mysql to mysql and `oss:cos` in file migration means migration from Alibaba Cloud OSS to Tencent COS.
        :type MigrateClass: str
        :param _SrcInfo: Migration task source information
        :type SrcInfo: :class:`tencentcloud.msp.v20180319.models.SrcInfo`
        :param _DstInfo: Migration task destination information
        :type DstInfo: :class:`tencentcloud.msp.v20180319.models.DstInfo`
        :param _SrcAccessType: Source instance access type. Valid values for database migration include `extranet` (public network), `cvm` (CVM-created instance), `dcg` (Direct Connect-enabled instance), `vpncloud` (Tencent Cloud VPN-enabled instance), `vpnselfbuild` (self-built VPN-enabled instance), `cdb` (TencentDB instance)
        :type SrcAccessType: str
        :param _SrcDatabaseType: Database type of the source instance. Valid values for database migration: `mysql`, `redis`, `percona`, `mongodb`, `postgresql`, `sqlserver`, `mariadb`
        :type SrcDatabaseType: str
        :param _DstAccessType: Target instance access type. Valid values for database migration include `extranet` (public network), `cvm` (CVM-created instance), `dcg` (Direct Connect-enabled instance), `vpncloud` (Tencent Cloud VPN-enabled instance), `vpnselfbuild` (self-built VPN-enabled instance), `cdb` (TencentDB instance)
        :type DstAccessType: str
        :param _DstDatabaseType: Database type of the target instance. Valid values for database migration: `mysql`, `redis`, `percona`, `mongodb`, `postgresql`, `sqlserver`, `mariadb`
        :type DstDatabaseType: str
        """
        self._TaskType = None
        self._TaskName = None
        self._ServiceSupplier = None
        self._CreateTime = None
        self._UpdateTime = None
        self._MigrateClass = None
        self._SrcInfo = None
        self._DstInfo = None
        self._SrcAccessType = None
        self._SrcDatabaseType = None
        self._DstAccessType = None
        self._DstDatabaseType = None

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def TaskName(self):
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def ServiceSupplier(self):
        return self._ServiceSupplier

    @ServiceSupplier.setter
    def ServiceSupplier(self, ServiceSupplier):
        self._ServiceSupplier = ServiceSupplier

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def MigrateClass(self):
        return self._MigrateClass

    @MigrateClass.setter
    def MigrateClass(self, MigrateClass):
        self._MigrateClass = MigrateClass

    @property
    def SrcInfo(self):
        return self._SrcInfo

    @SrcInfo.setter
    def SrcInfo(self, SrcInfo):
        self._SrcInfo = SrcInfo

    @property
    def DstInfo(self):
        return self._DstInfo

    @DstInfo.setter
    def DstInfo(self, DstInfo):
        self._DstInfo = DstInfo

    @property
    def SrcAccessType(self):
        return self._SrcAccessType

    @SrcAccessType.setter
    def SrcAccessType(self, SrcAccessType):
        self._SrcAccessType = SrcAccessType

    @property
    def SrcDatabaseType(self):
        return self._SrcDatabaseType

    @SrcDatabaseType.setter
    def SrcDatabaseType(self, SrcDatabaseType):
        self._SrcDatabaseType = SrcDatabaseType

    @property
    def DstAccessType(self):
        return self._DstAccessType

    @DstAccessType.setter
    def DstAccessType(self, DstAccessType):
        self._DstAccessType = DstAccessType

    @property
    def DstDatabaseType(self):
        return self._DstDatabaseType

    @DstDatabaseType.setter
    def DstDatabaseType(self, DstDatabaseType):
        self._DstDatabaseType = DstDatabaseType


    def _deserialize(self, params):
        self._TaskType = params.get("TaskType")
        self._TaskName = params.get("TaskName")
        self._ServiceSupplier = params.get("ServiceSupplier")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._MigrateClass = params.get("MigrateClass")
        if params.get("SrcInfo") is not None:
            self._SrcInfo = SrcInfo()
            self._SrcInfo._deserialize(params.get("SrcInfo"))
        if params.get("DstInfo") is not None:
            self._DstInfo = DstInfo()
            self._DstInfo._deserialize(params.get("DstInfo"))
        self._SrcAccessType = params.get("SrcAccessType")
        self._SrcDatabaseType = params.get("SrcDatabaseType")
        self._DstAccessType = params.get("DstAccessType")
        self._DstDatabaseType = params.get("DstDatabaseType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterMigrationTaskResponse(AbstractModel):
    """RegisterMigrationTask response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID
        :type TaskId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class SrcInfo(AbstractModel):
    """Migration source information

    """

    def __init__(self):
        r"""
        :param _Region: Migration source region
        :type Region: str
        :param _Ip: 
        :type Ip: str
        :param _Port: Migration source port
        :type Port: str
        :param _InstanceId: Migration source instance ID
        :type InstanceId: str
        """
        self._Region = None
        self._Ip = None
        self._Port = None
        self._InstanceId = None

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Task(AbstractModel):
    """Migration task type

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID
        :type TaskId: str
        :param _TaskName: Task name
        :type TaskName: str
        :param _MigrationType: Migration type
        :type MigrationType: str
        :param _Status: Migration status
        :type Status: str
        :param _ProjectId: Project ID
        :type ProjectId: int
        :param _ProjectName: Project name
        :type ProjectName: str
        :param _SrcInfo: Migration source information
        :type SrcInfo: :class:`tencentcloud.msp.v20180319.models.SrcInfo`
        :param _MigrationTimeLine: Migration time information
        :type MigrationTimeLine: :class:`tencentcloud.msp.v20180319.models.TimeObj`
        :param _Updated: Status update time
        :type Updated: str
        :param _DstInfo: Migration destination information
        :type DstInfo: :class:`tencentcloud.msp.v20180319.models.DstInfo`
        """
        self._TaskId = None
        self._TaskName = None
        self._MigrationType = None
        self._Status = None
        self._ProjectId = None
        self._ProjectName = None
        self._SrcInfo = None
        self._MigrationTimeLine = None
        self._Updated = None
        self._DstInfo = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskName(self):
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def MigrationType(self):
        return self._MigrationType

    @MigrationType.setter
    def MigrationType(self, MigrationType):
        self._MigrationType = MigrationType

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def SrcInfo(self):
        return self._SrcInfo

    @SrcInfo.setter
    def SrcInfo(self, SrcInfo):
        self._SrcInfo = SrcInfo

    @property
    def MigrationTimeLine(self):
        return self._MigrationTimeLine

    @MigrationTimeLine.setter
    def MigrationTimeLine(self, MigrationTimeLine):
        self._MigrationTimeLine = MigrationTimeLine

    @property
    def Updated(self):
        return self._Updated

    @Updated.setter
    def Updated(self, Updated):
        self._Updated = Updated

    @property
    def DstInfo(self):
        return self._DstInfo

    @DstInfo.setter
    def DstInfo(self, DstInfo):
        self._DstInfo = DstInfo


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TaskName = params.get("TaskName")
        self._MigrationType = params.get("MigrationType")
        self._Status = params.get("Status")
        self._ProjectId = params.get("ProjectId")
        self._ProjectName = params.get("ProjectName")
        if params.get("SrcInfo") is not None:
            self._SrcInfo = SrcInfo()
            self._SrcInfo._deserialize(params.get("SrcInfo"))
        if params.get("MigrationTimeLine") is not None:
            self._MigrationTimeLine = TimeObj()
            self._MigrationTimeLine._deserialize(params.get("MigrationTimeLine"))
        self._Updated = params.get("Updated")
        if params.get("DstInfo") is not None:
            self._DstInfo = DstInfo()
            self._DstInfo._deserialize(params.get("DstInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskStatus(AbstractModel):
    """Migration details list

    """

    def __init__(self):
        r"""
        :param _Status: Migration status
        :type Status: str
        :param _Progress: Migration progress
        :type Progress: str
        :param _UpdateTime: Migration date
        :type UpdateTime: str
        """
        self._Status = None
        self._Progress = None
        self._UpdateTime = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Progress(self):
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Progress = params.get("Progress")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimeObj(AbstractModel):
    """Time object

    """

    def __init__(self):
        r"""
        :param _CreateTime: The creation time
        :type CreateTime: str
        :param _EndTime: End time
        :type EndTime: str
        """
        self._CreateTime = None
        self._EndTime = None

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._CreateTime = params.get("CreateTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        