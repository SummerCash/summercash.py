import accounts
import chain
import chainconfig
import common
import coordinationchain
import crypto
import transaction

# SourceAPI - set API provider
def SourceAPI(provider_url: str):
    global provider # Init provider buffer
    
    provider = provider_url # Set API provider

if __name__ == "__main__":
    SourceAPI("https://localhost:8080") # Source API
    
    myAccounts = accounts.Accounts(provider)
    r = myAccounts.CallMethod("NewAccount", "", "")
    print(r)

    myAccounts = accounts.Accounts(provider)
    r = myAccounts.CallMethod("GetAllAccounts", "", "")
    print(r)
