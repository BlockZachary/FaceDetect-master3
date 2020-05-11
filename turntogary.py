#Author： Zachary
import cv2


img = cv2.imread("ph2.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("ph2_gray.png",gray)


cv2.destroyAllWindows()