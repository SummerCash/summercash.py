provider = ""  # Init provider buffer


def source_api(provider_url: str):
    """
    Set API provider

    :param provider_url:
    :return: Nothing (set method)
    """
    global provider  # Get provider
    
    provider = provider_url  # Set API provider


def get_provider():
    """
    Get provider reference.

    :return: Provider
    """
    global provider  # Get provider

    return provider


if __name__ == "__main__":
    source_api("https://localhost:8080")  # Source API
