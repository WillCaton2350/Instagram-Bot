from selenium import webdriver as web
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait as WDW
from urllib.error import HTTPError
import random
import time

commentList = ['This is cool', 'Great Job', 'Solid!', 'Great Work', 'Niceee!!']
class webDriver():
    def __init__(self):
        self.driver = None
    def startDriver(self):
        self.driver = web.Safari()
        self.driver.maximize_window()
    def openBrowser(self):
        self.driver.get("https://www.instagram.com/")
        try:
            WDW(self.driver, timeout=20).until(EC.url_to_be("https://www.instagram.com/"))
        except HTTPError as err:
            print('Error: ',err," - Page Not Found")
        time.sleep(2)
    def login(self):
        self.driver.find_element(By.NAME,"username").send_keys("alexa2savage")
        self.driver.find_element(By.NAME,"password").send_keys("Comm@nd5354")
        try:
            WDW(self.driver, timeout=10).until(EC.element_to_be_clickable((By.TAG_NAME, "button")))
            self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        except HTTPError as e:
            print("Error: Selenium can't activate element",e)   
        WDW(self.driver,timeout=10).until(EC.element_to_be_clickable((By.XPATH,'//span[contains(@class, "x1lliihq") and contains(text(), "Home")]')))
        self.driver.find_element(By.XPATH,'//span[contains(@class, "x1lliihq") and contains(text(), "Home")]').click()
    def findElement(self):
        try:
            for i in range(3):  
                self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
                time.sleep(1)
                target_element_xpath = '//*[@id="mount_0_0_hj"]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/div/textarea'
                try:
                    WDW(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, target_element_xpath)))
                    break 
                except Exception:
                    continue
            self.driver.execute_script("window.scrollBy(0, -500);")
            time.sleep(1)
        except Exception as err:
            print("Error: ", err)
    def commentFunc(self):
        WDW(self.driver,timeout=10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mount_0_0_hj"]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/div/textarea')))    
        comment = self.driver.find_element(By.XPATH,
        '//*[@id="mount_0_0_hj"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/section/div[1]/div[3]/div/div/div[1]/div/article[1]/div/div[3]/div/div/section[1]/span[2]/div/div/svg')
        comment.click()
        writeComment = commentList
        for i in (commentList):
            commentSection = self.driver.find_element(By.XPATH, '//*[@id="mount_0_0_hj"]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/div/textarea')
            commentSection.send_keys(random.choice(str(writeComment)))
            time.sleep(0.50)
            commentSection.send_keys(Keys.RETURN)
            break
    def quitDriver(self):
        self.driver.quit()
if __name__ =="__main__":
    func = webDriver()
    func.startDriver()
    func.openBrowser()
    func.login()
    func.findElement()
    func.commentFunc()
    func.quitDriver()