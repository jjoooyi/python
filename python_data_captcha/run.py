import cv2
import numpy as np
import utils
import requests
import shutil
import time

FILE_NAME = 'trained.npz'

# 각 글자의 (1X400) 데이터와 정답 (0~9, +, -, *)
with np.load(FILE_NAME) as data:
    train = data['train']
    train_labels = data['train_labels']

knn = cv2.ml.KNearest_create()
knn.train(train, cv2.ml.ROW_SAMPLE, train_labels)


def check(test, train, train_labels):
    # 가장 가까운 K개의 글자를 찾아, 어떤 숫자에 해당하는지 찾습니다.
    # (테스트 데이터 개수에 따라 조절)(학습시킨 이미지가 거의 동일하기 때문에 k=1로 설정)
    ret, result, neighbors, dist = knn.findNearest(test, k=1)
    return result  # 조회된 결과의 레이블 출력


def get_result(file_name):
    image = cv2.imread(file_name)
    # 들어온 캐릭터를 왼쪽부터 각각의 이미지를 잘라 저장
    chars = utils.extract_chars(image)
    result_str = ''
    for char in chars:
        # 이미지가 분류된 값
        matched = check(utils.resize20(char[1]), train, train_labels)
        if matched < 10:
            result_str += str(int(matched))
            continue
        if matched == 10:
            matched = '+'
        elif matched == 11:
            matched = '-'
        elif matched == 12:
            matched = '*'
        result_str += matched
    return result_str


# print(get_result('1.png'))

host = 'http://localhost:10000'
url = '/start'

# target_images 폴더에 이미지 저장
with requests.Session() as s:
    answer = ''  # 처음에는 답이 필요없기 때문에 공백
    for i in range(0, 100):
        start_time = time.time()
        params = {'ans': answer}

        # 정답을 파라미터에 달아서 전송하여 이미지 경로를 받아옴
        response = s.post(host + url, params)
        print('Server Return: ' + response.text)
        if i == 0:
            returned = response.text
            image_url = host + returned
            url = '/check'
        else:
            returned = response.json()
            image_url = host + returned['url']
        print('Problem' + str(i) + ': ' + image_url)

        # 특정한 폴더에 이미지 파일을 다운로드 받습니다.
        response = s.get(image_url, stream=True)
        target_image = './target_images/' + str(i) + '.png'
        with open(target_image, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response

        # 다운로드 받은 이미지 파일을 분석하여 답을 도출
        answer_string = get_result(target_image)
        print('String: ' + answer_string)
        answer_string = utils.remove_first_zero(answer_string)
        answer = str(eval(answer_string))
        print('Answer: ' + answer)
        print('--- %s seconds ---' % (time.time() - start_time))
