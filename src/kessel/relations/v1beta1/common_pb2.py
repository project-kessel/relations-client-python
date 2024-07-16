# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kessel/relations/v1beta1/common.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%kessel/relations/v1beta1/common.proto\x12\x18kessel.relations.v1beta1\x1a\x17validate/validate.proto\"\xb7\x01\n\x0cRelationship\x12\x45\n\x08resource\x18\x01 \x01(\x0b\x32).kessel.relations.v1beta1.ObjectReferenceB\x08\xfa\x42\x05\xa2\x01\x02\x08\x01\x12\x19\n\x08relation\x18\x02 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\x12\x45\n\x07subject\x18\x03 \x01(\x0b\x32*.kessel.relations.v1beta1.SubjectReferenceB\x08\xfa\x42\x05\xa2\x01\x02\x08\x01\"|\n\x10SubjectReference\x12\x15\n\x08relation\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x44\n\x07subject\x18\x02 \x01(\x0b\x32).kessel.relations.v1beta1.ObjectReferenceB\x08\xfa\x42\x05\xa2\x01\x02\x08\x01\x42\x0b\n\t_relation\"c\n\x11RequestPagination\x12\x16\n\x05limit\x18\x01 \x01(\rB\x07\xfa\x42\x04*\x02 \x00\x12\x1f\n\x12\x63ontinuation_token\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x15\n\x13_continuation_token\"0\n\x12ResponsePagination\x12\x1a\n\x12\x63ontinuation_token\x18\x01 \x01(\t\"d\n\x0fObjectReference\x12<\n\x04type\x18\x01 \x01(\x0b\x32$.kessel.relations.v1beta1.ObjectTypeB\x08\xfa\x42\x05\xa2\x01\x02\x08\x01\x12\x13\n\x02id\x18\x02 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\"?\n\nObjectType\x12\x1a\n\tnamespace\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\x12\x15\n\x04name\x18\x02 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\x42r\n(org.project_kessel.api.relations.v1beta1P\x01ZDgithub.com/project-kessel/relations-api/api/kessel/relations/v1beta1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'kessel.relations.v1beta1.common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n(org.project_kessel.api.relations.v1beta1P\001ZDgithub.com/project-kessel/relations-api/api/kessel/relations/v1beta1'
  _globals['_RELATIONSHIP'].fields_by_name['resource']._loaded_options = None
  _globals['_RELATIONSHIP'].fields_by_name['resource']._serialized_options = b'\372B\005\242\001\002\010\001'
  _globals['_RELATIONSHIP'].fields_by_name['relation']._loaded_options = None
  _globals['_RELATIONSHIP'].fields_by_name['relation']._serialized_options = b'\372B\004r\002\020\001'
  _globals['_RELATIONSHIP'].fields_by_name['subject']._loaded_options = None
  _globals['_RELATIONSHIP'].fields_by_name['subject']._serialized_options = b'\372B\005\242\001\002\010\001'
  _globals['_SUBJECTREFERENCE'].fields_by_name['subject']._loaded_options = None
  _globals['_SUBJECTREFERENCE'].fields_by_name['subject']._serialized_options = b'\372B\005\242\001\002\010\001'
  _globals['_REQUESTPAGINATION'].fields_by_name['limit']._loaded_options = None
  _globals['_REQUESTPAGINATION'].fields_by_name['limit']._serialized_options = b'\372B\004*\002 \000'
  _globals['_OBJECTREFERENCE'].fields_by_name['type']._loaded_options = None
  _globals['_OBJECTREFERENCE'].fields_by_name['type']._serialized_options = b'\372B\005\242\001\002\010\001'
  _globals['_OBJECTREFERENCE'].fields_by_name['id']._loaded_options = None
  _globals['_OBJECTREFERENCE'].fields_by_name['id']._serialized_options = b'\372B\004r\002\020\001'
  _globals['_OBJECTTYPE'].fields_by_name['namespace']._loaded_options = None
  _globals['_OBJECTTYPE'].fields_by_name['namespace']._serialized_options = b'\372B\004r\002\020\001'
  _globals['_OBJECTTYPE'].fields_by_name['name']._loaded_options = None
  _globals['_OBJECTTYPE'].fields_by_name['name']._serialized_options = b'\372B\004r\002\020\001'
  _globals['_RELATIONSHIP']._serialized_start=93
  _globals['_RELATIONSHIP']._serialized_end=276
  _globals['_SUBJECTREFERENCE']._serialized_start=278
  _globals['_SUBJECTREFERENCE']._serialized_end=402
  _globals['_REQUESTPAGINATION']._serialized_start=404
  _globals['_REQUESTPAGINATION']._serialized_end=503
  _globals['_RESPONSEPAGINATION']._serialized_start=505
  _globals['_RESPONSEPAGINATION']._serialized_end=553
  _globals['_OBJECTREFERENCE']._serialized_start=555
  _globals['_OBJECTREFERENCE']._serialized_end=655
  _globals['_OBJECTTYPE']._serialized_start=657
  _globals['_OBJECTTYPE']._serialized_end=720
# @@protoc_insertion_point(module_scope)