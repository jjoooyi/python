# 자료구조의 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu)) # set

menu = list(menu)
print(menu, type(menu)) # list

menu = tuple(menu)
print(menu, type(menu)) # tuple

menu = set(menu)
print(menu, type(menu)) # set


''' Quiz> 추첨
조건1: 편의상 댓글은 20명이 작성, 아이디는 1~20이라고 가정
조건2: 댓글 내용 상관 없이 무작위 추첨, 중복 불가
조건3: random 모듈의 suffle 과 sample 활용

(출력 예제)
-- 당첨자 발표 --
치킨 당첨자 : 1
커피 당첨자 : [2, 3, 4]
-- 축하합니다 --

(홀용 예제)
from random import *
list = [1, 2, 3, 4, 5]
print(list)
shuffle(list) # 리스트 무작위 섞기
print(list)
print(sample(list, 1)) # 리스트에서 무작위 샘플 1개 뽑기
'''

from random import *
users = range(1, 21) # 1부터 20까지 숫자를 생성
# print(type(users)) # range 타입
users = list(users)

shuffle(users)
winners = sample(users, 4)

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다 --")
