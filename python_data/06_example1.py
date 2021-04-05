import cv2
import time

image = cv2.imread('python_data/test.png')

# 픽셀 수 및 이미지 크기 확인
print(image.shape)
print(image.size)

# 이미지 Numpy 객체의 특정 픽셀 가리키기 => [B G R] 행렬 값 추출
px = image[100, 100]

# B, G, R 순서로 출력
# Gray Scale: B, G, R로 구분되지 않음
print(px)

# R 값만 출력하기
print(px[2])


# 특정 범위 픽셀 변경
# 방법1) 하나하나 값을 변경해주기 때문에 속도 느림
start_time = time.time()
for i in range(0, 100):
    for j in range(0, 100):
        image[i, j] = [255, 255, 255]
print('--- %s seconds ---' % (time.time() - start_time))
# --------------------------------------------------------
# 방법2) 빠름, 슬라이싱 연산 사용
start_time = time.time()
image[0:100, 0:100] = [0, 0, 0]
print('--- %s seconds ---' % (time.time() - start_time))
# --------------------------------------------------------

cv2.imshow('Image', image)
cv2.waitKey(0)
