import requests, json
import common.common as common
import main as main

def GeneralRequest(genesisPath):
    obj = {
        "genesisPath": genesisPath
    }

    return obj

def CallMethod(self, method, genesisPath):
    response = requests.post(main.provider + "/twirp/chainConfig.ChainConfig/" + method, data = json.dumps(GeneralRequest(genesisPath)),
        headers=common.RequestHeaders, verify=common.RequestShouldVerify) # Send request
    return common.GetRequestResponse(response) # Return response