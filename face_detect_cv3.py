import cv2

# Get user supplied values

#获取图片路径
#imagePath = "ph1.png"
#imagePath = "ph2.png"
#imagePath ="ph3.png"
imagePath ="ph4.png"
cascPath = "haarcascade_frontalface_default.xml"       #加载haar分类器的xml文件

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)     #创建haar级联并使用面部级联对其进行初始化，
                                                  #这会将面部级联加载到内存中，以便使用，
                                                  #级联只是一个XML文件，其中包含用于检测人脸的数据

# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)     #读取图像并转化为灰度
#cv2.imshow("Faces", gray)

# Detect faces in the image
faces = faceCascade.detectMultiScale(    #面部级联检测
    gray,               #灰度图像
    scaleFactor=1.1,    #比例因子对图像进行补偿
    minNeighbors=5,     #定义在当前对象前检测到多少对象
    minSize=(30, 30),    #给出每个窗口的最小值
)
print("Found {0} faces!".format(len(faces)))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:           #在检测到的面部周围画框
    cv2.rectangle(image, (x, y), (x+w, y+h), (0,255,0), 2)

cv2.imshow("Faces found", image)    #展示结果
cv2.waitKey(0)
