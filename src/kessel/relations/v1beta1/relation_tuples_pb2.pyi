from google.api import annotations_pb2 as _annotations_pb2
from kessel.relations.v1beta1 import common_pb2 as _common_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ImportBulkTuplesRequest(_message.Message):
    __slots__ = ("tuples",)
    TUPLES_FIELD_NUMBER: _ClassVar[int]
    tuples: _containers.RepeatedCompositeFieldContainer[_common_pb2.Relationship]
    def __init__(self, tuples: _Optional[_Iterable[_Union[_common_pb2.Relationship, _Mapping]]] = ...) -> None: ...

class ImportBulkTuplesResponse(_message.Message):
    __slots__ = ("num_imported",)
    NUM_IMPORTED_FIELD_NUMBER: _ClassVar[int]
    num_imported: int
    def __init__(self, num_imported: _Optional[int] = ...) -> None: ...

class CreateTuplesRequest(_message.Message):
    __slots__ = ("upsert", "tuples")
    UPSERT_FIELD_NUMBER: _ClassVar[int]
    TUPLES_FIELD_NUMBER: _ClassVar[int]
    upsert: bool
    tuples: _containers.RepeatedCompositeFieldContainer[_common_pb2.Relationship]
    def __init__(self, upsert: bool = ..., tuples: _Optional[_Iterable[_Union[_common_pb2.Relationship, _Mapping]]] = ...) -> None: ...

class CreateTuplesResponse(_message.Message):
    __slots__ = ("consistency_token",)
    CONSISTENCY_TOKEN_FIELD_NUMBER: _ClassVar[int]
    consistency_token: _common_pb2.ConsistencyToken
    def __init__(self, consistency_token: _Optional[_Union[_common_pb2.ConsistencyToken, _Mapping]] = ...) -> None: ...

class ReadTuplesRequest(_message.Message):
    __slots__ = ("filter", "pagination", "consistency")
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    CONSISTENCY_FIELD_NUMBER: _ClassVar[int]
    filter: RelationTupleFilter
    pagination: _common_pb2.RequestPagination
    consistency: _common_pb2.Consistency
    def __init__(self, filter: _Optional[_Union[RelationTupleFilter, _Mapping]] = ..., pagination: _Optional[_Union[_common_pb2.RequestPagination, _Mapping]] = ..., consistency: _Optional[_Union[_common_pb2.Consistency, _Mapping]] = ...) -> None: ...

class ReadTuplesResponse(_message.Message):
    __slots__ = ("tuple", "pagination", "consistency_token")
    TUPLE_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    CONSISTENCY_TOKEN_FIELD_NUMBER: _ClassVar[int]
    tuple: _common_pb2.Relationship
    pagination: _common_pb2.ResponsePagination
    consistency_token: _common_pb2.ConsistencyToken
    def __init__(self, tuple: _Optional[_Union[_common_pb2.Relationship, _Mapping]] = ..., pagination: _Optional[_Union[_common_pb2.ResponsePagination, _Mapping]] = ..., consistency_token: _Optional[_Union[_common_pb2.ConsistencyToken, _Mapping]] = ...) -> None: ...

class DeleteTuplesRequest(_message.Message):
    __slots__ = ("filter",)
    FILTER_FIELD_NUMBER: _ClassVar[int]
    filter: RelationTupleFilter
    def __init__(self, filter: _Optional[_Union[RelationTupleFilter, _Mapping]] = ...) -> None: ...

class DeleteTuplesResponse(_message.Message):
    __slots__ = ("consistency_token",)
    CONSISTENCY_TOKEN_FIELD_NUMBER: _ClassVar[int]
    consistency_token: _common_pb2.ConsistencyToken
    def __init__(self, consistency_token: _Optional[_Union[_common_pb2.ConsistencyToken, _Mapping]] = ...) -> None: ...

class RelationTupleFilter(_message.Message):
    __slots__ = ("resource_namespace", "resource_type", "resource_id", "relation", "subject_filter")
    RESOURCE_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    RELATION_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FILTER_FIELD_NUMBER: _ClassVar[int]
    resource_namespace: str
    resource_type: str
    resource_id: str
    relation: str
    subject_filter: SubjectFilter
    def __init__(self, resource_namespace: _Optional[str] = ..., resource_type: _Optional[str] = ..., resource_id: _Optional[str] = ..., relation: _Optional[str] = ..., subject_filter: _Optional[_Union[SubjectFilter, _Mapping]] = ...) -> None: ...

class SubjectFilter(_message.Message):
    __slots__ = ("subject_namespace", "subject_type", "subject_id", "relation")
    SUBJECT_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    RELATION_FIELD_NUMBER: _ClassVar[int]
    subject_namespace: str
    subject_type: str
    subject_id: str
    relation: str
    def __init__(self, subject_namespace: _Optional[str] = ..., subject_type: _Optional[str] = ..., subject_id: _Optional[str] = ..., relation: _Optional[str] = ...) -> None: ...
