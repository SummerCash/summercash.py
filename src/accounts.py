import grpc

from proto.grpc import accounts_pb2
from proto.grpc import accounts_pb2_grpc

class Accounts:
    def __init__(self, channel):
        self.channel = channel
        self.stub = accounts_pb2_grpc.AccountsStub(channel)

    def NewAccount(self, address, privateKey)
        response = self.stub.NewAccount(accounts_pb2.GeneralRequest(address=address, privateKey=privateKey))
        return response.message

    def AccountFromKey(self, address, privateKey):
        response = self.stub.AccountFromKey(accounts_pb2.GeneralRequest(address=address, privateKey=privateKey))
        return response.message

    def GetAllAccounts(self, address, privateKey):
        response = self.stub.GetAllAccounts(accounts_pb2.GeneralRequest(address=address, privateKey=privateKey))
        return response.message

    def MakeEncodingSafe(self, address, privateKey):
        response = self.stub.MakeEncodingSafe(accounts_pb2.GeneralRequest(address=address, privateKey=privateKey))
        return response.message

    def RecoverSafeEncoding(self, address, privateKey):
        response = self.stub.RecoverSafeEncoding(accounts_pb2.GeneralRequest(address=address, privateKey=privateKey))
        return response.message
        
    def String(self, address, privateKey):
        response = self.stub.String(accounts_pb2.GeneralRequest(address=address, privateKey=privateKey))
        return response.message

    def Bytes(self, address, privateKey):
        response = self.stub.Bytes(accounts_pb2.GeneralRequest(address=address, privateKey=privateKey))
        return response.message

    def ReadAccountFromMemory(self, address, privateKey):
        response = self.stub.ReadAccountFromMemory(accounts_pb2.GeneralRequest(address=address, privateKey=privateKey))
        return response.message
