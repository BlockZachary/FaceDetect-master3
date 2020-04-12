#Author： Zachary

import cv2


face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# For each person, enter one numeric face id
face_id = input('\n enter user id end press <return> ==>  ')
# Initialize individual sampling face count
count = input('\n enter count number end press <return> ==>  ')


img = cv2.imread("Curry/30.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_detector.detectMultiScale(gray, 1.3, 5)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Save the captured image into the datasets folder
    cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y + h, x:x + w])

    cv2.imshow('image', img)

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")

cv2.destroyAllWindows()