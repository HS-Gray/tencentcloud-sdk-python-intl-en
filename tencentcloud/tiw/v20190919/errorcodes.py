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


# Failed to download the document. To correct this, check whether the URL in the request parameter is correct. If you are using another file storage service, check the upload bandwidth of the file storage service. The document transcoding service supports downloading with a maximum duration of 1 minute. If the download fails, the transcoding request will also fail.
FAILEDOPERATION_FILEDOWNLOADFAIL = 'FailedOperation.FileDownloadFail'

# The document format is invalid. Read-only or encrypted documents cannot be transcoded.
FAILEDOPERATION_FILEFORMATERROR = 'FailedOperation.FileFormatError'

# Failed to open the document. To correct this, check whether the document for transcoding is encrypted or encounters other format issues.
FAILEDOPERATION_FILEOPENFAIL = 'FailedOperation.FileOpenFail'

# Failed to upload the transcoding result. To correct this, try again later.
FAILEDOPERATION_FILEUPLOADFAIL = 'FailedOperation.FileUploadFail'

# Failed to record. For more information, see the error description.
FAILEDOPERATION_RECORD = 'FailedOperation.Record'

# Failed to transcode. For more information, see the error description or contact our customer service.
FAILEDOPERATION_TRANSCODE = 'FailedOperation.Transcode'

# The transcoding service encountered an internal error. Please try again later or contact our customer service.
FAILEDOPERATION_TRANSCODESERVERERROR = 'FailedOperation.TranscodeServerError'

# A parameter error occurred.
INVALIDPARAMETER = 'InvalidParameter'

# The parameter type does not match.
INVALIDPARAMETER_BODYPARAMETERTYPEUNMATCHED = 'InvalidParameter.BodyParameterTypeUnmatched'

# The callback address format is invalid.
INVALIDPARAMETER_CALLBACKADDRESSFORMATERROR = 'InvalidParameter.CallbackAddressFormatError'

# The document extension is not supported.
INVALIDPARAMETER_FILEFORMATUNSUPPORTED = 'InvalidParameter.FileFormatUnsupported'

# The specified special feature does not exist.
INVALIDPARAMETER_INVALIDEXTRA = 'InvalidParameter.InvalidExtra'

# The format of the real-time recording parameter is invalid.
INVALIDPARAMETER_RECORDPARAMETER = 'InvalidParameter.RecordParameter'

# The SdkAppId does not exist or is invalid.
INVALIDPARAMETER_SDKAPPIDNOTFOUND = 'InvalidParameter.SdkAppIdNotFound'

# The task to query does not exist.
INVALIDPARAMETER_TASKNOTFOUND = 'InvalidParameter.TaskNotFound'

# The document transcoding parameter format is invalid.
INVALIDPARAMETER_TRANSCODEPARAMETER = 'InvalidParameter.TranscodeParameter'

# The document download URL format is invalid. To correct this, check the URL in the request parameter.
INVALIDPARAMETER_URLFORMATERROR = 'InvalidParameter.UrlFormatError'

# The number of concurrent transcoding or recording tasks exceeds the limit. For more information, see the error description or try again later.
LIMITEXCEEDED_TASKCONCURRENCY = 'LimitExceeded.TaskConcurrency'

# The number of pages exceeds the limit. Transcoding a file with more than 500 pages is currently unsupported. If you do need this feature, contact our customer service.
LIMITEXCEEDED_TRANSCODEPAGESLIMITATION = 'LimitExceeded.TranscodePagesLimitation'

# The recording user account for real-time recording has started another recording task.
RESOURCEINUSE_RECORDUSERID = 'ResourceInUse.RecordUserId'

# TIW is not enabled.
RESOURCEUNAVAILABLE_NOTREGISTERED = 'ResourceUnavailable.NotRegistered'

# The account is in arrears or the TIW service has expired.
RESOURCEUNAVAILABLE_SERVICEEXPIRED = 'ResourceUnavailable.ServiceExpired'

# The SdkAppId does not exist or does not match the current Tencent Cloud account.
UNAUTHORIZEDOPERATION_SDKAPPID = 'UnauthorizedOperation.SdkAppId'

# The specified operation cannot be performed for pending tasks in this state. For example, you cannot resume recording for a recording task.
UNSUPPORTEDOPERATION_INVALIDTASKSTATUS = 'UnsupportedOperation.InvalidTaskStatus'

# The task is completed, and therefore the specified operation cannot be performed.
UNSUPPORTEDOPERATION_TASKHASALREADYSTOPPED = 'UnsupportedOperation.TaskHasAlreadyStopped'
