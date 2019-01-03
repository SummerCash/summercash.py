import grpc

from proto.grpc import common_pb2
from proto.grpc import common_pb2_grpc


def run():
    with grpc.secure_channel('https://localhost:8080') as channel:
        stub = common_pb2_grpc.CommonStub(channel)
        
        response = stub.DecodeString(common_pb2.GeneralRequest(input=b'test', s='test'))
    print("Greeter client received: " + response.message)


if __name__ == '__main__':
    run()
# python3 -m grpc_tools.protoc -I./proto/src --python_out=./proto/build --grpc_python_out=. ./proto/src/*