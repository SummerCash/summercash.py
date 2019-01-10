import requests
import json
import common.common as common

def GeneralRequest(address):
    obj = {
        "address": address
    }

    return obj

class Chain:
    def __init__(self, server):
        self.server = server
        self.server.ip
        self.stub = self.server.ip + "/twirp/chain.Chain/"

    def CallMethod(self, method, address):
        response = requests.post(self.stub + method, data = json.dumps(GeneralRequest(address)),
            headers=common.RequestHeaders, verify=common.RequestShouldVerify) # Send request
        return common.GetRequestResponse(response) # Return response