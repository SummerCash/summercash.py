import requests
import json
import src.commonutil.common as common
import src.main as main


def general_request(_input, s):
    obj = {
        "input": _input,
        "s": s
    }

    return obj


def call_method(method, _input, s):
    """
    Makes a request

    :param method:
    :param _input:
    :param s:
    :return: Response
    """
    response = requests.post(main.get_provider() + "/twirp/common.Common/" + method,
                             data = json.dumps(general_request(_input, s)),
                             headers=common.RequestHeaders,
                             verify=common.RequestShouldVerify)  # Send request
    return common.GetRequestResponse(response)  # Return response
