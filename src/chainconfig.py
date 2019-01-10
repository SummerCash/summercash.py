import requests
import json
import common.common as common

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
        response = requests.post(self.stub + method, data = json.dumps(GeneralRequest(genesisPath)),
        headers=common.RequestHeaders, verify=common.RequestShouldVerify) # Send request
        return common.GetRequestResponse(response) # Return response