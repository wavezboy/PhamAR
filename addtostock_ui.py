# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addtostock.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1304, 848)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 1321, 851))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/newPrefix/start.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.Welcome_10 = QtWidgets.QLabel(Dialog)
        self.Welcome_10.setGeometry(QtCore.QRect(20, 140, 301, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(48)
        self.Welcome_10.setFont(font)
        self.Welcome_10.setAlignment(QtCore.Qt.AlignCenter)
        self.Welcome_10.setObjectName("Welcome_10")
        self.ordersName_2 = QtWidgets.QLineEdit(Dialog)
        self.ordersName_2.setGeometry(QtCore.QRect(300, 150, 341, 51))
        self.ordersName_2.setStyleSheet("QLineEdit{\n"
"    border-radius: 20px;\n"
"    border-color:rgb(0, 0, 0);\n"
"}")
        self.ordersName_2.setObjectName("ordersName_2")
        self.ordersName_3 = QtWidgets.QLineEdit(Dialog)
        self.ordersName_3.setGeometry(QtCore.QRect(860, 270, 341, 51))
        self.ordersName_3.setStyleSheet("QLineEdit{\n"
"    border-radius: 20px;\n"
"    border-color:rgb(0, 0, 0);\n"
"}")
        self.ordersName_3.setObjectName("ordersName_3")
        self.Welcome_11 = QtWidgets.QLabel(Dialog)
        self.Welcome_11.setGeometry(QtCore.QRect(10, 250, 301, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(48)
        self.Welcome_11.setFont(font)
        self.Welcome_11.setAlignment(QtCore.Qt.AlignCenter)
        self.Welcome_11.setObjectName("Welcome_11")
        self.Welcome_12 = QtWidgets.QLabel(Dialog)
        self.Welcome_12.setGeometry(QtCore.QRect(620, 140, 301, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(48)
        self.Welcome_12.setFont(font)
        self.Welcome_12.setAlignment(QtCore.Qt.AlignCenter)
        self.Welcome_12.setObjectName("Welcome_12")
        self.ordersName_4 = QtWidgets.QLineEdit(Dialog)
        self.ordersName_4.setGeometry(QtCore.QRect(300, 270, 341, 51))
        self.ordersName_4.setStyleSheet("QLineEdit{\n"
"    border-radius: 20px;\n"
"    border-color:rgb(0, 0, 0);\n"
"}")
        self.ordersName_4.setObjectName("ordersName_4")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(140, 440, 1001, 371))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("QTableWidget {\n"
"    border: 1px solid black;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid rgb(15, 12, 107);\n"
"    font-weight: bold;\n"
"    font-size: 18px;\n"
"    color: black;\n"
"}\n"
"")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(250)
        self.tableWidget.verticalHeader().setDefaultSectionSize(50)
        self.tableWidget.verticalHeader().setMinimumSectionSize(50)
        self.Welcome_13 = QtWidgets.QLabel(Dialog)
        self.Welcome_13.setGeometry(QtCore.QRect(620, 260, 301, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(48)
        self.Welcome_13.setFont(font)
        self.Welcome_13.setAlignment(QtCore.Qt.AlignCenter)
        self.Welcome_13.setObjectName("Welcome_13")
        self.ordersName_5 = QtWidgets.QLineEdit(Dialog)
        self.ordersName_5.setGeometry(QtCore.QRect(860, 150, 341, 51))
        self.ordersName_5.setStyleSheet("QLineEdit{\n"
"    border-radius: 20px;\n"
"    border-color:rgb(0, 0, 0);\n"
"}")
        self.ordersName_5.setObjectName("ordersName_5")
        self.signup_button_8 = QtWidgets.QPushButton(Dialog)
        self.signup_button_8.setGeometry(QtCore.QRect(460, 350, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.signup_button_8.setFont(font)
        self.signup_button_8.setObjectName("signup_button_8")
        self.signup_button_9 = QtWidgets.QPushButton(Dialog)
        self.signup_button_9.setGeometry(QtCore.QRect(720, 350, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.signup_button_9.setFont(font)
        self.signup_button_9.setObjectName("signup_button_9")
        self.Welcome_14 = QtWidgets.QLabel(Dialog)
        self.Welcome_14.setGeometry(QtCore.QRect(330, 0, 631, 111))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(72)
        self.Welcome_14.setFont(font)
        self.Welcome_14.setAlignment(QtCore.Qt.AlignCenter)
        self.Welcome_14.setObjectName("Welcome_14")
        self.back = QtWidgets.QPushButton(Dialog)
        self.back.setGeometry(QtCore.QRect(20, 10, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.back.setFont(font)
        self.back.setObjectName("back")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Welcome_10.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:24pt; color:#ffffff;\">Drugs name</span></p></body></html>"))
        self.Welcome_11.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:24pt; color:#ffffff;\">Expiry date</span></p></body></html>"))
        self.Welcome_12.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:24pt; color:#ffffff;\">Provider</span></p></body></html>"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Drug name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Provider"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Quantity "))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Expiry date"))
        self.Welcome_13.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:24pt; color:#ffffff;\">Quantity</span></p></body></html>"))
        self.signup_button_8.setText(_translate("Dialog", "Add drug"))
        self.signup_button_9.setText(_translate("Dialog", "Remove drug"))
        self.Welcome_14.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:48pt; color:#ffffff;\">Add item to stock</span></p></body></html>"))
        self.back.setText(_translate("Dialog", "Back"))
import image_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
