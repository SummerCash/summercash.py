message GeneralRequest {
    uint32 nonce = 1; // Transaction nonce

    string address = 2; // Transaction address

    string address2 = 3; // Second address

    double amount = 4; // Tx amount (actually a float64)

    bytes payload = 5; // Tx payload
}

import requests

def GeneralRequest(nonce, address, address2, amount, payload):
    obj = {
        "nonce": nonce,
        "address": address
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
        response = requests.post(self.stub + method, data = GeneralRequest(nonce, address, address2, amount, payload))
        return response.message