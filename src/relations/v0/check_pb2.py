# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: relations/v0/check.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from relations.v0 import common_pb2 as relations_dot_v0_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18relations/v0/check.proto\x12\x13kessel.relations.v0\x1a\x1cgoogle/api/annotations.proto\x1a\x19relations/v0/common.proto\"\x90\x01\n\x0c\x43heckRequest\x12\x36\n\x08resource\x18\x01 \x01(\x0b\x32$.kessel.relations.v0.ObjectReference\x12\x10\n\x08relation\x18\x02 \x01(\t\x12\x36\n\x07subject\x18\x03 \x01(\x0b\x32%.kessel.relations.v0.SubjectReference\"\x95\x01\n\rCheckResponse\x12;\n\x07\x61llowed\x18\x01 \x01(\x0e\x32*.kessel.relations.v0.CheckResponse.Allowed\"G\n\x07\x41llowed\x12\x17\n\x13\x41LLOWED_UNSPECIFIED\x10\x00\x12\x10\n\x0c\x41LLOWED_TRUE\x10\x01\x12\x11\n\rALLOWED_FALSE\x10\x02\x32z\n\x12KesselCheckService\x12\x64\n\x05\x43heck\x12!.kessel.relations.v0.CheckRequest\x1a\".kessel.relations.v0.CheckResponse\"\x14\x82\xd3\xe4\x93\x02\x0e\"\t/v0/check:\x01*BG\n#org.project_kessel.api.relations.v0P\x01Z\x1e\x63iam-rebac/api/relations/v0;v0b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'relations.v0.check_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n#org.project_kessel.api.relations.v0P\001Z\036ciam-rebac/api/relations/v0;v0'
  _globals['_KESSELCHECKSERVICE'].methods_by_name['Check']._options = None
  _globals['_KESSELCHECKSERVICE'].methods_by_name['Check']._serialized_options = b'\202\323\344\223\002\016\"\t/v0/check:\001*'
  _globals['_CHECKREQUEST']._serialized_start=107
  _globals['_CHECKREQUEST']._serialized_end=251
  _globals['_CHECKRESPONSE']._serialized_start=254
  _globals['_CHECKRESPONSE']._serialized_end=403
  _globals['_CHECKRESPONSE_ALLOWED']._serialized_start=332
  _globals['_CHECKRESPONSE_ALLOWED']._serialized_end=403
  _globals['_KESSELCHECKSERVICE']._serialized_start=405
  _globals['_KESSELCHECKSERVICE']._serialized_end=527
# @@protoc_insertion_point(module_scope)