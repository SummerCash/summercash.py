import requests, json
import src.commonutil.common as common
import src.main as main

def GeneralRequest(address, privateKey):
    obj = {
        "address": address,
        "privateKey": privateKey
    }

    return obj


def CallMethod(method, address, privateKey):
    """
    Uses the requests library
    :param method:
    :param address:
    :param privateKey:
    :return:
    """
    response = requests.post(main.provider + "/twirp/accounts.Accounts/" + method, data = json.dumps(GeneralRequest(address, privateKey)),
        headers=common.RequestHeaders, verify=common.RequestShouldVerify) 
    return common.GetRequestResponse(response) 
