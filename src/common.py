import requests
import json
import common.common as common

def GeneralRequest(_input, s):
    obj = {
        "input": _input,
        "s": s
    }
    
    return obj

class Common:
    def __init__(self, server):
        self.server = server
        self.server.ip
        self.stub = self.server.ip + "/twirp/common.Common/"

    def CallMethod(self, method, _input, s):
        response = requests.post(self.stub + method, data = json.dumps(GeneralRequest(_input, s)),
            headers=common.RequestHeaders, verify=common.RequestShouldVerify) # Send request
        return response.json()['msg'] # Return response