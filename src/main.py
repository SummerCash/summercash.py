import grpc
import os
from grpc.beta import implementations



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

    # GetChannel - get, store channel metadata
    def GetChannel(self):
        channel = grpc.secure_channel(target=self.ip, credentials=self.credentials, options=None)
        # with grpc.secure_channel(target=self.ip, credentials=self.credentials, options=None) as channel:
        #     self.channel = channel
        self.channel = implementations.Channel(channel)


if __name__ == "__main__":
    api = API("localhost:8080")
    api.GetChannel()
    import common
    _common = common.Common(api.channel)
    response = _common.Encode(b"test", "test")
    print(response)
#         with grpc.secure_channel(target=self.ip, credentials=self.credentials, options=None) as channel: # Init secure channelA
#             self.channel = channel # Set channel


# if __name__ == "__main__":
#     api = API("localhost:8080") # Init API instance
#     api.GetChannel() # Get API channel
