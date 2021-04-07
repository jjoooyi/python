# 입력에 들어온 숫자를 구분하기 위하여 KNN 알고리즘 이용

import os
import cv2
import numpy as np

# training_data에 저장한 파일을 불러오기 위한 리스트
file_names = list(range(0, 13))
train = []  # 불러온 이미지 파일 저장
train_labels = []  # 각 이미지 당 해당하는 숫자 레이블 저장

# 각각의 숫자 이미지 데이터 파일 읽어오기
for file_name in file_names:
    path = './training_data/' + str(file_name) + '/'
    file_count = len(next(os.walk(path))[2])

    for i in range(1, file_count+1):
        img = cv2.imread(path + str(i) + '.png')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        train.append(gray)
        train_labels.append(file_name)

x = np.array(train)
# 학습 시키기 위하여 20X20 -> 400(1차원 배열) 으로 변환
train = x[:, :].reshape(-1, 400).astype(np.float32)
train_labels = np.array(train_labels)[:, np.newaxis]  # 배열 형태로 변환

print(train.shape)  # (27, 400)
print(train_labels.shape)  # (27, 1)

np.savez('trained.npz', train=train, train_labels=train_labels)
