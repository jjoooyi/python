'''
KNN Algorithm
# K-Nearest Neighbor
• KNN은 비지도학습(Unsupervised Learning)의 가장 간단한 예시입니다.
• 다양한 레이블의 데이터 중에서, 자신과 가까운 데이터를 찾아 자신의 레이블을 결정하는 방식입니다.
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

# 각 데이터의 위치: 25 X 2 크기에 각각 0 ~ 100, 총 25개의 데이터를 (x, y)2차원 그래프에 생성
trainData = np.random.randint(0, 100, (25, 2)).astype(np.float32)
# 각 데이터는 0 또는 1
response = np.random.randint(0, 2, (25, 1)).astype(np.float32)

# 값이 0인 데이터를 각각 (x, y) 위치에 빨간색으로 칠합니다.
red = trainData[response.ravel() == 0]
plt.scatter(red[:, 0], red[:, 1], 80, 'r', '^')  # 빨간색(r), 세모(^)

# 값이 1인 데이터를 각각 (x, y) 위치에 파란색으로 칠합니다.
blue = trainData[response.ravel() == 1]
plt.scatter(blue[:, 0], blue[:, 1], 80, 'b', 's')  # 파란색(b), 네모(s)

# (0 ~ 100, 0 ~ 100) 의 랜덤위치에 임의의 데이터를 하나 생성하여 칠합니다
newcomer = np.random.randint(0, 100, (1, 2)).astype(np.float32)
plt.scatter(newcomer[:, 0], newcomer[:, 1], 80, 'g', 'o')  # 초록색(g), 동그라미(o)

knn = cv2.ml.KNearest_create()  # 객체 초기화
knn.train(trainData, cv2.ml.ROW_SAMPLE, response)  # 생성한 데이터 값으로 초기화
ret, results, neighbors, dist = knn.findNearest(newcomer, 3)  # 가까운 3개를 확인

# 가까운 3개를 찾고, 거리를 고려하여 자신을 정합니다.
print('result : ', results)
print('neighbors : ', neighbors)
print('distance : ', dist)

plt.show()
