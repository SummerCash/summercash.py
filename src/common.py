import requests

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
        response = requests.post(self.stub + method, data = GeneralRequest(_input, s))
        return response.message