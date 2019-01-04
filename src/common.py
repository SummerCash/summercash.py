import grpc

from proto.grpc import common_pb2
from proto.grpc import common_pb2_grpc

class Common:
    def __init__(self, channel):
        self.channel = channel
        self.stub = common_pb2_grpc.CommonStub(channel)

    def Encode(self, _input, s)
        response = self.stub.Encode(common_pb2.GeneralRequest(input=_input, s=s))
        return response.message

    def EncodeString(self, _input, s):
        response = self.stub.EncodeString(common_pb2.GeneralRequest(input=_input, s=s))
        return response.message

    def Decode(self, _input, s):
        response = self.stub.Decode(common_pb2.GeneralRequest(input=_input, s=s))
        return response.message

    def DecodeString(self, _input, s):
        response = self.stub.DecodeString(common_pb2.GeneralRequest(input=_input, s=s))
        return response.message