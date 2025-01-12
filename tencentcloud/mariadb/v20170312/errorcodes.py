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


# CAM signature/authentication error
AUTHFAILURE = 'AuthFailure'

# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# Failed to add the security group information of an instance.
FAILEDOPERATION_ADDINSTANCEINFOFAILED = 'FailedOperation.AddInstanceInfoFailed'

# Failed to associate the security group.
FAILEDOPERATION_ASSOCIATESECURITYGROUPSFAILED = 'FailedOperation.AssociateSecurityGroupsFailed'

# Authentication failed.
FAILEDOPERATION_AUTHNOSTRATEGY = 'FailedOperation.AuthNoStrategy'

# Failed to clear the security group information of an instance.
FAILEDOPERATION_CLEARINSTANCEINFOFAILED = 'FailedOperation.ClearInstanceInfoFailed'

# An error occurred while copying account permissions.
FAILEDOPERATION_COPYRIGHTERROR = 'FailedOperation.CopyRightError'

# Failed to create the flow.
FAILEDOPERATION_CREATEFLOWFAILED = 'FailedOperation.CreateFlowFailed'

# Failed to create an order.
FAILEDOPERATION_CREATEORDERFAILED = 'FailedOperation.CreateOrderFailed'

# Failed to create the account.
FAILEDOPERATION_CREATEUSERFAILED = 'FailedOperation.CreateUserFailed'

# Failed to delete the account.
FAILEDOPERATION_DELETEUSERFAILED = 'FailedOperation.DeleteUserFailed'

# Failed to unassociate the security group.
FAILEDOPERATION_DISASSOCIATESECURITYGROUPSFAILED = 'FailedOperation.DisassociateSecurityGroupsFailed'

# Failed to modify account permissions.
FAILEDOPERATION_MODIFYRIGHTFAILED = 'FailedOperation.ModifyRightFailed'

# Failed to request the backend API.
FAILEDOPERATION_OSSOPERATIONFAILED = 'FailedOperation.OssOperationFailed'

# Failed to reset the account password.
FAILEDOPERATION_RESETPASSWORDFAILED = 'FailedOperation.ResetPasswordFailed'

# Failed to set a rule.
FAILEDOPERATION_SETRULELOCATIONFAILED = 'FailedOperation.SetRuleLocationFailed'

# Either tag key/value verification or tag API authentication failed.
FAILEDOPERATION_TAGDRYRUNERROR = 'FailedOperation.TagDryRunError'

# Failed to update the security group information of an instance.
FAILEDOPERATION_UPDATEINSTANCEINFOFAILED = 'FailedOperation.UpdateInstanceInfoFailed'

# Internal error.
INTERNALERROR = 'InternalError'

# CAM authentication request failed.
INTERNALERROR_CAMAUTHFAILED = 'InternalError.CamAuthFailed'

# Invalid COS address configuration.
INTERNALERROR_COSCONFIGURATION = 'InternalError.CosConfiguration'

# Backup file signature failed.
INTERNALERROR_COSSIGNURL = 'InternalError.CosSignUrl'

# Failed to create a task.
INTERNALERROR_CREATEFLOWFAILED = 'InternalError.CreateFlowFailed'

# No database data has changed.
INTERNALERROR_DBROWSAFFECTEDERROR = 'InternalError.DBRowsAffectedError'

# Failed to query the database.
INTERNALERROR_DBOPERATIONFAILED = 'InternalError.DbOperationFailed'

# Failed to query the information of a dedicated cluster.
INTERNALERROR_FENCEERROR = 'InternalError.FenceError'

# Failed to get the backend instance information.
INTERNALERROR_GETINSTANCEINFOFAILED = 'InternalError.GetInstanceInfoFailed'

# Failed to get the current account permissions.
INTERNALERROR_GETRIGHTFAILED = 'InternalError.GetRightFailed'

# Failed to query security group details.
INTERNALERROR_GETSECURITYGROUPDETAILFAILED = 'InternalError.GetSecurityGroupDetailFailed'

# Failed to query the VPC subnet information.
INTERNALERROR_GETSUBNETFAILED = 'InternalError.GetSubnetFailed'

# Failed to get the account list.
INTERNALERROR_GETUSERLISTFAILED = 'InternalError.GetUserListFailed'

# Failed to query the security group quota of the user.
INTERNALERROR_GETUSGQUOTAERROR = 'InternalError.GetUsgQuotaError'

# Failed to query the VPC information.
INTERNALERROR_GETVPCFAILED = 'InternalError.GetVpcFailed'

# Failed to read the backup file.
INTERNALERROR_HDFSERROR = 'InternalError.HDFSError'

# Missing internal configuration.
INTERNALERROR_INNERCONFIGURATIONMISSING = 'InternalError.InnerConfigurationMissing'

# Internal system error.
INTERNALERROR_INNERSYSTEMERROR = 'InternalError.InnerSystemError'

# Failed to insert data into the database.
INTERNALERROR_INSERTFAIL = 'InternalError.InsertFail'

# You have no permission to operate this instance.
INTERNALERROR_INSTANCEOPERATEPERMISSIONERROR = 'InternalError.InstanceOperatePermissionError'

# The maximum number of security groups with which a single instance can associate has been reached.
INTERNALERROR_INSTANCESGOVERLIMITERROR = 'InternalError.InstanceSGOverLimitError'

# The number of resources returned is inconsistent with the number specified in the request of querying instance information.
INTERNALERROR_LISTINSTANCERESPRESOURCECOUNTNOTMATCHERROR = 'InternalError.ListInstanceRespResourceCountNotMatchError'

# An error occurred when querying an instance.
INTERNALERROR_LISTINSTANCESERROR = 'InternalError.ListInstancesError'

# Database operation failed.
INTERNALERROR_OPERATEDATABASEFAILED = 'InternalError.OperateDatabaseFailed'

# An error occurred when reading data from the database.
INTERNALERROR_QUERYDATABASEFAILED = 'InternalError.QueryDatabaseFailed'

# An error occurred when reading data from the database.
INTERNALERROR_READDATABASEFAILED = 'InternalError.ReadDatabaseFailed'

# Route not found.
INTERNALERROR_ROUTENOTFOUND = 'InternalError.RouteNotFound'

# The security group policy of the resource failed to take effect.
INTERNALERROR_SETSVCLOCATIONFAILED = 'InternalError.SetSvcLocationFailed'

# Failed to update the database.
INTERNALERROR_UPDATEDATABASEFAILED = 'InternalError.UpdateDatabaseFailed'

# Public network operation failed.
INTERNALERROR_WANSERVICEFAILED = 'InternalError.WanServiceFailed'

# Parameter error.
INVALIDPARAMETER = 'InvalidParameter'

# The password contains invalid characters.
INVALIDPARAMETER_CHARACTERERROR = 'InvalidParameter.CharacterError'

# Verification of input parameters failed.
INVALIDPARAMETER_CHECKPARAMNOTPASS = 'InvalidParameter.CheckParamNotPass'

# An error occurred while verifying parameter validity.
INVALIDPARAMETER_GENERICPARAMETERERROR = 'InvalidParameter.GenericParameterError'

# Invalid parameters
INVALIDPARAMETER_ILLEGALPARAMETERERROR = 'InvalidParameter.IllegalParameterError'

# Failed to find the requested instance.
INVALIDPARAMETER_INSTANCENOTFOUND = 'InvalidParameter.InstanceNotFound'

# You have no permission to manipulate this API or resource.
INVALIDPARAMETER_PERMISSIONDENIED = 'InvalidParameter.PermissionDenied'

# Security group validity test failed.
INVALIDPARAMETER_SGCHECKFAIL = 'InvalidParameter.SGCheckFail'

# The instance shard does not exist.
INVALIDPARAMETER_SHARDRESOURCEIDNOTFOUND = 'InvalidParameter.ShardResourceIdNotFound'

# The specified VPC subnet was not found.
INVALIDPARAMETER_SUBNETNOTFOUND = 'InvalidParameter.SubnetNotFound'

# The specified VPC subnet was not found.
INVALIDPARAMETER_VPCNOTFOUND = 'InvalidParameter.VpcNotFound'

# The account to be created already exists.
INVALIDPARAMETERVALUE_ACCOUNTALREADYEXISTS = 'InvalidParameterValue.AccountAlreadyExists'

# The specified permission could not be granted to this account.
INVALIDPARAMETERVALUE_BADUSERRIGHT = 'InvalidParameterValue.BadUserRight'

# Invalid account type.
INVALIDPARAMETERVALUE_BADUSERTYPE = 'InvalidParameterValue.BadUserType'

# The dedicated cluster to which the database instance belongs was not found.
INVALIDPARAMETERVALUE_ILLEGALEXCLUSTERID = 'InvalidParameterValue.IllegalExclusterID'

# The number of products exceeds the upper limit.
INVALIDPARAMETERVALUE_ILLEGALQUANTITY = 'InvalidParameterValue.IllegalQuantity'

# Incorrect permission parameters
INVALIDPARAMETERVALUE_ILLEGALRIGHTPARAM = 'InvalidParameterValue.IllegalRightParam'

# Information of the specified AZ was not found.
INVALIDPARAMETERVALUE_ILLEGALZONE = 'InvalidParameterValue.IllegalZone'

# Parameter verification error.
INVALIDPARAMETERVALUE_INVALIDPARAMETERVALUEERROR = 'InvalidParameterValue.InvalidParameterValueError'

# The specification information of the database instance was not found.
INVALIDPARAMETERVALUE_SPECIDILLEGAL = 'InvalidParameterValue.SpecIdIllegal'

# Operations by a system user are not allowed.
INVALIDPARAMETERVALUE_SUPERUSERFORBIDDEN = 'InvalidParameterValue.SuperUserForbidden'

# The specified account does not exist.
RESOURCENOTFOUND_ACCOUNTDOESNOTEXIST = 'ResourceNotFound.AccountDoesNotExist'

# The instance does not exist.
RESOURCENOTFOUND_INSTANCENOTFOUND = 'ResourceNotFound.InstanceNotFound'

# The specified database instance was not found.
RESOURCENOTFOUND_NOINSTANCEFOUND = 'ResourceNotFound.NoInstanceFound'

# Failed to find the configuration of the product associated with the security group.
RESOURCENOTFOUND_PRODUCTCONFIGNOTEXISTEDERROR = 'ResourceNotFound.ProductConfigNotExistedError'

# The sync task has been deleted.
RESOURCENOTFOUND_SYNCTASKDELETED = 'ResourceNotFound.SyncTaskDeleted'

# An error occurred while calling COS APIs.
RESOURCEUNAVAILABLE_COSAPIFAILED = 'ResourceUnavailable.CosApiFailed'

# The database instance has been deleted.
RESOURCEUNAVAILABLE_INSTANCEALREADYDELETED = 'ResourceUnavailable.InstanceAlreadyDeleted'

# The database instance has been locked. Operations are not allowed.
RESOURCEUNAVAILABLE_INSTANCEHASBEENLOCKED = 'ResourceUnavailable.InstanceHasBeenLocked'

# Incorrect database instance status. Operations are not allowed.
RESOURCEUNAVAILABLE_INSTANCESTATUSABNORMAL = 'ResourceUnavailable.InstanceStatusAbnormal'

# You have no permission to manipulate this API or resource.
UNAUTHORIZEDOPERATION_PERMISSIONDENIED = 'UnauthorizedOperation.PermissionDenied'

# The proxy program is too old. Please contact customer service for upgrade and try again.
UNSUPPORTEDOPERATION_OLDPROXYVERSION = 'UnsupportedOperation.OldProxyVersion'
