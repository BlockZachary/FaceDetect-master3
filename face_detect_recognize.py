#Author： Zachary
import cv2

# Get user supplied values

#获取图片路径
#imagePath = "ph1.png"
imagePath = "ph2.png"
#imagePath ="ph3.png"
#imagePath ="ph4.png"
#imagePath = "ph5.png"

#加载haar分类器的xml文件路径
cascPath = "haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)     #创建haar级联并使用面部级联对其进行初始化，
                                                  #这会将面部级联加载到内存中，以便使用，
                                                  #级联只是一个XML文件，其中包含用于检测人脸的数据

#显示信息字体
font = cv2.FONT_HERSHEY_COMPLEX_SMALL

#创建识别器对象,并读取训练好的识别yml文件
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')

#初始化人物id及其姓名列表
id = 0
names = ['None', 'Alice', 'Curry', 'Zanba', 'Haili', 'Wang']

# Read the image
image = cv2.imread(imagePath)
temp = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)             #COLOR_BGR2RGBA
gray = cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)     #读取图像并转化为灰度

#cv2.imshow("gray",gray)


# Detect faces in the image
faces = faceCascade.detectMultiScale(    #面部级联检测
    gray,               #灰度图像
    scaleFactor=1.1,    #比例因子对图像进行补偿
    minNeighbors=5,     #定义在当前对象前检测到多少对象
    minSize=(30, 30),    #给出每个窗口的最小值
)
print("Found {0} faces!".format(len(faces)))

# Draw a rectangle around the faces and recognize and sign
for (x, y, w, h) in faces:           #在检测到的面部周围画框
    cv2.rectangle(image, (x, y), (x+w, y+h), (237, 149, 100), 2)
    id, confidence = recognizer.predict(gray[y:y + h, x:x + w])

    # Check if confidence is less them 100 ==> "0" is perfect match
    if (confidence < 100):
        id = names[id]
        confidence = "  {0}%".format(round(100 - confidence))
        cv2.putText(image, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 1)
        cv2.putText(image, str(confidence), (x + 5, y + h + 15), font, 1, (255, 255, 0), 1)
    else:
        id = "unknown"
        #confidence = "  {0}%".format(round(100 - confidence))
        cv2.putText(image, str(id), (x - w + 15 , y - 5), font, 1, (255, 0, 255), 1)




#展示结果
cv2.imshow("Faces result", image)
cv2.waitKey(0)