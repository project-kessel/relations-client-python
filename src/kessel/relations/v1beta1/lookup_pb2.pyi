from google.api import annotations_pb2 as _annotations_pb2
from kessel.relations.v1beta1 import common_pb2 as _common_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LookupResourcesRequest(_message.Message):
    __slots__ = ("resource_type", "relation", "subject", "pagination", "consistency")
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    RELATION_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    CONSISTENCY_FIELD_NUMBER: _ClassVar[int]
    resource_type: _common_pb2.ObjectType
    relation: str
    subject: _common_pb2.SubjectReference
    pagination: _common_pb2.RequestPagination
    consistency: _common_pb2.Consistency
    def __init__(self, resource_type: _Optional[_Union[_common_pb2.ObjectType, _Mapping]] = ..., relation: _Optional[str] = ..., subject: _Optional[_Union[_common_pb2.SubjectReference, _Mapping]] = ..., pagination: _Optional[_Union[_common_pb2.RequestPagination, _Mapping]] = ..., consistency: _Optional[_Union[_common_pb2.Consistency, _Mapping]] = ...) -> None: ...

class LookupResourcesResponse(_message.Message):
    __slots__ = ("resource", "pagination", "consistency_token")
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    CONSISTENCY_TOKEN_FIELD_NUMBER: _ClassVar[int]
    resource: _common_pb2.ObjectReference
    pagination: _common_pb2.ResponsePagination
    consistency_token: _common_pb2.ConsistencyToken
    def __init__(self, resource: _Optional[_Union[_common_pb2.ObjectReference, _Mapping]] = ..., pagination: _Optional[_Union[_common_pb2.ResponsePagination, _Mapping]] = ..., consistency_token: _Optional[_Union[_common_pb2.ConsistencyToken, _Mapping]] = ...) -> None: ...

class LookupSubjectsRequest(_message.Message):
    __slots__ = ("resource", "relation", "subject_type", "subject_relation", "pagination", "consistency")
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    RELATION_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_RELATION_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    CONSISTENCY_FIELD_NUMBER: _ClassVar[int]
    resource: _common_pb2.ObjectReference
    relation: str
    subject_type: _common_pb2.ObjectType
    subject_relation: str
    pagination: _common_pb2.RequestPagination
    consistency: _common_pb2.Consistency
    def __init__(self, resource: _Optional[_Union[_common_pb2.ObjectReference, _Mapping]] = ..., relation: _Optional[str] = ..., subject_type: _Optional[_Union[_common_pb2.ObjectType, _Mapping]] = ..., subject_relation: _Optional[str] = ..., pagination: _Optional[_Union[_common_pb2.RequestPagination, _Mapping]] = ..., consistency: _Optional[_Union[_common_pb2.Consistency, _Mapping]] = ...) -> None: ...

class LookupSubjectsResponse(_message.Message):
    __slots__ = ("subject", "pagination", "consistency_token")
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    CONSISTENCY_TOKEN_FIELD_NUMBER: _ClassVar[int]
    subject: _common_pb2.SubjectReference
    pagination: _common_pb2.ResponsePagination
    consistency_token: _common_pb2.ConsistencyToken
    def __init__(self, subject: _Optional[_Union[_common_pb2.SubjectReference, _Mapping]] = ..., pagination: _Optional[_Union[_common_pb2.ResponsePagination, _Mapping]] = ..., consistency_token: _Optional[_Union[_common_pb2.ConsistencyToken, _Mapping]] = ...) -> None: ...
