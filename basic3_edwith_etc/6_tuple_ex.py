c = {'a': 10, 'b': 1, 'c': 22}

# 딕셔너리 value 값으로 정렬하기
# 1)
tmp = list()
for k, v in c.items():
    tmp.append((v, k))
tmp = sorted(tmp, reverse=True)
print(tmp)

# 2) 더 짧게
# List Comprehension
print(sorted([(v, k) for k, v in c.items()]))


# 가장 많이 쓰는 단어 10개 찾기
fhand = open('romeo.txt')
counts = {}  # {} == dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
lst = []  # [] == list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)
for val, key in lst[:10]:
    print(key, val)
