import random

import pyperclip
from selenium.webdriver.common.by import By
from selenium import webdriver
from PyQt5.QtCore import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
from PyQt5.QtCore import QThread


class NaverLoginClass(QThread):
    def __init__(self,driver, Id, Pw):
        super().__init__()
        self.driver = driver
        self.Id = Id
        self.Pw = Pw

    def run(self):
        url = 'https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/'
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