import time
import math
import sys
from selenium import webdriver
from PyQt5 import uic
from PyQt5.QtWidgets import *
import webbrowser
from webdriver_manager.chrome import ChromeDriverManager
from NaverIDCollectfile import NaverIdCollectClass
from NaverLogin import NaverLoginClass
from PyQt5.QtCore import *
from FriendAdd import FriendAddClass
import MainUi
import LoginUi
"""
환경: python 3.9.16 my_proj:conda
"""
app = QApplication(sys.argv)
import sys
import os
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
form = resource_path("LoginUi.ui")
form1 = resource_path("MainUi.ui")
form_class = uic.loadUiType(form)[0]
form_class_1 = uic.loadUiType(form1)[0]

class MyWindow(QMainWindow, LoginUi.Ui_Dialog):
    progress_start = pyqtSignal(int)
    progress_finish = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.selen = None
        self.setupUi(self)
        self.StartBtn.clicked.connect(self.resume)
        self.HowToUse.clicked.connect(self.manul_link)
        self.InstaLInk.clicked.connect(self.insta_link)
    def resume(self):
        LoginInfor = self.Login()
        if LoginInfor == 1:
            self.show_alert('로그인 성공 \n확인 클릭시 제품 페이지로 이동합니다')
            self.hide()
            self.selen = SecondWindow()
            self.selen.show()
        else:
            self.show_alert('로그인 실패 \n아이디와 패스워드를 다시 입력해주세요.')
    def pause(self):
        self.selen.pause()
    def Login(self):
        if self.ID.text() == 'admin' and self.PW.text() == "1004":
            return 1
        else:
            return 2
    def show_alert(self, text):
        alert = QMessageBox()
        alert.setWindowTitle("알림")
        alert.setText(text)
        alert.setIcon(QMessageBox.Information)
        alert.setStandardButtons(QMessageBox.Ok)
        alert.exec_()
    def insta_link(self):
        url = r"https://www.instagram.com/onetouch_sol/" 
        webbrowser.open(url)
    def manul_link(self):
        url = r"https://cafe.naver.com/onetouchsolution" 
        webbrowser.open(url)

class SecondWindow(QMainWindow, form_class_1):
    def __init__(self):
        super().__init__()
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.MacroCollect = None
        self.setupUi(self)
        self.flag = False
        self.KeyWordList= self.KeyWord.text()
        self.IdCollectBtn.clicked.connect(self.StartCollect)
        self.AddFriendBtn.clicked.connect(self.NaverLog)

    def StartCollect(self):
        try:
            print("SecondWindow->StartCollec 함수 호출\n")
            self.flag = True 
            print(self.KeyWordList, self)
            time.sleep(1)
            if self.KeyWord.text() != "":
                self.KeyWordList= self.KeyWord.text()
                self.KeyWordList = [self.KeyWordList]
                self.MacroCollect = NaverIdCollectClass(self.driver, self.KeyWordList, self.CollectStatus, self.Rest, int(self.Count.text()))
                self.MacroCollect.start()
                print(self.MacroCollect.Count, self.MacroCollect.Keyward)
                time.sleep(1)
                print("SecondWindow->MacroCollect.start() 함수 종료\n")
            else:
                self.show_alert("키워드를 입력해주세요.")
        except Exception as e:
            print("SecondWindow->StartCollect 함수 에러: "+str(e))
            self.show_alert("개수를 입력해주세요.")

    def NaverLog(self):
        if self.flag:
            if self.Id.text() != "" and self.Pw.text() != "":
                NaverLogin = NaverLoginClass(self.driver,self.Id.text(), self.Pw.text())
                NaverLoginReturn = NaverLogin.run()
                if NaverLoginReturn == 1:
                    self.startFriendAdd()
            else:
                self.show_alert("네이버 아이디를 먼저 입력해주세요.")
        else:
            self.show_alert("아이디 수집을 먼저 진행해주세요.")

    def startFriendAdd(self):
        self.friend_thread = FriendAddClass(self.driver, self.MacroCollect.IdList, self.message.text())
        self.friend_thread.update_signal.connect(self.update_gui)
        self.friend_thread.start()

    def update_gui(self, message):
        self.CollectStatus2.append(message)
        
    def show_alert(self, text):
        alert = QMessageBox()
        alert.setWindowTitle("알림")
        alert.setText(text)
        alert.setIcon(QMessageBox.Information)
        alert.setStandardButtons(QMessageBox.Ok)
        alert.exec_()
        
if __name__ == "__main__":
    myWindow = MyWindow()
    myWindow.show()
    sys.exit(app.exec_())

# python -m PyQt5.uic.pyuic -x LoginUi.ui -o Ui.py
# python -m PyInstaller --onefile --noconsole main.py
# python -m PyInstaller --onefile main.py
# python -m pyinstaller --onefile --add-data "path/to/other_script.py;." main_script.py