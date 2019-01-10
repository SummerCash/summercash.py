import accounts
import chain
import chainconfig
import common
import coordinationchain
import crypto
import transaction

global provider # Init provider buffer

class Server:
    def __init__(self, ip):
        self.ip = ip

# SourceAPI - set API provider
def SourceAPI(provider: str):
    provider = Server(provider) # Set API provider

if __name__ == "__main__":
    server = Server("https://localhost:8080")
    
    myAccounts = accounts.Accounts(server)
    r = myAccounts.CallMethod("NewAccount", "", "")
    print(r)

    myAccounts = accounts.Accounts(server)
    r = myAccounts.CallMethod("GetAllAccounts", "", "")
    print(r)
