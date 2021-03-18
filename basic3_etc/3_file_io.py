# 파일에 저장된 문자의 빈도수 출력하는 함수
def process(filename):
    with open(filename, 'r') as f:
        # 키: 알파벳, 값: 빈도수
        dct = {}
        data = f.read()
        for i in data:
            if i in dct:
                dict[i] += 1
            else:
                dict[i] = 1


dct = process("basic3_etc/input.txt")

# 빈도수를 기준으로 내림차순 정렬
dct = sorted(dct.items(), key=lambda a: a[1], reverse=True)
for data, count in dct:
    if data == '\n' or data == ' ':
        continue
    print("{0}번 출현: {1}".format(count, data))
