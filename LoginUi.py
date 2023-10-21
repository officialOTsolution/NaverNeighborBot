# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(457, 543)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setBold(False)
        font.setWeight(50)
        Dialog.setFont(font)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("background-color: rgb(255,255,255);\n"
"border-radius: 100px;")
        Dialog.setLocale(QtCore.QLocale(QtCore.QLocale.Korean, QtCore.QLocale.SouthKorea))
        self.StartBtn = QtWidgets.QPushButton(Dialog)
        self.StartBtn.setGeometry(QtCore.QRect(80, 340, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.StartBtn.setFont(font)
        self.StartBtn.setStyleSheet("background-color: #ff0000;border: 2px solid red;")
        self.StartBtn.setObjectName("StartBtn")
        self.ID = QtWidgets.QLineEdit(Dialog)
        self.ID.setGeometry(QtCore.QRect(220, 230, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.ID.setFont(font)
        self.ID.setStyleSheet("border: 1px solid black;")
        self.ID.setObjectName("ID")
        self.PW = QtWidgets.QLineEdit(Dialog)
        self.PW.setGeometry(QtCore.QRect(220, 280, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.PW.setFont(font)
        self.PW.setStyleSheet("border: 1px solid black;")
        self.PW.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PW.setObjectName("PW")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(80, 230, 111, 29))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(80, 280, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, -20, 171, 111))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(90, 90, 291, 71))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(20)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.HowToUse = QtWidgets.QPushButton(Dialog)
        self.HowToUse.setGeometry(QtCore.QRect(240, 400, 151, 41))
        self.HowToUse.setStyleSheet("background-color: #a0a0a0;")
        self.HowToUse.setObjectName("HowToUse")
        self.InstaLInk = QtWidgets.QPushButton(Dialog)
        self.InstaLInk.setGeometry(QtCore.QRect(80, 400, 141, 41))
        self.InstaLInk.setStyleSheet("background-color: #a0a0a0;")
        self.InstaLInk.setObjectName("InstaLInk")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "서이추 봇"))
        self.StartBtn.setText(_translate("Dialog", "로그인"))
        self.label_6.setText(_translate("Dialog", "아이디:"))
        self.label_7.setText(_translate("Dialog", "비밀번호"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/logo/one_touch_solutions_logo2.png\"/></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">서로 이웃 요청 자동화 봇</span></p></body></html>"))
        self.HowToUse.setText(_translate("Dialog", "사용 방법"))
        self.InstaLInk.setText(_translate("Dialog", "개발자 인스타"))
import logo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
