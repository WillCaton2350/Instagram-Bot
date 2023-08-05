from selenium import webdriver as web
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from urllib.error import HTTPError
from selenium.common.exceptions import NoSuchElementException
from Dataset.dataset import symbolsArray,alphaNumericArray
import random

class WebDriver:
    def __init__(self):
        self.driver = None
    
    def startDriver(self):
        self.driver = web.Firefox(executable_path='/usr/local/bin/geckodriver')
        self.driver.maximize_window()
    
    def openBrowser(self):
        self.driver.get("https://www.instagram.com/")
        try:
            WDW(self.driver, timeout=10).until(EC.url_to_be("https://www.instagram.com/"))
        except HTTPError as err:
            print(err,"Page Not Found")
        self.driver.implicitly_wait(3)
    def login(self):
        try:
            WDW(self.driver, timeout=10).until(EC.presence_of_element_located((By.NAME,"username")))
        except NoSuchElementException as err:
            print(err,"Element Not Found")
        self.driver.implicitly_wait(3)
        user = self.driver.find_element(By.NAME,"username")
        user.send_keys("UsernameID")
    def passwordField(self):                            
        password = ''.join([random.choice(symbolsArray) for _ in range(3)]) + str(random.choice(alphaNumericArray)) + str(random.randint(10, 500))
        self.driver.find_element(By.NAME,"password").send_keys(password)
        try:
            WDW(self.driver, timeout=10).until(EC.element_to_be_clickable((By.TAG_NAME, "button")))
            self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        except HTTPError as e:
            print("Error: Selenium can't activate element",e) 
    def closeBrowser(self):
        self.driver.quit()
