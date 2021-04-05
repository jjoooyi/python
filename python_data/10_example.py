import cv2
import numpy as np

# cv2.createTrackbar(track_bar_name, window_name, value, count, on_change) Tracker를 생성하는 함수
# value: 초깃값, count: Max 값(Min: 0), on_change: 값이 변경될 때 호출되는 Callback 함수

# cv2.getTrackerPos(track_bar_name, window_name) Tracker로부터 값을 얻어 오는 함수


def change_color(x):
    r = cv2.getTrackbarPos('R', 'Image')
    g = cv2.getTrackbarPos('G', 'Image')
    b = cv2.getTrackbarPos('B', 'Image')
    image[:] = [b, g, r]
    cv2.imshow('Image', image)


image = np.zeros((600, 400, 3), np.uint8)  # numpy로 3가지 색이 사용되는 이미지 생성
cv2.namedWindow("Image")

cv2.createTrackbar('R', 'Image', 0, 255, change_color)
cv2.createTrackbar('G', 'Image', 0, 255, change_color)
cv2.createTrackbar('B', 'Image', 0, 255, change_color)

cv2.imshow('Image', image)
cv2.waitKey(0)
