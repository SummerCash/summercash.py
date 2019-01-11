import requests
import json
import src.commonutil.common as common
import src.main as main


def GeneralRequests(nonce, address, address2, amount, payload):
    """
    Gets an object from the specified parameter.

    :param nonce:
    :param address:
    :param address2:
    :param amount:
    :param payload:
    :return: obj
    """
    obj = {
        "nonce": nonce,
        "address": address,
        "address2": address2,
        "amount": amount,
        "payload": payload
    }

    return obj


def CallMethod(method, nonce, address, address2, amount, payload):
    """
    Calls a method

    :param method:
    :param nonce:
    :param address:
    :param address2:
    :param amount:
    :param payload:
    :return: Response
    """
    response = requests.post(main.provider + "/twirp/transaction.Transaction/" + method, data = json.dumps(GeneralRequest(nonce, address, address2, amount, payload)),
        headers=common.RequestHeaders, verify=common.RequestShouldVerify) # Send request
    return common.GetRequestResponse(response) # Return response
