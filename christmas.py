import cv2

image = cv2.imread("image-2.jpg")
grey_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey_img)

blur = cv2.GaussianBlur(invert,(21,21),0)
invertedblur = cv2.bitwise_not(blur)

sketh = cv2.divide(grey_img,invertedblur,scale=256.0)

cv2.imwrite("newimage-2.png",sketh)