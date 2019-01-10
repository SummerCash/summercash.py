import requests, json
import src.commonutil.common as common
import src.main as main

def GeneralRequest(genesisPath):
    obj = {
        "genesisPath": genesisPath
    }

    return obj

def CallMethod(method, genesisPath):
    response = requests.post(main.provider + "/twirp/chainConfig.ChainConfig/" + method, data = json.dumps(GeneralRequest(genesisPath)),
        headers=common.RequestHeaders, verify=common.RequestShouldVerify) # Send request
    return common.GetRequestResponse(response) # Return response