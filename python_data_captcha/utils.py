# 색상별로 이미지 추출

import cv2
import numpy as np

BLUE = 0
GREEN = 1
RED = 2


# 특정한 색상의 모든 단어가 포함된 이미지를 추출합니다.(R/G/B)
def get_chars(image, color):
    # 가져온 color 외의 다른 2 색 정보 가져오기
    other_1 = (color + 1) % 3
    other_2 = (color + 2) % 3

    # other_1, other_2 색이 FF라면(추출하려는 색 이외의 색이라면) 검은색으로
    c = image[:, :, other_1] == 255
    image[c] = [0, 0, 0]
    c = image[:, :, other_2] == 255
    image[c] = [0, 0, 0]
    # 겹친 부분의 색일 경우(other_1, other_2 겹친 부분), AA이하
    c = image[:, :, color] < 170
    image[c] = [0, 0, 0]
    # 추출하려는 색만 남아있기 때문에 그 부분을 하얀색으로 변경
    c = image[:, :, color] != 0
    image[c] = [255, 255, 255]

    return image


# 전체 이미지에서 왼쪽부터 단어별로 이미지 추출
def extract_chars(image):
    chars = []
    colors = [BLUE, GREEN, RED]
    for color in colors:
        image_from_one_color = get_chars(image.copy(), color)
        image_gray = cv2.cvtColor(image_from_one_color, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(image_gray, 127, 255, 0)
        # RETR_EXTERNAL 옵션으로 숫자의 와곽을 기준으로 분리
        contours, _ = cv2.findContours(
            thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            # 추출된 이미지 크기가 50이상인 경우만 실제 문자 데이터인 것으로 파악, 부스러기 무시하기
            area = cv2.contourArea(contour)
            if area > 50:
                x, y, width, height = cv2.boundingRect(contour)
                roi = image_gray[y:y+height, x:x+width]
                chars.append((x, roi))
    chars = sorted(chars, key=lambda char: char[0])  # x 값에 따라 정렬
    return chars


# 이미지를 (20X20) 크기로 통일
def resize20(image):
    resized = cv2.resize(image, (20, 20))
    return resized.reshape(-1, 400).astype(np.float32)
