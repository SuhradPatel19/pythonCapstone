import cv2

image=cv2.imread("images/boy.jpg")
greyImage=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
invertedImage=255-greyImage
bluredImage=cv2.GaussianBlur(invertedImage,(21,21),0)

bluredInverted=255-bluredImage
pencilSketch=cv2.divide(greyImage,bluredInverted,scale=255)

cv2.imshow("Orignal Image: ", image)
cv2.imshow("Grey Image: ", greyImage)
cv2.imshow("Inverted Image: ", invertedImage)
cv2.imshow("Blured Image: ", bluredImage)
cv2.imshow("Blured Image Inverted: ", bluredInverted)
cv2.imshow("Pencil Sketch Image: ", pencilSketch)
cv2.waitKey(0)
