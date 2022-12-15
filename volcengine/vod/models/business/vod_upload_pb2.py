# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vod/business/vod_upload.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from volcengine.vod.models.business import vod_common_pb2 as vod_dot_business_dot_vod__common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dvod/business/vod_upload.proto\x12\x1eVolcengine.Vod.Models.Business\x1a\x1dvod/business/vod_common.proto\"\xe4\x01\n\x12VodUrlUploadURLSet\x12\x11\n\tSourceUrl\x18\x01 \x01(\t\x12\x14\n\x0c\x43\x61llbackArgs\x18\x02 \x01(\t\x12\x0b\n\x03Md5\x18\x03 \x01(\t\x12\x12\n\nTemplateId\x18\x04 \x01(\t\x12\r\n\x05Title\x18\x05 \x01(\t\x12\x13\n\x0b\x44\x65scription\x18\x06 \x01(\t\x12\x0c\n\x04Tags\x18\x07 \x01(\t\x12\x10\n\x08\x43\x61tegory\x18\x08 \x01(\t\x12\x10\n\x08\x46ileName\x18\t \x01(\t\x12\x18\n\x10\x43lassificationId\x18\n \x01(\x03\x12\x14\n\x0cStorageClass\x18\x0b \x01(\x05\"M\n\x12VodUrlResponseData\x12\x37\n\x04\x44\x61ta\x18\x01 \x03(\x0b\x32).Volcengine.Vod.Models.Business.ValuePair\"-\n\tValuePair\x12\r\n\x05JobId\x18\x01 \x01(\t\x12\x11\n\tSourceUrl\x18\x02 \x01(\t\"R\n\x0cVodQueryData\x12\x42\n\x04\x44\x61ta\x18\x01 \x01(\x0b\x32\x34.Volcengine.Vod.Models.Business.VodQueryUploadResult\"p\n\x14VodQueryUploadResult\x12@\n\rMediaInfoList\x18\x01 \x03(\x0b\x32).Volcengine.Vod.Models.Business.VodURLSet\x12\x16\n\x0eNotExistJobIds\x18\x02 \x03(\t\"^\n\rVodCommitData\x12M\n\x04\x44\x61ta\x18\x01 \x01(\x0b\x32?.Volcengine.Vod.Models.Business.VodCommitUploadInfoResponseData\"\xa7\x01\n\x1fVodCommitUploadInfoResponseData\x12\x0b\n\x03Vid\x18\x01 \x01(\t\x12\x41\n\nSourceInfo\x18\x02 \x01(\x0b\x32-.Volcengine.Vod.Models.Business.VodSourceInfo\x12\x11\n\tPosterUri\x18\x03 \x01(\t\x12\x14\n\x0c\x43\x61llbackArgs\x18\x04 \x01(\t\x12\x0b\n\x03Mid\x18\x05 \x01(\t\"\xc5\x01\n\tVodURLSet\x12\x11\n\tRequestId\x18\x01 \x01(\t\x12\r\n\x05JobId\x18\x02 \x01(\t\x12\x11\n\tSourceUrl\x18\x03 \x01(\t\x12\r\n\x05State\x18\x04 \x01(\t\x12\x0b\n\x03Vid\x18\x05 \x01(\t\x12\x11\n\tSpaceName\x18\x06 \x01(\t\x12\x11\n\tAccountId\x18\x07 \x01(\t\x12\x41\n\nSourceInfo\x18\x08 \x01(\x0b\x32-.Volcengine.Vod.Models.Business.VodSourceInfo\"`\n\x18VodApplyUploadInfoResult\x12\x44\n\x04\x44\x61ta\x18\x01 \x01(\x0b\x32\x36.Volcengine.Vod.Models.Business.VodApplyUploadInfoData\"a\n\x16VodApplyUploadInfoData\x12G\n\rUploadAddress\x18\x01 \x01(\x0b\x32\x30.Volcengine.Vod.Models.Business.VodUploadAddress\"\xc2\x01\n\x10VodUploadAddress\x12@\n\nStoreInfos\x18\x01 \x03(\x0b\x32,.Volcengine.Vod.Models.Business.VodStoreInfo\x12\x13\n\x0bUploadHosts\x18\x02 \x03(\t\x12\x43\n\x0cUploadHeader\x18\x03 \x03(\x0b\x32-.Volcengine.Vod.Models.Business.VodHeaderPair\x12\x12\n\nSessionKey\x18\x04 \x01(\t\".\n\x0cVodStoreInfo\x12\x10\n\x08StoreUri\x18\x01 \x01(\t\x12\x0c\n\x04\x41uth\x18\x02 \x01(\t\"+\n\rVodHeaderPair\x12\x0b\n\x03Key\x18\x01 \x01(\t\x12\r\n\x05Value\x18\x02 \x01(\t\"b\n\x19VodCommitUploadInfoResult\x12\x45\n\x04\x44\x61ta\x18\x01 \x01(\x0b\x32\x37.Volcengine.Vod.Models.Business.VodCommitUploadInfoData\"\x89\x01\n\x17VodCommitUploadInfoData\x12\x0b\n\x03Vid\x18\x01 \x01(\t\x12\x11\n\tPosterUri\x18\x02 \x01(\t\x12\x41\n\nSourceInfo\x18\x03 \x01(\x0b\x32-.Volcengine.Vod.Models.Business.VodSourceInfo\x12\x0b\n\x03Mid\x18\x04 \x01(\t\"\xc8\x02\n\x16VodUploadFunctionInput\x12\x14\n\x0cSnapshotTime\x18\x01 \x01(\x01\x12\r\n\x05Title\x18\x02 \x01(\t\x12\x0c\n\x04Tags\x18\x03 \x01(\t\x12\x13\n\x0b\x44\x65scription\x18\x04 \x01(\t\x12\x10\n\x08\x43\x61tegory\x18\x05 \x01(\t\x12\x12\n\nRecordType\x18\x06 \x01(\x05\x12\x0e\n\x06\x46ormat\x18\x07 \x01(\t\x12\x18\n\x10\x43lassificationId\x18\x08 \x01(\x05\x12\x12\n\nTemplateId\x18\t \x01(\t\x12\x0b\n\x03Vid\x18\n \x01(\t\x12\x0b\n\x03\x46id\x18\x0b \x01(\t\x12\x10\n\x08Language\x18\x0c \x01(\t\x12\x10\n\x08StoreUri\x18\r \x01(\t\x12\x0e\n\x06Source\x18\x0e \x01(\t\x12\x0b\n\x03Tag\x18\x0f \x01(\t\x12\x13\n\x0b\x41utoPublish\x18\x10 \x01(\x08\x12\x12\n\nActionType\x18\x11 \x01(\t\"h\n\x11VodUploadFunction\x12\x0c\n\x04Name\x18\x01 \x01(\t\x12\x45\n\x05Input\x18\x02 \x01(\x0b\x32\x36.Volcengine.Vod.Models.Business.VodUploadFunctionInput\"\x9a\x01\n\x15\x43ommitUploadInfoParam\x12\x11\n\tSpaceName\x18\x01 \x01(\t\x12\x14\n\x0c\x43\x61llbackArgs\x18\x02 \x01(\t\x12\x12\n\nSessionKey\x18\x03 \x01(\t\x12\x44\n\tFunctions\x18\x04 \x03(\x0b\x32\x31.Volcengine.Vod.Models.Business.VodUploadFunction\"g\n\x15\x43ommitRequestBodyJson\x12\x11\n\tSpaceName\x18\x01 \x01(\t\x12\x12\n\nSessionKey\x18\x02 \x01(\t\x12\x14\n\x0c\x43\x61llbackArgs\x18\x03 \x01(\t\x12\x11\n\tFunctions\x18\x04 \x01(\t\"\xec\x01\n\x14\x41pplyUploadInfoParam\x12\x11\n\tSpaceName\x18\x01 \x01(\t\x12\x10\n\x08\x46ileType\x18\x02 \x01(\t\x12\x12\n\nSessionKey\x18\x03 \x01(\t\x12\x10\n\x08\x46ileSize\x18\x04 \x01(\x01\x12\x11\n\tMediaType\x18\x05 \x01(\t\x12\x0f\n\x07TosKeys\x18\x06 \x01(\t\x12\x15\n\rFileExtension\x18\x07 \x01(\t\x12\x12\n\nFilePrefix\x18\x08 \x01(\t\x12\x17\n\x0f\x46lushUploadMode\x18\t \x01(\x05\x12\x0b\n\x03Md5\x18\n \x01(\t\x12\x14\n\x0cStorageClass\x18\x0b \x01(\x05\"\x96\x01\n\x0e\x43ommitResponse\x12\x0b\n\x03Vid\x18\x01 \x01(\t\x12\x0b\n\x03Mid\x18\x02 \x01(\t\x12\x41\n\nSourceInfo\x18\x03 \x01(\x0b\x32-.Volcengine.Vod.Models.Business.VodSourceInfo\x12\x11\n\tPosterUri\x18\x04 \x01(\t\x12\x14\n\x0c\x43\x61llbackArgs\x18\x05 \x01(\t\")\n\x13VodUploadOptionInfo\x12\x12\n\nTemplateId\x18\x01 \x01(\t\"\x98\x02\n\x15VodUploadCallbackData\x12\x0c\n\x04\x43ode\x18\x01 \x01(\t\x12\x0f\n\x07Message\x18\x02 \x01(\t\x12\x14\n\x0c\x43\x61llbackArgs\x18\x03 \x01(\t\x12\x0b\n\x03Vid\x18\x04 \x01(\t\x12\x0b\n\x03Mid\x18\x05 \x01(\t\x12\x11\n\tSpaceName\x18\x06 \x01(\t\x12\x41\n\nSourceInfo\x18\x07 \x01(\x0b\x32-.Volcengine.Vod.Models.Business.VodSourceInfo\x12\x11\n\tPosterUri\x18\x08 \x01(\t\x12G\n\nOptionInfo\x18\t \x01(\x0b\x32\x33.Volcengine.Vod.Models.Business.VodUploadOptionInfo\"\xa1\x01\n\x10\x43\x61llbackResponse\x12\x11\n\tRequestId\x18\x01 \x01(\t\x12\x0f\n\x07Version\x18\x02 \x01(\t\x12\x11\n\tEventTime\x18\x03 \x01(\t\x12\x11\n\tEventType\x18\x04 \x01(\t\x12\x43\n\x04\x44\x61ta\x18\x05 \x01(\x0b\x32\x35.Volcengine.Vod.Models.Business.VodUploadCallbackData\"+\n\tStoreInfo\x12\x10\n\x08StoreUri\x18\x01 \x01(\t\x12\x0c\n\x04\x41uth\x18\x02 \x01(\t\"(\n\nHeaderPair\x12\x0b\n\x03Key\x18\x01 \x01(\t\x12\r\n\x05Value\x18\x02 \x01(\t\"\xb9\x01\n\rUploadAddress\x12=\n\nStoreInfos\x18\x01 \x03(\x0b\x32).Volcengine.Vod.Models.Business.StoreInfo\x12\x13\n\x0bUploadHosts\x18\x02 \x03(\t\x12@\n\x0cUploadHeader\x18\x03 \x03(\x0b\x32*.Volcengine.Vod.Models.Business.HeaderPair\x12\x12\n\nSessionKey\x18\x04 \x01(\t\"\xae\x01\n\x11\x46lushUploadResult\x12\x13\n\x0b\x46lushUpload\x18\x01 \x01(\x08\x12\x0b\n\x03Vid\x18\x02 \x01(\t\x12\x0b\n\x03Mid\x18\x03 \x01(\t\x12\x41\n\nSourceInfo\x18\x04 \x01(\x0b\x32-.Volcengine.Vod.Models.Business.VodSourceInfo\x12\x11\n\tPosterUri\x18\x05 \x01(\t\x12\x14\n\x0c\x43\x61llbackArgs\x18\x06 \x01(\t\"\xb5\x01\n\rApplyResponse\x12\x44\n\rUploadAddress\x18\x01 \x01(\x0b\x32-.Volcengine.Vod.Models.Business.UploadAddress\x12L\n\x11\x46lushUploadResult\x18\x02 \x01(\x0b\x32\x31.Volcengine.Vod.Models.Business.FlushUploadResult\x12\x10\n\x08SDKParam\x18\x03 \x01(\t*:\n\x10StorageClassType\x12\x0b\n\x07\x44\x65\x66\x61ult\x10\x00\x12\x0c\n\x08Standard\x10\x01\x12\x0b\n\x07\x41rchive\x10\x02\x42\xcd\x01\n)com.volcengine.service.vod.model.businessB\tVodUploadP\x01ZAgithub.com/volcengine/volc-sdk-golang/service/vod/models/business\xa0\x01\x01\xd8\x01\x01\xc2\x02\x00\xca\x02 Volc\\Service\\Vod\\Models\\Business\xe2\x02#Volc\\Service\\Vod\\Models\\GPBMetadatab\x06proto3')

_STORAGECLASSTYPE = DESCRIPTOR.enum_types_by_name['StorageClassType']
StorageClassType = enum_type_wrapper.EnumTypeWrapper(_STORAGECLASSTYPE)
Default = 0
Standard = 1
Archive = 2


_VODURLUPLOADURLSET = DESCRIPTOR.message_types_by_name['VodUrlUploadURLSet']
_VODURLRESPONSEDATA = DESCRIPTOR.message_types_by_name['VodUrlResponseData']
_VALUEPAIR = DESCRIPTOR.message_types_by_name['ValuePair']
_VODQUERYDATA = DESCRIPTOR.message_types_by_name['VodQueryData']
_VODQUERYUPLOADRESULT = DESCRIPTOR.message_types_by_name['VodQueryUploadResult']
_VODCOMMITDATA = DESCRIPTOR.message_types_by_name['VodCommitData']
_VODCOMMITUPLOADINFORESPONSEDATA = DESCRIPTOR.message_types_by_name['VodCommitUploadInfoResponseData']
_VODURLSET = DESCRIPTOR.message_types_by_name['VodURLSet']
_VODAPPLYUPLOADINFORESULT = DESCRIPTOR.message_types_by_name['VodApplyUploadInfoResult']
_VODAPPLYUPLOADINFODATA = DESCRIPTOR.message_types_by_name['VodApplyUploadInfoData']
_VODUPLOADADDRESS = DESCRIPTOR.message_types_by_name['VodUploadAddress']
_VODSTOREINFO = DESCRIPTOR.message_types_by_name['VodStoreInfo']
_VODHEADERPAIR = DESCRIPTOR.message_types_by_name['VodHeaderPair']
_VODCOMMITUPLOADINFORESULT = DESCRIPTOR.message_types_by_name['VodCommitUploadInfoResult']
_VODCOMMITUPLOADINFODATA = DESCRIPTOR.message_types_by_name['VodCommitUploadInfoData']
_VODUPLOADFUNCTIONINPUT = DESCRIPTOR.message_types_by_name['VodUploadFunctionInput']
_VODUPLOADFUNCTION = DESCRIPTOR.message_types_by_name['VodUploadFunction']
_COMMITUPLOADINFOPARAM = DESCRIPTOR.message_types_by_name['CommitUploadInfoParam']
_COMMITREQUESTBODYJSON = DESCRIPTOR.message_types_by_name['CommitRequestBodyJson']
_APPLYUPLOADINFOPARAM = DESCRIPTOR.message_types_by_name['ApplyUploadInfoParam']
_COMMITRESPONSE = DESCRIPTOR.message_types_by_name['CommitResponse']
_VODUPLOADOPTIONINFO = DESCRIPTOR.message_types_by_name['VodUploadOptionInfo']
_VODUPLOADCALLBACKDATA = DESCRIPTOR.message_types_by_name['VodUploadCallbackData']
_CALLBACKRESPONSE = DESCRIPTOR.message_types_by_name['CallbackResponse']
_STOREINFO = DESCRIPTOR.message_types_by_name['StoreInfo']
_HEADERPAIR = DESCRIPTOR.message_types_by_name['HeaderPair']
_UPLOADADDRESS = DESCRIPTOR.message_types_by_name['UploadAddress']
_FLUSHUPLOADRESULT = DESCRIPTOR.message_types_by_name['FlushUploadResult']
_APPLYRESPONSE = DESCRIPTOR.message_types_by_name['ApplyResponse']
VodUrlUploadURLSet = _reflection.GeneratedProtocolMessageType('VodUrlUploadURLSet', (_message.Message,), {
  'DESCRIPTOR' : _VODURLUPLOADURLSET,
  '__module__' : 'vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodUrlUploadURLSet)
  })
_sym_db.RegisterMessage(VodUrlUploadURLSet)

VodUrlResponseData = _reflection.GeneratedProtocolMessageType('VodUrlResponseData', (_message.Message,), {
  'DESCRIPTOR' : _VODURLRESPONSEDATA,
  '__module__' : 'vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodUrlResponseData)
  })
_sym_db.RegisterMessage(VodUrlResponseData)

ValuePair = _reflection.GeneratedProtocolMessageType('ValuePair', (_message.Message,), {
  'DESCRIPTOR' : _VALUEPAIR,
  '__module__' : 'vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.ValuePair)
  })
_sym_db.RegisterMessage(ValuePair)

VodQueryData = _reflection.GeneratedProtocolMessageType('VodQueryData', (_message.Message,), {
  'DESCRIPTOR' : _VODQUERYDATA,
  '__module__' : 'vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodQueryData)
  })
_sym_db.RegisterMessage(VodQueryData)

VodQueryUploadResult = _reflection.GeneratedProtocolMessageType('VodQueryUploadResult', (_message.Message,), {
  'DESCRIPTOR' : _VODQUERYUPLOADRESULT,
  '__module__' : 'vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodQueryUploadResult)
  })
_sym_db.RegisterMessage(VodQueryUploadResult)

VodCommitData = _reflection.GeneratedProtocolMessageType('VodCommitData', (_message.Message,), {
  'DESCRIPTOR' : _VODCOMMITDATA,
  '__module__' : 'vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodCommitData)
  })
_sym_db.RegisterMessage(VodCommitData)

VodCommitUploadInfoResponseData = _reflection.GeneratedProtocolMessageType('VodCommitUploadInfoResponseData', (_message.Message,), {
  'DESCRIPTOR' : _VODCOMMITUPLOADINFORESPONSEDATA,
  '__module__' : 'vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodCommitUploadInfoResponseData)
  })
_sym_db.RegisterMessage(VodCommitUploadInfoResponseData)

VodURLSet = _reflection.GeneratedProtocolMessageType('VodURLSet', (_message.Message,), {
  'DESCRIPTOR' : _VODURLSET,
  '__module__' : 'vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodURLSet)
  })
_sym_db.RegisterMessage(VodURLSet)

VodApplyUploadInfoResult = _reflection.GeneratedProtocolMessageType('VodApplyUploadInfoResult', (_message.Message,), {
  'DESCRIPTOR' : _VODAPPLYUPLOADINFORESULT,
  '__module__' : 'vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodApplyUploadInfoResult)
  })
_sym_db.RegisterMessage(VodApplyUploadInfoResult)

VodApplyUploadInfoData = _reflection.GeneratedProtocolMessageType('VodApplyUploadInfoData', (_message.Message,), {
  'DESCRIPTOR' : _VODAPPLYUPLOADINFODATA,
  '__module__' : 'vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodApplyUploadInfoData)
  })
_sym_db.RegisterMessage(VodApplyUploadInfoData)

VodUploadAddress = _reflection.GeneratedProtocolMessageType('VodUploadAddress', (_message.Message,), {
  'DESCRIPTOR' : _VODUPLOADADDRESS,
  '__module__' : 'vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodUploadAddress)
  })
_sym_db.RegisterMessage(VodUploadAddress)

VodStoreInfo = _reflection.GeneratedProtocolMessageType('VodStoreInfo', (_message.Message,), {
  'DESCRIPTOR' : _VODSTOREINFO,
  '__module__' : 'vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodStoreInfo)
  })
_sym_db.RegisterMessage(VodStoreInfo)

VodHeaderPair = _reflection.GeneratedProtocolMessageType('VodHeaderPair', (_message.Message,), {
  'DESCRIPTOR' : _VODHEADERPAIR,
  '__module__' : 'vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodHeaderPair)
  })
_sym_db.RegisterMessage(VodHeaderPair)

VodCommitUploadInfoResult = _reflection.GeneratedProtocolMessageType('VodCommitUploadInfoResult', (_message.Message,), {
  'DESCRIPTOR' : _VODCOMMITUPLOADINFORESULT,
  '__module__' : 'vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodCommitUploadInfoResult)
  })
_sym_db.RegisterMessage(VodCommitUploadInfoResult)

VodCommitUploadInfoData = _reflection.GeneratedProtocolMessageType('VodCommitUploadInfoData', (_message.Message,), {
  'DESCRIPTOR' : _VODCOMMITUPLOADINFODATA,
  '__module__' : 'vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodCommitUploadInfoData)
  })
_sym_db.RegisterMessage(VodCommitUploadInfoData)

VodUploadFunctionInput = _reflection.GeneratedProtocolMessageType('VodUploadFunctionInput', (_message.Message,), {
  'DESCRIPTOR' : _VODUPLOADFUNCTIONINPUT,
  '__module__' : 'vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodUploadFunctionInput)
  })
_sym_db.RegisterMessage(VodUploadFunctionInput)

VodUploadFunction = _reflection.GeneratedProtocolMessageType('VodUploadFunction', (_message.Message,), {
  'DESCRIPTOR' : _VODUPLOADFUNCTION,
  '__module__' : 'vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodUploadFunction)
  })
_sym_db.RegisterMessage(VodUploadFunction)

CommitUploadInfoParam = _reflection.GeneratedProtocolMessageType('CommitUploadInfoParam', (_message.Message,), {
  'DESCRIPTOR' : _COMMITUPLOADINFOPARAM,
  '__module__' : 'vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.CommitUploadInfoParam)
  })
_sym_db.RegisterMessage(CommitUploadInfoParam)

CommitRequestBodyJson = _reflection.GeneratedProtocolMessageType('CommitRequestBodyJson', (_message.Message,), {
  'DESCRIPTOR' : _COMMITREQUESTBODYJSON,
  '__module__' : 'vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.CommitRequestBodyJson)
  })
_sym_db.RegisterMessage(CommitRequestBodyJson)

ApplyUploadInfoParam = _reflection.GeneratedProtocolMessageType('ApplyUploadInfoParam', (_message.Message,), {
  'DESCRIPTOR' : _APPLYUPLOADINFOPARAM,
  '__module__' : 'vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.ApplyUploadInfoParam)
  })
_sym_db.RegisterMessage(ApplyUploadInfoParam)

CommitResponse = _reflection.GeneratedProtocolMessageType('CommitResponse', (_message.Message,), {
  'DESCRIPTOR' : _COMMITRESPONSE,
  '__module__' : 'vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.CommitResponse)
  })
_sym_db.RegisterMessage(CommitResponse)

VodUploadOptionInfo = _reflection.GeneratedProtocolMessageType('VodUploadOptionInfo', (_message.Message,), {
  'DESCRIPTOR' : _VODUPLOADOPTIONINFO,
  '__module__' : 'vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodUploadOptionInfo)
  })
_sym_db.RegisterMessage(VodUploadOptionInfo)

VodUploadCallbackData = _reflection.GeneratedProtocolMessageType('VodUploadCallbackData', (_message.Message,), {
  'DESCRIPTOR' : _VODUPLOADCALLBACKDATA,
  '__module__' : 'vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodUploadCallbackData)
  })
_sym_db.RegisterMessage(VodUploadCallbackData)

CallbackResponse = _reflection.GeneratedProtocolMessageType('CallbackResponse', (_message.Message,), {
  'DESCRIPTOR' : _CALLBACKRESPONSE,
  '__module__' : 'vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.CallbackResponse)
  })
_sym_db.RegisterMessage(CallbackResponse)

StoreInfo = _reflection.GeneratedProtocolMessageType('StoreInfo', (_message.Message,), {
  'DESCRIPTOR' : _STOREINFO,
  '__module__' : 'vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.StoreInfo)
  })
_sym_db.RegisterMessage(StoreInfo)

HeaderPair = _reflection.GeneratedProtocolMessageType('HeaderPair', (_message.Message,), {
  'DESCRIPTOR' : _HEADERPAIR,
  '__module__' : 'vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.HeaderPair)
  })
_sym_db.RegisterMessage(HeaderPair)

UploadAddress = _reflection.GeneratedProtocolMessageType('UploadAddress', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADADDRESS,
  '__module__' : 'vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.UploadAddress)
  })
_sym_db.RegisterMessage(UploadAddress)

FlushUploadResult = _reflection.GeneratedProtocolMessageType('FlushUploadResult', (_message.Message,), {
  'DESCRIPTOR' : _FLUSHUPLOADRESULT,
  '__module__' : 'vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.FlushUploadResult)
  })
_sym_db.RegisterMessage(FlushUploadResult)

ApplyResponse = _reflection.GeneratedProtocolMessageType('ApplyResponse', (_message.Message,), {
  'DESCRIPTOR' : _APPLYRESPONSE,
  '__module__' : 'vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.ApplyResponse)
  })
_sym_db.RegisterMessage(ApplyResponse)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n)com.volcengine.service.vod.model.businessB\tVodUploadP\001ZAgithub.com/volcengine/volc-sdk-golang/service/vod/models/business\240\001\001\330\001\001\302\002\000\312\002 Volc\\Service\\Vod\\Models\\Business\342\002#Volc\\Service\\Vod\\Models\\GPBMetadata'
  _STORAGECLASSTYPE._serialized_start=4061
  _STORAGECLASSTYPE._serialized_end=4119
  _VODURLUPLOADURLSET._serialized_start=97
  _VODURLUPLOADURLSET._serialized_end=325
  _VODURLRESPONSEDATA._serialized_start=327
  _VODURLRESPONSEDATA._serialized_end=404
  _VALUEPAIR._serialized_start=406
  _VALUEPAIR._serialized_end=451
  _VODQUERYDATA._serialized_start=453
  _VODQUERYDATA._serialized_end=535
  _VODQUERYUPLOADRESULT._serialized_start=537
  _VODQUERYUPLOADRESULT._serialized_end=649
  _VODCOMMITDATA._serialized_start=651
  _VODCOMMITDATA._serialized_end=745
  _VODCOMMITUPLOADINFORESPONSEDATA._serialized_start=748
  _VODCOMMITUPLOADINFORESPONSEDATA._serialized_end=915
  _VODURLSET._serialized_start=918
  _VODURLSET._serialized_end=1115
  _VODAPPLYUPLOADINFORESULT._serialized_start=1117
  _VODAPPLYUPLOADINFORESULT._serialized_end=1213
  _VODAPPLYUPLOADINFODATA._serialized_start=1215
  _VODAPPLYUPLOADINFODATA._serialized_end=1312
  _VODUPLOADADDRESS._serialized_start=1315
  _VODUPLOADADDRESS._serialized_end=1509
  _VODSTOREINFO._serialized_start=1511
  _VODSTOREINFO._serialized_end=1557
  _VODHEADERPAIR._serialized_start=1559
  _VODHEADERPAIR._serialized_end=1602
  _VODCOMMITUPLOADINFORESULT._serialized_start=1604
  _VODCOMMITUPLOADINFORESULT._serialized_end=1702
  _VODCOMMITUPLOADINFODATA._serialized_start=1705
  _VODCOMMITUPLOADINFODATA._serialized_end=1842
  _VODUPLOADFUNCTIONINPUT._serialized_start=1845
  _VODUPLOADFUNCTIONINPUT._serialized_end=2173
  _VODUPLOADFUNCTION._serialized_start=2175
  _VODUPLOADFUNCTION._serialized_end=2279
  _COMMITUPLOADINFOPARAM._serialized_start=2282
  _COMMITUPLOADINFOPARAM._serialized_end=2436
  _COMMITREQUESTBODYJSON._serialized_start=2438
  _COMMITREQUESTBODYJSON._serialized_end=2541
  _APPLYUPLOADINFOPARAM._serialized_start=2544
  _APPLYUPLOADINFOPARAM._serialized_end=2780
  _COMMITRESPONSE._serialized_start=2783
  _COMMITRESPONSE._serialized_end=2933
  _VODUPLOADOPTIONINFO._serialized_start=2935
  _VODUPLOADOPTIONINFO._serialized_end=2976
  _VODUPLOADCALLBACKDATA._serialized_start=2979
  _VODUPLOADCALLBACKDATA._serialized_end=3259
  _CALLBACKRESPONSE._serialized_start=3262
  _CALLBACKRESPONSE._serialized_end=3423
  _STOREINFO._serialized_start=3425
  _STOREINFO._serialized_end=3468
  _HEADERPAIR._serialized_start=3470
  _HEADERPAIR._serialized_end=3510
  _UPLOADADDRESS._serialized_start=3513
  _UPLOADADDRESS._serialized_end=3698
  _FLUSHUPLOADRESULT._serialized_start=3701
  _FLUSHUPLOADRESULT._serialized_end=3875
  _APPLYRESPONSE._serialized_start=3878
  _APPLYRESPONSE._serialized_end=4059
# @@protoc_insertion_point(module_scope)
