import accounts
import chain
import chainconfig
import common
import coordinationchain
import crypto
import transaction

class Server:
    def __init__(self, ip):
        self.ip = ip
    
if __name__ == "__main__":
    server = Server("https://localhost:8080")
    
    myAccounts = accounts.Accounts(server)
    r = myAccounts.CallMethod("NewAccount", "", "")
    print(r)

    myChain = chain.Chain(server)
    r = myChain.CallMethod("GetBalance", "an account address")
    print(r)

    # myAccounts = accounts.Accounts(server)
    # r = myAccounts.CallMethod("NewAccount", "", "")
    print(r)
