from States.data import url, usernameField, passwordField, geckoDriverPath,searchBarLocator
from States.data import password,username, loginBtn,notNow, NotNow2, hashtagList
from States.data import searchBarIndicator, locator, firstDDTag, likeBtn
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import ElementNotSelectableException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.common.exceptions import NoSuchElementException
from urllib.error import HTTPError as PageNotFound
from selenium.webdriver.common.by import By
from selenium import webdriver as web
from time import sleep
import random
import os

class webDriver():
    def __init__(self):
        self.driver = None
    
    def startDriver(self):
        firefox_options = web.FirefoxOptions()
        self.driver = web.Firefox(
            options=firefox_options
        )
        os.environ[
            "webdriver.firefox.driver"
            ] =  geckoDriverPath
        self.driver.maximize_window()
    
    def getBrowser(self):
        self.driver.get(url)
        try:
            WDW(
                self.driver, 
                timeout=10).until(
                EC.url_to_be(url))
            sleep(3)
        except PageNotFound as err:
            print(err, "Page Not Found")
    def login(self):
        try:
            WDW(
                self.driver,
                timeout=10).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR,usernameField
            )))
        except NoSuchElementException as e:
            print(e)
        try:
            self.driver.find_element(
                By.CSS_SELECTOR,
                usernameField).send_keys(
                    username
                    )
        except ElementNotSelectableException as err:
            print(
                err,
            "Error: Can't write to input field")
        finally:
            self.driver.find_element(
                By.CSS_SELECTOR,
                passwordField).send_keys(
                    password
                    )
        try:
            self.driver.find_element(
                By.CSS_SELECTOR,
                loginBtn).click()
        except NoSuchElementException as err:
            print(
                err,
            "Error: Can't click element")
        try:
            WDW(
                self.driver,
                timeout=10).until(
                EC.presence_of_element_located((
                    By.XPATH,notNow
                )))
        except ElementNotSelectableException as e:
            print(e)
        try:
            self.driver.find_element(
                By.XPATH,
                notNow).click()
        except NoSuchElementException as e:
            print(e)
        sleep(1)
        try:
            self.driver.find_element(
                By.XPATH,
                NotNow2).click()
        except NoSuchElementException as e:
            print(e)
        sleep(1)
    def search(self):
        try:
        # find search icon
            WDW(
                self.driver, 
                timeout=10).until(
            EC.element_to_be_clickable((
                By.XPATH,
            searchBarLocator)))
        except Exception as e:
            print(e,"Error: can't find element")
        # click on search icon
        searchBar = self.driver.find_element(
            By.XPATH,
        searchBarLocator)
        searchBar.click()
        sleep(3)
        try:
            WDW(
                self.driver, 
                timeout=10).until(
                EC.element_to_be_clickable((
                By.XPATH,
              searchBarIndicator)))
        except Exception as e:
            print(e,"Error: can't find element")
        # define search inputfield 
        sendSearch = self.driver.find_element(
            By.XPATH, 
        searchBarIndicator)
        sleep(2)
        # fill search input with random hashtag
        for i in range(1):
            try:
                selectedTag = random.choice(
                    hashtagList)
                sendSearch.send_keys(
                    selectedTag)
            except PageNotFound as e:
                if e.code == 404:
                    print(
                "Error: Page Not Found")
                else:
                    pass
            break   
        sleep(3)
        # find first hashtag in dropdown
        try:
            WDW(
                self.driver, 
                timeout=10).until(
            EC.element_to_be_clickable((
            By.XPATH,
                firstDDTag
            )))
        except Exception as e:
            print(
                e,
            "Error: can't find element")
        #click on first hashtag in dropdown
        try:
            self.driver.find_element(
                By.XPATH,
                firstDDTag
                ).click()
        except ElementClickInterceptedException as err:
            print(
                "Error: ",
                err)
        sleep(3)
        # click on first picture / expand picture
    def select(self):
        n = 1
        max_value = 1 
        for i in range(max_value):
            WDW(
                self.driver, 
                timeout=10).until(
            EC.presence_of_element_located((
                By.XPATH,
                locator
            )))
            sleep(3)
            self.driver.implicitly_wait(1)
            self.driver.find_element(
                By.XPATH, 
                locator).click()
            n += 1
            break
        sleep(3)
        try:
            WDW(
                self.driver, 
                timeout=10).until(
            EC.element_to_be_clickable((
                By.XPATH,likeBtn
            )))
        except Exception as e:
            print(
                e,
            "Error: can't find element")
        finally:
            self.driver.find_element(
                By.XPATH,
                likeBtn
                ).click()
        sleep(1)
        self.driver.back()
        sleep(1)
        self.driver.back()
    def closeDriver(self):
        self.driver.close()
