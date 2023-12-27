# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginUi2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(410, 486)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
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
        self.StartBtn.setGeometry(QtCore.QRect(50, 280, 311, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StartBtn.sizePolicy().hasHeightForWidth())
        self.StartBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Spoqa Han Sans Neo Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.StartBtn.setFont(font)
        self.StartBtn.setAutoFillBackground(False)
        self.StartBtn.setStyleSheet("background-color: black;\n"
"border-radius: 5px;\n"
"color : white;")
        self.StartBtn.setObjectName("StartBtn")
        self.ID = QtWidgets.QLineEdit(Dialog)
        self.ID.setGeometry(QtCore.QRect(50, 100, 311, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ID.sizePolicy().hasHeightForWidth())
        self.ID.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Spoqa Han Sans Neo")
        font.setPointSize(12)
        self.ID.setFont(font)
        self.ID.setStyleSheet("border: 1px solid #C7C7C7;\n"
"border-radius: 5px;\n"
"padding : 0px 5px;")
        self.ID.setText("")
        self.ID.setObjectName("ID")
        self.PW = QtWidgets.QLineEdit(Dialog)
        self.PW.setGeometry(QtCore.QRect(50, 200, 311, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PW.sizePolicy().hasHeightForWidth())
        self.PW.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.PW.setFont(font)
        self.PW.setStyleSheet("border: 1px solid #C7C7C7;\n"
"border-radius: 5px;\n"
"padding : 0px 5px;")
        self.PW.setText("")
        self.PW.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PW.setObjectName("PW")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(50, 70, 91, 29))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Spoqa Han Sans Neo")
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(50, 170, 91, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Spoqa Han Sans Neo")
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.HowToUse = QtWidgets.QPushButton(Dialog)
        self.HowToUse.setGeometry(QtCore.QRect(210, 350, 151, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HowToUse.sizePolicy().hasHeightForWidth())
        self.HowToUse.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Spoqa Han Sans Neo")
        font.setPointSize(10)
        self.HowToUse.setFont(font)
        self.HowToUse.setStyleSheet("border : 1px solid #c7c7c7;\n"
"color : #A7A7A7;\n"
"border-radius: 5px;")
        self.HowToUse.setObjectName("HowToUse")
        self.InstaLInk = QtWidgets.QPushButton(Dialog)
        self.InstaLInk.setGeometry(QtCore.QRect(50, 350, 141, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InstaLInk.sizePolicy().hasHeightForWidth())
        self.InstaLInk.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Spoqa Han Sans Neo")
        font.setPointSize(10)
        self.InstaLInk.setFont(font)
        self.InstaLInk.setStyleSheet("border : 1px solid #c7c7c7;\n"
"color : #A7A7A7;\n"
"border-radius: 5px;\n"
"")
        self.InstaLInk.setObjectName("InstaLInk")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "서이추 봇"))
        self.StartBtn.setText(_translate("Dialog", "로그인"))
        self.label_6.setText(_translate("Dialog", "아이디"))
        self.label_7.setText(_translate("Dialog", "비밀번호"))
        self.HowToUse.setText(_translate("Dialog", "사용 방법"))
        self.InstaLInk.setText(_translate("Dialog", "개발자 인스타"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())