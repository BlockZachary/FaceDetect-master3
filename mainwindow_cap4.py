# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow_cap3.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!
import os
import sys
import cv2
import time
import numpy as np
from PIL import Image
from PyQt5.QtCore import QTimer, Qt, QThread, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets


#线程类
class Thread_click(QThread):
    _signal = pyqtSignal(int)

    def __init__(self):
        super(Thread_click, self).__init__()

    def run(self):
        self._signal.emit(1)
        time.sleep(1)


class Ui_MainWindow(object):

    # 加载haar分类器的xml文件路径
    cascPath = "haarcascade_frontalface_default.xml"

    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(cascPath)  # 创建haar级联并使用面部级联对其进行初始化，
    # 这会将面部级联加载到内存中，以便使用，
    # 级联只是一个XML文件，其中包含用于检测人脸的数据
    # 显示信息字体
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL

    path = 'dataset'
    capture_path = "capture.png"

    # 创建识别器对象,并读取训练好的识别yml文件
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')

    # 初始化人物id及其姓名列表
    id = 0
    names = ['None', 'Alice', 'Curry', 'zachary', 'Tom']

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Face-detect-recog")
        MainWindow.resize(1032, 602)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(890, 280, 93, 28))
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
        self.lineEdit.setGeometry(QtCore.QRect(890, 160, 91, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(890, 190, 72, 15))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(890, 250, 72, 15))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(890, 220, 91, 31))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Face-detect-recog"))
        self.pushButton.setText(_translate("MainWindow", "获取数据"))
        self.pushButton_2.setText(_translate("MainWindow", "训练"))
        self.pushButton_3.setText(_translate("MainWindow", "拍摄图片"))
        self.pushButton_4.setText(_translate("MainWindow", "人脸检测"))
        self.label.setText(_translate("MainWindow", "显示"))
        self.pushButton_5.setText(_translate("MainWindow", "人脸识别"))
        self.label_2.setText(_translate("MainWindow", "User id"))
        self.label_3.setText(_translate("MainWindow", "Name"))
        self.pushButton_6.setText(_translate("MainWindow", "打开摄像头"))

        # 刷新摄像头的显示时间，实时显示
        self.timer = QTimer()
        self.timer.start()
        self.timer.setInterval(100)

        self.textBrowser.setText("[INFO] 请选择操作")

        # 点击pushButton_6 打开摄像头 显示在label标签上 先调用 cap_start()以实现摄像头刷新
        self.pushButton_6.clicked.connect(self.pushbutton6_clicked)

        # 先打开摄像头 在label_2 label_3 输入User_id和Name 点击pushButton 获取30张摄像头前人脸图像 保存于dataset文件夹中
        self.pushButton.clicked.connect(self.pushbutton_clicked)

        # 点击pushButton2 训练当前的数据集图像信息生成yml文件
        self.pushButton_2.clicked.connect(self.pushbutton2_clicked)

        # 点击pushButton_3 拍摄图片
        self.pushButton_3.clicked.connect(self.pushbutton3_clicked)

        # 点击pushButton_4 人脸检测
        self.pushButton_4.clicked.connect(self.pushbutton4_clicked)

        # 点击pushButton_5 人脸识别
        self.pushButton_5.clicked.connect(self.pushbutton5_clicked)



# 通过timer调用打开摄像头 实现连续摄像
    def pushbutton6_clicked(self):
        self.th6 = Thread_click()
        self.th6._signal.connect(self.cap_start)
        self.th6.start()
    def cap_start(self):
        self.cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        self.cam.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
        self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)
        self.cam.set(cv2.CAP_PROP_FPS, 20)
        self.timer.timeout.connect(self.open_cap)

# 从cap_start处 调用打开摄像头
    def open_cap(self):
        if (self.cam.isOpened()):
            # 获取单帧
            ret, self.img = self.cam.read()
            self.img_temp = cv2.flip(self.img, 1)  # 水平翻转
            # img = cv2.flip(img, -1)     #水平垂直翻转
            height, width, bytesPerComponent = self.img_temp.shape
            bytesPerLine = bytesPerComponent * width
            # 变换彩色空间顺序
            self.img_temp = cv2.cvtColor(self.img_temp, cv2.COLOR_BGR2RGB)
            # 转为QImage对象
            self.image = QImage(self.img_temp.data, width, height, bytesPerLine, QImage.Format_RGB888)
            self.label.setPixmap(QPixmap.fromImage(self.image))


# 获取训练数据
    def pushbutton_clicked(self):
        self.th = Thread_click()
        self.th._signal.connect(self.acquire_data)
        self.th.start()
    def acquire_data(self):
        self.User_id = self.lineEdit.text()
        self.Name = self.lineEdit_2.text()
        # 将id[]中的新数据更新了
        int_id = int(self.User_id)
        self.names[int_id] = self.Name
        print(self.names)

        if self.cam.isOpened():
            self.cam.release()
            self.label.setText(" ")

        cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        cam.set(3, 640)  # set video width
        cam.set(4, 480)  # set video height
        count = 0

        while (True):
            ret, img = cam.read()
            img = cv2.flip(img, 1)  # 水平翻转
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = self.faceCascade.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), ( 255, 0, 0), 2)
                count += 1
                # Save the captured image into the datasets folder
                cv2.imwrite("dataset/User." + str(self.User_id) + '.' + str(count) + ".jpg", gray[y:y + h, x:x + w])
                img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # opencv读取的bgr格式图片转换成rgb格式
                _image = QtGui.QImage(img2[:], img2.shape[1], img2.shape[0], img2.shape[1] * 3,
                                      QtGui.QImage.Format_RGB888)  # pyqt5转换成自己能放的图片格式
                jpg_out = QtGui.QPixmap(_image)
                self.label.setPixmap(jpg_out)  # 设置图片显示

            k = cv2.waitKey(100) & 0xff  # Press 'ESC' for exiting video
            if k == 27:
                break
            elif count >= 30:  # Take 30 face sample and stop video
                break
        self.textBrowser.clear()
        self.textBrowser.setText("[INFO] 数据捕获完成")
        time.sleep(2)
        self.label.setText(" ")


        # self.cap_start()


# 训练数据——生成yml
    def pushbutton2_clicked(self):
        self.th2 = Thread_click()
        self.th2._signal.connect(self.train_data)
        self.th2.start()
    def train_data(self):
        self.textBrowser.setText("[INFO] 训练数据中 请稍后...")
        # print("\n [INFO] Training faces. It will take a few seconds. Wait ...")
        imagePaths = [os.path.join(self.path, f) for f in os.listdir(self.path)]
        faceSamples = []
        ids = []
        for imagePath in imagePaths:
            PIL_img = Image.open(imagePath).convert('L')  # convert it to grayscale
            img_numpy = np.array(PIL_img, 'uint8')
            id = int(os.path.split(imagePath)[-1].split(".")[1])
            faces = self.faceCascade.detectMultiScale(img_numpy)
            for (x, y, w, h) in faces:
                faceSamples.append(img_numpy[y:y + h, x:x + w])
                ids.append(id)

        self.recognizer.train(faceSamples, np.array(ids))

        # 保存训练模型到 trainer/trainer.yml
        self.recognizer.write('trainer/trainer.yml')  # recognizer.save() worked on Mac, but not on Pi

        # 打印训练的人脸数目
        self.textBrowser.setText("[INFO] 训练结束，获得{0}个面部数据".format(len(np.unique(ids))))
        # print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))


#定义拍照方法
    def capmethod(self):
        self.cam.release()
        self.label.setText(" ")

        cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        cam.set(3, 800)  # set video width
        cam.set(4, 600)  # set video height
        ret, self.img = cam.read()
        self.img = cv2.flip(self.img, 1)  # 水平翻转
        img2 = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)  # opencv读取的bgr格式图片转换成rgb格式
        _image = QtGui.QImage(img2[:], img2.shape[1], img2.shape[0], img2.shape[1] * 3,
                              QtGui.QImage.Format_RGB888)  # pyqt5转换成自己能放的图片格式
        jpg_out = QtGui.QPixmap(_image)
        self.label.setPixmap(jpg_out)  # 设置图片显示


    def pushbutton3_clicked(self):
        self.th3 = Thread_click()
        self.th3._signal.connect(self.capture_ph)
        self.th3.start()
    def capture_ph(self):  # 拍摄待检测或识别图像
        self.textBrowser.setText("[INFO] 请等待拍摄图像...")
        self.cap_start()
        if self.cam.isOpened():
            self.capmethod()
            cv2.imwrite(self.capture_path, self.img)

        return


# 人脸检测
    def pushbutton4_clicked(self):
        self.th4 = Thread_click()
        self.th4._signal.connect(self.face_detect)
        self.th4.start()
    def face_detect(self):
        # Read the image
        self.textBrowser.setText("[INFO] 人脸检测")
        image = cv2.imread(self.capture_path)
        temp = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)  # COLOR_BGR2RGBA
        gray = cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)  # 读取图像并转化为灰度
        # Detect faces in the image
        faces = self.faceCascade.detectMultiScale(  # 面部级联检测
            gray,  # 灰度图像
            scaleFactor=1.1,  # 比例因子对图像进行补偿
            minNeighbors=5,  # 定义在当前对象前检测到多少对象
            minSize=(30, 30),  # 给出每个窗口的最小值
        )
        self.textBrowser.setText("Found {0} faces!".format(len(faces)))
        # Draw a rectangle around the faces and recognize and sign
        for (x, y, w, h) in faces:  # 在检测到的面部周围画框
            cv2.rectangle(image, (x, y), (x + w, y + h), (237, 149, 100), 2)
        img2 = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # opencv读取的bgr格式图片转换成rgb格式
        _image = QtGui.QImage(img2[:], img2.shape[1], img2.shape[0], img2.shape[1] * 3,
                              QtGui.QImage.Format_RGB888)  # pyqt5转换成自己能放的图片格式
        jpg_out = QtGui.QPixmap(_image)
        self.label.setPixmap(jpg_out)  # 设置图片显示
        return


# 人脸识别
    def pushbutton5_clicked(self):
        self.th5 = Thread_click()
        self.th5._signal.connect(self.face_recognize)
        self.th5.start()
    def face_recognize(self):
        self.textBrowser.setText("[INFO] 人脸识别")
        image = cv2.imread(self.capture_path)
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
        _image = QtGui.QImage(img2[:], img2.shape[1], img2.shape[0], img2.shape[1] * 3,
                              QtGui.QImage.Format_RGB888)  # pyqt5转换成自己能放的图片格式
        jpg_out = QtGui.QPixmap(_image)
        self.label.setPixmap(jpg_out)  # 设置图片显示
        return


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # 创建一个QApplication，也就是你要开发的软件app
    MainWindow = QtWidgets.QMainWindow()  # 创建一个QMainWindow，用来装载你需要的各种组件、控件
    ui = Ui_MainWindow()  # ui是Ui_MainWindow()类的实例化对象
    ui.setupUi(MainWindow)  # 执行类中的setupUi方法，方法的参数是第二步中创建的QMainWindow
    MainWindow.show()  # 执行QMainWindow的show()方法，显示这个QMainWindow
    sys.exit(app.exec_())  # 使用exit()或者点击关闭按钮退出QApplication
