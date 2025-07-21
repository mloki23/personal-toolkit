import pyshorteners

def shorten_url(long_url):
    """
    Shortens a URL using the TinyURL service.
    """
    s = pyshorteners.Shortener()
    return s.tinyurl.short(long_url)