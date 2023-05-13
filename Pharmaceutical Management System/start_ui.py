# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1275, 844)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(-10, 0, 1290, 861))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("tabWidget{\n"
"font-color: rgb(255, 28, 244);\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(-90, 0, 1451, 811))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/start.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.Welcome = QtWidgets.QLabel(self.tab)
        self.Welcome.setGeometry(QtCore.QRect(430, 10, 261, 81))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(48)
        self.Welcome.setFont(font)
        self.Welcome.setAlignment(QtCore.Qt.AlignCenter)
        self.Welcome.setObjectName("Welcome")
        self.homeTable = QtWidgets.QTableView(self.tab)
        self.homeTable.setGeometry(QtCore.QRect(20, 190, 831, 521))
        self.homeTable.setObjectName("homeTable")
        self.homeTotal = QtWidgets.QLineEdit(self.tab)
        self.homeTotal.setGeometry(QtCore.QRect(960, 650, 141, 61))
        self.homeTotal.setStyleSheet("QLineEdit{\n"
"    border-radius: 20px;\n"
"    border-color:rgb(0, 0, 0);\n"
"}")
        self.homeTotal.setObjectName("homeTotal")
        self.homeName = QtWidgets.QLineEdit(self.tab)
        self.homeName.setGeometry(QtCore.QRect(650, 30, 191, 51))
        self.homeName.setStyleSheet("QLineEdit{\n"
"    border-radius: 20px;\n"
"    border-color:rgb(0, 0, 0);\n"
"    background-image: url(:/newPrefix/start2.jpg);}")
        self.homeName.setObjectName("homeName")
        self.homeName.setAlignment(QtCore.Qt.AlignCenter)
        self.Welcome_3 = QtWidgets.QLabel(self.tab)
        self.Welcome_3.setGeometry(QtCore.QRect(820, 570, 261, 81))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(48)
        self.Welcome_3.setFont(font)
        self.Welcome_3.setAlignment(QtCore.Qt.AlignCenter)
        self.Welcome_3.setObjectName("Welcome_3")
        self.Welcome_7 = QtWidgets.QLabel(self.tab)
        self.Welcome_7.setGeometry(QtCore.QRect(20, 110, 391, 81))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.Welcome_7.setFont(font)
        self.Welcome_7.setAlignment(QtCore.Qt.AlignCenter)
        self.Welcome_7.setObjectName("Welcome_7")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.ordersMobile = QtWidgets.QLineEdit(self.tab_2)
        self.ordersMobile.setGeometry(QtCore.QRect(300, 140, 281, 51))
        self.ordersMobile.setStyleSheet("QLineEdit{\n"
"    border-radius: 20px;\n"
"    border-color:rgb(0, 0, 0);\n"
"}")
        self.ordersMobile.setObjectName("ordersMobile")
        self.Welcome_5 = QtWidgets.QLabel(self.tab_2)
        self.Welcome_5.setGeometry(QtCore.QRect(-10, 30, 301, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(48)
        self.Welcome_5.setFont(font)
        self.Welcome_5.setAlignment(QtCore.Qt.AlignCenter)
        self.Welcome_5.setObjectName("Welcome_5")
        self.Welcome_6 = QtWidgets.QLabel(self.tab_2)
        self.Welcome_6.setGeometry(QtCore.QRect(0, 140, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(48)
        self.Welcome_6.setFont(font)
        self.Welcome_6.setAlignment(QtCore.Qt.AlignCenter)
        self.Welcome_6.setObjectName("Welcome_6")
        self.ordersTable = QtWidgets.QTableView(self.tab_2)
        self.ordersTable.setGeometry(QtCore.QRect(30, 350, 911, 301))
        self.ordersTable.setStyleSheet("QTableView{\n"
"border-radius: 222px;\n"
"border: 1px solid black;\n"
"}")
        self.ordersTable.setObjectName("ordersTable")
        self.Welcome_8 = QtWidgets.QLabel(self.tab_2)
        self.Welcome_8.setGeometry(QtCore.QRect(20, 270, 221, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(48)
        self.Welcome_8.setFont(font)
        self.Welcome_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Welcome_8.setObjectName("Welcome_8")
        self.startShift_3 = QtWidgets.QLineEdit(self.tab_2)
        self.startShift_3.setGeometry(QtCore.QRect(130, 280, 341, 51))
        self.startShift_3.setStyleSheet("QLineEdit{\n"
"    border-radius: 20px;\n"
"    border-color:rgb(0, 0, 0);\n"
"}")
        self.startShift_3.setObjectName("startShift_3")
        self.signup_button_3 = QtWidgets.QPushButton(self.tab_2)
        self.signup_button_3.setGeometry(QtCore.QRect(650, 290, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.signup_button_3.setFont(font)
        self.signup_button_3.setObjectName("signup_button_3")
        self.Welcome_9 = QtWidgets.QLabel(self.tab_2)
        self.Welcome_9.setGeometry(QtCore.QRect(-10, 690, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(48)
        self.Welcome_9.setFont(font)
        self.Welcome_9.setAlignment(QtCore.Qt.AlignCenter)
        self.Welcome_9.setObjectName("Welcome_9")
        self.startShift_4 = QtWidgets.QLineEdit(self.tab_2)
        self.startShift_4.setGeometry(QtCore.QRect(130, 690, 121, 51))
        self.startShift_4.setStyleSheet("QLineEdit{\n"
"    border-radius: 20px;\n"
"    border-color:rgb(0, 0, 0);\n"
"}")
        self.startShift_4.setObjectName("startShift_4")
        self.signup_button_4 = QtWidgets.QPushButton(self.tab_2)
        self.signup_button_4.setGeometry(QtCore.QRect(300, 700, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.signup_button_4.setFont(font)
        self.signup_button_4.setObjectName("signup_button_4")
        self.ordersName = QtWidgets.QLineEdit(self.tab_2)
        self.ordersName.setGeometry(QtCore.QRect(300, 40, 271, 51))
        self.ordersName.setStyleSheet("QLineEdit{\n"
"    border-radius: 20px;\n"
"    border-color:rgb(0, 0, 0);\n"
"}")
        self.ordersName.setObjectName("ordersName")
        self.signup_button_7 = QtWidgets.QPushButton(self.tab_2)
        self.signup_button_7.setGeometry(QtCore.QRect(500, 290, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.signup_button_7.setFont(font)
        self.signup_button_7.setObjectName("signup_button_7")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(-40, -30, 1321, 851))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/newPrefix/start.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_3.raise_()
        self.ordersMobile.raise_()
        self.Welcome_5.raise_()
        self.Welcome_6.raise_()
        self.ordersTable.raise_()
        self.Welcome_8.raise_()
        self.startShift_3.raise_()
        self.signup_button_3.raise_()
        self.Welcome_9.raise_()
        self.startShift_4.raise_()
        self.signup_button_4.raise_()
        self.ordersName.raise_()
        self.signup_button_7.raise_()
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setGeometry(QtCore.QRect(-40, -20, 1321, 821))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/newPrefix/start.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.ordersTable_2 = QtWidgets.QTableView(self.tab_3)
        self.ordersTable_2.setGeometry(QtCore.QRect(20, 140, 971, 481))
        self.ordersTable_2.setStyleSheet("QTableView{\n"
"border-radius: 222px;\n"
"border: 1px solid black;\n"
"}")
        self.ordersTable_2.setObjectName("ordersTable_2")
        self.Welcome_10 = QtWidgets.QLabel(self.tab_3)
        self.Welcome_10.setGeometry(QtCore.QRect(0, 0, 301, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(48)
        self.Welcome_10.setFont(font)
        self.Welcome_10.setAlignment(QtCore.Qt.AlignCenter)
        self.Welcome_10.setObjectName("Welcome_10")
        self.signup_button_5 = QtWidgets.QPushButton(self.tab_3)
        self.signup_button_5.setGeometry(QtCore.QRect(850, 630, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.signup_button_5.setFont(font)
        self.signup_button_5.setObjectName("signup_button_5")
        self.ordersName_2 = QtWidgets.QLineEdit(self.tab_3)
        self.ordersName_2.setGeometry(QtCore.QRect(60, 70, 341, 51))
        self.ordersName_2.setStyleSheet("QLineEdit{\n"
"    border-radius: 20px;\n"
"    border-color:rgb(0, 0, 0);\n"
"}")
        self.ordersName_2.setObjectName("ordersName_2")
        self.signup_button_6 = QtWidgets.QPushButton(self.tab_3)
        self.signup_button_6.setGeometry(QtCore.QRect(440, 80, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.signup_button_6.setFont(font)
        self.signup_button_6.setObjectName("signup_button_6")
        self.signup_button_8 = QtWidgets.QPushButton(self.tab_3)
        self.signup_button_8.setGeometry(QtCore.QRect(600, 80, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.signup_button_8.setFont(font)
        self.signup_button_8.setObjectName("signup_button_8")
        self.signup_button_9 = QtWidgets.QPushButton(self.tab_3)
        self.signup_button_9.setGeometry(QtCore.QRect(770, 80, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.signup_button_9.setFont(font)
        self.signup_button_9.setObjectName("signup_button_9")
        self.tabWidget.addTab(self.tab_3, "")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1301, 811))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/start.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.tabWidget.raise_()

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Welcome.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:28pt; font-weight:600; color:#ffffff;\">Welcome</span></p></body></html>"))
        self.Welcome_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:28pt; font-weight:600; color:#ffffff;\">Total</span></p></body></html>"))
        self.Welcome_7.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:28pt; font-weight:600; color:#ffffff;\">Today\'s Purchases</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Home"))
        self.Welcome_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:22pt; color:#ffffff;\">Customer name</span></p></body></html>"))
        self.Welcome_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:22pt; color:#ffffff;\">Mobile number</span></p></body></html>"))
        self.Welcome_8.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:24pt; color:#ffffff;\">Order</span></p></body></html>"))
        self.signup_button_3.setText(_translate("Dialog", "Delete"))
        self.Welcome_9.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:24pt; color:#ffffff;\">Total</span></p></body></html>"))
        self.signup_button_4.setText(_translate("Dialog", "Print order"))
        self.signup_button_7.setText(_translate("Dialog", "Add"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Orders"))
        self.Welcome_10.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:24pt; color:#ffffff;\">Drugs available</span></p></body></html>"))
        self.signup_button_5.setText(_translate("Dialog", "Print report"))
        self.signup_button_6.setText(_translate("Dialog", "search"))
        self.signup_button_8.setText(_translate("Dialog", "Add to stock"))
        self.signup_button_9.setText(_translate("Dialog", "Delete from stock"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Stock"))
import image_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
