from selenium import webdriver as web
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait as WDW
from urllib.error import HTTPError
import time


class webDriver():
    def __init__(self):
        self.driver = None
    
    def startDriver(self):
        self.driver = web.Safari()
        #self.driver = web.Firefox(executable_path='/usr/local/bin/geckodriver')
        self.driver.maximize_window()
    
    def openBrowser(self):
        self.driver.get("https://www.instagram.com/")
        try:
            WDW(self.driver, timeout=10).until(EC.url_to_be("https://www.instagram.com/"))
        except HTTPError as err:
            print(err,"Page Not Found")
        time.sleep(2)
    def login(self):
        self.driver.find_element(By.NAME,"username").send_keys("username")
        self.driver.find_element(By.NAME,"password").send_keys("password")
        try:
            WDW(self.driver, timeout=10).until(EC.element_to_be_clickable((By.TAG_NAME, "button")))
            self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        except HTTPError as e:
            print("Error: Selenium can't activate element",e)   
       
    def directMessage(self):
        try:
            WDW(self.driver, timeout=10).until(EC.element_to_be_clickable((By.XPATH,'//span[contains(@class, "x1lliihq") and contains(text(), "Messages")]')))
        except Exception as e:
            print("Error: can't find element",e)
        directM = self.driver.find_element(By.XPATH,'//span[contains(@class, "x1lliihq") and contains(text(), "Messages")]')
        directM.click()
        try:
            WDW(self.driver, timeout=10).until(EC.element_to_be_clickable((By.XPATH,'//div[contains(@class, "x1i10hfl") and contains(text(), "Send message")]')))
        except Exception as e:
            print("Error: can't find element",e)
        sendM = self.driver.find_element(By.XPATH,'//div[contains(@class, "x1i10hfl") and contains(text(), "Send message")]')
        sendM.click()
        try:
            WDW(self.driver, timeout=10).until(EC.element_to_be_clickable((By.XPATH,'//input[contains(@class, "x1j8ye7u") and @placeholder="Search..."]')))
        except Exception as e:
            print("Error: can't find element",e)
        sendToSearch = self.driver.find_element(By.XPATH,'//input[contains(@class, "x1j8ye7u") and @placeholder="Search..."]')
        sendToSearch.click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,'//input[contains(@class, "x1j8ye7u") and @placeholder="Search..."]').send_keys("@realdonaldtrump")
        try:
            WDW(self.driver, timeout=10).until(EC.element_to_be_clickable((By.XPATH,'//div[contains(@class, "x9f619") and contains(@class, "xjbqb8w") and contains(@class, "x78zum5") and contains(@class, "x168nmei") and contains(@class, "x13lgxp2") and contains(@class, "x5pf9jr") and contains(@class, "xo71vjh") and contains(@class, "x1uhb9sk") and contains(@class, "x1plvlek") and contains(@class, "xryxfnj") and contains(@class, "x1iyjqo2") and contains(@class, "x2lwn1j") and contains(@class, "xeuugli") and contains(@class, "xdt5ytf") and contains(@class, "xqjyukv") and contains(@class, "x1cy8zhl") and contains(@class, "x1oa3qoh") and contains(@class, "x1nhvcw1")]')))
        except Exception as e:
            print("Error: can't find element",e)
        self.driver.find_element(By.XPATH,'//div[contains(@class, "x9f619") and contains(@class, "xjbqb8w") and contains(@class, "x78zum5") and contains(@class, "x168nmei") and contains(@class, "x13lgxp2") and contains(@class, "x5pf9jr") and contains(@class, "xo71vjh") and contains(@class, "x1uhb9sk") and contains(@class, "x1plvlek") and contains(@class, "xryxfnj") and contains(@class, "x1iyjqo2") and contains(@class, "x2lwn1j") and contains(@class, "xeuugli") and contains(@class, "xdt5ytf") and contains(@class, "xqjyukv") and contains(@class, "x1cy8zhl") and contains(@class, "x1oa3qoh") and contains(@class, "x1nhvcw1")]').click()
        try:
            WDW(self.driver, timeout=10).until(EC.element_to_be_clickable((By.XPATH,'//div[contains(@class, "x9f619") and contains(@class, "xjbqb8w") and contains(@class, "x78zum5") and contains(@class, "x168nmei") and contains(@class, "x13lgxp2") and contains(@class, "x5pf9jr") and contains(@class, "xo71vjh") and contains(@class, "x1uhb9sk") and contains(@class, "x1plvlek") and contains(@class, "xryxfnj") and contains(@class, "x1iyjqo2") and contains(@class, "x2lwn1j") and contains(@class, "xeuugli") and contains(@class, "xdt5ytf") and contains(@class, "xqjyukv") and contains(@class, "x1cy8zhl") and contains(@class, "x1oa3qoh") and contains(@class, "x1nhvcw1")]')))
        except Exception as e:
            print("Error: can't find element",e)
        self.driver.find_element(By.XPATH,'//div[contains(@class, "x1i10hfl") and contains(text(), "Chat")]').click()
        time.sleep(2)   

    def loop(self):
        writeText = "You're Trash"
        textLooper = 10
        for i in range(textLooper):
            text_field = self.driver.find_element(By.XPATH, "//div[@class='x1n2onr6']")
            text_field.send_keys(writeText)
            time.sleep(0.50)
            text_field.send_keys(Keys.RETURN)
    
    def closeBrowser(self):
        self.driver.quit()
                            
func = webDriver()
func.startDriver()
func.openBrowser()
func.login()
func.directMessage()
func.loop()
func.closeBrowser()


                
        
                
        
