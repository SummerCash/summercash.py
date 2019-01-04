import grpc

from proto.grpc import chainconfig_pb2
from proto.grpc import chainconfig_pb2_grpc

class ChainConfig:
    def __init__(self, channel):
        self.channel = channel
        self.stub = chainconfig_pb2_grpc.ConfigStub(channel)

    def NewChainConfig(self, genesisPath)
        response = self.stub.NewChainConfig(chainconfig_pb2.GeneralRequest(genesisPath=genesisPath))
        return response.message

    def Bytes(self, genesisPath):
        response = self.stub.Bytes(chainconfig_pb2.GeneralRequest(genesisPath=genesisPath))
        return response.message

    def String(self, genesisPath):
        response = self.stub.String(chainconfig_pb2.GeneralRequest(genesisPath=genesisPath))
        return response.message

    def WriteToMemory(self, genesisPath):
        response = self.stub.WriteToMemory(chainconfig_pb2.GeneralRequest(genesisPath=genesisPath))
        return response.message

    def ReadChainConfigFromMemory(self, genesisPath):
        response = self.stub.ReadChainConfigFromMemory(chainconfig_pb2.GeneralRequest(genesisPath=genesisPath))
        return response.message
        
    def GetTotalSupply(self, genesisPath):
        response = self.stub.GetTotalSupply(chainconfig_pb2.GeneralRequest(genesisPath=genesisPath))
        return response.message