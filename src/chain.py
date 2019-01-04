import grpc

from proto.grpc import chain_pb2
from proto.grpc import chain_pb2_grpc

class Chain:
    def __init__(self, channel):
        self.channel = channel
        self.stub = chain_pb2_grpc.ChainStub(channel)

    def GetBalance(self, address)
        response = self.stub.GetBalance(chain_pb2.GeneralRequest(address=address))
        return response.message

    def Bytes(self, address):
        response = self.stub.Bytes(chain_pb2.GeneralRequest(address=address))
        return response.message

    def String(self, address):
        response = self.stub.String(chain_pb2.GeneralRequest(address=address))
        return response.message

    def ReadChainFromMemory(self, address):
        response = self.stub.ReadChainFromMemory(chain_pb2.GeneralRequest(address=address))
        return response.message

    def QueryTransaction(self, address):
        response = self.stub.QueryTransaction(chain_pb2.GeneralRequest(address=address))
        return response.message
        
    def GetNumTransactions(self, address):
        response = self.stub.GetNumTransactions(chain_pb2.GeneralRequest(address=address))
        return response.message