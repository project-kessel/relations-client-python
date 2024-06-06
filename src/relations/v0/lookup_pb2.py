# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: relations/v0/lookup.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19relations/v0/lookup.proto\x12\x13kessel.relations.v0\x1a\x1cgoogle/api/annotations.proto\x1a\x19relations/v0/common.proto\"\x9c\x02\n\x15LookupSubjectsRequest\x12\x36\n\x08resource\x18\x01 \x01(\x0b\x32$.kessel.relations.v0.ObjectReference\x12\x10\n\x08relation\x18\x02 \x01(\t\x12\x35\n\x0csubject_type\x18\x03 \x01(\x0b\x32\x1f.kessel.relations.v0.ObjectType\x12\x1d\n\x10subject_relation\x18\x04 \x01(\tH\x00\x88\x01\x01\x12?\n\npagination\x18\x05 \x01(\x0b\x32&.kessel.relations.v0.RequestPaginationH\x01\x88\x01\x01\x42\x13\n\x11_subject_relationB\r\n\x0b_pagination\"\x8d\x01\n\x16LookupSubjectsResponse\x12\x36\n\x07subject\x18\x01 \x01(\x0b\x32%.kessel.relations.v0.SubjectReference\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.kessel.relations.v0.ResponsePagination2\x99\x01\n\x13KesselLookupService\x12\x81\x01\n\x0eLookupSubjects\x12*.kessel.relations.v0.LookupSubjectsRequest\x1a+.kessel.relations.v0.LookupSubjectsResponse\"\x14\x82\xd3\xe4\x93\x02\x0e\x12\x0c/v0/subjects0\x01\x42G\n#org.project_kessel.api.relations.v0P\x01Z\x1e\x63iam-rebac/api/relations/v0;v0b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'relations.v0.lookup_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n#org.project_kessel.api.relations.v0P\001Z\036ciam-rebac/api/relations/v0;v0'
  _globals['_KESSELLOOKUPSERVICE'].methods_by_name['LookupSubjects']._options = None
  _globals['_KESSELLOOKUPSERVICE'].methods_by_name['LookupSubjects']._serialized_options = b'\202\323\344\223\002\016\022\014/v0/subjects'
  _globals['_LOOKUPSUBJECTSREQUEST']._serialized_start=108
  _globals['_LOOKUPSUBJECTSREQUEST']._serialized_end=392
  _globals['_LOOKUPSUBJECTSRESPONSE']._serialized_start=395
  _globals['_LOOKUPSUBJECTSRESPONSE']._serialized_end=536
  _globals['_KESSELLOOKUPSERVICE']._serialized_start=539
  _globals['_KESSELLOOKUPSERVICE']._serialized_end=692
# @@protoc_insertion_point(module_scope)
