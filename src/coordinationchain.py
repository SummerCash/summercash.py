import grpc

from proto.build import coordinationchain_pb2, coordinationchain_pb2_grpc

class CoordinationChain:
    def __init__(self, channel):
        self.channel = channel
        self.stub = coordinationchain_pb2_grpc.CoordinationChainStub(channel)

    def SyncNetwork(self):
        response = self.stub.SyncNetwork(coordinationchain_pb2.GeneralRequest())
        return response.message

    def GetPeers(self):
        response = self.stub.GetPeers(coordinationchain_pb2.GeneralRequest())
        return response.message

    def Bytes(self):
        response = self.stub.Bytes(coordinationchain_pb2.GeneralRequest())
        return response.message

    def String(self):
        response = self.stub.String(coordinationchain_pb2.GeneralRequest())
        return response.message