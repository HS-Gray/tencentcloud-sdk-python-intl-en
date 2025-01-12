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


class AIAnalysisTemplateItem(AbstractModel):
    """AI-based intelligent analysis template details

    """

    def __init__(self):
        r"""
        :param Definition: Unique ID of intelligent analysis template.
        :type Definition: int
        :param Name: Intelligent analysis template name.
        :type Name: str
        :param Comment: Intelligent analysis template description.
        :type Comment: str
        :param ClassificationConfigure: Control parameter of intelligent categorization task.
        :type ClassificationConfigure: :class:`tencentcloud.mps.v20190612.models.ClassificationConfigureInfo`
        :param TagConfigure: Control parameter of intelligent tagging task.
        :type TagConfigure: :class:`tencentcloud.mps.v20190612.models.TagConfigureInfo`
        :param CoverConfigure: Control parameter of intelligent cover generating task.
        :type CoverConfigure: :class:`tencentcloud.mps.v20190612.models.CoverConfigureInfo`
        :param FrameTagConfigure: Control parameter of intelligent frame-specific tagging task.
        :type FrameTagConfigure: :class:`tencentcloud.mps.v20190612.models.FrameTagConfigureInfo`
        :param CreateTime: Creation time of template in [ISO date format](https://intl.cloud.tencent.com/document/product/862/37710?from_cn_redirect=1#52).
        :type CreateTime: str
        :param UpdateTime: Last modified time of template in [ISO date format](https://intl.cloud.tencent.com/document/product/862/37710?from_cn_redirect=1#52).
        :type UpdateTime: str
        :param Type: The template type. Valid values:
* Preset
* Custom
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Type: str
        """
        self.Definition = None
        self.Name = None
        self.Comment = None
        self.ClassificationConfigure = None
        self.TagConfigure = None
        self.CoverConfigure = None
        self.FrameTagConfigure = None
        self.CreateTime = None
        self.UpdateTime = None
        self.Type = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("ClassificationConfigure") is not None:
            self.ClassificationConfigure = ClassificationConfigureInfo()
            self.ClassificationConfigure._deserialize(params.get("ClassificationConfigure"))
        if params.get("TagConfigure") is not None:
            self.TagConfigure = TagConfigureInfo()
            self.TagConfigure._deserialize(params.get("TagConfigure"))
        if params.get("CoverConfigure") is not None:
            self.CoverConfigure = CoverConfigureInfo()
            self.CoverConfigure._deserialize(params.get("CoverConfigure"))
        if params.get("FrameTagConfigure") is not None:
            self.FrameTagConfigure = FrameTagConfigureInfo()
            self.FrameTagConfigure._deserialize(params.get("FrameTagConfigure"))
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AIRecognitionTemplateItem(AbstractModel):
    """Details of a video content recognition template

    """

    def __init__(self):
        r"""
        :param Definition: Unique ID of a video content recognition template.
        :type Definition: int
        :param Name: Name of a video content recognition template.
        :type Name: str
        :param Comment: Description of a video content recognition template.
        :type Comment: str
        :param FaceConfigure: Face recognition control parameter.
Note: This field may return null, indicating that no valid values can be obtained.
        :type FaceConfigure: :class:`tencentcloud.mps.v20190612.models.FaceConfigureInfo`
        :param OcrFullTextConfigure: Full text recognition control parameter.
Note: This field may return null, indicating that no valid values can be obtained.
        :type OcrFullTextConfigure: :class:`tencentcloud.mps.v20190612.models.OcrFullTextConfigureInfo`
        :param OcrWordsConfigure: Text keyword recognition control parameter.
Note: This field may return null, indicating that no valid values can be obtained.
        :type OcrWordsConfigure: :class:`tencentcloud.mps.v20190612.models.OcrWordsConfigureInfo`
        :param AsrFullTextConfigure: Full speech recognition control parameter.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AsrFullTextConfigure: :class:`tencentcloud.mps.v20190612.models.AsrFullTextConfigureInfo`
        :param AsrWordsConfigure: Speech keyword recognition control parameter.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AsrWordsConfigure: :class:`tencentcloud.mps.v20190612.models.AsrWordsConfigureInfo`
        :param CreateTime: Creation time of a template in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F).
        :type CreateTime: str
        :param UpdateTime: Last modified time of a template in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F).
        :type UpdateTime: str
        :param Type: The template type. Valid values:
* Preset
* Custom
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Type: str
        """
        self.Definition = None
        self.Name = None
        self.Comment = None
        self.FaceConfigure = None
        self.OcrFullTextConfigure = None
        self.OcrWordsConfigure = None
        self.AsrFullTextConfigure = None
        self.AsrWordsConfigure = None
        self.CreateTime = None
        self.UpdateTime = None
        self.Type = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("FaceConfigure") is not None:
            self.FaceConfigure = FaceConfigureInfo()
            self.FaceConfigure._deserialize(params.get("FaceConfigure"))
        if params.get("OcrFullTextConfigure") is not None:
            self.OcrFullTextConfigure = OcrFullTextConfigureInfo()
            self.OcrFullTextConfigure._deserialize(params.get("OcrFullTextConfigure"))
        if params.get("OcrWordsConfigure") is not None:
            self.OcrWordsConfigure = OcrWordsConfigureInfo()
            self.OcrWordsConfigure._deserialize(params.get("OcrWordsConfigure"))
        if params.get("AsrFullTextConfigure") is not None:
            self.AsrFullTextConfigure = AsrFullTextConfigureInfo()
            self.AsrFullTextConfigure._deserialize(params.get("AsrFullTextConfigure"))
        if params.get("AsrWordsConfigure") is not None:
            self.AsrWordsConfigure = AsrWordsConfigureInfo()
            self.AsrWordsConfigure._deserialize(params.get("AsrWordsConfigure"))
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdaptiveDynamicStreamingInfoItem(AbstractModel):
    """Adaptive bitrate streaming information

    """

    def __init__(self):
        r"""
        :param Definition: Adaptive bitrate streaming specification.
        :type Definition: int
        :param Package: Container format. Valid values: HLS, MPEG-DASH.
        :type Package: str
        :param Path: Playback address.
        :type Path: str
        :param Storage: Storage location of adaptive bitrate streaming files.
        :type Storage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        """
        self.Definition = None
        self.Package = None
        self.Path = None
        self.Storage = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Package = params.get("Package")
        self.Path = params.get("Path")
        if params.get("Storage") is not None:
            self.Storage = TaskOutputStorage()
            self.Storage._deserialize(params.get("Storage"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdaptiveDynamicStreamingTaskInput(AbstractModel):
    """Input parameter type of adaptive bitrate streaming

    """

    def __init__(self):
        r"""
        :param Definition: Adaptive bitrate streaming template ID.
        :type Definition: int
        :param WatermarkSet: List of up to 10 image or text watermarks.
        :type WatermarkSet: list of WatermarkInput
        :param OutputStorage: Target bucket of an output file after being transcoded to adaptive bitrate streaming. If this parameter is left empty, the `OutputStorage` value of the upper folder will be inherited.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        :param OutputObjectPath: The relative or absolute output path of the manifest file after being transcoded to adaptive bitrate streaming. If this parameter is left empty, a relative path in the following format will be used by default: `{inputName}_adaptiveDynamicStreaming_{definition}.{format}`.
        :type OutputObjectPath: str
        :param SubStreamObjectName: The relative output path of the substream file after being transcoded to adaptive bitrate streaming. If this parameter is left empty, a relative path in the following format will be used by default: `{inputName}_adaptiveDynamicStreaming_{definition}_{subStreamNumber}.{format}`.
        :type SubStreamObjectName: str
        :param SegmentObjectName: The relative output path of the segment file after being transcoded to adaptive bitrate streaming (in HLS format only). If this parameter is left empty, a relative path in the following format will be used by default: `{inputName}_adaptiveDynamicStreaming_{definition}_{subStreamNumber}_{segmentNumber}.{format}`.
        :type SegmentObjectName: str
        """
        self.Definition = None
        self.WatermarkSet = None
        self.OutputStorage = None
        self.OutputObjectPath = None
        self.SubStreamObjectName = None
        self.SegmentObjectName = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        if params.get("WatermarkSet") is not None:
            self.WatermarkSet = []
            for item in params.get("WatermarkSet"):
                obj = WatermarkInput()
                obj._deserialize(item)
                self.WatermarkSet.append(obj)
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.OutputObjectPath = params.get("OutputObjectPath")
        self.SubStreamObjectName = params.get("SubStreamObjectName")
        self.SegmentObjectName = params.get("SegmentObjectName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdaptiveDynamicStreamingTemplate(AbstractModel):
    """Details of an adaptive bitrate streaming template

    """

    def __init__(self):
        r"""
        :param Definition: Unique ID of an adaptive bitrate streaming template.
        :type Definition: int
        :param Type: Template type. Valid values:
<li>Preset: preset template;</li>
<li>Custom: custom template.</li>
        :type Type: str
        :param Name: Name of an adaptive bitrate streaming template.
        :type Name: str
        :param Comment: Description of an adaptive bitrate streaming template.
        :type Comment: str
        :param Format: Adaptive bitrate streaming format. Valid values:
<li>HLS;</li>
<li>MPEG-DASH.</li>
        :type Format: str
        :param StreamInfos: Parameter information of input streams for transcoding to adaptive bitrate streaming. Up to 10 streams can be input.
        :type StreamInfos: list of AdaptiveStreamTemplate
        :param DisableHigherVideoBitrate: Whether to prohibit transcoding from low bitrate to high bitrate. Valid values:
<li>0: no,</li>
<li>1: yes.</li>
        :type DisableHigherVideoBitrate: int
        :param DisableHigherVideoResolution: Whether to prohibit transcoding from low resolution to high resolution. Valid values:
<li>0: no,</li>
<li>1: yes.</li>
        :type DisableHigherVideoResolution: int
        :param CreateTime: Creation time of template in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I).
        :type CreateTime: str
        :param UpdateTime: Last modified time of template in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I).
        :type UpdateTime: str
        """
        self.Definition = None
        self.Type = None
        self.Name = None
        self.Comment = None
        self.Format = None
        self.StreamInfos = None
        self.DisableHigherVideoBitrate = None
        self.DisableHigherVideoResolution = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.Format = params.get("Format")
        if params.get("StreamInfos") is not None:
            self.StreamInfos = []
            for item in params.get("StreamInfos"):
                obj = AdaptiveStreamTemplate()
                obj._deserialize(item)
                self.StreamInfos.append(obj)
        self.DisableHigherVideoBitrate = params.get("DisableHigherVideoBitrate")
        self.DisableHigherVideoResolution = params.get("DisableHigherVideoResolution")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdaptiveStreamTemplate(AbstractModel):
    """Adaptive bitrate streaming parameter template

    """

    def __init__(self):
        r"""
        :param Video: Video parameter information.
        :type Video: :class:`tencentcloud.mps.v20190612.models.VideoTemplateInfo`
        :param Audio: Audio parameter information.
        :type Audio: :class:`tencentcloud.mps.v20190612.models.AudioTemplateInfo`
        :param RemoveAudio: Whether to remove audio stream. Valid values:
<li>0: no,</li>
<li>1: yes.</li>
        :type RemoveAudio: int
        :param RemoveVideo: Whether to remove video stream. Valid values:
<li>0: no,</li>
<li>1: yes.</li>
        :type RemoveVideo: int
        """
        self.Video = None
        self.Audio = None
        self.RemoveAudio = None
        self.RemoveVideo = None


    def _deserialize(self, params):
        if params.get("Video") is not None:
            self.Video = VideoTemplateInfo()
            self.Video._deserialize(params.get("Video"))
        if params.get("Audio") is not None:
            self.Audio = AudioTemplateInfo()
            self.Audio._deserialize(params.get("Audio"))
        self.RemoveAudio = params.get("RemoveAudio")
        self.RemoveVideo = params.get("RemoveVideo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisResult(AbstractModel):
    """Intelligent analysis results

    """

    def __init__(self):
        r"""
        :param Type: Task type. Valid values:
<li>Classification: intelligent categorization</li>
<li>Cover: intelligent cover generating</li>
<li>Tag: intelligent tagging</li>
<li>FrameTag: intelligent frame-specific tagging</li>
<li>Highlight: intelligent highlight generating</li>
        :type Type: str
        :param ClassificationTask: Query result of intelligent categorization task in video content analysis, which is valid if task type is `Classification`.
        :type ClassificationTask: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskClassificationResult`
        :param CoverTask: Query result of intelligent cover generating task in video content analysis, which is valid if task type is `Cover`.
        :type CoverTask: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskCoverResult`
        :param TagTask: Query result of intelligent tagging task in video content analysis, which is valid if task type is `Tag`.
        :type TagTask: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskTagResult`
        :param FrameTagTask: Query result of intelligent frame-specific tagging task in video content analysis, which is valid if task type is `FrameTag`.
        :type FrameTagTask: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskFrameTagResult`
        """
        self.Type = None
        self.ClassificationTask = None
        self.CoverTask = None
        self.TagTask = None
        self.FrameTagTask = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("ClassificationTask") is not None:
            self.ClassificationTask = AiAnalysisTaskClassificationResult()
            self.ClassificationTask._deserialize(params.get("ClassificationTask"))
        if params.get("CoverTask") is not None:
            self.CoverTask = AiAnalysisTaskCoverResult()
            self.CoverTask._deserialize(params.get("CoverTask"))
        if params.get("TagTask") is not None:
            self.TagTask = AiAnalysisTaskTagResult()
            self.TagTask._deserialize(params.get("TagTask"))
        if params.get("FrameTagTask") is not None:
            self.FrameTagTask = AiAnalysisTaskFrameTagResult()
            self.FrameTagTask._deserialize(params.get("FrameTagTask"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisTaskClassificationInput(AbstractModel):
    """Input type of intelligent categorization task

    """

    def __init__(self):
        r"""
        :param Definition: Intelligent video categorization template ID.
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisTaskClassificationOutput(AbstractModel):
    """Result information of intelligent categorization

    """

    def __init__(self):
        r"""
        :param ClassificationSet: List of intelligently generated video categories.
        :type ClassificationSet: list of MediaAiAnalysisClassificationItem
        """
        self.ClassificationSet = None


    def _deserialize(self, params):
        if params.get("ClassificationSet") is not None:
            self.ClassificationSet = []
            for item in params.get("ClassificationSet"):
                obj = MediaAiAnalysisClassificationItem()
                obj._deserialize(item)
                self.ClassificationSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisTaskClassificationResult(AbstractModel):
    """Result type of intelligent categorization task

    """

    def __init__(self):
        r"""
        :param Status: Task status. Valid values: PROCESSING, SUCCESS, FAIL.
        :type Status: str
        :param ErrCodeExt: Error code. An empty string indicates the task is successful; otherwise it is failed. For details about the values, see [Error Code List](https://intl.cloud.tencent.com/document/product/862/50369?from_cn_redirect=1#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81).
        :type ErrCodeExt: str
        :param ErrCode: Error code. 0 indicates the task is successful; otherwise it is failed. This parameter is no longer recommended. Consider using the new error code parameter ErrCodeExt.
        :type ErrCode: int
        :param Message: Error message.
        :type Message: str
        :param Input: Input of intelligent categorization task.
        :type Input: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskClassificationInput`
        :param Output: Output of intelligent categorization task.
        :type Output: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskClassificationOutput`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiAnalysisTaskClassificationInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiAnalysisTaskClassificationOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisTaskCoverInput(AbstractModel):
    """Input type of intelligent categorization task

    """

    def __init__(self):
        r"""
        :param Definition: Intelligent video cover generating template ID.
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisTaskCoverOutput(AbstractModel):
    """Result information of intelligent cover generating

    """

    def __init__(self):
        r"""
        :param CoverSet: List of intelligently generated covers.
        :type CoverSet: list of MediaAiAnalysisCoverItem
        :param OutputStorage: Storage location of intelligently generated cover.
        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        """
        self.CoverSet = None
        self.OutputStorage = None


    def _deserialize(self, params):
        if params.get("CoverSet") is not None:
            self.CoverSet = []
            for item in params.get("CoverSet"):
                obj = MediaAiAnalysisCoverItem()
                obj._deserialize(item)
                self.CoverSet.append(obj)
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisTaskCoverResult(AbstractModel):
    """Result type of intelligent cover generating task

    """

    def __init__(self):
        r"""
        :param Status: Task status. Valid values: PROCESSING, SUCCESS, FAIL.
        :type Status: str
        :param ErrCodeExt: Error code. An empty string indicates the task is successful; otherwise it is failed. For details about the values, see [Error Code List](https://intl.cloud.tencent.com/document/product/862/50369?from_cn_redirect=1#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81).
        :type ErrCodeExt: str
        :param ErrCode: Error code. 0 indicates the task is successful; otherwise it is failed. This parameter is no longer recommended. Consider using the new error code parameter ErrCodeExt.
        :type ErrCode: int
        :param Message: Error message.
        :type Message: str
        :param Input: Input of intelligent cover generating task.
        :type Input: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskCoverInput`
        :param Output: Output of intelligent cover generating task.
        :type Output: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskCoverOutput`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiAnalysisTaskCoverInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiAnalysisTaskCoverOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisTaskFrameTagInput(AbstractModel):
    """Input type of intelligent frame-specific tagging task

    """

    def __init__(self):
        r"""
        :param Definition: Intelligent frame-specific video tagging template ID.
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisTaskFrameTagOutput(AbstractModel):
    """Result information of intelligent frame-specific tagging

    """

    def __init__(self):
        r"""
        :param SegmentSet: List of frame-specific video tags.
        :type SegmentSet: list of MediaAiAnalysisFrameTagSegmentItem
        """
        self.SegmentSet = None


    def _deserialize(self, params):
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaAiAnalysisFrameTagSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisTaskFrameTagResult(AbstractModel):
    """Result type of intelligent frame-specific tagging

    """

    def __init__(self):
        r"""
        :param Status: Task status. Valid values: PROCESSING, SUCCESS, FAIL.
        :type Status: str
        :param ErrCodeExt: Error code. An empty string indicates the task is successful; otherwise it is failed. For details about the values, see [Error Code List](https://intl.cloud.tencent.com/document/product/862/50369?from_cn_redirect=1#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81).
        :type ErrCodeExt: str
        :param ErrCode: Error code. 0 indicates the task is successful; otherwise it is failed. This parameter is no longer recommended. Consider using the new error code parameter ErrCodeExt.
        :type ErrCode: int
        :param Message: Error message.
        :type Message: str
        :param Input: Input of intelligent frame-specific tagging task.
        :type Input: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskFrameTagInput`
        :param Output: Output of intelligent frame-specific tagging task.
        :type Output: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskFrameTagOutput`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiAnalysisTaskFrameTagInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiAnalysisTaskFrameTagOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisTaskInput(AbstractModel):
    """AI video intelligent analysis input parameter types

    """

    def __init__(self):
        r"""
        :param Definition: Video content analysis template ID.
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisTaskTagInput(AbstractModel):
    """Input type of intelligent tagging task

    """

    def __init__(self):
        r"""
        :param Definition: Intelligent video tagging template ID.
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisTaskTagOutput(AbstractModel):
    """Result information of intelligent tagging

    """

    def __init__(self):
        r"""
        :param TagSet: List of intelligently generated video tags.
        :type TagSet: list of MediaAiAnalysisTagItem
        """
        self.TagSet = None


    def _deserialize(self, params):
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = MediaAiAnalysisTagItem()
                obj._deserialize(item)
                self.TagSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisTaskTagResult(AbstractModel):
    """Result type of intelligent tagging task

    """

    def __init__(self):
        r"""
        :param Status: Task status. Valid values: PROCESSING, SUCCESS, FAIL.
        :type Status: str
        :param ErrCodeExt: Error code. An empty string indicates the task is successful; otherwise it is failed. For details about the values, see [Error Code List](https://intl.cloud.tencent.com/document/product/862/50369?from_cn_redirect=1#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81).
        :type ErrCodeExt: str
        :param ErrCode: Error code. 0 indicates the task is successful; otherwise it is failed. This parameter is no longer recommended. Consider using the new error code parameter ErrCodeExt.
        :type ErrCode: int
        :param Message: Error message.
        :type Message: str
        :param Input: Input of intelligent tagging task.
        :type Input: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskTagInput`
        :param Output: Output of intelligent tagging task.
        :type Output: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskTagOutput`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiAnalysisTaskTagInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiAnalysisTaskTagOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiContentReviewResult(AbstractModel):
    """Content audit result

    """

    def __init__(self):
        r"""
        :param Type: Task type. Valid values:
<li>Porn (in images)</li>
<li>Terrorism (in images)</li>
<li>Political (in images)</li>
<li>Porn.Asr</li>
<li>Porn.Ocr</li>
<li>Political.Asr</li>
<li>Political.Ocr</li>
<li>Terrorism.Ocr</li>
<li>Prohibited.Asr</li>
<li>Prohibited.Ocr</li>
        :type Type: str
        :param SampleRate: Sample rate, which indicates the number of video frames captured per second for audit
        :type SampleRate: float
        :param Duration: Audited video duration in seconds.
        :type Duration: float
        :param PornTask: Query result of an intelligent porn information detection in image task in video content audit, which is valid when task type is `Porn`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PornTask: :class:`tencentcloud.mps.v20190612.models.AiReviewTaskPornResult`
        :param TerrorismTask: The result of detecting terrorism content in images, which is valid when the task type is `Terrorism`.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type TerrorismTask: :class:`tencentcloud.mps.v20190612.models.AiReviewTaskTerrorismResult`
        :param PoliticalTask: The result of detecting politically sensitive information in images, which is valid when the task type is `Political`.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type PoliticalTask: :class:`tencentcloud.mps.v20190612.models.AiReviewTaskPoliticalResult`
        :param PornAsrTask: Query result of an ASR-based porn information detection in text task in video content audit, which is valid when task type is `Porn.Asr`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PornAsrTask: :class:`tencentcloud.mps.v20190612.models.AiReviewTaskPornAsrResult`
        :param PornOcrTask: Query result of an OCR-based porn information detection in text task in video content audit, which is valid when task type is `Porn.Ocr`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PornOcrTask: :class:`tencentcloud.mps.v20190612.models.AiReviewTaskPornOcrResult`
        :param PoliticalAsrTask: The result of detecting politically sensitive information based on ASR, which is valid when the task type is `Political.Asr`.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type PoliticalAsrTask: :class:`tencentcloud.mps.v20190612.models.AiReviewTaskPoliticalAsrResult`
        :param PoliticalOcrTask: The result of detecting politically sensitive information based on OCR, which is valid when the task type is `Political.Ocr`.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type PoliticalOcrTask: :class:`tencentcloud.mps.v20190612.models.AiReviewTaskPoliticalOcrResult`
        :param TerrorismOcrTask: The result of detecting terrorism content based on OCR, which is valid when task type is `Terrorism.Ocr`.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type TerrorismOcrTask: :class:`tencentcloud.mps.v20190612.models.AiReviewTaskTerrorismOcrResult`
        :param ProhibitedAsrTask: Query result of ASR-based prohibited information detection in speech task in video content audit, which is valid if task type is `Prohibited.Asr`.
        :type ProhibitedAsrTask: :class:`tencentcloud.mps.v20190612.models.AiReviewTaskProhibitedAsrResult`
        :param ProhibitedOcrTask: Query result of OCR-based prohibited information detection in text task in video content audit, which is valid if task type is `Prohibited.Ocr`.
        :type ProhibitedOcrTask: :class:`tencentcloud.mps.v20190612.models.AiReviewTaskProhibitedOcrResult`
        """
        self.Type = None
        self.SampleRate = None
        self.Duration = None
        self.PornTask = None
        self.TerrorismTask = None
        self.PoliticalTask = None
        self.PornAsrTask = None
        self.PornOcrTask = None
        self.PoliticalAsrTask = None
        self.PoliticalOcrTask = None
        self.TerrorismOcrTask = None
        self.ProhibitedAsrTask = None
        self.ProhibitedOcrTask = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.SampleRate = params.get("SampleRate")
        self.Duration = params.get("Duration")
        if params.get("PornTask") is not None:
            self.PornTask = AiReviewTaskPornResult()
            self.PornTask._deserialize(params.get("PornTask"))
        if params.get("TerrorismTask") is not None:
            self.TerrorismTask = AiReviewTaskTerrorismResult()
            self.TerrorismTask._deserialize(params.get("TerrorismTask"))
        if params.get("PoliticalTask") is not None:
            self.PoliticalTask = AiReviewTaskPoliticalResult()
            self.PoliticalTask._deserialize(params.get("PoliticalTask"))
        if params.get("PornAsrTask") is not None:
            self.PornAsrTask = AiReviewTaskPornAsrResult()
            self.PornAsrTask._deserialize(params.get("PornAsrTask"))
        if params.get("PornOcrTask") is not None:
            self.PornOcrTask = AiReviewTaskPornOcrResult()
            self.PornOcrTask._deserialize(params.get("PornOcrTask"))
        if params.get("PoliticalAsrTask") is not None:
            self.PoliticalAsrTask = AiReviewTaskPoliticalAsrResult()
            self.PoliticalAsrTask._deserialize(params.get("PoliticalAsrTask"))
        if params.get("PoliticalOcrTask") is not None:
            self.PoliticalOcrTask = AiReviewTaskPoliticalOcrResult()
            self.PoliticalOcrTask._deserialize(params.get("PoliticalOcrTask"))
        if params.get("TerrorismOcrTask") is not None:
            self.TerrorismOcrTask = AiReviewTaskTerrorismOcrResult()
            self.TerrorismOcrTask._deserialize(params.get("TerrorismOcrTask"))
        if params.get("ProhibitedAsrTask") is not None:
            self.ProhibitedAsrTask = AiReviewTaskProhibitedAsrResult()
            self.ProhibitedAsrTask._deserialize(params.get("ProhibitedAsrTask"))
        if params.get("ProhibitedOcrTask") is not None:
            self.ProhibitedOcrTask = AiReviewTaskProhibitedOcrResult()
            self.ProhibitedOcrTask._deserialize(params.get("ProhibitedOcrTask"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiContentReviewTaskInput(AbstractModel):
    """Task type of intelligent content audit

    """

    def __init__(self):
        r"""
        :param Definition: Video content audit template ID.
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionResult(AbstractModel):
    """Intelligent recognition result.

    """

    def __init__(self):
        r"""
        :param Type: Task type. Valid values:
<li>FaceRecognition: Face recognition,</li>
<li>AsrWordsRecognition: Speech keyword recognition,</li>
<li>OcrWordsRecognition: Text keyword recognition,</li>
<li>AsrFullTextRecognition: Full speech recognition,</li>
<li>OcrFullTextRecognition: Full text recognition,</li>
<li>HeadTailRecognition: Video opening and ending credits recognition,</li>
<li>ObjectRecognition: Object recognition.</li>
        :type Type: str
        :param FaceTask: Face recognition result, which is valid when `Type` is 
 `FaceRecognition`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type FaceTask: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskFaceResult`
        :param AsrWordsTask: Speech keyword recognition result, which is valid when `Type` is
 `AsrWordsRecognition`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AsrWordsTask: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskAsrWordsResult`
        :param AsrFullTextTask: Full speech recognition result, which is valid when `Type` is
 `AsrFullTextRecognition`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AsrFullTextTask: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskAsrFullTextResult`
        :param OcrWordsTask: Text keyword recognition result, which is valid when `Type` is
 `OcrWordsRecognition`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type OcrWordsTask: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskOcrWordsResult`
        :param OcrFullTextTask: Full text recognition result, which is valid when `Type` is
 `OcrFullTextRecognition`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type OcrFullTextTask: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskOcrFullTextResult`
        """
        self.Type = None
        self.FaceTask = None
        self.AsrWordsTask = None
        self.AsrFullTextTask = None
        self.OcrWordsTask = None
        self.OcrFullTextTask = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("FaceTask") is not None:
            self.FaceTask = AiRecognitionTaskFaceResult()
            self.FaceTask._deserialize(params.get("FaceTask"))
        if params.get("AsrWordsTask") is not None:
            self.AsrWordsTask = AiRecognitionTaskAsrWordsResult()
            self.AsrWordsTask._deserialize(params.get("AsrWordsTask"))
        if params.get("AsrFullTextTask") is not None:
            self.AsrFullTextTask = AiRecognitionTaskAsrFullTextResult()
            self.AsrFullTextTask._deserialize(params.get("AsrFullTextTask"))
        if params.get("OcrWordsTask") is not None:
            self.OcrWordsTask = AiRecognitionTaskOcrWordsResult()
            self.OcrWordsTask._deserialize(params.get("OcrWordsTask"))
        if params.get("OcrFullTextTask") is not None:
            self.OcrFullTextTask = AiRecognitionTaskOcrFullTextResult()
            self.OcrFullTextTask._deserialize(params.get("OcrFullTextTask"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskAsrFullTextResult(AbstractModel):
    """Full speech recognition result.

    """

    def __init__(self):
        r"""
        :param Status: Task status. Valid values: PROCESSING, SUCCESS, FAIL.
        :type Status: str
        :param ErrCodeExt: Error code. An empty string indicates the task is successful; otherwise it is failed. For details about the values, see [Error Code List](https://intl.cloud.tencent.com/document/product/862/50369?from_cn_redirect=1#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81).
        :type ErrCodeExt: str
        :param ErrCode: Error code. 0 indicates the task is successful; otherwise it is failed. This parameter is no longer recommended. Consider using the new error code parameter ErrCodeExt.
        :type ErrCode: int
        :param Message: Error message.
        :type Message: str
        :param Input: Input information of a full speech recognition task.
        :type Input: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskAsrFullTextResultInput`
        :param Output: Output information of a full speech recognition task.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Output: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskAsrFullTextResultOutput`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiRecognitionTaskAsrFullTextResultInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiRecognitionTaskAsrFullTextResultOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskAsrFullTextResultInput(AbstractModel):
    """Input for full speech recognition.

    """

    def __init__(self):
        r"""
        :param Definition: Full speech recognition template ID.
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskAsrFullTextResultOutput(AbstractModel):
    """Full speech recognition result.

    """

    def __init__(self):
        r"""
        :param SegmentSet: List of full speech recognition segments.
        :type SegmentSet: list of AiRecognitionTaskAsrFullTextSegmentItem
        :param SubtitlePath: Subtitles file address.
        :type SubtitlePath: str
        :param OutputStorage: Subtitles file storage location.
        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        """
        self.SegmentSet = None
        self.SubtitlePath = None
        self.OutputStorage = None


    def _deserialize(self, params):
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = AiRecognitionTaskAsrFullTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        self.SubtitlePath = params.get("SubtitlePath")
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskAsrFullTextSegmentItem(AbstractModel):
    """Full speech recognition segment.

    """

    def __init__(self):
        r"""
        :param Confidence: Confidence of a recognition segment. Value range: 0-100.
        :type Confidence: float
        :param StartTimeOffset: Start time offset of a recognition segment in seconds.
        :type StartTimeOffset: float
        :param EndTimeOffset: End time offset of a recognition segment in seconds.
        :type EndTimeOffset: float
        :param Text: Recognized text.
        :type Text: str
        """
        self.Confidence = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.Text = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskAsrWordsResult(AbstractModel):
    """Speech keyword recognition result.

    """

    def __init__(self):
        r"""
        :param Status: Task status. Valid values: PROCESSING, SUCCESS, FAIL.
        :type Status: str
        :param ErrCodeExt: Error code. An empty string indicates the task is successful; otherwise it is failed. For details about the values, see [Error Code List](https://intl.cloud.tencent.com/document/product/862/50369?from_cn_redirect=1#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81).
        :type ErrCodeExt: str
        :param ErrCode: Error code. 0 indicates the task is successful; otherwise it is failed. This parameter is no longer recommended. Consider using the new error code parameter ErrCodeExt.
        :type ErrCode: int
        :param Message: Error message.
        :type Message: str
        :param Input: Input information of a speech keyword recognition task.
        :type Input: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskAsrWordsResultInput`
        :param Output: Output information of a speech keyword recognition task.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Output: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskAsrWordsResultOutput`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiRecognitionTaskAsrWordsResultInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiRecognitionTaskAsrWordsResultOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskAsrWordsResultInput(AbstractModel):
    """Input for speech keyword recognition.

    """

    def __init__(self):
        r"""
        :param Definition: Speech keyword recognition template ID.
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskAsrWordsResultItem(AbstractModel):
    """Speech keyword recognition result.

    """

    def __init__(self):
        r"""
        :param Word: Speech keyword.
        :type Word: str
        :param SegmentSet: List of time segments that contain the speech keyword.
        :type SegmentSet: list of AiRecognitionTaskAsrWordsSegmentItem
        """
        self.Word = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Word = params.get("Word")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = AiRecognitionTaskAsrWordsSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskAsrWordsResultOutput(AbstractModel):
    """Output of speech keyword recognition.

    """

    def __init__(self):
        r"""
        :param ResultSet: Speech keyword recognition result set.
        :type ResultSet: list of AiRecognitionTaskAsrWordsResultItem
        """
        self.ResultSet = None


    def _deserialize(self, params):
        if params.get("ResultSet") is not None:
            self.ResultSet = []
            for item in params.get("ResultSet"):
                obj = AiRecognitionTaskAsrWordsResultItem()
                obj._deserialize(item)
                self.ResultSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskAsrWordsSegmentItem(AbstractModel):
    """Speech recognition segment.

    """

    def __init__(self):
        r"""
        :param StartTimeOffset: Start time offset of a recognition segment in seconds.
        :type StartTimeOffset: float
        :param EndTimeOffset: End time offset of a recognition segment in seconds.
        :type EndTimeOffset: float
        :param Confidence: Confidence of a recognition segment. Value range: 0-100.
        :type Confidence: float
        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.Confidence = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.Confidence = params.get("Confidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskFaceResult(AbstractModel):
    """Face recognition result.

    """

    def __init__(self):
        r"""
        :param Status: Task status. Valid values: PROCESSING, SUCCESS, FAIL.
        :type Status: str
        :param ErrCodeExt: Error code. An empty string indicates the task is successful; otherwise it is failed. For details about the values, see [Error Code List](https://intl.cloud.tencent.com/document/product/862/50369?from_cn_redirect=1#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81).
        :type ErrCodeExt: str
        :param ErrCode: Error code. 0 indicates the task is successful; otherwise it is failed. This parameter is no longer recommended. Consider using the new error code parameter ErrCodeExt.
        :type ErrCode: int
        :param Message: Error message.
        :type Message: str
        :param Input: Input information of a face recognition task.
        :type Input: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskFaceResultInput`
        :param Output: Output information of a face recognition task.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Output: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskFaceResultOutput`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiRecognitionTaskFaceResultInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiRecognitionTaskFaceResultOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskFaceResultInput(AbstractModel):
    """Face recognition input.

    """

    def __init__(self):
        r"""
        :param Definition: Face recognition template ID.
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskFaceResultItem(AbstractModel):
    """Face recognition result

    """

    def __init__(self):
        r"""
        :param Id: Unique ID of a figure.
        :type Id: str
        :param Type: Figure library type, indicating to which figure library the recognized figure belongs:
<li>Default: Default figure library;</li>
<li>UserDefine: Custom figure library.</li>
        :type Type: str
        :param Name: Name of a figure.
        :type Name: str
        :param SegmentSet: Result set of segments that contain a figure.
        :type SegmentSet: list of AiRecognitionTaskFaceSegmentItem
        """
        self.Id = None
        self.Type = None
        self.Name = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = AiRecognitionTaskFaceSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskFaceResultOutput(AbstractModel):
    """Output of intelligent face recognition.

    """

    def __init__(self):
        r"""
        :param ResultSet: Intelligent face recognition result set.
        :type ResultSet: list of AiRecognitionTaskFaceResultItem
        """
        self.ResultSet = None


    def _deserialize(self, params):
        if params.get("ResultSet") is not None:
            self.ResultSet = []
            for item in params.get("ResultSet"):
                obj = AiRecognitionTaskFaceResultItem()
                obj._deserialize(item)
                self.ResultSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskFaceSegmentItem(AbstractModel):
    """Face recognition result segment

    """

    def __init__(self):
        r"""
        :param StartTimeOffset: Start time offset of a recognition segment in seconds.
        :type StartTimeOffset: float
        :param EndTimeOffset: End time offset of a recognition segment in seconds.
        :type EndTimeOffset: float
        :param Confidence: Confidence of a recognition segment. Value range: 0-100.
        :type Confidence: float
        :param AreaCoordSet: Zone coordinates of a recognition result. The array contains four elements: [x1,y1,x2,y2], i.e., the horizontal and vertical coordinates of the top-left and bottom-right corners.
        :type AreaCoordSet: list of int
        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.Confidence = None
        self.AreaCoordSet = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.Confidence = params.get("Confidence")
        self.AreaCoordSet = params.get("AreaCoordSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskInput(AbstractModel):
    """Input parameter type of video content recognition

    """

    def __init__(self):
        r"""
        :param Definition: Intelligent video recognition template ID.
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskOcrFullTextResult(AbstractModel):
    """Full text recognition result.

    """

    def __init__(self):
        r"""
        :param Status: Task status. Valid values: PROCESSING, SUCCESS, FAIL.
        :type Status: str
        :param ErrCodeExt: Error code. An empty string indicates the task is successful; otherwise it is failed. For details about the values, see [Error Code List](https://intl.cloud.tencent.com/document/product/862/50369?from_cn_redirect=1#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81).
        :type ErrCodeExt: str
        :param ErrCode: Error code. 0 indicates the task is successful; otherwise it is failed. This parameter is no longer recommended. Consider using the new error code parameter ErrCodeExt.
        :type ErrCode: int
        :param Message: Error message.
        :type Message: str
        :param Input: Input information of a full text recognition task.
        :type Input: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskOcrFullTextResultInput`
        :param Output: Output information of a full text recognition task.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Output: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskOcrFullTextResultOutput`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiRecognitionTaskOcrFullTextResultInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiRecognitionTaskOcrFullTextResultOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskOcrFullTextResultInput(AbstractModel):
    """Input for full text recognition.

    """

    def __init__(self):
        r"""
        :param Definition: Full text recognition template ID.
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskOcrFullTextResultOutput(AbstractModel):
    """Output of full text recognition.

    """

    def __init__(self):
        r"""
        :param SegmentSet: Full text recognition result set.
        :type SegmentSet: list of AiRecognitionTaskOcrFullTextSegmentItem
        """
        self.SegmentSet = None


    def _deserialize(self, params):
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = AiRecognitionTaskOcrFullTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskOcrFullTextSegmentItem(AbstractModel):
    """Full text recognition segment.

    """

    def __init__(self):
        r"""
        :param StartTimeOffset: Start time offset of a recognition segment in seconds.
        :type StartTimeOffset: float
        :param EndTimeOffset: End time offset of a recognition segment in seconds.
        :type EndTimeOffset: float
        :param TextSet: Recognition segment result set.
        :type TextSet: list of AiRecognitionTaskOcrFullTextSegmentTextItem
        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.TextSet = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        if params.get("TextSet") is not None:
            self.TextSet = []
            for item in params.get("TextSet"):
                obj = AiRecognitionTaskOcrFullTextSegmentTextItem()
                obj._deserialize(item)
                self.TextSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskOcrFullTextSegmentTextItem(AbstractModel):
    """Full text recognition segment.

    """

    def __init__(self):
        r"""
        :param Confidence: Confidence of a recognition segment. Value range: 0-100.
        :type Confidence: float
        :param AreaCoordSet: Zone coordinates of a recognition result. The array contains four elements: [x1,y1,x2,y2], i.e., the horizontal and vertical coordinates of the top-left and bottom-right corners.
        :type AreaCoordSet: list of int
        :param Text: Recognized text.
        :type Text: str
        """
        self.Confidence = None
        self.AreaCoordSet = None
        self.Text = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.AreaCoordSet = params.get("AreaCoordSet")
        self.Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskOcrWordsResult(AbstractModel):
    """Text keyword recognition result.

    """

    def __init__(self):
        r"""
        :param Status: Task status. Valid values: PROCESSING, SUCCESS, FAIL.
        :type Status: str
        :param ErrCodeExt: Error code. An empty string indicates the task is successful; otherwise it is failed. For details about the values, see [Error Code List](https://intl.cloud.tencent.com/document/product/862/50369?from_cn_redirect=1#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81).
        :type ErrCodeExt: str
        :param ErrCode: Error code. 0 indicates the task is successful; otherwise it is failed. This parameter is no longer recommended. Consider using the new error code parameter ErrCodeExt.
        :type ErrCode: int
        :param Message: Error message.
        :type Message: str
        :param Input: Input information of a text keyword recognition task.
        :type Input: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskOcrWordsResultInput`
        :param Output: Output information of a text keyword recognition task.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Output: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskOcrWordsResultOutput`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiRecognitionTaskOcrWordsResultInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiRecognitionTaskOcrWordsResultOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskOcrWordsResultInput(AbstractModel):
    """Input for text keyword recognition.

    """

    def __init__(self):
        r"""
        :param Definition: Text keyword recognition template ID.
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskOcrWordsResultItem(AbstractModel):
    """Text keyword recognition result.

    """

    def __init__(self):
        r"""
        :param Word: Text keyword.
        :type Word: str
        :param SegmentSet: List of segments that contain a text keyword.
        :type SegmentSet: list of AiRecognitionTaskOcrWordsSegmentItem
        """
        self.Word = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Word = params.get("Word")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = AiRecognitionTaskOcrWordsSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskOcrWordsResultOutput(AbstractModel):
    """Output of text keyword recognition.

    """

    def __init__(self):
        r"""
        :param ResultSet: Text keyword recognition result set.
        :type ResultSet: list of AiRecognitionTaskOcrWordsResultItem
        """
        self.ResultSet = None


    def _deserialize(self, params):
        if params.get("ResultSet") is not None:
            self.ResultSet = []
            for item in params.get("ResultSet"):
                obj = AiRecognitionTaskOcrWordsResultItem()
                obj._deserialize(item)
                self.ResultSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskOcrWordsSegmentItem(AbstractModel):
    """Text recognition segment.

    """

    def __init__(self):
        r"""
        :param StartTimeOffset: Start time offset of a recognition segment in seconds.
        :type StartTimeOffset: float
        :param EndTimeOffset: End time offset of a recognition segment in seconds.
        :type EndTimeOffset: float
        :param Confidence: Confidence of a recognition segment. Value range: 0-100.
        :type Confidence: float
        :param AreaCoordSet: Zone coordinates of a recognition result. The array contains four elements: [x1,y1,x2,y2], i.e., the horizontal and vertical coordinates of the top-left and bottom-right corners.
        :type AreaCoordSet: list of int
        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.Confidence = None
        self.AreaCoordSet = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.Confidence = params.get("Confidence")
        self.AreaCoordSet = params.get("AreaCoordSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewPoliticalAsrTaskInput(AbstractModel):
    """The input parameters for ASR-based detection of politically sensitive information.

    """

    def __init__(self):
        r"""
        :param Definition: The template ID.
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewPoliticalAsrTaskOutput(AbstractModel):
    """The information about the sensitive content detected based on ASR.

    """

    def __init__(self):
        r"""
        :param Confidence: The confidence score for the ASR-based detection of sensitive information. Value range: 0-100.
        :type Confidence: float
        :param Suggestion: The suggestion for handling the sensitive information detected based on ASR. Valid values:
<li>pass</li>
<li>review</li>
<li>block</li>
        :type Suggestion: str
        :param SegmentSet: The video segments that contain sensitive information detected based on ASR.
        :type SegmentSet: list of MediaContentReviewAsrTextSegmentItem
        """
        self.Confidence = None
        self.Suggestion = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaContentReviewAsrTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewPoliticalOcrTaskInput(AbstractModel):
    """The input parameters for OCR-based detection of politically sensitive information.

    """

    def __init__(self):
        r"""
        :param Definition: The template ID.
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewPoliticalOcrTaskOutput(AbstractModel):
    """The information about the sensitive content detected based on OCR.

    """

    def __init__(self):
        r"""
        :param Confidence: The confidence score for the OCR-based detection of sensitive information. Value range: 0-100.
        :type Confidence: float
        :param Suggestion: The suggestion for handling the sensitive information detected based on OCR. Valid values:
<li>pass</li>
<li>review</li>
<li>block</li>
        :type Suggestion: str
        :param SegmentSet: The video segments that contain sensitive information detected based on OCR.
        :type SegmentSet: list of MediaContentReviewOcrTextSegmentItem
        """
        self.Confidence = None
        self.Suggestion = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaContentReviewOcrTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewPoliticalTaskInput(AbstractModel):
    """The input parameters for the detection of politically sensitive information.

    """

    def __init__(self):
        r"""
        :param Definition: The template ID.
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewPoliticalTaskOutput(AbstractModel):
    """The sensitive information detected.

    """

    def __init__(self):
        r"""
        :param Confidence: The confidence score for the detection of sensitive information. Value range: 0-100.
        :type Confidence: float
        :param Suggestion: The suggestion for handling the sensitive information detected. Valid values:
<li>pass</li>
<li>review</li>
<li>block</li>
        :type Suggestion: str
        :param Label: The labels for the detected sensitive content. The relationship between the values of this parameter and those of the `LabelSet` parameter in [PoliticalImgReviewTemplateInfo](https://intl.cloud.tencent.com/document/api/862/37615?from_cn_redirect=1#AiReviewPoliticalTaskOutput) is as follows:
violation_photo:
<li>violation_photo (banned icons)</li>
Other values (politician/entertainment/sport/entrepreneur/scholar/celebrity/military):
<li>politician</li>
        :type Label: str
        :param SegmentSet: The video segments that contain sensitive information.
        :type SegmentSet: list of MediaContentReviewPoliticalSegmentItem
        """
        self.Confidence = None
        self.Suggestion = None
        self.Label = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.Label = params.get("Label")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaContentReviewPoliticalSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewPornAsrTaskInput(AbstractModel):
    """Input parameter type of an ASR-based porn information detection in text task during content audit

    """

    def __init__(self):
        r"""
        :param Definition: ID of a porn information detection template.
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewPornAsrTaskOutput(AbstractModel):
    """ASR-detected porn information in text

    """

    def __init__(self):
        r"""
        :param Confidence: Score of the ASR-detected porn information in text from 0 to 100.
        :type Confidence: float
        :param Suggestion: Suggestion for the ASR-detected porn information in text. Valid values:
<li>pass.</li>
<li>review.</li>
<li>block.</li>
        :type Suggestion: str
        :param SegmentSet: List of video segments that contain the ASR-detected porn information in text.
        :type SegmentSet: list of MediaContentReviewAsrTextSegmentItem
        """
        self.Confidence = None
        self.Suggestion = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaContentReviewAsrTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewPornOcrTaskInput(AbstractModel):
    """Input parameter type of an OCR-based porn information detection in text task during content audit

    """

    def __init__(self):
        r"""
        :param Definition: ID of a porn information detection template.
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewPornOcrTaskOutput(AbstractModel):
    """OCR-detected porn information in text

    """

    def __init__(self):
        r"""
        :param Confidence: Score of the OCR-detected porn information in text from 0 to 100.
        :type Confidence: float
        :param Suggestion: Suggestion for the OCR-detected porn information in text. Valid values:
<li>pass.</li>
<li>review.</li>
<li>block.</li>
        :type Suggestion: str
        :param SegmentSet: List of video segments that contain the OCR-detected porn information in text.
        :type SegmentSet: list of MediaContentReviewOcrTextSegmentItem
        """
        self.Confidence = None
        self.Suggestion = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaContentReviewOcrTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewPornTaskInput(AbstractModel):
    """Input parameter type of a porn information detection task during content audit

    """

    def __init__(self):
        r"""
        :param Definition: ID of a porn information detection template.
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewPornTaskOutput(AbstractModel):
    """Porn information detection result

    """

    def __init__(self):
        r"""
        :param Confidence: Score of the detected porn information in video from 0 to 100.
        :type Confidence: float
        :param Suggestion: Suggestion for the detected porn information. Valid values:
<li>pass.</li>
<li>review.</li>
<li>block.</li>
        :type Suggestion: str
        :param Label: Tag of the detected porn information in video. Valid values:
<li>porn: Porn.</li>
<li>sexy: Sexiness.</li>
<li>vulgar: Vulgarity.</li>
<li>intimacy: Intimacy.</li>
        :type Label: str
        :param SegmentSet: List of video segments that contain the detected porn information.
        :type SegmentSet: list of MediaContentReviewSegmentItem
        """
        self.Confidence = None
        self.Suggestion = None
        self.Label = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.Label = params.get("Label")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaContentReviewSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewProhibitedAsrTaskInput(AbstractModel):
    """Input parameter type of ASR-based prohibited information detection in speech task in content audit

    """

    def __init__(self):
        r"""
        :param Definition: Prohibited information detection template ID.
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewProhibitedAsrTaskOutput(AbstractModel):
    """ASR-detected prohibited information in speech

    """

    def __init__(self):
        r"""
        :param Confidence: Score of ASR-detected prohibited information in speech between 0 and 100.
        :type Confidence: float
        :param Suggestion: Suggestion for ASR-detected prohibited information in speech. Valid values:
<li>pass.</li>
<li>review.</li>
<li>block.</li>
        :type Suggestion: str
        :param SegmentSet: List of video segments that contain the ASR-detected prohibited information in speech.
        :type SegmentSet: list of MediaContentReviewAsrTextSegmentItem
        """
        self.Confidence = None
        self.Suggestion = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaContentReviewAsrTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewProhibitedOcrTaskInput(AbstractModel):
    """Input parameter type of OCR-based prohibited information detection in text task in content audit

    """

    def __init__(self):
        r"""
        :param Definition: Prohibited information detection template ID.
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewProhibitedOcrTaskOutput(AbstractModel):
    """OCR-detected prohibited information in text

    """

    def __init__(self):
        r"""
        :param Confidence: Score of OCR-detected prohibited information in text between 0 and 100.
        :type Confidence: float
        :param Suggestion: Suggestion for OCR-detected prohibited information in text. Valid values:
<li>pass.</li>
<li>review.</li>
<li>block.</li>
        :type Suggestion: str
        :param SegmentSet: List of video segments that contain the OCR-detected prohibited information in text.
        :type SegmentSet: list of MediaContentReviewOcrTextSegmentItem
        """
        self.Confidence = None
        self.Suggestion = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaContentReviewOcrTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewTaskPoliticalAsrResult(AbstractModel):
    """The result of ASR-based detection of politically sensitive information.

    """

    def __init__(self):
        r"""
        :param Status: Task status. Valid values: PROCESSING, SUCCESS, FAIL.
        :type Status: str
        :param ErrCodeExt: Error code. An empty string indicates the task is successful; otherwise it is failed. For details about the values, see the list of [Error Codes](https://intl.cloud.tencent.com/document/product/862/50369?from_cn_redirect=1#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81).
        :type ErrCodeExt: str
        :param ErrCode: Error code. 0 indicates the task is successful; otherwise it is failed. This parameter is no longer recommended. Consider using the new error code parameter ErrCodeExt.
        :type ErrCode: int
        :param Message: Error message.
        :type Message: str
        :param Input: The input parameter for ASR-based detection of politically sensitive information.
        :type Input: :class:`tencentcloud.mps.v20190612.models.AiReviewPoliticalAsrTaskInput`
        :param Output: The output of ASR-based detection of politically sensitive information.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Output: :class:`tencentcloud.mps.v20190612.models.AiReviewPoliticalAsrTaskOutput`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewPoliticalAsrTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewPoliticalAsrTaskOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewTaskPoliticalOcrResult(AbstractModel):
    """The result of OCR-based detection of politically sensitive information.

    """

    def __init__(self):
        r"""
        :param Status: Task status. Valid values: PROCESSING, SUCCESS, FAIL.
        :type Status: str
        :param ErrCodeExt: Error code. An empty string indicates the task is successful; otherwise it is failed. For details about the values, see [Error Code List](https://intl.cloud.tencent.com/document/product/862/50369?from_cn_redirect=1#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81).
        :type ErrCodeExt: str
        :param ErrCode: Error code. 0 indicates the task is successful; otherwise it is failed. This parameter is no longer recommended. Consider using the new error code parameter ErrCodeExt.
        :type ErrCode: int
        :param Message: Error message.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Message: str
        :param Input: The input parameter for OCR-based detection of politically sensitive information.
        :type Input: :class:`tencentcloud.mps.v20190612.models.AiReviewPoliticalOcrTaskInput`
        :param Output: The output of OCR-based detection of politically sensitive information.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Output: :class:`tencentcloud.mps.v20190612.models.AiReviewPoliticalOcrTaskOutput`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewPoliticalOcrTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewPoliticalOcrTaskOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewTaskPoliticalResult(AbstractModel):
    """The result of sensitive information detection.

    """

    def __init__(self):
        r"""
        :param Status: Task status. Valid values: PROCESSING, SUCCESS, FAIL.
        :type Status: str
        :param ErrCodeExt: Error code. An empty string indicates the task is successful; otherwise it is failed. For details about the values, see [Error Code List](https://intl.cloud.tencent.com/document/product/862/50369?from_cn_redirect=1#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81).
        :type ErrCodeExt: str
        :param ErrCode: Error code. 0 indicates the task is successful; otherwise it is failed. This parameter is no longer recommended. Consider using the new error code parameter ErrCodeExt.
        :type ErrCode: int
        :param Message: Error message.
        :type Message: str
        :param Input: The input parameter for sensitive information detection.
        :type Input: :class:`tencentcloud.mps.v20190612.models.AiReviewPoliticalTaskInput`
        :param Output: The output of sensitive information detection.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Output: :class:`tencentcloud.mps.v20190612.models.AiReviewPoliticalTaskOutput`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewPoliticalTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewPoliticalTaskOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewTaskPornAsrResult(AbstractModel):
    """Result type of an ASR-based porn information detection in text task during content audit

    """

    def __init__(self):
        r"""
        :param Status: Task status. Valid values: PROCESSING, SUCCESS, FAIL.
        :type Status: str
        :param ErrCodeExt: Error code. An empty string indicates the task is successful; otherwise it is failed. For details about the values, see [Error Code List](https://intl.cloud.tencent.com/document/product/862/50369?from_cn_redirect=1#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81).
        :type ErrCodeExt: str
        :param ErrCode: Error code. 0 indicates the task is successful; otherwise it is failed. This parameter is no longer recommended. Consider using the new error code parameter ErrCodeExt.
        :type ErrCode: int
        :param Message: Error message.
        :type Message: str
        :param Input: Input for an ASR-based porn information detection in text task during content audit.
        :type Input: :class:`tencentcloud.mps.v20190612.models.AiReviewPornAsrTaskInput`
        :param Output: Output of an ASR-based porn information detection in text task during content audit.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Output: :class:`tencentcloud.mps.v20190612.models.AiReviewPornAsrTaskOutput`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewPornAsrTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewPornAsrTaskOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewTaskPornOcrResult(AbstractModel):
    """Result type of an OCR-based porn information detection in text task during content audit

    """

    def __init__(self):
        r"""
        :param Status: Task status. Valid values: PROCESSING, SUCCESS, FAIL.
        :type Status: str
        :param ErrCodeExt: Error code. An empty string indicates the task is successful; otherwise it is failed. For details about the values, see [Error Code List](https://intl.cloud.tencent.com/document/product/862/50369?from_cn_redirect=1#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81).
        :type ErrCodeExt: str
        :param ErrCode: Error code. 0 indicates the task is successful; otherwise it is failed. This parameter is no longer recommended. Consider using the new error code parameter ErrCodeExt.
        :type ErrCode: int
        :param Message: Error message.
        :type Message: str
        :param Input: Input for an OCR-based porn information detection in text task during content audit.
        :type Input: :class:`tencentcloud.mps.v20190612.models.AiReviewPornOcrTaskInput`
        :param Output: Output of an OCR-based porn information detection in text task during content audit.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Output: :class:`tencentcloud.mps.v20190612.models.AiReviewPornOcrTaskOutput`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewPornOcrTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewPornOcrTaskOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewTaskPornResult(AbstractModel):
    """Result type of a porn information detection task during content audit

    """

    def __init__(self):
        r"""
        :param Status: Task status. Valid values: PROCESSING, SUCCESS, FAIL.
        :type Status: str
        :param ErrCodeExt: Error code. An empty string indicates the task is successful; otherwise it is failed. For details about the values, see [Error Code List](https://intl.cloud.tencent.com/document/product/862/50369?from_cn_redirect=1#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81).
        :type ErrCodeExt: str
        :param ErrCode: Error code. 0 indicates the task is successful; otherwise it is failed. This parameter is no longer recommended. Consider using the new error code parameter ErrCodeExt.
        :type ErrCode: int
        :param Message: Error message.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Message: str
        :param Input: Input for a porn information detection task during content audit.
        :type Input: :class:`tencentcloud.mps.v20190612.models.AiReviewPornTaskInput`
        :param Output: Output of a porn information detection task during content audit.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Output: :class:`tencentcloud.mps.v20190612.models.AiReviewPornTaskOutput`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewPornTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewPornTaskOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewTaskProhibitedAsrResult(AbstractModel):
    """Result type of ASR-based prohibited information detection in speech task in content audit

    """

    def __init__(self):
        r"""
        :param Status: Task status. Valid values: PROCESSING, SUCCESS, FAIL.
        :type Status: str
        :param ErrCodeExt: Error code. An empty string indicates the task is successful; otherwise it is failed. For details about the values, see [Error Code List](https://intl.cloud.tencent.com/document/product/862/50369?from_cn_redirect=1#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81).
        :type ErrCodeExt: str
        :param ErrCode: Error code. 0: success; other values: failure.
<li>40000: invalid input parameter. Please check it;</li>
<li>60000: invalid source file (e.g., video data is corrupted). Please check whether the source file is normal;</li>
<li>70000: internal service error. Please try again.</li>
        :type ErrCode: int
        :param Message: Error message.
        :type Message: str
        :param Input: Input of ASR-based prohibited information detection in speech task in content audit
        :type Input: :class:`tencentcloud.mps.v20190612.models.AiReviewProhibitedAsrTaskInput`
        :param Output: Output of ASR-based prohibited information detection in speech task in content audit
        :type Output: :class:`tencentcloud.mps.v20190612.models.AiReviewProhibitedAsrTaskOutput`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewProhibitedAsrTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewProhibitedAsrTaskOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewTaskProhibitedOcrResult(AbstractModel):
    """Result type of OCR-based prohibited information detection in text task in content audit

    """

    def __init__(self):
        r"""
        :param Status: Task status. Valid values: PROCESSING, SUCCESS, FAIL.
        :type Status: str
        :param ErrCodeExt: Error code. An empty string indicates the task is successful; otherwise it is failed. For details about the values, see [Error Code List](https://intl.cloud.tencent.com/document/product/862/50369?from_cn_redirect=1#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81).
        :type ErrCodeExt: str
        :param ErrCode: Error code. 0: success; other values: failure.
<li>40000: invalid input parameter. Please check it;</li>
<li>60000: invalid source file (e.g., video data is corrupted). Please check whether the source file is normal;</li>
<li>70000: internal service error. Please try again.</li>
        :type ErrCode: int
        :param Message: Error message.
        :type Message: str
        :param Input: Input of OCR-based prohibited information detection in text task in content audit
        :type Input: :class:`tencentcloud.mps.v20190612.models.AiReviewProhibitedOcrTaskInput`
        :param Output: Output of OCR-based prohibited information detection in text task in content audit
        :type Output: :class:`tencentcloud.mps.v20190612.models.AiReviewProhibitedOcrTaskOutput`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewProhibitedOcrTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewProhibitedOcrTaskOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewTaskTerrorismOcrResult(AbstractModel):
    """The result of OCR-based detection of terrorism content.

    """

    def __init__(self):
        r"""
        :param Status: Task status. Valid values: PROCESSING, SUCCESS, FAIL.
        :type Status: str
        :param ErrCodeExt: Error code. An empty string indicates the task is successful; otherwise it is failed. For details about the values, see [Error Code List](https://intl.cloud.tencent.com/document/product/862/50369?from_cn_redirect=1#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81).
        :type ErrCodeExt: str
        :param ErrCode: Error code. 0: success; other values: failure.
<li>40000: invalid input parameter. Please check it;</li>
<li>60000: invalid source file (e.g., video data is corrupted). Please check whether the source file is normal;</li>
<li>70000: internal service error. Please try again.</li>
        :type ErrCode: int
        :param Message: Error message.
        :type Message: str
        :param Input: The input parameter for OCR-based detection of terrorism content.
        :type Input: :class:`tencentcloud.mps.v20190612.models.AiReviewTerrorismOcrTaskInput`
        :param Output: The output of OCR-based detection of terrorism content.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Output: :class:`tencentcloud.mps.v20190612.models.AiReviewTerrorismOcrTaskOutput`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewTerrorismOcrTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewTerrorismOcrTaskOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewTaskTerrorismResult(AbstractModel):
    """The result of sensitive information detection.

    """

    def __init__(self):
        r"""
        :param Status: Task status. Valid values: PROCESSING, SUCCESS, FAIL.
        :type Status: str
        :param ErrCodeExt: Error code. An empty string indicates the task is successful; otherwise it is failed. For details about the values, see [Error Code List](https://intl.cloud.tencent.com/document/product/862/50369?from_cn_redirect=1#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81).
        :type ErrCodeExt: str
        :param ErrCode: Error code. 0 indicates the task is successful; otherwise it is failed. This parameter is no longer recommended. Consider using the new error code parameter ErrCodeExt.
        :type ErrCode: int
        :param Message: Error message.
        :type Message: str
        :param Input: The input parameter for sensitive information detection.
        :type Input: :class:`tencentcloud.mps.v20190612.models.AiReviewTerrorismTaskInput`
        :param Output: The output of sensitive information detection.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Output: :class:`tencentcloud.mps.v20190612.models.AiReviewTerrorismTaskOutput`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewTerrorismTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewTerrorismTaskOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewTerrorismOcrTaskInput(AbstractModel):
    """The input parameter for OCR-based detection of sensitive information.

    """

    def __init__(self):
        r"""
        :param Definition: The template ID.
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewTerrorismOcrTaskOutput(AbstractModel):
    """The information about the sensitive content detected based on OCR.

    """

    def __init__(self):
        r"""
        :param Confidence: The confidence score for the OCR-based detection of sensitive information. Value range: 1-100.
        :type Confidence: float
        :param Suggestion: The suggestion for handling the sensitive information detected based on OCR. Valid values:
<li>pass</li>
<li>review</li>
<li>block</li>
        :type Suggestion: str
        :param SegmentSet: The video segments that contain sensitive information detected based on OCR.
        :type SegmentSet: list of MediaContentReviewOcrTextSegmentItem
        """
        self.Confidence = None
        self.Suggestion = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaContentReviewOcrTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewTerrorismTaskInput(AbstractModel):
    """The input parameter for the detection of sensitive information.

    """

    def __init__(self):
        r"""
        :param Definition: The template ID.
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewTerrorismTaskOutput(AbstractModel):
    """The information about the sensitive content detected.

    """

    def __init__(self):
        r"""
        :param Confidence: The confidence score for the detection of sensitive information. Value range: 0-100.
        :type Confidence: float
        :param Suggestion: The suggestion for handling the sensitive information detected. Valid values:
<li>pass</li>
<li>review</li>
<li>block</li>
        :type Suggestion: str
        :param Label: The labels for the detected sensitive content. Valid values:
<li>guns</li>
<li>crowd</li>
<li>police</li>
<li>bloody</li>
<li>banners (sensitive flags)</li>
<li>militant</li>
<li>explosion</li>
<li>terrorists</li>
<li>scenario (sensitive scenes) </li>
        :type Label: str
        :param SegmentSet: The video segments that contain sensitive information.
        :type SegmentSet: list of MediaContentReviewSegmentItem
        """
        self.Confidence = None
        self.Suggestion = None
        self.Label = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.Label = params.get("Label")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaContentReviewSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiSampleFaceInfo(AbstractModel):
    """AI-based sample management - face information.

    """

    def __init__(self):
        r"""
        :param FaceId: Face image ID.
        :type FaceId: str
        :param Url: Face image address.
        :type Url: str
        """
        self.FaceId = None
        self.Url = None


    def _deserialize(self, params):
        self.FaceId = params.get("FaceId")
        self.Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiSampleFaceOperation(AbstractModel):
    """AI-based sample management - face data operation.

    """

    def __init__(self):
        r"""
        :param Type: Operation type. Valid values: add, delete, reset. The `reset` operation will clear the existing face data of a figure and add `FaceContents` as the specified face data.
        :type Type: str
        :param FaceIds: Face ID set. This field is required when `Type` is `delete`.
        :type FaceIds: list of str
        :param FaceContents: String set generated by [Base64-encoding](https://tools.ietf.org/html/rfc4648) the face image.
<li>This field is required when `Type` is `add` or `reset`;</li>
<li>Array length limit: 5 images.</li>
Note: The image must be a relatively clear full-face photo of a figure in at least 200 * 200 px.
        :type FaceContents: list of str
        """
        self.Type = None
        self.FaceIds = None
        self.FaceContents = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.FaceIds = params.get("FaceIds")
        self.FaceContents = params.get("FaceContents")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiSampleFailFaceInfo(AbstractModel):
    """AI-based sample management - face information failing to be processed.

    """

    def __init__(self):
        r"""
        :param Index: Corresponds to incorrect image subscripts in the `FaceContents` input parameter, starting from 0.
        :type Index: int
        :param ErrCode: Error code. Valid values:
<li>0: Succeeded;</li>
<li>Other values: Failed.</li>
        :type ErrCode: int
        :param Message: Error description.
        :type Message: str
        """
        self.Index = None
        self.ErrCode = None
        self.Message = None


    def _deserialize(self, params):
        self.Index = params.get("Index")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiSamplePerson(AbstractModel):
    """AI-based sample management - figure information.

    """

    def __init__(self):
        r"""
        :param PersonId: Figure ID.
        :type PersonId: str
        :param Name: Name of a figure.
        :type Name: str
        :param Description: Figure description.
        :type Description: str
        :param FaceInfoSet: Face information.
        :type FaceInfoSet: list of AiSampleFaceInfo
        :param TagSet: Figure tag.
        :type TagSet: list of str
        :param UsageSet: Use case.
        :type UsageSet: list of str
        :param CreateTime: Creation time in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F).
        :type CreateTime: str
        :param UpdateTime: Last modified time in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F).
        :type UpdateTime: str
        """
        self.PersonId = None
        self.Name = None
        self.Description = None
        self.FaceInfoSet = None
        self.TagSet = None
        self.UsageSet = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        if params.get("FaceInfoSet") is not None:
            self.FaceInfoSet = []
            for item in params.get("FaceInfoSet"):
                obj = AiSampleFaceInfo()
                obj._deserialize(item)
                self.FaceInfoSet.append(obj)
        self.TagSet = params.get("TagSet")
        self.UsageSet = params.get("UsageSet")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiSampleTagOperation(AbstractModel):
    """AI-based sample management - tag operation.

    """

    def __init__(self):
        r"""
        :param Type: Operation type. Valid values: add, delete, reset.
        :type Type: str
        :param Tags: Tag. Length limit: 128 characters.
        :type Tags: list of str
        """
        self.Type = None
        self.Tags = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Tags = params.get("Tags")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiSampleWord(AbstractModel):
    """AI-based sample management - keyword output information.

    """

    def __init__(self):
        r"""
        :param Keyword: Keyword.
        :type Keyword: str
        :param TagSet: Keyword tag.
        :type TagSet: list of str
        :param UsageSet: Keyword use case.
        :type UsageSet: list of str
        :param CreateTime: Creation time in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F).
        :type CreateTime: str
        :param UpdateTime: Last modified time in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F).
        :type UpdateTime: str
        """
        self.Keyword = None
        self.TagSet = None
        self.UsageSet = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Keyword = params.get("Keyword")
        self.TagSet = params.get("TagSet")
        self.UsageSet = params.get("UsageSet")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiSampleWordInfo(AbstractModel):
    """AI-based sample management - keyword input information.

    """

    def __init__(self):
        r"""
        :param Keyword: Keyword. Length limit: 20 characters.
        :type Keyword: str
        :param Tags: Keyword tag
<li>Array length limit: 20 tags;</li>
<li>Tag length limit: 128 characters.</li>
        :type Tags: list of str
        """
        self.Keyword = None
        self.Tags = None


    def _deserialize(self, params):
        self.Keyword = params.get("Keyword")
        self.Tags = params.get("Tags")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnimatedGraphicTaskInput(AbstractModel):
    """Type of an animated image generating task.

    """

    def __init__(self):
        r"""
        :param Definition: Animated image generating template ID.
        :type Definition: int
        :param StartTimeOffset: Start time of an animated image in a video in seconds.
        :type StartTimeOffset: float
        :param EndTimeOffset: End time of an animated image in a video in seconds.
        :type EndTimeOffset: float
        :param OutputStorage: Target bucket of a generated animated image file. If this parameter is left empty, the `OutputStorage` value of the upper folder will be inherited.
Note: This field may return null, indicating that no valid values can be obtained.
        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        :param OutputObjectPath: Output path to a generated animated image file, which can be a relative path or an absolute path. If this parameter is left empty, the following relative path will be used by default: `{inputName}_animatedGraphic_{definition}.{format}`.
        :type OutputObjectPath: str
        """
        self.Definition = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.OutputStorage = None
        self.OutputObjectPath = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.OutputObjectPath = params.get("OutputObjectPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnimatedGraphicsTemplate(AbstractModel):
    """Details of an animated image generating template.

    """

    def __init__(self):
        r"""
        :param Definition: Unique ID of an animated image generating template.
        :type Definition: int
        :param Type: Template type. Valid values:
<li>Preset: Preset template;</li>
<li>Custom: Custom template.</li>
        :type Type: str
        :param Name: Name of an animated image generating template.
        :type Name: str
        :param Comment: Description of an animated image generating template.
        :type Comment: str
        :param Width: Maximum value of the width (or long side) of an animated image in px. Value range: 0 and [128, 4,096].
<li>If both `Width` and `Height` are 0, the resolution will be the same as that of the source video;</li>
<li>If `Width` is 0, but `Height` is not 0, `Width` will be proportionally scaled;</li>
<li>If `Width` is not 0, but `Height` is 0, `Height` will be proportionally scaled;</li>
<li>If both `Width` and `Height` are not 0, the custom resolution will be used.</li>
Default value: 0.
        :type Width: int
        :param Height: Maximum value of the height (or short side) of an animated image in px. Value range: 0 and [128, 4,096].
<li>If both `Width` and `Height` are 0, the resolution will be the same as that of the source video;</li>
<li>If `Width` is 0, but `Height` is not 0, `Width` will be proportionally scaled;</li>
<li>If `Width` is not 0, but `Height` is 0, `Height` will be proportionally scaled;</li>
<li>If both `Width` and `Height` are not 0, the custom resolution will be used.</li>
Default value: 0.
        :type Height: int
        :param ResolutionAdaptive: Resolution adaption. Valid values:
<li>open: Enabled. In this case, `Width` represents the long side of a video, while `Height` the short side;</li>
<li>close: Disabled. In this case, `Width` represents the width of a video, while `Height` the height.</li>
Default value: open.
        :type ResolutionAdaptive: str
        :param Format: Animated image format.
        :type Format: str
        :param Fps: Frame rate.
        :type Fps: int
        :param Quality: Image quality.
        :type Quality: float
        :param CreateTime: Creation time of a template in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F).
        :type CreateTime: str
        :param UpdateTime: Last modified time of a template in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F).
        :type UpdateTime: str
        """
        self.Definition = None
        self.Type = None
        self.Name = None
        self.Comment = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.Format = None
        self.Fps = None
        self.Quality = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Format = params.get("Format")
        self.Fps = params.get("Fps")
        self.Quality = params.get("Quality")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AsrFullTextConfigureInfo(AbstractModel):
    """Control parameter of a full speech recognition task.

    """

    def __init__(self):
        r"""
        :param Switch: Switch of a full speech recognition task. Valid values:
<li>ON: Enables an intelligent full speech recognition task;</li>
<li>OFF: Disables an intelligent full speech recognition task.</li>
        :type Switch: str
        :param SubtitleFormat: Format of the generated subtitles file. If this parameter is left empty or an empty string is entered, no subtitles files will be generated. Valid value:
<li>vtt: Generates a WebVTT subtitles file.</li>
        :type SubtitleFormat: str
        """
        self.Switch = None
        self.SubtitleFormat = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.SubtitleFormat = params.get("SubtitleFormat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AsrFullTextConfigureInfoForUpdate(AbstractModel):
    """Control parameter of a full speech recognition task.

    """

    def __init__(self):
        r"""
        :param Switch: Switch of a full speech recognition task. Valid values:
<li>ON: Enables an intelligent full speech recognition task;</li>
<li>OFF: Disables an intelligent full speech recognition task.</li>
        :type Switch: str
        :param SubtitleFormat: Format of the generated subtitles file. If an empty string is entered, no subtitles files will be generated. Valid value:
<li>vtt: Generates a WebVTT subtitles file.</li>
        :type SubtitleFormat: str
        """
        self.Switch = None
        self.SubtitleFormat = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.SubtitleFormat = params.get("SubtitleFormat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AsrWordsConfigureInfo(AbstractModel):
    """Speech keyword recognition control parameter.

    """

    def __init__(self):
        r"""
        :param Switch: Switch of a speech keyword recognition task. Valid values:
<li>ON: Enables a speech keyword recognition task;</li>
<li>OFF: Disables a speech keyword recognition task.</li>
        :type Switch: str
        :param LabelSet: Keyword filter tag, which specifies the keyword tag that needs to be returned. If this parameter is left empty, all results will be returned.
There can be up to 10 tags, each with a length limit of 16 characters.
        :type LabelSet: list of str
        """
        self.Switch = None
        self.LabelSet = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AsrWordsConfigureInfoForUpdate(AbstractModel):
    """Speech keyword recognition control parameter.

    """

    def __init__(self):
        r"""
        :param Switch: Switch of a speech keyword recognition task. Valid values:
<li>ON: Enables a speech keyword recognition task;</li>
<li>OFF: Disables a speech keyword recognition task.</li>
        :type Switch: str
        :param LabelSet: Keyword filter tag, which specifies the keyword tag that needs to be returned. If this parameter is left empty, all results will be returned.
There can be up to 10 tags, each with a length limit of 16 characters.
        :type LabelSet: list of str
        """
        self.Switch = None
        self.LabelSet = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioTemplateInfo(AbstractModel):
    """Audio stream configuration parameter

    """

    def __init__(self):
        r"""
        :param Codec: Audio stream codec.
When the outer `Container` parameter is `mp3`, the valid value is:
<li>libmp3lame.</li>
When the outer `Container` parameter is `ogg` or `flac`, the valid value is:
<li>flac.</li>
When the outer `Container` parameter is `m4a`, the valid values include:
<li>libfdk_aac;</li>
<li>libmp3lame;</li>
<li>ac3.</li>
When the outer `Container` parameter is `mp4` or `flv`, the valid values include:
<li>libfdk_aac: more suitable for mp4;</li>
<li>libmp3lame: more suitable for flv.</li>
When the outer `Container` parameter is `hls`, the valid values include:
<li>libfdk_aac;</li>
<li>libmp3lame.</li>
        :type Codec: str
        :param Bitrate: Audio stream bitrate in Kbps. Value range: 0 and [26, 256].
If the value is 0, the bitrate of the audio stream will be the same as that of the original audio.
        :type Bitrate: int
        :param SampleRate: Audio stream sample rate. Valid values:
<li>32,000</li>
<li>44,100</li>
<li>48,000</li>
In Hz.
        :type SampleRate: int
        :param AudioChannel: Audio channel system. Valid values:
<li>1: Mono</li>
<li>2: Dual</li>
<li>6: Stereo</li>
When the media is packaged in audio format (FLAC, OGG, MP3, M4A), the sound channel cannot be set to stereo.
Default value: 2
        :type AudioChannel: int
        """
        self.Codec = None
        self.Bitrate = None
        self.SampleRate = None
        self.AudioChannel = None


    def _deserialize(self, params):
        self.Codec = params.get("Codec")
        self.Bitrate = params.get("Bitrate")
        self.SampleRate = params.get("SampleRate")
        self.AudioChannel = params.get("AudioChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioTemplateInfoForUpdate(AbstractModel):
    """Audio stream configuration parameter

    """

    def __init__(self):
        r"""
        :param Codec: Audio stream codec.
When the outer `Container` parameter is `mp3`, the valid value is:
<li>libmp3lame.</li>
When the outer `Container` parameter is `ogg` or `flac`, the valid value is:
<li>flac.</li>
When the outer `Container` parameter is `m4a`, the valid values include:
<li>libfdk_aac;</li>
<li>libmp3lame;</li>
<li>ac3.</li>
When the outer `Container` parameter is `mp4` or `flv`, the valid values include:
<li>libfdk_aac: More suitable for mp4;</li>
<li>libmp3lame: More suitable for flv;</li>
<li>mp2.</li>
When the outer `Container` parameter is `hls`, the valid values include:
<li>libfdk_aac;</li>
<li>libmp3lame.</li>
        :type Codec: str
        :param Bitrate: Audio stream bitrate in Kbps. Value range: 0 and [26, 256]. If the value is 0, the bitrate of the audio stream will be the same as that of the original audio.
        :type Bitrate: int
        :param SampleRate: Audio stream sample rate. Valid values:
<li>32,000</li>
<li>44,100</li>
<li>48,000</li>
In Hz.
        :type SampleRate: int
        :param AudioChannel: Audio channel system. Valid values:
<li>1: Mono</li>
<li>2: Dual</li>
<li>6: Stereo</li>
When the media is packaged in audio format (FLAC, OGG, MP3, M4A), the sound channel cannot be set to stereo.
        :type AudioChannel: int
        """
        self.Codec = None
        self.Bitrate = None
        self.SampleRate = None
        self.AudioChannel = None


    def _deserialize(self, params):
        self.Codec = params.get("Codec")
        self.Bitrate = params.get("Bitrate")
        self.SampleRate = params.get("SampleRate")
        self.AudioChannel = params.get("AudioChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClassificationConfigureInfo(AbstractModel):
    """Control parameter of intelligent categorization task

    """

    def __init__(self):
        r"""
        :param Switch: Switch of intelligent categorization task. Valid values:
<li>ON: enables intelligent categorization task;</li>
<li>OFF: disables intelligent categorization task.</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClassificationConfigureInfoForUpdate(AbstractModel):
    """Control parameter of intelligent categorization task

    """

    def __init__(self):
        r"""
        :param Switch: Switch of intelligent categorization task. Valid values:
<li>ON: enables intelligent categorization task;</li>
<li>OFF: disables intelligent categorization task.</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContentReviewTemplateItem(AbstractModel):
    """Details of a content audit template

    """

    def __init__(self):
        r"""
        :param Definition: Unique ID of a content audit template.
        :type Definition: int
        :param Name: Name of a content audit template. Length limit: 64 characters.
        :type Name: str
        :param Comment: Description of a content audit template. Length limit: 256 characters.
        :type Comment: str
        :param PornConfigure: Porn information detection control parameter.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PornConfigure: :class:`tencentcloud.mps.v20190612.models.PornConfigureInfo`
        :param TerrorismConfigure: The parameters for detecting sensitive information.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type TerrorismConfigure: :class:`tencentcloud.mps.v20190612.models.TerrorismConfigureInfo`
        :param PoliticalConfigure: The parameters for detecting sensitive information.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type PoliticalConfigure: :class:`tencentcloud.mps.v20190612.models.PoliticalConfigureInfo`
        :param ProhibitedConfigure: Control parameter of prohibited information detection. Prohibited information includes:
<li>Abusive;</li>
<li>Drug-related.</li>
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProhibitedConfigure: :class:`tencentcloud.mps.v20190612.models.ProhibitedConfigureInfo`
        :param UserDefineConfigure: Custom content audit control parameter.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UserDefineConfigure: :class:`tencentcloud.mps.v20190612.models.UserDefineConfigureInfo`
        :param CreateTime: Creation time of a template in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F).
        :type CreateTime: str
        :param UpdateTime: Last modified time of a template in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F).
        :type UpdateTime: str
        :param Type: The template type. Valid values:
* Preset
* Custom
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Type: str
        """
        self.Definition = None
        self.Name = None
        self.Comment = None
        self.PornConfigure = None
        self.TerrorismConfigure = None
        self.PoliticalConfigure = None
        self.ProhibitedConfigure = None
        self.UserDefineConfigure = None
        self.CreateTime = None
        self.UpdateTime = None
        self.Type = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("PornConfigure") is not None:
            self.PornConfigure = PornConfigureInfo()
            self.PornConfigure._deserialize(params.get("PornConfigure"))
        if params.get("TerrorismConfigure") is not None:
            self.TerrorismConfigure = TerrorismConfigureInfo()
            self.TerrorismConfigure._deserialize(params.get("TerrorismConfigure"))
        if params.get("PoliticalConfigure") is not None:
            self.PoliticalConfigure = PoliticalConfigureInfo()
            self.PoliticalConfigure._deserialize(params.get("PoliticalConfigure"))
        if params.get("ProhibitedConfigure") is not None:
            self.ProhibitedConfigure = ProhibitedConfigureInfo()
            self.ProhibitedConfigure._deserialize(params.get("ProhibitedConfigure"))
        if params.get("UserDefineConfigure") is not None:
            self.UserDefineConfigure = UserDefineConfigureInfo()
            self.UserDefineConfigure._deserialize(params.get("UserDefineConfigure"))
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosFileUploadTrigger(AbstractModel):
    """Input rule bound to COS.

    """

    def __init__(self):
        r"""
        :param Bucket: Name of the COS bucket bound to a workflow, such as `TopRankVideo-125xxx88`.
        :type Bucket: str
        :param Region: Region of the COS bucket bound to a workflow, such as `ap-chongiqng`.
        :type Region: str
        :param Dir: Input path directory bound to a workflow, such as `/movie/201907/`. If this parameter is left empty, the `/` root directory will be used.
        :type Dir: str
        :param Formats: Format list of files that can trigger a workflow, such as ["mp4", "flv", "mov"]. If this parameter is left empty, files in all formats can trigger the workflow.
        :type Formats: list of str
        """
        self.Bucket = None
        self.Region = None
        self.Dir = None
        self.Formats = None


    def _deserialize(self, params):
        self.Bucket = params.get("Bucket")
        self.Region = params.get("Region")
        self.Dir = params.get("Dir")
        self.Formats = params.get("Formats")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosInputInfo(AbstractModel):
    """Information of the COS object for video processing.

    """

    def __init__(self):
        r"""
        :param Bucket: Name of the COS bucket where a video processing object file is located, such as `TopRankVideo-125xxx88`.
        :type Bucket: str
        :param Region: Region of the COS bucket where a video processing object file is located, such as `ap-chongqing`.
        :type Region: str
        :param Object: Path to an input object file for video processing, such as `/movie/201907/WildAnimal.mov`.
        :type Object: str
        """
        self.Bucket = None
        self.Region = None
        self.Object = None


    def _deserialize(self, params):
        self.Bucket = params.get("Bucket")
        self.Region = params.get("Region")
        self.Object = params.get("Object")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosOutputStorage(AbstractModel):
    """Information of a COS output object generated from video processing.

    """

    def __init__(self):
        r"""
        :param Bucket: Name of the target bucket of a video processing output file, such as `TopRankVideo-125xxx88`. If this parameter is left empty, the parameter of the upper folder will be inherited.
        :type Bucket: str
        :param Region: Region of the target bucket of a video processing output file, such as `ap-chongqing`. If this parameter is left empty, the parameter of the upper folder will be inherited.
        :type Region: str
        """
        self.Bucket = None
        self.Region = None


    def _deserialize(self, params):
        self.Bucket = params.get("Bucket")
        self.Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CoverConfigureInfo(AbstractModel):
    """Control parameter of intelligent cover generating task

    """

    def __init__(self):
        r"""
        :param Switch: Switch of intelligent cover generating task. Valid values:
<li>ON: enables intelligent cover generating task;</li>
<li>OFF: disables intelligent cover generating task.</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CoverConfigureInfoForUpdate(AbstractModel):
    """Control parameter of intelligent cover generating task

    """

    def __init__(self):
        r"""
        :param Switch: Switch of intelligent cover generating task. Valid values:
<li>ON: enables intelligent cover generating task;</li>
<li>OFF: disables intelligent cover generating task.</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAIAnalysisTemplateRequest(AbstractModel):
    """CreateAIAnalysisTemplate request structure.

    """

    def __init__(self):
        r"""
        :param Name: Video content analysis template name. Length limit: 64 characters.
        :type Name: str
        :param Comment: Video content analysis template description. Length limit: 256 characters.
        :type Comment: str
        :param ClassificationConfigure: Control parameter of intelligent categorization task.
        :type ClassificationConfigure: :class:`tencentcloud.mps.v20190612.models.ClassificationConfigureInfo`
        :param TagConfigure: Control parameter of intelligent tagging task.
        :type TagConfigure: :class:`tencentcloud.mps.v20190612.models.TagConfigureInfo`
        :param CoverConfigure: Control parameter of intelligent cover generating task.
        :type CoverConfigure: :class:`tencentcloud.mps.v20190612.models.CoverConfigureInfo`
        :param FrameTagConfigure: Control parameter of intelligent frame-specific tagging task.
        :type FrameTagConfigure: :class:`tencentcloud.mps.v20190612.models.FrameTagConfigureInfo`
        """
        self.Name = None
        self.Comment = None
        self.ClassificationConfigure = None
        self.TagConfigure = None
        self.CoverConfigure = None
        self.FrameTagConfigure = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("ClassificationConfigure") is not None:
            self.ClassificationConfigure = ClassificationConfigureInfo()
            self.ClassificationConfigure._deserialize(params.get("ClassificationConfigure"))
        if params.get("TagConfigure") is not None:
            self.TagConfigure = TagConfigureInfo()
            self.TagConfigure._deserialize(params.get("TagConfigure"))
        if params.get("CoverConfigure") is not None:
            self.CoverConfigure = CoverConfigureInfo()
            self.CoverConfigure._deserialize(params.get("CoverConfigure"))
        if params.get("FrameTagConfigure") is not None:
            self.FrameTagConfigure = FrameTagConfigureInfo()
            self.FrameTagConfigure._deserialize(params.get("FrameTagConfigure"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAIAnalysisTemplateResponse(AbstractModel):
    """CreateAIAnalysisTemplate response structure.

    """

    def __init__(self):
        r"""
        :param Definition: Unique ID of video content analysis template.
        :type Definition: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Definition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.RequestId = params.get("RequestId")


class CreateAIRecognitionTemplateRequest(AbstractModel):
    """CreateAIRecognitionTemplate request structure.

    """

    def __init__(self):
        r"""
        :param Name: Name of a video content recognition template. Length limit: 64 characters.
        :type Name: str
        :param Comment: Description of a video content recognition template. Length limit: 256 characters.
        :type Comment: str
        :param FaceConfigure: Face recognition control parameter.
        :type FaceConfigure: :class:`tencentcloud.mps.v20190612.models.FaceConfigureInfo`
        :param OcrFullTextConfigure: Full text recognition control parameter.
        :type OcrFullTextConfigure: :class:`tencentcloud.mps.v20190612.models.OcrFullTextConfigureInfo`
        :param OcrWordsConfigure: Text keyword recognition control parameter.
        :type OcrWordsConfigure: :class:`tencentcloud.mps.v20190612.models.OcrWordsConfigureInfo`
        :param AsrFullTextConfigure: Full speech recognition control parameter.
        :type AsrFullTextConfigure: :class:`tencentcloud.mps.v20190612.models.AsrFullTextConfigureInfo`
        :param AsrWordsConfigure: Speech keyword recognition control parameter.
        :type AsrWordsConfigure: :class:`tencentcloud.mps.v20190612.models.AsrWordsConfigureInfo`
        """
        self.Name = None
        self.Comment = None
        self.FaceConfigure = None
        self.OcrFullTextConfigure = None
        self.OcrWordsConfigure = None
        self.AsrFullTextConfigure = None
        self.AsrWordsConfigure = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("FaceConfigure") is not None:
            self.FaceConfigure = FaceConfigureInfo()
            self.FaceConfigure._deserialize(params.get("FaceConfigure"))
        if params.get("OcrFullTextConfigure") is not None:
            self.OcrFullTextConfigure = OcrFullTextConfigureInfo()
            self.OcrFullTextConfigure._deserialize(params.get("OcrFullTextConfigure"))
        if params.get("OcrWordsConfigure") is not None:
            self.OcrWordsConfigure = OcrWordsConfigureInfo()
            self.OcrWordsConfigure._deserialize(params.get("OcrWordsConfigure"))
        if params.get("AsrFullTextConfigure") is not None:
            self.AsrFullTextConfigure = AsrFullTextConfigureInfo()
            self.AsrFullTextConfigure._deserialize(params.get("AsrFullTextConfigure"))
        if params.get("AsrWordsConfigure") is not None:
            self.AsrWordsConfigure = AsrWordsConfigureInfo()
            self.AsrWordsConfigure._deserialize(params.get("AsrWordsConfigure"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAIRecognitionTemplateResponse(AbstractModel):
    """CreateAIRecognitionTemplate response structure.

    """

    def __init__(self):
        r"""
        :param Definition: Unique ID of a video content recognition template.
        :type Definition: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Definition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.RequestId = params.get("RequestId")


class CreateAdaptiveDynamicStreamingTemplateRequest(AbstractModel):
    """CreateAdaptiveDynamicStreamingTemplate request structure.

    """

    def __init__(self):
        r"""
        :param Format: Adaptive bitrate streaming format. Valid values:
<li>HLS,</li>
<li>MPEG-DASH.</li>
        :type Format: str
        :param StreamInfos: Parameter information of output substreams for transcoding to adaptive bitrate streaming. Up to 10 substreams can be output.
Note: the frame rate of each substream must be consistent; otherwise, the frame rate of the first substream is used as the output frame rate.
        :type StreamInfos: list of AdaptiveStreamTemplate
        :param Name: Template name. Length limit: 64 characters.
        :type Name: str
        :param DisableHigherVideoBitrate: Whether to prohibit transcoding from low bitrate to high bitrate. Valid values:
<li>0: no,</li>
<li>1: yes.</li>
Default value: 0.
        :type DisableHigherVideoBitrate: int
        :param DisableHigherVideoResolution: Whether to prohibit transcoding from low resolution to high resolution. Valid values:
<li>0: no,</li>
<li>1: yes.</li>
Default value: 0.
        :type DisableHigherVideoResolution: int
        :param Comment: Template description. Length limit: 256 characters.
        :type Comment: str
        """
        self.Format = None
        self.StreamInfos = None
        self.Name = None
        self.DisableHigherVideoBitrate = None
        self.DisableHigherVideoResolution = None
        self.Comment = None


    def _deserialize(self, params):
        self.Format = params.get("Format")
        if params.get("StreamInfos") is not None:
            self.StreamInfos = []
            for item in params.get("StreamInfos"):
                obj = AdaptiveStreamTemplate()
                obj._deserialize(item)
                self.StreamInfos.append(obj)
        self.Name = params.get("Name")
        self.DisableHigherVideoBitrate = params.get("DisableHigherVideoBitrate")
        self.DisableHigherVideoResolution = params.get("DisableHigherVideoResolution")
        self.Comment = params.get("Comment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAdaptiveDynamicStreamingTemplateResponse(AbstractModel):
    """CreateAdaptiveDynamicStreamingTemplate response structure.

    """

    def __init__(self):
        r"""
        :param Definition: Unique ID of an adaptive bitrate streaming template.
        :type Definition: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Definition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.RequestId = params.get("RequestId")


class CreateAnimatedGraphicsTemplateRequest(AbstractModel):
    """CreateAnimatedGraphicsTemplate request structure.

    """

    def __init__(self):
        r"""
        :param Fps: Video frame rate in Hz. Value range: [1, 30].
        :type Fps: int
        :param Width: Maximum value of the width (or long side) of an animated image in px. Value range: 0 and [128, 4,096].
<li>If both `Width` and `Height` are 0, the resolution will be the same as that of the source video;</li>
<li>If `Width` is 0, but `Height` is not 0, `Width` will be proportionally scaled;</li>
<li>If `Width` is not 0, but `Height` is 0, `Height` will be proportionally scaled;</li>
<li>If both `Width` and `Height` are not 0, the custom resolution will be used.</li>
Default value: 0.
        :type Width: int
        :param Height: Maximum value of the height (or short side) of a video stream in px. Value range: 0 and [128, 4,096].
<li>If both `Width` and `Height` are 0, the resolution will be the same as that of the source video;</li>
<li>If `Width` is 0, but `Height` is not 0, `Width` will be proportionally scaled;</li>
<li>If `Width` is not 0, but `Height` is 0, `Height` will be proportionally scaled;</li>
<li>If both `Width` and `Height` are not 0, the custom resolution will be used.</li>
Default value: 0.
        :type Height: int
        :param ResolutionAdaptive: Resolution adaption. Valid values:
<li>open: enabled. In this case, `Width` represents the long side of a video, while `Height` the short side;</li>
<li>close: disabled. In this case, `Width` represents the width of a video, while `Height` the height.</li>
Default value: open.
        :type ResolutionAdaptive: str
        :param Format: Animated image format. Valid values: gif; webp. Default value: gif.
        :type Format: str
        :param Quality: Image quality. Value range: [1, 100]. Default value: 75.
        :type Quality: float
        :param Name: Name of an animated image generating template. Length limit: 64 characters.
        :type Name: str
        :param Comment: Template description. Length limit: 256 characters.
        :type Comment: str
        """
        self.Fps = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.Format = None
        self.Quality = None
        self.Name = None
        self.Comment = None


    def _deserialize(self, params):
        self.Fps = params.get("Fps")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Format = params.get("Format")
        self.Quality = params.get("Quality")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAnimatedGraphicsTemplateResponse(AbstractModel):
    """CreateAnimatedGraphicsTemplate response structure.

    """

    def __init__(self):
        r"""
        :param Definition: Unique ID of an animated image generating template.
        :type Definition: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Definition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.RequestId = params.get("RequestId")


class CreateContentReviewTemplateRequest(AbstractModel):
    """CreateContentReviewTemplate request structure.

    """

    def __init__(self):
        r"""
        :param Name: Name of an intelligent content recognition template. Length limit: 64 characters
        :type Name: str
        :param Comment: Description of an intelligent content recognition template. Length limit: 256 characters
        :type Comment: str
        :param PornConfigure: Control parameter for porn information
        :type PornConfigure: :class:`tencentcloud.mps.v20190612.models.PornConfigureInfo`
        :param TerrorismConfigure: Control parameter for terrorism information
        :type TerrorismConfigure: :class:`tencentcloud.mps.v20190612.models.TerrorismConfigureInfo`
        :param PoliticalConfigure: Control parameter for politically sensitive information
        :type PoliticalConfigure: :class:`tencentcloud.mps.v20190612.models.PoliticalConfigureInfo`
        :param ProhibitedConfigure: Control parameter of prohibited information detection. Prohibited information includes:
<li>Abusive;</li>
<li>Drug-related.</li>
Note: this parameter is not supported yet.
        :type ProhibitedConfigure: :class:`tencentcloud.mps.v20190612.models.ProhibitedConfigureInfo`
        :param UserDefineConfigure: Control parameter for custom intelligent content recognition tasks
        :type UserDefineConfigure: :class:`tencentcloud.mps.v20190612.models.UserDefineConfigureInfo`
        """
        self.Name = None
        self.Comment = None
        self.PornConfigure = None
        self.TerrorismConfigure = None
        self.PoliticalConfigure = None
        self.ProhibitedConfigure = None
        self.UserDefineConfigure = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("PornConfigure") is not None:
            self.PornConfigure = PornConfigureInfo()
            self.PornConfigure._deserialize(params.get("PornConfigure"))
        if params.get("TerrorismConfigure") is not None:
            self.TerrorismConfigure = TerrorismConfigureInfo()
            self.TerrorismConfigure._deserialize(params.get("TerrorismConfigure"))
        if params.get("PoliticalConfigure") is not None:
            self.PoliticalConfigure = PoliticalConfigureInfo()
            self.PoliticalConfigure._deserialize(params.get("PoliticalConfigure"))
        if params.get("ProhibitedConfigure") is not None:
            self.ProhibitedConfigure = ProhibitedConfigureInfo()
            self.ProhibitedConfigure._deserialize(params.get("ProhibitedConfigure"))
        if params.get("UserDefineConfigure") is not None:
            self.UserDefineConfigure = UserDefineConfigureInfo()
            self.UserDefineConfigure._deserialize(params.get("UserDefineConfigure"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateContentReviewTemplateResponse(AbstractModel):
    """CreateContentReviewTemplate response structure.

    """

    def __init__(self):
        r"""
        :param Definition: Unique ID of an intelligent content recognition template
        :type Definition: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Definition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.RequestId = params.get("RequestId")


class CreateImageSpriteTemplateRequest(AbstractModel):
    """CreateImageSpriteTemplate request structure.

    """

    def __init__(self):
        r"""
        :param SampleType: Sampling type. Valid values:
<li>Percent: By percent.</li>
<li>Time: By time interval.</li>
        :type SampleType: str
        :param SampleInterval: Sampling interval.
<li>If `SampleType` is `Percent`, sampling will be performed at an interval of the specified percentage.</li>
<li>If `SampleType` is `Time`, sampling will be performed at the specified time interval in seconds.</li>
        :type SampleInterval: int
        :param RowCount: Subimage row count of an image sprite.
        :type RowCount: int
        :param ColumnCount: Subimage column count of an image sprite.
        :type ColumnCount: int
        :param Name: Name of an image sprite generating template. Length limit: 64 characters.
        :type Name: str
        :param Width: Subimage width of an image sprite in px. Value range: [128, 4,096].
        :type Width: int
        :param Height: Subimage height of an image sprite in px. Value range: [128, 4,096].
        :type Height: int
        :param ResolutionAdaptive: Resolution adaption. Valid values:
<li>open: enabled. In this case, `Width` represents the long side of a video, while `Height` the short side;</li>
<li>close: disabled. In this case, `Width` represents the width of a video, while `Height` the height.</li>
Default value: open.
        :type ResolutionAdaptive: str
        :param FillType: Fill type. "Fill" refers to the way of processing a screenshot when its aspect ratio is different from that of the source video. The following fill types are supported:
<li> stretch: stretch. The screenshot will be stretched frame by frame to match the aspect ratio of the source video, which may make the screenshot "shorter" or "longer";</li>
<li>black: fill with black. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with black color blocks.</li>
Default value: black.
        :type FillType: str
        :param Comment: Template description. Length limit: 256 characters.
        :type Comment: str
        """
        self.SampleType = None
        self.SampleInterval = None
        self.RowCount = None
        self.ColumnCount = None
        self.Name = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.FillType = None
        self.Comment = None


    def _deserialize(self, params):
        self.SampleType = params.get("SampleType")
        self.SampleInterval = params.get("SampleInterval")
        self.RowCount = params.get("RowCount")
        self.ColumnCount = params.get("ColumnCount")
        self.Name = params.get("Name")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.FillType = params.get("FillType")
        self.Comment = params.get("Comment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateImageSpriteTemplateResponse(AbstractModel):
    """CreateImageSpriteTemplate response structure.

    """

    def __init__(self):
        r"""
        :param Definition: Unique ID of an image sprite generating template.
        :type Definition: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Definition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.RequestId = params.get("RequestId")


class CreatePersonSampleRequest(AbstractModel):
    """CreatePersonSample request structure.

    """

    def __init__(self):
        r"""
        :param Name: Name of an image. Length limit: 20 characters
        :type Name: str
        :param Usages: Image usage. Valid values:
1. Recognition: used for content recognition; equivalent to `Recognition.Face`
2. Review: used for inappropriate information recognition; equivalent to `Review.Face`
3. All: equivalent to 1+2
        :type Usages: list of str
        :param Description: Image description. Length limit: 1,024 characters
        :type Description: str
        :param FaceContents: [Base64](https://tools.ietf.org/html/rfc4648) string converted from an image. Only JPEG and PNG images are supported. Array length limit: 5 images
Note: the image must be a relatively clear facial feature photo of one person with a size of at least 200 x 200 pixels.
        :type FaceContents: list of str
        :param Tags: Image tag
<li>Array length limit: 20 tags</li>
<li>Tag length limit: 128 characters</li>
        :type Tags: list of str
        """
        self.Name = None
        self.Usages = None
        self.Description = None
        self.FaceContents = None
        self.Tags = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Usages = params.get("Usages")
        self.Description = params.get("Description")
        self.FaceContents = params.get("FaceContents")
        self.Tags = params.get("Tags")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePersonSampleResponse(AbstractModel):
    """CreatePersonSample response structure.

    """

    def __init__(self):
        r"""
        :param Person: Image information
        :type Person: :class:`tencentcloud.mps.v20190612.models.AiSamplePerson`
        :param FailFaceInfoSet: Information of images that failed the verification by facial feature positioning
        :type FailFaceInfoSet: list of AiSampleFailFaceInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Person = None
        self.FailFaceInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Person") is not None:
            self.Person = AiSamplePerson()
            self.Person._deserialize(params.get("Person"))
        if params.get("FailFaceInfoSet") is not None:
            self.FailFaceInfoSet = []
            for item in params.get("FailFaceInfoSet"):
                obj = AiSampleFailFaceInfo()
                obj._deserialize(item)
                self.FailFaceInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class CreateSampleSnapshotTemplateRequest(AbstractModel):
    """CreateSampleSnapshotTemplate request structure.

    """

    def __init__(self):
        r"""
        :param SampleType: Sampled screencapturing type. Valid values:
<li>Percent: By percent.</li>
<li>Time: By time interval.</li>
        :type SampleType: str
        :param SampleInterval: Sampling interval.
<li>If `SampleType` is `Percent`, sampling will be performed at an interval of the specified percentage.</li>
<li>If `SampleType` is `Time`, sampling will be performed at the specified time interval in seconds.</li>
        :type SampleInterval: int
        :param Name: Name of a sampled screencapturing template. Length limit: 64 characters.
        :type Name: str
        :param Width: Image width in px. Value range: [128, 4,096].
        :type Width: int
        :param Height: Image height in px. Value range: [128, 4,096].
        :type Height: int
        :param ResolutionAdaptive: Resolution adaption. Valid values:
<li>open: enabled. In this case, `Width` represents the long side of a video, while `Height` the short side;</li>
<li>close: disabled. In this case, `Width` represents the width of a video, while `Height` the height.</li>
Default value: open.
        :type ResolutionAdaptive: str
        :param Format: Image format. Valid values: jpg; png. Default value: jpg.
        :type Format: str
        :param Comment: Template description. Length limit: 256 characters.
        :type Comment: str
        :param FillType: Fill type. "Fill" refers to the way of processing a screenshot when its aspect ratio is different from that of the source video. The following fill types are supported:
<li> stretch: stretch. The screenshot will be stretched frame by frame to match the aspect ratio of the source video, which may make the screenshot "shorter" or "longer";</li>
<li>black: fill with black. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with black color blocks.</li>
<li>white: fill with white. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with white color blocks.</li>
<li>gauss: fill with Gaussian blur. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with Gaussian blur.</li>
Default value: black.
        :type FillType: str
        """
        self.SampleType = None
        self.SampleInterval = None
        self.Name = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.Format = None
        self.Comment = None
        self.FillType = None


    def _deserialize(self, params):
        self.SampleType = params.get("SampleType")
        self.SampleInterval = params.get("SampleInterval")
        self.Name = params.get("Name")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Format = params.get("Format")
        self.Comment = params.get("Comment")
        self.FillType = params.get("FillType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSampleSnapshotTemplateResponse(AbstractModel):
    """CreateSampleSnapshotTemplate response structure.

    """

    def __init__(self):
        r"""
        :param Definition: Unique ID of a sampled screencapturing template.
        :type Definition: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Definition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.RequestId = params.get("RequestId")


class CreateSnapshotByTimeOffsetTemplateRequest(AbstractModel):
    """CreateSnapshotByTimeOffsetTemplate request structure.

    """

    def __init__(self):
        r"""
        :param Name: Name of a time point screencapturing template. Length limit: 64 characters.
        :type Name: str
        :param Width: Image width in px. Value range: [128, 4,096].
        :type Width: int
        :param Height: Image height in px. Value range: [128, 4,096].
        :type Height: int
        :param ResolutionAdaptive: Resolution adaption. Valid values:
<li>open: enabled. In this case, `Width` represents the long side of a video, while `Height` the short side;</li>
<li>close: disabled. In this case, `Width` represents the width of a video, while `Height` the height.</li>
Default value: open.
        :type ResolutionAdaptive: str
        :param Format: Image format. Valid values: jpg; png. Default value: jpg.
        :type Format: str
        :param Comment: Template description. Length limit: 256 characters.
        :type Comment: str
        :param FillType: Fill type. "Fill" refers to the way of processing a screenshot when its aspect ratio is different from that of the source video. The following fill types are supported:
<li> stretch: stretch. The screenshot will be stretched frame by frame to match the aspect ratio of the source video, which may make the screenshot "shorter" or "longer";</li>
<li>black: fill with black. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with black color blocks.</li>
<li>white: fill with white. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with white color blocks.</li>
<li>gauss: fill with Gaussian blur. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with Gaussian blur.</li>
Default value: black.
        :type FillType: str
        """
        self.Name = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.Format = None
        self.Comment = None
        self.FillType = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Format = params.get("Format")
        self.Comment = params.get("Comment")
        self.FillType = params.get("FillType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSnapshotByTimeOffsetTemplateResponse(AbstractModel):
    """CreateSnapshotByTimeOffsetTemplate response structure.

    """

    def __init__(self):
        r"""
        :param Definition: Unique ID of a time point screencapturing template.
        :type Definition: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Definition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.RequestId = params.get("RequestId")


class CreateTranscodeTemplateRequest(AbstractModel):
    """CreateTranscodeTemplate request structure.

    """

    def __init__(self):
        r"""
        :param Container: Container format. Valid values: mp4; flv; hls; mp3; flac; ogg; m4a. Among them, mp3, flac, ogg, and m4a are for audio files.
        :type Container: str
        :param Name: Name of a transcoding template. Length limit: 64 characters.
        :type Name: str
        :param Comment: Template description. Length limit: 256 characters.
        :type Comment: str
        :param RemoveVideo: Whether to remove video data. Valid values:
<li>0: Retain</li>
<li>1: Remove</li>
Default value: 0.
        :type RemoveVideo: int
        :param RemoveAudio: Whether to remove audio data. Valid values:
<li>0: Retain</li>
<li>1: Remove</li>
Default value: 0.
        :type RemoveAudio: int
        :param VideoTemplate: Video stream configuration parameter. This field is required when `RemoveVideo` is 0.
        :type VideoTemplate: :class:`tencentcloud.mps.v20190612.models.VideoTemplateInfo`
        :param AudioTemplate: Audio stream configuration parameter. This field is required when `RemoveAudio` is 0.
        :type AudioTemplate: :class:`tencentcloud.mps.v20190612.models.AudioTemplateInfo`
        :param TEHDConfig: TESHD transcoding parameter. To enable it, please contact your Tencent Cloud sales rep.
        :type TEHDConfig: :class:`tencentcloud.mps.v20190612.models.TEHDConfig`
        """
        self.Container = None
        self.Name = None
        self.Comment = None
        self.RemoveVideo = None
        self.RemoveAudio = None
        self.VideoTemplate = None
        self.AudioTemplate = None
        self.TEHDConfig = None


    def _deserialize(self, params):
        self.Container = params.get("Container")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.RemoveVideo = params.get("RemoveVideo")
        self.RemoveAudio = params.get("RemoveAudio")
        if params.get("VideoTemplate") is not None:
            self.VideoTemplate = VideoTemplateInfo()
            self.VideoTemplate._deserialize(params.get("VideoTemplate"))
        if params.get("AudioTemplate") is not None:
            self.AudioTemplate = AudioTemplateInfo()
            self.AudioTemplate._deserialize(params.get("AudioTemplate"))
        if params.get("TEHDConfig") is not None:
            self.TEHDConfig = TEHDConfig()
            self.TEHDConfig._deserialize(params.get("TEHDConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTranscodeTemplateResponse(AbstractModel):
    """CreateTranscodeTemplate response structure.

    """

    def __init__(self):
        r"""
        :param Definition: Unique ID of a transcoding template.
        :type Definition: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Definition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.RequestId = params.get("RequestId")


class CreateWatermarkTemplateRequest(AbstractModel):
    """CreateWatermarkTemplate request structure.

    """

    def __init__(self):
        r"""
        :param Type: Watermarking type. Valid values:
<li>image: Image watermark;</li>
<li>text: Text watermark;</li>
<li>svg: SVG watermark.</li>
        :type Type: str
        :param Name: Watermarking template name. Length limit: 64 characters.
        :type Name: str
        :param Comment: Template description. Length limit: 256 characters.
        :type Comment: str
        :param CoordinateOrigin: Origin position. Valid values:
<li>TopLeft: The origin of coordinates is in the top-left corner of the video, and the origin of the watermark is in the top-left corner of the image or text;</li>
<li>TopRight: The origin of coordinates is in the top-right corner of the video, and the origin of the watermark is in the top-right corner of the image or text;</li>
<li>BottomLeft: The origin of coordinates is in the bottom-left corner of the video, and the origin of the watermark is in the bottom-left corner of the image or text;</li>
<li>BottomRight: The origin of coordinates is in the bottom-right corner of the video, and the origin of the watermark is in the bottom-right corner of the image or text.</li>
Default value: TopLeft.
        :type CoordinateOrigin: str
        :param XPos: The horizontal position of the origin of the watermark relative to the origin of coordinates of the video. % and px formats are supported:
<li>If the string ends in %, the `XPos` of the watermark will be the specified percentage of the video width; for example, `10%` means that `XPos` is 10% of the video width;</li>
<li>If the string ends in px, the `XPos` of the watermark will be the specified px; for example, `100px` means that `XPos` is 100 px.</li>
Default value: 0 px.
        :type XPos: str
        :param YPos: The vertical position of the origin of the watermark relative to the origin of coordinates of the video. % and px formats are supported:
<li>If the string ends in %, the `YPos` of the watermark will be the specified percentage of the video height; for example, `10%` means that `YPos` is 10% of the video height;</li>
<li>If the string ends in px, the `YPos` of the watermark will be the specified px; for example, `100px` means that `YPos` is 100 px.</li>
Default value: 0 px.
        :type YPos: str
        :param ImageTemplate: Image watermarking template. This field is required and valid only when `Type` is `image`.
        :type ImageTemplate: :class:`tencentcloud.mps.v20190612.models.ImageWatermarkInput`
        :param TextTemplate: Text watermarking template. This field is required and valid only when `Type` is `text`.
        :type TextTemplate: :class:`tencentcloud.mps.v20190612.models.TextWatermarkTemplateInput`
        :param SvgTemplate: SVG watermarking template. This field is required and valid only when `Type` is `svg`.
        :type SvgTemplate: :class:`tencentcloud.mps.v20190612.models.SvgWatermarkInput`
        """
        self.Type = None
        self.Name = None
        self.Comment = None
        self.CoordinateOrigin = None
        self.XPos = None
        self.YPos = None
        self.ImageTemplate = None
        self.TextTemplate = None
        self.SvgTemplate = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.CoordinateOrigin = params.get("CoordinateOrigin")
        self.XPos = params.get("XPos")
        self.YPos = params.get("YPos")
        if params.get("ImageTemplate") is not None:
            self.ImageTemplate = ImageWatermarkInput()
            self.ImageTemplate._deserialize(params.get("ImageTemplate"))
        if params.get("TextTemplate") is not None:
            self.TextTemplate = TextWatermarkTemplateInput()
            self.TextTemplate._deserialize(params.get("TextTemplate"))
        if params.get("SvgTemplate") is not None:
            self.SvgTemplate = SvgWatermarkInput()
            self.SvgTemplate._deserialize(params.get("SvgTemplate"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWatermarkTemplateResponse(AbstractModel):
    """CreateWatermarkTemplate response structure.

    """

    def __init__(self):
        r"""
        :param Definition: Unique ID of a watermarking template.
        :type Definition: int
        :param ImageUrl: Watermark image address. This field is valid only when `Type` is `image`.
        :type ImageUrl: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Definition = None
        self.ImageUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.ImageUrl = params.get("ImageUrl")
        self.RequestId = params.get("RequestId")


class CreateWordSamplesRequest(AbstractModel):
    """CreateWordSamples request structure.

    """

    def __init__(self):
        r"""
        :param Usages: <b>Keyword usage. Valid values:</b>
1. Recognition.Ocr: OCR-based content recognition
2. Recognition.Asr: ASR-based content recognition
3. Review.Ocr: OCR-based inappropriate information recognition
4. Review.Asr: ASR-based inappropriate information recognition
<b>Valid values can also be:</b>
5. Recognition: ASR- and OCR-based content recognition; equivalent to 1+2
6. Review: ASR- and OCR-based inappropriate information recognition; equivalent to 3+4
7. All: ASR- and OCR-based content recognition and inappropriate information detection; equivalent to 1+2+3+4
        :type Usages: list of str
        :param Words: Keyword. Array length limit: 100.
        :type Words: list of AiSampleWordInfo
        """
        self.Usages = None
        self.Words = None


    def _deserialize(self, params):
        self.Usages = params.get("Usages")
        if params.get("Words") is not None:
            self.Words = []
            for item in params.get("Words"):
                obj = AiSampleWordInfo()
                obj._deserialize(item)
                self.Words.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWordSamplesResponse(AbstractModel):
    """CreateWordSamples response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateWorkflowRequest(AbstractModel):
    """CreateWorkflow request structure.

    """

    def __init__(self):
        r"""
        :param WorkflowName: Workflow name of up to 128 characters, which must be unique for the same user.
        :type WorkflowName: str
        :param Trigger: Triggering rule bound to a workflow. If an uploaded video hits the rule for the object, the workflow will be triggered.
        :type Trigger: :class:`tencentcloud.mps.v20190612.models.WorkflowTrigger`
        :param OutputStorage: Storage location of a video processing output file. If this parameter is left empty, the storage location in `Trigger` will be inherited.
        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        :param OutputDir: Target directory of a video processing output file, such as `/movie/201907/`. If this parameter is left empty, the file will be outputted to the same directory where the source file is located.
        :type OutputDir: str
        :param MediaProcessTask: Parameter of a video processing task.
        :type MediaProcessTask: :class:`tencentcloud.mps.v20190612.models.MediaProcessTaskInput`
        :param AiContentReviewTask: Type parameter of a video content audit task.
        :type AiContentReviewTask: :class:`tencentcloud.mps.v20190612.models.AiContentReviewTaskInput`
        :param AiAnalysisTask: Video content analysis task parameter.
        :type AiAnalysisTask: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskInput`
        :param AiRecognitionTask: Type parameter of a video content recognition task.
        :type AiRecognitionTask: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskInput`
        :param TaskNotifyConfig: Event notification configuration for a task. If this parameter is left empty, no event notifications will be obtained.
        :type TaskNotifyConfig: :class:`tencentcloud.mps.v20190612.models.TaskNotifyConfig`
        :param TaskPriority: Workflow priority. The higher the value, the higher the priority. Value range: [-10, 10]. If this parameter is left empty, 0 will be used.
        :type TaskPriority: int
        """
        self.WorkflowName = None
        self.Trigger = None
        self.OutputStorage = None
        self.OutputDir = None
        self.MediaProcessTask = None
        self.AiContentReviewTask = None
        self.AiAnalysisTask = None
        self.AiRecognitionTask = None
        self.TaskNotifyConfig = None
        self.TaskPriority = None


    def _deserialize(self, params):
        self.WorkflowName = params.get("WorkflowName")
        if params.get("Trigger") is not None:
            self.Trigger = WorkflowTrigger()
            self.Trigger._deserialize(params.get("Trigger"))
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.OutputDir = params.get("OutputDir")
        if params.get("MediaProcessTask") is not None:
            self.MediaProcessTask = MediaProcessTaskInput()
            self.MediaProcessTask._deserialize(params.get("MediaProcessTask"))
        if params.get("AiContentReviewTask") is not None:
            self.AiContentReviewTask = AiContentReviewTaskInput()
            self.AiContentReviewTask._deserialize(params.get("AiContentReviewTask"))
        if params.get("AiAnalysisTask") is not None:
            self.AiAnalysisTask = AiAnalysisTaskInput()
            self.AiAnalysisTask._deserialize(params.get("AiAnalysisTask"))
        if params.get("AiRecognitionTask") is not None:
            self.AiRecognitionTask = AiRecognitionTaskInput()
            self.AiRecognitionTask._deserialize(params.get("AiRecognitionTask"))
        if params.get("TaskNotifyConfig") is not None:
            self.TaskNotifyConfig = TaskNotifyConfig()
            self.TaskNotifyConfig._deserialize(params.get("TaskNotifyConfig"))
        self.TaskPriority = params.get("TaskPriority")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWorkflowResponse(AbstractModel):
    """CreateWorkflow response structure.

    """

    def __init__(self):
        r"""
        :param WorkflowId: Workflow ID.
        :type WorkflowId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.WorkflowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.WorkflowId = params.get("WorkflowId")
        self.RequestId = params.get("RequestId")


class DeleteAIAnalysisTemplateRequest(AbstractModel):
    """DeleteAIAnalysisTemplate request structure.

    """

    def __init__(self):
        r"""
        :param Definition: Unique ID of video content analysis template.
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAIAnalysisTemplateResponse(AbstractModel):
    """DeleteAIAnalysisTemplate response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteAIRecognitionTemplateRequest(AbstractModel):
    """DeleteAIRecognitionTemplate request structure.

    """

    def __init__(self):
        r"""
        :param Definition: Unique ID of a video content recognition template.
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAIRecognitionTemplateResponse(AbstractModel):
    """DeleteAIRecognitionTemplate response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteAdaptiveDynamicStreamingTemplateRequest(AbstractModel):
    """DeleteAdaptiveDynamicStreamingTemplate request structure.

    """

    def __init__(self):
        r"""
        :param Definition: Unique ID of an adaptive bitrate streaming template.
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAdaptiveDynamicStreamingTemplateResponse(AbstractModel):
    """DeleteAdaptiveDynamicStreamingTemplate response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteAnimatedGraphicsTemplateRequest(AbstractModel):
    """DeleteAnimatedGraphicsTemplate request structure.

    """

    def __init__(self):
        r"""
        :param Definition: Unique ID of an animated image generating template.
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAnimatedGraphicsTemplateResponse(AbstractModel):
    """DeleteAnimatedGraphicsTemplate response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteContentReviewTemplateRequest(AbstractModel):
    """DeleteContentReviewTemplate request structure.

    """

    def __init__(self):
        r"""
        :param Definition: Unique ID of an intelligent content recognition template
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteContentReviewTemplateResponse(AbstractModel):
    """DeleteContentReviewTemplate response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteImageSpriteTemplateRequest(AbstractModel):
    """DeleteImageSpriteTemplate request structure.

    """

    def __init__(self):
        r"""
        :param Definition: Unique ID of an image sprite generating template.
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteImageSpriteTemplateResponse(AbstractModel):
    """DeleteImageSpriteTemplate response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeletePersonSampleRequest(AbstractModel):
    """DeletePersonSample request structure.

    """

    def __init__(self):
        r"""
        :param PersonId: Image ID
        :type PersonId: str
        """
        self.PersonId = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePersonSampleResponse(AbstractModel):
    """DeletePersonSample response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSampleSnapshotTemplateRequest(AbstractModel):
    """DeleteSampleSnapshotTemplate request structure.

    """

    def __init__(self):
        r"""
        :param Definition: Unique ID of a sampled screencapturing template.
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSampleSnapshotTemplateResponse(AbstractModel):
    """DeleteSampleSnapshotTemplate response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSnapshotByTimeOffsetTemplateRequest(AbstractModel):
    """DeleteSnapshotByTimeOffsetTemplate request structure.

    """

    def __init__(self):
        r"""
        :param Definition: Unique ID of a time point screencapturing template.
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSnapshotByTimeOffsetTemplateResponse(AbstractModel):
    """DeleteSnapshotByTimeOffsetTemplate response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTranscodeTemplateRequest(AbstractModel):
    """DeleteTranscodeTemplate request structure.

    """

    def __init__(self):
        r"""
        :param Definition: Unique ID of a transcoding template.
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTranscodeTemplateResponse(AbstractModel):
    """DeleteTranscodeTemplate response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteWatermarkTemplateRequest(AbstractModel):
    """DeleteWatermarkTemplate request structure.

    """

    def __init__(self):
        r"""
        :param Definition: Unique ID of a watermarking template.
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteWatermarkTemplateResponse(AbstractModel):
    """DeleteWatermarkTemplate response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteWordSamplesRequest(AbstractModel):
    """DeleteWordSamples request structure.

    """

    def __init__(self):
        r"""
        :param Keywords: Keyword. Array length limit: 100 words.
        :type Keywords: list of str
        """
        self.Keywords = None


    def _deserialize(self, params):
        self.Keywords = params.get("Keywords")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteWordSamplesResponse(AbstractModel):
    """DeleteWordSamples response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteWorkflowRequest(AbstractModel):
    """DeleteWorkflow request structure.

    """

    def __init__(self):
        r"""
        :param WorkflowId: Workflow ID.
        :type WorkflowId: int
        """
        self.WorkflowId = None


    def _deserialize(self, params):
        self.WorkflowId = params.get("WorkflowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteWorkflowResponse(AbstractModel):
    """DeleteWorkflow response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAIAnalysisTemplatesRequest(AbstractModel):
    """DescribeAIAnalysisTemplates request structure.

    """

    def __init__(self):
        r"""
        :param Definitions: Unique ID filter of video content analysis templates. Array length limit: 10.
        :type Definitions: list of int
        :param Offset: Pagination offset. Default value: 0.
        :type Offset: int
        :param Limit: Number of returned entries. Default value: 10. Maximum value: 100.
        :type Limit: int
        :param Type: The filter for querying templates. If this parameter is left empty, both preset and custom templates are returned. Valid values:
* Preset
* Custom
        :type Type: str
        """
        self.Definitions = None
        self.Offset = None
        self.Limit = None
        self.Type = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAIAnalysisTemplatesResponse(AbstractModel):
    """DescribeAIAnalysisTemplates response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of eligible entries.
        :type TotalCount: int
        :param AIAnalysisTemplateSet: List of video content analysis template details.
        :type AIAnalysisTemplateSet: list of AIAnalysisTemplateItem
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.AIAnalysisTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AIAnalysisTemplateSet") is not None:
            self.AIAnalysisTemplateSet = []
            for item in params.get("AIAnalysisTemplateSet"):
                obj = AIAnalysisTemplateItem()
                obj._deserialize(item)
                self.AIAnalysisTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAIRecognitionTemplatesRequest(AbstractModel):
    """DescribeAIRecognitionTemplates request structure.

    """

    def __init__(self):
        r"""
        :param Definitions: Unique ID filter of video content recognition templates. Array length limit: 10.
        :type Definitions: list of int
        :param Offset: Paging offset. Default value: 0.
        :type Offset: int
        :param Limit: Number of returned entries. Default value: 10. Maximum value: 50.
        :type Limit: int
        :param Type: The filter for querying templates. If this parameter is left empty, both preset and custom templates are returned. Valid values:
* Preset
* Custom
        :type Type: str
        """
        self.Definitions = None
        self.Offset = None
        self.Limit = None
        self.Type = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAIRecognitionTemplatesResponse(AbstractModel):
    """DescribeAIRecognitionTemplates response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of eligible entries.
        :type TotalCount: int
        :param AIRecognitionTemplateSet: List of video content recognition template details.
        :type AIRecognitionTemplateSet: list of AIRecognitionTemplateItem
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.AIRecognitionTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AIRecognitionTemplateSet") is not None:
            self.AIRecognitionTemplateSet = []
            for item in params.get("AIRecognitionTemplateSet"):
                obj = AIRecognitionTemplateItem()
                obj._deserialize(item)
                self.AIRecognitionTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAdaptiveDynamicStreamingTemplatesRequest(AbstractModel):
    """DescribeAdaptiveDynamicStreamingTemplates request structure.

    """

    def __init__(self):
        r"""
        :param Definitions: Unique ID filter of adaptive bitrate streaming templates. Array length limit: 100.
        :type Definitions: list of int non-negative
        :param Offset: Pagination offset. Default value: 0.
        :type Offset: int
        :param Limit: Number of returned entries. Default value: 10. Maximum value: 100.
        :type Limit: int
        :param Type: Template type filter. Valid values:
<li>Preset: preset template;</li>
<li>Custom: custom template.</li>
        :type Type: str
        """
        self.Definitions = None
        self.Offset = None
        self.Limit = None
        self.Type = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAdaptiveDynamicStreamingTemplatesResponse(AbstractModel):
    """DescribeAdaptiveDynamicStreamingTemplates response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of eligible entries.
        :type TotalCount: int
        :param AdaptiveDynamicStreamingTemplateSet: List of adaptive bitrate streaming template details.
        :type AdaptiveDynamicStreamingTemplateSet: list of AdaptiveDynamicStreamingTemplate
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.AdaptiveDynamicStreamingTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AdaptiveDynamicStreamingTemplateSet") is not None:
            self.AdaptiveDynamicStreamingTemplateSet = []
            for item in params.get("AdaptiveDynamicStreamingTemplateSet"):
                obj = AdaptiveDynamicStreamingTemplate()
                obj._deserialize(item)
                self.AdaptiveDynamicStreamingTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAnimatedGraphicsTemplatesRequest(AbstractModel):
    """DescribeAnimatedGraphicsTemplates request structure.

    """

    def __init__(self):
        r"""
        :param Definitions: Unique ID filter of animated image generating templates. Array length limit: 100.
        :type Definitions: list of int non-negative
        :param Offset: Paging offset. Default value: 0.
        :type Offset: int
        :param Limit: Number of returned entries. Default value: 10. Maximum value: 100.
        :type Limit: int
        :param Type: Template type filter. Valid values:
<li>Preset: Preset template;</li>
<li>Custom: Custom template.</li>
        :type Type: str
        """
        self.Definitions = None
        self.Offset = None
        self.Limit = None
        self.Type = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAnimatedGraphicsTemplatesResponse(AbstractModel):
    """DescribeAnimatedGraphicsTemplates response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of eligible entries.
        :type TotalCount: int
        :param AnimatedGraphicsTemplateSet: List of animated image generating template details.
        :type AnimatedGraphicsTemplateSet: list of AnimatedGraphicsTemplate
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.AnimatedGraphicsTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AnimatedGraphicsTemplateSet") is not None:
            self.AnimatedGraphicsTemplateSet = []
            for item in params.get("AnimatedGraphicsTemplateSet"):
                obj = AnimatedGraphicsTemplate()
                obj._deserialize(item)
                self.AnimatedGraphicsTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeContentReviewTemplatesRequest(AbstractModel):
    """DescribeContentReviewTemplates request structure.

    """

    def __init__(self):
        r"""
        :param Definitions: Unique ID of intelligent content recognition templates as the filter. Array length limit: 50
        :type Definitions: list of int
        :param Offset: Paging offset. Default value: 0.
        :type Offset: int
        :param Limit: Number of returned entries. Default value: 10. Maximum value: 50.
        :type Limit: int
        :param Type: The filter for querying templates. If this parameter is left empty, both preset and custom templates are returned. Valid values:
* Preset
* Custom
        :type Type: str
        """
        self.Definitions = None
        self.Offset = None
        self.Limit = None
        self.Type = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeContentReviewTemplatesResponse(AbstractModel):
    """DescribeContentReviewTemplates response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of eligible entries.
        :type TotalCount: int
        :param ContentReviewTemplateSet: List of content audit template details.
        :type ContentReviewTemplateSet: list of ContentReviewTemplateItem
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.ContentReviewTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ContentReviewTemplateSet") is not None:
            self.ContentReviewTemplateSet = []
            for item in params.get("ContentReviewTemplateSet"):
                obj = ContentReviewTemplateItem()
                obj._deserialize(item)
                self.ContentReviewTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeImageSpriteTemplatesRequest(AbstractModel):
    """DescribeImageSpriteTemplates request structure.

    """

    def __init__(self):
        r"""
        :param Definitions: Unique ID filter of image sprite generating templates. Array length limit: 100.
        :type Definitions: list of int non-negative
        :param Offset: Paging offset. Default value: 0.
        :type Offset: int
        :param Limit: Number of returned entries. Default value: 10. Maximum value: 100.
        :type Limit: int
        :param Type: Template type filter. Valid values:
<li>Preset: Preset template;</li>
<li>Custom: Custom template.</li>
        :type Type: str
        """
        self.Definitions = None
        self.Offset = None
        self.Limit = None
        self.Type = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImageSpriteTemplatesResponse(AbstractModel):
    """DescribeImageSpriteTemplates response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of eligible entries.
        :type TotalCount: int
        :param ImageSpriteTemplateSet: List of image sprite generating template details.
        :type ImageSpriteTemplateSet: list of ImageSpriteTemplate
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.ImageSpriteTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ImageSpriteTemplateSet") is not None:
            self.ImageSpriteTemplateSet = []
            for item in params.get("ImageSpriteTemplateSet"):
                obj = ImageSpriteTemplate()
                obj._deserialize(item)
                self.ImageSpriteTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMediaMetaDataRequest(AbstractModel):
    """DescribeMediaMetaData request structure.

    """

    def __init__(self):
        r"""
        :param InputInfo: Input information of file for metadata getting.
        :type InputInfo: :class:`tencentcloud.mps.v20190612.models.MediaInputInfo`
        """
        self.InputInfo = None


    def _deserialize(self, params):
        if params.get("InputInfo") is not None:
            self.InputInfo = MediaInputInfo()
            self.InputInfo._deserialize(params.get("InputInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMediaMetaDataResponse(AbstractModel):
    """DescribeMediaMetaData response structure.

    """

    def __init__(self):
        r"""
        :param MetaData: Media metadata.
        :type MetaData: :class:`tencentcloud.mps.v20190612.models.MediaMetaData`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.MetaData = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MetaData") is not None:
            self.MetaData = MediaMetaData()
            self.MetaData._deserialize(params.get("MetaData"))
        self.RequestId = params.get("RequestId")


class DescribePersonSamplesRequest(AbstractModel):
    """DescribePersonSamples request structure.

    """

    def __init__(self):
        r"""
        :param Type: Type of images to pull. Valid values:
<li>UserDefine: custom image library</li>
<li>Default: default image library</li>

Default value: UserDefine. Samples in the custom image library will be pulled.
Note: you can pull the default image library only using the image name or a combination of the image name and ID, and only one face image is returned.
        :type Type: str
        :param PersonIds: Image ID. Array length limit: 100
        :type PersonIds: list of str
        :param Names: Image name. Array length limit: 20
        :type Names: list of str
        :param Tags: Image tag. Array length limit: 20
        :type Tags: list of str
        :param Offset: Paging offset. Default value: 0.
        :type Offset: int
        :param Limit: Number of returned entries. Default value: 100. Maximum value: 100.
        :type Limit: int
        """
        self.Type = None
        self.PersonIds = None
        self.Names = None
        self.Tags = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.PersonIds = params.get("PersonIds")
        self.Names = params.get("Names")
        self.Tags = params.get("Tags")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePersonSamplesResponse(AbstractModel):
    """DescribePersonSamples response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of eligible entries.
        :type TotalCount: int
        :param PersonSet: Image information
        :type PersonSet: list of AiSamplePerson
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.PersonSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("PersonSet") is not None:
            self.PersonSet = []
            for item in params.get("PersonSet"):
                obj = AiSamplePerson()
                obj._deserialize(item)
                self.PersonSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSampleSnapshotTemplatesRequest(AbstractModel):
    """DescribeSampleSnapshotTemplates request structure.

    """

    def __init__(self):
        r"""
        :param Definitions: Unique ID filter of sampled screencapturing templates. Array length limit: 100.
        :type Definitions: list of int non-negative
        :param Offset: Paging offset. Default value: 0.
        :type Offset: int
        :param Limit: Number of returned entries. Default value: 10. Maximum value: 100.
        :type Limit: int
        :param Type: Template type filter. Valid values:
<li>Preset: Preset template;</li>
<li>Custom: Custom template.</li>
        :type Type: str
        """
        self.Definitions = None
        self.Offset = None
        self.Limit = None
        self.Type = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSampleSnapshotTemplatesResponse(AbstractModel):
    """DescribeSampleSnapshotTemplates response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of eligible entries.
        :type TotalCount: int
        :param SampleSnapshotTemplateSet: List of sampled screencapturing template details.
        :type SampleSnapshotTemplateSet: list of SampleSnapshotTemplate
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.SampleSnapshotTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("SampleSnapshotTemplateSet") is not None:
            self.SampleSnapshotTemplateSet = []
            for item in params.get("SampleSnapshotTemplateSet"):
                obj = SampleSnapshotTemplate()
                obj._deserialize(item)
                self.SampleSnapshotTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSnapshotByTimeOffsetTemplatesRequest(AbstractModel):
    """DescribeSnapshotByTimeOffsetTemplates request structure.

    """

    def __init__(self):
        r"""
        :param Definitions: Unique ID filter of time point screencapturing templates. Array length limit: 100.
        :type Definitions: list of int non-negative
        :param Offset: Paging offset. Default value: 0.
        :type Offset: int
        :param Limit: Number of returned entries. Default value: 10. Maximum value: 100.
        :type Limit: int
        :param Type: Template type filter. Valid values:
<li>Preset: Preset template;</li>
<li>Custom: Custom template.</li>
        :type Type: str
        """
        self.Definitions = None
        self.Offset = None
        self.Limit = None
        self.Type = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSnapshotByTimeOffsetTemplatesResponse(AbstractModel):
    """DescribeSnapshotByTimeOffsetTemplates response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of eligible entries.
        :type TotalCount: int
        :param SnapshotByTimeOffsetTemplateSet: List of time point screencapturing template details.
        :type SnapshotByTimeOffsetTemplateSet: list of SnapshotByTimeOffsetTemplate
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.SnapshotByTimeOffsetTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("SnapshotByTimeOffsetTemplateSet") is not None:
            self.SnapshotByTimeOffsetTemplateSet = []
            for item in params.get("SnapshotByTimeOffsetTemplateSet"):
                obj = SnapshotByTimeOffsetTemplate()
                obj._deserialize(item)
                self.SnapshotByTimeOffsetTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTaskDetailRequest(AbstractModel):
    """DescribeTaskDetail request structure.

    """

    def __init__(self):
        r"""
        :param TaskId: Video processing task ID.
        :type TaskId: str
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskDetailResponse(AbstractModel):
    """DescribeTaskDetail response structure.

    """

    def __init__(self):
        r"""
        :param TaskType: Task type. Currently valid values:
<li>WorkflowTask: Video workflow processing task.</li>
<li>LiveStreamProcessTask: Live stream processing task.</li>
        :type TaskType: str
        :param Status: Task status. Valid values:
<li>WAITING: Waiting;</li>
<li>PROCESSING: Processing;</li>
<li>FINISH: Completed.</li>
        :type Status: str
        :param CreateTime: Creation time of a task in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F).
        :type CreateTime: str
        :param BeginProcessTime: Start time of task execution in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F).
        :type BeginProcessTime: str
        :param FinishTime: End time of task execution in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F).
        :type FinishTime: str
        :param WorkflowTask: Information of a video processing task. This field has a value only when `TaskType` is `WorkflowTask`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type WorkflowTask: :class:`tencentcloud.mps.v20190612.models.WorkflowTask`
        :param EditMediaTask: Video editing task information. This field has a value only when `TaskType` is `EditMediaTask`.
        :type EditMediaTask: :class:`tencentcloud.mps.v20190612.models.EditMediaTask`
        :param LiveStreamProcessTask: Information of a live stream processing task. This field has a value only when `TaskType` is `LiveStreamProcessTask`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LiveStreamProcessTask: :class:`tencentcloud.mps.v20190612.models.LiveStreamProcessTask`
        :param TaskNotifyConfig: Event notification information of a task.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskNotifyConfig: :class:`tencentcloud.mps.v20190612.models.TaskNotifyConfig`
        :param TasksPriority: Task flow priority. Value range: [-10, 10].
        :type TasksPriority: int
        :param SessionId: The ID used for deduplication. If there was a request with the same ID in the last seven days, the current request will return an error. The ID can contain up to 50 characters. If this parameter is left empty or an empty string is entered, no deduplication will be performed.
        :type SessionId: str
        :param SessionContext: The source context which is used to pass through the user request information. The task flow status change callback will return the value of this field. It can contain up to 1,000 characters.
        :type SessionContext: str
        :param ExtInfo: Extended information field, used in specific scenarios.
        :type ExtInfo: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskType = None
        self.Status = None
        self.CreateTime = None
        self.BeginProcessTime = None
        self.FinishTime = None
        self.WorkflowTask = None
        self.EditMediaTask = None
        self.LiveStreamProcessTask = None
        self.TaskNotifyConfig = None
        self.TasksPriority = None
        self.SessionId = None
        self.SessionContext = None
        self.ExtInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskType = params.get("TaskType")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.BeginProcessTime = params.get("BeginProcessTime")
        self.FinishTime = params.get("FinishTime")
        if params.get("WorkflowTask") is not None:
            self.WorkflowTask = WorkflowTask()
            self.WorkflowTask._deserialize(params.get("WorkflowTask"))
        if params.get("EditMediaTask") is not None:
            self.EditMediaTask = EditMediaTask()
            self.EditMediaTask._deserialize(params.get("EditMediaTask"))
        if params.get("LiveStreamProcessTask") is not None:
            self.LiveStreamProcessTask = LiveStreamProcessTask()
            self.LiveStreamProcessTask._deserialize(params.get("LiveStreamProcessTask"))
        if params.get("TaskNotifyConfig") is not None:
            self.TaskNotifyConfig = TaskNotifyConfig()
            self.TaskNotifyConfig._deserialize(params.get("TaskNotifyConfig"))
        self.TasksPriority = params.get("TasksPriority")
        self.SessionId = params.get("SessionId")
        self.SessionContext = params.get("SessionContext")
        self.ExtInfo = params.get("ExtInfo")
        self.RequestId = params.get("RequestId")


class DescribeTasksRequest(AbstractModel):
    """DescribeTasks request structure.

    """

    def __init__(self):
        r"""
        :param Status: Filter: Task status. Valid values: WAITING (waiting), PROCESSING (processing), FINISH (completed).
        :type Status: str
        :param Limit: Number of returned entries. Default value: 10. Maximum value: 100.
        :type Limit: int
        :param ScrollToken: Scrolling identifier which is used for pulling in batches. If a single request cannot pull all the data entries, the API will return `ScrollToken`, and if the next request carries it, the next pull will start from the next entry.
        :type ScrollToken: str
        """
        self.Status = None
        self.Limit = None
        self.ScrollToken = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Limit = params.get("Limit")
        self.ScrollToken = params.get("ScrollToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTasksResponse(AbstractModel):
    """DescribeTasks response structure.

    """

    def __init__(self):
        r"""
        :param TaskSet: Task overview list.
        :type TaskSet: list of TaskSimpleInfo
        :param ScrollToken: Scrolling identifier. If a request does not return all the data entries, this field indicates the ID of the next entry. If this field is an empty string, there is no more data.
        :type ScrollToken: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskSet = None
        self.ScrollToken = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TaskSet") is not None:
            self.TaskSet = []
            for item in params.get("TaskSet"):
                obj = TaskSimpleInfo()
                obj._deserialize(item)
                self.TaskSet.append(obj)
        self.ScrollToken = params.get("ScrollToken")
        self.RequestId = params.get("RequestId")


class DescribeTranscodeTemplatesRequest(AbstractModel):
    """DescribeTranscodeTemplates request structure.

    """

    def __init__(self):
        r"""
        :param Definitions: Unique ID filter of transcoding templates. Array length limit: 100.
        :type Definitions: list of int
        :param Type: Template type filter. Valid values:
<li>Preset: Preset template;</li>
<li>Custom: Custom template.</li>
        :type Type: str
        :param ContainerType: Container format filter. Valid values:
<li>Video: Video container format that can contain both video stream and audio stream;</li>
<li>PureAudio: Audio container format that can contain only audio stream.</li>
        :type ContainerType: str
        :param TEHDType: TESHD filter, which is used to filter common transcoding or ultra-fast HD transcoding templates. Valid values:
<li>Common: Common transcoding template;</li>
<li>TEHD: TESHD template.</li>
        :type TEHDType: str
        :param Offset: Paging offset. Default value: 0.
        :type Offset: int
        :param Limit: Number of returned entries. Default value: 10. Maximum value: 100.
        :type Limit: int
        """
        self.Definitions = None
        self.Type = None
        self.ContainerType = None
        self.TEHDType = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Type = params.get("Type")
        self.ContainerType = params.get("ContainerType")
        self.TEHDType = params.get("TEHDType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTranscodeTemplatesResponse(AbstractModel):
    """DescribeTranscodeTemplates response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of eligible entries.
        :type TotalCount: int
        :param TranscodeTemplateSet: List of transcoding template details.
        :type TranscodeTemplateSet: list of TranscodeTemplate
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.TranscodeTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TranscodeTemplateSet") is not None:
            self.TranscodeTemplateSet = []
            for item in params.get("TranscodeTemplateSet"):
                obj = TranscodeTemplate()
                obj._deserialize(item)
                self.TranscodeTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeWatermarkTemplatesRequest(AbstractModel):
    """DescribeWatermarkTemplates request structure.

    """

    def __init__(self):
        r"""
        :param Definitions: Unique ID filter of watermarking templates. Array length limit: 100.
        :type Definitions: list of int
        :param Type: Watermark type filter. Valid values:
<li>image: Image watermark;</li>
<li>text: Text watermark.</li>
        :type Type: str
        :param Offset: Paging offset. Default value: 0.
        :type Offset: int
        :param Limit: Number of returned entries
<li>Default value: 10;</li>
<li>Maximum value: 100.</li>
        :type Limit: int
        """
        self.Definitions = None
        self.Type = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Type = params.get("Type")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWatermarkTemplatesResponse(AbstractModel):
    """DescribeWatermarkTemplates response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of eligible entries.
        :type TotalCount: int
        :param WatermarkTemplateSet: List of watermarking template details.
        :type WatermarkTemplateSet: list of WatermarkTemplate
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.WatermarkTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("WatermarkTemplateSet") is not None:
            self.WatermarkTemplateSet = []
            for item in params.get("WatermarkTemplateSet"):
                obj = WatermarkTemplate()
                obj._deserialize(item)
                self.WatermarkTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeWordSamplesRequest(AbstractModel):
    """DescribeWordSamples request structure.

    """

    def __init__(self):
        r"""
        :param Keywords: Keyword filter. Array length limit: 100 words.
        :type Keywords: list of str
        :param Usages: <b>Keyword usage. Valid values:</b>
1. Recognition.Ocr: OCR-based content recognition
2. Recognition.Asr: ASR-based content recognition
3. Review.Ocr: OCR-based inappropriate information recognition
4. Review.Asr: ASR-based inappropriate information recognition
<b>Valid values can also be:</b>
5. Recognition: ASR- and OCR-based content recognition; equivalent to 1+2
6. Review: ASR- and OCR-based inappropriate information recognition; equivalent to 3+4
You can select multiple elements, which are connected by OR logic. If a usage contains any element in this parameter, the keyword sample will be used.
        :type Usages: list of str
        :param Tags: Tag filter. Array length limit: 20 words.
        :type Tags: list of str
        :param Offset: Paging offset. Default value: 0.
        :type Offset: int
        :param Limit: Number of returned entries. Default value: 100. Maximum value: 100.
        :type Limit: int
        """
        self.Keywords = None
        self.Usages = None
        self.Tags = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Keywords = params.get("Keywords")
        self.Usages = params.get("Usages")
        self.Tags = params.get("Tags")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWordSamplesResponse(AbstractModel):
    """DescribeWordSamples response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of eligible entries.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param WordSet: Keyword information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type WordSet: list of AiSampleWord
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.WordSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("WordSet") is not None:
            self.WordSet = []
            for item in params.get("WordSet"):
                obj = AiSampleWord()
                obj._deserialize(item)
                self.WordSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeWorkflowsRequest(AbstractModel):
    """DescribeWorkflows request structure.

    """

    def __init__(self):
        r"""
        :param WorkflowIds: Workflow ID filter. Array length limit: 100.
        :type WorkflowIds: list of int
        :param Status: Workflow status. Valid values:
<li>Enabled: Enabled,</li>
<li>Disabled: Disabled.</li>
If this parameter is left empty, the workflow status will not be distinguished.
        :type Status: str
        :param Offset: Paging offset. Default value: 0.
        :type Offset: int
        :param Limit: Number of returned entries. Default value: 10. Maximum value: 100.
        :type Limit: int
        """
        self.WorkflowIds = None
        self.Status = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.WorkflowIds = params.get("WorkflowIds")
        self.Status = params.get("Status")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWorkflowsResponse(AbstractModel):
    """DescribeWorkflows response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of eligible entries.
        :type TotalCount: int
        :param WorkflowInfoSet: Workflow information array.
        :type WorkflowInfoSet: list of WorkflowInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.WorkflowInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("WorkflowInfoSet") is not None:
            self.WorkflowInfoSet = []
            for item in params.get("WorkflowInfoSet"):
                obj = WorkflowInfo()
                obj._deserialize(item)
                self.WorkflowInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DisableWorkflowRequest(AbstractModel):
    """DisableWorkflow request structure.

    """

    def __init__(self):
        r"""
        :param WorkflowId: Workflow ID.
        :type WorkflowId: int
        """
        self.WorkflowId = None


    def _deserialize(self, params):
        self.WorkflowId = params.get("WorkflowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableWorkflowResponse(AbstractModel):
    """DisableWorkflow response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EditMediaFileInfo(AbstractModel):
    """VOD video file editing information

    """

    def __init__(self):
        r"""
        :param InputInfo: Video input information.
        :type InputInfo: :class:`tencentcloud.mps.v20190612.models.MediaInputInfo`
        :param StartTimeOffset: Start time offset of video clipping in seconds.
        :type StartTimeOffset: float
        :param EndTimeOffset: End time offset of video clipping in seconds.
        :type EndTimeOffset: float
        """
        self.InputInfo = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None


    def _deserialize(self, params):
        if params.get("InputInfo") is not None:
            self.InputInfo = MediaInputInfo()
            self.InputInfo._deserialize(params.get("InputInfo"))
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EditMediaOutputConfig(AbstractModel):
    """Configuration for output files of video editing

    """

    def __init__(self):
        r"""
        :param Container: Format. Valid values: `mp4` (default), `hls`, `mov`, `flv`, `avi`
        :type Container: str
        """
        self.Container = None


    def _deserialize(self, params):
        self.Container = params.get("Container")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EditMediaRequest(AbstractModel):
    """EditMedia request structure.

    """

    def __init__(self):
        r"""
        :param FileInfos: Information of input video file.
        :type FileInfos: list of EditMediaFileInfo
        :param OutputStorage: Target storage of video processing output file.
        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        :param OutputObjectPath: Target path of video processing output file.
        :type OutputObjectPath: str
        :param OutputConfig: Configuration for output files of video editing
        :type OutputConfig: :class:`tencentcloud.mps.v20190612.models.EditMediaOutputConfig`
        :param TaskNotifyConfig: Event notification information of task. If this parameter is left empty, no event notifications will be obtained.
        :type TaskNotifyConfig: :class:`tencentcloud.mps.v20190612.models.TaskNotifyConfig`
        :param TasksPriority: Task priority. The higher the value, the higher the priority. Value range: -10–10. If this parameter is left empty, 0 will be used.
        :type TasksPriority: int
        :param SessionId: The ID used for deduplication. If there was a request with the same ID in the last three days, the current request will return an error. The ID can contain up to 50 characters. If this parameter is left empty or an empty string is entered, no deduplication will be performed.
        :type SessionId: str
        :param SessionContext: The source context which is used to pass through the user request information. The task flow status change callback will return the value of this field. It can contain up to 1,000 characters.
        :type SessionContext: str
        """
        self.FileInfos = None
        self.OutputStorage = None
        self.OutputObjectPath = None
        self.OutputConfig = None
        self.TaskNotifyConfig = None
        self.TasksPriority = None
        self.SessionId = None
        self.SessionContext = None


    def _deserialize(self, params):
        if params.get("FileInfos") is not None:
            self.FileInfos = []
            for item in params.get("FileInfos"):
                obj = EditMediaFileInfo()
                obj._deserialize(item)
                self.FileInfos.append(obj)
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.OutputObjectPath = params.get("OutputObjectPath")
        if params.get("OutputConfig") is not None:
            self.OutputConfig = EditMediaOutputConfig()
            self.OutputConfig._deserialize(params.get("OutputConfig"))
        if params.get("TaskNotifyConfig") is not None:
            self.TaskNotifyConfig = TaskNotifyConfig()
            self.TaskNotifyConfig._deserialize(params.get("TaskNotifyConfig"))
        self.TasksPriority = params.get("TasksPriority")
        self.SessionId = params.get("SessionId")
        self.SessionContext = params.get("SessionContext")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EditMediaResponse(AbstractModel):
    """EditMedia response structure.

    """

    def __init__(self):
        r"""
        :param TaskId: Video editing task ID, which can be used to query the status of an editing task.
        :type TaskId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class EditMediaTask(AbstractModel):
    """Video editing task information

    """

    def __init__(self):
        r"""
        :param TaskId: Task ID.
        :type TaskId: str
        :param Status: Task status. Valid values:
<li>PROCESSING: processing;</li>
<li>FINISH: completed.</li>
        :type Status: str
        :param ErrCode: Error code
<li>0: success;</li>
<li>Other values: failure.</li>
        :type ErrCode: int
        :param Message: Error message.
        :type Message: str
        :param Input: Input of video editing task.
        :type Input: :class:`tencentcloud.mps.v20190612.models.EditMediaTaskInput`
        :param Output: Output of video editing task.
        :type Output: :class:`tencentcloud.mps.v20190612.models.EditMediaTaskOutput`
        """
        self.TaskId = None
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = EditMediaTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = EditMediaTaskOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EditMediaTaskInput(AbstractModel):
    """Input of video editing task.

    """

    def __init__(self):
        r"""
        :param FileInfoSet: Information of input video file.
        :type FileInfoSet: list of EditMediaFileInfo
        """
        self.FileInfoSet = None


    def _deserialize(self, params):
        if params.get("FileInfoSet") is not None:
            self.FileInfoSet = []
            for item in params.get("FileInfoSet"):
                obj = EditMediaFileInfo()
                obj._deserialize(item)
                self.FileInfoSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EditMediaTaskOutput(AbstractModel):
    """Output of video editing task

    """

    def __init__(self):
        r"""
        :param OutputStorage: Target storage of edited file.
        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        :param Path: Path of edited video file.
        :type Path: str
        """
        self.OutputStorage = None
        self.Path = None


    def _deserialize(self, params):
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.Path = params.get("Path")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableWorkflowRequest(AbstractModel):
    """EnableWorkflow request structure.

    """

    def __init__(self):
        r"""
        :param WorkflowId: Workflow ID.
        :type WorkflowId: int
        """
        self.WorkflowId = None


    def _deserialize(self, params):
        self.WorkflowId = params.get("WorkflowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableWorkflowResponse(AbstractModel):
    """EnableWorkflow response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ExecuteFunctionRequest(AbstractModel):
    """ExecuteFunction request structure.

    """

    def __init__(self):
        r"""
        :param FunctionName: Name of called backend API.
        :type FunctionName: str
        :param FunctionArg: API parameter. Parameter format will depend on the actual function definition.
        :type FunctionArg: str
        """
        self.FunctionName = None
        self.FunctionArg = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.FunctionArg = params.get("FunctionArg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExecuteFunctionResponse(AbstractModel):
    """ExecuteFunction response structure.

    """

    def __init__(self):
        r"""
        :param Result: Packed string, which will vary according to the custom API.
        :type Result: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class FaceConfigureInfo(AbstractModel):
    """Control parameter of a face recognition task

    """

    def __init__(self):
        r"""
        :param Switch: Switch of a face recognition task. Valid values:
<li>ON: Enables an intelligent face recognition task;</li>
<li>OFF: Disables an intelligent face recognition task.</li>
        :type Switch: str
        :param Score: Face recognition filter score. If this score is reached or exceeded, a recognition result will be returned. Value range: 0-100. Default value: 95.
        :type Score: float
        :param DefaultLibraryLabelSet: The default face filter labels, which specify the types of faces to return. If this parameter is left empty, the detection results for all labels are returned. Valid values:
<li>entertainment (people in the entertainment industry)</li>
<li>sport (sports celebrities)</li>
<li>politician</li>
        :type DefaultLibraryLabelSet: list of str
        :param UserDefineLibraryLabelSet: Custom face tags for filter, which specify the face recognition results to return. If this parameter is not specified or left empty, the recognition results for all custom face tags are returned.
Up to 100 tags are allowed, each containing no more than 16 characters.
        :type UserDefineLibraryLabelSet: list of str
        :param FaceLibrary: Figure library. Valid values:
<li>Default: Default figure library;</li>
<li>UserDefine: Custom figure library.</li>
<li>All: Both default and custom figure libraries will be used.</li>
Default value: All (both default and custom figure libraries will be used.)
        :type FaceLibrary: str
        """
        self.Switch = None
        self.Score = None
        self.DefaultLibraryLabelSet = None
        self.UserDefineLibraryLabelSet = None
        self.FaceLibrary = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Score = params.get("Score")
        self.DefaultLibraryLabelSet = params.get("DefaultLibraryLabelSet")
        self.UserDefineLibraryLabelSet = params.get("UserDefineLibraryLabelSet")
        self.FaceLibrary = params.get("FaceLibrary")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FaceConfigureInfoForUpdate(AbstractModel):
    """Control parameter of a face recognition task

    """

    def __init__(self):
        r"""
        :param Switch: Switch of a face recognition task. Valid values:
<li>ON: Enables an intelligent face recognition task;</li>
<li>OFF: Disables an intelligent face recognition task.</li>
        :type Switch: str
        :param Score: Face recognition filter score. If this score is reached or exceeded, a recognition result will be returned. Value range: 0-100.
        :type Score: float
        :param DefaultLibraryLabelSet: The default face filter labels, which specify the types of faces to return. If this parameter is left empty, the detection results for all labels are returned. Valid values:
<li>entertainment (people in the entertainment industry)</li>
<li>sport (sports celebrities)</li>
<li>politician</li>
        :type DefaultLibraryLabelSet: list of str
        :param UserDefineLibraryLabelSet: Custom face tags for filter, which specify the face recognition results to return. If this parameter is not specified or left empty, the recognition results for all custom face tags are returned.
Up to 100 tags are allowed, each containing no more than 16 characters.
        :type UserDefineLibraryLabelSet: list of str
        :param FaceLibrary: Figure library. Valid values:
<li>Default: Default figure library;</li>
<li>UserDefine: Custom figure library.</li>
<li>All: Both default and custom figure libraries will be used.</li>
        :type FaceLibrary: str
        """
        self.Switch = None
        self.Score = None
        self.DefaultLibraryLabelSet = None
        self.UserDefineLibraryLabelSet = None
        self.FaceLibrary = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Score = params.get("Score")
        self.DefaultLibraryLabelSet = params.get("DefaultLibraryLabelSet")
        self.UserDefineLibraryLabelSet = params.get("UserDefineLibraryLabelSet")
        self.FaceLibrary = params.get("FaceLibrary")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FrameTagConfigureInfo(AbstractModel):
    """Control parameter of intelligent frame-specific tagging task

    """

    def __init__(self):
        r"""
        :param Switch: Switch of intelligent frame-specific tagging task. Valid values:
<li>ON: enables intelligent frame-specific tagging task;</li>
<li>OFF: disables intelligent frame-specific tagging task.</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FrameTagConfigureInfoForUpdate(AbstractModel):
    """Control parameter of intelligent frame-specific tagging task

    """

    def __init__(self):
        r"""
        :param Switch: Switch of intelligent frame-specific tagging task. Valid values:
<li>ON: enables intelligent frame-specific tagging task;</li>
<li>OFF: disables intelligent frame-specific tagging task.</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HeadTailParameter(AbstractModel):
    """Opening and closing credits parameters

    """

    def __init__(self):
        r"""
        :param HeadSet: Opening credits list
        :type HeadSet: list of MediaInputInfo
        :param TailSet: Closing credits list
        :type TailSet: list of MediaInputInfo
        """
        self.HeadSet = None
        self.TailSet = None


    def _deserialize(self, params):
        if params.get("HeadSet") is not None:
            self.HeadSet = []
            for item in params.get("HeadSet"):
                obj = MediaInputInfo()
                obj._deserialize(item)
                self.HeadSet.append(obj)
        if params.get("TailSet") is not None:
            self.TailSet = []
            for item in params.get("TailSet"):
                obj = MediaInputInfo()
                obj._deserialize(item)
                self.TailSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageSpriteTaskInput(AbstractModel):
    """Input parameter type of an image sprite generating task

    """

    def __init__(self):
        r"""
        :param Definition: ID of an image sprite generating template.
        :type Definition: int
        :param OutputStorage: Target bucket of a generated image sprite. If this parameter is left empty, the `OutputStorage` value of the upper folder will be inherited.
Note: This field may return null, indicating that no valid values can be obtained.
        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        :param OutputObjectPath: Output path to a generated image sprite file, which can be a relative path or an absolute path. If this parameter is left empty, the following relative path will be used by default: `{inputName}_imageSprite_{definition}_{number}.{format}`.
        :type OutputObjectPath: str
        :param WebVttObjectName: Output path to the WebVTT file after an image sprite is generated, which can only be a relative path. If this parameter is left empty, the following relative path will be used by default: `{inputName}_imageSprite_{definition}.{format}`.
        :type WebVttObjectName: str
        :param ObjectNumberFormat: Rule of the `{number}` variable in the image sprite output path.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ObjectNumberFormat: :class:`tencentcloud.mps.v20190612.models.NumberFormat`
        """
        self.Definition = None
        self.OutputStorage = None
        self.OutputObjectPath = None
        self.WebVttObjectName = None
        self.ObjectNumberFormat = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.OutputObjectPath = params.get("OutputObjectPath")
        self.WebVttObjectName = params.get("WebVttObjectName")
        if params.get("ObjectNumberFormat") is not None:
            self.ObjectNumberFormat = NumberFormat()
            self.ObjectNumberFormat._deserialize(params.get("ObjectNumberFormat"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageSpriteTemplate(AbstractModel):
    """Details of an image sprite generating template

    """

    def __init__(self):
        r"""
        :param Definition: Unique ID of an image sprite generating template.
        :type Definition: int
        :param Type: Template type. Valid values:
<li>Preset: Preset template;</li>
<li>Custom: Custom template.</li>
        :type Type: str
        :param Name: Name of an image sprite generating template.
        :type Name: str
        :param Width: Subimage width of an image sprite.
        :type Width: int
        :param Height: Subimage height of an image sprite.
        :type Height: int
        :param ResolutionAdaptive: Resolution adaption. Valid values:
<li>open: enabled. In this case, `Width` represents the long side of a video, while `Height` the short side;</li>
<li>close: disabled. In this case, `Width` represents the width of a video, while `Height` the height.</li>
Default value: open.
        :type ResolutionAdaptive: str
        :param SampleType: Sampling type.
        :type SampleType: str
        :param SampleInterval: Sampling interval.
        :type SampleInterval: int
        :param RowCount: Subimage row count of an image sprite.
        :type RowCount: int
        :param ColumnCount: Subimage column count of an image sprite.
        :type ColumnCount: int
        :param CreateTime: Creation time of a template in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F).
        :type CreateTime: str
        :param UpdateTime: Last modified time of a template in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F).
        :type UpdateTime: str
        :param FillType: Fill type. "Fill" refers to the way of processing a screenshot when its aspect ratio is different from that of the source video. The following fill types are supported:
<li> stretch: Stretch. The screenshot will be stretched frame by frame to match the aspect ratio of the source video, which may make the screenshot "shorter" or "longer";</li>
<li>black: Fill with black. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with black color blocks.</li>
Default value: black.
        :type FillType: str
        :param Comment: Template description.
        :type Comment: str
        """
        self.Definition = None
        self.Type = None
        self.Name = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.SampleType = None
        self.SampleInterval = None
        self.RowCount = None
        self.ColumnCount = None
        self.CreateTime = None
        self.UpdateTime = None
        self.FillType = None
        self.Comment = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.SampleType = params.get("SampleType")
        self.SampleInterval = params.get("SampleInterval")
        self.RowCount = params.get("RowCount")
        self.ColumnCount = params.get("ColumnCount")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.FillType = params.get("FillType")
        self.Comment = params.get("Comment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageWatermarkInput(AbstractModel):
    """Input parameter of an image watermarking template

    """

    def __init__(self):
        r"""
        :param ImageContent: String generated by [Base64-encoding](https://tools.ietf.org/html/rfc4648) a watermark image. JPEG and PNG images are supported.
        :type ImageContent: str
        :param Width: Watermark width. % and px formats are supported:
<li>If the string ends in %, the `Width` of the watermark will be the specified percentage of the video width. For example, `10%` means that `Width` is 10% of the video width;</li>
<li>If the string ends in px, the `Width` of the watermark will be in pixels. For example, `100px` means that `Width` is 100 pixels. Value range: [8, 4096].</li>
Default value: 10%.
        :type Width: str
        :param Height: Watermark height. % and px formats are supported:
<li>If the string ends in %, the `Height` of the watermark will be the specified percentage of the video height. For example, `10%` means that `Height` is 10% of the video height;</li>
<li>If the string ends in px, the `Height` of the watermark will be in pixels. For example, `100px` means that `Height` is 100 pixels. Value range: 0 or [8, 4096].</li>
Default value: 0px, which means that `Height` will be proportionally scaled according to the aspect ratio of the original watermark image.
        :type Height: str
        :param RepeatType: Repeat type of an animated watermark. Valid values:
<li>once: no longer appears after watermark playback ends.</li>
<li>repeat_last_frame: stays on the last frame after watermark playback ends.</li>
<li>repeat (default): repeats the playback until the video ends.</li>
        :type RepeatType: str
        """
        self.ImageContent = None
        self.Width = None
        self.Height = None
        self.RepeatType = None


    def _deserialize(self, params):
        self.ImageContent = params.get("ImageContent")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.RepeatType = params.get("RepeatType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageWatermarkInputForUpdate(AbstractModel):
    """Input parameter of an image watermarking template

    """

    def __init__(self):
        r"""
        :param ImageContent: String generated by [Base64-encoding](https://tools.ietf.org/html/rfc4648) a watermark image. JPEG and PNG images are supported.
        :type ImageContent: str
        :param Width: Watermark width. % and px formats are supported:
<li>If the string ends in %, the `Width` of the watermark will be the specified percentage of the video width. For example, `10%` means that `Width` is 10% of the video width;</li>
<li>If the string ends in px, the `Width` of the watermark will be in pixels. For example, `100px` means that `Width` is 100 pixels. Value range: [8, 4096].</li>
        :type Width: str
        :param Height: Watermark height. % and px formats are supported:
<li>If the string ends in %, the `Height` of the watermark will be the specified percentage of the video height. For example, `10%` means that `Height` is 10% of the video height;</li>
<li>If the string ends in px, the `Height` of the watermark will be in pixels. For example, `100px` means that `Height` is 100 pixels. Value range: 0 or [8, 4096].</li>
Default value: 0px, which means that `Height` will be proportionally scaled according to the aspect ratio of the original watermark image.
        :type Height: str
        :param RepeatType: Repeat type of an animated watermark. Valid values:
<li>once: no longer appears after watermark playback ends.</li>
<li>repeat_last_frame: stays on the last frame after watermark playback ends.</li>
<li>repeat (default): repeats the playback until the video ends.</li>
        :type RepeatType: str
        """
        self.ImageContent = None
        self.Width = None
        self.Height = None
        self.RepeatType = None


    def _deserialize(self, params):
        self.ImageContent = params.get("ImageContent")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.RepeatType = params.get("RepeatType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageWatermarkTemplate(AbstractModel):
    """Image watermarking template

    """

    def __init__(self):
        r"""
        :param ImageUrl: Watermark image address.
        :type ImageUrl: str
        :param Width: Watermark width. % and px formats are supported:
<li>If the string ends in %, the `Width` of the watermark will be the specified percentage of the video width; for example, `10%` means that `Width` is 10% of the video width;</li>
<li>If the string ends in px, the `Width` of the watermark will be in px; for example, `100px` means that `Width` is 100 px.</li>
        :type Width: str
        :param Height: Watermark height. % and px formats are supported:
<li>If the string ends in %, the `Height` of the watermark will be the specified percentage of the video height. For example, `10%` means that `Height` is 10% of the video height;</li>
<li>If the string ends in px, the `Height` of the watermark will be in pixels. For example, `100px` means that `Height` is 100 pixels.</li>
`0px` means that `Height` will be proportionally scaled according to the video width.
        :type Height: str
        :param RepeatType: Repeat type of an animated watermark. Valid values:
<li>once: no longer appears after watermark playback ends.</li>
<li>repeat_last_frame: stays on the last frame after watermark playback ends.</li>
<li>repeat (default): repeats the playback until the video ends.</li>
        :type RepeatType: str
        """
        self.ImageUrl = None
        self.Width = None
        self.Height = None
        self.RepeatType = None


    def _deserialize(self, params):
        self.ImageUrl = params.get("ImageUrl")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.RepeatType = params.get("RepeatType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveStreamAiRecognitionResultInfo(AbstractModel):
    """Live stream AI recognition results

    """

    def __init__(self):
        r"""
        :param ResultSet: Content recognition result list.
        :type ResultSet: list of LiveStreamAiRecognitionResultItem
        """
        self.ResultSet = None


    def _deserialize(self, params):
        if params.get("ResultSet") is not None:
            self.ResultSet = []
            for item in params.get("ResultSet"):
                obj = LiveStreamAiRecognitionResultItem()
                obj._deserialize(item)
                self.ResultSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveStreamAiRecognitionResultItem(AbstractModel):
    """AI-based live stream recognition result

    """

    def __init__(self):
        r"""
        :param Type: Result type. Valid values:
<li>FaceRecognition: face recognition,</li>
<li>AsrWordsRecognition: speech keyword recognition,</li>
<li>OcrWordsRecognition: text keyword recognition,</li>
<li>AsrFullTextRecognition: full speech recognition,</li>
<li>OcrFullTextRecognition: full text recognition.</li>
        :type Type: str
        :param FaceRecognitionResultSet: Face recognition result, which is valid when `Type` is
`FaceRecognition`.
        :type FaceRecognitionResultSet: list of LiveStreamFaceRecognitionResult
        :param AsrWordsRecognitionResultSet: Speech keyword recognition result, which is valid when `Type` is
`AsrWordsRecognition`.
        :type AsrWordsRecognitionResultSet: list of LiveStreamAsrWordsRecognitionResult
        :param OcrWordsRecognitionResultSet: Text keyword recognition result, which is valid when `Type` is
`OcrWordsRecognition`.
        :type OcrWordsRecognitionResultSet: list of LiveStreamOcrWordsRecognitionResult
        :param AsrFullTextRecognitionResultSet: Full speech recognition result, which is valid when `Type` is
`AsrFullTextRecognition`.
        :type AsrFullTextRecognitionResultSet: list of LiveStreamAsrFullTextRecognitionResult
        :param OcrFullTextRecognitionResultSet: Full text recognition result, which is valid when `Type` is
`OcrFullTextRecognition`.
        :type OcrFullTextRecognitionResultSet: list of LiveStreamOcrFullTextRecognitionResult
        """
        self.Type = None
        self.FaceRecognitionResultSet = None
        self.AsrWordsRecognitionResultSet = None
        self.OcrWordsRecognitionResultSet = None
        self.AsrFullTextRecognitionResultSet = None
        self.OcrFullTextRecognitionResultSet = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("FaceRecognitionResultSet") is not None:
            self.FaceRecognitionResultSet = []
            for item in params.get("FaceRecognitionResultSet"):
                obj = LiveStreamFaceRecognitionResult()
                obj._deserialize(item)
                self.FaceRecognitionResultSet.append(obj)
        if params.get("AsrWordsRecognitionResultSet") is not None:
            self.AsrWordsRecognitionResultSet = []
            for item in params.get("AsrWordsRecognitionResultSet"):
                obj = LiveStreamAsrWordsRecognitionResult()
                obj._deserialize(item)
                self.AsrWordsRecognitionResultSet.append(obj)
        if params.get("OcrWordsRecognitionResultSet") is not None:
            self.OcrWordsRecognitionResultSet = []
            for item in params.get("OcrWordsRecognitionResultSet"):
                obj = LiveStreamOcrWordsRecognitionResult()
                obj._deserialize(item)
                self.OcrWordsRecognitionResultSet.append(obj)
        if params.get("AsrFullTextRecognitionResultSet") is not None:
            self.AsrFullTextRecognitionResultSet = []
            for item in params.get("AsrFullTextRecognitionResultSet"):
                obj = LiveStreamAsrFullTextRecognitionResult()
                obj._deserialize(item)
                self.AsrFullTextRecognitionResultSet.append(obj)
        if params.get("OcrFullTextRecognitionResultSet") is not None:
            self.OcrFullTextRecognitionResultSet = []
            for item in params.get("OcrFullTextRecognitionResultSet"):
                obj = LiveStreamOcrFullTextRecognitionResult()
                obj._deserialize(item)
                self.OcrFullTextRecognitionResultSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveStreamAiReviewImagePoliticalResult(AbstractModel):
    """The result of detecting sensitive information in live streaming videos.

    """

    def __init__(self):
        r"""
        :param StartPtsTime: Start PTS time of a suspected segment in seconds.
        :type StartPtsTime: float
        :param EndPtsTime: End PTS time of a suspected segment in seconds.
        :type EndPtsTime: float
        :param Confidence: The confidence score for the detected sensitive segments.
        :type Confidence: float
        :param Suggestion: Suggestion for porn information detection of a suspected segment. Valid values:
<li>pass</li>
<li>review</li>
<li>block</li>
        :type Suggestion: str
        :param Label: The labels for the detected sensitive information. Valid values:
<li>politician</li>
<li>violation_photo (banned icons)</li>
        :type Label: str
        :param Name: The name of a sensitive person or banned icon.
        :type Name: str
        :param AreaCoordSet: The pixel coordinates of the detected sensitive people or banned icons. The format is [x1, y1, x2, y2], which indicates the coordinates of the top-left and bottom-right corners.
        :type AreaCoordSet: list of int
        :param Url: URL of a suspected image (which will not be permanently stored
and will be deleted after `PicUrlExpireTime`).
        :type Url: str
        :param PicUrlExpireTime: Expiration time of a suspected image URL in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F).
        :type PicUrlExpireTime: str
        """
        self.StartPtsTime = None
        self.EndPtsTime = None
        self.Confidence = None
        self.Suggestion = None
        self.Label = None
        self.Name = None
        self.AreaCoordSet = None
        self.Url = None
        self.PicUrlExpireTime = None


    def _deserialize(self, params):
        self.StartPtsTime = params.get("StartPtsTime")
        self.EndPtsTime = params.get("EndPtsTime")
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.Label = params.get("Label")
        self.Name = params.get("Name")
        self.AreaCoordSet = params.get("AreaCoordSet")
        self.Url = params.get("Url")
        self.PicUrlExpireTime = params.get("PicUrlExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveStreamAiReviewImagePornResult(AbstractModel):
    """Result of porn information detection in image in AI-based live stream content audit

    """

    def __init__(self):
        r"""
        :param StartPtsTime: Start PTS time of a suspected segment in seconds.
        :type StartPtsTime: float
        :param EndPtsTime: End PTS time of a suspected segment in seconds.
        :type EndPtsTime: float
        :param Confidence: Score of a suspected porn segment.
        :type Confidence: float
        :param Suggestion: Suggestion for porn information detection of a suspected segment. Valid values:
<li>pass</li>
<li>review</li>
<li>block</li>
        :type Suggestion: str
        :param Label: Tag of the detected porn information in video. Valid values:
<li>porn: Porn.</li>
<li>sexy: Sexiness.</li>
<li>vulgar: Vulgarity.</li>
<li>intimacy: Intimacy.</li>
        :type Label: str
        :param Url: URL of a suspected image (which will not be permanently stored
and will be deleted after `PicUrlExpireTime`).
        :type Url: str
        :param PicUrlExpireTime: Expiration time of a suspected image URL in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F).
        :type PicUrlExpireTime: str
        """
        self.StartPtsTime = None
        self.EndPtsTime = None
        self.Confidence = None
        self.Suggestion = None
        self.Label = None
        self.Url = None
        self.PicUrlExpireTime = None


    def _deserialize(self, params):
        self.StartPtsTime = params.get("StartPtsTime")
        self.EndPtsTime = params.get("EndPtsTime")
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.Label = params.get("Label")
        self.Url = params.get("Url")
        self.PicUrlExpireTime = params.get("PicUrlExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveStreamAiReviewImageTerrorismResult(AbstractModel):
    """The result of detecting sensitive information in live streaming videos.

    """

    def __init__(self):
        r"""
        :param StartPtsTime: Start PTS time of a suspected segment in seconds.
        :type StartPtsTime: float
        :param EndPtsTime: End PTS time of a suspected segment in seconds.
        :type EndPtsTime: float
        :param Confidence: The confidence score for the detected sensitive segments.
        :type Confidence: float
        :param Suggestion: The suggestion for handling the sensitive segments. Valid values:
<li>pass</li>
<li>review</li>
<li>block</li>
        :type Suggestion: str
        :param Label: The labels for the detected sensitive content. Valid values:
<li>guns</li>
<li>crowd</li>
<li>police</li>
<li>bloody</li>
<li>banners (sensitive flags)</li>
<li>militant</li>
<li>explosion</li>
<li>terrorists</li>
        :type Label: str
        :param Url: URL of a suspected image (which will not be permanently stored
and will be deleted after `PicUrlExpireTime`).
        :type Url: str
        :param PicUrlExpireTime: Expiration time of a suspected image URL in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F).
        :type PicUrlExpireTime: str
        """
        self.StartPtsTime = None
        self.EndPtsTime = None
        self.Confidence = None
        self.Suggestion = None
        self.Label = None
        self.Url = None
        self.PicUrlExpireTime = None


    def _deserialize(self, params):
        self.StartPtsTime = params.get("StartPtsTime")
        self.EndPtsTime = params.get("EndPtsTime")
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.Label = params.get("Label")
        self.Url = params.get("Url")
        self.PicUrlExpireTime = params.get("PicUrlExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveStreamAiReviewResultInfo(AbstractModel):
    """Result of AI-based live stream audit

    """

    def __init__(self):
        r"""
        :param ResultSet: List of content audit results.
        :type ResultSet: list of LiveStreamAiReviewResultItem
        """
        self.ResultSet = None


    def _deserialize(self, params):
        if params.get("ResultSet") is not None:
            self.ResultSet = []
            for item in params.get("ResultSet"):
                obj = LiveStreamAiReviewResultItem()
                obj._deserialize(item)
                self.ResultSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveStreamAiReviewResultItem(AbstractModel):
    """Result of AI-based live stream audit

    """

    def __init__(self):
        r"""
        :param Type: The type of the moderation result. Valid values:
<li>ImagePorn</li>
<li>ImageTerrorism</li>
<li>ImagePolitical</li>
<li>PornVoice (pornographic content in speech)</li>
        :type Type: str
        :param ImagePornResultSet: Result of porn information detection in image, which is valid when `Type` is `ImagePorn`.
        :type ImagePornResultSet: list of LiveStreamAiReviewImagePornResult
        :param ImageTerrorismResultSet: The result of detecting sensitive information in images, which is valid if `Type` is `ImageTerrorism`.
        :type ImageTerrorismResultSet: list of LiveStreamAiReviewImageTerrorismResult
        :param ImagePoliticalResultSet: The result of detecting sensitive information in images, which is valid if `Type` is `ImagePolitical`.
        :type ImagePoliticalResultSet: list of LiveStreamAiReviewImagePoliticalResult
        :param VoicePornResultSet: Result of porn information detection in speech, which is valid when `Type` is `PornVoice`.
        :type VoicePornResultSet: list of LiveStreamAiReviewVoicePornResult
        """
        self.Type = None
        self.ImagePornResultSet = None
        self.ImageTerrorismResultSet = None
        self.ImagePoliticalResultSet = None
        self.VoicePornResultSet = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("ImagePornResultSet") is not None:
            self.ImagePornResultSet = []
            for item in params.get("ImagePornResultSet"):
                obj = LiveStreamAiReviewImagePornResult()
                obj._deserialize(item)
                self.ImagePornResultSet.append(obj)
        if params.get("ImageTerrorismResultSet") is not None:
            self.ImageTerrorismResultSet = []
            for item in params.get("ImageTerrorismResultSet"):
                obj = LiveStreamAiReviewImageTerrorismResult()
                obj._deserialize(item)
                self.ImageTerrorismResultSet.append(obj)
        if params.get("ImagePoliticalResultSet") is not None:
            self.ImagePoliticalResultSet = []
            for item in params.get("ImagePoliticalResultSet"):
                obj = LiveStreamAiReviewImagePoliticalResult()
                obj._deserialize(item)
                self.ImagePoliticalResultSet.append(obj)
        if params.get("VoicePornResultSet") is not None:
            self.VoicePornResultSet = []
            for item in params.get("VoicePornResultSet"):
                obj = LiveStreamAiReviewVoicePornResult()
                obj._deserialize(item)
                self.VoicePornResultSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveStreamAiReviewVoicePornResult(AbstractModel):
    """Result of porn information detection in speech in AI-based live stream content audit

    """

    def __init__(self):
        r"""
        :param StartPtsTime: Start PTS time of a suspected segment in seconds.
        :type StartPtsTime: float
        :param EndPtsTime: End PTS time of a suspected segment in seconds.
        :type EndPtsTime: float
        :param Confidence: Score of a suspected porn segment.
        :type Confidence: float
        :param Suggestion: Suggestion for porn information detection of a suspected segment. Valid values:
<li>pass</li>
<li>review</li>
<li>block</li>
        :type Suggestion: str
        :param Label: Tag of the detected porn information in video. Valid values:
<li>sexual_moan: Sexual moans.</li>
        :type Label: str
        """
        self.StartPtsTime = None
        self.EndPtsTime = None
        self.Confidence = None
        self.Suggestion = None
        self.Label = None


    def _deserialize(self, params):
        self.StartPtsTime = params.get("StartPtsTime")
        self.EndPtsTime = params.get("EndPtsTime")
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.Label = params.get("Label")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveStreamAsrFullTextRecognitionResult(AbstractModel):
    """ASR-based full live stream recognition

    """

    def __init__(self):
        r"""
        :param Text: Recognized text.
        :type Text: str
        :param StartPtsTime: Start PTS time of recognized segment in seconds.
        :type StartPtsTime: float
        :param EndPtsTime: End PTS time of recognized segment in seconds.
        :type EndPtsTime: float
        :param Confidence: Confidence of recognized segment. Value range: 0–100.
        :type Confidence: float
        """
        self.Text = None
        self.StartPtsTime = None
        self.EndPtsTime = None
        self.Confidence = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.StartPtsTime = params.get("StartPtsTime")
        self.EndPtsTime = params.get("EndPtsTime")
        self.Confidence = params.get("Confidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveStreamAsrWordsRecognitionResult(AbstractModel):
    """AI-based ASR-based live streaming keyword recognition result

    """

    def __init__(self):
        r"""
        :param Word: Speech keyword.
        :type Word: str
        :param StartPtsTime: Start PTS time of recognized segment in seconds.
        :type StartPtsTime: float
        :param EndPtsTime: End PTS time of recognized segment in seconds.
        :type EndPtsTime: float
        :param Confidence: Confidence of recognized segment. Value range: 0–100.
        :type Confidence: float
        """
        self.Word = None
        self.StartPtsTime = None
        self.EndPtsTime = None
        self.Confidence = None


    def _deserialize(self, params):
        self.Word = params.get("Word")
        self.StartPtsTime = params.get("StartPtsTime")
        self.EndPtsTime = params.get("EndPtsTime")
        self.Confidence = params.get("Confidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveStreamFaceRecognitionResult(AbstractModel):
    """AI-based live streaming face recognition result

    """

    def __init__(self):
        r"""
        :param Id: Unique ID of figure.
        :type Id: str
        :param Name: Figure name.
        :type Name: str
        :param Type: Figure library type, indicating to which figure library the recognized figure belongs:
<li>Default: default figure library</li><li>UserDefine: custom figure library</li>
        :type Type: str
        :param StartPtsTime: Start PTS time of recognized segment in seconds.
        :type StartPtsTime: float
        :param EndPtsTime: End PTS time of recognized segment in seconds.
        :type EndPtsTime: float
        :param Confidence: Confidence of recognized segment. Value range: 0–100.
        :type Confidence: float
        :param AreaCoordSet: Zone coordinates of recognition result. The array contains four elements: [x1,y1,x2,y2], i.e., the horizontal and vertical coordinates of the top-left and bottom-right corners.
        :type AreaCoordSet: list of int
        """
        self.Id = None
        self.Name = None
        self.Type = None
        self.StartPtsTime = None
        self.EndPtsTime = None
        self.Confidence = None
        self.AreaCoordSet = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.StartPtsTime = params.get("StartPtsTime")
        self.EndPtsTime = params.get("EndPtsTime")
        self.Confidence = params.get("Confidence")
        self.AreaCoordSet = params.get("AreaCoordSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveStreamOcrFullTextRecognitionResult(AbstractModel):
    """OCR-based full live stream recognition

    """

    def __init__(self):
        r"""
        :param Text: Speech text.
        :type Text: str
        :param StartPtsTime: Start PTS time of recognized segment in seconds.
        :type StartPtsTime: float
        :param EndPtsTime: End PTS time of recognized segment in seconds.
        :type EndPtsTime: float
        :param Confidence: Confidence of recognized segment. Value range: 0–100.
        :type Confidence: float
        :param AreaCoordSet: Zone coordinates of recognition result. The array contains four elements: [x1,y1,x2,y2], i.e., the horizontal and vertical coordinates of the top-left and bottom-right corners.
        :type AreaCoordSet: list of int
        """
        self.Text = None
        self.StartPtsTime = None
        self.EndPtsTime = None
        self.Confidence = None
        self.AreaCoordSet = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.StartPtsTime = params.get("StartPtsTime")
        self.EndPtsTime = params.get("EndPtsTime")
        self.Confidence = params.get("Confidence")
        self.AreaCoordSet = params.get("AreaCoordSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveStreamOcrWordsRecognitionResult(AbstractModel):
    """AI-based OCR-based live streaming keyword recognition result

    """

    def __init__(self):
        r"""
        :param Word: Text keyword.
        :type Word: str
        :param StartPtsTime: Start PTS time of recognized segment in seconds.
        :type StartPtsTime: float
        :param EndPtsTime: End PTS time of recognized segment in seconds.
        :type EndPtsTime: float
        :param Confidence: Confidence of recognized segment. Value range: 0–100.
        :type Confidence: float
        :param AreaCoords: Zone coordinates of recognition result. The array contains four elements: [x1,y1,x2,y2], i.e., the horizontal and vertical coordinates of the top-left and bottom-right corners.
        :type AreaCoords: list of int
        """
        self.Word = None
        self.StartPtsTime = None
        self.EndPtsTime = None
        self.Confidence = None
        self.AreaCoords = None


    def _deserialize(self, params):
        self.Word = params.get("Word")
        self.StartPtsTime = params.get("StartPtsTime")
        self.EndPtsTime = params.get("EndPtsTime")
        self.Confidence = params.get("Confidence")
        self.AreaCoords = params.get("AreaCoords")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveStreamProcessErrorInfo(AbstractModel):
    """Information of a live stream processing error

    """

    def __init__(self):
        r"""
        :param ErrCode: Error code:
<li>0: No error;</li>
<li>If this parameter is not 0, an error has occurred. Please see the error message (`Message`).</li>
        :type ErrCode: int
        :param Message: Error message.
        :type Message: str
        """
        self.ErrCode = None
        self.Message = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveStreamProcessTask(AbstractModel):
    """Information of a live stream processing task

    """

    def __init__(self):
        r"""
        :param TaskId: Video processing task ID.
        :type TaskId: str
        :param Status: Task flow status. Valid values:
<li>PROCESSING: Processing;</li>
<li>FINISH: Completed.</li>
        :type Status: str
        :param ErrCode: Error code. 0: success; other values: failure.
        :type ErrCode: int
        :param Message: Error message.
        :type Message: str
        :param Url: Live stream URL.
        :type Url: str
        """
        self.TaskId = None
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Url = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        self.Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveStreamTaskNotifyConfig(AbstractModel):
    """Event notification configuration of a task.

    """

    def __init__(self):
        r"""
        :param CmqModel: CMQ model. There are two types: `Queue` and `Topic`. Currently, only `Queue` is supported.
        :type CmqModel: str
        :param CmqRegion: CMQ region, such as `sh` and `bj`.
        :type CmqRegion: str
        :param QueueName: This parameter is valid when the model is `Queue`, indicating the name of the CMQ queue for receiving event notifications.
        :type QueueName: str
        :param TopicName: This parameter is valid when the model is `Topic`, indicating the name of the CMQ topic for receiving event notifications.
        :type TopicName: str
        :param NotifyType: Notification type, `CMQ` by default. If this parameter is set to `URL`, HTTP callbacks are sent to the URL specified by `NotifyUrl`.
        :type NotifyType: str
        :param NotifyUrl: HTTP callback URL, required if `NotifyType` is set to `URL`
        :type NotifyUrl: str
        """
        self.CmqModel = None
        self.CmqRegion = None
        self.QueueName = None
        self.TopicName = None
        self.NotifyType = None
        self.NotifyUrl = None


    def _deserialize(self, params):
        self.CmqModel = params.get("CmqModel")
        self.CmqRegion = params.get("CmqRegion")
        self.QueueName = params.get("QueueName")
        self.TopicName = params.get("TopicName")
        self.NotifyType = params.get("NotifyType")
        self.NotifyUrl = params.get("NotifyUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManageTaskRequest(AbstractModel):
    """ManageTask request structure.

    """

    def __init__(self):
        r"""
        :param OperationType: Operation type. Valid values:
<ul>
<li>Abort: task termination. Description:
<ul><li>If the [task type](https://intl.cloud.tencent.com/document/product/862/37614?from_cn_redirect=1#3.-.E8.BE.93.E5.87.BA.E5.8F.82.E6.95.B0) is live stream processing (`LiveStreamProcessTask`), tasks whose [task status](https://intl.cloud.tencent.com/document/product/862/37614?from_cn_redirect=1#3.-.E8.BE.93.E5.87.BA.E5.8F.82.E6.95.B0) is `WAITING` or `PROCESSING` can be terminated.</li>
<li>For other [task types](https://intl.cloud.tencent.com/document/product/862/37614?from_cn_redirect=1#3.-.E8.BE.93.E5.87.BA.E5.8F.82.E6.95.B0), only tasks whose [task status](https://intl.cloud.tencent.com/document/product/862/37614?from_cn_redirect=1#3.-.E8.BE.93.E5.87.BA.E5.8F.82.E6.95.B0) is `WAITING` can be terminated.</li></ul>
</li></ul>
        :type OperationType: str
        :param TaskId: Video processing task ID.
        :type TaskId: str
        """
        self.OperationType = None
        self.TaskId = None


    def _deserialize(self, params):
        self.OperationType = params.get("OperationType")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManageTaskResponse(AbstractModel):
    """ManageTask response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class MediaAiAnalysisClassificationItem(AbstractModel):
    """Intelligent categorization result

    """

    def __init__(self):
        r"""
        :param Classification: Name of intelligently generated category.
        :type Classification: str
        :param Confidence: Confidence of intelligently generated category between 0 and 100.
        :type Confidence: float
        """
        self.Classification = None
        self.Confidence = None


    def _deserialize(self, params):
        self.Classification = params.get("Classification")
        self.Confidence = params.get("Confidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaAiAnalysisCoverItem(AbstractModel):
    """Information of intelligently generated cover

    """

    def __init__(self):
        r"""
        :param CoverPath: Storage path of intelligently generated cover.
        :type CoverPath: str
        :param Confidence: Confidence of intelligently generated cover between 0 and 100.
        :type Confidence: float
        """
        self.CoverPath = None
        self.Confidence = None


    def _deserialize(self, params):
        self.CoverPath = params.get("CoverPath")
        self.Confidence = params.get("Confidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaAiAnalysisFrameTagItem(AbstractModel):
    """Result information of intelligent frame-specific tagging

    """

    def __init__(self):
        r"""
        :param Tag: Frame-specific tag name.
        :type Tag: str
        :param CategorySet: 
        :type CategorySet: list of str
        :param Confidence: Confidence of intelligently generated frame-specific tag between 0 and 100.
        :type Confidence: float
        """
        self.Tag = None
        self.CategorySet = None
        self.Confidence = None


    def _deserialize(self, params):
        self.Tag = params.get("Tag")
        self.CategorySet = params.get("CategorySet")
        self.Confidence = params.get("Confidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaAiAnalysisFrameTagSegmentItem(AbstractModel):
    """List of frame-specific tag segments

    """

    def __init__(self):
        r"""
        :param StartTimeOffset: Start time offset of frame-specific tag.
        :type StartTimeOffset: float
        :param EndTimeOffset: End time offset of frame-specific tag.
        :type EndTimeOffset: float
        :param TagSet: List of tags in time period.
        :type TagSet: list of MediaAiAnalysisFrameTagItem
        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.TagSet = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = MediaAiAnalysisFrameTagItem()
                obj._deserialize(item)
                self.TagSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaAiAnalysisTagItem(AbstractModel):
    """Result information of intelligent tagging

    """

    def __init__(self):
        r"""
        :param Tag: Tag name.
        :type Tag: str
        :param Confidence: Confidence of tag between 0 and 100.
        :type Confidence: float
        """
        self.Tag = None
        self.Confidence = None


    def _deserialize(self, params):
        self.Tag = params.get("Tag")
        self.Confidence = params.get("Confidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaAnimatedGraphicsItem(AbstractModel):
    """Result information of an animated image generating task

    """

    def __init__(self):
        r"""
        :param Storage: Storage location of a generated animated image file.
        :type Storage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        :param Path: Path to a generated animated image file.
        :type Path: str
        :param Definition: ID of an animated image generating template. For more information, please see [Animated Image Generating Parameter Template](https://intl.cloud.tencent.com/document/product/266/33481?from_cn_redirect=1#.E8.BD.AC.E5.8A.A8.E5.9B.BE.E6.A8.A1.E6.9D.BF).
        :type Definition: int
        :param Container: Animated image format, such as gif.
        :type Container: str
        :param Height: Height of an animated image in px.
        :type Height: int
        :param Width: Width of an animated image in px.
        :type Width: int
        :param Bitrate: Bitrate of an animated image in bps.
        :type Bitrate: int
        :param Size: Size of an animated image in bytes.
        :type Size: int
        :param Md5: MD5 value of an animated image.
        :type Md5: str
        :param StartTimeOffset: Start time offset of an animated image in the video in seconds.
        :type StartTimeOffset: float
        :param EndTimeOffset: End time offset of an animated image in the video in seconds.
        :type EndTimeOffset: float
        """
        self.Storage = None
        self.Path = None
        self.Definition = None
        self.Container = None
        self.Height = None
        self.Width = None
        self.Bitrate = None
        self.Size = None
        self.Md5 = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None


    def _deserialize(self, params):
        if params.get("Storage") is not None:
            self.Storage = TaskOutputStorage()
            self.Storage._deserialize(params.get("Storage"))
        self.Path = params.get("Path")
        self.Definition = params.get("Definition")
        self.Container = params.get("Container")
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.Bitrate = params.get("Bitrate")
        self.Size = params.get("Size")
        self.Md5 = params.get("Md5")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaAudioStreamItem(AbstractModel):
    """Information of the audio stream in a VOD file

    """

    def __init__(self):
        r"""
        :param Bitrate: Bitrate of an audio stream in bps.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Bitrate: int
        :param SamplingRate: Sample rate of an audio stream in Hz.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SamplingRate: int
        :param Codec: Audio stream codec, such as aac.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Codec: str
        :param Channel: Number of sound channels, e.g., 2
Note: this field may return `null`, indicating that no valid value was found.
        :type Channel: int
        """
        self.Bitrate = None
        self.SamplingRate = None
        self.Codec = None
        self.Channel = None


    def _deserialize(self, params):
        self.Bitrate = params.get("Bitrate")
        self.SamplingRate = params.get("SamplingRate")
        self.Codec = params.get("Codec")
        self.Channel = params.get("Channel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaContentReviewAsrTextSegmentItem(AbstractModel):
    """Suspected segment identified during ASR-based text audit during content audit

    """

    def __init__(self):
        r"""
        :param StartTimeOffset: Start time offset of a suspected segment in seconds.
        :type StartTimeOffset: float
        :param EndTimeOffset: End time offset of a suspected segment in seconds.
        :type EndTimeOffset: float
        :param Confidence: Confidence of a suspected segment.
        :type Confidence: float
        :param Suggestion: Suggestion for suspected segment audit. Valid values:
<li>pass.</li>
<li>review.</li>
<li>block.</li>
        :type Suggestion: str
        :param KeywordSet: List of suspected keywords.
        :type KeywordSet: list of str
        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.Confidence = None
        self.Suggestion = None
        self.KeywordSet = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.KeywordSet = params.get("KeywordSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaContentReviewOcrTextSegmentItem(AbstractModel):
    """Suspected segment identified during OCR-based text audit during content audit

    """

    def __init__(self):
        r"""
        :param StartTimeOffset: Start time offset of a suspected segment in seconds.
        :type StartTimeOffset: float
        :param EndTimeOffset: End time offset of a suspected segment in seconds.
        :type EndTimeOffset: float
        :param Confidence: Confidence of a suspected segment.
        :type Confidence: float
        :param Suggestion: Suggestion for suspected segment audit. Valid values:
<li>pass.</li>
<li>review.</li>
<li>block.</li>
        :type Suggestion: str
        :param KeywordSet: List of suspected keywords.
        :type KeywordSet: list of str
        :param AreaCoordSet: Zone coordinates (at the pixel level) of suspected text: [x1, y1, x2, y2], i.e., the coordinates of the top-left and bottom-right corners.
        :type AreaCoordSet: list of int
        :param Url: URL of a suspected image (which will not be permanently stored
and will be deleted after `PicUrlExpireTime`).
        :type Url: str
        :param PicUrlExpireTime: Expiration time of a suspected image URL in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F).
        :type PicUrlExpireTime: str
        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.Confidence = None
        self.Suggestion = None
        self.KeywordSet = None
        self.AreaCoordSet = None
        self.Url = None
        self.PicUrlExpireTime = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.KeywordSet = params.get("KeywordSet")
        self.AreaCoordSet = params.get("AreaCoordSet")
        self.Url = params.get("Url")
        self.PicUrlExpireTime = params.get("PicUrlExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaContentReviewPoliticalSegmentItem(AbstractModel):
    """The information about the sensitive segments detected.

    """

    def __init__(self):
        r"""
        :param StartTimeOffset: Start time offset of a suspected segment in seconds.
        :type StartTimeOffset: float
        :param EndTimeOffset: End time offset of a suspected segment in seconds.
        :type EndTimeOffset: float
        :param Confidence: The confidence score for the detected sensitive segments.
        :type Confidence: float
        :param Suggestion: The suggestion for handling the sensitive segments. Valid values:
<li>pass</li>
<li>review</li>
<li>block</li>
        :type Suggestion: str
        :param Name: The name of a sensitive person or banned icon.
        :type Name: str
        :param Label: The labels for the detected sensitive segments. The relationship between the values of this parameter and those of the `LabelSet` parameter in [PoliticalImgReviewTemplateInfo](https://intl.cloud.tencent.com/document/api/862/37615?from_cn_redirect=1#PoliticalImgReviewTemplateInfo) is as follows:
violation_photo:
<li>violation_photo (banned icons)</li>
politician:
<li>nation_politician (state leader)</li>
<li>province_politician (provincial officials)</li>
<li>bureau_politician (bureau-level officials)</li>
<li>county_politician (county-level officials)</li>
<li>rural_politician (township-level officials)</li>
<li>sensitive_politician (sensitive people)</li>
<li>foreign_politician (state leaders of other countries)</li>
entertainment:
<li>sensitive_entertainment (sensitive people in the entertainment industry</li>
sport:
<li>sensitive_sport (sensitive sports celebrities)</li>
entrepreneur:
<li>sensitive_entrepreneur</li>
scholar:
<li>sensitive_scholar</li>
celebrity:
<li>sensitive_celebrity</li>
<li>historical_celebrity (sensitive historical figures)</li>
military:
<li>sensitive_military (sensitive people in military)</li>
        :type Label: str
        :param Url: URL of a suspected image (which will not be permanently stored
 and will be deleted after `PicUrlExpireTime`).
        :type Url: str
        :param AreaCoordSet: The pixel coordinates of the detected sensitive people or banned icons. The format is [x1, y1, x2, y2], which indicates the coordinates of the top-left and bottom-right corners.
        :type AreaCoordSet: list of int
        :param PicUrlExpireTime: Expiration time of a suspected image URL in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F).
        :type PicUrlExpireTime: str
        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.Confidence = None
        self.Suggestion = None
        self.Name = None
        self.Label = None
        self.Url = None
        self.AreaCoordSet = None
        self.PicUrlExpireTime = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.Name = params.get("Name")
        self.Label = params.get("Label")
        self.Url = params.get("Url")
        self.AreaCoordSet = params.get("AreaCoordSet")
        self.PicUrlExpireTime = params.get("PicUrlExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaContentReviewSegmentItem(AbstractModel):
    """The information about the detected pornographic/sensitive segments.

    """

    def __init__(self):
        r"""
        :param StartTimeOffset: Start time offset of a suspected segment in seconds.
        :type StartTimeOffset: float
        :param EndTimeOffset: End time offset of a suspected segment in seconds.
        :type EndTimeOffset: float
        :param Confidence: Score of a suspected porn segment.
        :type Confidence: float
        :param Label: Tag of porn information detection result of a suspected segment.
        :type Label: str
        :param Suggestion: Suggestion for porn information detection of a suspected segment. Valid values:
<li>pass.</li>
<li>review.</li>
<li>block.</li>
        :type Suggestion: str
        :param Url: URL of a suspected image (which will not be permanently stored
 and will be deleted after `PicUrlExpireTime`).
        :type Url: str
        :param PicUrlExpireTime: Expiration time of a suspected image URL in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F).
        :type PicUrlExpireTime: str
        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.Confidence = None
        self.Label = None
        self.Suggestion = None
        self.Url = None
        self.PicUrlExpireTime = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.Confidence = params.get("Confidence")
        self.Label = params.get("Label")
        self.Suggestion = params.get("Suggestion")
        self.Url = params.get("Url")
        self.PicUrlExpireTime = params.get("PicUrlExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaImageSpriteItem(AbstractModel):
    """Image sprite information

    """

    def __init__(self):
        r"""
        :param Definition: Image sprite specification. For more information, please see [Image Sprite Parameter Template](https://intl.cloud.tencent.com/document/product/266/33480?from_cn_redirect=1#.E9.9B.AA.E7.A2.A7.E5.9B.BE.E6.A8.A1.E6.9D.BF).
        :type Definition: int
        :param Height: Subimage height of an image sprite.
        :type Height: int
        :param Width: Subimage width of an image sprite.
        :type Width: int
        :param TotalCount: Total number of subimages in each image sprite.
        :type TotalCount: int
        :param ImagePathSet: Path to each image sprite.
        :type ImagePathSet: list of str
        :param WebVttPath: Path to a WebVtt file for the position-time relationship among subimages in an image sprite. The WebVtt file indicates the corresponding time points of each subimage and their coordinates in the image sprite, which is typically used by the player for implementing preview.
        :type WebVttPath: str
        :param Storage: Storage location of an image sprite file.
        :type Storage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        """
        self.Definition = None
        self.Height = None
        self.Width = None
        self.TotalCount = None
        self.ImagePathSet = None
        self.WebVttPath = None
        self.Storage = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.TotalCount = params.get("TotalCount")
        self.ImagePathSet = params.get("ImagePathSet")
        self.WebVttPath = params.get("WebVttPath")
        if params.get("Storage") is not None:
            self.Storage = TaskOutputStorage()
            self.Storage._deserialize(params.get("Storage"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaInputInfo(AbstractModel):
    """Information of a video processing input object.

    """

    def __init__(self):
        r"""
        :param Type: The type of video processing input object, which supports COS and URL.
        :type Type: str
        :param CosInputInfo: This parameter is required and valid when `Type` is `COS`, indicating the information of a COS object for video processing.
        :type CosInputInfo: :class:`tencentcloud.mps.v20190612.models.CosInputInfo`
        :param UrlInputInfo: This parameter is required and valid when `Type` is `URL`, indicating the information of a URL object for video processing.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type UrlInputInfo: :class:`tencentcloud.mps.v20190612.models.UrlInputInfo`
        """
        self.Type = None
        self.CosInputInfo = None
        self.UrlInputInfo = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("CosInputInfo") is not None:
            self.CosInputInfo = CosInputInfo()
            self.CosInputInfo._deserialize(params.get("CosInputInfo"))
        if params.get("UrlInputInfo") is not None:
            self.UrlInputInfo = UrlInputInfo()
            self.UrlInputInfo._deserialize(params.get("UrlInputInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaMetaData(AbstractModel):
    """Metadata of a VOD media file

    """

    def __init__(self):
        r"""
        :param Size: Size of an uploaded media file in bytes (which is the sum of size of m3u8 and ts files if the video is in HLS format).
Note: This field may return null, indicating that no valid values can be obtained.
        :type Size: int
        :param Container: Container, such as m4a and mp4.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Container: str
        :param Bitrate: Sum of the average bitrate of a video stream and that of an audio stream in bps.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Bitrate: int
        :param Height: Maximum value of the height of a video stream in px.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Height: int
        :param Width: Maximum value of the width of a video stream in px.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Width: int
        :param Duration: Video duration in seconds.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Duration: float
        :param Rotate: Selected angle during video recording in degrees.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Rotate: int
        :param VideoStreamSet: Video stream information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type VideoStreamSet: list of MediaVideoStreamItem
        :param AudioStreamSet: Audio stream information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AudioStreamSet: list of MediaAudioStreamItem
        :param VideoDuration: Video duration in seconds.
Note: This field may return null, indicating that no valid values can be obtained.
        :type VideoDuration: float
        :param AudioDuration: Audio duration in seconds.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AudioDuration: float
        """
        self.Size = None
        self.Container = None
        self.Bitrate = None
        self.Height = None
        self.Width = None
        self.Duration = None
        self.Rotate = None
        self.VideoStreamSet = None
        self.AudioStreamSet = None
        self.VideoDuration = None
        self.AudioDuration = None


    def _deserialize(self, params):
        self.Size = params.get("Size")
        self.Container = params.get("Container")
        self.Bitrate = params.get("Bitrate")
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.Duration = params.get("Duration")
        self.Rotate = params.get("Rotate")
        if params.get("VideoStreamSet") is not None:
            self.VideoStreamSet = []
            for item in params.get("VideoStreamSet"):
                obj = MediaVideoStreamItem()
                obj._deserialize(item)
                self.VideoStreamSet.append(obj)
        if params.get("AudioStreamSet") is not None:
            self.AudioStreamSet = []
            for item in params.get("AudioStreamSet"):
                obj = MediaAudioStreamItem()
                obj._deserialize(item)
                self.AudioStreamSet.append(obj)
        self.VideoDuration = params.get("VideoDuration")
        self.AudioDuration = params.get("AudioDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaProcessTaskAdaptiveDynamicStreamingResult(AbstractModel):
    """Result type of adaptive bitrate streaming task

    """

    def __init__(self):
        r"""
        :param Status: Task status. Valid values: PROCESSING, SUCCESS, FAIL.
        :type Status: str
        :param ErrCodeExt: Error code. An empty string indicates the task is successful; otherwise it is failed. For details about the values, see [Error Code List](https://intl.cloud.tencent.com/document/product/862/50369?from_cn_redirect=1#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81).
        :type ErrCodeExt: str
        :param ErrCode: Error code. 0 indicates the task is successful; otherwise it is failed. This parameter is no longer recommended. Consider using the new error code parameter ErrCodeExt.
        :type ErrCode: int
        :param Message: Error message.
        :type Message: str
        :param Input: Input of an adaptive bitrate streaming task.
        :type Input: :class:`tencentcloud.mps.v20190612.models.AdaptiveDynamicStreamingTaskInput`
        :param Output: Output of an adaptive bitrate streaming task.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Output: :class:`tencentcloud.mps.v20190612.models.AdaptiveDynamicStreamingInfoItem`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AdaptiveDynamicStreamingTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AdaptiveDynamicStreamingInfoItem()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaProcessTaskAnimatedGraphicResult(AbstractModel):
    """Result type of an animated image generating task

    """

    def __init__(self):
        r"""
        :param Status: Task status. Valid values: PROCESSING, SUCCESS, FAIL.
        :type Status: str
        :param ErrCodeExt: Error code. An empty string indicates the task is successful; otherwise it is failed. For details about the values, see [Error Code List](https://intl.cloud.tencent.com/document/product/862/50369?from_cn_redirect=1#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81).
        :type ErrCodeExt: str
        :param ErrCode: Error code. 0 indicates the task is successful; otherwise it is failed. This parameter is no longer recommended. Consider using the new error code parameter ErrCodeExt.
        :type ErrCode: int
        :param Message: Error message.
        :type Message: str
        :param Input: Input for an animated image generating task.
        :type Input: :class:`tencentcloud.mps.v20190612.models.AnimatedGraphicTaskInput`
        :param Output: Output of an animated image generating task.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Output: :class:`tencentcloud.mps.v20190612.models.MediaAnimatedGraphicsItem`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AnimatedGraphicTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = MediaAnimatedGraphicsItem()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaProcessTaskImageSpriteResult(AbstractModel):
    """Result type of an image sprite generating task

    """

    def __init__(self):
        r"""
        :param Status: Task status. Valid values: PROCESSING, SUCCESS, FAIL.
        :type Status: str
        :param ErrCodeExt: Error code. An empty string indicates the task is successful; otherwise it is failed. For details about the values, see [Error Code List](https://intl.cloud.tencent.com/document/product/862/50369?from_cn_redirect=1#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81).
        :type ErrCodeExt: str
        :param ErrCode: Error code. 0 indicates the task is successful; otherwise it is failed. This parameter is no longer recommended. Consider using the new error code parameter ErrCodeExt.
        :type ErrCode: int
        :param Message: Error message.
        :type Message: str
        :param Input: Input for an image sprite generating task.
        :type Input: :class:`tencentcloud.mps.v20190612.models.ImageSpriteTaskInput`
        :param Output: Output of an image sprite generating task.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Output: :class:`tencentcloud.mps.v20190612.models.MediaImageSpriteItem`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = ImageSpriteTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = MediaImageSpriteItem()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaProcessTaskInput(AbstractModel):
    """Type of a video processing task

    """

    def __init__(self):
        r"""
        :param TranscodeTaskSet: List of transcoding tasks.
        :type TranscodeTaskSet: list of TranscodeTaskInput
        :param AnimatedGraphicTaskSet: List of animated image generating tasks.
        :type AnimatedGraphicTaskSet: list of AnimatedGraphicTaskInput
        :param SnapshotByTimeOffsetTaskSet: List of time point screencapturing tasks.
        :type SnapshotByTimeOffsetTaskSet: list of SnapshotByTimeOffsetTaskInput
        :param SampleSnapshotTaskSet: List of sampled screencapturing tasks.
        :type SampleSnapshotTaskSet: list of SampleSnapshotTaskInput
        :param ImageSpriteTaskSet: List of image sprite generating tasks.
        :type ImageSpriteTaskSet: list of ImageSpriteTaskInput
        :param AdaptiveDynamicStreamingTaskSet: List of adaptive bitrate streaming tasks.
        :type AdaptiveDynamicStreamingTaskSet: list of AdaptiveDynamicStreamingTaskInput
        """
        self.TranscodeTaskSet = None
        self.AnimatedGraphicTaskSet = None
        self.SnapshotByTimeOffsetTaskSet = None
        self.SampleSnapshotTaskSet = None
        self.ImageSpriteTaskSet = None
        self.AdaptiveDynamicStreamingTaskSet = None


    def _deserialize(self, params):
        if params.get("TranscodeTaskSet") is not None:
            self.TranscodeTaskSet = []
            for item in params.get("TranscodeTaskSet"):
                obj = TranscodeTaskInput()
                obj._deserialize(item)
                self.TranscodeTaskSet.append(obj)
        if params.get("AnimatedGraphicTaskSet") is not None:
            self.AnimatedGraphicTaskSet = []
            for item in params.get("AnimatedGraphicTaskSet"):
                obj = AnimatedGraphicTaskInput()
                obj._deserialize(item)
                self.AnimatedGraphicTaskSet.append(obj)
        if params.get("SnapshotByTimeOffsetTaskSet") is not None:
            self.SnapshotByTimeOffsetTaskSet = []
            for item in params.get("SnapshotByTimeOffsetTaskSet"):
                obj = SnapshotByTimeOffsetTaskInput()
                obj._deserialize(item)
                self.SnapshotByTimeOffsetTaskSet.append(obj)
        if params.get("SampleSnapshotTaskSet") is not None:
            self.SampleSnapshotTaskSet = []
            for item in params.get("SampleSnapshotTaskSet"):
                obj = SampleSnapshotTaskInput()
                obj._deserialize(item)
                self.SampleSnapshotTaskSet.append(obj)
        if params.get("ImageSpriteTaskSet") is not None:
            self.ImageSpriteTaskSet = []
            for item in params.get("ImageSpriteTaskSet"):
                obj = ImageSpriteTaskInput()
                obj._deserialize(item)
                self.ImageSpriteTaskSet.append(obj)
        if params.get("AdaptiveDynamicStreamingTaskSet") is not None:
            self.AdaptiveDynamicStreamingTaskSet = []
            for item in params.get("AdaptiveDynamicStreamingTaskSet"):
                obj = AdaptiveDynamicStreamingTaskInput()
                obj._deserialize(item)
                self.AdaptiveDynamicStreamingTaskSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaProcessTaskResult(AbstractModel):
    """Query result type of a task

    """

    def __init__(self):
        r"""
        :param Type: Task type. Valid values:
<li>Transcode: Transcoding</li>
<li>AnimatedGraphics: Animated image generating</li>
<li>SnapshotByTimeOffset: Time point screencapturing</li>
<li>SampleSnapshot: Sampled screencapturing</li>
<li>ImageSprites: Image sprite generating</li>
<li>CoverBySnapshot: Screencapturing for cover image</li>
<li>AdaptiveDynamicStreaming: Adaptive bitrate streaming</li>
        :type Type: str
        :param TranscodeTask: Query result of a transcoding task, which is valid when task type is `Transcode`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TranscodeTask: :class:`tencentcloud.mps.v20190612.models.MediaProcessTaskTranscodeResult`
        :param AnimatedGraphicTask: Query result of an animated image generating task, which is valid when task type is `AnimatedGraphics`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AnimatedGraphicTask: :class:`tencentcloud.mps.v20190612.models.MediaProcessTaskAnimatedGraphicResult`
        :param SnapshotByTimeOffsetTask: Query result of a time point screencapturing task, which is valid when task type is `SnapshotByTimeOffset`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SnapshotByTimeOffsetTask: :class:`tencentcloud.mps.v20190612.models.MediaProcessTaskSnapshotByTimeOffsetResult`
        :param SampleSnapshotTask: Query result of a sampled screencapturing task, which is valid when task type is `SampleSnapshot`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SampleSnapshotTask: :class:`tencentcloud.mps.v20190612.models.MediaProcessTaskSampleSnapshotResult`
        :param ImageSpriteTask: Query result of an image sprite generating task, which is valid when task type is `ImageSprite`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ImageSpriteTask: :class:`tencentcloud.mps.v20190612.models.MediaProcessTaskImageSpriteResult`
        :param AdaptiveDynamicStreamingTask: Query result of an adaptive bitrate streaming task, which is valid if the task type is `AdaptiveDynamicStreaming`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AdaptiveDynamicStreamingTask: :class:`tencentcloud.mps.v20190612.models.MediaProcessTaskAdaptiveDynamicStreamingResult`
        """
        self.Type = None
        self.TranscodeTask = None
        self.AnimatedGraphicTask = None
        self.SnapshotByTimeOffsetTask = None
        self.SampleSnapshotTask = None
        self.ImageSpriteTask = None
        self.AdaptiveDynamicStreamingTask = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("TranscodeTask") is not None:
            self.TranscodeTask = MediaProcessTaskTranscodeResult()
            self.TranscodeTask._deserialize(params.get("TranscodeTask"))
        if params.get("AnimatedGraphicTask") is not None:
            self.AnimatedGraphicTask = MediaProcessTaskAnimatedGraphicResult()
            self.AnimatedGraphicTask._deserialize(params.get("AnimatedGraphicTask"))
        if params.get("SnapshotByTimeOffsetTask") is not None:
            self.SnapshotByTimeOffsetTask = MediaProcessTaskSnapshotByTimeOffsetResult()
            self.SnapshotByTimeOffsetTask._deserialize(params.get("SnapshotByTimeOffsetTask"))
        if params.get("SampleSnapshotTask") is not None:
            self.SampleSnapshotTask = MediaProcessTaskSampleSnapshotResult()
            self.SampleSnapshotTask._deserialize(params.get("SampleSnapshotTask"))
        if params.get("ImageSpriteTask") is not None:
            self.ImageSpriteTask = MediaProcessTaskImageSpriteResult()
            self.ImageSpriteTask._deserialize(params.get("ImageSpriteTask"))
        if params.get("AdaptiveDynamicStreamingTask") is not None:
            self.AdaptiveDynamicStreamingTask = MediaProcessTaskAdaptiveDynamicStreamingResult()
            self.AdaptiveDynamicStreamingTask._deserialize(params.get("AdaptiveDynamicStreamingTask"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaProcessTaskSampleSnapshotResult(AbstractModel):
    """Result type of a sampled screencapturing task

    """

    def __init__(self):
        r"""
        :param Status: Task status. Valid values: PROCESSING, SUCCESS, FAIL.
        :type Status: str
        :param ErrCodeExt: Error code. An empty string indicates the task is successful; otherwise it is failed. For details about the values, see [Error Code List](https://intl.cloud.tencent.com/document/product/862/50369?from_cn_redirect=1#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81).
        :type ErrCodeExt: str
        :param ErrCode: Error code. 0 indicates the task is successful; otherwise it is failed. This parameter is no longer recommended. Consider using the new error code parameter ErrCodeExt.
        :type ErrCode: int
        :param Message: Error message.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Message: str
        :param Input: Input for a sampled screencapturing task.
        :type Input: :class:`tencentcloud.mps.v20190612.models.SampleSnapshotTaskInput`
        :param Output: Output of a sampled screencapturing task.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Output: :class:`tencentcloud.mps.v20190612.models.MediaSampleSnapshotItem`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = SampleSnapshotTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = MediaSampleSnapshotItem()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaProcessTaskSnapshotByTimeOffsetResult(AbstractModel):
    """Result type of a time point screencapturing task

    """

    def __init__(self):
        r"""
        :param Status: Task status. Valid values: PROCESSING, SUCCESS, FAIL.
        :type Status: str
        :param ErrCodeExt: Error code. An empty string indicates the task is successful; otherwise it is failed. For details about the values, see [Error Code List](https://intl.cloud.tencent.com/document/product/862/50369?from_cn_redirect=1#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81).
        :type ErrCodeExt: str
        :param ErrCode: Error code. 0 indicates the task is successful; otherwise it is failed. This parameter is no longer recommended. Consider using the new error code parameter ErrCodeExt.
        :type ErrCode: int
        :param Message: Error message.
        :type Message: str
        :param Input: Input for a time point screencapturing task.
        :type Input: :class:`tencentcloud.mps.v20190612.models.SnapshotByTimeOffsetTaskInput`
        :param Output: Output of a time point screencapturing task.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Output: :class:`tencentcloud.mps.v20190612.models.MediaSnapshotByTimeOffsetItem`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = SnapshotByTimeOffsetTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = MediaSnapshotByTimeOffsetItem()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaProcessTaskTranscodeResult(AbstractModel):
    """Result type of a transcoding task

    """

    def __init__(self):
        r"""
        :param Status: Task status. Valid values: PROCESSING, SUCCESS, FAIL.
        :type Status: str
        :param ErrCodeExt: Error code. An empty string indicates the task is successful; otherwise it is failed. For details about the values, see [Error Code List](https://intl.cloud.tencent.com/document/product/862/50369?from_cn_redirect=1#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81).
        :type ErrCodeExt: str
        :param ErrCode: Error code. 0 indicates the task is successful; otherwise it is failed. This parameter is no longer recommended. Consider using the new error code parameter ErrCodeExt.
        :type ErrCode: int
        :param Message: Error message.
        :type Message: str
        :param Input: Input for a transcoding task.
        :type Input: :class:`tencentcloud.mps.v20190612.models.TranscodeTaskInput`
        :param Output: Output of a transcoding task.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Output: :class:`tencentcloud.mps.v20190612.models.MediaTranscodeItem`
        :param Progress: Transcoding progress. Value range: 0-100
Note: This field may return `null`, indicating that no valid value was found.
        :type Progress: int
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None
        self.Progress = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = TranscodeTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = MediaTranscodeItem()
            self.Output._deserialize(params.get("Output"))
        self.Progress = params.get("Progress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaSampleSnapshotItem(AbstractModel):
    """Information of a sampled screenshot

    """

    def __init__(self):
        r"""
        :param Definition: Sampled screenshot specification ID. For more information, please see [Sampled Screencapturing Parameter Template](https://intl.cloud.tencent.com/document/product/266/33480?from_cn_redirect=1#.E9.87.87.E6.A0.B7.E6.88.AA.E5.9B.BE.E6.A8.A1.E6.9D.BF).
        :type Definition: int
        :param SampleType: Sample type. Valid values:
<li>Percent: Samples at the specified percentage interval.</li>
<li>Time: Samples at the specified time interval.</li>
        :type SampleType: str
        :param Interval: Sampling interval
<li>If `SampleType` is `Percent`, this value means taking a screenshot at an interval of the specified percentage.</li>
<li>If `SampleType` is `Time`, this value means taking a screenshot at an interval of the specified time (in seconds). The first screenshot is always the first video frame.</li>
        :type Interval: int
        :param Storage: Storage location of a generated screenshot file.
        :type Storage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        :param ImagePathSet: List of paths to generated screenshots.
        :type ImagePathSet: list of str
        :param WaterMarkDefinition: List of watermarking template IDs if the screenshots are watermarked.
        :type WaterMarkDefinition: list of int
        """
        self.Definition = None
        self.SampleType = None
        self.Interval = None
        self.Storage = None
        self.ImagePathSet = None
        self.WaterMarkDefinition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.SampleType = params.get("SampleType")
        self.Interval = params.get("Interval")
        if params.get("Storage") is not None:
            self.Storage = TaskOutputStorage()
            self.Storage._deserialize(params.get("Storage"))
        self.ImagePathSet = params.get("ImagePathSet")
        self.WaterMarkDefinition = params.get("WaterMarkDefinition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaSnapshotByTimeOffsetItem(AbstractModel):
    """Information of the time point screenshots in a VOD file

    """

    def __init__(self):
        r"""
        :param Definition: Specification of a time point screenshot. For more information, please see [Parameter Template for Time Point Screencapturing](https://intl.cloud.tencent.com/document/product/266/33480?from_cn_redirect=1#.E6.97.B6.E9.97.B4.E7.82.B9.E6.88.AA.E5.9B.BE.E6.A8.A1.E6.9D.BF).
        :type Definition: int
        :param PicInfoSet: Information set of screenshots of the same specification. Each element represents a screenshot.
        :type PicInfoSet: list of MediaSnapshotByTimePicInfoItem
        :param Storage: Location of a time point screenshot file.
        :type Storage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        """
        self.Definition = None
        self.PicInfoSet = None
        self.Storage = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        if params.get("PicInfoSet") is not None:
            self.PicInfoSet = []
            for item in params.get("PicInfoSet"):
                obj = MediaSnapshotByTimePicInfoItem()
                obj._deserialize(item)
                self.PicInfoSet.append(obj)
        if params.get("Storage") is not None:
            self.Storage = TaskOutputStorage()
            self.Storage._deserialize(params.get("Storage"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaSnapshotByTimePicInfoItem(AbstractModel):
    """Information of a time point screenshot

    """

    def __init__(self):
        r"""
        :param TimeOffset: The timestamp (seconds) of the screenshot.
        :type TimeOffset: float
        :param Path: Path to the screenshot.
        :type Path: str
        :param WaterMarkDefinition: List of watermarking template IDs if the screenshots are watermarked.
        :type WaterMarkDefinition: list of int
        """
        self.TimeOffset = None
        self.Path = None
        self.WaterMarkDefinition = None


    def _deserialize(self, params):
        self.TimeOffset = params.get("TimeOffset")
        self.Path = params.get("Path")
        self.WaterMarkDefinition = params.get("WaterMarkDefinition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaTranscodeItem(AbstractModel):
    """Transcoding information

    """

    def __init__(self):
        r"""
        :param OutputStorage: Target bucket of an output file.
        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        :param Path: Path to an output video file.
        :type Path: str
        :param Definition: Transcoding specification ID. For more information, please see [Transcoding Parameter Template](https://intl.cloud.tencent.com/document/product/266/33478?from_cn_redirect=1#.E8.BD.AC.E7.A0.81.E6.A8.A1.E6.9D.BF).
        :type Definition: int
        :param Bitrate: Sum of the average bitrate of a video stream and that of an audio stream in bps.
        :type Bitrate: int
        :param Height: Maximum value of the height of a video stream in px.
        :type Height: int
        :param Width: Maximum value of the width of a video stream in px.
        :type Width: int
        :param Size: Total size of a media file in bytes (which is the sum of size of m3u8 and ts files if the video is in HLS format).
        :type Size: int
        :param Duration: Video duration in seconds.
        :type Duration: float
        :param Container: Container, such as m4a and mp4.
        :type Container: str
        :param Md5: MD5 value of a video.
        :type Md5: str
        :param AudioStreamSet: Audio stream information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AudioStreamSet: list of MediaAudioStreamItem
        :param VideoStreamSet: Video stream information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type VideoStreamSet: list of MediaVideoStreamItem
        """
        self.OutputStorage = None
        self.Path = None
        self.Definition = None
        self.Bitrate = None
        self.Height = None
        self.Width = None
        self.Size = None
        self.Duration = None
        self.Container = None
        self.Md5 = None
        self.AudioStreamSet = None
        self.VideoStreamSet = None


    def _deserialize(self, params):
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.Path = params.get("Path")
        self.Definition = params.get("Definition")
        self.Bitrate = params.get("Bitrate")
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.Size = params.get("Size")
        self.Duration = params.get("Duration")
        self.Container = params.get("Container")
        self.Md5 = params.get("Md5")
        if params.get("AudioStreamSet") is not None:
            self.AudioStreamSet = []
            for item in params.get("AudioStreamSet"):
                obj = MediaAudioStreamItem()
                obj._deserialize(item)
                self.AudioStreamSet.append(obj)
        if params.get("VideoStreamSet") is not None:
            self.VideoStreamSet = []
            for item in params.get("VideoStreamSet"):
                obj = MediaVideoStreamItem()
                obj._deserialize(item)
                self.VideoStreamSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaVideoStreamItem(AbstractModel):
    """Information of the video stream in a VOD file

    """

    def __init__(self):
        r"""
        :param Bitrate: Bitrate of a video stream in bps.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Bitrate: int
        :param Height: Height of a video stream in px.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Height: int
        :param Width: Width of a video stream in px.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Width: int
        :param Codec: Video stream codec, such as h264.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Codec: str
        :param Fps: Frame rate in Hz.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Fps: int
        :param ColorPrimaries: Color primaries
Note: this field may return `null`, indicating that no valid value was found.
        :type ColorPrimaries: str
        :param ColorSpace: Color space
Note: this field may return `null`, indicating that no valid value was found.
        :type ColorSpace: str
        :param ColorTransfer: Color transfer
Note: this field may return `null`, indicating that no valid value was found.
        :type ColorTransfer: str
        :param HdrType: HDR type
Note: This field may return `null`, indicating that no valid value was found.
        :type HdrType: str
        """
        self.Bitrate = None
        self.Height = None
        self.Width = None
        self.Codec = None
        self.Fps = None
        self.ColorPrimaries = None
        self.ColorSpace = None
        self.ColorTransfer = None
        self.HdrType = None


    def _deserialize(self, params):
        self.Bitrate = params.get("Bitrate")
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.Codec = params.get("Codec")
        self.Fps = params.get("Fps")
        self.ColorPrimaries = params.get("ColorPrimaries")
        self.ColorSpace = params.get("ColorSpace")
        self.ColorTransfer = params.get("ColorTransfer")
        self.HdrType = params.get("HdrType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAIAnalysisTemplateRequest(AbstractModel):
    """ModifyAIAnalysisTemplate request structure.

    """

    def __init__(self):
        r"""
        :param Definition: Unique ID of video content analysis template.
        :type Definition: int
        :param Name: Video content analysis template name. Length limit: 64 characters.
        :type Name: str
        :param Comment: Video content analysis template description. Length limit: 256 characters.
        :type Comment: str
        :param ClassificationConfigure: Control parameter of intelligent categorization task.
        :type ClassificationConfigure: :class:`tencentcloud.mps.v20190612.models.ClassificationConfigureInfoForUpdate`
        :param TagConfigure: Control parameter of intelligent tagging task.
        :type TagConfigure: :class:`tencentcloud.mps.v20190612.models.TagConfigureInfoForUpdate`
        :param CoverConfigure: Control parameter of intelligent cover generating task.
        :type CoverConfigure: :class:`tencentcloud.mps.v20190612.models.CoverConfigureInfoForUpdate`
        :param FrameTagConfigure: Control parameter of intelligent frame-specific tagging task.
        :type FrameTagConfigure: :class:`tencentcloud.mps.v20190612.models.FrameTagConfigureInfoForUpdate`
        """
        self.Definition = None
        self.Name = None
        self.Comment = None
        self.ClassificationConfigure = None
        self.TagConfigure = None
        self.CoverConfigure = None
        self.FrameTagConfigure = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("ClassificationConfigure") is not None:
            self.ClassificationConfigure = ClassificationConfigureInfoForUpdate()
            self.ClassificationConfigure._deserialize(params.get("ClassificationConfigure"))
        if params.get("TagConfigure") is not None:
            self.TagConfigure = TagConfigureInfoForUpdate()
            self.TagConfigure._deserialize(params.get("TagConfigure"))
        if params.get("CoverConfigure") is not None:
            self.CoverConfigure = CoverConfigureInfoForUpdate()
            self.CoverConfigure._deserialize(params.get("CoverConfigure"))
        if params.get("FrameTagConfigure") is not None:
            self.FrameTagConfigure = FrameTagConfigureInfoForUpdate()
            self.FrameTagConfigure._deserialize(params.get("FrameTagConfigure"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAIAnalysisTemplateResponse(AbstractModel):
    """ModifyAIAnalysisTemplate response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAIRecognitionTemplateRequest(AbstractModel):
    """ModifyAIRecognitionTemplate request structure.

    """

    def __init__(self):
        r"""
        :param Definition: Unique ID of a video content recognition template.
        :type Definition: int
        :param Name: Name of a video content recognition template. Length limit: 64 characters.
        :type Name: str
        :param Comment: Description of a video content recognition template. Length limit: 256 characters.
        :type Comment: str
        :param FaceConfigure: Face recognition control parameter.
        :type FaceConfigure: :class:`tencentcloud.mps.v20190612.models.FaceConfigureInfoForUpdate`
        :param OcrFullTextConfigure: Full text recognition control parameter.
        :type OcrFullTextConfigure: :class:`tencentcloud.mps.v20190612.models.OcrFullTextConfigureInfoForUpdate`
        :param OcrWordsConfigure: Text keyword recognition control parameter.
        :type OcrWordsConfigure: :class:`tencentcloud.mps.v20190612.models.OcrWordsConfigureInfoForUpdate`
        :param AsrFullTextConfigure: Full speech recognition control parameter.
        :type AsrFullTextConfigure: :class:`tencentcloud.mps.v20190612.models.AsrFullTextConfigureInfoForUpdate`
        :param AsrWordsConfigure: Speech keyword recognition control parameter.
        :type AsrWordsConfigure: :class:`tencentcloud.mps.v20190612.models.AsrWordsConfigureInfoForUpdate`
        """
        self.Definition = None
        self.Name = None
        self.Comment = None
        self.FaceConfigure = None
        self.OcrFullTextConfigure = None
        self.OcrWordsConfigure = None
        self.AsrFullTextConfigure = None
        self.AsrWordsConfigure = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("FaceConfigure") is not None:
            self.FaceConfigure = FaceConfigureInfoForUpdate()
            self.FaceConfigure._deserialize(params.get("FaceConfigure"))
        if params.get("OcrFullTextConfigure") is not None:
            self.OcrFullTextConfigure = OcrFullTextConfigureInfoForUpdate()
            self.OcrFullTextConfigure._deserialize(params.get("OcrFullTextConfigure"))
        if params.get("OcrWordsConfigure") is not None:
            self.OcrWordsConfigure = OcrWordsConfigureInfoForUpdate()
            self.OcrWordsConfigure._deserialize(params.get("OcrWordsConfigure"))
        if params.get("AsrFullTextConfigure") is not None:
            self.AsrFullTextConfigure = AsrFullTextConfigureInfoForUpdate()
            self.AsrFullTextConfigure._deserialize(params.get("AsrFullTextConfigure"))
        if params.get("AsrWordsConfigure") is not None:
            self.AsrWordsConfigure = AsrWordsConfigureInfoForUpdate()
            self.AsrWordsConfigure._deserialize(params.get("AsrWordsConfigure"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAIRecognitionTemplateResponse(AbstractModel):
    """ModifyAIRecognitionTemplate response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAdaptiveDynamicStreamingTemplateRequest(AbstractModel):
    """ModifyAdaptiveDynamicStreamingTemplate request structure.

    """

    def __init__(self):
        r"""
        :param Definition: Unique ID of an adaptive bitrate streaming template.
        :type Definition: int
        :param Name: Template name. Length limit: 64 characters.
        :type Name: str
        :param Format: Adaptive bitrate streaming format. Valid values:
<li>HLS,</li>
<li>MPEG-DASH.</li>
        :type Format: str
        :param DisableHigherVideoBitrate: Whether to prohibit transcoding from low bitrate to high bitrate. Valid values:
<li>0: no,</li>
<li>1: yes.</li>
        :type DisableHigherVideoBitrate: int
        :param DisableHigherVideoResolution: Whether to prohibit transcoding from low resolution to high resolution. Valid values:
<li>0: no,</li>
<li>1: yes.</li>
        :type DisableHigherVideoResolution: int
        :param StreamInfos: Parameter information of input streams for transcoding to adaptive bitrate streaming. Up to 10 streams can be input.
Note: the frame rate of each stream must be consistent; otherwise, the frame rate of the first stream is used as the output frame rate.
        :type StreamInfos: list of AdaptiveStreamTemplate
        :param Comment: Template description. Length limit: 256 characters.
        :type Comment: str
        """
        self.Definition = None
        self.Name = None
        self.Format = None
        self.DisableHigherVideoBitrate = None
        self.DisableHigherVideoResolution = None
        self.StreamInfos = None
        self.Comment = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Format = params.get("Format")
        self.DisableHigherVideoBitrate = params.get("DisableHigherVideoBitrate")
        self.DisableHigherVideoResolution = params.get("DisableHigherVideoResolution")
        if params.get("StreamInfos") is not None:
            self.StreamInfos = []
            for item in params.get("StreamInfos"):
                obj = AdaptiveStreamTemplate()
                obj._deserialize(item)
                self.StreamInfos.append(obj)
        self.Comment = params.get("Comment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAdaptiveDynamicStreamingTemplateResponse(AbstractModel):
    """ModifyAdaptiveDynamicStreamingTemplate response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAnimatedGraphicsTemplateRequest(AbstractModel):
    """ModifyAnimatedGraphicsTemplate request structure.

    """

    def __init__(self):
        r"""
        :param Definition: Unique ID of an animated image generating template.
        :type Definition: int
        :param Name: Name of an animated image generating template. Length limit: 64 characters.
        :type Name: str
        :param Width: Maximum value of the width (or long side) of an animated image in px. Value range: 0 and [128, 4,096].
<li>If both `Width` and `Height` are 0, the resolution will be the same as that of the source video;</li>
<li>If `Width` is 0, but `Height` is not 0, `Width` will be proportionally scaled;</li>
<li>If `Width` is not 0, but `Height` is 0, `Height` will be proportionally scaled;</li>
<li>If both `Width` and `Height` are not 0, the custom resolution will be used.</li>
Default value: 0.
        :type Width: int
        :param Height: Maximum value of the height (or short side) of a video stream in px. Value range: 0 and [128, 4,096].
<li>If both `Width` and `Height` are 0, the resolution will be the same as that of the source video;</li>
<li>If `Width` is 0, but `Height` is not 0, `Width` will be proportionally scaled;</li>
<li>If `Width` is not 0, but `Height` is 0, `Height` will be proportionally scaled;</li>
<li>If both `Width` and `Height` are not 0, the custom resolution will be used.</li>
Default value: 0.
        :type Height: int
        :param ResolutionAdaptive: Resolution adaption. Valid values:
<li>open: enabled. In this case, `Width` represents the long side of a video, while `Height` the short side;</li>
<li>close: disabled. In this case, `Width` represents the width of a video, while `Height` the height.</li>
Default value: open.
        :type ResolutionAdaptive: str
        :param Format: Animated image format. Valid values: gif, webp.
        :type Format: str
        :param Fps: Video frame rate in Hz. Value range: [1, 30].
        :type Fps: int
        :param Quality: Image quality. Value range: [1, 100]. Default value: 75.
        :type Quality: float
        :param Comment: Template description. Length limit: 256 characters.
        :type Comment: str
        """
        self.Definition = None
        self.Name = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.Format = None
        self.Fps = None
        self.Quality = None
        self.Comment = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Format = params.get("Format")
        self.Fps = params.get("Fps")
        self.Quality = params.get("Quality")
        self.Comment = params.get("Comment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAnimatedGraphicsTemplateResponse(AbstractModel):
    """ModifyAnimatedGraphicsTemplate response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyContentReviewTemplateRequest(AbstractModel):
    """ModifyContentReviewTemplate request structure.

    """

    def __init__(self):
        r"""
        :param Definition: Unique ID of an intelligent content recognition template
        :type Definition: int
        :param Name: Name of an intelligent content recognition template. Length limit: 64 characters
        :type Name: str
        :param Comment: Description of an intelligent content recognition template. Length limit: 256 characters
        :type Comment: str
        :param PornConfigure: Control parameter for porn information
        :type PornConfigure: :class:`tencentcloud.mps.v20190612.models.PornConfigureInfoForUpdate`
        :param TerrorismConfigure: Control parameter for terrorism information
        :type TerrorismConfigure: :class:`tencentcloud.mps.v20190612.models.TerrorismConfigureInfoForUpdate`
        :param PoliticalConfigure: Control parameter for politically sensitive information
        :type PoliticalConfigure: :class:`tencentcloud.mps.v20190612.models.PoliticalConfigureInfoForUpdate`
        :param ProhibitedConfigure: Control parameter of prohibited information detection. Prohibited information includes:
<li>Abusive;</li>
<li>Drug-related.</li>
Note: this parameter is not supported yet.
        :type ProhibitedConfigure: :class:`tencentcloud.mps.v20190612.models.ProhibitedConfigureInfoForUpdate`
        :param UserDefineConfigure: Control parameter for custom intelligent content recognition tasks
        :type UserDefineConfigure: :class:`tencentcloud.mps.v20190612.models.UserDefineConfigureInfoForUpdate`
        """
        self.Definition = None
        self.Name = None
        self.Comment = None
        self.PornConfigure = None
        self.TerrorismConfigure = None
        self.PoliticalConfigure = None
        self.ProhibitedConfigure = None
        self.UserDefineConfigure = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("PornConfigure") is not None:
            self.PornConfigure = PornConfigureInfoForUpdate()
            self.PornConfigure._deserialize(params.get("PornConfigure"))
        if params.get("TerrorismConfigure") is not None:
            self.TerrorismConfigure = TerrorismConfigureInfoForUpdate()
            self.TerrorismConfigure._deserialize(params.get("TerrorismConfigure"))
        if params.get("PoliticalConfigure") is not None:
            self.PoliticalConfigure = PoliticalConfigureInfoForUpdate()
            self.PoliticalConfigure._deserialize(params.get("PoliticalConfigure"))
        if params.get("ProhibitedConfigure") is not None:
            self.ProhibitedConfigure = ProhibitedConfigureInfoForUpdate()
            self.ProhibitedConfigure._deserialize(params.get("ProhibitedConfigure"))
        if params.get("UserDefineConfigure") is not None:
            self.UserDefineConfigure = UserDefineConfigureInfoForUpdate()
            self.UserDefineConfigure._deserialize(params.get("UserDefineConfigure"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyContentReviewTemplateResponse(AbstractModel):
    """ModifyContentReviewTemplate response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyImageSpriteTemplateRequest(AbstractModel):
    """ModifyImageSpriteTemplate request structure.

    """

    def __init__(self):
        r"""
        :param Definition: Unique ID of an image sprite generating template.
        :type Definition: int
        :param Name: Name of an image sprite generating template. Length limit: 64 characters.
        :type Name: str
        :param Width: Subimage width of an image sprite in px. Value range: [128, 4,096].
        :type Width: int
        :param Height: Subimage height of an image sprite in px. Value range: [128, 4,096].
        :type Height: int
        :param ResolutionAdaptive: Resolution adaption. Valid values:
<li>open: enabled. In this case, `Width` represents the long side of a video, while `Height` the short side;</li>
<li>close: disabled. In this case, `Width` represents the width of a video, while `Height` the height.</li>
Default value: open.
        :type ResolutionAdaptive: str
        :param SampleType: Sampling type. Valid values:
<li>Percent: By percent.</li>
<li>Time: By time interval.</li>
        :type SampleType: str
        :param SampleInterval: Sampling interval.
<li>If `SampleType` is `Percent`, sampling will be performed at an interval of the specified percentage.</li>
<li>If `SampleType` is `Time`, sampling will be performed at the specified time interval in seconds.</li>
        :type SampleInterval: int
        :param RowCount: Subimage row count of an image sprite.
        :type RowCount: int
        :param ColumnCount: Subimage column count of an image sprite.
        :type ColumnCount: int
        :param FillType: Fill type. "Fill" refers to the way of processing a screenshot when its aspect ratio is different from that of the source video. The following fill types are supported:
<li> stretch: stretch. The screenshot will be stretched frame by frame to match the aspect ratio of the source video, which may make the screenshot "shorter" or "longer";</li>
<li>black: fill with black. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with black color blocks.</li>
Default value: black.
        :type FillType: str
        :param Comment: Template description. Length limit: 256 characters.
        :type Comment: str
        """
        self.Definition = None
        self.Name = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.SampleType = None
        self.SampleInterval = None
        self.RowCount = None
        self.ColumnCount = None
        self.FillType = None
        self.Comment = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.SampleType = params.get("SampleType")
        self.SampleInterval = params.get("SampleInterval")
        self.RowCount = params.get("RowCount")
        self.ColumnCount = params.get("ColumnCount")
        self.FillType = params.get("FillType")
        self.Comment = params.get("Comment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyImageSpriteTemplateResponse(AbstractModel):
    """ModifyImageSpriteTemplate response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyPersonSampleRequest(AbstractModel):
    """ModifyPersonSample request structure.

    """

    def __init__(self):
        r"""
        :param PersonId: Image ID
        :type PersonId: str
        :param Name: Name. Length limit: 128 characters.
        :type Name: str
        :param Description: Description. Length limit: 1,024 characters.
        :type Description: str
        :param Usages: Image usage. Valid values:
1. Recognition: used for content recognition; equivalent to `Recognition.Face`
2. Review: used for inappropriate information recognition; equivalent to `Review.Face`
3. All: used for content recognition and inappropriate information recognition; equivalent to 1+2
        :type Usages: list of str
        :param FaceOperationInfo: Information of operations on facial features
        :type FaceOperationInfo: :class:`tencentcloud.mps.v20190612.models.AiSampleFaceOperation`
        :param TagOperationInfo: Tag operation information.
        :type TagOperationInfo: :class:`tencentcloud.mps.v20190612.models.AiSampleTagOperation`
        """
        self.PersonId = None
        self.Name = None
        self.Description = None
        self.Usages = None
        self.FaceOperationInfo = None
        self.TagOperationInfo = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.Usages = params.get("Usages")
        if params.get("FaceOperationInfo") is not None:
            self.FaceOperationInfo = AiSampleFaceOperation()
            self.FaceOperationInfo._deserialize(params.get("FaceOperationInfo"))
        if params.get("TagOperationInfo") is not None:
            self.TagOperationInfo = AiSampleTagOperation()
            self.TagOperationInfo._deserialize(params.get("TagOperationInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPersonSampleResponse(AbstractModel):
    """ModifyPersonSample response structure.

    """

    def __init__(self):
        r"""
        :param Person: Image information
        :type Person: :class:`tencentcloud.mps.v20190612.models.AiSamplePerson`
        :param FailFaceInfoSet: Information of images that failed the verification by facial feature positioning.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type FailFaceInfoSet: list of AiSampleFailFaceInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Person = None
        self.FailFaceInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Person") is not None:
            self.Person = AiSamplePerson()
            self.Person._deserialize(params.get("Person"))
        if params.get("FailFaceInfoSet") is not None:
            self.FailFaceInfoSet = []
            for item in params.get("FailFaceInfoSet"):
                obj = AiSampleFailFaceInfo()
                obj._deserialize(item)
                self.FailFaceInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class ModifySampleSnapshotTemplateRequest(AbstractModel):
    """ModifySampleSnapshotTemplate request structure.

    """

    def __init__(self):
        r"""
        :param Definition: Unique ID of a sampled screencapturing template.
        :type Definition: int
        :param Name: Name of a sampled screencapturing template. Length limit: 64 characters.
        :type Name: str
        :param Width: Image width in px. Value range: [128, 4,096].
        :type Width: int
        :param Height: Image height in px. Value range: [128, 4,096].
        :type Height: int
        :param ResolutionAdaptive: Resolution adaption. Valid values:
<li>open: enabled. In this case, `Width` represents the long side of a video, while `Height` the short side;</li>
<li>close: disabled. In this case, `Width` represents the width of a video, while `Height` the height.</li>
Default value: open.
        :type ResolutionAdaptive: str
        :param SampleType: Sampled screencapturing type. Valid values:
<li>Percent: By percent.</li>
<li>Time: By time interval.</li>
        :type SampleType: str
        :param SampleInterval: Sampling interval.
<li>If `SampleType` is `Percent`, sampling will be performed at an interval of the specified percentage.</li>
<li>If `SampleType` is `Time`, sampling will be performed at the specified time interval in seconds.</li>
        :type SampleInterval: int
        :param Format: Image format. Valid values: jpg; png.
        :type Format: str
        :param Comment: Template description. Length limit: 256 characters.
        :type Comment: str
        :param FillType: Fill type. "Fill" refers to the way of processing a screenshot when its aspect ratio is different from that of the source video. The following fill types are supported:
<li> stretch: stretch. The screenshot will be stretched frame by frame to match the aspect ratio of the source video, which may make the screenshot "shorter" or "longer";</li>
<li>black: fill with black. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with black color blocks.</li>
<li>white: fill with white. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with white color blocks.</li>
<li>gauss: fill with Gaussian blur. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with Gaussian blur.</li>
Default value: black.
        :type FillType: str
        """
        self.Definition = None
        self.Name = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.SampleType = None
        self.SampleInterval = None
        self.Format = None
        self.Comment = None
        self.FillType = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.SampleType = params.get("SampleType")
        self.SampleInterval = params.get("SampleInterval")
        self.Format = params.get("Format")
        self.Comment = params.get("Comment")
        self.FillType = params.get("FillType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySampleSnapshotTemplateResponse(AbstractModel):
    """ModifySampleSnapshotTemplate response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySnapshotByTimeOffsetTemplateRequest(AbstractModel):
    """ModifySnapshotByTimeOffsetTemplate request structure.

    """

    def __init__(self):
        r"""
        :param Definition: Unique ID of a time point screencapturing template.
        :type Definition: int
        :param Name: Name of a time point screencapturing template. Length limit: 64 characters.
        :type Name: str
        :param Width: Image width in px. Value range: [128, 4,096].
        :type Width: int
        :param Height: Image height in px. Value range: [128, 4,096].
        :type Height: int
        :param ResolutionAdaptive: Resolution adaption. Valid values:
<li>open: enabled. In this case, `Width` represents the long side of a video, while `Height` the short side;</li>
<li>close: disabled. In this case, `Width` represents the width of a video, while `Height` the height.</li>
Default value: open.
        :type ResolutionAdaptive: str
        :param Format: Image format. Valid values: jpg, png.
        :type Format: str
        :param Comment: Template description. Length limit: 256 characters.
        :type Comment: str
        :param FillType: Fill type. "Fill" refers to the way of processing a screenshot when its aspect ratio is different from that of the source video. The following fill types are supported:
<li> stretch: stretch. The screenshot will be stretched frame by frame to match the aspect ratio of the source video, which may make the screenshot "shorter" or "longer";</li>
<li>black: fill with black. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with black color blocks.</li>
<li>white: fill with white. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with white color blocks.</li>
<li>gauss: fill with Gaussian blur. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with Gaussian blur.</li>
Default value: black.
        :type FillType: str
        """
        self.Definition = None
        self.Name = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.Format = None
        self.Comment = None
        self.FillType = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Format = params.get("Format")
        self.Comment = params.get("Comment")
        self.FillType = params.get("FillType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySnapshotByTimeOffsetTemplateResponse(AbstractModel):
    """ModifySnapshotByTimeOffsetTemplate response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTranscodeTemplateRequest(AbstractModel):
    """ModifyTranscodeTemplate request structure.

    """

    def __init__(self):
        r"""
        :param Definition: Unique ID of a transcoding template.
        :type Definition: int
        :param Container: Container format. Valid values: mp4; flv; hls; mp3; flac; ogg; m4a. Among them, mp3, flac, ogg, and m4a are for audio files.
        :type Container: str
        :param Name: Name of a transcoding template. Length limit: 64 characters.
        :type Name: str
        :param Comment: Template description. Length limit: 256 characters.
        :type Comment: str
        :param RemoveVideo: Whether to remove video data. Valid values:
<li>0: Retain</li>
<li>1: Remove</li>
        :type RemoveVideo: int
        :param RemoveAudio: Whether to remove audio data. Valid values:
<li>0: Retain</li>
<li>1: Remove</li>
        :type RemoveAudio: int
        :param VideoTemplate: Video stream configuration parameter.
        :type VideoTemplate: :class:`tencentcloud.mps.v20190612.models.VideoTemplateInfoForUpdate`
        :param AudioTemplate: Audio stream configuration parameter.
        :type AudioTemplate: :class:`tencentcloud.mps.v20190612.models.AudioTemplateInfoForUpdate`
        :param TEHDConfig: TESHD transcoding parameter. To enable it, please contact your Tencent Cloud sales rep.
        :type TEHDConfig: :class:`tencentcloud.mps.v20190612.models.TEHDConfigForUpdate`
        """
        self.Definition = None
        self.Container = None
        self.Name = None
        self.Comment = None
        self.RemoveVideo = None
        self.RemoveAudio = None
        self.VideoTemplate = None
        self.AudioTemplate = None
        self.TEHDConfig = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Container = params.get("Container")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.RemoveVideo = params.get("RemoveVideo")
        self.RemoveAudio = params.get("RemoveAudio")
        if params.get("VideoTemplate") is not None:
            self.VideoTemplate = VideoTemplateInfoForUpdate()
            self.VideoTemplate._deserialize(params.get("VideoTemplate"))
        if params.get("AudioTemplate") is not None:
            self.AudioTemplate = AudioTemplateInfoForUpdate()
            self.AudioTemplate._deserialize(params.get("AudioTemplate"))
        if params.get("TEHDConfig") is not None:
            self.TEHDConfig = TEHDConfigForUpdate()
            self.TEHDConfig._deserialize(params.get("TEHDConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTranscodeTemplateResponse(AbstractModel):
    """ModifyTranscodeTemplate response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyWatermarkTemplateRequest(AbstractModel):
    """ModifyWatermarkTemplate request structure.

    """

    def __init__(self):
        r"""
        :param Definition: Unique ID of a watermarking template.
        :type Definition: int
        :param Name: Watermarking template name. Length limit: 64 characters.
        :type Name: str
        :param Comment: Template description. Length limit: 256 characters.
        :type Comment: str
        :param CoordinateOrigin: Origin position. Valid values:
<li>TopLeft: The origin of coordinates is in the top-left corner of the video, and the origin of the watermark is in the top-left corner of the image or text;</li>
<li>TopRight: The origin of coordinates is in the top-right corner of the video, and the origin of the watermark is in the top-right corner of the image or text;</li>
<li>BottomLeft: The origin of coordinates is in the bottom-left corner of the video, and the origin of the watermark is in the bottom-left corner of the image or text;</li>
<li>BottomRight: The origin of coordinates is in the bottom-right corner of the video, and the origin of the watermark is in the bottom-right corner of the image or text.</li>
        :type CoordinateOrigin: str
        :param XPos: The horizontal position of the origin of the watermark relative to the origin of coordinates of the video. % and px formats are supported:
<li>If the string ends in %, the `XPos` of the watermark will be the specified percentage of the video width; for example, `10%` means that `XPos` is 10% of the video width;</li>
<li>If the string ends in px, the `XPos` of the watermark will be the specified px; for example, `100px` means that `XPos` is 100 px.</li>
        :type XPos: str
        :param YPos: The vertical position of the origin of the watermark relative to the origin of coordinates of the video. % and px formats are supported:
<li>If the string ends in %, the `YPos` of the watermark will be the specified percentage of the video height; for example, `10%` means that `YPos` is 10% of the video height;</li>
<li>If the string ends in px, the `YPos` of the watermark will be the specified px; for example, `100px` means that `YPos` is 100 px.</li>
        :type YPos: str
        :param ImageTemplate: Image watermarking template. This field is valid only for image watermarking templates.
        :type ImageTemplate: :class:`tencentcloud.mps.v20190612.models.ImageWatermarkInputForUpdate`
        :param TextTemplate: Text watermarking template. This field is valid only for text watermarking templates.
        :type TextTemplate: :class:`tencentcloud.mps.v20190612.models.TextWatermarkTemplateInputForUpdate`
        :param SvgTemplate: SVG watermarking template. This field is required when `Type` is `svg` and is invalid when `Type` is `image` or `text`.
        :type SvgTemplate: :class:`tencentcloud.mps.v20190612.models.SvgWatermarkInputForUpdate`
        """
        self.Definition = None
        self.Name = None
        self.Comment = None
        self.CoordinateOrigin = None
        self.XPos = None
        self.YPos = None
        self.ImageTemplate = None
        self.TextTemplate = None
        self.SvgTemplate = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.CoordinateOrigin = params.get("CoordinateOrigin")
        self.XPos = params.get("XPos")
        self.YPos = params.get("YPos")
        if params.get("ImageTemplate") is not None:
            self.ImageTemplate = ImageWatermarkInputForUpdate()
            self.ImageTemplate._deserialize(params.get("ImageTemplate"))
        if params.get("TextTemplate") is not None:
            self.TextTemplate = TextWatermarkTemplateInputForUpdate()
            self.TextTemplate._deserialize(params.get("TextTemplate"))
        if params.get("SvgTemplate") is not None:
            self.SvgTemplate = SvgWatermarkInputForUpdate()
            self.SvgTemplate._deserialize(params.get("SvgTemplate"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyWatermarkTemplateResponse(AbstractModel):
    """ModifyWatermarkTemplate response structure.

    """

    def __init__(self):
        r"""
        :param ImageUrl: Image watermark address. This field is valid only when `ImageTemplate.ImageContent` is non-empty.
        :type ImageUrl: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ImageUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ImageUrl = params.get("ImageUrl")
        self.RequestId = params.get("RequestId")


class ModifyWordSampleRequest(AbstractModel):
    """ModifyWordSample request structure.

    """

    def __init__(self):
        r"""
        :param Keyword: Keyword. Length limit: 128 characters.
        :type Keyword: str
        :param Usages: <b>Keyword usage. Valid values:</b>
1. Recognition.Ocr: OCR-based content recognition
2. Recognition.Asr: ASR-based content recognition
3. Review.Ocr: OCR-based inappropriate information recognition
4. Review.Asr: ASR-based inappropriate information recognition
<b>Valid values can also be:</b>
5. Recognition: ASR- and OCR-based content recognition; equivalent to 1+2
6. Review: ASR- and OCR-based inappropriate information recognition; equivalent to 3+4
7. All: equivalent to 1+2+3+4
        :type Usages: list of str
        :param TagOperationInfo: Tag operation information.
        :type TagOperationInfo: :class:`tencentcloud.mps.v20190612.models.AiSampleTagOperation`
        """
        self.Keyword = None
        self.Usages = None
        self.TagOperationInfo = None


    def _deserialize(self, params):
        self.Keyword = params.get("Keyword")
        self.Usages = params.get("Usages")
        if params.get("TagOperationInfo") is not None:
            self.TagOperationInfo = AiSampleTagOperation()
            self.TagOperationInfo._deserialize(params.get("TagOperationInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyWordSampleResponse(AbstractModel):
    """ModifyWordSample response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class MosaicInput(AbstractModel):
    """Blur parameter type of video processing task

    """

    def __init__(self):
        r"""
        :param CoordinateOrigin: Origin position, which currently can only be:
<li>TopLeft: the origin of coordinates is in the top-left corner of the video, and the origin of the blur is in the top-left corner of the image or text.</li>
Default value: TopLeft.
        :type CoordinateOrigin: str
        :param XPos: The horizontal position of the origin of the blur relative to the origin of coordinates of the video. % and px formats are supported:
<li>If the string ends in %, the `XPos` of the blur will be the specified percentage of the video width; for example, `10%` means that `XPos` is 10% of the video width;</li>
<li>If the string ends in px, the `XPos` of the blur will be the specified px; for example, `100px` means that `XPos` is 100 px.</li>
Default value: 0 px.
        :type XPos: str
        :param YPos: Vertical position of the origin of blur relative to the origin of coordinates of video. % and px formats are supported:
<li>If the string ends in %, the `YPos` of the blur will be the specified percentage of the video height; for example, `10%` means that `YPos` is 10% of the video height;</li>
<li>If the string ends in px, the `YPos` of the blur will be the specified px; for example, `100px` means that `YPos` is 100 px.</li>
Default value: 0 px.
        :type YPos: str
        :param Width: Blur width. % and px formats are supported:
<li>If the string ends in %, the `Width` of the blur will be the specified percentage of the video width; for example, `10%` means that `Width` is 10% of the video width;</li>
<li>If the string ends in px, the `Width` of the blur will be in px; for example, `100px` means that `Width` is 100 px.</li>
Default value: 10%.
        :type Width: str
        :param Height: Blur height. % and px formats are supported:
<li>If the string ends in %, the `Height` of the blur will be the specified percentage of the video height; for example, `10%` means that `Height` is 10% of the video height;</li>
<li>If the string ends in px, the `Height` of the blur will be in px; for example, `100px` means that `Height` is 100 px.</li>
Default value: 10%.
        :type Height: str
        :param StartTimeOffset: Start time offset of blur in seconds. If this parameter is left empty or 0 is entered, the blur will appear upon the first video frame.
<li>If this parameter is left empty or 0 is entered, the blur will appear upon the first video frame;</li>
<li>If this value is greater than 0 (e.g., n), the blur will appear at second n after the first video frame;</li>
<li>If this value is smaller than 0 (e.g., -n), the blur will appear at second n before the last video frame.</li>
        :type StartTimeOffset: float
        :param EndTimeOffset: End time offset of blur in seconds.
<li>If this parameter is left empty or 0 is entered, the blur will exist till the last video frame;</li>
<li>If this value is greater than 0 (e.g., n), the blur will exist till second n;</li>
<li>If this value is smaller than 0 (e.g., -n), the blur will exist till second n before the last video frame.</li>
        :type EndTimeOffset: float
        """
        self.CoordinateOrigin = None
        self.XPos = None
        self.YPos = None
        self.Width = None
        self.Height = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None


    def _deserialize(self, params):
        self.CoordinateOrigin = params.get("CoordinateOrigin")
        self.XPos = params.get("XPos")
        self.YPos = params.get("YPos")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NumberFormat(AbstractModel):
    """Rule of the `{number}` variable in the output file name.

    """

    def __init__(self):
        r"""
        :param InitialValue: Start value of the `{number}` variable. Default value: 0.
        :type InitialValue: int
        :param Increment: Increment of the `{number}` variable. Default value: 1.
        :type Increment: int
        :param MinLength: Minimum length of the `{number}` variable. A placeholder will be used if the variable length is below the minimum requirement. Default value: 1.
        :type MinLength: int
        :param PlaceHolder: Placeholder used when the `{number}` variable length is below the minimum requirement. Default value: 0.
        :type PlaceHolder: str
        """
        self.InitialValue = None
        self.Increment = None
        self.MinLength = None
        self.PlaceHolder = None


    def _deserialize(self, params):
        self.InitialValue = params.get("InitialValue")
        self.Increment = params.get("Increment")
        self.MinLength = params.get("MinLength")
        self.PlaceHolder = params.get("PlaceHolder")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OcrFullTextConfigureInfo(AbstractModel):
    """Control parameter of a full text recognition task

    """

    def __init__(self):
        r"""
        :param Switch: Switch of a full text recognition task. Valid values:
<li>ON: Enables an intelligent full text recognition task;</li>
<li>OFF: Disables an intelligent full text recognition task.</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OcrFullTextConfigureInfoForUpdate(AbstractModel):
    """Control parameter of a full text recognition task

    """

    def __init__(self):
        r"""
        :param Switch: Switch of a full text recognition task. Valid values:
<li>ON: Enables an intelligent full text recognition task;</li>
<li>OFF: Disables an intelligent full text recognition task.</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OcrWordsConfigureInfo(AbstractModel):
    """Text keyword recognition control parameter.

    """

    def __init__(self):
        r"""
        :param Switch: Switch of a text keyword recognition task. Valid values:
<li>ON: Enables a text keyword recognition task;</li>
<li>OFF: Disables a text keyword recognition task.</li>
        :type Switch: str
        :param LabelSet: Keyword filter tag, which specifies the keyword tag that needs to be returned. If this parameter is left empty, all results will be returned.
There can be up to 10 tags, each with a length limit of 16 characters.
        :type LabelSet: list of str
        """
        self.Switch = None
        self.LabelSet = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OcrWordsConfigureInfoForUpdate(AbstractModel):
    """Text keyword recognition control parameter.

    """

    def __init__(self):
        r"""
        :param Switch: Switch of a text keyword recognition task. Valid values:
<li>ON: Enables a text keyword recognition task;</li>
<li>OFF: Disables a text keyword recognition task.</li>
        :type Switch: str
        :param LabelSet: Keyword filter tag, which specifies the keyword tag that needs to be returned. If this parameter is left empty, all results will be returned.
There can be up to 10 tags, each with a length limit of 16 characters.
        :type LabelSet: list of str
        """
        self.Switch = None
        self.LabelSet = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OverrideTranscodeParameter(AbstractModel):
    """Custom specification parameters for video processing, which are used to override corresponding parameters in templates.

    """

    def __init__(self):
        r"""
        :param Container: Container format. Valid values: mp4, flv, hls, mp3, flac, ogg, and m4a; mp3, flac, ogg, and m4a are formats of audio files.
        :type Container: str
        :param RemoveVideo: Whether to remove video data. Valid values:
<li>0: retain</li>
<li>1: remove</li>
        :type RemoveVideo: int
        :param RemoveAudio: Whether to remove audio data. Valid values:
<li>0: retain</li>
<li>1: remove</li>
        :type RemoveAudio: int
        :param VideoTemplate: Video stream configuration parameter.
        :type VideoTemplate: :class:`tencentcloud.mps.v20190612.models.VideoTemplateInfoForUpdate`
        :param AudioTemplate: Audio stream configuration parameter.
        :type AudioTemplate: :class:`tencentcloud.mps.v20190612.models.AudioTemplateInfoForUpdate`
        :param TEHDConfig: TESHD transcoding parameter.
        :type TEHDConfig: :class:`tencentcloud.mps.v20190612.models.TEHDConfigForUpdate`
        """
        self.Container = None
        self.RemoveVideo = None
        self.RemoveAudio = None
        self.VideoTemplate = None
        self.AudioTemplate = None
        self.TEHDConfig = None


    def _deserialize(self, params):
        self.Container = params.get("Container")
        self.RemoveVideo = params.get("RemoveVideo")
        self.RemoveAudio = params.get("RemoveAudio")
        if params.get("VideoTemplate") is not None:
            self.VideoTemplate = VideoTemplateInfoForUpdate()
            self.VideoTemplate._deserialize(params.get("VideoTemplate"))
        if params.get("AudioTemplate") is not None:
            self.AudioTemplate = AudioTemplateInfoForUpdate()
            self.AudioTemplate._deserialize(params.get("AudioTemplate"))
        if params.get("TEHDConfig") is not None:
            self.TEHDConfig = TEHDConfigForUpdate()
            self.TEHDConfig._deserialize(params.get("TEHDConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParseLiveStreamProcessNotificationRequest(AbstractModel):
    """ParseLiveStreamProcessNotification request structure.

    """

    def __init__(self):
        r"""
        :param Content: Live stream event notification obtained from CMQ.
        :type Content: str
        """
        self.Content = None


    def _deserialize(self, params):
        self.Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParseLiveStreamProcessNotificationResponse(AbstractModel):
    """ParseLiveStreamProcessNotification response structure.

    """

    def __init__(self):
        r"""
        :param NotificationType: Result type of live stream processing. Valid values:
<li>AiReviewResult: Content audit result;</li>
<li>ProcessEof: Live stream processing has been completed.</li>
        :type NotificationType: str
        :param TaskId: Video processing task ID.
        :type TaskId: str
        :param ProcessEofInfo: Information of a live stream processing error, which is valid when `NotificationType` is `ProcessEof`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProcessEofInfo: :class:`tencentcloud.mps.v20190612.models.LiveStreamProcessErrorInfo`
        :param AiReviewResultInfo: Content audit result, which is valid when `NotificationType` is `AiReviewResult`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AiReviewResultInfo: :class:`tencentcloud.mps.v20190612.models.LiveStreamAiReviewResultInfo`
        :param AiRecognitionResultInfo: Content recognition result, which is valid if `NotificationType` is `AiRecognitionResult`.
        :type AiRecognitionResultInfo: :class:`tencentcloud.mps.v20190612.models.LiveStreamAiRecognitionResultInfo`
        :param SessionId: The ID used for deduplication. If there was a request with the same ID in the last seven days, the current request will return an error. The ID can contain up to 50 characters. If this parameter is left empty or an empty string is entered, no deduplication will be performed.
        :type SessionId: str
        :param SessionContext: The source context which is used to pass through the user request information. The task flow status change callback will return the value of this field. It can contain up to 1,000 characters.
        :type SessionContext: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.NotificationType = None
        self.TaskId = None
        self.ProcessEofInfo = None
        self.AiReviewResultInfo = None
        self.AiRecognitionResultInfo = None
        self.SessionId = None
        self.SessionContext = None
        self.RequestId = None


    def _deserialize(self, params):
        self.NotificationType = params.get("NotificationType")
        self.TaskId = params.get("TaskId")
        if params.get("ProcessEofInfo") is not None:
            self.ProcessEofInfo = LiveStreamProcessErrorInfo()
            self.ProcessEofInfo._deserialize(params.get("ProcessEofInfo"))
        if params.get("AiReviewResultInfo") is not None:
            self.AiReviewResultInfo = LiveStreamAiReviewResultInfo()
            self.AiReviewResultInfo._deserialize(params.get("AiReviewResultInfo"))
        if params.get("AiRecognitionResultInfo") is not None:
            self.AiRecognitionResultInfo = LiveStreamAiRecognitionResultInfo()
            self.AiRecognitionResultInfo._deserialize(params.get("AiRecognitionResultInfo"))
        self.SessionId = params.get("SessionId")
        self.SessionContext = params.get("SessionContext")
        self.RequestId = params.get("RequestId")


class ParseNotificationRequest(AbstractModel):
    """ParseNotification request structure.

    """

    def __init__(self):
        r"""
        :param Content: Event notification obtained from CMQ.
        :type Content: str
        """
        self.Content = None


    def _deserialize(self, params):
        self.Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParseNotificationResponse(AbstractModel):
    """ParseNotification response structure.

    """

    def __init__(self):
        r"""
        :param EventType: Supported event type. Valid values:
<li>WorkflowTask: Video workflow processing task.</li>
        :type EventType: str
        :param WorkflowTaskEvent: Information of a video processing task. This field has a value only when `TaskType` is `WorkflowTask`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type WorkflowTaskEvent: :class:`tencentcloud.mps.v20190612.models.WorkflowTask`
        :param EditMediaTaskEvent: Video editing task information. This field has a value only when `TaskType` is `EditMediaTask`.
        :type EditMediaTaskEvent: :class:`tencentcloud.mps.v20190612.models.EditMediaTask`
        :param SessionId: The ID used for deduplication. If there was a request with the same ID in the last seven days, the current request will return an error. The ID can contain up to 50 characters. If this parameter is left empty or an empty string is entered, no deduplication will be performed.
        :type SessionId: str
        :param SessionContext: The source context which is used to pass through the user request information. The task flow status change callback will return the value of this field. It can contain up to 1,000 characters.
        :type SessionContext: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.EventType = None
        self.WorkflowTaskEvent = None
        self.EditMediaTaskEvent = None
        self.SessionId = None
        self.SessionContext = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EventType = params.get("EventType")
        if params.get("WorkflowTaskEvent") is not None:
            self.WorkflowTaskEvent = WorkflowTask()
            self.WorkflowTaskEvent._deserialize(params.get("WorkflowTaskEvent"))
        if params.get("EditMediaTaskEvent") is not None:
            self.EditMediaTaskEvent = EditMediaTask()
            self.EditMediaTaskEvent._deserialize(params.get("EditMediaTaskEvent"))
        self.SessionId = params.get("SessionId")
        self.SessionContext = params.get("SessionContext")
        self.RequestId = params.get("RequestId")


class PoliticalAsrReviewTemplateInfo(AbstractModel):
    """The parameters for detecting sensitive information based on ASR.

    """

    def __init__(self):
        r"""
        :param Switch: Whether to detect sensitive information based on ASR. Valid values:
<li>ON</li>
<li>OFF</li>
        :type Switch: str
        :param BlockConfidence: Threshold score for violation. If this score is reached or exceeded during intelligent audit, it will be deemed that a suspected violation has occurred. If this parameter is left empty, 100 will be used by default. Value range: 0-100.
        :type BlockConfidence: int
        :param ReviewConfidence: Threshold score for human audit. If this score is reached or exceeded during intelligent audit, human audit will be considered necessary. If this parameter is left empty, 75 will be used by default. Value range: 0-100.
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PoliticalAsrReviewTemplateInfoForUpdate(AbstractModel):
    """The parameters for detecting sensitive information based on ASR.

    """

    def __init__(self):
        r"""
        :param Switch: Whether to detect sensitive information based on ASR. Valid values:
<li>ON</li>
<li>OFF</li>
        :type Switch: str
        :param BlockConfidence: Threshold score for violation. If this score is reached or exceeded during intelligent audit, it will be deemed that a suspected violation has occurred. Value range: 0-100.
        :type BlockConfidence: int
        :param ReviewConfidence: Threshold score for human audit. If this score is reached or exceeded during intelligent audit, human audit will be considered necessary. Value range: 0-100.
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PoliticalConfigureInfo(AbstractModel):
    """The parameters for detecting sensitive information.

    """

    def __init__(self):
        r"""
        :param ImgReviewInfo: The parameters for detecting sensitive information in images.
        :type ImgReviewInfo: :class:`tencentcloud.mps.v20190612.models.PoliticalImgReviewTemplateInfo`
        :param AsrReviewInfo: The parameters for detecting sensitive information based on ASR.
        :type AsrReviewInfo: :class:`tencentcloud.mps.v20190612.models.PoliticalAsrReviewTemplateInfo`
        :param OcrReviewInfo: The parameters for detecting sensitive information based on OCR.
        :type OcrReviewInfo: :class:`tencentcloud.mps.v20190612.models.PoliticalOcrReviewTemplateInfo`
        """
        self.ImgReviewInfo = None
        self.AsrReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("ImgReviewInfo") is not None:
            self.ImgReviewInfo = PoliticalImgReviewTemplateInfo()
            self.ImgReviewInfo._deserialize(params.get("ImgReviewInfo"))
        if params.get("AsrReviewInfo") is not None:
            self.AsrReviewInfo = PoliticalAsrReviewTemplateInfo()
            self.AsrReviewInfo._deserialize(params.get("AsrReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = PoliticalOcrReviewTemplateInfo()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PoliticalConfigureInfoForUpdate(AbstractModel):
    """The parameters for detecting sensitive information.

    """

    def __init__(self):
        r"""
        :param ImgReviewInfo: The parameters for detecting sensitive information in images.
        :type ImgReviewInfo: :class:`tencentcloud.mps.v20190612.models.PoliticalImgReviewTemplateInfoForUpdate`
        :param AsrReviewInfo: The parameters for detecting sensitive information based on ASR.
        :type AsrReviewInfo: :class:`tencentcloud.mps.v20190612.models.PoliticalAsrReviewTemplateInfoForUpdate`
        :param OcrReviewInfo: The parameters for detecting sensitive information based on OCR.
        :type OcrReviewInfo: :class:`tencentcloud.mps.v20190612.models.PoliticalOcrReviewTemplateInfoForUpdate`
        """
        self.ImgReviewInfo = None
        self.AsrReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("ImgReviewInfo") is not None:
            self.ImgReviewInfo = PoliticalImgReviewTemplateInfoForUpdate()
            self.ImgReviewInfo._deserialize(params.get("ImgReviewInfo"))
        if params.get("AsrReviewInfo") is not None:
            self.AsrReviewInfo = PoliticalAsrReviewTemplateInfoForUpdate()
            self.AsrReviewInfo._deserialize(params.get("AsrReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = PoliticalOcrReviewTemplateInfoForUpdate()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PoliticalImgReviewTemplateInfo(AbstractModel):
    """The parameters for detecting sensitive information in images.

    """

    def __init__(self):
        r"""
        :param Switch: Whether to detect sensitive information in images. Valid values:
<li>ON</li>
<li>OFF</li>
        :type Switch: str
        :param LabelSet: The filter labels for sensitive information detection in images, which specify the types of sensitive information to return. If this parameter is left empty, the detection results for all labels are returned. Valid values:
<li>violation_photo (banned icons)</li>
<li>politician</li>
<li>entertainment (people in the entertainment industry)</li>
<li>sport (people in the sports industry)</li>
<li>entrepreneur</li>
<li>scholar</li>
<li>celebrity</li>
<li>military (people in military)</li>
        :type LabelSet: list of str
        :param BlockConfidence: Threshold score for violation. If this score is reached or exceeded during intelligent audit, it will be deemed that a suspected violation has occurred. If this parameter is left empty, 97 will be used by default. Value range: 0-100.
        :type BlockConfidence: int
        :param ReviewConfidence: Threshold score for human audit. If this score is reached or exceeded during intelligent audit, human audit will be considered necessary. If this parameter is left empty, 95 will be used by default. Value range: 0-100.
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PoliticalImgReviewTemplateInfoForUpdate(AbstractModel):
    """The parameters for detecting sensitive information in images.

    """

    def __init__(self):
        r"""
        :param Switch: Whether to detect sensitive information in images. Valid values:
<li>ON</li>
<li>OFF</li>
        :type Switch: str
        :param LabelSet: The filter labels for sensitive information detection in images, which specify the types of sensitive information to return. If this parameter is left empty, the detection results for all labels are returned. Valid values:
<li>violation_photo (banned icons)</li>
<li>politician</li>
<li>entertainment (people in the entertainment industry)</li>
<li>sport (people in the sports industry)</li>
<li>entrepreneur</li>
<li>scholar</li>
<li>celebrity</li>
<li>military (people in military)</li>
        :type LabelSet: list of str
        :param BlockConfidence: Threshold score for violation. If this score is reached or exceeded during intelligent audit, it will be deemed that a suspected violation has occurred. Value range: 0-100.
        :type BlockConfidence: int
        :param ReviewConfidence: Threshold score for human audit. If this score is reached or exceeded during intelligent audit, human audit will be considered necessary. Value range: 0-100.
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PoliticalOcrReviewTemplateInfo(AbstractModel):
    """The parameters for detecting sensitive information based on OCR.

    """

    def __init__(self):
        r"""
        :param Switch: Whether to detect sensitive information based on OCR. Valid values:
<li>ON</li>
<li>OFF</li>
        :type Switch: str
        :param BlockConfidence: Threshold score for violation. If this score is reached or exceeded during intelligent audit, it will be deemed that a suspected violation has occurred. If this parameter is left empty, 100 will be used by default. Value range: 0-100.
        :type BlockConfidence: int
        :param ReviewConfidence: Threshold score for human audit. If this score is reached or exceeded during intelligent audit, human audit will be considered necessary. If this parameter is left empty, 75 will be used by default. Value range: 0-100.
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PoliticalOcrReviewTemplateInfoForUpdate(AbstractModel):
    """The parameters for detecting sensitive information based on OCR.

    """

    def __init__(self):
        r"""
        :param Switch: Whether to detect sensitive information based on OCR. Valid values:
<li>ON</li>
<li>OFF</li>
        :type Switch: str
        :param BlockConfidence: Threshold score for violation. If this score is reached or exceeded during intelligent audit, it will be deemed that a suspected violation has occurred. Value range: 0-100.
        :type BlockConfidence: int
        :param ReviewConfidence: Threshold score for human audit. If this score is reached or exceeded during intelligent audit, human audit will be considered necessary. Value range: 0-100.
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PornAsrReviewTemplateInfo(AbstractModel):
    """Control parameter of a porn information detection in speech task

    """

    def __init__(self):
        r"""
        :param Switch: Switch of a porn information detection in speech task. Valid values:
<li>ON: Enables a porn information detection in speech task;</li>
<li>OFF: Disables a porn information detection in speech task.</li>
        :type Switch: str
        :param BlockConfidence: Threshold score for violation. If this score is reached or exceeded during intelligent audit, it will be deemed that a suspected violation has occurred. If this parameter is left empty, 100 will be used by default. Value range: 0-100.
        :type BlockConfidence: int
        :param ReviewConfidence: Threshold score for human audit. If this score is reached or exceeded during intelligent audit, human audit will be considered necessary. If this parameter is left empty, 75 will be used by default. Value range: 0-100.
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PornAsrReviewTemplateInfoForUpdate(AbstractModel):
    """Control parameter of a porn information detection in speech task.

    """

    def __init__(self):
        r"""
        :param Switch: Switch of a porn information detection in speech task. Valid values:
<li>ON: Enables a porn information detection in speech task;</li>
<li>OFF: Disables a porn information detection in speech task.</li>
        :type Switch: str
        :param BlockConfidence: Threshold score for violation. If this score is reached or exceeded during intelligent audit, it will be deemed that a suspected violation has occurred. Value range: 0-100.
        :type BlockConfidence: int
        :param ReviewConfidence: Threshold score for human audit. If this score is reached or exceeded during intelligent audit, human audit will be considered necessary. Value range: 0-100.
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PornConfigureInfo(AbstractModel):
    """Control parameter of a porn information detection task

    """

    def __init__(self):
        r"""
        :param ImgReviewInfo: Control parameter of porn information detection in image.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ImgReviewInfo: :class:`tencentcloud.mps.v20190612.models.PornImgReviewTemplateInfo`
        :param AsrReviewInfo: Control parameter of porn information detection in speech.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AsrReviewInfo: :class:`tencentcloud.mps.v20190612.models.PornAsrReviewTemplateInfo`
        :param OcrReviewInfo: Control parameter of porn information detection in text.
Note: This field may return null, indicating that no valid values can be obtained.
        :type OcrReviewInfo: :class:`tencentcloud.mps.v20190612.models.PornOcrReviewTemplateInfo`
        """
        self.ImgReviewInfo = None
        self.AsrReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("ImgReviewInfo") is not None:
            self.ImgReviewInfo = PornImgReviewTemplateInfo()
            self.ImgReviewInfo._deserialize(params.get("ImgReviewInfo"))
        if params.get("AsrReviewInfo") is not None:
            self.AsrReviewInfo = PornAsrReviewTemplateInfo()
            self.AsrReviewInfo._deserialize(params.get("AsrReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = PornOcrReviewTemplateInfo()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PornConfigureInfoForUpdate(AbstractModel):
    """Control parameter of a porn information detection task.

    """

    def __init__(self):
        r"""
        :param ImgReviewInfo: Control parameter of porn information detection in image.
        :type ImgReviewInfo: :class:`tencentcloud.mps.v20190612.models.PornImgReviewTemplateInfoForUpdate`
        :param AsrReviewInfo: Control parameter of porn information detection in speech.
        :type AsrReviewInfo: :class:`tencentcloud.mps.v20190612.models.PornAsrReviewTemplateInfoForUpdate`
        :param OcrReviewInfo: Control parameter of porn information detection in text.
        :type OcrReviewInfo: :class:`tencentcloud.mps.v20190612.models.PornOcrReviewTemplateInfoForUpdate`
        """
        self.ImgReviewInfo = None
        self.AsrReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("ImgReviewInfo") is not None:
            self.ImgReviewInfo = PornImgReviewTemplateInfoForUpdate()
            self.ImgReviewInfo._deserialize(params.get("ImgReviewInfo"))
        if params.get("AsrReviewInfo") is not None:
            self.AsrReviewInfo = PornAsrReviewTemplateInfoForUpdate()
            self.AsrReviewInfo._deserialize(params.get("AsrReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = PornOcrReviewTemplateInfoForUpdate()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PornImgReviewTemplateInfo(AbstractModel):
    """Control parameter of a porn information detection in image task

    """

    def __init__(self):
        r"""
        :param Switch: Switch of a porn information detection in image task. Valid values:
<li>ON: Enables a porn information detection in image task;</li>
<li>OFF: Disables a porn information detection in image task.</li>
        :type Switch: str
        :param LabelSet: Filter tag for porn information detection in image. If an audit result contains the selected tag, it will be returned; if the filter tag is empty, all audit results will be returned. Valid values:
<li>porn: Porn;</li>
<li>vulgar: Vulgarity;</li>
<li>intimacy: Intimacy;</li>
<li>sexy: Sexiness.</li>
        :type LabelSet: list of str
        :param BlockConfidence: Threshold score for violation. If this score is reached or exceeded during intelligent audit, it will be deemed that a suspected violation has occurred. If this parameter is left empty, 90 will be used by default. Value range: 0-100.
        :type BlockConfidence: int
        :param ReviewConfidence: Threshold score for human audit. If this score is reached or exceeded during intelligent audit, human audit will be considered necessary. If this parameter is left empty, 0 will be used by default. Value range: 0-100.
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PornImgReviewTemplateInfoForUpdate(AbstractModel):
    """Control parameter of a porn information detection in image task.

    """

    def __init__(self):
        r"""
        :param Switch: Switch of a porn information detection in image task. Valid values:
<li>ON: Enables a porn information detection in image task;</li>
<li>OFF: Disables a porn information detection in image task.</li>
        :type Switch: str
        :param LabelSet: Filter tag for porn information detection in image. If an audit result contains the selected tag, it will be returned; if the filter tag is empty, all audit results will be returned. Valid values:
<li>porn: Porn;</li>
<li>vulgar: Vulgarity;</li>
<li>intimacy: Intimacy;</li>
<li>sexy: Sexiness.</li>
        :type LabelSet: list of str
        :param BlockConfidence: Threshold score for violation. If this score is reached or exceeded during intelligent audit, it will be deemed that a suspected violation has occurred. Value range: 0-100.
        :type BlockConfidence: int
        :param ReviewConfidence: Threshold score for human audit. If this score is reached or exceeded during intelligent audit, human audit will be considered necessary. Value range: 0-100.
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PornOcrReviewTemplateInfo(AbstractModel):
    """Control parameter of a porn information detection in text task

    """

    def __init__(self):
        r"""
        :param Switch: Switch of a porn information detection in text task. Valid values:
<li>ON: Enables a porn information detection in text task;</li>
<li>OFF: Disables a porn information detection in text task.</li>
        :type Switch: str
        :param BlockConfidence: Threshold score for violation. If this score is reached or exceeded during intelligent audit, it will be deemed that a suspected violation has occurred. If this parameter is left empty, 100 will be used by default. Value range: 0-100.
        :type BlockConfidence: int
        :param ReviewConfidence: Threshold score for human audit. If this score is reached or exceeded during intelligent audit, human audit will be considered necessary. If this parameter is left empty, 75 will be used by default. Value range: 0-100.
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PornOcrReviewTemplateInfoForUpdate(AbstractModel):
    """Control parameter of a porn information detection in text task.

    """

    def __init__(self):
        r"""
        :param Switch: Switch of a porn information detection in text task. Valid values:
<li>ON: Enables a porn information detection in text task;</li>
<li>OFF: Disables a porn information detection in text task.</li>
        :type Switch: str
        :param BlockConfidence: Threshold score for violation. If this score is reached or exceeded during intelligent audit, it will be deemed that a suspected violation has occurred. Value range: 0-100.
        :type BlockConfidence: int
        :param ReviewConfidence: Threshold score for human audit. If this score is reached or exceeded during intelligent audit, human audit will be considered necessary. Value range: 0-100.
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProcessLiveStreamRequest(AbstractModel):
    """ProcessLiveStream request structure.

    """

    def __init__(self):
        r"""
        :param Url: Live stream URL, which must be a live stream file address. RTMP, HLS, and FLV are supported.
        :type Url: str
        :param TaskNotifyConfig: Event notification information of a task, which is used to specify the live stream processing result.
        :type TaskNotifyConfig: :class:`tencentcloud.mps.v20190612.models.LiveStreamTaskNotifyConfig`
        :param OutputStorage: Target bucket of a live stream processing output file. This parameter is required if a file will be output.
        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        :param OutputDir: Target directory of a live stream processing output file, such as `/movie/201909/`. If this parameter is left empty, the `/` directory will be used.
        :type OutputDir: str
        :param AiContentReviewTask: Type parameter of a video content audit task.
        :type AiContentReviewTask: :class:`tencentcloud.mps.v20190612.models.AiContentReviewTaskInput`
        :param AiRecognitionTask: Type parameter of video content recognition task.
        :type AiRecognitionTask: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskInput`
        :param SessionId: The ID used for deduplication. If there was a request with the same ID in the last seven days, the current request will return an error. The ID can contain up to 50 characters. If this parameter is left empty or an empty string is entered, no deduplication will be performed.
        :type SessionId: str
        :param SessionContext: The source context which is used to pass through the user request information. The task flow status change callback will return the value of this field. It can contain up to 1,000 characters.
        :type SessionContext: str
        """
        self.Url = None
        self.TaskNotifyConfig = None
        self.OutputStorage = None
        self.OutputDir = None
        self.AiContentReviewTask = None
        self.AiRecognitionTask = None
        self.SessionId = None
        self.SessionContext = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        if params.get("TaskNotifyConfig") is not None:
            self.TaskNotifyConfig = LiveStreamTaskNotifyConfig()
            self.TaskNotifyConfig._deserialize(params.get("TaskNotifyConfig"))
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.OutputDir = params.get("OutputDir")
        if params.get("AiContentReviewTask") is not None:
            self.AiContentReviewTask = AiContentReviewTaskInput()
            self.AiContentReviewTask._deserialize(params.get("AiContentReviewTask"))
        if params.get("AiRecognitionTask") is not None:
            self.AiRecognitionTask = AiRecognitionTaskInput()
            self.AiRecognitionTask._deserialize(params.get("AiRecognitionTask"))
        self.SessionId = params.get("SessionId")
        self.SessionContext = params.get("SessionContext")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProcessLiveStreamResponse(AbstractModel):
    """ProcessLiveStream response structure.

    """

    def __init__(self):
        r"""
        :param TaskId: Task ID
        :type TaskId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ProcessMediaRequest(AbstractModel):
    """ProcessMedia request structure.

    """

    def __init__(self):
        r"""
        :param InputInfo: Input information of a file for video processing.
        :type InputInfo: :class:`tencentcloud.mps.v20190612.models.MediaInputInfo`
        :param OutputStorage: Target bucket of a video processing output file. If this parameter is left empty, the storage location in `InputInfo` will be inherited.
        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        :param OutputDir: Target directory of a video processing output file, such as `/movie/201907/`. If this parameter is left empty, the file will be outputted to the same directory as that in `InputInfo`.
        :type OutputDir: str
        :param MediaProcessTask: Parameter of a video processing task.
        :type MediaProcessTask: :class:`tencentcloud.mps.v20190612.models.MediaProcessTaskInput`
        :param AiContentReviewTask: Type parameter of a video content audit task.
        :type AiContentReviewTask: :class:`tencentcloud.mps.v20190612.models.AiContentReviewTaskInput`
        :param AiAnalysisTask: Video content analysis task parameter.
        :type AiAnalysisTask: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskInput`
        :param AiRecognitionTask: Type parameter of a video content recognition task.
        :type AiRecognitionTask: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskInput`
        :param TaskNotifyConfig: Event notification information of a task. If this parameter is left empty, no event notifications will be obtained.
        :type TaskNotifyConfig: :class:`tencentcloud.mps.v20190612.models.TaskNotifyConfig`
        :param TasksPriority: Task flow priority. The higher the value, the higher the priority. Value range: [-10, 10]. If this parameter is left empty, 0 will be used.
        :type TasksPriority: int
        :param SessionId: The ID used for deduplication. If there was a request with the same ID in the last three days, the current request will return an error. The ID can contain up to 50 characters. If this parameter is left empty or an empty string is entered, no deduplication will be performed.
        :type SessionId: str
        :param SessionContext: The source context which is used to pass through the user request information. The task flow status change callback will return the value of this field. It can contain up to 1,000 characters.
        :type SessionContext: str
        """
        self.InputInfo = None
        self.OutputStorage = None
        self.OutputDir = None
        self.MediaProcessTask = None
        self.AiContentReviewTask = None
        self.AiAnalysisTask = None
        self.AiRecognitionTask = None
        self.TaskNotifyConfig = None
        self.TasksPriority = None
        self.SessionId = None
        self.SessionContext = None


    def _deserialize(self, params):
        if params.get("InputInfo") is not None:
            self.InputInfo = MediaInputInfo()
            self.InputInfo._deserialize(params.get("InputInfo"))
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.OutputDir = params.get("OutputDir")
        if params.get("MediaProcessTask") is not None:
            self.MediaProcessTask = MediaProcessTaskInput()
            self.MediaProcessTask._deserialize(params.get("MediaProcessTask"))
        if params.get("AiContentReviewTask") is not None:
            self.AiContentReviewTask = AiContentReviewTaskInput()
            self.AiContentReviewTask._deserialize(params.get("AiContentReviewTask"))
        if params.get("AiAnalysisTask") is not None:
            self.AiAnalysisTask = AiAnalysisTaskInput()
            self.AiAnalysisTask._deserialize(params.get("AiAnalysisTask"))
        if params.get("AiRecognitionTask") is not None:
            self.AiRecognitionTask = AiRecognitionTaskInput()
            self.AiRecognitionTask._deserialize(params.get("AiRecognitionTask"))
        if params.get("TaskNotifyConfig") is not None:
            self.TaskNotifyConfig = TaskNotifyConfig()
            self.TaskNotifyConfig._deserialize(params.get("TaskNotifyConfig"))
        self.TasksPriority = params.get("TasksPriority")
        self.SessionId = params.get("SessionId")
        self.SessionContext = params.get("SessionContext")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProcessMediaResponse(AbstractModel):
    """ProcessMedia response structure.

    """

    def __init__(self):
        r"""
        :param TaskId: Task ID.
        :type TaskId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ProhibitedAsrReviewTemplateInfo(AbstractModel):
    """Control parameter of prohibited information detection in speech task

    """

    def __init__(self):
        r"""
        :param Switch: Switch of prohibited information detection in speech task. Valid values:
<li>ON: enables prohibited information detection in speech task;</li>
<li>OFF: disables prohibited information detection in speech task.</li>
        :type Switch: str
        :param BlockConfidence: Threshold score for violation. If this score is reached or exceeded during intelligent audit, it will be deemed that a suspected violation has occurred. If this parameter is left empty, 100 will be used by default. Value range: 0–100.
        :type BlockConfidence: int
        :param ReviewConfidence: Threshold score for human audit. If this score is reached or exceeded during intelligent audit, human audit will be considered necessary. If this parameter is left empty, 75 will be used by default. Value range: 0–100.
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProhibitedAsrReviewTemplateInfoForUpdate(AbstractModel):
    """Control parameter of prohibited information detection in speech task

    """

    def __init__(self):
        r"""
        :param Switch: Switch of prohibited information detection in speech task. Valid values:
<li>ON: enables prohibited information detection in speech task;</li>
<li>OFF: disables prohibited information detection in speech task.</li>
        :type Switch: str
        :param BlockConfidence: Threshold score for violation. If this score is reached or exceeded during intelligent audit, it will be deemed that a suspected violation has occurred. If this parameter is left empty, 100 will be used by default. Value range: 0–100.
        :type BlockConfidence: int
        :param ReviewConfidence: Threshold score for human audit. If this score is reached or exceeded during intelligent audit, human audit will be considered necessary. If this parameter is left empty, 75 will be used by default. Value range: 0–100.
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProhibitedConfigureInfo(AbstractModel):
    """Control parameter of prohibited information detection task

    """

    def __init__(self):
        r"""
        :param AsrReviewInfo: Control parameter of prohibited information detection in speech.
        :type AsrReviewInfo: :class:`tencentcloud.mps.v20190612.models.ProhibitedAsrReviewTemplateInfo`
        :param OcrReviewInfo: Control parameter of prohibited information detection in text.
        :type OcrReviewInfo: :class:`tencentcloud.mps.v20190612.models.ProhibitedOcrReviewTemplateInfo`
        """
        self.AsrReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("AsrReviewInfo") is not None:
            self.AsrReviewInfo = ProhibitedAsrReviewTemplateInfo()
            self.AsrReviewInfo._deserialize(params.get("AsrReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = ProhibitedOcrReviewTemplateInfo()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProhibitedConfigureInfoForUpdate(AbstractModel):
    """Control parameter of prohibited information detection task

    """

    def __init__(self):
        r"""
        :param AsrReviewInfo: Control parameter of prohibited information detection in speech.
        :type AsrReviewInfo: :class:`tencentcloud.mps.v20190612.models.ProhibitedAsrReviewTemplateInfoForUpdate`
        :param OcrReviewInfo: Control parameter of prohibited information detection in text.
        :type OcrReviewInfo: :class:`tencentcloud.mps.v20190612.models.ProhibitedOcrReviewTemplateInfoForUpdate`
        """
        self.AsrReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("AsrReviewInfo") is not None:
            self.AsrReviewInfo = ProhibitedAsrReviewTemplateInfoForUpdate()
            self.AsrReviewInfo._deserialize(params.get("AsrReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = ProhibitedOcrReviewTemplateInfoForUpdate()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProhibitedOcrReviewTemplateInfo(AbstractModel):
    """Control parameter of prohibited information detection in text task

    """

    def __init__(self):
        r"""
        :param Switch: Switch of prohibited information detection in text task. Valid values:
<li>ON: enables prohibited information detection in text task;</li>
<li>OFF: disables prohibited information detection in text task.</li>
        :type Switch: str
        :param BlockConfidence: Threshold score for violation. If this score is reached or exceeded during intelligent audit, it will be deemed that a suspected violation has occurred. If this parameter is left empty, 100 will be used by default. Value range: 0–100.
        :type BlockConfidence: int
        :param ReviewConfidence: Threshold score for human audit. If this score is reached or exceeded during intelligent audit, human audit will be considered necessary. If this parameter is left empty, 75 will be used by default. Value range: 0–100.
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProhibitedOcrReviewTemplateInfoForUpdate(AbstractModel):
    """Control parameter of prohibited information detection in text task

    """

    def __init__(self):
        r"""
        :param Switch: Switch of prohibited information detection in text task. Valid values:
<li>ON: enables prohibited information detection in text task;</li>
<li>OFF: disables prohibited information detection in text task.</li>
        :type Switch: str
        :param BlockConfidence: Threshold score for violation. If this score is reached or exceeded during intelligent audit, it will be deemed that a suspected violation has occurred. If this parameter is left empty, 100 will be used by default. Value range: 0–100.
        :type BlockConfidence: int
        :param ReviewConfidence: Threshold score for human audit. If this score is reached or exceeded during intelligent audit, human audit will be considered necessary. If this parameter is left empty, 75 will be used by default. Value range: 0–100.
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RawImageWatermarkInput(AbstractModel):
    """Input parameter of image watermark template

    """

    def __init__(self):
        r"""
        :param ImageContent: Input content of watermark image. JPEG and PNG images are supported.
        :type ImageContent: :class:`tencentcloud.mps.v20190612.models.MediaInputInfo`
        :param Width: Watermark width. % and px formats are supported:
<li>If the string ends in %, the `Width` of the watermark will be the specified percentage of the video width; for example, `10%` means that `Width` is 10% of the video width;</li>
<li>If the string ends in px, the `Width` of the watermark will be in px; for example, `100px` means that `Width` is 100 px.</li>
Default value: 10%.
        :type Width: str
        :param Height: Watermark height. % and px formats are supported:
<li>If the string ends in %, the `Height` of the watermark will be the specified percentage of the video height; for example, `10%` means that `Height` is 10% of the video height;</li>
<li>If the string ends in px, the `Height` of the watermark will be in px; for example, `100px` means that `Height` is 100 px.</li>
Default value: 0 px, which means that `Height` will be proportionally scaled according to the aspect ratio of the original watermark image.
        :type Height: str
        :param RepeatType: Repeat type of an animated watermark. Valid values:
<li>`once`: no longer appears after watermark playback ends.</li>
<li>`repeat_last_frame`: stays on the last frame after watermark playback ends.</li>
<li>`repeat` (default): repeats the playback until the video ends.</li>
        :type RepeatType: str
        """
        self.ImageContent = None
        self.Width = None
        self.Height = None
        self.RepeatType = None


    def _deserialize(self, params):
        if params.get("ImageContent") is not None:
            self.ImageContent = MediaInputInfo()
            self.ImageContent._deserialize(params.get("ImageContent"))
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.RepeatType = params.get("RepeatType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RawTranscodeParameter(AbstractModel):
    """Specifications for custom transcoding

    """

    def __init__(self):
        r"""
        :param Container: Container. Valid values: mp4; flv; hls; mp3; flac; ogg; m4a. Among them, mp3, flac, ogg, and m4a are for audio files.
        :type Container: str
        :param RemoveVideo: Whether to remove video data. Valid values:
<li>0: retain;</li>
<li>1: remove.</li>
Default value: 0.
        :type RemoveVideo: int
        :param RemoveAudio: Whether to remove audio data. Valid values:
<li>0: retain;</li>
<li>1: remove.</li>
Default value: 0.
        :type RemoveAudio: int
        :param VideoTemplate: Video stream configuration parameter. This field is required when `RemoveVideo` is 0.
        :type VideoTemplate: :class:`tencentcloud.mps.v20190612.models.VideoTemplateInfo`
        :param AudioTemplate: Audio stream configuration parameter. This field is required when `RemoveAudio` is 0.
        :type AudioTemplate: :class:`tencentcloud.mps.v20190612.models.AudioTemplateInfo`
        :param TEHDConfig: TESHD transcoding parameter.
        :type TEHDConfig: :class:`tencentcloud.mps.v20190612.models.TEHDConfig`
        """
        self.Container = None
        self.RemoveVideo = None
        self.RemoveAudio = None
        self.VideoTemplate = None
        self.AudioTemplate = None
        self.TEHDConfig = None


    def _deserialize(self, params):
        self.Container = params.get("Container")
        self.RemoveVideo = params.get("RemoveVideo")
        self.RemoveAudio = params.get("RemoveAudio")
        if params.get("VideoTemplate") is not None:
            self.VideoTemplate = VideoTemplateInfo()
            self.VideoTemplate._deserialize(params.get("VideoTemplate"))
        if params.get("AudioTemplate") is not None:
            self.AudioTemplate = AudioTemplateInfo()
            self.AudioTemplate._deserialize(params.get("AudioTemplate"))
        if params.get("TEHDConfig") is not None:
            self.TEHDConfig = TEHDConfig()
            self.TEHDConfig._deserialize(params.get("TEHDConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RawWatermarkParameter(AbstractModel):
    """Custom watermark specifications.

    """

    def __init__(self):
        r"""
        :param Type: Watermark type. Valid values:
<li>image: image watermark.</li>
        :type Type: str
        :param CoordinateOrigin: Origin position, which currently can only be:
<li>TopLeft: the origin of coordinates is in the top-left corner of the video, and the origin of the watermark is in the top-left corner of the image or text.</li>
Default value: TopLeft.
        :type CoordinateOrigin: str
        :param XPos: The horizontal position of the origin of the watermark relative to the origin of coordinates of the video. % and px formats are supported:
<li>If the string ends in %, the `XPos` of the watermark will be the specified percentage of the video width; for example, `10%` means that `XPos` is 10% of the video width;</li>
<li>If the string ends in px, the `XPos` of the watermark will be the specified px; for example, `100px` means that `XPos` is 100 px.</li>
Default value: 0 px.
        :type XPos: str
        :param YPos: The vertical position of the origin of the watermark relative to the origin of coordinates of the video. % and px formats are supported:
<li>If the string ends in %, the `YPos` of the watermark will be the specified percentage of the video height; for example, `10%` means that `YPos` is 10% of the video height;</li>
<li>If the string ends in px, the `YPos` of the watermark will be the specified px; for example, `100px` means that `YPos` is 100 px.</li>
Default value: 0 px.
        :type YPos: str
        :param ImageTemplate: Image watermark template. This field is required when `Type` is `image` and is invalid when `Type` is `text`.
        :type ImageTemplate: :class:`tencentcloud.mps.v20190612.models.RawImageWatermarkInput`
        """
        self.Type = None
        self.CoordinateOrigin = None
        self.XPos = None
        self.YPos = None
        self.ImageTemplate = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.CoordinateOrigin = params.get("CoordinateOrigin")
        self.XPos = params.get("XPos")
        self.YPos = params.get("YPos")
        if params.get("ImageTemplate") is not None:
            self.ImageTemplate = RawImageWatermarkInput()
            self.ImageTemplate._deserialize(params.get("ImageTemplate"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetWorkflowRequest(AbstractModel):
    """ResetWorkflow request structure.

    """

    def __init__(self):
        r"""
        :param WorkflowId: Workflow ID.
        :type WorkflowId: int
        :param WorkflowName: Workflow name of up to 128 characters, which must be unique for the same user.
        :type WorkflowName: str
        :param Trigger: Triggering rule bound to a workflow. If an uploaded video hits the rule for the object, the workflow will be triggered.
        :type Trigger: :class:`tencentcloud.mps.v20190612.models.WorkflowTrigger`
        :param OutputStorage: Output configuration of a video processing output file. If this parameter is left empty, the storage location in `Trigger` will be inherited.
        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        :param OutputDir: Target directory of a video processing output file, such as `/movie/201907/`. If this parameter is left empty, the file will be outputted to the same directory where the source file is located, i.e.; `{inputDir}`.
        :type OutputDir: str
        :param MediaProcessTask: Parameter of a video processing task.
        :type MediaProcessTask: :class:`tencentcloud.mps.v20190612.models.MediaProcessTaskInput`
        :param AiContentReviewTask: Type parameter of a video content audit task.
        :type AiContentReviewTask: :class:`tencentcloud.mps.v20190612.models.AiContentReviewTaskInput`
        :param AiAnalysisTask: Video content analysis task parameter.
        :type AiAnalysisTask: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskInput`
        :param AiRecognitionTask: Type parameter of a video content recognition task.
        :type AiRecognitionTask: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskInput`
        :param TaskPriority: Workflow priority. The higher the value, the higher the priority. Value range: [-10, 10]. If this parameter is left empty, 0 will be used.
        :type TaskPriority: int
        :param TaskNotifyConfig: Event notification information of a task. If this parameter is left empty, no event notifications will be obtained.
        :type TaskNotifyConfig: :class:`tencentcloud.mps.v20190612.models.TaskNotifyConfig`
        """
        self.WorkflowId = None
        self.WorkflowName = None
        self.Trigger = None
        self.OutputStorage = None
        self.OutputDir = None
        self.MediaProcessTask = None
        self.AiContentReviewTask = None
        self.AiAnalysisTask = None
        self.AiRecognitionTask = None
        self.TaskPriority = None
        self.TaskNotifyConfig = None


    def _deserialize(self, params):
        self.WorkflowId = params.get("WorkflowId")
        self.WorkflowName = params.get("WorkflowName")
        if params.get("Trigger") is not None:
            self.Trigger = WorkflowTrigger()
            self.Trigger._deserialize(params.get("Trigger"))
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.OutputDir = params.get("OutputDir")
        if params.get("MediaProcessTask") is not None:
            self.MediaProcessTask = MediaProcessTaskInput()
            self.MediaProcessTask._deserialize(params.get("MediaProcessTask"))
        if params.get("AiContentReviewTask") is not None:
            self.AiContentReviewTask = AiContentReviewTaskInput()
            self.AiContentReviewTask._deserialize(params.get("AiContentReviewTask"))
        if params.get("AiAnalysisTask") is not None:
            self.AiAnalysisTask = AiAnalysisTaskInput()
            self.AiAnalysisTask._deserialize(params.get("AiAnalysisTask"))
        if params.get("AiRecognitionTask") is not None:
            self.AiRecognitionTask = AiRecognitionTaskInput()
            self.AiRecognitionTask._deserialize(params.get("AiRecognitionTask"))
        self.TaskPriority = params.get("TaskPriority")
        if params.get("TaskNotifyConfig") is not None:
            self.TaskNotifyConfig = TaskNotifyConfig()
            self.TaskNotifyConfig._deserialize(params.get("TaskNotifyConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetWorkflowResponse(AbstractModel):
    """ResetWorkflow response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SampleSnapshotTaskInput(AbstractModel):
    """Input parameter type of a sampled screencapturing task.

    """

    def __init__(self):
        r"""
        :param Definition: Sampled screencapturing template ID.
        :type Definition: int
        :param WatermarkSet: List of up to 10 image or text watermarks.
Note: This field may return null, indicating that no valid values can be obtained.
        :type WatermarkSet: list of WatermarkInput
        :param OutputStorage: Target bucket of a sampled screenshot. If this parameter is left empty, the `OutputStorage` value of the upper folder will be inherited.
Note: This field may return null, indicating that no valid values can be obtained.
        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        :param OutputObjectPath: Output path to a generated sampled screenshot, which can be a relative path or an absolute path. If this parameter is left empty, the following relative path will be used by default: `{inputName}_sampleSnapshot_{definition}_{number}.{format}`.
        :type OutputObjectPath: str
        :param ObjectNumberFormat: Rule of the `{number}` variable in the sampled screenshot output path.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ObjectNumberFormat: :class:`tencentcloud.mps.v20190612.models.NumberFormat`
        """
        self.Definition = None
        self.WatermarkSet = None
        self.OutputStorage = None
        self.OutputObjectPath = None
        self.ObjectNumberFormat = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        if params.get("WatermarkSet") is not None:
            self.WatermarkSet = []
            for item in params.get("WatermarkSet"):
                obj = WatermarkInput()
                obj._deserialize(item)
                self.WatermarkSet.append(obj)
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.OutputObjectPath = params.get("OutputObjectPath")
        if params.get("ObjectNumberFormat") is not None:
            self.ObjectNumberFormat = NumberFormat()
            self.ObjectNumberFormat._deserialize(params.get("ObjectNumberFormat"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SampleSnapshotTemplate(AbstractModel):
    """Details of a sampled screencapturing template

    """

    def __init__(self):
        r"""
        :param Definition: Unique ID of a sampled screencapturing template.
        :type Definition: int
        :param Type: Template type. Valid values:
<li>Preset: Preset template;</li>
<li>Custom: Custom template.</li>
        :type Type: str
        :param Name: Name of a sampled screencapturing template.
        :type Name: str
        :param Comment: Template description.
        :type Comment: str
        :param Width: Maximum value of the width (or long side) of a screenshot in px. Value range: 0 and [128, 4,096].
<li>If both `Width` and `Height` are 0, the resolution will be the same as that of the source video;</li>
<li>If `Width` is 0, but `Height` is not 0, `Width` will be proportionally scaled;</li>
<li>If `Width` is not 0, but `Height` is 0, `Height` will be proportionally scaled;</li>
<li>If both `Width` and `Height` are not 0, the custom resolution will be used.</li>
Default value: 0.
        :type Width: int
        :param Height: Maximum value of the height (or short side) of a screenshot in px. Value range: 0 and [128, 4,096].
<li>If both `Width` and `Height` are 0, the resolution will be the same as that of the source video;</li>
<li>If `Width` is 0, but `Height` is not 0, `Width` will be proportionally scaled;</li>
<li>If `Width` is not 0, but `Height` is 0, `Height` will be proportionally scaled;</li>
<li>If both `Width` and `Height` are not 0, the custom resolution will be used.</li>
Default value: 0.
        :type Height: int
        :param ResolutionAdaptive: Resolution adaption. Valid values:
<li>open: Enabled. In this case, `Width` represents the long side of a video, while `Height` the short side;</li>
<li>close: Disabled. In this case, `Width` represents the width of a video, while `Height` the height.</li>
Default value: open.
        :type ResolutionAdaptive: str
        :param Format: Image format.
        :type Format: str
        :param SampleType: Sampled screencapturing type.
        :type SampleType: str
        :param SampleInterval: Sampling interval.
        :type SampleInterval: int
        :param CreateTime: Creation time of a template in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F).
        :type CreateTime: str
        :param UpdateTime: Last modified time of a template in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F).
        :type UpdateTime: str
        :param FillType: Fill type. "Fill" refers to the way of processing a screenshot when its aspect ratio is different from that of the source video. The following fill types are supported:
<li> stretch: Stretch. The screenshot will be stretched frame by frame to match the aspect ratio of the source video, which may make the screenshot "shorter" or "longer";</li>
<li>black: Fill with black. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with black color blocks.</li>
<li>white: Fill with white. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with white color blocks.</li>
<li>gauss: Fill with Gaussian blur. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with Gaussian blur.</li>
Default value: black.
        :type FillType: str
        """
        self.Definition = None
        self.Type = None
        self.Name = None
        self.Comment = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.Format = None
        self.SampleType = None
        self.SampleInterval = None
        self.CreateTime = None
        self.UpdateTime = None
        self.FillType = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Format = params.get("Format")
        self.SampleType = params.get("SampleType")
        self.SampleInterval = params.get("SampleInterval")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.FillType = params.get("FillType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SnapshotByTimeOffsetTaskInput(AbstractModel):
    """Input parameter type of a time point screencapturing task

    """

    def __init__(self):
        r"""
        :param Definition: ID of a time point screencapturing template.
        :type Definition: int
        :param ExtTimeOffsetSet: List of screenshot time points in the format of `s` or `%`:
<li>If the string ends in `s`, it means that the time point is in seconds; for example, `3.5s` means that the time point is the 3.5th second;</li>
<li>If the string ends in `%`, it means that the time point is the specified percentage of the video duration; for example, `10%` means that the time point is 10% of the video duration.</li>
        :type ExtTimeOffsetSet: list of str
        :param TimeOffsetSet: List of time points of screenshots in <font color=red>seconds</font>.
        :type TimeOffsetSet: list of float
        :param WatermarkSet: List of up to 10 image or text watermarks.
Note: This field may return null, indicating that no valid values can be obtained.
        :type WatermarkSet: list of WatermarkInput
        :param OutputStorage: Target bucket of a generated time point screenshot file. If this parameter is left empty, the `OutputStorage` value of the upper folder will be inherited.
Note: This field may return null, indicating that no valid values can be obtained.
        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        :param OutputObjectPath: Output path to a generated time point screenshot, which can be a relative path or an absolute path. If this parameter is left empty, the following relative path will be used by default: `{inputName}_snapshotByTimeOffset_{definition}_{number}.{format}`.
        :type OutputObjectPath: str
        :param ObjectNumberFormat: Rule of the `{number}` variable in the time point screenshot output path.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ObjectNumberFormat: :class:`tencentcloud.mps.v20190612.models.NumberFormat`
        """
        self.Definition = None
        self.ExtTimeOffsetSet = None
        self.TimeOffsetSet = None
        self.WatermarkSet = None
        self.OutputStorage = None
        self.OutputObjectPath = None
        self.ObjectNumberFormat = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.ExtTimeOffsetSet = params.get("ExtTimeOffsetSet")
        self.TimeOffsetSet = params.get("TimeOffsetSet")
        if params.get("WatermarkSet") is not None:
            self.WatermarkSet = []
            for item in params.get("WatermarkSet"):
                obj = WatermarkInput()
                obj._deserialize(item)
                self.WatermarkSet.append(obj)
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.OutputObjectPath = params.get("OutputObjectPath")
        if params.get("ObjectNumberFormat") is not None:
            self.ObjectNumberFormat = NumberFormat()
            self.ObjectNumberFormat._deserialize(params.get("ObjectNumberFormat"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SnapshotByTimeOffsetTemplate(AbstractModel):
    """Details of a time point screencapturing template.

    """

    def __init__(self):
        r"""
        :param Definition: Unique ID of a time point screencapturing template.
        :type Definition: int
        :param Type: Template type. Valid values:
<li>Preset: Preset template;</li>
<li>Custom: Custom template.</li>
        :type Type: str
        :param Name: Name of a time point screencapturing template.
        :type Name: str
        :param Comment: Template description.
        :type Comment: str
        :param Width: Maximum value of the width (or long side) of a screenshot in px. Value range: 0 and [128, 4,096].
<li>If both `Width` and `Height` are 0, the resolution will be the same as that of the source video;</li>
<li>If `Width` is 0, but `Height` is not 0, `Width` will be proportionally scaled;</li>
<li>If `Width` is not 0, but `Height` is 0, `Height` will be proportionally scaled;</li>
<li>If both `Width` and `Height` are not 0, the custom resolution will be used.</li>
Default value: 0.
        :type Width: int
        :param Height: Maximum value of the height (or short side) of a screenshot in px. Value range: 0 and [128, 4,096].
<li>If both `Width` and `Height` are 0, the resolution will be the same as that of the source video;</li>
<li>If `Width` is 0, but `Height` is not 0, `Width` will be proportionally scaled;</li>
<li>If `Width` is not 0, but `Height` is 0, `Height` will be proportionally scaled;</li>
<li>If both `Width` and `Height` are not 0, the custom resolution will be used.</li>
Default value: 0.
        :type Height: int
        :param ResolutionAdaptive: Resolution adaption. Valid values:
<li>open: Enabled. In this case, `Width` represents the long side of a video, while `Height` the short side;</li>
<li>close: Disabled. In this case, `Width` represents the width of a video, while `Height` the height.</li>
Default value: open.
        :type ResolutionAdaptive: str
        :param Format: Image format.
        :type Format: str
        :param CreateTime: Creation time of a template in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F).
        :type CreateTime: str
        :param UpdateTime: Last modified time of a template in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F).
        :type UpdateTime: str
        :param FillType: Fill type. "Fill" refers to the way of processing a screenshot when its aspect ratio is different from that of the source video. The following fill types are supported:
<li> stretch: Stretch. The screenshot will be stretched frame by frame to match the aspect ratio of the source video, which may make the screenshot "shorter" or "longer";</li>
<li>black: Fill with black. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with black color blocks.</li>
<li>white: Fill with white. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with white color blocks.</li>
<li>gauss: Fill with Gaussian blur. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with Gaussian blur.</li>
Default value: black.
        :type FillType: str
        """
        self.Definition = None
        self.Type = None
        self.Name = None
        self.Comment = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.Format = None
        self.CreateTime = None
        self.UpdateTime = None
        self.FillType = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Format = params.get("Format")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.FillType = params.get("FillType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SvgWatermarkInput(AbstractModel):
    """Input parameter of an SVG watermarking template

    """

    def __init__(self):
        r"""
        :param Width: Watermark width, which supports six formats of px, %, W%, H%, S%, and L%:
<li>If the string ends in px, the `Width` of the watermark will be in px; for example, `100px` means that `Width` is 100 px; if `0px` is entered
 and `Height` is not `0px`, the watermark width will be proportionally scaled based on the source SVG image; if `0px` is entered for both `Width` and `Height`, the watermark width will be the width of the source SVG image;</li>
<li>If the string ends in `W%`, the `Width` of the watermark will be the specified percentage of the video width; for example, `10W%` means that `Width` is 10% of the video width;</li>
<li>If the string ends in `H%`, the `Width` of the watermark will be the specified percentage of the video height; for example, `10H%` means that `Width` is 10% of the video height;</li>
<li>If the string ends in `S%`, the `Width` of the watermark will be the specified percentage of the short side of the video; for example, `10S%` means that `Width` is 10% of the short side of the video;</li>
<li>If the string ends in `L%`, the `Width` of the watermark will be the specified percentage of the long side of the video; for example, `10L%` means that `Width` is 10% of the long side of the video;</li>
<li>If the string ends in %, the meaning is the same as `W%`.</li>
Default value: 10W%.
        :type Width: str
        :param Height: Watermark height, which supports six formats of px, %, W%, H%, S%, and L%:
<li>If the string ends in px, the `Height` of the watermark will be in px; for example, `100px` means that `Height` is 100 px; if `0px` is entered
 and `Width` is not `0px`, the watermark height will be proportionally scaled based on the source SVG image; if `0px` is entered for both `Width` and `Height`, the watermark height will be the height of the source SVG image;</li>
<li>If the string ends in `W%`, the `Height` of the watermark will be the specified percentage of the video width; for example, `10W%` means that `Height` is 10% of the video width;</li>
<li>If the string ends in `H%`, the `Height` of the watermark will be the specified percentage of the video height; for example, `10H%` means that `Height` is 10% of the video height;</li>
<li>If the string ends in `S%`, the `Height` of the watermark will be the specified percentage of the short side of the video; for example, `10S%` means that `Height` is 10% of the short side of the video;</li>
<li>If the string ends in `L%`, the `Height` of the watermark will be the specified percentage of the long side of the video; for example, `10L%` means that `Height` is 10% of the long side of the video;</li>
<li>If the string ends in %, the meaning is the same as `H%`.</li>
Default value: 0 px.
        :type Height: str
        """
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SvgWatermarkInputForUpdate(AbstractModel):
    """Input parameter of an SVG watermarking template

    """

    def __init__(self):
        r"""
        :param Width: Watermark width, which supports six formats of px, %, W%, H%, S%, and L%:
<li>If the string ends in px, the `Width` of the watermark will be in px; for example, `100px` means that `Width` is 100 px; if `0px` is entered
 and `Height` is not `0px`, the watermark width will be proportionally scaled based on the source SVG image; if `0px` is entered for both `Width` and `Height`, the watermark width will be the width of the source SVG image;</li>
<li>If the string ends in `W%`, the `Width` of the watermark will be the specified percentage of the video width; for example, `10W%` means that `Width` is 10% of the video width;</li>
<li>If the string ends in `H%`, the `Width` of the watermark will be the specified percentage of the video height; for example, `10H%` means that `Width` is 10% of the video height;</li>
<li>If the string ends in `S%`, the `Width` of the watermark will be the specified percentage of the short side of the video; for example, `10S%` means that `Width` is 10% of the short side of the video;</li>
<li>If the string ends in `L%`, the `Width` of the watermark will be the specified percentage of the long side of the video; for example, `10L%` means that `Width` is 10% of the long side of the video;</li>
<li>If the string ends in %, the meaning is the same as `W%`.</li>
Default value: 10W%.
        :type Width: str
        :param Height: Watermark height, which supports six formats of px, %, W%, H%, S%, and L%:
<li>If the string ends in px, the `Height` of the watermark will be in px; for example, `100px` means that `Height` is 100 px; if `0px` is entered
 and `Width` is not `0px`, the watermark height will be proportionally scaled based on the source SVG image; if `0px` is entered for both `Width` and `Height`, the watermark height will be the height of the source SVG image;</li>
<li>If the string ends in `W%`, the `Height` of the watermark will be the specified percentage of the video width; for example, `10W%` means that `Height` is 10% of the video width;</li>
<li>If the string ends in `H%`, the `Height` of the watermark will be the specified percentage of the video height; for example, `10H%` means that `Height` is 10% of the video height;</li>
<li>If the string ends in `S%`, the `Height` of the watermark will be the specified percentage of the short side of the video; for example, `10S%` means that `Height` is 10% of the short side of the video;</li>
<li>If the string ends in `L%`, the `Height` of the watermark will be the specified percentage of the long side of the video; for example, `10L%` means that `Height` is 10% of the long side of the video;</li>
<li>If the string ends in %, the meaning is the same as `H%`.
Default value: 0 px.
        :type Height: str
        """
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TEHDConfig(AbstractModel):
    """TESHD parameter configuration.

    """

    def __init__(self):
        r"""
        :param Type: TESHD type. Valid values:
<li>TEHD-100: TESHD-100.</li>
If this parameter is left empty, TESHD will not be enabled.
        :type Type: str
        :param MaxVideoBitrate: Maximum bitrate, which is valid when `Type` is `TESHD`.
If this parameter is left empty or 0 is entered, there will be no upper limit for bitrate.
        :type MaxVideoBitrate: int
        """
        self.Type = None
        self.MaxVideoBitrate = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.MaxVideoBitrate = params.get("MaxVideoBitrate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TEHDConfigForUpdate(AbstractModel):
    """TESHD parameter configuration.

    """

    def __init__(self):
        r"""
        :param Type: TESHD type. Valid values:
<li>TEHD-100: TESHD-100.</li>
If this parameter is left blank, no modification will be made.
        :type Type: str
        :param MaxVideoBitrate: Maximum bitrate. If this parameter is left empty, no modification will be made.
        :type MaxVideoBitrate: int
        """
        self.Type = None
        self.MaxVideoBitrate = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.MaxVideoBitrate = params.get("MaxVideoBitrate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagConfigureInfo(AbstractModel):
    """Control parameter of intelligent tagging task

    """

    def __init__(self):
        r"""
        :param Switch: Switch of intelligent tagging task. Valid values:
<li>ON: enables intelligent tagging task;</li>
<li>OFF: disables intelligent tagging task.</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagConfigureInfoForUpdate(AbstractModel):
    """Control parameter of intelligent tagging task

    """

    def __init__(self):
        r"""
        :param Switch: Switch of intelligent tagging task. Valid values:
<li>ON: enables intelligent tagging task;</li>
<li>OFF: disables intelligent tagging task.</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskNotifyConfig(AbstractModel):
    """Event notification configuration of a task.

    """

    def __init__(self):
        r"""
        :param CmqModel: CMQ model. There are two types: `Queue` and `Topic`. Currently, only `Queue` is supported.
        :type CmqModel: str
        :param CmqRegion: CMQ region, such as `sh` and `bj`.
        :type CmqRegion: str
        :param QueueName: This parameter is valid when the model is `Queue`, indicating the name of the CMQ queue for receiving event notifications.
        :type QueueName: str
        :param TopicName: This parameter is valid when the model is `Topic`, indicating the name of the CMQ topic for receiving event notifications.
        :type TopicName: str
        :param NotifyMode: Workflow notification method. Valid values: Finish, Change. If this parameter is left empty, `Finish` will be used.
        :type NotifyMode: str
        :param NotifyType: Notification type, `CMQ` by default. If `URL` is passed in, HTTP callbacks are sent to the URL specified by `NotifyUrl`.
        :type NotifyType: str
        :param NotifyUrl: HTTP callback URL, required if `NotifyType` is set to `URL`
        :type NotifyUrl: str
        """
        self.CmqModel = None
        self.CmqRegion = None
        self.QueueName = None
        self.TopicName = None
        self.NotifyMode = None
        self.NotifyType = None
        self.NotifyUrl = None


    def _deserialize(self, params):
        self.CmqModel = params.get("CmqModel")
        self.CmqRegion = params.get("CmqRegion")
        self.QueueName = params.get("QueueName")
        self.TopicName = params.get("TopicName")
        self.NotifyMode = params.get("NotifyMode")
        self.NotifyType = params.get("NotifyType")
        self.NotifyUrl = params.get("NotifyUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskOutputStorage(AbstractModel):
    """Information of a video processing output object.

    """

    def __init__(self):
        r"""
        :param Type: Storage location type of a video processing output object. Only COS is supported currently.
        :type Type: str
        :param CosOutputStorage: This parameter is valid and required when `Type` is COS, indicating the location of an output COS object after video processing.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CosOutputStorage: :class:`tencentcloud.mps.v20190612.models.CosOutputStorage`
        """
        self.Type = None
        self.CosOutputStorage = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("CosOutputStorage") is not None:
            self.CosOutputStorage = CosOutputStorage()
            self.CosOutputStorage._deserialize(params.get("CosOutputStorage"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskSimpleInfo(AbstractModel):
    """Task overview information

    """

    def __init__(self):
        r"""
        :param TaskId: Task ID.
        :type TaskId: str
        :param TaskType: Task type. Valid values:
<li> WorkflowTask: Workflow processing task;</li>
<li> LiveProcessTask: Live stream processing task.</li>
        :type TaskType: str
        :param CreateTime: Creation time of a task in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F).
        :type CreateTime: str
        :param BeginProcessTime: Start time of task execution in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F). If the task has not been started yet, this field will be `0000-00-00T00:00:00Z`.
        :type BeginProcessTime: str
        :param FinishTime: End time of a task in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F). If the task has not been completed yet, this field will be `0000-00-00T00:00:00Z`.
        :type FinishTime: str
        """
        self.TaskId = None
        self.TaskType = None
        self.CreateTime = None
        self.BeginProcessTime = None
        self.FinishTime = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.TaskType = params.get("TaskType")
        self.CreateTime = params.get("CreateTime")
        self.BeginProcessTime = params.get("BeginProcessTime")
        self.FinishTime = params.get("FinishTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerrorismConfigureInfo(AbstractModel):
    """The parameters for detecting sensitive information.

    """

    def __init__(self):
        r"""
        :param ImgReviewInfo: The parameters for detecting sensitive information in images.
        :type ImgReviewInfo: :class:`tencentcloud.mps.v20190612.models.TerrorismImgReviewTemplateInfo`
        :param OcrReviewInfo: The parameters for detecting sensitive information based on OCR.
        :type OcrReviewInfo: :class:`tencentcloud.mps.v20190612.models.TerrorismOcrReviewTemplateInfo`
        """
        self.ImgReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("ImgReviewInfo") is not None:
            self.ImgReviewInfo = TerrorismImgReviewTemplateInfo()
            self.ImgReviewInfo._deserialize(params.get("ImgReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = TerrorismOcrReviewTemplateInfo()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerrorismConfigureInfoForUpdate(AbstractModel):
    """The parameters for detecting sensitive information.

    """

    def __init__(self):
        r"""
        :param ImgReviewInfo: The parameters for detecting sensitive information in images.
        :type ImgReviewInfo: :class:`tencentcloud.mps.v20190612.models.TerrorismImgReviewTemplateInfoForUpdate`
        :param OcrReviewInfo: The parameters for detecting sensitive information based on OCR.
        :type OcrReviewInfo: :class:`tencentcloud.mps.v20190612.models.TerrorismOcrReviewTemplateInfoForUpdate`
        """
        self.ImgReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("ImgReviewInfo") is not None:
            self.ImgReviewInfo = TerrorismImgReviewTemplateInfoForUpdate()
            self.ImgReviewInfo._deserialize(params.get("ImgReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = TerrorismOcrReviewTemplateInfoForUpdate()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerrorismImgReviewTemplateInfo(AbstractModel):
    """The parameters for detecting sensitive information in images.

    """

    def __init__(self):
        r"""
        :param Switch: Whether to detect sensitive information in images. Valid values:
<li>ON</li>
<li>OFF</li>
        :type Switch: str
        :param LabelSet: The filter labels for sensitive information detection in images, which specify the types of sensitive information to return. If this parameter is left empty, the detection results for all labels are returned. Valid values:
<li>guns</li>
<li>crowd</li>
<li>bloody</li>
<li>police</li>
<li>banners (sensitive flags)</li>
<li>militant</li>
<li>explosion</li>
<li>terrorists</li>
<li>scenario (sensitive scenes) </li>
        :type LabelSet: list of str
        :param BlockConfidence: Threshold score for violation. If this score is reached or exceeded during intelligent audit, it will be deemed that a suspected violation has occurred. If this parameter is left empty, 90 will be used by default. Value range: 0-100.
        :type BlockConfidence: int
        :param ReviewConfidence: Threshold score for human audit. If this score is reached or exceeded during intelligent audit, human audit will be considered necessary. If this parameter is left empty, 80 will be used by default. Value range: 0-100.
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerrorismImgReviewTemplateInfoForUpdate(AbstractModel):
    """The parameters for detecting sensitive information in images.

    """

    def __init__(self):
        r"""
        :param Switch: Whether to detect sensitive information in images. Valid values:
<li>ON</li>
<li>OFF</li>
        :type Switch: str
        :param LabelSet: The filter labels for sensitive information detection in images, which specify the types of sensitive information to return. If this parameter is left empty, the detection results for all labels are returned. Valid values:
<li>guns</li>
<li>crowd</li>
<li>bloody</li>
<li>police</li>
<li>banners (sensitive flags)</li>
<li>militant</li>
<li>explosion</li>
<li>terrorists</li>
<li>scenario (sensitive scenes) </li>
        :type LabelSet: list of str
        :param BlockConfidence: Threshold score for violation. If this score is reached or exceeded during intelligent audit, it will be deemed that a suspected violation has occurred. Value range: 0-100.
        :type BlockConfidence: int
        :param ReviewConfidence: Threshold score for human audit. If this score is reached or exceeded during intelligent audit, human audit will be considered necessary. Value range: 0-100.
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerrorismOcrReviewTemplateInfo(AbstractModel):
    """The parameters for detecting sensitive information based on OCR.

    """

    def __init__(self):
        r"""
        :param Switch: Whether to detect sensitive information based on OCR. Valid values:
<li>ON</li>
<li>OFF</li>
        :type Switch: str
        :param BlockConfidence: Threshold score for violation. If this score is reached or exceeded during intelligent audit, it will be deemed that a suspected violation has occurred. If this parameter is left empty, 100 will be used by default. Value range: 0–100.
        :type BlockConfidence: int
        :param ReviewConfidence: Threshold score for human audit. If this score is reached or exceeded during intelligent audit, human audit will be considered necessary. If this parameter is left empty, 75 will be used by default. Value range: 0–100.
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerrorismOcrReviewTemplateInfoForUpdate(AbstractModel):
    """The parameters for detecting sensitive information based on OCR.

    """

    def __init__(self):
        r"""
        :param Switch: Whether to detect sensitive information based on OCR. Valid values:
<li>ON</li>
<li>OFF</li>
        :type Switch: str
        :param BlockConfidence: Threshold score for violation. If this score is reached or exceeded during intelligent audit, it will be deemed that a suspected violation has occurred. If this parameter is left empty, 100 will be used by default. Value range: 0–100.
        :type BlockConfidence: int
        :param ReviewConfidence: Threshold score for human audit. If this score is reached or exceeded during intelligent audit, human audit will be considered necessary. If this parameter is left empty, 75 will be used by default. Value range: 0–100.
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextWatermarkTemplateInput(AbstractModel):
    """Text watermarking template

    """

    def __init__(self):
        r"""
        :param FontType: Font type. Currently, two types are supported:
<li>simkai.ttf: Both Chinese and English are supported;</li>
<li>arial.ttf: Only English is supported.</li>
        :type FontType: str
        :param FontSize: Font size in Npx format where N is a numeric value.
        :type FontSize: str
        :param FontColor: Font color in 0xRRGGBB format. Default value: 0xFFFFFF (white).
        :type FontColor: str
        :param FontAlpha: Text transparency. Value range: (0, 1]
<li>0: Completely transparent</li>
<li>1: Completely opaque</li>
Default value: 1.
        :type FontAlpha: float
        """
        self.FontType = None
        self.FontSize = None
        self.FontColor = None
        self.FontAlpha = None


    def _deserialize(self, params):
        self.FontType = params.get("FontType")
        self.FontSize = params.get("FontSize")
        self.FontColor = params.get("FontColor")
        self.FontAlpha = params.get("FontAlpha")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextWatermarkTemplateInputForUpdate(AbstractModel):
    """Text watermarking template

    """

    def __init__(self):
        r"""
        :param FontType: Font type. Currently, two types are supported:
<li>simkai.ttf: Both Chinese and English are supported;</li>
<li>arial.ttf: Only English is supported.</li>
        :type FontType: str
        :param FontSize: Font size in Npx format where N is a numeric value.
        :type FontSize: str
        :param FontColor: Font color in 0xRRGGBB format. Default value: 0xFFFFFF (white).
        :type FontColor: str
        :param FontAlpha: Text transparency. Value range: (0, 1]
<li>0: Completely transparent</li>
<li>1: Completely opaque</li>
        :type FontAlpha: float
        """
        self.FontType = None
        self.FontSize = None
        self.FontColor = None
        self.FontAlpha = None


    def _deserialize(self, params):
        self.FontType = params.get("FontType")
        self.FontSize = params.get("FontSize")
        self.FontColor = params.get("FontColor")
        self.FontAlpha = params.get("FontAlpha")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TranscodeTaskInput(AbstractModel):
    """Input parameter type of a transcoding task

    """

    def __init__(self):
        r"""
        :param Definition: ID of a video transcoding template.
        :type Definition: int
        :param RawParameter: Custom video transcoding parameter, which is valid if `Definition` is 0.
This parameter is used in highly customized scenarios. We recommend you use `Definition` to specify the transcoding parameter preferably.
        :type RawParameter: :class:`tencentcloud.mps.v20190612.models.RawTranscodeParameter`
        :param OverrideParameter: Video transcoding custom parameter, which is valid when `Definition` is not 0.
When any parameters in this structure are entered, they will be used to override corresponding parameters in templates.
This parameter is used in highly customized scenarios. We recommend you only use `Definition` to specify the transcoding parameter.
Note: this field may return `null`, indicating that no valid value was found.
        :type OverrideParameter: :class:`tencentcloud.mps.v20190612.models.OverrideTranscodeParameter`
        :param WatermarkSet: List of up to 10 image or text watermarks.
Note: This field may return null, indicating that no valid values can be obtained.
        :type WatermarkSet: list of WatermarkInput
        :param MosaicSet: List of blurs. Up to 10 ones can be supported.
        :type MosaicSet: list of MosaicInput
        :param StartTimeOffset: Start time offset of a transcoded video, in seconds.
<li>If this parameter is left empty or set to 0, the transcoded video will start at the same time as the original video.</li>
<li>If this parameter is set to a positive number (n for example), the transcoded video will start at the nth second of the original video.</li>
<li>If this parameter is set to a negative number (-n for example), the transcoded video will start at the nth second before the end of the original video.</li>
        :type StartTimeOffset: float
        :param EndTimeOffset: End time offset of a transcoded video, in seconds.
<li>If this parameter is left empty or set to 0, the transcoded video will end at the same time as the original video.</li>
<li>If this parameter is set to a positive number (n for example), the transcoded video will end at the nth second of the original video.</li>
<li>If this parameter is set to a negative number (-n for example), the transcoded video will end at the nth second before the end of the original video.</li>
        :type EndTimeOffset: float
        :param OutputStorage: Target bucket of an output file. If this parameter is left empty, the `OutputStorage` value of the upper folder will be inherited.
Note: This field may return null, indicating that no valid values can be obtained.
        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        :param OutputObjectPath: Path to a primary output file, which can be a relative path or an absolute path. If this parameter is left empty, the following relative path will be used by default: `{inputName}_transcode_{definition}.{format}`.
        :type OutputObjectPath: str
        :param SegmentObjectName: Path to an output file part (the path to ts during transcoding to HLS), which can only be a relative path. If this parameter is left empty, the following relative path will be used by default: `{inputName}_transcode_{definition}_{number}.{format}`.
        :type SegmentObjectName: str
        :param ObjectNumberFormat: Rule of the `{number}` variable in the output path after transcoding.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ObjectNumberFormat: :class:`tencentcloud.mps.v20190612.models.NumberFormat`
        :param HeadTailParameter: Opening and closing credits parameters
Note: this field may return `null`, indicating that no valid value was found.
        :type HeadTailParameter: :class:`tencentcloud.mps.v20190612.models.HeadTailParameter`
        """
        self.Definition = None
        self.RawParameter = None
        self.OverrideParameter = None
        self.WatermarkSet = None
        self.MosaicSet = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.OutputStorage = None
        self.OutputObjectPath = None
        self.SegmentObjectName = None
        self.ObjectNumberFormat = None
        self.HeadTailParameter = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        if params.get("RawParameter") is not None:
            self.RawParameter = RawTranscodeParameter()
            self.RawParameter._deserialize(params.get("RawParameter"))
        if params.get("OverrideParameter") is not None:
            self.OverrideParameter = OverrideTranscodeParameter()
            self.OverrideParameter._deserialize(params.get("OverrideParameter"))
        if params.get("WatermarkSet") is not None:
            self.WatermarkSet = []
            for item in params.get("WatermarkSet"):
                obj = WatermarkInput()
                obj._deserialize(item)
                self.WatermarkSet.append(obj)
        if params.get("MosaicSet") is not None:
            self.MosaicSet = []
            for item in params.get("MosaicSet"):
                obj = MosaicInput()
                obj._deserialize(item)
                self.MosaicSet.append(obj)
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.OutputObjectPath = params.get("OutputObjectPath")
        self.SegmentObjectName = params.get("SegmentObjectName")
        if params.get("ObjectNumberFormat") is not None:
            self.ObjectNumberFormat = NumberFormat()
            self.ObjectNumberFormat._deserialize(params.get("ObjectNumberFormat"))
        if params.get("HeadTailParameter") is not None:
            self.HeadTailParameter = HeadTailParameter()
            self.HeadTailParameter._deserialize(params.get("HeadTailParameter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TranscodeTemplate(AbstractModel):
    """Details of a transcoding template

    """

    def __init__(self):
        r"""
        :param Definition: Unique ID of a transcoding template.
        :type Definition: str
        :param Container: Container format. Valid values: mp4, flv, hls, mp3, flac, ogg.
        :type Container: str
        :param Name: Name of a transcoding template.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Name: str
        :param Comment: Template description.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Comment: str
        :param Type: Template type. Valid values:
<li>Preset: Preset template;</li>
<li>Custom: Custom template.</li>
        :type Type: str
        :param RemoveVideo: Whether to remove video data. Valid values:
<li>0: Retain;</li>
<li>1: Remove.</li>
        :type RemoveVideo: int
        :param RemoveAudio: Whether to remove audio data. Valid values:
<li>0: Retain;</li>
<li>1: Remove.</li>
        :type RemoveAudio: int
        :param VideoTemplate: Video stream configuration parameter. This field is valid only when `RemoveVideo` is 0.
Note: This field may return null, indicating that no valid values can be obtained.
        :type VideoTemplate: :class:`tencentcloud.mps.v20190612.models.VideoTemplateInfo`
        :param AudioTemplate: Audio stream configuration parameter. This field is valid only when `RemoveAudio` is 0.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AudioTemplate: :class:`tencentcloud.mps.v20190612.models.AudioTemplateInfo`
        :param TEHDConfig: TESHD transcoding parameter. To enable it, please contact your Tencent Cloud sales rep.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TEHDConfig: :class:`tencentcloud.mps.v20190612.models.TEHDConfig`
        :param ContainerType: Container format filter. Valid values:
<li>Video: Video container format that can contain both video stream and audio stream;</li>
<li>PureAudio: Audio container format that can contain only audio stream.</li>
        :type ContainerType: str
        :param CreateTime: Creation time of a template in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F).
        :type CreateTime: str
        :param UpdateTime: Last modified time of a template in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F).
        :type UpdateTime: str
        """
        self.Definition = None
        self.Container = None
        self.Name = None
        self.Comment = None
        self.Type = None
        self.RemoveVideo = None
        self.RemoveAudio = None
        self.VideoTemplate = None
        self.AudioTemplate = None
        self.TEHDConfig = None
        self.ContainerType = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Container = params.get("Container")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.Type = params.get("Type")
        self.RemoveVideo = params.get("RemoveVideo")
        self.RemoveAudio = params.get("RemoveAudio")
        if params.get("VideoTemplate") is not None:
            self.VideoTemplate = VideoTemplateInfo()
            self.VideoTemplate._deserialize(params.get("VideoTemplate"))
        if params.get("AudioTemplate") is not None:
            self.AudioTemplate = AudioTemplateInfo()
            self.AudioTemplate._deserialize(params.get("AudioTemplate"))
        if params.get("TEHDConfig") is not None:
            self.TEHDConfig = TEHDConfig()
            self.TEHDConfig._deserialize(params.get("TEHDConfig"))
        self.ContainerType = params.get("ContainerType")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UrlInputInfo(AbstractModel):
    """Information of a video processing URL object.

    """

    def __init__(self):
        r"""
        :param Url: URL of a video.
        :type Url: str
        """
        self.Url = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserDefineAsrTextReviewTemplateInfo(AbstractModel):
    """Control parameter of a custom speech audit task

    """

    def __init__(self):
        r"""
        :param Switch: Switch of a custom speech audit task. Valid values:
<li>ON: Enables a custom speech audit task;</li>
<li>OFF: Disables a custom speech audit task.</li>
        :type Switch: str
        :param LabelSet: Custom speech filter tag. If an audit result contains the selected tag, it will be returned; if the filter tag is empty, all audit results will be returned. To use the tag filtering feature, you need to add the corresponding tag when adding materials for custom speech keywords.
There can be up to 10 tags, each with a length limit of 16 characters.
        :type LabelSet: list of str
        :param BlockConfidence: Threshold score for violation. If this score is reached or exceeded during intelligent audit, it will be deemed that a suspected violation has occurred. If this parameter is left empty, 100 will be used by default. Value range: 0-100.
        :type BlockConfidence: int
        :param ReviewConfidence: Threshold score for human audit. If this score is reached or exceeded during intelligent audit, human audit will be considered necessary. If this parameter is left empty, 75 will be used by default. Value range: 0-100.
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserDefineAsrTextReviewTemplateInfoForUpdate(AbstractModel):
    """Control parameter of a custom speech audit task

    """

    def __init__(self):
        r"""
        :param Switch: Switch of a custom speech audit task. Valid values:
<li>ON: Enables a custom speech audit task;</li>
<li>OFF: Disables a custom speech audit task.</li>
        :type Switch: str
        :param LabelSet: Custom speech filter tag. If an audit result contains the selected tag, it will be returned; if the filter tag is empty, all audit results will be returned. To use the tag filtering feature, you need to add the corresponding tag when adding materials for custom speech keywords.
There can be up to 10 tags, each with a length limit of 16 characters.
        :type LabelSet: list of str
        :param BlockConfidence: Threshold score for violation. If this score is reached or exceeded during intelligent audit, it will be deemed that a suspected violation has occurred. Value range: 0-100.
        :type BlockConfidence: int
        :param ReviewConfidence: Threshold score for human audit. If this score is reached or exceeded during intelligent audit, human audit will be considered necessary. Value range: 0-100.
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserDefineConfigureInfo(AbstractModel):
    """Control parameter of a custom audit task

    """

    def __init__(self):
        r"""
        :param FaceReviewInfo: Control parameter of custom figure audit.
Note: This field may return null, indicating that no valid values can be obtained.
        :type FaceReviewInfo: :class:`tencentcloud.mps.v20190612.models.UserDefineFaceReviewTemplateInfo`
        :param AsrReviewInfo: Control parameter of custom speech audit.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AsrReviewInfo: :class:`tencentcloud.mps.v20190612.models.UserDefineAsrTextReviewTemplateInfo`
        :param OcrReviewInfo: Control parameter of custom text audit.
Note: This field may return null, indicating that no valid values can be obtained.
        :type OcrReviewInfo: :class:`tencentcloud.mps.v20190612.models.UserDefineOcrTextReviewTemplateInfo`
        """
        self.FaceReviewInfo = None
        self.AsrReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("FaceReviewInfo") is not None:
            self.FaceReviewInfo = UserDefineFaceReviewTemplateInfo()
            self.FaceReviewInfo._deserialize(params.get("FaceReviewInfo"))
        if params.get("AsrReviewInfo") is not None:
            self.AsrReviewInfo = UserDefineAsrTextReviewTemplateInfo()
            self.AsrReviewInfo._deserialize(params.get("AsrReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = UserDefineOcrTextReviewTemplateInfo()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserDefineConfigureInfoForUpdate(AbstractModel):
    """Control parameter of a custom audit task.

    """

    def __init__(self):
        r"""
        :param FaceReviewInfo: Control parameter of custom figure audit.
        :type FaceReviewInfo: :class:`tencentcloud.mps.v20190612.models.UserDefineFaceReviewTemplateInfoForUpdate`
        :param AsrReviewInfo: Control parameter of custom speech audit.
        :type AsrReviewInfo: :class:`tencentcloud.mps.v20190612.models.UserDefineAsrTextReviewTemplateInfoForUpdate`
        :param OcrReviewInfo: Control parameter of custom text audit.
        :type OcrReviewInfo: :class:`tencentcloud.mps.v20190612.models.UserDefineOcrTextReviewTemplateInfoForUpdate`
        """
        self.FaceReviewInfo = None
        self.AsrReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("FaceReviewInfo") is not None:
            self.FaceReviewInfo = UserDefineFaceReviewTemplateInfoForUpdate()
            self.FaceReviewInfo._deserialize(params.get("FaceReviewInfo"))
        if params.get("AsrReviewInfo") is not None:
            self.AsrReviewInfo = UserDefineAsrTextReviewTemplateInfoForUpdate()
            self.AsrReviewInfo._deserialize(params.get("AsrReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = UserDefineOcrTextReviewTemplateInfoForUpdate()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserDefineFaceReviewTemplateInfo(AbstractModel):
    """Control parameter of a custom figure audit task

    """

    def __init__(self):
        r"""
        :param Switch: Switch of a custom figure audit task. Valid values:
<li>ON: Enables a custom figure audit task;</li>
<li>OFF: Disables a custom figure audit task.</li>
        :type Switch: str
        :param LabelSet: Custom figure filter tag. If an audit result contains the selected tag, it will be returned; if the filter tag is empty, all audit results will be returned. To use the tag filtering feature, you need to add the corresponding tag when adding materials for the custom figure library.
There can be up to 10 tags, each with a length limit of 16 characters.
        :type LabelSet: list of str
        :param BlockConfidence: Threshold score for violation. If this score is reached or exceeded during intelligent audit, it will be deemed that a suspected violation has occurred. If this parameter is left empty, 97 will be used by default. Value range: 0-100.
        :type BlockConfidence: int
        :param ReviewConfidence: Threshold score for human audit. If this score is reached or exceeded during intelligent audit, human audit will be considered necessary. If this parameter is left empty, 95 will be used by default. Value range: 0-100.
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserDefineFaceReviewTemplateInfoForUpdate(AbstractModel):
    """Control parameter of a custom figure audit task.

    """

    def __init__(self):
        r"""
        :param Switch: Switch of a custom figure audit task. Valid values:
<li>ON: Enables a custom figure audit task;</li>
<li>OFF: Disables a custom figure audit task.</li>
        :type Switch: str
        :param LabelSet: Custom figure filter tag. If an audit result contains the selected tag, it will be returned; if the filter tag is empty, all audit results will be returned. To use the tag filtering feature, you need to add the corresponding tag when adding materials for the custom figure library.
There can be up to 10 tags, each with a length limit of 16 characters.
        :type LabelSet: list of str
        :param BlockConfidence: Threshold score for violation. If this score is reached or exceeded during intelligent audit, it will be deemed that a suspected violation has occurred. Value range: 0-100.
        :type BlockConfidence: int
        :param ReviewConfidence: Threshold score for human audit. If this score is reached or exceeded during intelligent audit, human audit will be considered necessary. Value range: 0-100.
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserDefineOcrTextReviewTemplateInfo(AbstractModel):
    """Control parameter of a custom text audit task

    """

    def __init__(self):
        r"""
        :param Switch: Switch of a custom text audit task. Valid values:
<li>ON: Enables a custom text audit task;</li>
<li>OFF: Disables a custom text audit task.</li>
        :type Switch: str
        :param LabelSet: Custom text filter tag. If an audit result contains the selected tag, it will be returned; if the filter tag is empty, all audit results will be returned. To use the tag filtering feature, you need to add the corresponding tag when adding materials for custom text keywords.
There can be up to 10 tags, each with a length limit of 16 characters.
        :type LabelSet: list of str
        :param BlockConfidence: Threshold score for violation. If this score is reached or exceeded during intelligent audit, it will be deemed that a suspected violation has occurred. If this parameter is left empty, 100 will be used by default. Value range: 0-100.
        :type BlockConfidence: int
        :param ReviewConfidence: Threshold score for human audit. If this score is reached or exceeded during intelligent audit, human audit will be considered necessary. If this parameter is left empty, 75 will be used by default. Value range: 0-100.
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserDefineOcrTextReviewTemplateInfoForUpdate(AbstractModel):
    """Control parameter of a custom text audit task.

    """

    def __init__(self):
        r"""
        :param Switch: Switch of a custom text audit task. Valid values:
<li>ON: Enables a custom text audit task;</li>
<li>OFF: Disables a custom text audit task.</li>
        :type Switch: str
        :param LabelSet: Custom text filter tag. If an audit result contains the selected tag, it will be returned; if the filter tag is empty, all audit results will be returned. To use the tag filtering feature, you need to add the corresponding tag when adding materials for custom text keywords.
There can be up to 10 tags, each with a length limit of 16 characters.
        :type LabelSet: str
        :param BlockConfidence: Threshold score for violation. If this score is reached or exceeded during intelligent audit, it will be deemed that a suspected violation has occurred. Value range: 0-100.
        :type BlockConfidence: int
        :param ReviewConfidence: Threshold score for human audit. If this score is reached or exceeded during intelligent audit, human audit will be considered necessary. Value range: 0-100.
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoTemplateInfo(AbstractModel):
    """Video stream configuration parameter

    """

    def __init__(self):
        r"""
        :param Codec: Video stream codec. Valid values:
<li>`libx264`: H.264</li>
<li>`libx265`: H.265</li>
<li>`av1`: AOMedia Video 1</li>
        :type Codec: str
        :param Fps: Video frame rate in Hz. Value range: [0, 100].
If the value is 0, the frame rate will be the same as that of the source video.
        :type Fps: int
        :param Bitrate: Video stream bitrate (Kbps). Valid values: `0`; [75, 35000]
If the value is `0`, the original video bitrate will be used.
        :type Bitrate: int
        :param ResolutionAdaptive: Resolution adaption. Valid values:
<li>open: Enabled. In this case, `Width` represents the long side of a video, while `Height` the short side;</li>
<li>close: Disabled. In this case, `Width` represents the width of a video, while `Height` the height.</li>
Default value: open.
        :type ResolutionAdaptive: str
        :param Width: Maximum value of the width (or long side) of a video stream in px. Value range: 0 and [128, 4,096].
<li>If both `Width` and `Height` are 0, the resolution will be the same as that of the source video;</li>
<li>If `Width` is 0, but `Height` is not 0, `Width` will be proportionally scaled;</li>
<li>If `Width` is not 0, but `Height` is 0, `Height` will be proportionally scaled;</li>
<li>If both `Width` and `Height` are not 0, the custom resolution will be used.</li>
Default value: 0.
        :type Width: int
        :param Height: Maximum value of the height (or short side) of a video stream in px. Value range: 0 and [128, 4,096].
<li>If both `Width` and `Height` are 0, the resolution will be the same as that of the source video;</li>
<li>If `Width` is 0, but `Height` is not 0, `Width` will be proportionally scaled;</li>
<li>If `Width` is not 0, but `Height` is 0, `Height` will be proportionally scaled;</li>
<li>If both `Width` and `Height` are not 0, the custom resolution will be used.</li>
Default value: 0.
        :type Height: int
        :param Gop: Frame interval between I keyframes. Value range: 0 and [1,100000].
If this parameter is 0 or left empty, the system will automatically set the GOP length.
        :type Gop: int
        :param FillType: Fill type. "Fill" refers to the way of processing a screenshot when its aspect ratio is different from that of the source video. The following fill types are supported:
<li> stretch: stretch. The screenshot will be stretched frame by frame to match the aspect ratio of the source video, which may make the screenshot "shorter" or "longer";</li>
<li>black: fill with black. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with black color blocks.</li>
<li>white: fill with white. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with white color blocks.</li>
<li>gauss: fill with Gaussian blur. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with Gaussian blur.</li>
Default value: black.
        :type FillType: str
        :param Vcrf: The control factor of video constant bitrate. Value range: [1, 51]
If this parameter is specified, CRF (a bitrate control method) will be used for transcoding. (Video bitrate will no longer take effect.)
It is not recommended to specify this parameter if there are no special requirements.
        :type Vcrf: int
        """
        self.Codec = None
        self.Fps = None
        self.Bitrate = None
        self.ResolutionAdaptive = None
        self.Width = None
        self.Height = None
        self.Gop = None
        self.FillType = None
        self.Vcrf = None


    def _deserialize(self, params):
        self.Codec = params.get("Codec")
        self.Fps = params.get("Fps")
        self.Bitrate = params.get("Bitrate")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.Gop = params.get("Gop")
        self.FillType = params.get("FillType")
        self.Vcrf = params.get("Vcrf")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoTemplateInfoForUpdate(AbstractModel):
    """Video stream configuration parameter

    """

    def __init__(self):
        r"""
        :param Codec: Video stream codec. Valid values:
<li>libx264: H.264</li>
<li>libx265: H.265</li>
Currently, a resolution within 640*480p must be specified for H.265.
        :type Codec: str
        :param Fps: Video frame rate in Hz. Value range: [0, 100].
If the value is 0, the frame rate will be the same as that of the source video.
        :type Fps: int
        :param Bitrate: Bitrate of a video stream in Kbps. Value range: 0 and [128, 35,000].
If the value is 0, the bitrate of the video will be the same as that of the source video.
        :type Bitrate: int
        :param ResolutionAdaptive: Resolution adaption. Valid values:
<li>open: Enabled. In this case, `Width` represents the long side of a video, while `Height` the short side;</li>
<li>close: Disabled. In this case, `Width` represents the width of a video, while `Height` the height.</li>
        :type ResolutionAdaptive: str
        :param Width: Maximum value of the width (or long side) of a video stream in px. Value range: 0 and [128, 4,096].
<li>If both `Width` and `Height` are 0, the resolution will be the same as that of the source video;</li>
<li>If `Width` is 0, but `Height` is not 0, `Width` will be proportionally scaled;</li>
<li>If `Width` is not 0, but `Height` is 0, `Height` will be proportionally scaled;</li>
<li>If both `Width` and `Height` are not 0, the custom resolution will be used.</li>
        :type Width: int
        :param Height: Maximum value of the height (or short side) of a video stream in px. Value range: 0 and [128, 4,096].
        :type Height: int
        :param Gop: Frame interval between I keyframes. Value range: 0 and [1,100000]. If this parameter is 0, the system will automatically set the GOP length.
        :type Gop: int
        :param FillType: Fill type. "Fill" refers to the way of processing a screenshot when its aspect ratio is different from that of the source video. The following fill types are supported:
<li> stretch: stretch. The screenshot will be stretched frame by frame to match the aspect ratio of the source video, which may make the screenshot "shorter" or "longer";</li>
<li>black: fill with black. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with black color blocks.</li>
<li>white: fill with white. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with white color blocks.</li>
<li>gauss: fill with Gaussian blur. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with Gaussian blur.</li>
        :type FillType: str
        :param Vcrf: The control factor of video constant bitrate. Value range: [0, 51]. This parameter will be disabled if you enter `0`.
It is not recommended to specify this parameter if there are no special requirements.
        :type Vcrf: int
        :param ContentAdaptStream: Whether to enable adaptive encoding. Valid values:
<li>0: Disable</li>
<li>1: Enable</li>
Default value: 0. If this parameter is set to `1`, multiple streams with different resolutions and bitrates will be generated automatically. The highest resolution, bitrate, and quality of the streams are determined by the values of `width` and `height`, `Bitrate`, and `Vcrf` in `VideoTemplate` respectively. If these parameters are not set in `VideoTemplate`, the highest resolution generated will be the same as that of the source video, and the highest video quality will be close to VMAF 95. To use this parameter or learn about the billing details of adaptive encoding, please contact your sales rep.
        :type ContentAdaptStream: int
        """
        self.Codec = None
        self.Fps = None
        self.Bitrate = None
        self.ResolutionAdaptive = None
        self.Width = None
        self.Height = None
        self.Gop = None
        self.FillType = None
        self.Vcrf = None
        self.ContentAdaptStream = None


    def _deserialize(self, params):
        self.Codec = params.get("Codec")
        self.Fps = params.get("Fps")
        self.Bitrate = params.get("Bitrate")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.Gop = params.get("Gop")
        self.FillType = params.get("FillType")
        self.Vcrf = params.get("Vcrf")
        self.ContentAdaptStream = params.get("ContentAdaptStream")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WatermarkInput(AbstractModel):
    """Watermark parameter type of a video processing task

    """

    def __init__(self):
        r"""
        :param Definition: ID of a watermarking template.
        :type Definition: int
        :param RawParameter: Custom watermark parameter, which is valid if `Definition` is 0.
This parameter is used in highly customized scenarios. We recommend you use `Definition` to specify the watermark parameter preferably.
Custom watermark parameter is not available for screenshot.
        :type RawParameter: :class:`tencentcloud.mps.v20190612.models.RawWatermarkParameter`
        :param TextContent: Text content of up to 100 characters. This field is required only when the watermark type is text.
Text watermark is not available for screenshot.
        :type TextContent: str
        :param SvgContent: SVG content of up to 2,000,000 characters. This field is required only when the watermark type is `SVG`.
SVG watermark is not available for screenshot.
        :type SvgContent: str
        :param StartTimeOffset: Start time offset of a watermark in seconds. If this parameter is left empty or 0 is entered, the watermark will appear upon the first video frame.
<li>If this parameter is left empty or 0 is entered, the watermark will appear upon the first video frame;</li>
<li>If this value is greater than 0 (e.g., n), the watermark will appear at second n after the first video frame;</li>
<li>If this value is smaller than 0 (e.g., -n), the watermark will appear at second n before the last video frame.</li>
        :type StartTimeOffset: float
        :param EndTimeOffset: End time offset of a watermark in seconds.
<li>If this parameter is left empty or 0 is entered, the watermark will exist till the last video frame;</li>
<li>If this value is greater than 0 (e.g., n), the watermark will exist till second n;</li>
<li>If this value is smaller than 0 (e.g., -n), the watermark will exist till second n before the last video frame.</li>
        :type EndTimeOffset: float
        """
        self.Definition = None
        self.RawParameter = None
        self.TextContent = None
        self.SvgContent = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        if params.get("RawParameter") is not None:
            self.RawParameter = RawWatermarkParameter()
            self.RawParameter._deserialize(params.get("RawParameter"))
        self.TextContent = params.get("TextContent")
        self.SvgContent = params.get("SvgContent")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WatermarkTemplate(AbstractModel):
    """Details of a watermarking template

    """

    def __init__(self):
        r"""
        :param Definition: Unique ID of a watermarking template.
        :type Definition: int
        :param Type: Watermark type. Valid values:
<li>image: Image watermark;</li>
<li>text: Text watermark.</li>
        :type Type: str
        :param Name: Name of a watermarking template.
        :type Name: str
        :param Comment: Template description.
        :type Comment: str
        :param XPos: Horizontal position of the origin of the watermark image relative to the origin of the video.
<li>If the string ends in %, the `Left` edge of the watermark will be at the position of the specified percentage of the video width; for example, `10%` means that the `Left` edge is at 10% of the video width;</li>
<li>If the string ends in px, the `Left` edge of the watermark will be at the position of the specified px of the video width; for example, `100px` means that the `Left` edge is at the position of 100 px.</li>
        :type XPos: str
        :param YPos: Vertical position of the origin of the watermark image relative to the origin of the video.
<li>If the string ends in %, the `Top` edge of the watermark will beat the position of the specified percentage of the video height; for example, `10%` means that the `Top` edge is at 10% of the video height;</li>
<li>If the string ends in px, the `Top` edge of the watermark will be at the position of the specified px of the video height; for example, `100px` means that the `Top` edge is at the position of 100 px.</li>
        :type YPos: str
        :param ImageTemplate: Image watermarking template. This field is valid only when `Type` is `image`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ImageTemplate: :class:`tencentcloud.mps.v20190612.models.ImageWatermarkTemplate`
        :param TextTemplate: Text watermarking template. This field is valid only when `Type` is `text`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TextTemplate: :class:`tencentcloud.mps.v20190612.models.TextWatermarkTemplateInput`
        :param SvgTemplate: SVG watermarking template. This field is valid when `Type` is `svg`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SvgTemplate: :class:`tencentcloud.mps.v20190612.models.SvgWatermarkInput`
        :param CreateTime: Creation time of a template in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F).
        :type CreateTime: str
        :param UpdateTime: Last modified time of a template in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F).
        :type UpdateTime: str
        :param CoordinateOrigin: Origin position. Valid values:
<li>topLeft: The origin of coordinates is in the top-left corner of the video, and the origin of the watermark is in the top-left corner of the image or text;</li>
<li>topRight: The origin of coordinates is in the top-right corner of the video, and the origin of the watermark is in the top-right corner of the image or text;</li>
<li>bottomLeft: The origin of coordinates is in the bottom-left corner of the video, and the origin of the watermark is in the bottom-left corner of the image or text;</li>
<li>bottomRight: The origin of coordinates is in the bottom-right corner of the video, and the origin of the watermark is in the bottom-right corner of the image or text.</li>
        :type CoordinateOrigin: str
        """
        self.Definition = None
        self.Type = None
        self.Name = None
        self.Comment = None
        self.XPos = None
        self.YPos = None
        self.ImageTemplate = None
        self.TextTemplate = None
        self.SvgTemplate = None
        self.CreateTime = None
        self.UpdateTime = None
        self.CoordinateOrigin = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.XPos = params.get("XPos")
        self.YPos = params.get("YPos")
        if params.get("ImageTemplate") is not None:
            self.ImageTemplate = ImageWatermarkTemplate()
            self.ImageTemplate._deserialize(params.get("ImageTemplate"))
        if params.get("TextTemplate") is not None:
            self.TextTemplate = TextWatermarkTemplateInput()
            self.TextTemplate._deserialize(params.get("TextTemplate"))
        if params.get("SvgTemplate") is not None:
            self.SvgTemplate = SvgWatermarkInput()
            self.SvgTemplate._deserialize(params.get("SvgTemplate"))
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.CoordinateOrigin = params.get("CoordinateOrigin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkflowInfo(AbstractModel):
    """Workflow information details.

    """

    def __init__(self):
        r"""
        :param WorkflowId: Workflow ID.
        :type WorkflowId: int
        :param WorkflowName: Workflow name.
        :type WorkflowName: str
        :param Status: Workflow status. Valid values:
<li>Enabled: Enabled,</li>
<li>Disabled: Disabled.</li>
        :type Status: str
        :param Trigger: Input rule bound to a workflow. If an uploaded video hits the rule for the object, the workflow will be triggered.
        :type Trigger: :class:`tencentcloud.mps.v20190612.models.WorkflowTrigger`
        :param OutputStorage: Target storage of a video processing output file.
Note: This field may return null, indicating that no valid values can be obtained.
        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        :param MediaProcessTask: Parameter of a video processing task.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MediaProcessTask: :class:`tencentcloud.mps.v20190612.models.MediaProcessTaskInput`
        :param AiContentReviewTask: Type parameter of a video content audit task.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AiContentReviewTask: :class:`tencentcloud.mps.v20190612.models.AiContentReviewTaskInput`
        :param AiAnalysisTask: Video content analysis task parameter.
        :type AiAnalysisTask: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskInput`
        :param AiRecognitionTask: Type parameter of a video content recognition task.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AiRecognitionTask: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskInput`
        :param TaskNotifyConfig: Event notification information of a task. If this parameter is left empty, no event notifications will be obtained.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskNotifyConfig: :class:`tencentcloud.mps.v20190612.models.TaskNotifyConfig`
        :param TaskPriority: Task flow priority. The higher the value, the higher the priority. Value range: [-10, 10]. If this parameter is left empty, 0 will be used.
        :type TaskPriority: int
        :param OutputDir: Target directory of a video processing output file, such as `/movie/201907/`.
        :type OutputDir: str
        :param CreateTime: Creation time of a workflow in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F).
        :type CreateTime: str
        :param UpdateTime: Last modified time of a workflow in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F).
        :type UpdateTime: str
        """
        self.WorkflowId = None
        self.WorkflowName = None
        self.Status = None
        self.Trigger = None
        self.OutputStorage = None
        self.MediaProcessTask = None
        self.AiContentReviewTask = None
        self.AiAnalysisTask = None
        self.AiRecognitionTask = None
        self.TaskNotifyConfig = None
        self.TaskPriority = None
        self.OutputDir = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.WorkflowId = params.get("WorkflowId")
        self.WorkflowName = params.get("WorkflowName")
        self.Status = params.get("Status")
        if params.get("Trigger") is not None:
            self.Trigger = WorkflowTrigger()
            self.Trigger._deserialize(params.get("Trigger"))
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        if params.get("MediaProcessTask") is not None:
            self.MediaProcessTask = MediaProcessTaskInput()
            self.MediaProcessTask._deserialize(params.get("MediaProcessTask"))
        if params.get("AiContentReviewTask") is not None:
            self.AiContentReviewTask = AiContentReviewTaskInput()
            self.AiContentReviewTask._deserialize(params.get("AiContentReviewTask"))
        if params.get("AiAnalysisTask") is not None:
            self.AiAnalysisTask = AiAnalysisTaskInput()
            self.AiAnalysisTask._deserialize(params.get("AiAnalysisTask"))
        if params.get("AiRecognitionTask") is not None:
            self.AiRecognitionTask = AiRecognitionTaskInput()
            self.AiRecognitionTask._deserialize(params.get("AiRecognitionTask"))
        if params.get("TaskNotifyConfig") is not None:
            self.TaskNotifyConfig = TaskNotifyConfig()
            self.TaskNotifyConfig._deserialize(params.get("TaskNotifyConfig"))
        self.TaskPriority = params.get("TaskPriority")
        self.OutputDir = params.get("OutputDir")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkflowTask(AbstractModel):
    """Information of a video processing task

    """

    def __init__(self):
        r"""
        :param TaskId: Video processing task ID.
        :type TaskId: str
        :param Status: Task flow status. Valid values:
<li>PROCESSING: Processing;</li>
<li>FINISH: Completed.</li>
        :type Status: str
        :param ErrCode: Disused. Please use `ErrCode` of each specific task.
        :type ErrCode: int
        :param Message: Disused. Please use `Message` of each specific task.
        :type Message: str
        :param InputInfo: Information of a target file of video processing.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InputInfo: :class:`tencentcloud.mps.v20190612.models.MediaInputInfo`
        :param MetaData: Metadata of a source video.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MetaData: :class:`tencentcloud.mps.v20190612.models.MediaMetaData`
        :param MediaProcessResultSet: Execution status and result of a video processing task.
        :type MediaProcessResultSet: list of MediaProcessTaskResult
        :param AiContentReviewResultSet: Execution status and result of a video content audit task.
        :type AiContentReviewResultSet: list of AiContentReviewResult
        :param AiAnalysisResultSet: Execution status and result of video content analysis task.
        :type AiAnalysisResultSet: list of AiAnalysisResult
        :param AiRecognitionResultSet: Execution status and result of a video content recognition task.
        :type AiRecognitionResultSet: list of AiRecognitionResult
        """
        self.TaskId = None
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.InputInfo = None
        self.MetaData = None
        self.MediaProcessResultSet = None
        self.AiContentReviewResultSet = None
        self.AiAnalysisResultSet = None
        self.AiRecognitionResultSet = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("InputInfo") is not None:
            self.InputInfo = MediaInputInfo()
            self.InputInfo._deserialize(params.get("InputInfo"))
        if params.get("MetaData") is not None:
            self.MetaData = MediaMetaData()
            self.MetaData._deserialize(params.get("MetaData"))
        if params.get("MediaProcessResultSet") is not None:
            self.MediaProcessResultSet = []
            for item in params.get("MediaProcessResultSet"):
                obj = MediaProcessTaskResult()
                obj._deserialize(item)
                self.MediaProcessResultSet.append(obj)
        if params.get("AiContentReviewResultSet") is not None:
            self.AiContentReviewResultSet = []
            for item in params.get("AiContentReviewResultSet"):
                obj = AiContentReviewResult()
                obj._deserialize(item)
                self.AiContentReviewResultSet.append(obj)
        if params.get("AiAnalysisResultSet") is not None:
            self.AiAnalysisResultSet = []
            for item in params.get("AiAnalysisResultSet"):
                obj = AiAnalysisResult()
                obj._deserialize(item)
                self.AiAnalysisResultSet.append(obj)
        if params.get("AiRecognitionResultSet") is not None:
            self.AiRecognitionResultSet = []
            for item in params.get("AiRecognitionResultSet"):
                obj = AiRecognitionResult()
                obj._deserialize(item)
                self.AiRecognitionResultSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkflowTrigger(AbstractModel):
    """Input rule. If an uploaded video hits the rule, the workflow will be triggered.

    """

    def __init__(self):
        r"""
        :param Type: Trigger type. Only `CosFileUpload` is supported currently.
        :type Type: str
        :param CosFileUploadTrigger: This parameter is required and valid when `Type` is `CosFileUpload`, indicating the COS trigger rule.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CosFileUploadTrigger: :class:`tencentcloud.mps.v20190612.models.CosFileUploadTrigger`
        """
        self.Type = None
        self.CosFileUploadTrigger = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("CosFileUploadTrigger") is not None:
            self.CosFileUploadTrigger = CosFileUploadTrigger()
            self.CosFileUploadTrigger._deserialize(params.get("CosFileUploadTrigger"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        