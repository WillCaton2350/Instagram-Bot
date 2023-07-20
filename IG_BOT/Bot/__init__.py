from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.common.exceptions import NoSuchElementException 
from hashtags.tags import hashtagList, commentList
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver as web
from urllib.error import HTTPError 
import time
import random
cookie_path = '/Users/Mac/Desktop/Python Projects/Selenium/InstaBotAuto/cookies/ua.json'
mainURL = "https://www.instagram.com/"
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
                print(err,"Error: Page Not Found")
            else:
                pass
        finally:
            time.sleep(3)
        self.driver.find_element(
            By.XPATH, 
            "//*[@id='loginForm']/div/div[1]/div/label/input"
            ).send_keys("username")
        self.driver.find_element(
            By.XPATH, 
            '//*[@id="loginForm"]/div/div[2]/div/label/input'
            ).send_keys("password")
        time.sleep(3)
        self.driver.find_element(
            By.XPATH, 
            '//*[@id="loginForm"]/div/div[3]'
            ).send_keys(Keys.ENTER)
        try:
            WDW(self.driver, timeout=10).until(
            EC.url_to_be(
            mainURL))
        except HTTPError as err:
            if err.code == 404:
                print("Error: Page Not Found", err)
            else:
                pass
        time.sleep(5)
    def popup(self):
        time.sleep(2)
        self.driver.back()
        self.driver.implicitly_wait(2)
    def search(self):
        try:
        # find search icon
            WDW(self.driver, timeout=10).until(EC.element_to_be_clickable((By.XPATH,
            '//span[contains(@class, "x1lliihq") and contains(text(), "Search")]')))
        except Exception as e:
            print(e,"Error: can't find element")
        # click on search icon
        searchBar = self.driver.find_element(By.XPATH,
        '//span[contains(@class, "x1lliihq") and contains(text(), "Search")]')
        searchBar.click()
        time.sleep(3)
        try:
            WDW(self.driver, timeout=10).until(EC.element_to_be_clickable((By.XPATH,
              '//input[contains(@class, "x1lugfcp") and @placeholder="Search"]')))
        except Exception as e:
            print(e,"Error: can't find element")
        # define search inputfield 
        sendSearch = self.driver.find_element(By.XPATH, 
        '//input[contains(@class, "x1lugfcp") and @placeholder="Search"]')
        time.sleep(2)
        # fill search input with random hashtag
        for i in range(1):
            try:
                selectedTag = random.choice(hashtagList)
                sendSearch.send_keys(selectedTag)
            except HTTPError as e:
                if e.code == 404:
                    print("Error: Page Not Found")
                else:
                    pass
            break   
        time.sleep(3)
        # find first # in dropdown
        try:
            WDW(self.driver, timeout=10).until(EC.element_to_be_clickable((By.XPATH,'//div[contains(@class, "x9f619") and contains(@class, "xjbqb8w") and contains(@class, "x78zum5") and contains(@class, "x168nmei") and contains(@class, "x13lgxp2") and contains(@class, "x5pf9jr") and contains(@class, "xo71vjh") and contains(@class, "x1uhb9sk") and contains(@class, "x1plvlek") and contains(@class, "xryxfnj") and contains(@class, "x1iyjqo2") and contains(@class, "x2lwn1j") and contains(@class, "xeuugli") and contains(@class, "xdt5ytf") and contains(@class, "xqjyukv") and contains(@class, "x1cy8zhl") and contains(@class, "x1oa3qoh") and contains(@class, "x1nhvcw1")]')))
        except Exception as e:
            print(e,"Error: can't find element")
        #click on first hashtag in dropdown
        try:
            self.driver.find_element(By.XPATH,'//div[contains(@class, "x9f619") and contains(@class, "xjbqb8w") and contains(@class, "x78zum5") and contains(@class, "x168nmei") and contains(@class, "x13lgxp2") and contains(@class, "x5pf9jr") and contains(@class, "xo71vjh") and contains(@class, "x1uhb9sk") and contains(@class, "x1plvlek") and contains(@class, "xryxfnj") and contains(@class, "x1iyjqo2") and contains(@class, "x2lwn1j") and contains(@class, "xeuugli") and contains(@class, "xdt5ytf") and contains(@class, "xqjyukv") and contains(@class, "x1cy8zhl") and contains(@class, "x1oa3qoh") and contains(@class, "x1nhvcw1")]').click()
        except ElementClickInterceptedException as err:
            print("Error: ",err)
        time.sleep(3)
        # click on first picture / expand picture
    def select(self):
        n = 1
        max_value = 1 
        for i in range(max_value):
            locator = '//div[contains(@class, "_aagu")]'
            WDW(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, locator)))
            time.sleep(3)
            self.driver.implicitly_wait(1)
            self.driver.find_element(By.XPATH, locator).click()
            n += 1
            break
        time.sleep(3)
    def follow_Comment(self):
        # follow
        try:
            WDW(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "_aacl") and contains(text(), "Follow")]')))
            self.driver.implicitly_wait(2)
            self.driver.find_element(By.XPATH, '//div[contains(@class, "_aacl") and contains(text(), "Follow")]').click()
            time.sleep(2)
        except NoSuchElementException as e:
            print(e,"Error: Element already clicked")
            pass
        time.sleep(2)
        self.driver.implicitly_wait(1)
        # comment
        for i in range(1):
            try:
                commentSection = self.driver.find_element(By.XPATH, '//textarea[contains(@class, "x1i0vuye") and @placeholder="Add a comment…"]')
                selectedCom = random.choice(commentList)
                commentSection.send_keys(selectedCom)
            except NoSuchElementException as e:
                print(e,"Error: Element already clicked")
                pass
            time.sleep(2)
        # post comment
        try:
            self.driver.find_element(By.XPATH, '//div[contains(@class, "x1i10hfl") and contains(@class, "xjqpnuy") and contains(@class, "xa49m3k") and contains(@class, "xqeqjp1") and contains(@class, "x2hbi6w") and contains(@class, "xdl72j9") and contains(@class, "x2lah0s") and contains(@class, "xe8uvvx") and contains(@class, "xdj266r") and contains(@class, "x11i5rnm") and contains(@class, "xat24cr") and contains(@class, "x1mh8g0r") and contains(@class, "x2lwn1j") and contains(@class, "xeuugli") and contains(@class, "x1hl2dhg") and contains(@class, "xggy1nq") and contains(@class, "x1ja2u2z") and contains(@class, "x1t137rt") and contains(@class, "x1q0g3np") and contains(@class, "x1lku1pv") and contains(@class, "x1a2a7pz") and contains(@class, "x6s0dn4") and contains(@class, "xjyslct") and contains(@class, "x1ejq31n") and contains(@class, "xd10rxx") and contains(@class, "x1sy0etr") and contains(@class, "x17r0tee") and contains(@class, "x9f619") and contains(@class, "x1ypdohk") and contains(@class, "x1i0vuye") and contains(@class, "x1f6kntn") and contains(@class, "xwhw2v2") and contains(@class, "xl56j7k") and contains(@class, "x17ydfre") and contains(@class, "x2b8uid") and contains(@class, "xlyipyv") and contains(@class, "x87ps6o") and contains(@class, "x14atkfc") and contains(@class, "x1d5wrs8") and contains(@class, "xjbqb8w") and contains(@class, "xm3z3ea") and contains(@class, "x1x8b98j") and contains(@class, "x131883w") and contains(@class, "x16mih1h") and contains(@class, "x972fbf") and contains(@class, "xcfux6l") and contains(@class, "x1qhh985") and contains(@class, "xm0m39n") and contains(@class, "xt0psk2") and contains(@class, "xt7dq6l") and contains(@class, "xexx8yu") and contains(@class, "x4uap5") and contains(@class, "x18d9i69") and contains(@class, "xkhd6sd") and contains(@class, "x1n2onr6") and contains(@class, "x1n5bzlp") and contains(@class, "x173jzuc") and contains(@class, "x1yc6y37")]').click()
            time.sleep(3)
        except NoSuchElementException as err:
            print(err,"Error: Element already clicked")
        # double back
        self.driver.back()
        time.sleep(1)
        self.driver.back()
        time.sleep(2)
    def closeDriver(self):
        self.driver.quit()
