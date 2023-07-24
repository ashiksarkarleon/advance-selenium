import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions


def head_less():
    print("Please wait...")
    options = ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    print("Browser is running...")
    driver.get("https://www.google.com")
    try:
        assert "https://www.google.com" in driver.current_url, f"invalid url: %s" % driver.current_url
        print("Page open Successfully: %s" % driver.current_url)
    except Exception as e:
        print("Page open Exception: ", type(e).__name__)


head_less()
