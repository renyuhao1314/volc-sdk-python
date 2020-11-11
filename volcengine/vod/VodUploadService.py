# Code generated by protoc-gen-volcengine-sdk
# source: VodUploadService
# DO NOT EDIT!
# coding:utf-8

from __future__ import print_function
import os
import threading
import time
from zlib import crc32
from volcengine.ApiInfo import ApiInfo
from volcengine.Credentials import Credentials
from volcengine.ServiceInfo import ServiceInfo
from volcengine.base.Service import Service
from volcengine.const.Const import *
from volcengine.Policy import *
from volcengine.util.Util import *
from google.protobuf.json_format import *
from volcengine.vod.VodService import VodService
from volcengine.models.vod.request.request_vod_pb2 import *
from volcengine.models.vod.response.response_vod_pb2 import *


#
# Generated from protobuf service <code>VodUploadService</code>
#
class VodUploadService(VodService):

    #
    # UploadMediaByUrl.
    #
    # @param request VodUrlUploadRequest
    # @return VodUrlUploadResponse
    # @raise Exception
    def upload_media_by_url(self, request: VodUrlUploadRequest) -> VodUrlUploadResponse:
        try:
            jsonData = MessageToJson(request, False, True)
            params = json.loads(jsonData)
            for k, v in params.items():
                if isinstance(v, (int, float, bool, str)) is True:
                    continue
                else:
                    params[k] = json.dumps(v)
            res = self.get("UploadMediaByUrl", params)
        except Exception as Argument:
            try:
                resp = Parse(Argument.__str__(), VodUrlUploadResponse(), True)
            except Exception:
                raise Argument
            else:
                raise Exception(resp.ResponseMetadata.Error.Code)
        else:
            return Parse(res, VodUrlUploadResponse(), True)

    #
    # QueryUploadTaskInfo.
    #
    # @param request VodQueryUploadTaskInfoRequest
    # @return VodQueryUploadTaskInfoResponse
    # @raise Exception
    def query_upload_task_info(self, request: VodQueryUploadTaskInfoRequest) -> VodQueryUploadTaskInfoResponse:
        try:
            jsonData = MessageToJson(request, False, True)
            params = json.loads(jsonData)
            for k, v in params.items():
                if isinstance(v, (int, float, bool, str)) is True:
                    continue
                else:
                    params[k] = json.dumps(v)
            res = self.get("QueryUploadTaskInfo", params)
        except Exception as Argument:
            try:
                resp = Parse(Argument.__str__(), VodQueryUploadTaskInfoResponse(), True)
            except Exception:
                raise Argument
            else:
                raise Exception(resp.ResponseMetadata.Error.Code)
        else:
            return Parse(res, VodQueryUploadTaskInfoResponse(), True)

    #
    # ApplyUploadInfo.
    #
    # @param request VodApplyUploadInfoRequest
    # @return VodApplyUploadInfoResponse
    # @raise Exception
    def apply_upload_info(self, request: VodApplyUploadInfoRequest) -> VodApplyUploadInfoResponse:
        try:
            jsonData = MessageToJson(request, False, True)
            params = json.loads(jsonData)
            for k, v in params.items():
                if isinstance(v, (int, float, bool, str)) is True:
                    continue
                else:
                    params[k] = json.dumps(v)
            res = self.get("ApplyUploadInfo", params)
        except Exception as Argument:
            try:
                resp = Parse(Argument.__str__(), VodApplyUploadInfoResponse(), True)
            except Exception:
                raise Argument
            else:
                raise Exception(resp.ResponseMetadata.Error.Code)
        else:
            return Parse(res, VodApplyUploadInfoResponse(), True)

    #
    # CommitUploadInfo.
    #
    # @param request VodCommitUploadInfoRequest
    # @return VodCommitUploadInfoResponse
    # @raise Exception
    def commit_upload_info(self, request: VodCommitUploadInfoRequest) -> VodCommitUploadInfoResponse:
        try:
            jsonData = MessageToJson(request, False, True)
            params = json.loads(jsonData)
            for k, v in params.items():
                if isinstance(v, (int, float, bool, str)) is True:
                    continue
                else:
                    params[k] = json.dumps(v)
            res = self.get("CommitUploadInfo", params)
        except Exception as Argument:
            try:
                resp = Parse(Argument.__str__(), VodCommitUploadInfoResponse(), True)
                print(resp)
            except Exception:
                raise Argument
            else:
                raise Exception(resp.ResponseMetadata.Error.Code)
        else:
            return Parse(res, VodCommitUploadInfoResponse(), True)

    # end of service interface