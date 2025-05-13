from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Relationship(_message.Message):
    __slots__ = ("resource", "relation", "subject")
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    RELATION_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    resource: ObjectReference
    relation: str
    subject: SubjectReference
    def __init__(self, resource: _Optional[_Union[ObjectReference, _Mapping]] = ..., relation: _Optional[str] = ..., subject: _Optional[_Union[SubjectReference, _Mapping]] = ...) -> None: ...

class SubjectReference(_message.Message):
    __slots__ = ("relation", "subject")
    RELATION_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    relation: str
    subject: ObjectReference
    def __init__(self, relation: _Optional[str] = ..., subject: _Optional[_Union[ObjectReference, _Mapping]] = ...) -> None: ...

class RequestPagination(_message.Message):
    __slots__ = ("limit", "continuation_token")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    CONTINUATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    limit: int
    continuation_token: str
    def __init__(self, limit: _Optional[int] = ..., continuation_token: _Optional[str] = ...) -> None: ...

class ResponsePagination(_message.Message):
    __slots__ = ("continuation_token",)
    CONTINUATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    continuation_token: str
    def __init__(self, continuation_token: _Optional[str] = ...) -> None: ...

class ObjectReference(_message.Message):
    __slots__ = ("type", "id")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    type: ObjectType
    id: str
    def __init__(self, type: _Optional[_Union[ObjectType, _Mapping]] = ..., id: _Optional[str] = ...) -> None: ...

class ObjectType(_message.Message):
    __slots__ = ("namespace", "name")
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    namespace: str
    name: str
    def __init__(self, namespace: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class Consistency(_message.Message):
    __slots__ = ("minimize_latency", "at_least_as_fresh")
    MINIMIZE_LATENCY_FIELD_NUMBER: _ClassVar[int]
    AT_LEAST_AS_FRESH_FIELD_NUMBER: _ClassVar[int]
    minimize_latency: bool
    at_least_as_fresh: ConsistencyToken
    def __init__(self, minimize_latency: bool = ..., at_least_as_fresh: _Optional[_Union[ConsistencyToken, _Mapping]] = ...) -> None: ...

class ConsistencyToken(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...
