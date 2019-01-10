import requests, json
import src.commonutil.common as common
import src.main as main

def GeneralRequest(_input, s):
    obj = {
        "input": _input,
        "s": s
    }

    return obj

def CallMethod(method, _input, s):
    response = requests.post(main.GetProvider() + "/twirp/common.Common/" + method, data = json.dumps(GeneralRequest(_input, s)),
        headers=common.RequestHeaders, verify=common.RequestShouldVerify) # Send request
    return common.GetRequestResponse(response) # Return response