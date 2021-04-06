import cv2
import numpy as np
import glob

FILE_NAME = 'trained.npz'


def load_train_data(file_name):  # 파일로부터 학습 데이터를 불러옵니다.
    with np.load(file_name) as data:
        train = data['train']
        train_labels = data['train_labels']
    return train, train_labels


def resize20(image):  # 손글씨 이미지를 (20X20) 크기로 Scaling 합니다.
    img = cv2.imread(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_resize = cv2.resize(gray, (20, 20))
    # 최종적으로는 (1X400) 크기로 반환
    cv2.imshow('Image', gray_resize)
    return gray_resize.reshape(-1, 400).astype(np.float32)


def check(test, train, train_labels):
    knn = cv2.ml.KNearest_create()
    knn.train(train, cv2.ml.ROW_SAMPLE, train_labels)
    # 가장 가까운 5개의 글자를 찾아, 어떤 숫자에 해당하는지 찾습니다.
    ret, result, neighbors, dist = knn.findNearest(test, k=5)
    return result


train, train_labels = load_train_data(FILE_NAME)

for file_name in glob.glob('./test*.png'):
    test = resize20(file_name)
    result = check(test, train, train_labels)
    print(result)
    cv2.waitKey(0)

cv2.destroyAllWindows()
