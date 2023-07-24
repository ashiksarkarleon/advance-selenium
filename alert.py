import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


def alerts():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    # normal alert
    driver.find_element(By.CSS_SELECTOR, "li:nth-of-type(1) > button").click()
    time.sleep(1)
    driver.switch_to.alert.accept()
    time.sleep(1)

    # confirm alert
    driver.find_element(By.CSS_SELECTOR, "li:nth-of-type(2) > button").click()
    time.sleep(1)
    driver.switch_to.alert.dismiss()
    time.sleep(1)

    # prompt alert
    driver.find_element(By.CSS_SELECTOR, "li:nth-of-type(3) > button").click()
    time.sleep(1)
    driver.switch_to.alert.send_keys("Hello, world!")
    time.sleep(1)
    driver.switch_to.alert.accept()
    time.sleep(1)
    driver.execute_script('alert("Hello, world!")')     # Execute script
    time.sleep(1)


alerts()
