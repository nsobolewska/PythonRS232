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
        self.show()

def run():
    app = QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec())

run()