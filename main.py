from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QStackedWidget, QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSignal

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

import time
import sys
import os
from pymongo import MongoClient
import datetime

import webbrowser
from FriendAdd import FriendAddClass
from FriendDelete import FriendDeleteClass
from NaverIDCollectfile import NaverIdCollectClass
from NaverLogin import NaverLoginClass

import LoginUi2
import MainUi
import Setting
import DeleteUi



"""
환경: python 3.9.16 my_proj:conda
"""

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

class Parent(QDialog):
    def __init__(self):
        super().__init__()
        #self.widget =  QStackedWidget()
        
    def show_alert(self, text):
        alert = QMessageBox()
        alert.setWindowTitle("알림")
        alert.setText(text)
        alert.setIcon(QMessageBox.Information)
        alert.setStandardButtons(QMessageBox.Ok)
        alert.exec_()

    def show_setting_window(self):
        settingwindow = FirthdWindow()
        #settingwindow.setWindowTitle("서로이웃 추가 자동화 봇 - 설정창")
        settingwindow.setFixedSize(761,718)
        self.widget.addWidget(settingwindow)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
        self.setCentralWidget(self.widget)

    def show_delete_window(self):
        thirdwindow = ThirdWindow()
        #thirdwindow.setWindowTitle("서로이웃 추가 자동화 봇 - 삭제창")
        thirdwindow.setFixedSize(761,718)
        self.widget.addWidget(thirdwindow)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
        self.setCentralWidget(self.widget)

    def show_main_window(self):
        secondwindow = SecondWindow()
        #secondwindow.setWindowTitle("서로이웃 추가 자동화 봇 - 추가창")
        secondwindow.setFixedSize(761,718)
        self.widget.addWidget(secondwindow)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
        self.setCentralWidget(self.widget)

class MyWindow(QMainWindow,Parent):
    #progress_start = pyqtSignal(int)
    #progress_finish = pyqtSignal()
    def __init__(self):
        super(MyWindow, self).__init__()
        loadUi(resource_path("LoginUi2.ui"),self)
        self.selen = None
        self.widget = QStackedWidget()
        #self.setupUi(self)
        self.StartBtn.clicked.connect(self.resume)
        self.HowToUse.clicked.connect(self.manul_link)
        self.InstaLInk.clicked.connect(self.insta_link)
        try:
            with open(resource_path('user_login.txt'), 'r', encoding='utf-8') as file:
                lines = file.readlines()
                if lines:
                    self.ID.setText(lines[0].strip()) 
                    self.PW.setText(lines[1].strip())
                self.flag = True
        except:
            self.ID.setText("") 
            self.PW.setText("") 
            self.flag = False

    def resume(self):
        LoginInfor = self.Login()
        if LoginInfor == 1:
            self.show_alert('로그인 성공 \n확인 클릭시 제품 페이지로 이동합니다')
            self.hide()
            secondwindow = SecondWindow()
            secondwindow.setFixedSize(761,718)
            self.widget.addWidget(secondwindow)
            self.widget.show()
        else:
            self.show_alert('로그인 실패 \n아이디와 패스워드를 다시 입력해주세요.')
    def Login(self):
        entered_id = self.ID.text()
        entered_pw = self.PW.text()
        
        mongo_client = MongoClient("mongodb+srv://gimjeongheon38:1004@cluster0.8vxj3uo.mongodb.net/?retryWrites=true&w=majority")
        db = mongo_client["Client"]  
        user_collection = db['User_Datas']

        try:
            user_info = user_collection.find_one({"ID": entered_id})
            print(user_info)
            if user_info["password"] == entered_pw:
                if not self.flag:
                    with open(resource_path('user_login.txt'), 'w', encoding='utf-8') as file:
                        file.write(f"{entered_id}\n{entered_pw}\n")
                return 1
            else:
                return 2
        except:
            return 2
    def insta_link(self):
        url = r"https://www.instagram.com/official_otsolution/" 
        webbrowser.open(url)
    def manul_link(self):
        url = r"https://cafe.naver.com/onetouchsolution/2" 
        webbrowser.open(url)

class SecondWindow(QMainWindow,Parent):
    def __init__(self):
        super(SecondWindow, self).__init__()
        loadUi(resource_path("MainUi.ui"),self)
        self.MacroCollect = None
        self.widget = QStackedWidget()
        self.KeyWordList= self.KeyWord.text()
        self.IdCollectBtn.clicked.connect(self.StartCollect)
        self.ButtonDelete.clicked.connect(self.show_delete_window)
        self.ButtonSetting.clicked.connect(self.show_setting_window)
        self.AddFriendBtn.clicked.connect(self.startFriendAdd)
        self.driver = None

    def StartCollect(self):
        self.driver = webdriver.Chrome()
        try:
            print("StartCollect 함수 호출\n")
            print(self.KeyWordList)
            time.sleep(1)
            if self.KeyWord.text() != "":
                self.KeyWordList= self.KeyWord.text()
                self.MacroCollect = NaverIdCollectClass(self.driver, self.KeyWordList,int(self.Count.text()))

                # NaverIdCollectClass의 시그널과 연결
                self.MacroCollect.update_status.connect(self.CollectStatus.append)
                self.MacroCollect.finished_signal.connect(self.handle_finished2)
                self.MacroCollect.update_rest.connect(lambda value: self.Rest.setText(value))

                self.MacroCollect.start()
                print(self.MacroCollect.Count, self.MacroCollect.Keyward)
                print("MacroCollect.start() 함수 종료\n")
            else:
                self.show_alert("키워드를 입력해주세요.")
                self.driver.quit()
        except Exception as e:
            print("SecondWindow->StartCollect 함수 에러: "+str(e))
            self.show_alert("개수를 입력해주세요.")
    def handle_finished2(self, result):
        self.driver.quit()

    def startFriendAdd(self):
        self.driver = webdriver.Chrome()
        try:
            with open(resource_path('user_data.txt'), 'r', encoding='utf-8') as file:
                lines = file.readlines()
                if lines:
                    self.NaverId = lines[0].strip()
                    if len(lines) > 1:
                        self.NaverPw = lines[1].strip()
            try:
                with open(resource_path('user_message.txt'), 'r', encoding='utf-8') as file:
                        self.AutoMessage = file.read().strip()
                
                NaverLogin = NaverLoginClass(self.driver,self.NaverId, self.NaverPw)
                NaverLoginReturn = NaverLogin.run()
                if NaverLoginReturn == 1:
                    try:
                        with open(resource_path(r'NaverIds.txt'), 'r', encoding='utf-8') as file:
                            ids = file.readlines()
                        self.friend_thread = FriendAddClass(self.driver,ids, self.AutoMessage,self.GroupSelect.value())
                        self.friend_thread.update_signal.connect(self.update_gui)
                        self.friend_thread.finished_signal.connect(self.handle_finished)
                        self.friend_thread.start()
                    except:
                        self.driver.quit()
                        self.show_alert("네이버 아이디를 먼저 수집해주세요.")
            except:
                self.driver.quit()
                self.show_alert("서로이웃 신청 메세지를 먼저 설정해주세요.")

        except Exception as e:
            print(f"예외가 발생했습니다: {e}")
            self.driver.quit()
            self.show_alert("네이버 아이디를 먼저 설정해주세요.")
    def update_gui(self, message):
        self.CollectStatus2.append(message)
    def handle_finished(self, result):
        print("handle_finished 호출", result)
        if result == 2:
            with open(resource_path('NaverIds.txt'), 'w', encoding='utf-8') as file:
                file.write('')
            self.driver.quit()
            self.show_alert("서로이웃추가 종료\n더 요청을 보내려면 아이디를 추가로 수집하세요.")
        elif result == 1:
            self.driver.quit()
            self.show_alert("오늘치 서로이웃 종료합니다.")
        elif result == 3:
            self.driver.quit()
            self.show_alert("해당 그룹에는 더이상 이웃을 추가할 수 없습니다.")

#삭제창
class ThirdWindow(QMainWindow,Parent):
    def __init__(self):
        super(ThirdWindow,self).__init__()
        loadUi(resource_path("DeleteUi.ui"), self)
        self.widget =  QStackedWidget()
        self.ButtonAdd.clicked.connect(self.show_main_window)
        self.ButtonSetting.clicked.connect(self.show_setting_window)
        self.Delete.clicked.connect(self.Neighbor_delete)
        self.driver = None

    def Neighbor_delete(self):
        self.driver = webdriver.Chrome()
        try:
            with open(resource_path('user_data.txt'), 'r') as file:
                lines = file.readlines()
                if lines:
                    self.NaverId = lines[0].strip()
                    if len(lines) > 1:
                        self.NaverPw = lines[1].strip()
            print(self.NaverId, self.NaverPw)
            frienddelete = FriendDeleteClass(self.driver, self.NaverId, self.NaverPw)
            frienddelete.finished_signal.connect(self.handle_finished)
            frienddelete.run()

        except:
            self.show_alert("네이버 아이디 정보가 없습니다.")
            self.driver.quit()
    def handle_finished(self, result):
        print("handle_finished 호출", result)
        if result == 1:
            self.show_alert("삭제 완료")
            self.driver.quit()    
    
#설정창
class FirthdWindow(QMainWindow,Parent):
    def __init__(self):
        super(FirthdWindow,self).__init__()
        loadUi(resource_path("Setting.ui"), self)
        self.widget =  QStackedWidget()
        self.ButtonAdd.clicked.connect(self.show_main_window)
        self.ButtonDelete.clicked.connect(self.show_delete_window)
        self.LoginTest.clicked.connect(self.NaverLogTesting)
        self.SaveMessage.clicked.connect(self.save_message)
        self.driver = None
        try:
            with open(resource_path('user_data.txt'), 'r') as file:
                lines = file.readlines()
                if lines:
                    self.Id.setText(lines[0].strip())
                    self.Pw.setText(lines[1].strip()) 
        except:
            pass
        
        try:
            with open(resource_path('user_message.txt'), 'r', encoding='utf-8') as file:
                    self.Message.setText(file.read().strip())
        except:
            pass
        mongo_client = MongoClient("mongodb+srv://gimjeongheon38:1004@cluster0.8vxj3uo.mongodb.net/?retryWrites=true&w=majority")
        db = mongo_client["Client"]  
        user_collection = db['User_Datas']
        with open(resource_path('user_login.txt'), 'r', encoding='utf-8') as file:
                lines = file.readlines()
                if lines:
                    ID = lines[0].strip()
        found_item  = user_collection.find_one({"ID": ID})
        found_time  = found_item.get('time',None)
        current_time = datetime.datetime.now() 
        time_difference = found_time - current_time
        print(time_difference.days)
        self.Time.setText(f"{str(time_difference.days)}일")
    def NaverLogTesting(self):
        self.driver = webdriver.Chrome()
        if self.Id.text() != "" and self.Pw.text() != "":
            NaverLogin = NaverLoginClass(self.driver,self.Id.text(), self.Pw.text())
            NaverLoginReturn = NaverLogin.run()
            if NaverLoginReturn == 1:
                with open(resource_path('user_data.txt'), 'w', encoding='utf-8') as file:
                    file.write(f"{self.Id.text()}\n{self.Pw.text()}\n")
                    self.show_alert("네이버 로그인 성공")
                self.driver.quit()
            else:
                self.show_alert("네이버 로그인 실패")
        else:
            self.driver.quit()
            self.show_alert("네이버 아이디를 먼저 입력해주세요.")
    def save_message(self):
        with open(resource_path('user_message.txt'), 'w', encoding='utf-8') as file: 
            file.write(self.Message.text())
        self.show_alert("저장 완료")

 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()

    myWindow.setFixedHeight(486)
    myWindow.setFixedWidth(410)
    myWindow.show()
    sys.exit(app.exec_())

# python -m PyQt5.uic.pyuic -x LoginUi.ui -o Ui.py
# python -m PyInstaller --onefile --noconsole main.py
# python -m PyInstaller --icon=logo/KakaoTalk_20231229_172139171.png --onefile main.py
# python -m pyinstaller --onefile --add-data "path/to/other_script.py;." main_script.py
"""
pyinstaller --add-data "LoginUi2.ui;." --add-data "MainUi.ui;." --add-data "DeleteUi.ui;." --add-data "Setting.ui;." --add-data "SpoqaHanSansNeo_all/SpoqaHanSansNeo_OTF_original/*.otf;SpoqaHanSansNeo_OTF_original" --add-data "logo/*png;logo" --icon=logo/Last.png main.py
"""