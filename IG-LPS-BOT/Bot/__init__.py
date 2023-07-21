from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium import webdriver as web
from hashtag.tags import hashtagList 
from urllib.error import HTTPError
from Path.text import textPath
import pyautogui as pg 
import keyboard as key
import random
import time
class autoGui:
        def clickDrag(self):
            pg.leftClick(x=1213,y=6) 
            time.sleep(1)
            key.press_and_release('delete')
            time.sleep(1)
            key.write("IG-LPS-BOT")
            time.sleep(1)
            pg.leftClick(x=954, y=466)
            x_y_Coors = {
                1: "x=689, y=230",
                2: "x=793, y=224",
                3: "x=912, y=226",
                4: "x=1021, y=220",
                5: "x=689, y=339",
                6: "x=1136, y=233",
                7: "x=804, y=346",
            }
            time.sleep(2)
            rand_key = random.choice(list(x_y_Coors.keys()))
            coordinates = x_y_Coors[rand_key].strip() 
            try:
                x, y = [int(coord.split('=')[1]) for coord in coordinates.split(',')]
            except ValueError:
                print(f"Invalid format for coordinates: {coordinates}")
            time.sleep(2)
            pg.leftClick(x, y)
            time.sleep(2)
            pg.dragTo(x=460, y=615, button='left', duration=1.5)
            time.sleep(2)
            pg.leftClick(x=506, y=143) # exit btn
            time.sleep(3)
            pg.leftClick(x=847, y=171)
            time.sleep(2)# DOUBLE CLICK
            pg.leftClick(x=847, y=171)
            time.sleep(2)
            pg.leftClick(x=1015, y=170)
            time.sleep(2)
            pg.leftClick(x=740, y=278)
        def xClose(self):
            pg.leftClick(x=1252, y=84)
            time.sleep(5)
mainURL = "https://www.instagram.com/"
class instaBot:
    driver = None
    def __init__(self):
        self.driver = web.Safari()
        self.driver.maximize_window()
        time.sleep(2)
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
            By.XPATH,"//*[@id='loginForm']/div/div[1]/div/label/input").send_keys(
                "jjcollyns@gmail.com"
            )
        self.driver.find_element(
            By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(
                "superman2350"
            )
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
        time.sleep(3)
    def popup(self):
        time.sleep(1)
        self.driver.back()
        self.driver.implicitly_wait(2)
        time.sleep(3)
    def createPost(self):
        locator = '//div[contains(@class, "x9f619") and contains(@class, "xjbqb8w") and contains(@class, "x78zum5") and contains(@class, "x168nmei") and contains(@class, "x13lgxp2") and contains(@class, "x5pf9jr") and contains(@class, "xo71vjh") and contains(@class, "x1n2onr6") and contains(@class, "x1plvlek") and contains(@class, "xryxfnj") and contains(@class, "x1c4vz4f") and contains(@class, "x2lah0s") and contains(@class, "xdt5ytf") and contains(@class, "xqjyukv") and contains(@class, "x1qjc9v5") and contains(@class, "x1oa3qoh") and contains(@class, "x1nhvcw1")]'
        try:
            WDW(self.driver, timeout=10).until(
                EC.presence_of_element_located((
                    By.XPATH,locator
                    ))
                )
        except HTTPError as err:
            if err.code == 404:
                print(err, 
            "Error: Page Not Found")
            else:
                pass
        time.sleep(2)
        #click on post icon
        self.driver.find_element(By.XPATH,
        '//span[contains(@class, "x1lliihq") and contains(text(), "Create")]').click()
        time.sleep(2)
    def cadMethod(self):
        autoGui.clickDrag(self)
    def textAreaField(self):
        time.sleep(2)
        for i in range(1):
            textArea = self.driver.find_element(By.XPATH,'//*[@aria-label="Write a caption..."]')
            selectedText = random.choice(textPath)
            break
        textArea.send_keys(selectedText)
        time.sleep(3)
        shareBtn = '//div[contains(@class, "x1i10hfl") and contains(@class, "xjqpnuy") and contains(@class, "xa49m3k") and contains(@class, "xqeqjp1") and contains(@class, "x2hbi6w") and contains(@class, "xdl72j9") and contains(@class, "x2lah0s") and contains(@class, "xe8uvvx") and contains(@class, "xdj266r") and contains(@class, "x11i5rnm") and contains(@class, "xat24cr") and contains(@class, "x1mh8g0r") and contains(@class, "x2lwn1j") and contains(@class, "xeuugli") and contains(@class, "x1hl2dhg") and contains(@class, "xggy1nq") and contains(@class, "x1ja2u2z") and contains(@class, "x1t137rt") and contains(@class, "x1q0g3np") and contains(@class, "x1lku1pv") and contains(@class, "x1a2a7pz") and contains(@class, "x6s0dn4") and contains(@class, "xjyslct") and contains(@class, "x1ejq31n") and contains(@class, "xd10rxx") and contains(@class, "x1sy0etr") and contains(@class, "x17r0tee") and contains(@class, "x9f619") and contains(@class, "x1ypdohk") and contains(@class, "x1i0vuye") and contains(@class, "x1f6kntn") and contains(@class, "xwhw2v2") and contains(@class, "xl56j7k") and contains(@class, "x17ydfre") and contains(@class, "x2b8uid") and contains(@class, "xlyipyv") and contains(@class, "x87ps6o") and contains(@class, "x14atkfc") and contains(@class, "x1d5wrs8") and contains(@class, "xjbqb8w") and contains(@class, "xm3z3ea") and contains(@class, "x1x8b98j") and contains(@class, "x131883w") and contains(@class, "x16mih1h") and contains(@class, "x972fbf") and contains(@class, "xcfux6l") and contains(@class, "x1qhh985") and contains(@class, "xm0m39n") and contains(@class, "xt0psk2") and contains(@class, "xt7dq6l") and contains(@class, "xexx8yu") and contains(@class, "x4uap5") and contains(@class, "x18d9i69") and contains(@class, "xkhd6sd") and contains(@class, "x1n2onr6") and contains(@class, "x1n5bzlp") and contains(@class, "x173jzuc") and contains(@class, "x1yc6y37")]'
        try: 
            WDW(self.driver, timeout=10).until(EC.presence_of_element_located((By.XPATH,shareBtn)))
        except NoSuchElementException as e:
            print(e,"Error")           
        time.sleep(1)
        clickShare = self.driver.find_element(By.XPATH,shareBtn)
        clickShare.click()
        time.sleep(8)
    def search(self):
        try:
        # find search icon
            WDW(self.driver, timeout=10).until(EC.element_to_be_clickable((By.XPATH,
            '//span[contains(@class, "x1lliihq") and contains(text(), "Search")]')))
        except WebDriverException as e:
            print(e,"Error: can't find element")
        # click on search icon
        searchBar = self.driver.find_element(By.XPATH,
        '//span[contains(@class, "x1lliihq") and contains(text(), "Search")]')
        searchBar.click()
        self.driver.implicitly_wait(3)
        time.sleep(3)
        try:
            WDW(self.driver, timeout=10).until(EC.element_to_be_clickable((By.XPATH,
              '//input[contains(@class, "x1lugfcp") and @placeholder="Search"]')))
        except Exception as e:
            print(e,"Error: can't find element")
        # define search inputfield 
        sendSearch = self.driver.find_element(By.XPATH, 
        '//input[contains(@class, "x1lugfcp") and @placeholder="Search"]')
        self.driver.implicitly_wait(2)
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
        self.driver.implicitly_wait(3)
        time.sleep(3)
        # find first hashtag in dropdown
        try:
            WDW(self.driver, timeout=10).until(EC.element_to_be_clickable((By.XPATH,'//div[contains(@class, "x9f619") and contains(@class, "xjbqb8w") and contains(@class, "x78zum5") and contains(@class, "x168nmei") and contains(@class, "x13lgxp2") and contains(@class, "x5pf9jr") and contains(@class, "xo71vjh") and contains(@class, "x1uhb9sk") and contains(@class, "x1plvlek") and contains(@class, "xryxfnj") and contains(@class, "x1iyjqo2") and contains(@class, "x2lwn1j") and contains(@class, "xeuugli") and contains(@class, "xdt5ytf") and contains(@class, "xqjyukv") and contains(@class, "x1cy8zhl") and contains(@class, "x1oa3qoh") and contains(@class, "x1nhvcw1")]')))
        except Exception as e:
            print(e,"Error: can't find element")
        #click on first hashtag in dropdown
        try:
            self.driver.find_element(By.XPATH,'//div[contains(@class, "x9f619") and contains(@class, "xjbqb8w") and contains(@class, "x78zum5") and contains(@class, "x168nmei") and contains(@class, "x13lgxp2") and contains(@class, "x5pf9jr") and contains(@class, "xo71vjh") and contains(@class, "x1uhb9sk") and contains(@class, "x1plvlek") and contains(@class, "xryxfnj") and contains(@class, "x1iyjqo2") and contains(@class, "x2lwn1j") and contains(@class, "xeuugli") and contains(@class, "xdt5ytf") and contains(@class, "xqjyukv") and contains(@class, "x1cy8zhl") and contains(@class, "x1oa3qoh") and contains(@class, "x1nhvcw1")]').click()
        except ElementNotInteractableException as err:
            print("Error: ",err)
        self.driver.implicitly_wait(3)
        time.sleep(3)
        # click on first picture / expand picture
    def select(self):
        n = 1
        max_value = 1 
        for i in range(max_value):
            locator = '//div[contains(@class, "_aagu")]'
            WDW(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, locator)))
            self.driver.implicitly_wait(3)
            time.sleep(3)
            self.driver.find_element(By.XPATH, locator).click()
            n += 1
            break
        self.driver.implicitly_wait(2)
        time.sleep(2)
    def savePost(self):
        WDW(self.driver, timeout=10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@aria-label="Save"]'
                )))
        self.driver.find_element(By.XPATH, '//*[@aria-label="Save"]').click()
        time.sleep(2)
        self.driver.implicitly_wait(2)
        time.sleep(3)
        self.driver.back()
        self.driver.implicitly_wait(2)
        time.sleep(3)
        self.driver.back()
        time.sleep(3)
        self.driver.back()
    def closeBrowser(self):
        self.driver.quit()

            
            
            
            
            
            
        
            
        