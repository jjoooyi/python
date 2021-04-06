'''
OpenCV Filtering

# 필터링
• 이미지에 커널을 적용하여 이미지를 흐리게(Blurring = Smoothing) 처리할 수 있습니다.
• 이미지를 흐리게 만들면 노이즈 및 손상을 줄일 수 있습니다

# 컨볼루션 계산
• 특정한 이미지에서 커널(Kernel)을 적용해 컨볼루션 계산하여 필터링을 수행할 수 있습니다.

- Basic Kernel / Gaussian Kernel
'''

import cv2
import numpy as np

image = cv2.imread('gray_image.jpg')
cv2.imshow('Image', image)
cv2.waitKey(0)

# Basic Kernel, 직접 커널을 생성하여 필터 적용
# 1/16 으로 이루어진 4*4 행렬
size = 4
kernel = np.ones((size, size), np.float32) / (size ** 2)
print(kernel)

dst = cv2.filter2D(image, -1, kernel)
cv2.imshow('Image', dst)
cv2.waitKey(0)

# Basic Blur
dst = cv2.blur(image, (4, 4))
cv2.imshow('Image', dst)
cv2.waitKey(0)

# Gaussian Blur, kernel_size 홀수여야한다!
dst = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow('Image', dst)
cv2.waitKey(0)
