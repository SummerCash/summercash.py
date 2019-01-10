import requests, json
import common.common as common
import main as main

def GeneralRequest(_input, s):
    obj = {
        "input": _input,
        "s": s
    }

    return obj

def CallMethod(self, method, _input, s):
    response = requests.post(main.provider + "/twirp/common.Common/" + method, data = json.dumps(GeneralRequest(_input, s)),
        headers=common.RequestHeaders, verify=common.RequestShouldVerify) # Send request
    return common.GetRequestResponse(response) # Return response