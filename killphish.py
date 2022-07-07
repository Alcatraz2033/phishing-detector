# -*- coding: utf-8 -*-

import requests
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(438, 222)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(438, 222))
        MainWindow.setMaximumSize(QtCore.QSize(438, 222))
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 80, 95, 31))
        self.pushButton.setStyleSheet("QPushButton{    \n"
"background-color: rgb(136, 138, 133);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 10pt \"Hack NF\";\n"
"border-radius:9px;\n"
"}\n"
"\n"
"QPushButton:hover{    \n"
"    background-color: rgb(136, 138, 133);\n"
"    background-color: rgb(114, 159, 207);\n"
"    font: 75 10pt \"Hack NF\";\n"
"}\n"
"\n"
"QPushButton{    \n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 10pt \"Hack NF\";\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 120, 401, 71))
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font Mono")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(138, 226, 52);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 10, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Hack NF")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(238, 238, 236);")
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 50, 111, 17))
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font Mono")
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(238, 238, 236);")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 80, 301, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"font: 10pt \"Hack Nerd Font Mono\";\n"
"border-radius:9px;")
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.method_pushButton)
            
    def method_pushButton(self):
        link = self.lineEdit.text()
        url = 'https://isitphishing.org'
        data = { 'url' : link }
        headers = { 'X-Requested-With' : 'XMLHttpRequest', 'Referer' : 'https://isitphishing.org/' }

        s = requests.session()
        r = s.post(url + '/search-engine-process.php', data=data, headers=headers)
        res = r.text.split()[0]
        
        if res == 'PHISHING':
            self.label.setText("")
            self.label.setStyleSheet("color: rgb(164, 0, 0);")
            self.label.setText("PELIGRO PHISHING")

        elif res == 'UNKNOWN':
            self.label.setText("")
            self.label.setStyleSheet("color: rgb(138, 226, 52);")
            self.label.setText("NO PHISHING")

        else:
            self.label.setText("")
            self.label.setStyleSheet("color: rgb(238, 238, 236);")
            self.label.setText("Muchas Peticiones")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "KILLPHISH"))
        self.pushButton.setText(_translate("MainWindow", "Iniciar"))
        self.pushButton.setShortcut(_translate("MainWindow", "Return"))
        self.label.setText(_translate("MainWindow", ""))
        self.label_2.setText(_translate("MainWindow", "KILLPHISH"))
        self.label_3.setText(_translate("MainWindow", "BY: Alcatraz2033"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "LINK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
