import grpc

from proto.grpc import common_pb2
from proto.grpc import common_pb2_grpc
from credentials import credentials

def run():
    credentials = grpc.ssl_channel_credentials() # Get credentials

    with grpc.secure_channel(target="localhost:8080", credentials=credentials, options=None) as channel: # Open https channel
        stub = common_pb2_grpc.CommonStub(channel) # Get common.proto stub

        response = stub.DecodeString(common_pb2.GeneralRequest(input=b'test', s='test')) # Call
    print("Client received: " + response.message) # Get response


if __name__ == '__main__':
    run()
# python3 -m grpc_tools.protoc -I./proto/src --python_out=./proto/build --grpc_python_out=. ./proto/src/*
