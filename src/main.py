import sys, test

# SourceAPI - set API provider
def SourceAPI(provider_url: str):
    global provider # Init provider buffer

    provider = provider_url # Set API provider

if __name__ == "__main__":
    SourceAPI("https://localhost:8080") # Source API
    

'''
TODO:
    - finish removing classes from everything - DONE
'''