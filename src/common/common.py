RequestHeaders = {'Content-type': 'application/json'} # Init request headers
RequestShouldVerify = False # Global definition for verify= param

# GetRequestResponse - determine proper response, return it
def GetRequestResponse(request):
    if "msg" in request.json().keys(): # Check error
        return request.json()['msg'] # Return response
    elif "message" in request.json().keys(): # Check success
        return request.json()['message'] # Return response
    else:
        return request.json()['meta'] # Return RPC error