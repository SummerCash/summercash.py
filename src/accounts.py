from proto import accounts_pb2
import google.protobuf.service



def NewAccountDone():
    print("== DONE == NewAccount")

def NewAccount():
    # done = NewAccountDone

    # service.CallMethod(method_descriptor, rpc_controller, request, done)
    service.GetDescriptor()

    MethodDescriptor(
    name='NewAccount',
    full_name='accounts.Accounts.NewAccount',
    index=0,
    containing_service=None,
    input_type=_GENERALREQUEST,
    output_type=_GENERALRESPONSE,
    serialized_options=None,
  )

    pass

NewAccount()
# def AccountFromKey():

# def GetAllAccounts():

# def MakeEncodingSafe():

# def RecoverSafeEncoding():

# def String():

# def Bytes():

# def ReadAccountFromMemory():
