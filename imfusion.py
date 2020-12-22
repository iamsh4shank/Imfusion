import sys
import os
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QInputDialog, QLineEdit, QFileDialog, QHBoxLayout, QLabel, QTextEdit
from PyQt5.QtGui import QIcon, QPixmap  
import webbrowser
import fusion_main as fuse
import cv2

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(958, 775)
        self.fileName1 = ''
        self.fileName2 = ''
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 426, 354))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.radioButton1 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton1.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton1)
        self.radioButton2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton2.setObjectName("radioButton_4")
        self.verticalLayout.addWidget(self.radioButton2)
        self.radioButton3 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton3.setObjectName("radioButton_3")
        self.verticalLayout.addWidget(self.radioButton3)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.textBrowser_2.setEnabled(True)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.verticalLayout.addWidget(self.textBrowser_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, 6, 10, 6)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(460, 20, 151, 18))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(490, 60, 371, 271))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 480, 371, 271))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 440, 151, 18))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(530, 470, 371, 271))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(500, 440, 151, 18))
        self.label_6.setObjectName("label_6")

        self.generatedImage = ''

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.initUI()
    
    def initUI(self):
        self.pushButton.clicked.connect(self.on_click)
        self.pushButton_3.clicked.connect(self.openGenImage)
        self.radioButton1.clicked.connect(self.options_1)
        self.radioButton2.clicked.connect(self.options_2)
        self.radioButton3.clicked.connect(self.options_3)

        self.show()

    def options_1(self):
        self.textBrowser_2.setText("You selected Image Mixing")
        self.pushButton_2.clicked.connect(self.openFileNameDialog_1)
        self.pushButton_2.clicked.connect(self.openFileNameDialog_2)

    def options_2(self):
        self.textBrowser_2.setText("You selected Face Morphing ")    
        self.pushButton_2.clicked.connect(self.openFileNameDialog_1)
        self.pushButton_2.clicked.connect(self.openFileNameDialog_2)

    def options_3(self):
        self.textBrowser_2.setText("You selected Image restoration")
        self.pushButton_2.clicked.connect(self.openFileNameDialog_1)
        self.pushButton_2.clicked.connect(self.openFileNameDialog_2)


    def showImg(self, img ):
        hbox = QHBoxLayout(self)                                                                                                           
        pixmap = QPixmap(img)                                                                                                        

        lbl = QLabel(self)                                                                                                                 
        lbl.setPixmap(pixmap)                                                                                                              

        hbox.addWidget(lbl)                                                                                                                
        self.setLayout(hbox)                                                                                                               

        self.move(300, 200)                                                                                                                
        self.setWindowTitle('Image with PyQt')                                                                                             
        self.show() 

    @pyqtSlot()
    def openFileNameDialog_1(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName1, _ = QFileDialog.getOpenFileName(self,"Select file to insert", "","All Files (*);;Python Files (*.py)", options=options)
        if self.fileName1:
            print(self.fileName1)
            self.label.setText("Attached image: "+self.fileName1)
            pixmap = QPixmap(self.fileName1)
            pixmap2 = pixmap.scaledToWidth(100)
            pixmap3 = pixmap.scaledToHeight(400)
            self.label_3.setPixmap(pixmap3)
            #testing 
            #sample_images(1000)
            self.showImg(self.fileName1)

    @pyqtSlot()
    def openFileNameDialog_2(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName2, _ = QFileDialog.getOpenFileName(self,"Select file to insert", "","All Files (*);;Python Files (*.py)", options=options)
        if self.fileName2:
            print(self.fileName2)
            self.label.setText("Attached image: "+self.fileName2)
            pixmap = QPixmap(self.fileName2)
            pixmap2 = pixmap.scaledToWidth(100)
            pixmap3 = pixmap.scaledToHeight(400)
            self.label_5.setPixmap(pixmap3)
            #testing 
            #sample_images(1000)
            self.showImg(self.fileName2)

    @pyqtSlot()
    def openFileNameDialog_3(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName1, _ = QFileDialog.getOpenFileName(self,"Select file to insert", "","All Files (*);;Python Files (*.py)", options=options)
        if self.fileName1:
            print(self.fileName1)
            self.label.setText("Attached image: "+self.fileName1)
            pixmap = QPixmap(self.fileName1)
            pixmap2 = pixmap.scaledToWidth(100)
            pixmap3 = pixmap.scaledToHeight(400)
            self.label_3.setPixmap(pixmap3)
            #testing 
            #sample_images(1000)
            self.showImg(self.fileName1)

        
    @pyqtSlot()
    def openGenImage(self):
        self.generatedImage = fuse.fusion(self.fileName1, self.fileName2)    
        print(self.generatedImage)
        pixmap = QPixmap(self.generatedImage)
        pixmap2 = pixmap.scaledToWidth(100)
        pixmap3 = pixmap.scaledToHeight(400)
        self.label_2.setPixmap(pixmap3)
        #testing 
        #sample_images(1000)
        self.showImg(self.generatedImage)


        

    @pyqtSlot()
    def on_click(self):
        sys.exit()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu Medium Italic\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Welcome to Imfusion</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">An Open Source Imaging client of </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">pyImageFusion library</span></p></body></html>"))
        self.radioButton1.setText(_translate("Dialog", "Image Mixing"))
        self.radioButton2.setText(_translate("Dialog", "Face Morphing"))
        self.radioButton3.setText(_translate("Dialog", "Image Restoration"))
        self.pushButton_2.setText(_translate("Dialog", "Insert"))
        self.pushButton_3.setText(_translate("Dialog", "Generate Image"))
        self.pushButton.setText(_translate("Dialog", "Exit"))
        self.label.setText(_translate("Dialog", "Generated Image: "))
        self.label_2.setText(_translate("Dialog", "                               No Image"))
        self.label_3.setText(_translate("Dialog", "                               No Image"))
        self.label_4.setText(_translate("Dialog", "Image 1: "))
        self.label_5.setText(_translate("Dialog", "                               No Image"))
        self.label_6.setText(_translate("Dialog", "Image 2: "))
