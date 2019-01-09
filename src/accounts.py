import requests

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
        response = requests.post(self.stub + method, data = GeneralRequest(address, privateKey))
        return response.message