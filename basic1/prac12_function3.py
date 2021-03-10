gun = 10

def checkpoint(soldiers): # 경계근무
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총: {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2) # 2명이 경계 근무 나감
print("남은 총 : {0}".format(gun))

# 전역변수를 사용하기보다는 매개변수로 넘기고 반환값 받아서 관리하는것이 좋음! 코드기 복잡/더러워짐
def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))

''' Quiz) 표준 체중 구하는 프로그램
* 표준 체중 : 각 개인의 키에 적당한 체중

(성별에 따른 공식)
남자 : 키(m) * 키(m) * 22
여자 : 키(m) * 키(m) * 21

조건1: 표준 체중은 별도의 함수 내에서 계산
    * 함수명: std_weight
    * 전달값: 키(height), 성별(gender)
조건2: 표준 체중은 소수점 둘째자리까지 표시

(출력 예제)
키 175cm 남자의 표준 체중은 67.38kg 입니다.
'''

def std_weight(height, gender): # 키 m단위(실수), 성별 "남자" / "여자"
    if gender == '여자':
        return height * height * 21
    elif gender == '남자':
        return height * height * 22

height = 175 # cm 단위
gender = '남자'
weight = round(std_weight(height/100, gender), 2) # 소숫점 2째 자리까지 반올림
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))