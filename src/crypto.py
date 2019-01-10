import requests, json
import common.common as common
import main as main

def GeneralRequest(_input, n):
    obj = {
        "input": _input,
        "n": n
    }

    return obj

def CallMethod(self, method, _input, n):
    response = requests.post(main.provider + "/twirp/crypto.Crypto/" + method, data = json.dumps(GeneralRequest(_input, n)),
        headers=common.RequestHeaders, verify=common.RequestShouldVerify) # Send request
    return common.GetRequestResponse(response) # Return response