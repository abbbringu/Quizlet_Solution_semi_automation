import datetime
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

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