import requests
import json
import src.commonutil.common as common
import src.main as main


def GeneralRequest():
    """
    Returns an empty array

    :return: Empty array (obj)
    """
    obj = {}

    return obj


def CallMethod(method):
    """
    Makes a request

    :param method:
    :return: Response
    """
    response = requests.post(main.GetProvider() + "/twirp/coordinationChain.CoordinationChain/" + method,
                             data=json.dumps(GeneralRequest()),
                             headers=common.RequestHeaders,
                             verify=common.RequestShouldVerify)  # Send request
    return common.GetRequestResponse(response)
