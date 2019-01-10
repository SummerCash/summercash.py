import requests

def GeneralRequest(nonce, address, address2, amount, payload):
    obj = {
        "nonce": nonce,
        "address": address,
        "address2": address2,
        "amount": amount,
        "payload": payload
    }
    return obj

class Transaction:
    def __init__(self, server):
        self.server = server
        self.server.ip
        self.stub = self.server.ip + "/twirp/transaction.Transaction/"

    def CallMethod(self, method, nonce, address, address2, amount, payload):
        response = requests.get(self.stub + method, data = GeneralRequest(nonce, address, address2, amount, payload))
        return response.message
