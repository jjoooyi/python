# open() : 파일을 특정한 모드로 여는 함수, 읽을때는 r, 쓸 때는 w
# read() : 파일 객체로부터 모든 내용을 읽는 함수
# readline() : 파일 객체로부터 한 줄씩 문자열을 읽는 함수
# readlines() : 전체 내용을 한 번에 리스트에 담는 함수

f = open("basic3_etc/input.txt", "r", encoding="UTF-8")
f.seek(9)  # 9바이트 위치로 읽기 시작하는 지점 지정
data = f.read()
print(data)

# 한줄씩 읽어오기
count = 0
while count < 3:
    data = f.readline()
    count += 1
    print("{0}번째 줄: {1}".format(count, data), end='')

lst = f.readlines()
print(lst)
for i, data in enumerate(lst):
    print("{0}번째 줄: {1}".format(i+1, data), end='')

f.close()

with open('basic3_etc/input.txt', 'r', encoding='UTF-8') as f:
    lst = f.readlines()
    for i, data in enumerate(lst):
        print("{0}번째 줄: {1}".format(i+1, data), end='')

# 문자열 라이브러리에 있는 rstrip() 이용하여 오른쪽에서부터 공백 지울 수 있음
# 개행문자는 '공백'으로 취급되어 제거됨
for line in f:
    line = line.rstrip()
    # if line.startswith('From: '): # 아래 두줄과 같은 동작
    if not line.startswith('From:'):
        continue
    print(line)


# 잘못된 파일명이 입력될 경우 예외처리
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)
