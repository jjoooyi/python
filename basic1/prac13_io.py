print("Python", "Java", "JavaScript", sep=" vs ") # sep을 이용하여 두 문자 사이에 어떤 값이 올 지 정할 수 있음
print("Python", "Java", sep=", ", end="?") # end 문장의 끝부분을 지정
print("무엇이 더 재밌을까요?")

import sys
print("Python", "Java", file=sys.stdout) # 표준 출력
print("Python", "Java", file=sys.stderr) # 표준 에러(로그 관리)

# 시험 성적
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items(): # items() => (key, value) => 두 값이 tuple로 저장!
    print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":") 

# 은행 대기순번표
# 001, 002, 003, ...
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))

answer = input("아무 값이나 입력하세요 : ") # input()은 string 형으로 저장된다
print("입력하신 값은 "+answer+"입니다.")

# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되 총 10자리 공간을 확보
print("{0: >10}".format(500))

# 양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

# 왼쪽 정렬하고, 빈칸을 _로 채움, 부호 표시
print("{0:_<+10}".format(500))

# 3자리 마다 콤마 찍어주기
print("{0:,}".format(100000000000))

# 3자리 마다 콤마 찍으면서 +- 부호도 붙이기
print("{0:+,}".format(100000000000))
print("{0:+,}".format(-100000000000))

# 3자리 마다 콤마를 찍어주면서 부호도 붙이고 자릿수 확보하기, 빈자리는 ^로 채워주기
print("{0:^<+30,}".format(100000000000))
print("{0:^>+30,}".format(-100000000000))

# 소숫점 출력
print("{0:f}".format(5/3))

# 소숫점 특정 자릿수 까지만 표시 (소숫점 3째 자리에서 반올림)
print("{0:.2f}".format(5/3))