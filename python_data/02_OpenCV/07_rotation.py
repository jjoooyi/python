import cv2

# 이미지 회전
# cv2.getRotationMatrix2D(center, angle, scale) | 이미지 회전을 위한 변환 행렬을 생성합니다.
# center: 회전 중심, angle: 회전 각도, scale: Scale Factor

image = cv2.imread('python_data/test.png')

# 행과 열 정보만 저장
height, width = image.shape[:2]

M = cv2.getRotationMatrix2D((width/2, height/2), 90, 0.5)
dst = cv2.warpAffine(image, M, (width, height))
cv2.imshow('Image', dst)
cv2.waitKey(0)
