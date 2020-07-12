import sys
from PyQt5.QtWidgets import *
from tkinter import *
from PyQt5.QAxContainer import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")


        self.setWindowTitle("종목 코드")
        self.setGeometry(300, 300, 500, 300)

        connactionButton = QPushButton("접속하기", self)
        connactionButton.move(400, 10)
        connactionButton.resize(100,50)
        connactionButton.clicked.connect(self.connactionbutton_clicked)

        btn1 = QPushButton("종목코드 얻기", self)
        btn1.move(270, 10)
        btn1.clicked.connect(self.btn1_clicked)

        self.listWidget = QListWidget(self)
        self.listWidget.setGeometry(10, 10, 170, 200)

    def btn1_clicked(self):
        ret = self.kiwoom.dynamicCall("GetCodeListByMarket(QString)", ["0"])
        kospi_code_list = ret.split(';')
        kospi_code_name_list = []

        for x in kospi_code_list:
            name = self.kiwoom.dynamicCall("GetMasterCodeName(QString)", [x])
            kospi_code_name_list.append(x + " : " + name)

        self.listWidget.addItems(kospi_code_name_list)
        self.listWidget.itemDoubleClicked.connect(self.list_Clicked)

    def list_clicked(self):
        print(self.listWidget.currentItem().text())

    def connactionbutton_clicked(self):
        if self.kiwoom.dynamicCall("GetConnectState()") == 0:
            self.kiwoom.dynamicCall("CommConnect()")
        else:
            self.statusBar().showMessage("Already Connected")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    sys.exit(app.exec_())
