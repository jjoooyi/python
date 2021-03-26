'''
^ : 문장의 시작을 의미
. : 어떤 문자 한 글자
* : 앞의 문자가 여러 번 반복될 수 있음을 의미
+ : 앞의 문자가 1번 이상 나타남을 의미
\S : 공백 문자가 아닌 한 개의 문자
[0-9]+ : 0부터 9까지 문자가 1번 이상 반복되는 패턴
'$' 문자가 포함된 패턴을 찾고 싶을 경우 이스케이프 문자 사용!
\$ 사용하면됨
'''

import re

hand = open('mbox-short.txt')

# find() 사용하여 추출
for line in hand:
    line = line.rstrip()
    if line.find('From:') >= 0:
        print(line)

# 정규식을 사용하여 추출 re.research('추출하고자하는 정규식', 추출 대상)
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
        print(line)

for line in hand:
    line = line.rstrip()
    # 시작문자 지정
    if re.search('^From:', line):
        print(line)
