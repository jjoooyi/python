import cv2

# ROI(Range of Interest, 관심부분) 추출 및 복사
image = cv2.imread('python_data/test.png')

# Numpy Slicing: ROI 처리 가능
logo = image[60:190, 270:400]
cv2.imshow('Image', logo)
cv2.waitKey(0)

# ROI 단위로 이미지 복사하기
image[0:130, 0:130] = logo
cv2.imshow('Image', image)
cv2.waitKey(0)


# 픽셀별로 색상 다루기
# 특정 색상만 보여주기(0: Blue, 1: Green, 2: Red)
cv2.imshow('Image', image[:, :, 0])  # 전체 픽셀에서 Blue 값만 추출하여 보여주기??
cv2.waitKey(0)

# 특정 색상만 제거하기
image[:, :, 2] = 0
cv2.imshow('Image', image)
cv2.waitKey(0)
