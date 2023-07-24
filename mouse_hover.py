import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains


def mouser_hover():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demo.opencart.com/")

    # Hover Desktop Nav Bar
    try:
        desktop_nav = WebDriverWait(driver, 10, poll_frequency=2).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "li:nth-of-type(1) > .dropdown-toggle.nav-link")))
        all_actions = ActionChains(driver)
        all_actions.move_to_element(desktop_nav).perform()
    except Exception as e:
        print("desktop_nav Exception: ", type(e).__name__)

    # Click Mac (1)
    try:
        mac_1 = WebDriverWait(driver, 10, poll_frequency=2).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".dropdown:nth-of-type(1) li:nth-of-type(2) .nav-link")))
        mac_1.click()
    except Exception as e:
        print("Mac 1 Exception: ", type(e).__name__)

    time.sleep(2)


mouser_hover()
