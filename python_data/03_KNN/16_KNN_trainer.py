import cv2
import numpy as np

img = cv2.imread('digits.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 세로로 50줄, 가로로 100줄로 사진을 나눕니다.
# => 숫자 하나하나 씩 분리(20px X 20px)
cells = [np.hsplit(row, 100) for row in np.vsplit(gray, 50)]
x = np.array(cells)
print(x.shape)  # (50, 100, 20, 20) 세로 50개, 가로 100개, 20x20사이즈

# 각 (20X20) 크기의 사진을 한 줄 (1X400)으로 바꿉니다. 전체(-1)를 400 길이로 나열
train = x[:, :].reshape(-1, 400).astype(np.float32)
print(train.shape)  # (5000, 400) 5000개의 이미지가 400크기로 저장

# 0이 500개, 1이 500개 ... 로 총 5,000 개가 들어가는 (1X5000) 배열을 만듭니다.
k = np.arange(10)
train_labels = np.repeat(k, 500)[:, np.newaxis]
print(train_labels.shape)  # (5000, 1) 5000개, 0~9중 어떤 값인지 정보 1개 저장

np.savez('trained.npz', train=train, train_labels=train_labels)

print(x[0, 5].shape)

# 다음과 같이 하나씩 글자를 출력할 수 있습니다.
cv2.imshow('Image', x[0, 5])
cv2.waitKey(0)

# 다음과 같이 하나씩 글자를 저장할 수 있습니다.
cv2.imwrite('test0.png', x[0, 0])
cv2.imwrite('test1.png', x[5, 0])
cv2.imwrite('test2.png', x[10, 0])
cv2.imwrite('test3.png', x[15, 0])
cv2.imwrite('test4.png', x[20, 0])
cv2.imwrite('test5.png', x[25, 0])
cv2.imwrite('test6.png', x[30, 0])
cv2.imwrite('test7.png', x[35, 0])
cv2.imwrite('test8.png', x[40, 0])
cv2.imwrite('test9.png', x[45, 0])
