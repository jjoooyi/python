import cv2

# 이미지의 적응 임계점 처리
# cv2.adaptiveThreshold(image, max_value, adaptive_method, type, block_size, C) 적응 임계점 처리 함수
# max_value: 임계 값을 넘었을 때 적용할 값
# adaptive_method: 임계 값을 결정하는 계산 방법
# ADAPTIVE_THRESH_MEAN_C: 주변영역의 평균값으로 결정
#   적용할 픽셀 (x, y)를 중심으로 하는 Block Size * Block Size 안에 있는 픽셀 값의 평균에서 C를 뺀 값을 임계점으로 설정
# ADAPTIVE_THRESH_GAUSSIAN_C
#   - 적용할 픽셀 (x, y)를 중심으로 하는 Block Size * Block Size 안에 있는 Gaussian 윈도우 기반의 가중치들의 합에서 C를 뺀 값을 임계점으로 설정
# type: 임계점을 처리하는 방식, block_size: 임계 값을 적용할 영역의 크기, C: 평균이나 가중 평균에서 차감할 값
# Adaptive Threshold를 이용하면, 전체 픽셀을 기준으로 임계 값을 적용하지 않습니다.

image = cv2.imread('hand_writing_image.jpg', cv2.IMREAD_GRAYSCALE)

thres1 = cv2.adaptiveThreshold(
    image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 3)
thres2 = cv2.adaptiveThreshold(
    image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 3)

cv2.imshow('Image', image)
cv2.waitKey(0)

cv2.imshow('Image', thres1)
cv2.waitKey(0)

cv2.imshow('Image', thres2)
cv2.waitKey(0)
