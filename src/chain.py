import requests

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
        response = requests.post(self.stub + method, data = GeneralRequest(address))
        return response.message