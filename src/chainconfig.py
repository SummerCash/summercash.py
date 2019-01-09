import requests

def GeneralRequest(genesisPath):
    obj = {
        "genesisPath": genesisPath
    }
    return obj

class ChainConfig:
    def __init__(self, server):
        self.server = server
        self.server.ip
        self.stub = self.server.ip + "/twirp/chainConfig.ChainConfig/"

    def CallMethod(self, method, genesisPath):
        response = requests.post(self.stub + method, data = GeneralRequest(genesisPath))
        return response.message