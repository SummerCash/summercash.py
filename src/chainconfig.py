import requests
import json
import src.commonutil.common as common
import src.main as main


def GeneralRequest(genesisPath):
    """
    Returns an object with the passed genesisPath

    :param genesisPath:
    :return:
    """
    obj = {
        "genesisPath": genesisPath
    }

    return obj


def CallMethod(method, genesisPath):
    """
    Calls a requests action

    :param method:
    :param genesisPath:
    :return: response
    """
    response = requests.post(main.GetProvider() + "/twirp/chainConfig.ChainConfig/" + method,
                             data=json.dumps(GeneralRequest(genesisPath)),
                             headers=common.RequestHeaders,
                             verify=common.RequestShouldVerify)  # Send request
    return common.GetRequestResponse(response)
