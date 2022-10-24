from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow,QApplication
import sys
from os import path
from PyQt5.uic import loadUiType
FORM_CLASS,_ = loadUiType(path.join(path.dirname('__file__'), 'main.ui'))
from report import Report
from datetime import datetime
import os


class Main(QMainWindow, FORM_CLASS):
    def __init__(self, parent= None):
        super(Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.btn_post.clicked.connect(self.mki_report)
        self.btn_post_2.clicked.connect(self.jts2_report)
        self.btn_post_3.clicked.connect(self.jts1_report)
        self.user = os.getlogin()
    def mki_report(self):
        r = Report()
        r.agregate_storage_type(r.mki, 15, "MKI", "S:\Warehouse dept\Inventory control\Reporting and dashboards\Cycle_Count\Reports_CycleCount\MKI\\"+"MKI_" + datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p") + f"_{self.user.upper()}"+'.pdf') 

    def jts1_report(self):
        r = Report()
        r.agregate_storage_type(r.jts1, 10, "JTS1", "S:\Warehouse dept\Inventory control\Reporting and dashboards\Cycle_Count\Reports_CycleCount\JTS1\\"+"JTS1_" + datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p") + f"_{self.user.upper()}"+'.pdf')

    def jts2_report(self):
        r = Report()
        r.agregate_storage_type(r.jts2, 10, "JTS2", "S:\Warehouse dept\Inventory control\Reporting and dashboards\Cycle_Count\Reports_CycleCount\JTS2\\"+"JTS2_" + datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p") + f"_{self.user.upper()}"+'.pdf')

def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()