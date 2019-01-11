import requests
import json
import src.commonutil.common as common
import src.main as main


def GeneralRequest(_input, s):
    """
    Creates an object based on inputted parameters

    :param _input:
    :param s:
    :return:
    """
    obj = {
        "input": _input,
        "s": s
    }

    return obj


def CallMethod(method, _input, s):
    """
    Makes a request

    :param method:
    :param _input:
    :param s:
    :return: Response
    """
    response = requests.post(main.GetProvider() + "/twirp/common.Common/" + method,
                             data = json.dumps(GeneralRequest(_input, s)),
                             headers=common.RequestHeaders,
                             verify=common.RequestShouldVerify)  # Send request
    return common.GetRequestResponse(response)  # Return response
