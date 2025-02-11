# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Line_Rejection.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1000, 600)
        Dialog.setStyleSheet("background-color: rgb(103, 103, 103);")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(-3, 100, 1000, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 150, 60))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/PreBo_cmyk.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(590, 10, 161, 91))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Images/rb_1599.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(800, 10, 191, 91))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(180, 20, 381, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(150, 0, 20, 111))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(770, 0, 20, 111))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Dialog)
        self.line_4.setGeometry(QtCore.QRect(0, 140, 1000, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.calendarWidget = QtWidgets.QCalendarWidget(Dialog)
        self.calendarWidget.setGeometry(QtCore.QRect(0, 160, 321, 251))
        self.calendarWidget.setStyleSheet("border-color: rgb(255, 0, 0);\n"
"background-color: rgb(103, 103, 103);\n"
"color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(103, 103, 103);\n"
"background-color: rgb(9, 9, 9);\n"
"alternate-background-color: rgb(255, 255, 11);\n"
"alternate-background-color: rgb(20, 20, 20);\n"
"alternate-background-color: rgb(167, 167, 167);")
        self.calendarWidget.setObjectName("calendarWidget")
        self.line_5 = QtWidgets.QFrame(Dialog)
        self.line_5.setGeometry(QtCore.QRect(360, 490, 601, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_8 = QtWidgets.QFrame(Dialog)
        self.line_8.setGeometry(QtCore.QRect(483, 150, 20, 351))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_10 = QtWidgets.QFrame(Dialog)
        self.line_10.setGeometry(QtCore.QRect(350, 150, 20, 351))
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.line_11 = QtWidgets.QFrame(Dialog)
        self.line_11.setGeometry(QtCore.QRect(790, 150, 20, 351))
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.line_12 = QtWidgets.QFrame(Dialog)
        self.line_12.setGeometry(QtCore.QRect(950, 150, 20, 351))
        self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.line_6 = QtWidgets.QFrame(Dialog)
        self.line_6.setGeometry(QtCore.QRect(360, 180, 601, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.textEdit_11 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_11.setGeometry(QtCore.QRect(180, 420, 150, 30))
        self.textEdit_11.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_11.setObjectName("textEdit_11")
        self.label_43 = QtWidgets.QLabel(Dialog)
        self.label_43.setGeometry(QtCore.QRect(20, 465, 151, 21))
        self.label_43.setObjectName("label_43")
        self.label_30 = QtWidgets.QLabel(Dialog)
        self.label_30.setGeometry(QtCore.QRect(70, 425, 101, 21))
        self.label_30.setObjectName("label_30")
        self.textEdit_12 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_12.setGeometry(QtCore.QRect(180, 460, 150, 30))
        self.textEdit_12.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_12.setObjectName("textEdit_12")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(660, 520, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(540, 520, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_31 = QtWidgets.QLabel(Dialog)
        self.label_31.setGeometry(QtCore.QRect(70, 505, 101, 21))
        self.label_31.setObjectName("label_31")
        self.textEdit_13 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_13.setGeometry(QtCore.QRect(180, 500, 150, 30))
        self.textEdit_13.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_13.setObjectName("textEdit_13")
        self.textEdit_14 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_14.setGeometry(QtCore.QRect(180, 540, 150, 30))
        self.textEdit_14.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_14.setObjectName("textEdit_14")
        self.label_44 = QtWidgets.QLabel(Dialog)
        self.label_44.setGeometry(QtCore.QRect(20, 545, 151, 21))
        self.label_44.setObjectName("label_44")
        self.splitter = QtWidgets.QSplitter(Dialog)
        self.splitter.setGeometry(QtCore.QRect(10, 120, 981, 16))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label_5 = QtWidgets.QLabel(self.splitter)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.splitter)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.splitter_2 = QtWidgets.QSplitter(Dialog)
        self.splitter_2.setGeometry(QtCore.QRect(350, 160, 601, 20))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.label_7 = QtWidgets.QLabel(self.splitter_2)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.splitter_2)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.splitter_2)
        self.label_9.setObjectName("label_9")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(397, 200, 51, 291))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        self.label_12.setObjectName("label_12")
        self.verticalLayout.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget)
        self.label_13.setObjectName("label_13")
        self.verticalLayout.addWidget(self.label_13)
        self.label_19 = QtWidgets.QLabel(self.layoutWidget)
        self.label_19.setObjectName("label_19")
        self.verticalLayout.addWidget(self.label_19)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget)
        self.label_14.setObjectName("label_14")
        self.verticalLayout.addWidget(self.label_14)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget)
        self.label_15.setObjectName("label_15")
        self.verticalLayout.addWidget(self.label_15)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget)
        self.label_16.setObjectName("label_16")
        self.verticalLayout.addWidget(self.label_16)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget)
        self.label_17.setObjectName("label_17")
        self.verticalLayout.addWidget(self.label_17)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget)
        self.label_18.setObjectName("label_18")
        self.verticalLayout.addWidget(self.label_18)
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(540, 200, 217, 291))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_20 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_2.addWidget(self.label_20)
        self.label_21 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_2.addWidget(self.label_21)
        self.label_29 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_29.setObjectName("label_29")
        self.verticalLayout_2.addWidget(self.label_29)
        self.label_22 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_2.addWidget(self.label_22)
        self.label_24 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_2.addWidget(self.label_24)
        self.label_28 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_28.setObjectName("label_28")
        self.verticalLayout_2.addWidget(self.label_28)
        self.label_23 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_2.addWidget(self.label_23)
        self.label_25 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_2.addWidget(self.label_25)
        self.label_26 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_2.addWidget(self.label_26)
        self.label_27 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_2.addWidget(self.label_27)
        self.layoutWidget2 = QtWidgets.QWidget(Dialog)
        self.layoutWidget2.setGeometry(QtCore.QRect(830, 200, 101, 766))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textEdit = QtWidgets.QTextEdit(self.layoutWidget2)
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_3.addWidget(self.textEdit)
        self.textEdit_2 = QtWidgets.QTextEdit(self.layoutWidget2)
        self.textEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout_3.addWidget(self.textEdit_2)
        self.textEdit_3 = QtWidgets.QTextEdit(self.layoutWidget2)
        self.textEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_3.setObjectName("textEdit_3")
        self.verticalLayout_3.addWidget(self.textEdit_3)
        self.textEdit_4 = QtWidgets.QTextEdit(self.layoutWidget2)
        self.textEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_4.setObjectName("textEdit_4")
        self.verticalLayout_3.addWidget(self.textEdit_4)
        self.textEdit_5 = QtWidgets.QTextEdit(self.layoutWidget2)
        self.textEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_5.setObjectName("textEdit_5")
        self.verticalLayout_3.addWidget(self.textEdit_5)
        self.textEdit_8 = QtWidgets.QTextEdit(self.layoutWidget2)
        self.textEdit_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_8.setObjectName("textEdit_8")
        self.verticalLayout_3.addWidget(self.textEdit_8)
        self.textEdit_9 = QtWidgets.QTextEdit(self.layoutWidget2)
        self.textEdit_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_9.setObjectName("textEdit_9")
        self.verticalLayout_3.addWidget(self.textEdit_9)
        self.textEdit_10 = QtWidgets.QTextEdit(self.layoutWidget2)
        self.textEdit_10.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_10.setObjectName("textEdit_10")
        self.verticalLayout_3.addWidget(self.textEdit_10)
        self.textEdit_7 = QtWidgets.QTextEdit(self.layoutWidget2)
        self.textEdit_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_7.setObjectName("textEdit_7")
        self.verticalLayout_3.addWidget(self.textEdit_7)
        self.textEdit_6 = QtWidgets.QTextEdit(self.layoutWidget2)
        self.textEdit_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_6.setObjectName("textEdit_6")
        self.verticalLayout_3.addWidget(self.textEdit_6)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Doc.No : PBA/QC/R/06</span></p><p><span style=\" font-weight:600;\">Otiginal Data : 30-10-2019</span></p><p><span style=\" font-weight:600;\">Rev.No : </span></p><p><span style=\" font-weight:600;\">Rev.Date : </span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "Line Rejection DataSheet"))
        self.label_43.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Supervisor/Engg Sign:</span></p></body></html>"))
        self.label_30.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Operator Sign:</span></p></body></html>"))
        self.pushButton_4.setText(_translate("Dialog", "CLEAR"))
        self.pushButton_3.setText(_translate("Dialog", "SAVE"))
        self.label_31.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Operator Sign:</span></p></body></html>"))
        self.label_44.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Supervisor/Engg Sign:</span></p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Work Station :- Valve plate &amp; clamping sleeve Assy.</span></p></body></html>"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p align=\"right\"><span style=\" font-size:9pt; font-weight:600;\">Product.No:2447.222.126</span></p></body></html>"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Sr.No.</span></p></body></html>"))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Rejection Type</span></p></body></html>"))
        self.label_9.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Counts</span></p></body></html>"))
        self.label_10.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">1</span></p></body></html>"))
        self.label_11.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">2</span></p></body></html>"))
        self.label_12.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">3</span></p></body></html>"))
        self.label_13.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">4</span></p></body></html>"))
        self.label_19.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">5</span></p></body></html>"))
        self.label_14.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">6</span></p></body></html>"))
        self.label_15.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">7</span></p></body></html>"))
        self.label_16.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">8</span></p></body></html>"))
        self.label_17.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">9</span></p></body></html>"))
        self.label_18.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">10</span></p></body></html>"))
        self.label_20.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Threaded Ferrule Damage</span></p></body></html>"))
        self.label_21.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Threaded Ferrule Thread Damage</span></p></body></html>"))
        self.label_29.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Valve Plate Damage</span></p></body></html>"))
        self.label_22.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Spring short Length</span></p></body></html>"))
        self.label_24.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Filler Piece damage</span></p></body></html>"))
        self.label_28.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Clamping Sleeve Damage</span></p></body></html>"))
        self.label_23.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Leakage Not ok(LN1)</span></p></body></html>"))
        self.label_25.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Rust on clamping sleeve</span></p></body></html>"))
        self.label_26.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Filler Piece missing</span></p></body></html>"))
        self.label_27.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Fallen Down Part  (FD1)</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
