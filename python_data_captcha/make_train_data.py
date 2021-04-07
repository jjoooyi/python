# 트레이닝에 사용할 데이터 수집 및 정제

import os
import cv2
import utils


# training_data 폴더 생성 및 그 내부에 0, 1, 2, 3, 4, 5, ... 11, 12 폴더 생성
image = cv2.imread('3.png')
chars = utils.extract_chars(image)

for char in chars:
    cv2.imshow('Image', char[1])  # roi 추출
    input = cv2.waitKey(0)
    resized = cv2.resize(char[1], (20, 20))

    if input >= 48 and input <= 57:  # 0부터 9까지
        name = str(input - 48)
        # file_count = len(next(os.walk('./training_data/' + name + '/'))[2]) # 에러남
        file_count = len(os.listdir('./training_data/' + name + '/'))
        cv2.imwrite('./training_data/' + name + '/' +
                    str(file_count + 1) + '.png', resized)
    elif input == ord('a') or input == ord('b') or input == ord('c'):  # + - *
        name = str(input - ord('a') + 10)
        # file_count = len(next(os.walk('./training_data' + name + '/'))[2]) # 에러남
        file_count = len(os.listdir('./training_data/' + name + '/'))
        cv2.imwrite('./training_data/' + name + '/' +
                    str(file_count + 1) + '.png', resized)
