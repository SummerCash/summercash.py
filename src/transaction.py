import requests, json
import common.common as common
import main as main

def GeneralRequest(nonce, address, address2, amount, payload):
    obj = {
        "nonce": nonce,
        "address": address,
        "address2": address2,
        "amount": amount,
        "payload": payload
    }

    return obj

def CallMethod(self, method, nonce, address, address2, amount, payload):
    response = requests.post(main.provider + "/twirp/transaction.Transaction/" + method, data = json.dumps(GeneralRequest(nonce, address, address2, amount, payload)),
        headers=common.RequestHeaders, verify=common.RequestShouldVerify) # Send request
    return common.GetRequestResponse(response) # Return response
