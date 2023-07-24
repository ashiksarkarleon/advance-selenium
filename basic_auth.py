import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

def basic_auth_demo():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")

    time.sleep(3)

basic_auth_demo()