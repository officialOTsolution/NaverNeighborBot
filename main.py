import time
import math
import sys
from PyQt5.QtWidgets import *

from selenium import webdriver
from PyQt5 import uic
from NaverIDCollectfile import NaverIdCollectClass
from PyQt5.QtCore import *
from FriendAdd import FriendAddClass
import MainUi
import LoginUi
app = QApplication(sys.argv)

form_class = uic.loadUiType("LoginUi.ui")[0]
form_class_1 = uic.loadUiType("MainUi.ui")[0]

class MyWindow(QMainWindow, LoginUi.Ui_Dialog):
    progress_start = pyqtSignal(int)
    progress_finish = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.selen = None
        self.setupUi(self)
        self.StartBtn.clicked.connect(self.resume)

    def resume(self):
        LoginInfor = self.Login()
        if LoginInfor == 1:
            self.show_alert('로그인 성공 \n확인 클릭시 제품 페이지로 이동합니다')
            self.hide()
            self.selen = SecondWindow()
            self.selen.show()
        else:
            self.LoginResult.setText('아이디 혹은 비밀번호가 잘못되었습니다.')

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

class SecondWindow(QMainWindow, form_class_1):
    def __init__(self):
        super().__init__()
        self.driver = webdriver.Chrome()
        self.MacroCollect = None
        self.setupUi(self)
        self.KeyWordList= self.KeyWord.text()
        self.IdCollectBtn.clicked.connect(self.StartCollect)
        self.AddFriendBtn.clicked.connect(self.FriendAddFun)
    def StartCollect(self):
        try:
            print(self.KeyWordList, self)
            time.sleep(1)
            self.KeyWordList= self.KeyWord.text()
            if ',' in self.KeyWordList:
                self.KeyWordList = self.KeyWordList.split(',')
            else:
                self.KeyWordList = [self.KeyWordList]
            print('123123')
            self.MacroCollect = NaverIdCollectClass(self.driver, self.KeyWordList, int(self.Count.text()), self.CollectStatus, self.Rest)
            self.MacroCollect.start()

            print('1231233')
            print(self.MacroCollect.Count, self.MacroCollect.Keyward)
            time.sleep(2)

            print("hererere")
        except Exception as e:
            print(e)

    def FriendAddFun(self):
        FriendMacro = FriendAddClass(self.driver, self.MacroCollect.IdList, self.Id.text(), self.Pw.text(), self.CollectStatus2)
        FriendMacro.run()
if __name__ == "__main__":
    myWindow = MyWindow()
    myWindow.show()
    sys.exit(app.exec_())

# python -m PyQt5.uic.pyuic -x LoginUi.ui -o Ui.py
# python -m PyInstaller --onefile --noconsole main.py