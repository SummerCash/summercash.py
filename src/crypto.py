import requests
import json
import src.commonutil.common as common
import src.main as main


def GeneralRequest(_input, n):
    """
    Returns an array based on inputted parameters

    :param _input:
    :param n:
    :return: Generated object
    """
    obj = {
        "input": _input,
        "n": n
    }

    return obj


def CallMethod(method, _input, n):
    """
    Calls a method

    :param method:
    :param _input:
    :param n:
    :return: Response
    """
    response = requests.post(main.GetProvider() + "/twirp/crypto.Crypto/" + method,
                             data=json.dumps(GeneralRequest(_input, n)),
                             headers=common.RequestHeaders,
                             verify=common.RequestShouldVerify)  # Send request
    return common.GetRequestResponse(response)
