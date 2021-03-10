# absent = [2, 5] # 결석
# no_book = [7] # 책을 안가지고 옴
# for student in range(1, 11): # 출석번호 1~10
#     if student in absent:
#         continue # 다음 반복문 진행
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
#         break # 반복문 탈출
#     print("{0}, 책을 읽어봐".format(student))


'''Quiz> 50명의 승객과 매칭, 총 탑승 고객 수 구하기

조건1: 승객별 운행 소요 시간 5분 ~ 50분 사이의 난수
조건2: 소요시간 5~15분 사이의 승객만 매칭

'''
from random import *

customer = []
cnt = 0

for i in range(1, 51):
    customer.append(randint(5, 51))
    take = "X"
    if 5 <= customer[i-1] <= 15:
        take = "O"
        cnt += 1
    print("[{0}] {1}번째 손님 (소요시간 : {2}분)".format(take, i, customer[i-1]))

print("총 탑승 승개 : {0} 분".format(cnt))


cnt = 0 # 총 탑승 승객 수
for i in range(1, 51): # 1 ~ 50 이라는 수(승객)
    time = randrange(5, 51) # 5분 ~ 50분 소요 시간
    if 5 <= time <= 15: # 5분 ~ 15분 이내의 손님(매칭 성공), 탑승 승객 수 증가 처리
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        cnt += 1
    else: # 매칭 실패한 경우
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

print("총 탑승 승객 : {0} 분".format(cnt))