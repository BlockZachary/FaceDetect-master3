# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow1.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!
import sys
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.Qt import *


class Ui_MainWindow(object):


    # 加载haar分类器的xml文件路径
    cascPath = "haarcascade_frontalface_default.xml"

    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(cascPath)  # 创建haar级联并使用面部级联对其进行初始化，
    # 这会将面部级联加载到内存中，以便使用，
    # 级联只是一个XML文件，其中包含用于检测人脸的数据
    # 显示信息字体
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL

    # 创建识别器对象,并读取训练好的识别yml文件
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')

    # 初始化人物id及其姓名列表
    id = 0
    names = ['None', 'Alice', 'Curry']

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Face-detect-recog")
        MainWindow.resize(990, 626)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(750, 110, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(750, 170, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(750, 230, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 40, 601, 511))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 990, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Face-detect-recog"))
        self.pushButton.setText(_translate("MainWindow", "选择图片"))
        self.pushButton_2.setText(_translate("MainWindow", "人脸检测"))
        self.pushButton_3.setText(_translate("MainWindow", "人脸识别"))
        self.label.setText(_translate("MainWindow", "                                 显示图片"))
        self.pushButton.clicked.connect(self.openimage)
        self.pushButton_2.clicked.connect(self.detect_face)
        self.pushButton_3.clicked.connect(self.recognize_face)

    def openimage(self):
        imgName, imgType = QFileDialog.getOpenFileName(None, "打开图片", "./", "Image Files(*.jpg *.png)")
        jpg = QtGui.QPixmap(imgName)
        self.label.setPixmap(jpg)
        self.imagePath = imgName


    def detect_face(self):

        # Read the image
        image = cv2.imread(self.imagePath[-7:])
        temp = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)  # COLOR_BGR2RGBA
        gray = cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)  # 读取图像并转化为灰度
        # Detect faces in the image
        faces = self.faceCascade.detectMultiScale(  # 面部级联检测
            gray,  # 灰度图像
            scaleFactor=1.1,  # 比例因子对图像进行补偿
            minNeighbors=5,  # 定义在当前对象前检测到多少对象
            minSize=(30, 30),  # 给出每个窗口的最小值
        )
        print("Found {0} faces!".format(len(faces)))
        # Draw a rectangle around the faces and recognize and sign
        for (x, y, w, h) in faces:  # 在检测到的面部周围画框
            cv2.rectangle(image, (x, y), (x + w, y + h), (237, 149, 100), 2)
        img2 = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # opencv读取的bgr格式图片转换成rgb格式
        _image = QtGui.QImage(img2[:], img2.shape[1], img2.shape[0], img2.shape[1] * 3, QtGui.QImage.Format_RGB888)  # pyqt5转换成自己能放的图片格式
        jpg_out = QtGui.QPixmap(_image)
        self.label.setPixmap(jpg_out)  # 设置图片显示



    def recognize_face(self):
        image = cv2.imread(self.imagePath[-7:])
        temp = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)  # COLOR_BGR2RGBA
        gray = cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)  # 读取图像并转化为灰度
        faces = self.faceCascade.detectMultiScale(  # 面部级联检测
            gray,  # 灰度图像
            scaleFactor=1.1,  # 比例因子对图像进行补偿
            minNeighbors=5,  # 定义在当前对象前检测到多少对象
            minSize=(30, 30),  # 给出每个窗口的最小值
        )
        for (x, y, w, h) in faces:  # 在检测到的面部周围画框
            cv2.rectangle(image, (x, y), (x + w, y + h), (237, 149, 100), 2)
            id, confidence = self.recognizer.predict(gray[y:y + h, x:x + w])

            # Check if confidence is less them 100 ==> "0" is perfect match
            if (confidence < 100):
                id = self.names[id]
                confidence = "  {0}%".format(round(100 - confidence))
                cv2.putText(image, str(id), (x + 5, y - 5), self.font, 1, (255, 255, 255), 1)
                cv2.putText(image, str(confidence), (x + 5, y + h + 15), self.font, 1, (255, 255, 0), 1)
            else:
                id = "unknown"
                # confidence = "  {0}%".format(round(100 - confidence))
                cv2.putText(image, str(id), (x - w + 15, y - 5), self.font, 1, (255, 0, 255), 1)
        img2 = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # opencv读取的bgr格式图片转换成rgb格式
        _image = QtGui.QImage(img2[:], img2.shape[1], img2.shape[0], img2.shape[1] * 3, QtGui.QImage.Format_RGB888)  # pyqt5转换成自己能放的图片格式
        jpg_out = QtGui.QPixmap(_image)
        self.label.setPixmap(jpg_out)  # 设置图片显示


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # 创建一个QApplication，也就是你要开发的软件app
    MainWindow = QtWidgets.QMainWindow()    # 创建一个QMainWindow，用来装载你需要的各种组件、控件
    ui = Ui_MainWindow()                    # ui是Ui_MainWindow()类的实例化对象
    ui.setupUi(MainWindow)                  # 执行类中的setupUi方法，方法的参数是第二步中创建的QMainWindow
    MainWindow.show()                       # 执行QMainWindow的show()方法，显示这个QMainWindow
    sys.exit(app.exec_())                   # 使用exit()或者点击关闭按钮退出QApplication

