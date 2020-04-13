# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow_cap2.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!
import sys
from threading import Thread

import cv2
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QImage, QPixmap


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
    names = ['None', 'Alice', 'Curry', 'Ilza', 'Z', 'W']


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1032, 602)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(890, 160, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(890, 330, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(890, 380, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(890, 430, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 10, 961, 61))
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 90, 771, 461))
        self.label.setObjectName("label")
        self.label.setAlignment(Qt.AlignCenter)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(890, 480, 93, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(890, 210, 91, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(890, 240, 72, 15))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(890, 300, 72, 15))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(890, 270, 91, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(890, 110, 93, 28))
        self.pushButton_6.setObjectName("pushButton_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1032, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "获取数据"))
        self.pushButton_2.setText(_translate("MainWindow", "训练"))
        self.pushButton_3.setText(_translate("MainWindow", "拍摄图片"))
        self.pushButton_4.setText(_translate("MainWindow", "人脸检测"))
        # self.label.setText(_translate("MainWindow", "                                              显示"))
        self.label.setText(_translate("MainWindow", "显示"))
        self.pushButton_5.setText(_translate("MainWindow", "人脸识别"))
        self.label_2.setText(_translate("MainWindow", "User id"))
        self.label_3.setText(_translate("MainWindow", "Name"))
        self.pushButton_6.setText(_translate("MainWindow", "打开摄像头"))

        # 刷新摄像头的显示时间，实时显示
        self.timer = QTimer()
        self.timer.start()
        self.timer.setInterval(100)

        # 点击pushButton_6 打开摄像头 显示在label标签上 先调用 cap_start()以实现摄像头刷新
        self.pushButton_6.clicked.connect(self.cap_start)

        # 先打开摄像头 在label_2 label_3 输入User_id和Name 点击pushButton 获取30张摄像头前人脸图像 保存于dataset文件夹中

        # 点击pushButton2 训练当前的数据集图像信息生成yml文件

        # 点击pushButton_3 拍摄图片

        # 点击pushButton_4 人脸检测

        # 点击pushButton_5 人脸识别

    def cap_start(self):       # 通过timer调用打开摄像头 实现连续摄像
        self.cam = cv2.VideoCapture(0)
        self.cam.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
        self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)
        self.cam.set(cv2.CAP_PROP_FPS, 20)
        self.timer.timeout.connect(self.open_cap)


    def open_cap(self):        # 从cap_start处 调用打开摄像头
        if (self.cam.isOpened()):
            # 获取单帧
            ret, img = self.cam.read()
            img = cv2.flip(img, 1)        #水平翻转
            # img = cv2.flip(img, -1)     #水平垂直翻转
            height, width, bytesPerComponent = img.shape
            bytesPerLine = bytesPerComponent * width
            # 变换彩色空间顺序
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            # 转为QImage对象
            self.image = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
            self.label.setPixmap(QPixmap.fromImage(self.image))


    def acquire_data(self):    # 获取训练数据

        return

    def train_data(self):      # 训练数据——生成yml
        return

    def capture_ph(self):      # 拍摄待检测或识别图像
        return

    def face_detect(self):     # 人脸检测
        return

    def face_recognize(self):  # 人脸识别
        return


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # 创建一个QApplication，也就是你要开发的软件app
    MainWindow = QtWidgets.QMainWindow()  # 创建一个QMainWindow，用来装载你需要的各种组件、控件
    ui = Ui_MainWindow()  # ui是Ui_MainWindow()类的实例化对象
    ui.setupUi(MainWindow)  # 执行类中的setupUi方法，方法的参数是第二步中创建的QMainWindow
    MainWindow.show()  # 执行QMainWindow的show()方法，显示这个QMainWindow
    sys.exit(app.exec_())  # 使用exit()或者点击关闭按钮退出QApplication


