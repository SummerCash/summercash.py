import requests
import json
import common.common as common

def GeneralRequest(address, privateKey):
    obj = {
        "address": address,
        "privateKey": privateKey
    }

    return obj

class Accounts:
    def __init__(self, server):
        self.server = server
        self.server.ip
        self.stub = self.server.ip + "/twirp/accounts.Accounts/"

    def CallMethod(self, method, address, privateKey):
        response = requests.post(self.stub + method, data = json.dumps(GeneralRequest(address, privateKey)),
            headers=common.RequestHeaders, verify=common.RequestShouldVerify) # Send request
        return common.GetRequestResponse(response) # Return response # Return response