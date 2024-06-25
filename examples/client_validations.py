# To get all validations you can grep proto files with string "validate.rules"
# from https://github.com/project-kessel/relations-api/tree/main/api/relations/v0

from __future__ import print_function

import logging

import grpc
from relations.v0 import relation_tuples_pb2 
from relations.v0 import relation_tuples_pb2_grpc
from relations.v0 import common_pb2

from protoc_gen_validate.validator import validate, ValidationFailed, validate_all

relation_api_gRPC_server = "localhost:9000"
CHECK_ALLOWED = 1


def run():
    print("--Start of CreateTuples and empty relation attribute should cause validation error--")
    with grpc.insecure_channel(relation_api_gRPC_server) as channel:
        stub = relation_tuples_pb2_grpc.KesselTupleServiceStub(channel)

        request = relation_tuples_pb2.CreateTuplesRequest(
            upsert=True,
            tuples=[
                common_pb2.Relationship(
                    resource=common_pb2.ObjectReference(type=common_pb2.ObjectType(name="group"), id="bob_club"),
                    relation="",
                    subject=common_pb2.SubjectReference(
                        subject=common_pb2.ObjectReference(type=common_pb2.ObjectType(name="user"), id="bob")
                    )
                )
            ]
        )

        try:
            validate(request)
            responses = stub.CreateTuples(request)
            print(responses)
        except ValidationFailed as err:
            print(err)  # p.relation length is less than 1

    print("--End of CreateTuples--")
    print()

    print("--Start of CreateTuples and validate all is used--")

    with grpc.insecure_channel(relation_api_gRPC_server) as channel:
        stub = relation_tuples_pb2_grpc.KesselTupleServiceStub(channel)

        request = relation_tuples_pb2.CreateTuplesRequest(
            upsert=True,
            tuples=[
                common_pb2.Relationship()
            ]
        )

        try:
            validate_all(request)
            responses = stub.CreateTuples(request)
            print(responses)
        except ValidationFailed as err:
            # p.resource is required.
            # p.relation length is less than 1
            # p.subject is required.
            print(err)


    print("--End of CreateTuples--")
    print()

    print("--Start of CreateTuples and nested validations--")
    with grpc.insecure_channel(relation_api_gRPC_server) as channel:
        stub = relation_tuples_pb2_grpc.KesselTupleServiceStub(channel)

        print("--Validate Object Type --")
        resource_object_type = common_pb2.ObjectType(name="group")
        try:
            validate_all(resource_object_type)
        except ValidationFailed as err:
            print(err)
        print("--Validate Object Type End--")

        print("--Validate Object Reference --")
        resource = common_pb2.ObjectReference(type=resource_object_type, id="")
        try:
            validate_all(resource)
        except ValidationFailed as err:
            print(err)
        print("--Validate Object Reference End--")

        request = relation_tuples_pb2.CreateTuplesRequest(
            upsert=True,
            tuples=[
                common_pb2.Relationship(
                    resource=resource,
                    relation="",
                    subject=common_pb2.SubjectReference(
                        subject=common_pb2.ObjectReference(type=common_pb2.ObjectType(name="user"), id="bob")
                    )
                )
            ]
        )

        try:
            validate(request)
            responses = stub.CreateTuples(request)
            print(responses)
        except ValidationFailed as err:
            print(err)  # p.relation length is less than 1

    print("--End of CreateTuples--")
    print()


if __name__ == "__main__":
    logging.basicConfig()
    run()

