import requests

def GeneralRequest():
    obj = { }
    return obj

class CoordinationChain:
    def __init__(self, server):
        self.server = server
        self.server.ip
        self.stub = self.server.ip + "/twirp/coordinationChain.CoordinationChain/"

    def CallMethod(self, method):
        response = requests.post(self.stub + method, data = GeneralRequest())
        return response.message