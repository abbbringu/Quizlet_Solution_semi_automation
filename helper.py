import random
import string
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

def initDriverOption(Headless = False):
    options = Options()
    options.add_argument("--disable-web-security")
    options.add_argument("--disable-site-isolation-trials")
    options.add_argument('--log-level=1')
    options.add_argument("--lang=en")
    #options.add_argument("-profile")
    options.headless = Headless # Run without ui 
    options.add_argument('--disable-gpu')  # Last I checked this was necessary.
    return options

def rs(length):
    """
    Generate a random string of a given length.
    
    Args:
        length (int): The desired length of the string.
    
    Returns:
        A random string of the specified length.
    """
    return ''.join(random.choices(string.ascii_letters, k=length))