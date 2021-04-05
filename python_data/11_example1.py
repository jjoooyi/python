import cv2
import numpy as np

# 직선그리기
# cv2.circle(image, center, radian, color, thickness) 하나의 원을 그리는 함수
image = np.full((512, 512, 3), 255, np.uint8)  # 255로 값 초기화
image = cv2.line(image, (0, 0), (255, 255), (255, 0, 0), 3)

cv2.imshow('Image', image)
cv2.waitKey(0)


# 사각형그리기
# cv2.rectangle(image, start, end, color, thickness) 하나의 사각형을 그리는 함수
image = np.full((512, 512, 3), 255, np.uint8)  # 255로 값 초기화
image = cv2.rectangle(image, (20, 20), (255, 255), (255, 0, 0), 3)

cv2.imshow('Image', image)
cv2.waitKey(0)


# 원그리기
# cv2.circle(image, center, radian, color, thickness) 하나의 원을 그리는 함수
image = np.full((512, 512, 3), 255, np.uint8)
image = cv2.circle(image, (255, 255), 30, (255, 0, 0), 3)

cv2.imshow('Image', image)
cv2.waitKey(0)


# 다각형그리기
# cv2.polylines(image, points, is_closed, color, thickness) 하나의 다각형을 그리는 함수
image = np.full((512, 512, 3), 255, np.uint8)
points = np.array([[5, 5], [128, 258], [483, 444], [400, 150]])
image = cv2.polylines(image, [points], True, (0, 0, 255), 4)

cv2.imshow('Image', image)
cv2.waitKey(0)


# 텍스트그리기
# cv2.putText(image, text, position, font_type, font_scale, color) 하나의 텍스트를 그리는 함수
image = np.full((512, 512, 3), 255, np.uint8)
image = cv2.putText(image, 'Hello World', (0, 200),
                    cv2.FONT_ITALIC, 2, (255, 0, 0))

cv2.imshow('Image', image)
cv2.waitKey(0)
