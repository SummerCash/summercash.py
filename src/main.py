provider = ""  # Init provider buffer


def SourceAPI(provider_url: str):
    """
    Set API provider

    :param provider_url:
    :return: Nothing (set method)
    """
    global provider  # Get provider
    
    provider = provider_url  # Set API provider


def GetProvider():
    """
    Get provider reference.

    :return: Provider
    """
    global provider  # Get provider

    return provider


if __name__ == "__main__":
    SourceAPI("https://localhost:8080")  # Source API
