import grpc

from proto.grpc import common_pb2
from proto.grpc import common_pb2_grpc
from credentials import credentials

def run():
    # creds = grpc.ssl_channel_credentials(
    #     root_certificates=None,
    #     private_key=LoadKey(),
    #     certificate_chain=LoadCert()
        
    # )
    # # credentials = grpc.ssl_channel_credentials(LoadCert(), LoadKey())
    

    # with grpc.secure_channel(target="https://localhost:8080", credentials=credentials, options=None) as channel:
    with grpc.insecure_channel('https://localhost:8080') as channel:
        
        stub = common_pb2_grpc.CommonStub(channel)
        
        response = stub.DecodeString(common_pb2.GeneralRequest(input=b'test', s='test'))
    print("Client received: " + response.message)


if __name__ == '__main__':
    run()
# python3 -m grpc_tools.protoc -I./proto/src --python_out=./proto/build --grpc_python_out=. ./proto/src/*