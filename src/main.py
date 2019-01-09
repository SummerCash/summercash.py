import grpc
import os
# from grpc.beta import implementations

# import common

class API:
    # __init__ - initialize API instance
    def __init__(self, rpcIP):
        self.ip = rpcIP # Get IP
        self.cert = self.LoadCert("term") # Load certificate
        self.key = self.LoadKey("term") # Load key

        # self.credentials = grpc.ssl_channel_credentials(
        #     private_key=self.key,
        #     certificate_chain=self.cert
        # )
        # self.credentials = implementations.ssl_channel_credentials()
        self.credentials = grpc.ssl_channel_credentials( # Get credentials
            private_key=self.key,
            certificate_chain=self.cert
        )
        
        

    # LoadCert - load cert with given prefix
    def LoadCert(self, prefix):
        with open(os.path.abspath("../certs/new/" + prefix + "Cert.pem"), "rb") as f:
            return f.read()

    # LoadKey - load private key with given prefix
    def LoadKey(self, prefix):
        with open(os.path.abspath("../certs/new/" + prefix + "Key.pem"), "rb") as f:
            return f.read()

    # PrepChannel - prep, store channel metadata
    def PrepChannel(self):
        # channel = grpc.secure_channel(target=self.ip, credentials=self.credentials, options=None)
        with grpc.secure_channel(target=self.ip, credentials=self.credentials, options=None) as channel:
            # pass
            self.channel = channel
            from proto.build import common_pb2, common_pb2_grpc
            stub = common_pb2_grpc.CommonStub(self.channel)

            genReq = common_pb2.GeneralRequest(input=b"as", s="as")
            response = stub.Encode(genReq)


            # _common = common.Common(channel)
            # response = _common.Encode(b"test", "test")
            # print(response)
        # self.channel = implementations.Channel(channel)


if __name__ == "__main__":
    api = API("localhost:8080")
    api.PrepChannel()
    # import common
    # _common = common.Common(api.channel)
    # response = _common.Encode(b"test", "test")
#         with grpc.secure_channel(target=self.ip, credentials=self.credentials, options=None) as channel: # Init secure channelA
#             self.channel = channel # Set channel


# if __name__ == "__main__":
#     api = API("localhost:8080") # Init API instance
#     api.GetChannel() # Get API channel
