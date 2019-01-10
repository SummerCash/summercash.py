from server import Server
import accounts
import chain
import chainconfig
import common
import coordinationchain
import crypto
import transaction
# rpc NewAccount(GeneralRequest) returns (GeneralResponse) {} // Create new account
#     rpc AccountFromKey(GeneralRequest) returns (GeneralResponse) {} // Generate account from given private key
#     rpc GetAllAccounts(GeneralRequest) returns (GeneralResponse) {} // Walk keystore directory
#     rpc MakeEncodingSafe(GeneralRequest) returns (GeneralResponse) {} // Hash specified byte array n times
#     rpc RecoverSafeEncoding(GeneralRequest) returns (GeneralResponse) {} // Hash specified byte array n times to string
#     rpc String(GeneralRequest) returns (GeneralResponse) {} // Hash specified byte array using sha3d algorithm
#     rpc Bytes(GeneralRequest) returns (GeneralResponse) {} // Hash specified byte array to string using sha3d algorithm
#     rpc ReadAccountFromMemory(GeneralRequest) returns (GeneralResponse) {} // Read account from persistent memory
def TestAccounts():
    server = Server("https://localhost:8080")
    
    methods = [
        
    ]
    myAccounts = accounts.Accounts(server)
    r = myAccounts.CallMethod("NewAccount", "", "")
    print(r)



TestAccounts()