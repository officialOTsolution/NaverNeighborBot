from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PyQt5.QtCore import QThread
from PyQt5.QtCore import *

import time
import random
import pyperclip
from datetime import datetime

class NaverLoginClass(QThread):
    def __init__(self,driver, Id="", Pw=""):
        super().__init__()
        self.driver = driver
        self.Id = Id
        self.Pw = Pw
    def run(self):
        url = 'https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/'
        try:
            self.driver.get(url)
            pyperclip.copy(self.Id)
            self.driver.find_element(By.ID, 'id').send_keys(Keys.CONTROL, 'V')
            pyperclip.copy(self.Pw)
            self.driver.find_element(By.ID, 'pw').send_keys(Keys.CONTROL, 'V')
            self.driver.find_element(By.XPATH, '//*[@id="log.login"]/span').click()
            if self.driver.current_url != "https://nid.naver.com/nidlogin.login":
                return 1
            else:
                return 2
        except:
            self.driver = webdriver.Chrome() 
            self.run()