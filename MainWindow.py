# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(352, 530)
        Dialog.setMinimumSize(QtCore.QSize(352, 530))
        Dialog.setMaximumSize(QtCore.QSize(352, 530))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("python-logo.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.btn_directory_txt = QtWidgets.QToolButton(Dialog)
        self.btn_directory_txt.setGeometry(QtCore.QRect(290, 250, 41, 31))
        self.btn_directory_txt.setObjectName("btn_directory_txt")
        self.txt_directory_txt = QtWidgets.QLineEdit(Dialog)
        self.txt_directory_txt.setGeometry(QtCore.QRect(20, 250, 261, 31))
        self.txt_directory_txt.setObjectName("txt_directory_txt")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(110, 70, 131, 131))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("python-logo.svg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(5, 2, 341, 81))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 220, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.btn_directory_final = QtWidgets.QToolButton(Dialog)
        self.btn_directory_final.setGeometry(QtCore.QRect(290, 320, 41, 31))
        self.btn_directory_final.setObjectName("btn_directory_final")
        self.txt_directory_final = QtWidgets.QLineEdit(Dialog)
        self.txt_directory_final.setGeometry(QtCore.QRect(20, 320, 261, 31))
        self.txt_directory_final.setObjectName("txt_directory_final")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 290, 281, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(7, 470, 371, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setFormat("")
        self.progressBar.setObjectName("progressBar")
        self.btn_copiar = QtWidgets.QPushButton(Dialog)
        self.btn_copiar.setGeometry(QtCore.QRect(80, 370, 91, 41))
        self.btn_copiar.setObjectName("btn_copiar")
        self.btn_sair = QtWidgets.QPushButton(Dialog)
        self.btn_sair.setGeometry(QtCore.QRect(180, 370, 91, 41))
        self.btn_sair.setObjectName("btn_sair")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Copy To List"))
        self.btn_directory_txt.setText(_translate("Dialog", "..."))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:36pt; color:#00aaff;\">COPY TO LIST</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "Escolha o arquivo .txt:"))
        self.btn_directory_final.setText(_translate("Dialog", "..."))
        self.label_4.setText(_translate("Dialog", "Escolha a pasta que contem os arquivos:"))
        self.btn_copiar.setText(_translate("Dialog", "Copiar"))
        self.btn_sair.setText(_translate("Dialog", "Sair"))

