# re.findall() 매칭되는 모든 값을 리스트로 저장
import re
x = 'My 2 favorite numbers are 19 and 42'

y = re.findall('[0-9]+', x)
print(y)  # ['2', '19', '42']

y = re.findall('[AEIOU]+', x)
print(y)  # [] 빈 리스트

# 기본 설정: 탐욕적 방식, 일치하는 여러 패턴 중 가장 긴 것을 선택
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)  # ['From: Using the :']

# 비탐욕적 방식
y = re.findall('^F.+?:', x)
print(y)  # ['From:']


# () 이용하여 원하는 부분만 선택 추출
x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\S+@\S+', x)
print(y)  # ['stephen.marquard@uct.ac.za’]

# 좀더 섬세한 추출
y = re.findall('^From (\S+@\S+)', x)
print(y)  # ['stephen.marquard@uct.ac.za']


# 이메일 호스트를 추출하는 방법
# 문자열 함수를 활용하여 추출한 방법 find() / 문자열 슬라이싱 이용
# 1-1)
atpos = x.find('@')  # 21
sppos = x.find(' ', atpos)  # 31
host = x[atpos+1: sppos]
print(host)  # 'uct.ac.za'

# 1-2)
words = x.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])  # 'uct.ac.za'

# 2) 정규식 사용한 방법
y = re.findall('@([^ ]*)', x)
print(y)  # ['uct.ac.za']

# 2-1) 좀 더 정교한 방법
y = re.findall('^From .*@([^ ]*)', x)
print(y)

# 패턴 추출 및 최댓값 찾기
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1:
        continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum:', max(numlist))
