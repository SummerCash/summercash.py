import requests
import json
import common.common as common

def GeneralRequest():
    obj = { }
    
    return obj

class CoordinationChain:
    def __init__(self, server):
        self.server = server
        self.server.ip
        self.stub = self.server.ip + "/twirp/coordinationChain.CoordinationChain/"

    def CallMethod(self, method):
        response = requests.post(self.stub + method, data = json.dumps(GeneralRequest()),
            headers=common.RequestHeaders, verify=common.RequestShouldVerify) # Send request
        return response.json()['msg'] # Return response