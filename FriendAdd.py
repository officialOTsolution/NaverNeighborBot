from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
from PyQt5.QtCore import *
from PyQt5.QtCore import QThread, pyqtSignal

import random
import time
import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

class FriendAddClass(QThread):
    update_signal = pyqtSignal(str)  # Define a signal to send updates
    finished_signal = pyqtSignal(int) 
    def __init__(self, driver, ids,message ="",groupselect = 0):
        super().__init__()
        self.driver = driver
        self.message = message
        self.ids = ids
        self.UsedIds = []
        if groupselect == 0:
            self.GroupSelect = random.randint(0,25)
            self.flag = False
        else:
            self.flag = True
            self.GroupSelect = groupselect
        
    def run(self):
        cnt = 1
        for id in self.ids:
            if not self.flag:
                self.GroupSelect = random.randint(0,25)

            id = id.replace('\n', '')
            self.UsedIds.append(id)
            url = f'https://m.blog.naver.com/BuddyAddForm.naver?blogId={id}&returnUrl=https%253A%252F%252Fm.blog.naver.com%252F{id}'
            try:
                self.driver.get(url)
                # 서로이웃버튼 클릭
                button = self.driver.find_element(By.CSS_SELECTOR, '#bothBuddyRadio')
                button.click()
                self.driver.implicitly_wait(2)

                button = self.driver.find_element(By.CSS_SELECTOR, '#buddyGroupSelect')
                button.click()
                self.driver.implicitly_wait(0.5)

                for _ in range(self.GroupSelect):
                    webdriver.ActionChains(self.driver).send_keys(Keys.ARROW_DOWN).perform()

                self.driver.implicitly_wait(0.5)
                message = self.driver.find_element(By.CSS_SELECTOR,
                                            '#buddyAddForm > fieldset > div > div.set_detail_t1 > div.set_detail_t1 > div > textarea')
                message.clear()
                name = self.driver.find_element(By.CSS_SELECTOR, '#buddyAddForm > fieldset > div > div.set_txt_t1 > p > strong > em').text
                if "{사용자}" in self.message:
                    self.message = self.message.replace("{사용자}", name)
                message.send_keys(self.message)
                self.message = self.message.replace(name, "{사용자}")
                self.driver.implicitly_wait(0.5)
                button = self.driver.find_element(By.CSS_SELECTOR, 'body > ui-view > div.head.type1 > a.btn_ok')
                button.click()
                self.driver.implicitly_wait(0.5)
                try:
                    text = self.driver.find_element(By.CSS_SELECTOR, '#lyr6 > div > div.txt_area > p').text
                    if text == "선택 그룹의 이웃수가 초과되어 이웃을 추가할 수 없습니다 다른 그룹을 선택해주세요" and self.flag == True:
                        self.finished_signal.emit(3)
                        return 
                    else:
                        continue
                except:
                    pass
                self.update_signal.emit(f"보낸 서이 요청 수: {cnt}개")
                cnt += 1
            except:
                try:
                    try:
                        text = self.driver.find_element(By.CSS_SELECTOR, '#lyr6 > div > div.txt_area > p').text
                        if text == '하루에 신청 가능한 이웃수가 초과되어 더이상 이웃을 추가할 수 없습니다.':
                            print("오늘치 서로이웃 종료합니다.")
                            self.driver.quit()
                            ids = [id for id in self.ids if id not in self.UsedIds]
                            #서이요청 보낸 아이디 중복 제거
                            with open(resource_path('NaverIds.txt'), 'w', encoding='utf-8') as file:
                                for id in ids:
                                    file.write(id)
                            self.finished_signal.emit(1)
                            return 
                    except:
                        continue
                except Exception as e:
                    print("Error",e)  
                    continue
        self.finished_signal.emit(2)