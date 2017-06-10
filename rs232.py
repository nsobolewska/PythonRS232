import sys
from PyQt5.QtWidgets import *
# QMainWindow, QPushButton, QApplication, QAction
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import pyqtSlot, Qt

class Window(QMainWindow):
    listOfWords = []
    binary_list = []
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(700, 300, 500, 500)
        self.okno = QWidget(self)
        self.setCentralWidget(self.okno)
        self.mainLayout = QVBoxLayout()
        # self.mainLayout.setGeometry(100,100,300,300)
        self.gridLayout = QGridLayout()
        self.okno.setLayout(self.mainLayout)
        self.setWindowTitle("Menu")
        self.app_open = False
        self.app2_open = False
        self.buttons()
        self.show()

    def buttons(self):
        self.btn0 = QPushButton('Nadajnik', self)
        self.btn0.clicked.connect(self.on_click0)
        self.btn0.resize(400,100)
        self.btn0.move(50, 50)

        self.btn1 = QPushButton('Odbiornik', self)
        self.btn1.clicked.connect(self.on_click1)
        self.btn1.resize(400, 100)
        self.btn1.move(50, 170)

        self.btn2 = QPushButton('Zakoncz', self)
        self.btn2.clicked.connect(self.close)
        self.btn2.resize(400, 100)
        self.btn2.move(50, 290)

    def on_click0(self):
        if not self.app_open:
            self.app = childWindow(self)
            self.app_open = True
        else:
            self.app.close_window()
            self.app_open = False
        #sys.exit(self.app.exec())
    def on_click1(self):
        if not self.app2_open:
            self.app2 = childWindowreciv(self)
            self.app2_open = True
        else:
            self.app2.close_window()
            self.app2_open = False
        print(self.listOfWords)
        print("to odbiornik")
    def close(self):
        choice = QMessageBox.question(self, 'Extract', "Are you sure you want to quit?",
                                      QMessageBox.Yes | QMessageBox.No)

        if choice == QMessageBox.Yes:
            print("Zamykamy sie")
            sys.exit()
        else:
            pass
    def closeEvent(self, QCloseEvent):
        QCloseEvent.ignore()
        self.close()

class childWindow(QDialog):
    nowy = " "
    def __init__(self, parent = None):
        super(childWindow, self).__init__()
        self.setGeometry(200, 300, 500, 500)
        self.okno = QWidget(self)
        self.parent = parent
        self.setWindowTitle("Nadajnik")
        self.buttons()
        self.textbox()
        self.show()

    def textbox(self):
        self.textedit = QTextEdit("Wpisz tekst z klawiatury",self)
        self.textedit.move(50, 50)
        self.textedit.setFont(QtGui.QFont('SansSerif', 9))
        self.textedit.resize(400, 100)
        self.textedit2 = QTextEdit("Tu bedzie kod binarny", self)
        self.textedit2.move(50, 250)
        self.textedit2.setFont(QtGui.QFont('SansSerif', 9))
        self.textedit2.resize(400, 100)

        self.show()

    def buttons(self):
        self.btn0 = QPushButton('Nadaj', self)
        self.btn0.clicked.connect(self.on_click0)
        self.btn0.resize(80, 50)
        self.btn0.move(50, 180)

        self.btn1 = QPushButton('Czysc', self)
        self.btn1.clicked.connect(self.on_click1)
        self.btn1.resize(80, 50)
        self.btn1.move(150, 180)

        self.btn2 = QPushButton('Zakoncz', self)
        self.btn2.clicked.connect(self.close)
        self.btn2.resize(80, 50)
        self.btn2.move(250, 180)

    def on_click0(self):
        self.nowy = self.textedit.toPlainText()
        print(self.nowy)
        # split the text
        words = self.nowy.split()

        # for each word in the line:
        for word in words:
            # print the word
            Window.listOfWords.append(word)
            print(word)
        self.asciToBinary()

    def on_click1(self):
        Window.binary_list = []
        Window.listOfWords = []
        self.nowy = ""
        self.textedit.setText(self.nowy)

    def asciToBinary(self):
        Window.binary_list.append(1)
        for i in range(len(Window.listOfWords)):
            for letter in Window.listOfWords[i]:
                licz = 0
                # print(bin(ord(letter)))
                Window.binary_list.append(1)
                for k in bin(ord(letter)):
                    if licz>1:
                        Window.binary_list.append((int)(k))
                    licz = licz + 1
                print(licz)
                Window.binary_list.append(1)
                Window.binary_list.append(1)
            licz = 0
            Window.binary_list.append(1)
            Window.binary_list.append(0)
            for k in bin(32):
                if licz>1:
                    print("*")
                    Window.binary_list.append((int)(k))
                licz = licz + 1
            print(licz)
            Window.binary_list.append(1)
            Window.binary_list.append(1)

        Window.binary_list.append(1)
        Window.binary_list.append(1)
        self.binaryText = ""
        for i in Window.binary_list:
            self.binaryText = self.binaryText + (str)(i)
        self.textedit2.setText(self.binaryText)
        print(len(Window.binary_list))

    def close(self):
        choice = QMessageBox.question(self, 'Extract', "Are you sure you want to quit?",
                                      QMessageBox.Yes | QMessageBox.No)

        if choice == QMessageBox.Yes:
            print("Zamykamy sie")
            self.destroy()
            self.parent.app_open = False
        else:
            pass

    def closeEvent(self, QCloseEvent):
        QCloseEvent.ignore()
        self.close()

    def close_window(self):
        self.destroy()

class childWindowreciv(QDialog):
    nowy = " "
    def __init__(self, parent = None):
        super(childWindowreciv, self).__init__()
        self.setGeometry(900, 300, 500, 500)
        self.okno = QWidget(self)
        self.parent = parent
        self.setWindowTitle("Odbiornik")
        self.buttons()
        self.textbox()
        self.show()

    def textbox(self):
        self.textedit = QTextEdit("Tu pojawi sie odebrany tekst",self)
        self.textedit.move(50, 50)
        self.textedit.setFont(QtGui.QFont('SansSerif', 9))
        self.textedit.resize(400, 100)

        self.show()

    def buttons(self):
        self.btn0 = QPushButton('Odbierz', self)
        self.btn0.clicked.connect(self.on_click0)
        self.btn0.resize(80, 50)
        self.btn0.move(50, 290)

        self.btn2 = QPushButton('Zakoncz', self)
        self.btn2.clicked.connect(self.close)
        self.btn2.resize(80, 50)
        self.btn2.move(250, 290)

    def on_click0(self):

        count = 0
        countLetter = 0
        carry = (len(Window.binary_list)-3)%10
        ascicode = []
        code = 0
        power = 7
        if carry!=0:
            print(carry)
            self.textedit.setText("Blad transmisji- zgubiono bity")
        else:
            for i in Window.binary_list:
                print("Pierwszy for")
                if count>0 and count<(len(Window.binary_list)-2):
                    print("Pierwszy for pierwszy if")
                    if countLetter>0 and countLetter<8:
                        print("Pierwszy for pierwszy if pierwszy if")
                        print(i)
                        code = code +(i * 2**power)
                        print("potega",power)
                    if countLetter == 10:
                        print("Pierwszy for pierwszy if drugi if")
                        countLetter = 0
                        ascicode.append(code)
                        code = 0
                        power = 7
                    countLetter+=1
                    power-=1
                count+=1
            nowy = ""
            for let in ascicode:
                print("Drugi for")
                print(let)
                nowy = nowy + chr(let)
            # for i in range(len(Window.listOfWords)):
            #     nowy = nowy+Window.listOfWords[i]+" "
            self.textedit.setText(nowy)

    def close(self):
        choice = QMessageBox.question(self, 'Extract', "Are you sure you want to quit?",
                                      QMessageBox.Yes | QMessageBox.No)

        if choice == QMessageBox.Yes:
            print("Zamykamy sie")
            self.destroy()
            self.parent.app2_open = False
        else:
            pass

    def closeEvent(self, QCloseEvent):
        QCloseEvent.ignore()
        self.close()

    def close_window(self):
        self.destroy()


def run():
    app = QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec())

run()