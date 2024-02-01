# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: volcengine/vod/business/vod_play.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&volcengine/vod/business/vod_play.proto\x12\x1eVolcengine.Vod.Models.Business\"\xd8\x01\n\x1cVodGetOriginalPlayInfoResult\x12\x10\n\x08\x46ileType\x18\x01 \x01(\t\x12\x10\n\x08\x44uration\x18\x02 \x01(\x02\x12\x0c\n\x04Size\x18\x03 \x01(\x01\x12\x0e\n\x06Height\x18\x04 \x01(\x05\x12\r\n\x05Width\x18\x05 \x01(\x05\x12\x0e\n\x06\x46ormat\x18\x06 \x01(\t\x12\r\n\x05\x43odec\x18\x07 \x01(\t\x12\x0f\n\x07\x42itrate\x18\x08 \x01(\x05\x12\x0b\n\x03Md5\x18\t \x01(\t\x12\x13\n\x0bMainPlayUrl\x18\n \x01(\t\x12\x15\n\rBackupPlayUrl\x18\x0b \x01(\t\"H\n\x19VodPrivateDrmPlayAuthInfo\x12\x12\n\nPlayAuthId\x18\x01 \x01(\t\x12\x17\n\x0fPlayAuthContent\x18\x02 \x01(\t\"u\n\x1eVodGetPrivateDrmPlayAuthResult\x12S\n\x10PlayAuthInfoList\x18\x01 \x03(\x0b\x32\x39.Volcengine.Vod.Models.Business.VodPrivateDrmPlayAuthInfo\"V\n\x1cVodGetHlsDecryptionKeyResult\x12\x11\n\tSecretKey\x18\x01 \x01(\t\x12\x10\n\x08IsBase64\x18\x02 \x01(\x08\x12\x11\n\tKeyFormat\x18\x03 \x01(\t\"t\n!VodPlayInfoWithLiveTimeShiftScene\x12\x10\n\x08StoreUri\x18\x01 \x01(\t\x12\x13\n\x0bMainPlayUrl\x18\x02 \x01(\t\x12\x15\n\rBackupPlayUrl\x18\x03 \x01(\t\x12\x11\n\tUrlExpire\x18\x04 \x01(\x01\"\x85\x01\n*VodGetPlayInfoWithLiveTimeShiftSceneResult\x12W\n\x0cPlayInfoList\x18\x01 \x03(\x0b\x32\x41.Volcengine.Vod.Models.Business.VodPlayInfoWithLiveTimeShiftScene\"a\n\x1bVodDescribeDrmDataKeyResult\x12\x11\n\tSecretKey\x18\x01 \x01(\t\x12\n\n\x02\x41k\x18\x02 \x01(\t\x12\x10\n\x08IsBase64\x18\x03 \x01(\x08\x12\x11\n\tKeyFormat\x18\x04 \x01(\tB\xcb\x01\n)com.volcengine.service.vod.model.businessB\x07VodPlayP\x01ZAgithub.com/volcengine/volc-sdk-golang/service/vod/models/business\xa0\x01\x01\xd8\x01\x01\xc2\x02\x00\xca\x02 Volc\\Service\\Vod\\Models\\Business\xe2\x02#Volc\\Service\\Vod\\Models\\GPBMetadatab\x06proto3')



_VODGETORIGINALPLAYINFORESULT = DESCRIPTOR.message_types_by_name['VodGetOriginalPlayInfoResult']
_VODPRIVATEDRMPLAYAUTHINFO = DESCRIPTOR.message_types_by_name['VodPrivateDrmPlayAuthInfo']
_VODGETPRIVATEDRMPLAYAUTHRESULT = DESCRIPTOR.message_types_by_name['VodGetPrivateDrmPlayAuthResult']
_VODGETHLSDECRYPTIONKEYRESULT = DESCRIPTOR.message_types_by_name['VodGetHlsDecryptionKeyResult']
_VODPLAYINFOWITHLIVETIMESHIFTSCENE = DESCRIPTOR.message_types_by_name['VodPlayInfoWithLiveTimeShiftScene']
_VODGETPLAYINFOWITHLIVETIMESHIFTSCENERESULT = DESCRIPTOR.message_types_by_name['VodGetPlayInfoWithLiveTimeShiftSceneResult']
_VODDESCRIBEDRMDATAKEYRESULT = DESCRIPTOR.message_types_by_name['VodDescribeDrmDataKeyResult']
VodGetOriginalPlayInfoResult = _reflection.GeneratedProtocolMessageType('VodGetOriginalPlayInfoResult', (_message.Message,), {
  'DESCRIPTOR' : _VODGETORIGINALPLAYINFORESULT,
  '__module__' : 'volcengine.vod.business.vod_play_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodGetOriginalPlayInfoResult)
  })
_sym_db.RegisterMessage(VodGetOriginalPlayInfoResult)

VodPrivateDrmPlayAuthInfo = _reflection.GeneratedProtocolMessageType('VodPrivateDrmPlayAuthInfo', (_message.Message,), {
  'DESCRIPTOR' : _VODPRIVATEDRMPLAYAUTHINFO,
  '__module__' : 'volcengine.vod.business.vod_play_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodPrivateDrmPlayAuthInfo)
  })
_sym_db.RegisterMessage(VodPrivateDrmPlayAuthInfo)

VodGetPrivateDrmPlayAuthResult = _reflection.GeneratedProtocolMessageType('VodGetPrivateDrmPlayAuthResult', (_message.Message,), {
  'DESCRIPTOR' : _VODGETPRIVATEDRMPLAYAUTHRESULT,
  '__module__' : 'volcengine.vod.business.vod_play_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodGetPrivateDrmPlayAuthResult)
  })
_sym_db.RegisterMessage(VodGetPrivateDrmPlayAuthResult)

VodGetHlsDecryptionKeyResult = _reflection.GeneratedProtocolMessageType('VodGetHlsDecryptionKeyResult', (_message.Message,), {
  'DESCRIPTOR' : _VODGETHLSDECRYPTIONKEYRESULT,
  '__module__' : 'volcengine.vod.business.vod_play_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodGetHlsDecryptionKeyResult)
  })
_sym_db.RegisterMessage(VodGetHlsDecryptionKeyResult)

VodPlayInfoWithLiveTimeShiftScene = _reflection.GeneratedProtocolMessageType('VodPlayInfoWithLiveTimeShiftScene', (_message.Message,), {
  'DESCRIPTOR' : _VODPLAYINFOWITHLIVETIMESHIFTSCENE,
  '__module__' : 'volcengine.vod.business.vod_play_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodPlayInfoWithLiveTimeShiftScene)
  })
_sym_db.RegisterMessage(VodPlayInfoWithLiveTimeShiftScene)

VodGetPlayInfoWithLiveTimeShiftSceneResult = _reflection.GeneratedProtocolMessageType('VodGetPlayInfoWithLiveTimeShiftSceneResult', (_message.Message,), {
  'DESCRIPTOR' : _VODGETPLAYINFOWITHLIVETIMESHIFTSCENERESULT,
  '__module__' : 'volcengine.vod.business.vod_play_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodGetPlayInfoWithLiveTimeShiftSceneResult)
  })
_sym_db.RegisterMessage(VodGetPlayInfoWithLiveTimeShiftSceneResult)

VodDescribeDrmDataKeyResult = _reflection.GeneratedProtocolMessageType('VodDescribeDrmDataKeyResult', (_message.Message,), {
  'DESCRIPTOR' : _VODDESCRIBEDRMDATAKEYRESULT,
  '__module__' : 'volcengine.vod.business.vod_play_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodDescribeDrmDataKeyResult)
  })
_sym_db.RegisterMessage(VodDescribeDrmDataKeyResult)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n)com.volcengine.service.vod.model.businessB\007VodPlayP\001ZAgithub.com/volcengine/volc-sdk-golang/service/vod/models/business\240\001\001\330\001\001\302\002\000\312\002 Volc\\Service\\Vod\\Models\\Business\342\002#Volc\\Service\\Vod\\Models\\GPBMetadata'
  _VODGETORIGINALPLAYINFORESULT._serialized_start=75
  _VODGETORIGINALPLAYINFORESULT._serialized_end=291
  _VODPRIVATEDRMPLAYAUTHINFO._serialized_start=293
  _VODPRIVATEDRMPLAYAUTHINFO._serialized_end=365
  _VODGETPRIVATEDRMPLAYAUTHRESULT._serialized_start=367
  _VODGETPRIVATEDRMPLAYAUTHRESULT._serialized_end=484
  _VODGETHLSDECRYPTIONKEYRESULT._serialized_start=486
  _VODGETHLSDECRYPTIONKEYRESULT._serialized_end=572
  _VODPLAYINFOWITHLIVETIMESHIFTSCENE._serialized_start=574
  _VODPLAYINFOWITHLIVETIMESHIFTSCENE._serialized_end=690
  _VODGETPLAYINFOWITHLIVETIMESHIFTSCENERESULT._serialized_start=693
  _VODGETPLAYINFOWITHLIVETIMESHIFTSCENERESULT._serialized_end=826
  _VODDESCRIBEDRMDATAKEYRESULT._serialized_start=828
  _VODDESCRIBEDRMDATAKEYRESULT._serialized_end=925
# @@protoc_insertion_point(module_scope)
