import time
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import time
# from Ui import Ui_Dialog
from selenium.webdriver.common.by import By
from selenium import webdriver
from PyQt5.QtCore import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
from PyQt5.QtCore import *
class NaverIdCollectClass(QThread):
    def __init__(self, driver, Keyward, Count, CollectStatus, Rest):
        super().__init__()
        self.driver = driver
        self.Keyward = Keyward
        self.IdList = []
        self.Count = Count
        self.CollectStatus = CollectStatus
        self.Rest = Rest
        time.sleep(2)

    def run(self):
        try:
            print("herlelel")
            time.sleep(3)
            counting = 0
            time.sleep(1)
            for keyward in self.Keyward:
                print(keyward)
                url = f'https://search.naver.com/search.naver?where=blog&query={keyward}&sm=tab_opt&nso=so%3Add%2Cp%3Aall'
                self.driver.get(url)
                # 맨 밑 페이지로 이동.
                for _ in range(10):
                    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(1)

                eles = self.driver.find_elements(By.CSS_SELECTOR, '.sub_txt.sub_name')
                scroll_bar =self.CollectStatus.verticalScrollBar()

                for ele in eles:
                    href = ele.get_attribute('href')
                    href = href.replace('https://blog.naver.com/', '')
                    self.IdList.append(href)
                    counting += 1
                    self.CollectStatus.append(f'현재 수집된 아이디 개수 : {counting}')
                    scroll_bar.setValue(scroll_bar.maximum())
                if len(self.IdList) >= self.Count:
                    break
            # 중복제거
            self.IdList = list(set(self.IdList))
            self.Rest.setText(str(len(self.IdList)))

        except Exception as e:
            print("here", e)

    def resume(self):
        self.running = True

    def pause(self):
        self.running = False

    def NaverIdCollect(self):
        try:
            counting = 0
            time.sleep(1)
            for keyward in self.Keyward:
                print(keyward)
                url = f'https://search.naver.com/search.naver?where=blog&query={keyward}&sm=tab_opt&nso=so%3Add%2Cp%3Aall'
                self.driver.get(url)
                # 맨 밑 페이지로 이동.
                for _ in range(10):
                    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(1)

                eles = self.driver.find_elements(By.CSS_SELECTOR, '.sub_txt.sub_name')
                for ele in eles:
                    href = ele.get_attribute('href')
                    href = href.replace('https://blog.naver.com/', '')
                    self.IdList.append(href)
                    counting += 1
                    self.CollectStatus.append(f'현재 수집된 아이디 개수 : {counting}')
                if len(self.IdList) >= self.Count:
                    break
            # 중복제거
            self.IdList = list(set(self.IdList))
        except Exception as e:
            print('hekrekrh' , e)