from view import pyViewStory,passwordInput, usernameInput,clickLogin, mainURL
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver as web
from urllib.error import HTTPError 
import time

class instagramBot:
    driver = None
    def __init__(self):
        self.driver = web.Safari()
        self.driver.maximize_window()
        time.sleep(3)
    def login(self):
        self.driver.get(mainURL)
        try:
            WDW(
            self.driver, 
            timeout=10
            ).until(
            EC.url_to_be(
            mainURL))
        except HTTPError as err:
            if err.code == 404:
                print(
            "Error: Page Not Found",
                    err
                    )
            else:
                pass
        finally:
            time.sleep(3)
        self.driver.find_element(
            By.XPATH, 
            usernameInput
            ).send_keys(
                "username"
                )
        self.driver.find_element(
            By.XPATH, 
            passwordInput
            ).send_keys(
                "password"
                )
        time.sleep(3)
        self.driver.find_element(
            By.XPATH, 
            clickLogin
            ).send_keys(
            Keys.ENTER)
        try:
            WDW(
            self.driver, 
            timeout=10).until(
            EC.url_to_be(
            mainURL))
        except HTTPError as err:
            if err.code == 404:
                print(
            "Error: Page Not Found", 
                    err
                    )
            else:
                pass
        time.sleep(5)
    def popup(self):
        time.sleep(2)
        self.driver.back()
        self.driver.implicitly_wait(2)
    def viewStory(self):
        time.sleep(2)
        try:
            storyBtn = self.driver.find_element(
                By.XPATH,
                pyViewStory)
            storyBtn.click()
        except NoSuchElementException as err:
            print(
        "Error: Can't locate element",
                err
                )
        time.sleep(30)
        self.driver.back()
        self.driver.refresh()
        time.sleep(3)
    def closeBrowser(self):
        self.driver.quit()