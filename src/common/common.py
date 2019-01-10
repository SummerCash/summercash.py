RequestHeaders = {'Content-type': 'application/json'} # Init request headers
RequestShouldVerify = False # Global definition for verify= param

# GetRequestResponse - determine proper response, return it
def GetRequestResponse(request):
    if "msg" in request.keys(): # Check error
        return request['msg'] # Return response
    elif "message" in request.keys(): # Check success
        return request['message'] # Return response
    else:
        return request['meta'] # Return RPC error