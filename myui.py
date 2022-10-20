from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(341, 248)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../CycleCount/Cycle Counting/REPORT/Assets/icon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_post = QtWidgets.QPushButton(self.centralwidget)
        self.btn_post.setGeometry(QtCore.QRect(10, 10, 321, 66))
        self.btn_post.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 0, 0, 255), stop:0.339795 rgba(255, 0, 0, 255), stop:0.339799 rgba(255, 255, 255, 255), stop:0.662444 rgba(255, 255, 255, 255), stop:0.662469 rgba(0, 0, 255, 255), stop:1 rgba(0, 0, 255, 255));\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../CycleCount/Cycle Counting/REPORT/Assets/icons8-open-file-folder-96.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_post.setIcon(icon1)
        self.btn_post.setIconSize(QtCore.QSize(66, 66))
        self.btn_post.setObjectName("btn_post")
        self.btn_post_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_post_2.setGeometry(QtCore.QRect(10, 170, 321, 66))
        self.btn_post_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 0, 0, 255), stop:0.339795 rgba(255, 0, 0, 255), stop:0.339799 rgba(255, 255, 255, 255), stop:0.662444 rgba(255, 255, 255, 255), stop:0.662469 rgba(0, 0, 255, 255), stop:1 rgba(0, 0, 255, 255));\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"")
        self.btn_post_2.setIcon(icon1)
        self.btn_post_2.setIconSize(QtCore.QSize(66, 66))
        self.btn_post_2.setObjectName("btn_post_2")
        self.btn_post_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_post_3.setGeometry(QtCore.QRect(10, 90, 321, 66))
        self.btn_post_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 0, 0, 255), stop:0.339795 rgba(255, 0, 0, 255), stop:0.339799 rgba(255, 255, 255, 255), stop:0.662444 rgba(255, 255, 255, 255), stop:0.662469 rgba(0, 0, 255, 255), stop:1 rgba(0, 0, 255, 255));\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"")
        self.btn_post_3.setIcon(icon1)
        self.btn_post_3.setIconSize(QtCore.QSize(66, 66))
        self.btn_post_3.setObjectName("btn_post_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Reporter"))
        self.btn_post.setText(_translate("MainWindow", "MKI Report"))
        self.btn_post_2.setText(_translate("MainWindow", "JTS2 Report"))
        self.btn_post_3.setText(_translate("MainWindow", "JTS1 Report"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
