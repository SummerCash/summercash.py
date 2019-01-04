import grpc

from proto.build import crypto_pb2, crypto_pb2_grpc

class Crypto:
    def __init__(self, channel):
        self.channel = channel
        self.stub = crypto_pb2_grpc.CryptoStub(channel)

    def Sha3(self, _input, n):
        response = self.stub.Sha3(crypto_pb2.GeneralRequest(input=_input, n=n))
        return response.message

    def Sha3String(self, _input, n):
        response = self.stub.Sha3String(crypto_pb2.GeneralRequest(input=_input, n=n))
        return response.message

    def Sha3n(self, _input, n):
        response = self.stub.Sha3n(crypto_pb2.GeneralRequest(input=_input, n=n))
        return response.message

    def Sha3nString(self, _input, n):
        response = self.stub.Sha3nString(crypto_pb2.GeneralRequest(input=_input, n=n))
        return response.message

    def Sha3d(self, _input, n):
        response = self.stub.Sha3d(crypto_pb2.GeneralRequest(input=_input, n=n))
        return response.message

    def Sha3dString(self, _input, n):
        response = self.stub.Sha3dString(crypto_pb2.GeneralRequest(input=_input, n=n))
        return response.message