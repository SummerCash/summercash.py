from proto import accounts_pb2
from service import Service

def NewAccountDone():
    print("== DONE == NewAccount")

def NewAccount():
    # done = NewAccountDone

    # service.CallMethod(method_descriptor, rpc_controller, request, done)

    method = GetDescriptor()
    print(method)

NewAccount()
# def AccountFromKey():

# def GetAllAccounts():

# def MakeEncodingSafe():

# def RecoverSafeEncoding():

# def String():

# def Bytes():

# def ReadAccountFromMemory():
