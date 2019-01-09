import requests

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
        response = requests.post(self.stub + method, data = GeneralRequest(_input, n))
        return response.message