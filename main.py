from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import QMainWindow,QApplication
import sys
from os import path
from PyQt6.uic import loadUiType
FORM_CLASS,_ = loadUiType(path.join(path.dirname('__file__'), 'main.ui'))
from report import Report

class Main(QMainWindow, FORM_CLASS):
    def __init__(self, parent= None):
        super(Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.btn_post.clicked.connect(self.mki_report)
        self.btn_post_2.clicked.connect(self.jts2_report)
        self.btn_post_3.clicked.connect(self.jts1_report)
    def mki_report(self):
        r = Report()
        r.agregate_storage_type(r.mki, 15, "MKI") 
    def jts1_report(self):
        r = Report()
        r.agregate_storage_type(r.jts1, 10, "JTS1")
    def jts2_report(self):
        r = Report()
        r.agregate_storage_type(r.jts2, 10, "JTS2")

def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()