import requests
import json
import src.commonutil.common as common
import src.main as main


def general_request():
    """
    Returns an empty array

    :return: Empty array (obj)
    """
    obj = {}

    return obj


def call_method(method):
    """
    Makes a request

    :param method:
    :return: Response
    """
    response = requests.post(main.get_provider() + "/twirp/coordinationChain.CoordinationChain/" + method,
                             data=json.dumps(general_request()),
                             headers=common.RequestHeaders,
                             verify=common.RequestShouldVerify)  # Send request
    return common.GetRequestResponse(response)
