import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


def multiple_window_tab():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demo.opencart.com/")

    # Open blank tab
    # driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + "t")
    driver.execute_script("window.open()")

    # switch to new tab
    driver.switch_to.window(driver.window_handles[1])
    driver.get("https://demo.opencart.com/")
    time.sleep(2)

    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)


multiple_window_tab()
