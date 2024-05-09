# coding:utf-8
from .common import Field
import json
from .Doc import Doc
from .Point import Point

class Collection(object):
    def __init__(self, viking_kb_service, collection_name, kwargs=None):
        self.viking_kb_service      = viking_kb_service
        self.collection_name        = collection_name
        if kwargs is not None:
            self.description            = kwargs.get("description")
            self.doc_num                = kwargs.get("doc_num")
            self.create_time            = kwargs.get("create_time")
            self.update_time            = kwargs.get("update_time")
            self.creator                = kwargs.get("creator")
            self.pipeline_list          = kwargs.get("pipeline_list")
            self.preprocessing          = kwargs.get("preprocessing")
            self.fields                 = [Field(field) for field in kwargs.get("fields", [])]

    def add_doc(self, add_type, doc_id=None, doc_name=None, doc_type=None, tos_path=None, url=None, meta=None):
        params = {"collection_name": self.collection_name, "add_type": add_type}
        if add_type == "tos" :
            params["tos_path"]  = tos_path

        elif add_type == "url" :
            params["doc_id"]    = doc_id
            params["doc_name"]  = doc_name
            params["doc_type"]  = doc_type
            params["url"]       = url
            if meta is not None: 
                params["meta"]  = meta
        self.viking_kb_service.json_exception("AddDoc", {}, json.dumps(params))

    async def async_add_doc(self, add_type, doc_id=None, doc_name=None, doc_type=None, tos_path=None, url=None, meta=None):
        params = {"collection_name": self.collection_name, "add_type": add_type}
        if add_type == "tos" :
            params["tos_path"]  = tos_path

        elif add_type == "url" :
            params["doc_id"]    = doc_id
            params["doc_name"]  = doc_name
            params["doc_type"]  = doc_type
            params["url"]       = url
            if meta != None: 
                params["meta"]  = meta
        await self.viking_kb_service.async_json_exception("AddDoc", {}, json.dumps(params))

    def delete_doc(self, doc_id):
        params = {"collection_name": self.collection_name, "doc_id": doc_id}
        self.viking_kb_service.json_exception("DeleteDoc", {}, json.dumps(params))
    
    async def async_delete_doc(self, doc_id):
        params = {"collection_name": self.collection_name, "doc_id": doc_id}
        await self.viking_kb_service.async_json_exception("DeleteDoc", {}, json.dumps(params))

    def get_doc(self, doc_id):
        params = {"collection_name": self.collection_name, "doc_id": doc_id}
        res = self.viking_kb_service.json_exception("GetDocInfo", {}, json.dumps(params))
        data = json.loads(res)["data"]
        return Doc(data)

    async def async_get_doc(self, doc_id):
        params = {"collection_name": self.collection_name, "doc_id": doc_id}
        res = await self.viking_kb_service.async_json_exception("GetDocInfo", {}, json.dumps(params))
        data = json.loads(res)["data"]
        return Doc(data)

    def list_docs(self, offset=0, limit=-1, doc_type=None):
        params = {"collection_name": self.collection_name, "offset": offset, "limit": limit, "doc_type": doc_type}
        res = self.viking_kb_service.json_exception("ListDocs", {}, json.dumps(params))
        data = json.loads(res)["data"]
        docs = []
        for item in data["doc_list"]:
            docs.append(Doc(item))
        return docs

    async def async_list_docs(self, offset=0, limit=-1, doc_type=None):
        params = {"collection_name": self.collection_name, "offset": offset, "limit": limit, "doc_type": doc_type}
        res = await self.viking_kb_service.async_json_exception("ListDocs", {}, json.dumps(params))
        data = json.loads(res)["data"]
        docs = []
        for item in data["doc_list"]:
            docs.append(Doc(item))
        return docs

    def update_meta(self, doc_id, meta):
        params = {"collection_name": self.collection_name, "doc_id": doc_id, "meta": meta}
        self.viking_kb_service.json_exception("UpdateDocMeta", {}, json.dumps(params))
    
    async def async_update_meta(self, doc_id, meta):
        params = {"collection_name": self.collection_name, "doc_id": doc_id, "meta": meta}
        await self.viking_kb_service.async_json_exception("UpdateDocMeta", {}, json.dumps(params))

    def get_point(self, point_id):
        params = {"collection_name": self.collection_name, "point_id": point_id}
        res = self.viking_kb_service.json_exception("GetPointInfo", {}, json.dumps(params))
        res = json.loads(res)
        return Point(res["data"])
    
    async def async_get_point(self, point_id):
        params = {"collection_name": self.collection_name, "point_id": point_id}
        res = await self.viking_kb_service.async_json_exception("GetPointInfo", {}, json.dumps(params))
        res = json.loads(res)
        return Point(res["data"])

    def list_points(self, offset=0, limit=-1, doc_ids=None):
        params = {"collection_name": self.collection_name, "offset": offset, "limit": limit, "doc_ids": doc_ids}
        res = self.viking_kb_service.json_exception("ListPoints", {}, json.dumps(params))
        point_list = json.loads(res)["data"]["point_list"]
        points = []
        for item in point_list:
            points.append(Point(item))
        return points 
    
    async def async_list_points(self, offset=0, limit=-1, doc_ids=None):
        params = {"collection_name": self.collection_name, "offset": offset, "limit": limit, "doc_ids": doc_ids}
        res = await self.viking_kb_service.async_json_exception("ListPoints", {}, json.dumps(params))
        point_list = json.loads(res)["data"]["point_list"]
        points = []
        for item in point_list:
            points.append(Point(item))
        return points 