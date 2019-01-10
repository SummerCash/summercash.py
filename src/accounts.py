import requests
import json
import common.common as common
import main as main

def GeneralRequest(address, privateKey):
    obj = {
        "address": address,
        "privateKey": privateKey
    }

    return obj

def CallMethod(method, address, privateKey):
    response = requests.post(main.provider + "/twirp/accounts.Accounts/" + method, data = json.dumps(GeneralRequest(address, privateKey)),
        headers=common.RequestHeaders, verify=common.RequestShouldVerify) # Send request
    return common.GetRequestResponse(response) # Return response # Return response