from PyQt5.QtCore import QThread, QTimer, pyqtSignal
from selenium.webdriver.common.by import By
from selenium import webdriver
import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

class NaverIdCollectClass(QThread):
    # 스레드 간 통신을 위한 시그널 정의
    update_status = pyqtSignal(str)
    update_rest = pyqtSignal(str)
    finished_signal = pyqtSignal(int)
    def __init__(self, driver, Keyward, Count=1):
        super().__init__()
        self.driver = driver
        self.Keyward = Keyward
        self.IdList = []
        self.Count = Count//30
        self.running = False  # 스레드 일시 중지를 위한 플래그

    def run(self):
        try:
            print("NaverIdCollectClass->run 호출")
            
            # if not self.running:  # 일시 중지 중이면 실행하지 않음
            #     return

            counting = 0
            print(self.Keyward)
            url = f'https://search.naver.com/search.naver?where=blog&query={self.Keyward}&sm=tab_opt&nso=so%3Add%2Cp%3Aall'
            self.driver.get(url)

            for _ in range(self.Count):
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                self.sleep(1)  # time.sleep 대신 QThread의 sleep 사용

            eles = self.driver.find_elements(By.CSS_SELECTOR, '.user_info')

            for ele in eles:
                a_tag = ele.find_element(By.CSS_SELECTOR, 'a')
                href = a_tag.get_attribute('href')
                href = href.replace('https://blog.naver.com/', '')
                self.IdList.append(href)
                counting += 1

                # 스레드 간 통신을 통해 GUI 업데이트
                self.update_status.emit(f'현재 수집된 아이디 개수 : {counting}')

            # 중복 제거
            self.IdList = list(set(self.IdList))
            cnt = 0
            with open(resource_path('NaverIds.txt'), 'a', encoding='utf-8') as file:
                for id_item in self.IdList:
                    if not "http" in id_item:
                        cnt += 1
                        file.write(f"{id_item}\n")
            # 스레드 간 통신을 통해 GUI 업데이트
            self.update_rest.emit(str(cnt))

        except Exception as e:
            print("run 함수 에러 발생:" + str(e))
        finally:
            self.finished_signal.emit(1)