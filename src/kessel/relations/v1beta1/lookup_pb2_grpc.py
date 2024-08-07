# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from kessel.relations.v1beta1 import lookup_pb2 as kessel_dot_relations_dot_v1beta1_dot_lookup__pb2

GRPC_GENERATED_VERSION = '1.65.2'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.66.0'
SCHEDULED_RELEASE_DATE = 'August 6, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in kessel/relations/v1beta1/lookup_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class KesselLookupServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.LookupSubjects = channel.unary_stream(
                '/kessel.relations.v1beta1.KesselLookupService/LookupSubjects',
                request_serializer=kessel_dot_relations_dot_v1beta1_dot_lookup__pb2.LookupSubjectsRequest.SerializeToString,
                response_deserializer=kessel_dot_relations_dot_v1beta1_dot_lookup__pb2.LookupSubjectsResponse.FromString,
                _registered_method=True)
        self.LookupResources = channel.unary_stream(
                '/kessel.relations.v1beta1.KesselLookupService/LookupResources',
                request_serializer=kessel_dot_relations_dot_v1beta1_dot_lookup__pb2.LookupResourcesRequest.SerializeToString,
                response_deserializer=kessel_dot_relations_dot_v1beta1_dot_lookup__pb2.LookupResourcesResponse.FromString,
                _registered_method=True)


class KesselLookupServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def LookupSubjects(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LookupResources(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_KesselLookupServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'LookupSubjects': grpc.unary_stream_rpc_method_handler(
                    servicer.LookupSubjects,
                    request_deserializer=kessel_dot_relations_dot_v1beta1_dot_lookup__pb2.LookupSubjectsRequest.FromString,
                    response_serializer=kessel_dot_relations_dot_v1beta1_dot_lookup__pb2.LookupSubjectsResponse.SerializeToString,
            ),
            'LookupResources': grpc.unary_stream_rpc_method_handler(
                    servicer.LookupResources,
                    request_deserializer=kessel_dot_relations_dot_v1beta1_dot_lookup__pb2.LookupResourcesRequest.FromString,
                    response_serializer=kessel_dot_relations_dot_v1beta1_dot_lookup__pb2.LookupResourcesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'kessel.relations.v1beta1.KesselLookupService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('kessel.relations.v1beta1.KesselLookupService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class KesselLookupService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def LookupSubjects(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/kessel.relations.v1beta1.KesselLookupService/LookupSubjects',
            kessel_dot_relations_dot_v1beta1_dot_lookup__pb2.LookupSubjectsRequest.SerializeToString,
            kessel_dot_relations_dot_v1beta1_dot_lookup__pb2.LookupSubjectsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def LookupResources(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/kessel.relations.v1beta1.KesselLookupService/LookupResources',
            kessel_dot_relations_dot_v1beta1_dot_lookup__pb2.LookupResourcesRequest.SerializeToString,
            kessel_dot_relations_dot_v1beta1_dot_lookup__pb2.LookupResourcesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
