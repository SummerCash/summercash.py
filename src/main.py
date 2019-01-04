import grpc
import os

class API:
    def __init__(self, rpcIP):
        self.ip = rpcIP
        self.cert = self.LoadCert("term")
        self.key = self.LoadKey("term")

        self.credentials = grpc.ssl_channel_credentials(
            private_key=self.key,
            certificate_chain=self.cert
        )

    def LoadCert(self, prefix):
        with open(os.path.abspath("certs/new/" + prefix + "Cert.pem"), "rb") as f:
            return f.read()

    def LoadKey(self, prefix):
        with open(os.path.abspath("certs/new/" + prefix + "Key.pem"), "rb") as f:
            return f.read()
    
    def GetChannel(self):
        with grpc.secure_channel(target=self.ip, credentials=self.credentials, options=None) as channel:
            self.channel = channel


if __name__ == "__main__":
    API("localhost:8080")


"""
command to build proto files
python3 -m grpc_tools.protoc -I./proto/src --python_out=./proto/build --grpc_python_out=. ./proto/src/*
"""