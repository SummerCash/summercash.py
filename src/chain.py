import requests, json
import common.common as common
import main as main

def GeneralRequest(address):
    obj = {
        "address": address
    }

    return obj

def CallMethod(method, address):
    response = requests.post(main.provider + "/twirp/chain.Chain/" + method, data = json.dumps(GeneralRequest(address)),
        headers=common.RequestHeaders, verify=common.RequestShouldVerify) # Send request
    return common.GetRequestResponse(response) # Return response