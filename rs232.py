import sys
from PyQt5.QtWidgets import *
# QMainWindow, QPushButton, QApplication, QAction
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import pyqtSlot, Qt

class Window(QMainWindow):
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
            self.app = childWindow()
            self.app_open = True
        else:
            self.app.close_window()
            self.app_open = False
        #sys.exit(self.app.exec())
    def on_click1(self):
        print("to odbiornik")
    def close(self):
        choice = QMessageBox.question(self, 'Extract', "Are you sure you want to quit?",
                                      QMessageBox.Yes | QMessageBox.No)

        if choice == QMessageBox.Yes:
            print("Zamykamy sie")
            sys.exit()
        else:
            pass

class childWindow(QDialog):
    nowy = " "
    def __init__(self):
        super(childWindow, self).__init__()
        self.setGeometry(200, 300, 500, 500)
        self.okno = QWidget(self)
        # self.setCentralWidget(self.okno)
        self.mainLayout = QVBoxLayout()
        # self.mainLayout.setGeometry(100,100,300,300)
        self.gridLayout = QGridLayout()
        self.okno.setLayout(self.mainLayout)
        self.setWindowTitle("Menu")
        self.buttons()
        self.textbox()
        self.show()

    def textbox(self):
        self.text = QLabel("Wpisz tekst z klawiatury",self)
        # self.text.setText("Wpisz tekst z klawiatury")
        self.text.move(50,50)
        self.text.setFont(QtGui.QFont('SansSerif', 15))
        self.text.resize(self.text.minimumSizeHint())
        self.show()

    def buttons(self):
        self.btn0 = QPushButton('Nadaj', self)
        self.btn0.clicked.connect(self.on_click0)
        self.btn0.resize(80, 50)
        self.btn0.move(50, 290)

        self.btn1 = QPushButton('Czysc', self)
        self.btn1.clicked.connect(self.on_click1)
        self.btn1.resize(80, 50)
        self.btn1.move(150, 290)

        self.btn2 = QPushButton('Zakoncz', self)
        self.btn2.clicked.connect(self.close)
        self.btn2.resize(80, 50)
        self.btn2.move(250, 290)

    def on_click0(self):
        print("Tu bedzie przesylanie")

    def on_click1(self):
        print("to bedzie czyszczenie textboxa")

    def close(self):
        choice = QMessageBox.question(self, 'Extract', "Are you sure you want to quit?",
                                      QMessageBox.Yes | QMessageBox.No)

        if choice == QMessageBox.Yes:
            print("Zamykamy sie")
            sys.exit(self.exec())
        else:
            pass

    def closeEvent(self, QCloseEvent):
        QCloseEvent.ignore()
        self.close()

    def keyPressEvent(self, event):
        if type(event) == QtGui.QKeyEvent:
            self.nowy = (str)(event.key())
            self.text.setText(self.nowy)
            print(event.key())

    def close_window(self):
        self.destroy()


def run():
    app = QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec())

run()