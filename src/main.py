import sys, test

provider = "" # Init provider buffer

# SourceAPI - set API provider
def SourceAPI(provider_url: str):
    global provider # Get provider
    
    provider = provider_url # Set API provider

# GetProvider - get provider reference
def GetProvider():
    global provider # Get provider

    return provider # Return provider

if __name__ == "__main__":
    SourceAPI("https://localhost:8080") # Source API

'''
TODO:
    - finish removing classes from everything - DONE
'''