# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kessel/relations/v1beta1/relation_tuples.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from kessel.relations.v1beta1 import common_pb2 as kessel_dot_relations_dot_v1beta1_dot_common__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.kessel/relations/v1beta1/relation_tuples.proto\x12\x18kessel.relations.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a%kessel/relations/v1beta1/common.proto\x1a\x17validate/validate.proto\"]\n\x13\x43reateTuplesRequest\x12\x0e\n\x06upsert\x18\x01 \x01(\x08\x12\x36\n\x06tuples\x18\x02 \x03(\x0b\x32&.kessel.relations.v1beta1.Relationship\"\x16\n\x14\x43reateTuplesResponse\"\xb1\x01\n\x11ReadTuplesRequest\x12G\n\x06\x66ilter\x18\x01 \x01(\x0b\x32-.kessel.relations.v1beta1.RelationTupleFilterB\x08\xfa\x42\x05\xa2\x01\x02\x08\x01\x12\x44\n\npagination\x18\x02 \x01(\x0b\x32+.kessel.relations.v1beta1.RequestPaginationH\x00\x88\x01\x01\x42\r\n\x0b_pagination\"\x8d\x01\n\x12ReadTuplesResponse\x12\x35\n\x05tuple\x18\x01 \x01(\x0b\x32&.kessel.relations.v1beta1.Relationship\x12@\n\npagination\x18\x02 \x01(\x0b\x32,.kessel.relations.v1beta1.ResponsePagination\"^\n\x13\x44\x65leteTuplesRequest\x12G\n\x06\x66ilter\x18\x01 \x01(\x0b\x32-.kessel.relations.v1beta1.RelationTupleFilterB\x08\xfa\x42\x05\xa2\x01\x02\x08\x01\"\x16\n\x14\x44\x65leteTuplesResponse\"\xa2\x02\n\x13RelationTupleFilter\x12\x1f\n\x12resource_namespace\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x1a\n\rresource_type\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x18\n\x0bresource_id\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x15\n\x08relation\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x44\n\x0esubject_filter\x18\x05 \x01(\x0b\x32\'.kessel.relations.v1beta1.SubjectFilterH\x04\x88\x01\x01\x42\x15\n\x13_resource_namespaceB\x10\n\x0e_resource_typeB\x0e\n\x0c_resource_idB\x0b\n\t_relationB\x11\n\x0f_subject_filter\"\xbd\x01\n\rSubjectFilter\x12\x1e\n\x11subject_namespace\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x19\n\x0csubject_type\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x17\n\nsubject_id\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x15\n\x08relation\x18\x04 \x01(\tH\x03\x88\x01\x01\x42\x14\n\x12_subject_namespaceB\x0f\n\r_subject_typeB\r\n\x0b_subject_idB\x0b\n\t_relation2\xae\x03\n\x12KesselTupleService\x12\x89\x01\n\x0c\x43reateTuples\x12-.kessel.relations.v1beta1.CreateTuplesRequest\x1a..kessel.relations.v1beta1.CreateTuplesResponse\"\x1a\x82\xd3\xe4\x93\x02\x14\"\x0f/v1beta1/tuples:\x01*\x12\x82\x01\n\nReadTuples\x12+.kessel.relations.v1beta1.ReadTuplesRequest\x1a,.kessel.relations.v1beta1.ReadTuplesResponse\"\x17\x82\xd3\xe4\x93\x02\x11\x12\x0f/v1beta1/tuples0\x01\x12\x86\x01\n\x0c\x44\x65leteTuples\x12-.kessel.relations.v1beta1.DeleteTuplesRequest\x1a..kessel.relations.v1beta1.DeleteTuplesResponse\"\x17\x82\xd3\xe4\x93\x02\x11*\x0f/v1beta1/tuplesBr\n(org.project_kessel.api.relations.v1beta1P\x01ZDgithub.com/project-kessel/relations-api/api/kessel/relations/v1beta1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'kessel.relations.v1beta1.relation_tuples_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n(org.project_kessel.api.relations.v1beta1P\001ZDgithub.com/project-kessel/relations-api/api/kessel/relations/v1beta1'
  _globals['_READTUPLESREQUEST'].fields_by_name['filter']._loaded_options = None
  _globals['_READTUPLESREQUEST'].fields_by_name['filter']._serialized_options = b'\372B\005\242\001\002\010\001'
  _globals['_DELETETUPLESREQUEST'].fields_by_name['filter']._loaded_options = None
  _globals['_DELETETUPLESREQUEST'].fields_by_name['filter']._serialized_options = b'\372B\005\242\001\002\010\001'
  _globals['_KESSELTUPLESERVICE'].methods_by_name['CreateTuples']._loaded_options = None
  _globals['_KESSELTUPLESERVICE'].methods_by_name['CreateTuples']._serialized_options = b'\202\323\344\223\002\024\"\017/v1beta1/tuples:\001*'
  _globals['_KESSELTUPLESERVICE'].methods_by_name['ReadTuples']._loaded_options = None
  _globals['_KESSELTUPLESERVICE'].methods_by_name['ReadTuples']._serialized_options = b'\202\323\344\223\002\021\022\017/v1beta1/tuples'
  _globals['_KESSELTUPLESERVICE'].methods_by_name['DeleteTuples']._loaded_options = None
  _globals['_KESSELTUPLESERVICE'].methods_by_name['DeleteTuples']._serialized_options = b'\202\323\344\223\002\021*\017/v1beta1/tuples'
  _globals['_CREATETUPLESREQUEST']._serialized_start=170
  _globals['_CREATETUPLESREQUEST']._serialized_end=263
  _globals['_CREATETUPLESRESPONSE']._serialized_start=265
  _globals['_CREATETUPLESRESPONSE']._serialized_end=287
  _globals['_READTUPLESREQUEST']._serialized_start=290
  _globals['_READTUPLESREQUEST']._serialized_end=467
  _globals['_READTUPLESRESPONSE']._serialized_start=470
  _globals['_READTUPLESRESPONSE']._serialized_end=611
  _globals['_DELETETUPLESREQUEST']._serialized_start=613
  _globals['_DELETETUPLESREQUEST']._serialized_end=707
  _globals['_DELETETUPLESRESPONSE']._serialized_start=709
  _globals['_DELETETUPLESRESPONSE']._serialized_end=731
  _globals['_RELATIONTUPLEFILTER']._serialized_start=734
  _globals['_RELATIONTUPLEFILTER']._serialized_end=1024
  _globals['_SUBJECTFILTER']._serialized_start=1027
  _globals['_SUBJECTFILTER']._serialized_end=1216
  _globals['_KESSELTUPLESERVICE']._serialized_start=1219
  _globals['_KESSELTUPLESERVICE']._serialized_end=1649
# @@protoc_insertion_point(module_scope)
