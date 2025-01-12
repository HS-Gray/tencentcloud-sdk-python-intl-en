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


class DetectReflectLivenessAndCompareRequest(AbstractModel):
    """DetectReflectLivenessAndCompare request structure.

    """

    def __init__(self):
        r"""
        :param LiveDataUrl: URL of the liveness detection data package generated by the SDK
        :type LiveDataUrl: str
        :param LiveDataMd5: MD5 hash value (32-bit) of the liveness detection data package generated by the SDK, which is used to verify the LiveData consistency.
        :type LiveDataMd5: str
        :param ImageUrl: URL of the target image for comparison
        :type ImageUrl: str
        :param ImageMd5: MD5 hash value (32-bit) of the target image for comparison, which is used to verify the `Image` consistency.
        :type ImageMd5: str
        """
        self.LiveDataUrl = None
        self.LiveDataMd5 = None
        self.ImageUrl = None
        self.ImageMd5 = None


    def _deserialize(self, params):
        self.LiveDataUrl = params.get("LiveDataUrl")
        self.LiveDataMd5 = params.get("LiveDataMd5")
        self.ImageUrl = params.get("ImageUrl")
        self.ImageMd5 = params.get("ImageMd5")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetectReflectLivenessAndCompareResponse(AbstractModel):
    """DetectReflectLivenessAndCompare response structure.

    """

    def __init__(self):
        r"""
        :param BestFrameUrl: Temporary URL of the best screenshot (.jpg) of the video after successful verification. Both the screenshot and the URL are valid for two hours only, so you need to download the screenshot within this period.
        :type BestFrameUrl: str
        :param BestFrameMd5: MD5 hash value (32-bit) of the best screenshot of the video after successful verification, which is used to verify the `BestFrame` consistency.
        :type BestFrameMd5: str
        :param Result: Service error code. `Success` will be returned for success. For error information, see the `FailedOperation` section in the error code list below.
        :type Result: str
        :param Description: Service result description
        :type Description: str
        :param Sim: Similarity. Value range: [0.00, 100.00]. As a recommendation, when the similarity is greater than or equal to 70, it can be determined that the two faces are of the same person. You can adjust the threshold according to your specific scenario (the FAR at the threshold of 70 is 0.1%, and FAR at the threshold of 80 is 0.01%).
        :type Sim: float
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.BestFrameUrl = None
        self.BestFrameMd5 = None
        self.Result = None
        self.Description = None
        self.Sim = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BestFrameUrl = params.get("BestFrameUrl")
        self.BestFrameMd5 = params.get("BestFrameMd5")
        self.Result = params.get("Result")
        self.Description = params.get("Description")
        self.Sim = params.get("Sim")
        self.RequestId = params.get("RequestId")


class LivenessCompareRequest(AbstractModel):
    """LivenessCompare request structure.

    """

    def __init__(self):
        r"""
        :param LivenessType: Liveness detection type. Valid values: LIP/ACTION/SILENT.
LIP: numeric mode; ACTION: motion mode; SILENT: silent mode. You need to select a mode to input.
        :type LivenessType: str
        :param ImageBase64: Base64 string of the image for face comparison.
The size of the Base64-encoded image data can be up to 3 MB. JPG and PNG formats are supported.
Please use the standard Base64 encoding scheme (with the "=" padding). For the encoding conventions, please see RFC 4648.

Either the `ImageUrl` or `ImageBase64` of the image must be provided. If both are provided, only `ImageBase64` will be used.
        :type ImageBase64: str
        :param ImageUrl: URL of the image for face comparison. The size of the downloaded image after Base64 encoding can be up to 3 MB. JPG and PNG formats are supported.

Either the `ImageUrl` or `ImageBase64` of the image must be provided. If both are provided, only `ImageBase64` will be used.

We recommend you store the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability. The download speed and stability of non-Tencent Cloud URLs may be low.
        :type ImageUrl: str
        :param ValidateData: Lip mode: set this parameter to a custom 4-digit verification code.
Action mode: set this parameter to a custom action sequence (e.g., `2,1` or `1,2`).
Silent mode: do not pass in this parameter.
        :type ValidateData: str
        :param Optional: Optional configuration (a JSON string)
{
"BestFrameNum": 2  // Return multiple best screenshots. Value range: 2−10
}
        :type Optional: str
        :param VideoBase64: Base64 string of the video for liveness detection.
The size of the Base64-encoded video data can be up to 8 MB. MP4, AVI, and FLV formats are supported.
Please use the standard Base64 encoding scheme (with the "=" padding). For the encoding conventions, please see RFC 4648.

Either the `VideoUrl` or `VideoBase64` of the video must be provided. If both are provided, only `VideoBase64` will be used.
        :type VideoBase64: str
        :param VideoUrl: URL of the video for liveness detection. The size of the downloaded video after Base64 encoding can be up to 8 MB. It takes no more than 4 seconds to download. MP4, AVI, and FLV formats are supported.

Either the `VideoUrl` or `VideoBase64` of the video must be provided. If both are provided, only `VideoBase64` will be used.

We recommend you store the video in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability. The download speed and stability of non-Tencent Cloud URLs may be low.
        :type VideoUrl: str
        """
        self.LivenessType = None
        self.ImageBase64 = None
        self.ImageUrl = None
        self.ValidateData = None
        self.Optional = None
        self.VideoBase64 = None
        self.VideoUrl = None


    def _deserialize(self, params):
        self.LivenessType = params.get("LivenessType")
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.ValidateData = params.get("ValidateData")
        self.Optional = params.get("Optional")
        self.VideoBase64 = params.get("VideoBase64")
        self.VideoUrl = params.get("VideoUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LivenessCompareResponse(AbstractModel):
    """LivenessCompare response structure.

    """

    def __init__(self):
        r"""
        :param BestFrameBase64: The best screenshot of the video after successful verification. The photo is Base64-encoded and in JPG format.
        :type BestFrameBase64: str
        :param Sim: Similarity. Value range: [0.00, 100.00]. As a recommendation, when the similarity is greater than or equal to 70, it can be determined that the two faces are of the same person. You can adjust the threshold according to your specific scenario (the FAR at the threshold of 70 is 0.1%, and FAR at the threshold of 80 is 0.01%).
        :type Sim: float
        :param Result: Service error code. `Success` will be returned for success. For error information, please see the `FailedOperation` section in the error code list below.
        :type Result: str
        :param Description: Service result description.
        :type Description: str
        :param BestFrameList: 
        :type BestFrameList: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.BestFrameBase64 = None
        self.Sim = None
        self.Result = None
        self.Description = None
        self.BestFrameList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BestFrameBase64 = params.get("BestFrameBase64")
        self.Sim = params.get("Sim")
        self.Result = params.get("Result")
        self.Description = params.get("Description")
        self.BestFrameList = params.get("BestFrameList")
        self.RequestId = params.get("RequestId")