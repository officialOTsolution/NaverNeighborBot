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


class FriendAddClass(QThread):
    def __init__(self, driver, IdList,CollectStatus2, message="글 재밌게 읽었습니다.",):
        super().__init__()
        self.driver = driver
        self.IdList = IdList
        self.CollectStatus2 = CollectStatus2
        self.message = message

    def run(self):
        processed_ids = []
        cnt = 1
        random_number = random.randint(1, 13)
        for id in self.IdList:
            id = id.replace('\n', '')
            url = f'https://m.blog.naver.com/BuddyAddForm.naver?blogId={id}&returnUrl=https%253A%252F%252Fm.blog.naver.com%252F{id}'
            try:
                self.driver.get(url)
                # 서로이웃버튼 클릭
                time.sleep(0.5)
                button = self.driver.find_element(By.CSS_SELECTOR, '#bothBuddyRadio')
                button.click()
                self.driver.implicitly_wait(2)

                button = self.driver.find_element(By.CSS_SELECTOR, '#buddyGroupSelect')
                button.click()
                self.driver.implicitly_wait(0.5)

                for _ in range(random_number):
                    webdriver.ActionChains(self.driver).send_keys(Keys.ARROW_DOWN).perform()

                self.driver.implicitly_wait(0.5)
                message = self.driver.find_element(By.CSS_SELECTOR,
                                              '#buddyAddForm > fieldset > div > div.set_detail_t1 > div.set_detail_t1 > div > textarea')
                message.clear()
                time.sleep(1)
                print("출력할 메세지"+self.message)
                message.send_keys(self.message)
                self.driver.implicitly_wait(0.5)
                button = self.driver.find_element(By.CSS_SELECTOR, 'body > ui-view > div.head.type1 > a.btn_ok')
                button.click()
                self.driver.implicitly_wait(0.5)
                print(f"보낸 서이 요청 수: {cnt}개")
                self.CollectStatus2.append(f"보낸 서이 요청 수: {cnt}개")
                if cnt == 100:
                    print('오늘 자 서로이웃 완료')
                    break
                cnt += 1
            except:
                try:
                    text = self.driver.find_element(By.CSS_SELECTOR, '.txt_area.dsc').text
                    if text == '하루에 신청 가능한 이웃수가 초과되어 더이상 이웃을 추가할 수 없습니다.':
                        print('오늘 자 서로이웃 완료')
                        break
                except:
                    continue

                continue
            processed_ids.append(id)
        ids = [id for id in self.IdList if id not in processed_ids]

    def resume(self):
        self.running = True

    def pause(self):
        self.running = False
