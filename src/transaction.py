import requests
import json
import common.common as common

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
        response = requests.post(self.stub + method, data = json.dumps(GeneralRequest(nonce, address, address2, amount, payload)),
            headers=common.RequestHeaders, verify=common.RequestShouldVerify) # Send request
        return common.GetRequestResponse(response) # Return response
