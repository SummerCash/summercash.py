import requests
import json
import common.common as common

def GeneralRequest(_input, n):
    obj = {
        "input": _input,
        "n": n
    }

    return obj

class Crypto:
    def __init__(self, server):
        self.server = server
        self.server.ip
        self.stub = self.server.ip + "/twirp/crypto.Crypto/"

    def CallMethod(self, method, _input, n):
        response = requests.post(self.stub + method, data = json.dumps(GeneralRequest(_input, n)),
            headers=common.RequestHeaders, verify=common.RequestShouldVerify) # Send request
        return common.GetRequestResponse(response) # Return response