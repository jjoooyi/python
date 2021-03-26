# 숫자 세기 1-1 in 사용
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    if name in counts:
        counts[name] = counts[name] + 1
    else:
        counts[name] = 1
print(counts)


# 숫자세기 1-2 not in 사용
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)


# 숫자세기 2
# 딕셔너리.get(키값, 해당키가 없을 시 설정할 디폴트 값)
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    counts[name] = counts.get(name, 0) + 1  # 위의 if~else문과 같은 동작함!
print(counts)

# 파일에서 가장 많이 나온 단어 찾기!
name = input('Enter file:')
if len(name) < 1:
    name = 'score.txt'
handle = open(name)
counts = dict()
for line in handle:
    line = line.rstrip()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
bigcount = None
bigword = None
for word, count in counts.items():
    # 최댓값 찾는 루프
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)
