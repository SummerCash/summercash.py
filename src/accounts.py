from protoc import accounts_pb2
import google.protobuf.service

def NewAccountDone():
    print("== DONE == NewAccount")

def NewAccount():
    # done = NewAccountDone

    CallMethod(method_descriptor, rpc_controller, request, done)

    # method = service.GetDescriptor().FindMethodByName("Foo")

NewAccount()
# def AccountFromKey():

# def GetAllAccounts():

# def MakeEncodingSafe():

# def RecoverSafeEncoding():

# def String():

# def Bytes():

# def ReadAccountFromMemory():
