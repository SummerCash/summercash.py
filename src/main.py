import grpc
import os
from grpc.beta import implementations


class API:
    def __init__(self, rpcIP):
        self.ip = rpcIP
        self.cert = self.LoadCert("term")
        self.key = self.LoadKey("term")

        # self.credentials = grpc.ssl_channel_credentials(
        #     private_key=self.key,
        #     certificate_chain=self.cert
        # )
        self.credentials = implementations.ssl_channel_credentials(
            private_key=self.key,
            certificate_chain=self.cert
        )
        
        

    def LoadCert(self, prefix):
        with open(os.path.abspath("../certs/new/" + prefix + "Cert.pem"), "rb") as f:
            return f.read()

    def LoadKey(self, prefix):
        with open(os.path.abspath("../certs/new/" + prefix + "Key.pem"), "rb") as f:
            return f.read()
    
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