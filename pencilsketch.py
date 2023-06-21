import cv2
cv2.namedWindow("output",cv2.WINDOW_NORMAL)
image = cv2.imread("image.jpg",1)
cv2.imshow("output",image)
cv2.waitKey(0)

cv2.namedWindow("output2",cv2.WINDOW_NORMAL)
gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("output2",gray_image)
cv2.waitKey(0)


cv2.namedWindow("output3",cv2.WINDOW_NORMAL)
inverted_image=255-gray_image 
cv2.imshow("output3",gray_image)
cv2.waitKey(0)


cv2.namedWindow("output4",cv2.WINDOW_NORMAL)
blurred = cv2.GaussianBlur(inverted_image,(21,21),0)
cv2.imshow("output4",blurred)
cv2.waitKey(0)

cv2.namedWindow("output5",cv2.WINDOW_NORMAL)
inverted_blurred=255-blurred 
cv2.imshow("output5",inverted_blurred)
cv2.waitKey(0)

cv2.namedWindow("output6",cv2.WINDOW_NORMAL)
pencil_sketch=cv2.divide(gray_image,inverted_blurred,scale=256.0)
cv2.imshow("output6",pencil_sketch)
cv2.waitKey(0)
