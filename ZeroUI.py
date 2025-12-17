# Link for all UI Icons: https://www.istockphoto.com/search/search-by-asset?assetid=1325307677&assettype=film

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

with open('pwd.txt', 'r') as pwd:
    path = pwd.read()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Crystal")
        MainWindow.resize(1000, 1000)
        MainWindow.setWindowFlag(Qt.FramelessWindowHint)


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: black;")

        font = QtGui.QFont()
        font.setPointSize(50)
        font.setFamily('Sans Serif')

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("CRYSTAL ZERO")
        self.label.move(320, 150)
        self.label.setStyleSheet("color: white;")
        self.label.setFont(font)

        self.mic = QtWidgets.QPushButton(self.centralwidget)
        self.mic.setGeometry(QtCore.QRect(150, 650, 200, 200))
        self.mic.setText("")
        self.mic.setIcon(QIcon(f"{path}/img/UI/Mic.jpg"))
        self.mic.setIconSize(QtCore.QSize(150,150))
        self.mic.setStyleSheet("border-radius: 100px;")
        self.mic.setObjectName("Mic")

        self.speaker = QtWidgets.QPushButton("", self.centralwidget)
        self.speaker.setGeometry(QtCore.QRect(670, 680, 150, 150))
        self.speaker.setText("")
        self.speaker.setIcon(QIcon(f"{path}/img/UI/Speaker.jpg"))
        self.speaker.setIconSize(QtCore.QSize(150,150))
        self.speaker.setStyleSheet("border-radius: 100px;")
        self.speaker.setObjectName("Speaker")
        
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setFamily("Dash Horizon")

        self.textbox = QLineEdit(self.centralwidget)
        self.textbox.setFont(font)
        self.textbox.move(200, 300)
        self.textbox.setAlignment(Qt.AlignTop)
        self.textbox.setStyleSheet("color: white; border: 2px solid rgb(31, 121, 190);")
        self.textbox.resize(600,300)

        self.button = QPushButton('GENERATE RESPONSE', self.centralwidget)
        self.button.setFont(font)
        self.button.setStyleSheet('''border: 2px solid rgb(31, 121, 190);
            color: rgb(31, 121, 190);
            border-radius: 5px;
            padding: 10px 10px;''')
        self.button.move(425, 650)

        self.mic.raise_()
        self.speaker.raise_()
        self.textbox.raise_()
        self.button.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

