from selenium import webdriver as web
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from urllib.error import HTTPError
from Dataset.dataset import symbolsArray,alphaNumericArray
import random
import time


class WebDriver:
    def __init__(self):
        self.driver = None
    
    def startDriver(self):
        self.driver = web.Firefox(executable_path='/usr/local/bin/geckodriver')
        # Find a way to get tor webDriver/Firefox manipulation
        self.driver.maximize_window()
    
    def openBrowser(self):
        self.driver.get("https://www.instagram.com/")
        try:
            WDW(self.driver, timeout=10).until(EC.url_to_be("https://www.instagram.com/"))
        except HTTPError as err:
            print(err,"Page Not Found")
        time.sleep(2)
    def login(self):

        password = ''.join([random.choice(symbolsArray) for _ in range(3)]) + str(random.choice(alphaNumericArray)) + str(random.randint(10, 500))
        self.driver.find_element(By.ID, "usernamereg-password").send_keys(password) 

        self.driver.find_element(By.NAME,"password").send_keys(password)


        try:
            WDW(self.driver, timeout=10).until(EC.element_to_be_clickable((By.TAG_NAME, "button")))
            self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        except HTTPError as e:
            print("Error: Selenium can't activate element",e) 
