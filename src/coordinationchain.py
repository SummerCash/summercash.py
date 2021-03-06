import requests, json
import src.commonutil.common as common
import src.main as main

def GeneralRequest():
    obj = { }

    return obj

def CallMethod(method):
    response = requests.post(main.provider + "/twirp/coordinationChain.CoordinationChain/" + method, data = json.dumps(GeneralRequest()),
        headers=common.RequestHeaders, verify=common.RequestShouldVerify) # Send request
    return common.GetRequestResponse(response) # Return response