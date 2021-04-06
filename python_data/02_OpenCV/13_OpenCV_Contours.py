'''
# Contour의 사각형 외곽 찾기
cv2.boundingRect(contour) Contour를 포함하는 사각형을 그립니다.
사각형의 X, Y 좌표와 너비, 높이를 반환합니다.

# Contour의 Convex Hull
cv2.convexHull(contour) Convex Hull 알고리즘으로 외곽을 구하는 함수
대략적인 형태의 Contour 외곽을 빠르게 구할 수 있습니다. (단일 Contour 반환)

# Contour의 유사 다각형 구하기
cv2.approxPolyDP(curve, epsilon, closed) 근사치 Contour를 구합니다.
- curve: Contour
- epsilon: 최대 거리 (클수록 Point 개수 감소)
- closed: 폐곡선 여부

# Contour의 기본 정보
cv2.contourArea(contour) Contour의 면적을 구합니다.
cv2.arcLength(contour) Contour의 둘레를 구합니다.
cv2.moments(contour) Contour의 특징을 추출합니다.
'''
import cv2

image = cv2.imread('digit_image.png')

# gray scale threshhold 처리
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(image_gray, 230, 255, 0)  # 배경 화이트, 글자 블랙
thresh = cv2.bitwise_not(thresh)  # 흑백 반전
cv2.imshow('Image', thresh)
cv2.waitKey(0)

contours, hierarchy = cv2.findContours(
    thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
image = cv2.drawContours(image, contours, -1, (0, 0, 255), 4)  # 빨간색 윤곽선
cv2.imshow('Image', image)
cv2.waitKey(0)

contour = contours[0]  # 윤곽 구분해 둔 것 중 첫번째 것

# 사각형 외곽 찾기
x, y, w, h = cv2.boundingRect(contour)
image = cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 3)
cv2.imshow('Image', image)
cv2.waitKey(0)

# Convex Hull - 다각형
hull = cv2.convexHull(contour)
image = cv2.drawContours(image, [hull], -1, (255, 0, 0), 4)
cv2.imshow('Image', image)
cv2.waitKey(0)

# 유사 다각형 구하기
epsilon = 0.01 * cv2.arcLength(contour, True)
approx = cv2.approxPolyDP(contour, epsilon, True)
image = cv2.drawContours(image, [approx], -1, (0, 255, 0), 4)
cv2.imshow('Image', image)
cv2.waitKey(0)

# Contour의 기본 정보
area = cv2.contourArea(contour)
print(area)
length = cv2.arcLength(contour, True)
print(length)
M = cv2.moments(contour)
print(M)
