print("ㅋ"*9)
print(not True)
print(not False)
print(not (5 > 10))

#애완동물을 소개해주세요
animal = '강아지'
name = '연탄이'
age = 4
hobby = '산책'
is_adult = age >= 3

print("우리집" + animal + "이름은" + name + "입니다")
#print(name + "는" + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
print(name, "는", age, "살이며, ", hobby, "을 아주 좋아해요")
print(name + "는 어른일까요?" + str(is_adult))

'''Quiz> 변수를 이용하여 다음 문장을 출력하시오

변수명: station
변수값: "사당", "신도림", "인천공항" 순서대로 입력

출력 문장: XX행 열차가 들어오고 있습니다.
'''

station = '사당'
print(station + "행 열차가 들어오고 있습니다.")

print((3>0) and (3<5)) # True
print((3>0) and (3<5)) # True

print((3>0) or (3>5)) # True
print((3>0) | (3<5)) # True

print(5 > 4 > 3) # True
print(5 > 4 > 7) # False

print(2 + 3 * 4) # 14
print((2 + 3) * 4) # 20
number = 2 + 3 * 4
print(number)
number = number + 2 # 16
print(number)
number += 2 # 18
print(number)
number *= 2 # 26
print(number)
number /= 2 # 18
print(number)
number -= 2 # 16
print(number)
number %= 5 # 1
print(number)

print(abs(-5)) # 5,  절댓값
print(pow(4, 2)) # 4^2 = 4*4 = 16
print(max(5, 12)) # 최댓값 12
print(min(5, 12)) # 최솟값 5
print(round(3.14)) # 반올림 3
print(round(4.99)) # 반올림 5

from math import *
print(floor(4.99)) # 내림, 4
print(ceil(3.14)) # 올림, 4
print(sqrt(16)) # 제곱근, 4

from random import *
print(random()) # 0.0이상 1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값 생성
print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성

print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성

print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성

'''Quiz2> 월 4회 스터디를 하는데 3번은 온라인 1번은 오프라인
조건에 맞는 오프라인 모임 날짜 정해주는 프로그램

조건1: 랜덤으로 날짜 뽑아야 함
조건2: 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
조건3: 매월 1~3일은 스터디 준비를 해야하므로 제외
'''

date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 "+str(date)+"일로 선정되었습니다.")


sentence = '나는 소년입니다'
print(sentence)
sentence2 = '파이썬은 쉬워요'
print(sentence2)
sentence3 = '''
나는 소년이고,
파이썬은 쉬워요
'''
print(sentence3)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)

jumin = '990120-1234567'

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) # 0 부터 2 직전까지 (0 ,1)
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지
#print("뒤 7자리 : " + jumin[7:14])
print("뒤 7자리 : " + jumin[7:]) # 7 부터 끝까지
print("뒤 7자리 (뒤에부터) : " + jumin[-7:]) # 맨 뒷자리 -1 / 맨 뒤에서 7번째부터 끝까지

python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

# index, find, count
index = python.index("n")
print(index)
index = python.index("n", index + 1) # 처음  n을 찾은 다음 인덱스부터 n 찾기
print(index)

print(python.find("n"))
print(python.find("Java")) # 찾는 값 없을 때 -1 반환
# print(python.index("Java")) # 찾는 값 없을 때 에러 발생

print(python.count("n")) # n의 개수

# 문자열 포맷
print("a" + "b")
print("a", "b")

# 방법 1
print("나는 %d살입니다." % 20)
print("나는 %s을 좋아해요." % "파이썬")
print("Apple 은 %c로 시작해요" % "A")
# %s
print("나는 %s살입니다." % 20)
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# 방법 2
print("나는 {}살입니다." .format(20))
print("나는 {}색과 {}색을 좋아해요." .format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요." .format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요." .format("파란", "빨간"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요." .format(age = 20, color = "빨간"))
print("나는 {age}살이며, {color}색을 좋아해요." .format(color = "빨간", age = 20))

# 방법 4 (v3.6 이상~)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

# 탈출 문자(이스케이프 문자)
# \n : 줄바꿈
# \" \' : 문장 내에서 따옴표
# \\ : 문장 내에서 \
# \t : 탭

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine") # PineApple

# \b : 백스페이스(한 글자 삭제)
print("Redd\bApple") #RedApple

'''Quiz3> 사이트별 비밀번호 만들어주는 프로그램
예) http://naver.com
규칙1: https:// 부분은 제외
규칙2: 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙3: 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + '!'로 구성

=> 생성된 비밀번호 : nav51!
'''
url = "http://naver.com"
# 규칙1 : url.replace("http://", "")
word = url[7:url.index(".")]
pwd = word[:3] + str(len(word)) + str(word.count('e')) + '!'

print("{0}의 비밀번호는 {1}입니다." .format(url, pwd))
print(f"{url}의 비밀번호는 {pwd}입니다.")