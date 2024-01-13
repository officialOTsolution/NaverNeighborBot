from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *

from PyQt5.QtCore import *
from PyQt5.QtCore import QThread, pyqtSignal

import pyperclip
import time
import random

from webdriver_manager.chrome import ChromeDriverManager

class FriendDeleteClass(QThread):
    finished_signal = pyqtSignal(int) 
    def __init__(self, driver,id, pw):
        super().__init__()
        self.driver = driver
        self.Id = id
        self.Pw = pw

    def run(self):
        login_url = 'https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/'
        self.driver.get(login_url)
        pyperclip.copy(self.Id)
        self.driver.find_element(By.ID, 'id').send_keys(Keys.CONTROL, 'V')
        pyperclip.copy(self.Pw)
        print(self.Pw, self.Id)
        self.driver.find_element(By.ID, 'pw').send_keys(Keys.CONTROL, 'V') 
        self.driver.find_element(By.XPATH, '//*[@id="log.login"]/span').click()
        time.sleep(1)

        #유저 블로그 아이디 가져오기
        blog_url = 'https://section.blog.naver.com/BlogHome.naver?directoryNo=0&currentPage=1&groupId=0'
        self.driver.get(blog_url)
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.CSS_SELECTOR,'#container > div > aside > div > div:nth-child(1) > nav > a:nth-child(1)').click()
        self.driver.implicitly_wait(3)
        all_window_handles = self.driver.window_handles
        new_window_handle = all_window_handles[-1]
        self.driver.switch_to.window(new_window_handle)
        blog_id = self.driver.current_url.replace('https://blog.naver.com/','')
        time.sleep(1.5)
        print("블로그 아이디:",blog_id)

        #블로그 관리 페이지로 이동 구현 
        admin_url =f'https://admin.blog.naver.com/BuddyInviteSentManage.naver?blogId={blog_id}'
        self.driver.get(admin_url)
        self.driver.implicitly_wait(3)
        time.sleep(1.3)

        #서로이웃 신청 취소 구현 
        while(True):
            self.driver.find_element(By.CSS_SELECTOR,'#invite > table > thead > tr > th.checkwrap > input').click()
            self.driver.implicitly_wait(3)
            delete_button = self.driver.find_element(By.CSS_SELECTOR,'#invite > div.action2.neighborlist > div > span > button')
            delete_button.click()
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            if alert_text == '신청취소할 사람을 먼저 선택해주세요.':
                print("모든 요청 삭제 완료.")
                self.finished_signal.emit(1)
            print("Alert 내용:", alert_text)
            alert.accept()
            self.driver.implicitly_wait(3)
            alert.accept()
            self.driver.implicitly_wait(3)
            time.sleep(3)