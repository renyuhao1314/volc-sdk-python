# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: volcengine/vod/business/vod_measure.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)volcengine/vod/business/vod_measure.proto\x12\x1eVolcengine.Vod.Models.Business\"<\n\x1d\x44\x65scribeVodSpaceTranscodeItem\x12\x0c\n\x04Name\x18\x01 \x01(\t\x12\r\n\x05Value\x18\x02 \x01(\x03\"\x8f\x01\n%DescribeVodSpaceTranscodeDetailTVUnit\x12\x0c\n\x04Time\x18\x01 \x01(\t\x12X\n\x11TranscodeItemList\x18\x02 \x03(\x0b\x32=.Volcengine.Vod.Models.Business.DescribeVodSpaceTranscodeItem\"\xb5\x01\n\x1f\x44\x65scribeVodSpaceTranscodeDetail\x12\r\n\x05Space\x18\x01 \x01(\t\x12\x11\n\tTaskStage\x18\x02 \x01(\t\x12\r\n\x05Total\x18\x03 \x01(\x03\x12\x61\n\x12TranscodeUsageList\x18\x04 \x03(\x0b\x32\x45.Volcengine.Vod.Models.Business.DescribeVodSpaceTranscodeDetailTVUnit\"\xc0\x03\n#DescribeVodSpaceTranscodeDataResult\x12\x11\n\tSpaceList\x18\x01 \x03(\t\x12\x11\n\tStartTime\x18\x02 \x01(\t\x12\x0f\n\x07\x45ndTime\x18\x03 \x01(\t\x12\x15\n\rTranscodeType\x18\x04 \x01(\t\x12\x15\n\rSpecification\x18\x05 \x01(\t\x12\x15\n\rTaskStageList\x18\x06 \x03(\t\x12\x13\n\x0b\x41ggregation\x18\x07 \x01(\x03\x12\x17\n\x0f\x44\x65tailFieldList\x18\x08 \x03(\t\x12\x12\n\nRegionList\x18\t \x03(\t\x12\x1a\n\x12TotalTranscodeData\x18\n \x01(\x03\x12]\n\x16TotalTranscodeDataList\x18\x0b \x03(\x0b\x32=.Volcengine.Vod.Models.Business.DescribeVodSpaceTranscodeItem\x12`\n\x17TranscodeDataDetailList\x18\x0c \x03(\x0b\x32?.Volcengine.Vod.Models.Business.DescribeVodSpaceTranscodeDetail\"B\n DescribeVodSpaceAIStatisDataItem\x12\x0c\n\x04Time\x18\x01 \x01(\t\x12\x10\n\x08\x44uration\x18\x02 \x01(\x03\"\xa1\x01\n\"DescribeVodSpaceAIStatisDataDetail\x12\r\n\x05Space\x18\x01 \x01(\t\x12\x11\n\tTaskStage\x18\x02 \x01(\t\x12Y\n\x0f\x41iUsageDataList\x18\x03 \x03(\x0b\x32@.Volcengine.Vod.Models.Business.DescribeVodSpaceAIStatisDataItem\"\xa1\x03\n\"DescribeVodSpaceAIStatisDataResult\x12\x11\n\tSpaceList\x18\x01 \x03(\t\x12\x11\n\tStartTime\x18\x02 \x01(\t\x12\x0f\n\x07\x45ndTime\x18\x03 \x01(\t\x12\x13\n\x0bMediaAiType\x18\x04 \x01(\t\x12\x15\n\rTaskStageList\x18\x05 \x03(\t\x12\x13\n\x0b\x41ggregation\x18\x06 \x01(\x03\x12\x17\n\x0f\x44\x65tailFieldList\x18\x07 \x03(\t\x12\x12\n\nRegionList\x18\x08 \x03(\t\x12\x18\n\x10TotalAiUsageData\x18\t \x01(\x03\x12Y\n\x0f\x41iUsageDataList\x18\n \x03(\x0b\x32@.Volcengine.Vod.Models.Business.DescribeVodSpaceAIStatisDataItem\x12\x61\n\x15\x41iUsageDataDetailList\x18\x0b \x03(\x0b\x32\x42.Volcengine.Vod.Models.Business.DescribeVodSpaceAIStatisDataDetail\"E\n&DescribeVodSpaceSubtitleStatisDataItem\x12\x0c\n\x04Time\x18\x01 \x01(\t\x12\r\n\x05Usage\x18\x02 \x01(\x03\"\xb3\x01\n(DescribeVodSpaceSubtitleStatisDataDetail\x12\r\n\x05Space\x18\x01 \x01(\t\x12\x11\n\tTaskStage\x18\x02 \x01(\t\x12\x65\n\x15SubtitleUsageDataList\x18\x03 \x03(\x0b\x32\x46.Volcengine.Vod.Models.Business.DescribeVodSpaceSubtitleStatisDataItem\"\xc6\x03\n(DescribeVodSpaceSubtitleStatisDataResult\x12\x11\n\tSpaceList\x18\x01 \x03(\t\x12\x11\n\tStartTime\x18\x02 \x01(\t\x12\x0f\n\x07\x45ndTime\x18\x03 \x01(\t\x12\x14\n\x0cSubtitleType\x18\x04 \x01(\t\x12\x15\n\rTaskStageList\x18\x05 \x03(\t\x12\x13\n\x0b\x41ggregation\x18\x06 \x01(\x03\x12\x17\n\x0f\x44\x65tailFieldList\x18\x07 \x03(\t\x12\x12\n\nRegionList\x18\x08 \x03(\t\x12\x1e\n\x16TotalSubtitleUsageData\x18\t \x01(\x03\x12\x65\n\x15SubtitleUsageDataList\x18\n \x03(\x0b\x32\x46.Volcengine.Vod.Models.Business.DescribeVodSpaceSubtitleStatisDataItem\x12m\n\x1bSubtitleUsageDataDetailList\x18\x0b \x03(\x0b\x32H.Volcengine.Vod.Models.Business.DescribeVodSpaceSubtitleStatisDataDetail\"C\n$DescribeVodSpaceDetectStatisDataItem\x12\x0c\n\x04Time\x18\x01 \x01(\t\x12\r\n\x05Usage\x18\x02 \x01(\x03\"\xad\x01\n&DescribeVodSpaceDetectStatisDataDetail\x12\r\n\x05Space\x18\x01 \x01(\t\x12\x11\n\tTaskStage\x18\x02 \x01(\t\x12\x61\n\x13\x44\x65tectUsageDataList\x18\x03 \x03(\x0b\x32\x44.Volcengine.Vod.Models.Business.DescribeVodSpaceDetectStatisDataItem\"\xb8\x03\n&DescribeVodSpaceDetectStatisDataResult\x12\x11\n\tSpaceList\x18\x01 \x03(\t\x12\x11\n\tStartTime\x18\x02 \x01(\t\x12\x0f\n\x07\x45ndTime\x18\x03 \x01(\t\x12\x12\n\nDetectType\x18\x04 \x01(\t\x12\x15\n\rTaskStageList\x18\x05 \x03(\t\x12\x13\n\x0b\x41ggregation\x18\x06 \x01(\x03\x12\x17\n\x0f\x44\x65tailFieldList\x18\x07 \x03(\t\x12\x12\n\nRegionList\x18\x08 \x03(\t\x12\x1c\n\x14TotalDetectUsageData\x18\t \x01(\x03\x12\x61\n\x13\x44\x65tectUsageDataList\x18\n \x03(\x0b\x32\x44.Volcengine.Vod.Models.Business.DescribeVodSpaceDetectStatisDataItem\x12i\n\x19\x44\x65tectUsageDataDetailList\x18\x0b \x03(\x0b\x32\x46.Volcengine.Vod.Models.Business.DescribeVodSpaceDetectStatisDataDetail\":\n\x1b\x44\x65scribeVodSnapshotDataItem\x12\x0c\n\x04Time\x18\x01 \x01(\t\x12\r\n\x05\x43ount\x18\x02 \x01(\x03\"\xa7\x01\n\x1d\x44\x65scribeVodSnapshotDataDetail\x12\r\n\x05Space\x18\x01 \x01(\t\x12\x11\n\tTaskStage\x18\x02 \x01(\t\x12\r\n\x05Total\x18\x03 \x01(\t\x12U\n\x10SnapshotDataList\x18\x04 \x03(\x0b\x32;.Volcengine.Vod.Models.Business.DescribeVodSnapshotDataItem\"\x96\x03\n\x1d\x44\x65scribeVodSnapshotDataResult\x12\x11\n\tSpaceList\x18\x01 \x03(\t\x12\x11\n\tStartTime\x18\x02 \x01(\t\x12\x0f\n\x07\x45ndTime\x18\x03 \x01(\t\x12\x14\n\x0cSnapshotType\x18\x04 \x01(\t\x12\x15\n\rTaskStageList\x18\x05 \x03(\t\x12\x13\n\x0b\x41ggregation\x18\x06 \x01(\x03\x12\x17\n\x0f\x44\x65tailFieldList\x18\x07 \x03(\t\x12\x12\n\nRegionList\x18\x08 \x03(\t\x12\x19\n\x11TotalSnapshotData\x18\t \x01(\x03\x12U\n\x10SnapshotDataList\x18\n \x03(\x0b\x32;.Volcengine.Vod.Models.Business.DescribeVodSnapshotDataItem\x12]\n\x16SnapshotDetailDataList\x18\x0b \x03(\x0b\x32=.Volcengine.Vod.Models.Business.DescribeVodSnapshotDataDetail\"\xd8\x01\n%DescribeVodSpaceWorkflowTranscodeInfo\x12\x14\n\x0cTemplateType\x18\x01 \x01(\t\x12\x10\n\x08\x46ileType\x18\x02 \x01(\t\x12\x10\n\x08\x44uration\x18\x03 \x01(\x03\x12\r\n\x05\x43odec\x18\x04 \x01(\t\x12\r\n\x05Remux\x18\x05 \x01(\x08\x12\x12\n\nDefinition\x18\x06 \x01(\t\x12\r\n\x05Width\x18\x07 \x01(\x03\x12\x0e\n\x06Height\x18\x08 \x01(\x03\x12\r\n\x05Slice\x18\t \x01(\x08\x12\x15\n\rIsLowPriority\x18\n \x01(\x08\"c\n$DescribeVodSpaceWorkflowSnapshotInfo\x12\x14\n\x0cTemplateType\x18\x01 \x01(\t\x12\x0e\n\x06Number\x18\x02 \x01(\x03\x12\x15\n\rIsLowPriority\x18\x03 \x01(\x08\"h\n\'DescribeVodSpaceWorkflowEnhanceExecInfo\x12\x14\n\x0cTemplateType\x18\x01 \x01(\t\x12\x10\n\x08\x44uration\x18\x02 \x01(\x03\x12\x15\n\rIsLowPriority\x18\x03 \x01(\x08\"t\n#DescribeVodSpaceWorkflowVideoAIInfo\x12\x14\n\x0cTemplateType\x18\x01 \x01(\t\x12\x10\n\x08\x44uration\x18\x02 \x01(\x03\x12\x0e\n\x06Number\x18\x03 \x01(\x03\x12\x15\n\rIsLowPriority\x18\x04 \x01(\x08\"\x8d\x04\n\x1e\x44\x65scribeVodSpaceWorkflowDetail\x12\r\n\x05RunId\x18\x01 \x01(\t\x12\x0b\n\x03Vid\x18\x02 \x01(\t\x12\x12\n\nTemplateId\x18\x03 \x01(\t\x12\x11\n\tSpaceName\x18\x04 \x01(\t\x12\x0e\n\x06Status\x18\x05 \x01(\t\x12\x11\n\tStartTime\x18\x06 \x01(\t\x12\x0f\n\x07\x45ndTime\x18\x07 \x01(\t\x12\\\n\rTranscodeInfo\x18\x08 \x01(\x0b\x32\x45.Volcengine.Vod.Models.Business.DescribeVodSpaceWorkflowTranscodeInfo\x12Z\n\x0cSnapshotInfo\x18\t \x01(\x0b\x32\x44.Volcengine.Vod.Models.Business.DescribeVodSpaceWorkflowSnapshotInfo\x12`\n\x0f\x45nhanceExecInfo\x18\n \x01(\x0b\x32G.Volcengine.Vod.Models.Business.DescribeVodSpaceWorkflowEnhanceExecInfo\x12X\n\x0bVideoAIInfo\x18\x0b \x01(\x0b\x32\x43.Volcengine.Vod.Models.Business.DescribeVodSpaceWorkflowVideoAIInfo\"\xfb\x01\n(DescribeVodSpaceWorkflowDetailDataResult\x12\x0e\n\x06Region\x18\x01 \x01(\t\x12\r\n\x05Space\x18\x02 \x01(\t\x12\x11\n\tStartTime\x18\x03 \x01(\t\x12\x0f\n\x07\x45ndTime\x18\x04 \x01(\t\x12\x10\n\x08PageSize\x18\x05 \x01(\x03\x12\x0f\n\x07PageNum\x18\x06 \x01(\x03\x12\r\n\x05Total\x18\x07 \x01(\x03\x12Z\n\x12WorkflowDetailData\x18\x08 \x03(\x0b\x32>.Volcengine.Vod.Models.Business.DescribeVodSpaceWorkflowDetail\"\x81\x01\n\x1a\x44\x65scribeVodSpaceEditDetail\x12\x0c\n\x04Time\x18\x01 \x01(\t\x12\x11\n\tOutputVid\x18\x02 \x01(\t\x12\r\n\x05Space\x18\x03 \x01(\t\x12\r\n\x05\x43odec\x18\x04 \x01(\t\x12\x12\n\nDefinition\x18\x05 \x01(\t\x12\x10\n\x08\x44uration\x18\x06 \x01(\x03\"\xef\x01\n$DescribeVodSpaceEditDetailDataResult\x12\x0e\n\x06Region\x18\x01 \x01(\t\x12\r\n\x05Space\x18\x02 \x01(\t\x12\x11\n\tStartTime\x18\x03 \x01(\t\x12\x0f\n\x07\x45ndTime\x18\x04 \x01(\t\x12\x10\n\x08PageSize\x18\x05 \x01(\x03\x12\x0f\n\x07PageNum\x18\x06 \x01(\x03\x12\r\n\x05Total\x18\x07 \x01(\x03\x12R\n\x0e\x45\x64itDetailData\x18\x08 \x03(\x0b\x32:.Volcengine.Vod.Models.Business.DescribeVodSpaceEditDetail\"W\n\"DescribeVodPlayFileLogByDomainItem\x12\x0c\n\x04\x44\x61te\x18\x01 \x01(\t\x12\x0e\n\x06\x44omain\x18\x02 \x01(\t\x12\x13\n\x0b\x44ownloadUrl\x18\x03 \x01(\t\"\xb4\x01\n$DescribeVodPlayFileLogByDomainResult\x12\x11\n\tStartTime\x18\x01 \x01(\t\x12\x0f\n\x07\x45ndTime\x18\x02 \x01(\t\x12\x12\n\nDomainList\x18\x03 \x03(\t\x12T\n\x08\x46ileList\x18\x04 \x03(\x0b\x32\x42.Volcengine.Vod.Models.Business.DescribeVodPlayFileLogByDomainItemB\xcb\x01\n)com.volcengine.service.vod.model.businessB\nVodMeasureP\x01ZAgithub.com/volcengine/volc-sdk-golang/service/vod/models/business\xa0\x01\x01\xd8\x01\x01\xca\x02 Volc\\Service\\Vod\\Models\\Business\xe2\x02#Volc\\Service\\Vod\\Models\\GPBMetadatab\x06proto3')



_DESCRIBEVODSPACETRANSCODEITEM = DESCRIPTOR.message_types_by_name['DescribeVodSpaceTranscodeItem']
_DESCRIBEVODSPACETRANSCODEDETAILTVUNIT = DESCRIPTOR.message_types_by_name['DescribeVodSpaceTranscodeDetailTVUnit']
_DESCRIBEVODSPACETRANSCODEDETAIL = DESCRIPTOR.message_types_by_name['DescribeVodSpaceTranscodeDetail']
_DESCRIBEVODSPACETRANSCODEDATARESULT = DESCRIPTOR.message_types_by_name['DescribeVodSpaceTranscodeDataResult']
_DESCRIBEVODSPACEAISTATISDATAITEM = DESCRIPTOR.message_types_by_name['DescribeVodSpaceAIStatisDataItem']
_DESCRIBEVODSPACEAISTATISDATADETAIL = DESCRIPTOR.message_types_by_name['DescribeVodSpaceAIStatisDataDetail']
_DESCRIBEVODSPACEAISTATISDATARESULT = DESCRIPTOR.message_types_by_name['DescribeVodSpaceAIStatisDataResult']
_DESCRIBEVODSPACESUBTITLESTATISDATAITEM = DESCRIPTOR.message_types_by_name['DescribeVodSpaceSubtitleStatisDataItem']
_DESCRIBEVODSPACESUBTITLESTATISDATADETAIL = DESCRIPTOR.message_types_by_name['DescribeVodSpaceSubtitleStatisDataDetail']
_DESCRIBEVODSPACESUBTITLESTATISDATARESULT = DESCRIPTOR.message_types_by_name['DescribeVodSpaceSubtitleStatisDataResult']
_DESCRIBEVODSPACEDETECTSTATISDATAITEM = DESCRIPTOR.message_types_by_name['DescribeVodSpaceDetectStatisDataItem']
_DESCRIBEVODSPACEDETECTSTATISDATADETAIL = DESCRIPTOR.message_types_by_name['DescribeVodSpaceDetectStatisDataDetail']
_DESCRIBEVODSPACEDETECTSTATISDATARESULT = DESCRIPTOR.message_types_by_name['DescribeVodSpaceDetectStatisDataResult']
_DESCRIBEVODSNAPSHOTDATAITEM = DESCRIPTOR.message_types_by_name['DescribeVodSnapshotDataItem']
_DESCRIBEVODSNAPSHOTDATADETAIL = DESCRIPTOR.message_types_by_name['DescribeVodSnapshotDataDetail']
_DESCRIBEVODSNAPSHOTDATARESULT = DESCRIPTOR.message_types_by_name['DescribeVodSnapshotDataResult']
_DESCRIBEVODSPACEWORKFLOWTRANSCODEINFO = DESCRIPTOR.message_types_by_name['DescribeVodSpaceWorkflowTranscodeInfo']
_DESCRIBEVODSPACEWORKFLOWSNAPSHOTINFO = DESCRIPTOR.message_types_by_name['DescribeVodSpaceWorkflowSnapshotInfo']
_DESCRIBEVODSPACEWORKFLOWENHANCEEXECINFO = DESCRIPTOR.message_types_by_name['DescribeVodSpaceWorkflowEnhanceExecInfo']
_DESCRIBEVODSPACEWORKFLOWVIDEOAIINFO = DESCRIPTOR.message_types_by_name['DescribeVodSpaceWorkflowVideoAIInfo']
_DESCRIBEVODSPACEWORKFLOWDETAIL = DESCRIPTOR.message_types_by_name['DescribeVodSpaceWorkflowDetail']
_DESCRIBEVODSPACEWORKFLOWDETAILDATARESULT = DESCRIPTOR.message_types_by_name['DescribeVodSpaceWorkflowDetailDataResult']
_DESCRIBEVODSPACEEDITDETAIL = DESCRIPTOR.message_types_by_name['DescribeVodSpaceEditDetail']
_DESCRIBEVODSPACEEDITDETAILDATARESULT = DESCRIPTOR.message_types_by_name['DescribeVodSpaceEditDetailDataResult']
_DESCRIBEVODPLAYFILELOGBYDOMAINITEM = DESCRIPTOR.message_types_by_name['DescribeVodPlayFileLogByDomainItem']
_DESCRIBEVODPLAYFILELOGBYDOMAINRESULT = DESCRIPTOR.message_types_by_name['DescribeVodPlayFileLogByDomainResult']
DescribeVodSpaceTranscodeItem = _reflection.GeneratedProtocolMessageType('DescribeVodSpaceTranscodeItem', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEVODSPACETRANSCODEITEM,
  '__module__' : 'volcengine.vod.business.vod_measure_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.DescribeVodSpaceTranscodeItem)
  })
_sym_db.RegisterMessage(DescribeVodSpaceTranscodeItem)

DescribeVodSpaceTranscodeDetailTVUnit = _reflection.GeneratedProtocolMessageType('DescribeVodSpaceTranscodeDetailTVUnit', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEVODSPACETRANSCODEDETAILTVUNIT,
  '__module__' : 'volcengine.vod.business.vod_measure_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.DescribeVodSpaceTranscodeDetailTVUnit)
  })
_sym_db.RegisterMessage(DescribeVodSpaceTranscodeDetailTVUnit)

DescribeVodSpaceTranscodeDetail = _reflection.GeneratedProtocolMessageType('DescribeVodSpaceTranscodeDetail', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEVODSPACETRANSCODEDETAIL,
  '__module__' : 'volcengine.vod.business.vod_measure_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.DescribeVodSpaceTranscodeDetail)
  })
_sym_db.RegisterMessage(DescribeVodSpaceTranscodeDetail)

DescribeVodSpaceTranscodeDataResult = _reflection.GeneratedProtocolMessageType('DescribeVodSpaceTranscodeDataResult', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEVODSPACETRANSCODEDATARESULT,
  '__module__' : 'volcengine.vod.business.vod_measure_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.DescribeVodSpaceTranscodeDataResult)
  })
_sym_db.RegisterMessage(DescribeVodSpaceTranscodeDataResult)

DescribeVodSpaceAIStatisDataItem = _reflection.GeneratedProtocolMessageType('DescribeVodSpaceAIStatisDataItem', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEVODSPACEAISTATISDATAITEM,
  '__module__' : 'volcengine.vod.business.vod_measure_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.DescribeVodSpaceAIStatisDataItem)
  })
_sym_db.RegisterMessage(DescribeVodSpaceAIStatisDataItem)

DescribeVodSpaceAIStatisDataDetail = _reflection.GeneratedProtocolMessageType('DescribeVodSpaceAIStatisDataDetail', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEVODSPACEAISTATISDATADETAIL,
  '__module__' : 'volcengine.vod.business.vod_measure_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.DescribeVodSpaceAIStatisDataDetail)
  })
_sym_db.RegisterMessage(DescribeVodSpaceAIStatisDataDetail)

DescribeVodSpaceAIStatisDataResult = _reflection.GeneratedProtocolMessageType('DescribeVodSpaceAIStatisDataResult', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEVODSPACEAISTATISDATARESULT,
  '__module__' : 'volcengine.vod.business.vod_measure_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.DescribeVodSpaceAIStatisDataResult)
  })
_sym_db.RegisterMessage(DescribeVodSpaceAIStatisDataResult)

DescribeVodSpaceSubtitleStatisDataItem = _reflection.GeneratedProtocolMessageType('DescribeVodSpaceSubtitleStatisDataItem', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEVODSPACESUBTITLESTATISDATAITEM,
  '__module__' : 'volcengine.vod.business.vod_measure_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.DescribeVodSpaceSubtitleStatisDataItem)
  })
_sym_db.RegisterMessage(DescribeVodSpaceSubtitleStatisDataItem)

DescribeVodSpaceSubtitleStatisDataDetail = _reflection.GeneratedProtocolMessageType('DescribeVodSpaceSubtitleStatisDataDetail', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEVODSPACESUBTITLESTATISDATADETAIL,
  '__module__' : 'volcengine.vod.business.vod_measure_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.DescribeVodSpaceSubtitleStatisDataDetail)
  })
_sym_db.RegisterMessage(DescribeVodSpaceSubtitleStatisDataDetail)

DescribeVodSpaceSubtitleStatisDataResult = _reflection.GeneratedProtocolMessageType('DescribeVodSpaceSubtitleStatisDataResult', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEVODSPACESUBTITLESTATISDATARESULT,
  '__module__' : 'volcengine.vod.business.vod_measure_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.DescribeVodSpaceSubtitleStatisDataResult)
  })
_sym_db.RegisterMessage(DescribeVodSpaceSubtitleStatisDataResult)

DescribeVodSpaceDetectStatisDataItem = _reflection.GeneratedProtocolMessageType('DescribeVodSpaceDetectStatisDataItem', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEVODSPACEDETECTSTATISDATAITEM,
  '__module__' : 'volcengine.vod.business.vod_measure_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.DescribeVodSpaceDetectStatisDataItem)
  })
_sym_db.RegisterMessage(DescribeVodSpaceDetectStatisDataItem)

DescribeVodSpaceDetectStatisDataDetail = _reflection.GeneratedProtocolMessageType('DescribeVodSpaceDetectStatisDataDetail', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEVODSPACEDETECTSTATISDATADETAIL,
  '__module__' : 'volcengine.vod.business.vod_measure_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.DescribeVodSpaceDetectStatisDataDetail)
  })
_sym_db.RegisterMessage(DescribeVodSpaceDetectStatisDataDetail)

DescribeVodSpaceDetectStatisDataResult = _reflection.GeneratedProtocolMessageType('DescribeVodSpaceDetectStatisDataResult', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEVODSPACEDETECTSTATISDATARESULT,
  '__module__' : 'volcengine.vod.business.vod_measure_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.DescribeVodSpaceDetectStatisDataResult)
  })
_sym_db.RegisterMessage(DescribeVodSpaceDetectStatisDataResult)

DescribeVodSnapshotDataItem = _reflection.GeneratedProtocolMessageType('DescribeVodSnapshotDataItem', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEVODSNAPSHOTDATAITEM,
  '__module__' : 'volcengine.vod.business.vod_measure_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.DescribeVodSnapshotDataItem)
  })
_sym_db.RegisterMessage(DescribeVodSnapshotDataItem)

DescribeVodSnapshotDataDetail = _reflection.GeneratedProtocolMessageType('DescribeVodSnapshotDataDetail', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEVODSNAPSHOTDATADETAIL,
  '__module__' : 'volcengine.vod.business.vod_measure_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.DescribeVodSnapshotDataDetail)
  })
_sym_db.RegisterMessage(DescribeVodSnapshotDataDetail)

DescribeVodSnapshotDataResult = _reflection.GeneratedProtocolMessageType('DescribeVodSnapshotDataResult', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEVODSNAPSHOTDATARESULT,
  '__module__' : 'volcengine.vod.business.vod_measure_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.DescribeVodSnapshotDataResult)
  })
_sym_db.RegisterMessage(DescribeVodSnapshotDataResult)

DescribeVodSpaceWorkflowTranscodeInfo = _reflection.GeneratedProtocolMessageType('DescribeVodSpaceWorkflowTranscodeInfo', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEVODSPACEWORKFLOWTRANSCODEINFO,
  '__module__' : 'volcengine.vod.business.vod_measure_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.DescribeVodSpaceWorkflowTranscodeInfo)
  })
_sym_db.RegisterMessage(DescribeVodSpaceWorkflowTranscodeInfo)

DescribeVodSpaceWorkflowSnapshotInfo = _reflection.GeneratedProtocolMessageType('DescribeVodSpaceWorkflowSnapshotInfo', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEVODSPACEWORKFLOWSNAPSHOTINFO,
  '__module__' : 'volcengine.vod.business.vod_measure_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.DescribeVodSpaceWorkflowSnapshotInfo)
  })
_sym_db.RegisterMessage(DescribeVodSpaceWorkflowSnapshotInfo)

DescribeVodSpaceWorkflowEnhanceExecInfo = _reflection.GeneratedProtocolMessageType('DescribeVodSpaceWorkflowEnhanceExecInfo', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEVODSPACEWORKFLOWENHANCEEXECINFO,
  '__module__' : 'volcengine.vod.business.vod_measure_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.DescribeVodSpaceWorkflowEnhanceExecInfo)
  })
_sym_db.RegisterMessage(DescribeVodSpaceWorkflowEnhanceExecInfo)

DescribeVodSpaceWorkflowVideoAIInfo = _reflection.GeneratedProtocolMessageType('DescribeVodSpaceWorkflowVideoAIInfo', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEVODSPACEWORKFLOWVIDEOAIINFO,
  '__module__' : 'volcengine.vod.business.vod_measure_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.DescribeVodSpaceWorkflowVideoAIInfo)
  })
_sym_db.RegisterMessage(DescribeVodSpaceWorkflowVideoAIInfo)

DescribeVodSpaceWorkflowDetail = _reflection.GeneratedProtocolMessageType('DescribeVodSpaceWorkflowDetail', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEVODSPACEWORKFLOWDETAIL,
  '__module__' : 'volcengine.vod.business.vod_measure_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.DescribeVodSpaceWorkflowDetail)
  })
_sym_db.RegisterMessage(DescribeVodSpaceWorkflowDetail)

DescribeVodSpaceWorkflowDetailDataResult = _reflection.GeneratedProtocolMessageType('DescribeVodSpaceWorkflowDetailDataResult', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEVODSPACEWORKFLOWDETAILDATARESULT,
  '__module__' : 'volcengine.vod.business.vod_measure_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.DescribeVodSpaceWorkflowDetailDataResult)
  })
_sym_db.RegisterMessage(DescribeVodSpaceWorkflowDetailDataResult)

DescribeVodSpaceEditDetail = _reflection.GeneratedProtocolMessageType('DescribeVodSpaceEditDetail', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEVODSPACEEDITDETAIL,
  '__module__' : 'volcengine.vod.business.vod_measure_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.DescribeVodSpaceEditDetail)
  })
_sym_db.RegisterMessage(DescribeVodSpaceEditDetail)

DescribeVodSpaceEditDetailDataResult = _reflection.GeneratedProtocolMessageType('DescribeVodSpaceEditDetailDataResult', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEVODSPACEEDITDETAILDATARESULT,
  '__module__' : 'volcengine.vod.business.vod_measure_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.DescribeVodSpaceEditDetailDataResult)
  })
_sym_db.RegisterMessage(DescribeVodSpaceEditDetailDataResult)

DescribeVodPlayFileLogByDomainItem = _reflection.GeneratedProtocolMessageType('DescribeVodPlayFileLogByDomainItem', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEVODPLAYFILELOGBYDOMAINITEM,
  '__module__' : 'volcengine.vod.business.vod_measure_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.DescribeVodPlayFileLogByDomainItem)
  })
_sym_db.RegisterMessage(DescribeVodPlayFileLogByDomainItem)

DescribeVodPlayFileLogByDomainResult = _reflection.GeneratedProtocolMessageType('DescribeVodPlayFileLogByDomainResult', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEVODPLAYFILELOGBYDOMAINRESULT,
  '__module__' : 'volcengine.vod.business.vod_measure_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.DescribeVodPlayFileLogByDomainResult)
  })
_sym_db.RegisterMessage(DescribeVodPlayFileLogByDomainResult)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n)com.volcengine.service.vod.model.businessB\nVodMeasureP\001ZAgithub.com/volcengine/volc-sdk-golang/service/vod/models/business\240\001\001\330\001\001\312\002 Volc\\Service\\Vod\\Models\\Business\342\002#Volc\\Service\\Vod\\Models\\GPBMetadata'
  _DESCRIBEVODSPACETRANSCODEITEM._serialized_start=77
  _DESCRIBEVODSPACETRANSCODEITEM._serialized_end=137
  _DESCRIBEVODSPACETRANSCODEDETAILTVUNIT._serialized_start=140
  _DESCRIBEVODSPACETRANSCODEDETAILTVUNIT._serialized_end=283
  _DESCRIBEVODSPACETRANSCODEDETAIL._serialized_start=286
  _DESCRIBEVODSPACETRANSCODEDETAIL._serialized_end=467
  _DESCRIBEVODSPACETRANSCODEDATARESULT._serialized_start=470
  _DESCRIBEVODSPACETRANSCODEDATARESULT._serialized_end=918
  _DESCRIBEVODSPACEAISTATISDATAITEM._serialized_start=920
  _DESCRIBEVODSPACEAISTATISDATAITEM._serialized_end=986
  _DESCRIBEVODSPACEAISTATISDATADETAIL._serialized_start=989
  _DESCRIBEVODSPACEAISTATISDATADETAIL._serialized_end=1150
  _DESCRIBEVODSPACEAISTATISDATARESULT._serialized_start=1153
  _DESCRIBEVODSPACEAISTATISDATARESULT._serialized_end=1570
  _DESCRIBEVODSPACESUBTITLESTATISDATAITEM._serialized_start=1572
  _DESCRIBEVODSPACESUBTITLESTATISDATAITEM._serialized_end=1641
  _DESCRIBEVODSPACESUBTITLESTATISDATADETAIL._serialized_start=1644
  _DESCRIBEVODSPACESUBTITLESTATISDATADETAIL._serialized_end=1823
  _DESCRIBEVODSPACESUBTITLESTATISDATARESULT._serialized_start=1826
  _DESCRIBEVODSPACESUBTITLESTATISDATARESULT._serialized_end=2280
  _DESCRIBEVODSPACEDETECTSTATISDATAITEM._serialized_start=2282
  _DESCRIBEVODSPACEDETECTSTATISDATAITEM._serialized_end=2349
  _DESCRIBEVODSPACEDETECTSTATISDATADETAIL._serialized_start=2352
  _DESCRIBEVODSPACEDETECTSTATISDATADETAIL._serialized_end=2525
  _DESCRIBEVODSPACEDETECTSTATISDATARESULT._serialized_start=2528
  _DESCRIBEVODSPACEDETECTSTATISDATARESULT._serialized_end=2968
  _DESCRIBEVODSNAPSHOTDATAITEM._serialized_start=2970
  _DESCRIBEVODSNAPSHOTDATAITEM._serialized_end=3028
  _DESCRIBEVODSNAPSHOTDATADETAIL._serialized_start=3031
  _DESCRIBEVODSNAPSHOTDATADETAIL._serialized_end=3198
  _DESCRIBEVODSNAPSHOTDATARESULT._serialized_start=3201
  _DESCRIBEVODSNAPSHOTDATARESULT._serialized_end=3607
  _DESCRIBEVODSPACEWORKFLOWTRANSCODEINFO._serialized_start=3610
  _DESCRIBEVODSPACEWORKFLOWTRANSCODEINFO._serialized_end=3826
  _DESCRIBEVODSPACEWORKFLOWSNAPSHOTINFO._serialized_start=3828
  _DESCRIBEVODSPACEWORKFLOWSNAPSHOTINFO._serialized_end=3927
  _DESCRIBEVODSPACEWORKFLOWENHANCEEXECINFO._serialized_start=3929
  _DESCRIBEVODSPACEWORKFLOWENHANCEEXECINFO._serialized_end=4033
  _DESCRIBEVODSPACEWORKFLOWVIDEOAIINFO._serialized_start=4035
  _DESCRIBEVODSPACEWORKFLOWVIDEOAIINFO._serialized_end=4151
  _DESCRIBEVODSPACEWORKFLOWDETAIL._serialized_start=4154
  _DESCRIBEVODSPACEWORKFLOWDETAIL._serialized_end=4679
  _DESCRIBEVODSPACEWORKFLOWDETAILDATARESULT._serialized_start=4682
  _DESCRIBEVODSPACEWORKFLOWDETAILDATARESULT._serialized_end=4933
  _DESCRIBEVODSPACEEDITDETAIL._serialized_start=4936
  _DESCRIBEVODSPACEEDITDETAIL._serialized_end=5065
  _DESCRIBEVODSPACEEDITDETAILDATARESULT._serialized_start=5068
  _DESCRIBEVODSPACEEDITDETAILDATARESULT._serialized_end=5307
  _DESCRIBEVODPLAYFILELOGBYDOMAINITEM._serialized_start=5309
  _DESCRIBEVODPLAYFILELOGBYDOMAINITEM._serialized_end=5396
  _DESCRIBEVODPLAYFILELOGBYDOMAINRESULT._serialized_start=5399
  _DESCRIBEVODPLAYFILELOGBYDOMAINRESULT._serialized_end=5579
# @@protoc_insertion_point(module_scope)
