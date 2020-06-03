运行代码如:
face_detect_cv3+YCbCr.py 改变图片路径 可以查看不同人脸检测的效果

mainwindow等.py 是带有GUI界面的人脸检测及识别的，基于PyQt5开发！
目前主要完成的部分有：mainwindow1.py 可以实现从当前文件夹下寻找图片并展示在界面上，实现人脸检测和已训练人脸的识别！
		      mainwindow_cap3.py 可以实现 界面的人脸数据捕获 后续功能仍然在完成中。
		      mainwindow_cap4.py 再移植上一代码到树莓派后 发现有明显的卡顿 为了获取到较为流畅的视频加入多线程编程。


cascade.xml 是自己训练的8层强分类器级联起来的分类器，效果不明显！
              mainwindow_cap5.py 加载了自己训练了cascade.xml

