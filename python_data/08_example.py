import cv2

image_1 = cv2.imread('image_1.jpg')
image_2 = cv2.imread('image_2.png')

result = cv2.add(image_1, image_2)
cv2.imshow('Image', result)
cv2.waitKey(0)

result = image_1 + image_2
cv2.imshow('Image', result)
cv2.waitKey(0)
