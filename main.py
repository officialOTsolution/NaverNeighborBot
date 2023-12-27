from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QStackedWidget
from PyQt5 import QtWidgets 
from PyQt5.uic import loadUi

import webbrowser
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

import time
import sys
import os

import LoginUi2
import MainUi

from FriendAdd import FriendAddClass
from FriendDelete import FriendDeleteClass
from NaverIDCollectfile import NaverIdCollectClass
from NaverLogin import NaverLoginClass

"""
환경: python 3.9.16 my_proj:conda
"""
app = QApplication(sys.argv)
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

class Parent():
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.widget =  QStackedWidget()
        self.flag = False
    def set_flag_true(self):
        self.flag = True

    def show_alert(self, text):
        alert = QMessageBox()
        alert.setWindowTitle("알림")
        alert.setText(text)
        alert.setIcon(QMessageBox.Information)
        alert.setStandardButtons(QMessageBox.Ok)
        alert.exec_()

    def show_setting_window(self):
        self.driver.quit()
        settingwindow = FirthdWindow()
        #settingwindow.setFixedSize(360,259)
        self.widget.addWidget(settingwindow)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
        self.setCentralWidget(self.widget)

    def show_delete_window(self):
        self.driver.quit()
        thirdwindow = ThirdWindow()
        #thirdwindow.setFixedSize(360,259)
        self.widget.addWidget(thirdwindow)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
        self.setCentralWidget(self.widget)

    def show_main_window(self):
        secondwindow = SecondWindow()
        #secondwindow.setFixedSize(761,718)
        self.widget.addWidget(secondwindow)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
        self.setCentralWidget(self.widget)

class MyWindow(QMainWindow, LoginUi2.Ui_Dialog,Parent):
    progress_start = pyqtSignal(int)
    progress_finish = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.selen = None
        self.widget =  QStackedWidget()
        self.setupUi(self)
        self.StartBtn.clicked.connect(self.resume)
        self.HowToUse.clicked.connect(self.manul_link)
        self.InstaLInk.clicked.connect(self.insta_link)
    def resume(self):
        LoginInfor = self.Login()
        if LoginInfor == 1:
            self.show_alert('로그인 성공 \n확인 클릭시 제품 페이지로 이동합니다')
            self.hide()
            secondwindow = SecondWindow()
            self.widget.addWidget(secondwindow)
            self.widget.setFixedHeight(718)
            self.widget.setFixedWidth(761)
            self.widget.show()

        else:
            self.show_alert('로그인 실패 \n아이디와 패스워드를 다시 입력해주세요.')
    def Login(self):
        if self.ID.text() == 'admin' and self.PW.text() == "1004":
            return 1
        else:
            return 2
    def insta_link(self):
        url = r"https://www.instagram.com/onetouch_sol/" 
        webbrowser.open(url)
    def manul_link(self):
        url = r"https://cafe.naver.com/onetouchsolution" 
        webbrowser.open(url)

class SecondWindow(QMainWindow,QDialog,Parent):
    def __init__(self):
        super(SecondWindow, self).__init__()
        loadUi("MainUi.ui",self)
        self.MacroCollect = None
        self.widget =  QStackedWidget()
        self.KeyWordList= self.KeyWord.text()
        self.IdCollectBtn.clicked.connect(self.StartCollect)
        self.ButtonDelete.clicked.connect(self.show_delete_window)
        self.ButtonSetting.clicked.connect(self.show_setting_window)
        self.AddFriendBtn.clicked.connect(self.startFriendAdd)

    def StartCollect(self):
        try:
            print("StartCollect 함수 호출\n")
            print(self.KeyWordList)
            time.sleep(1)
            if self.KeyWord.text() != "":
                self.KeyWordList= self.KeyWord.text()
                self.KeyWordList = [self.KeyWordList]
                #self.MacroCollect = NaverIdCollectClass(self.driver, self.KeyWordList, self.CollectStatus, self.Rest, int(self.Count.text()))
                self.MacroCollect = NaverIdCollectClass(self.driver, self.KeyWordList,int(self.Count.text()))

                # NaverIdCollectClass의 시그널과 연결
                self.MacroCollect.update_status.connect(self.CollectStatus.append)
                self.MacroCollect.update_rest.connect(lambda value: self.Rest.setText(value))

                self.MacroCollect.start()
                print(self.MacroCollect.Count, self.MacroCollect.Keyward)
                print("MacroCollect.start() 함수 종료\n")
            else:
                self.show_alert("키워드를 입력해주세요.")
        except Exception as e:
            print("SecondWindow->StartCollect 함수 에러: "+str(e))
            self.show_alert("개수를 입력해주세요.")
    def startFriendAdd(self):
        try:
            with open('user_data.txt', 'r', encoding='utf-8') as file:
                lines = file.readlines()
                if lines:
                    self.NaverId = lines[0].strip()
                    if len(lines) > 1:
                        self.NaverPw = lines[1].strip()
            with open('user_message.txt', 'r', encoding='utf-8') as file:
                    self.AutoMessage = file.read().strip()
            
            NaverLogin = NaverLoginClass(self.driver,self.NaverId, self.NaverPw)
            NaverLoginReturn = NaverLogin.run()
            if NaverLoginReturn == 1:
                #print(self.AutoMessage)
                self.friend_thread = FriendAddClass(self.driver, self.MacroCollect.IdList, self.AutoMessage)
                self.friend_thread.update_signal.connect(self.update_gui)
                self.friend_thread.start()
        except Exception as e:
            print(f"예외가 발생했습니다: {e}")
            self.show_alert("네이버 아이디 정보가 없습니다.")
    def update_gui(self, message):
        self.CollectStatus2.append(message)


#삭제창
class ThirdWindow(QMainWindow,Parent):
    def __init__(self):
        super(ThirdWindow,self).__init__()
        loadUi("DeleteUi.ui", self)
        self.ButtonAdd.clicked.connect(self.show_main_window)
        self.ButtonSetting.clicked.connect(self.show_setting_window)
        self.Delete.clicked.connect(self.Neighbor_delete)
        
    def Neighbor_delete(self):
        try:
            with open('user_data.txt', 'r') as file:
                lines = file.readlines()
                if lines:
                    self.NaverId = lines[0].strip()
                    if len(lines) > 1:
                        self.NaverPw = lines[1].strip()
            print(self.NaverId, self.NaverPw)
            frienddelete = FriendDeleteClass(self.driver, self.NaverId, self.NaverPw)
            frienddeleteReturn = frienddelete.run()
            if frienddeleteReturn == 1:
                self.show_alert("삭제 완료")
        except:
            self.show_alert("네이버 아이디 정보가 없습니다.")
        
    
class FirthdWindow(QMainWindow,Parent):
    def __init__(self):
        super(FirthdWindow,self).__init__()
        loadUi("Setting.ui", self)
        self.widget =  QStackedWidget()
        self.ButtonAdd.clicked.connect(self.show_main_window)
        self.ButtonDelete.clicked.connect(self.show_delete_window)
        self.LoginTest.clicked.connect(self.NaverLogTesting)
        self.SaveMessage.clicked.connect(self.save_message)
        
    def NaverLogTesting(self):
        if self.Id.text() != "" and self.Pw.text() != "":
            NaverLogin = NaverLoginClass(self.driver,self.Id.text(), self.Pw.text())
            NaverLoginReturn = NaverLogin.run()
            if NaverLoginReturn == 1:
                with open('user_data.txt', 'w', encoding='utf-8') as file:
                    file.write(f"{self.Id.text()}\n{self.Pw.text()}\n")
                    self.show_alert("네이버 로그인 성공")
            else:
                self.show_alert("네이버 로그인 실패")
        else:
            self.show_alert("네이버 아이디를 먼저 입력해주세요.")
    def save_message(self):
        with open('user_message.txt', 'w', encoding='utf-8') as file: 
            file.write(self.Message.text())
        self.show_alert("저장 완료")

 
if __name__ == "__main__":
    myWindow = MyWindow()
    myWindow.setFixedHeight(486)
    myWindow.setFixedWidth(410)
    myWindow.show()

    sys.exit(app.exec_())

# python -m PyQt5.uic.pyuic -x LoginUi.ui -o Ui.py
# python -m PyInstaller --onefile --noconsole main.py
# python -m PyInstaller --onefile main.py
# python -m pyinstaller --onefile --add-data "path/to/other_script.py;." main_script.py