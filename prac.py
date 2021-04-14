# T if 조건 else F
# T : 조건이 참일 때 값
# F : 조건이 거짓일 때 값
# a, b = input().split()
# a, b = int(a), int(b)

# print(a if a > b else b)


# a, b, c = input().split()
# a, b, c = int(a), int(b), int(c)

# print((a if a < b else b) if ((a if a < b else b) < c) else c)

# print(ord('a'))
# print(chr(97))

# i = ord(input())
# cnt = 97
# while True:
#     print(chr(cnt))
#     cnt += 1

#     if cnt > i:
#         break

# i = int(input())
# sum = 0
# cnt = 0

# while sum != i:
#     cnt += 1
#     sum += cnt
# print(cnt)

# a, b = input().split()
# a, b = int(a), int(b)

# for i in range(1, a+1):
#     for j in range(1, b+1):
#         print(i, j)

# i = int(input())

# for i in range(1, i+1):
#     if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
#         print('X', end=' ')
#     else:
#         print(i, end=' ')

# a, b, c = input().split()
# a, b, c = int(a), int(b), int(c)

# # cnt = 0

# # for i in range(a):
# #     for j in range(b):
# #         for k in range(c):
# #             print(i, j, k)
# #             cnt += 1

# # print(cnt)

# result = a*b*c / 8 / 1024 / 1024
# print(result)

# a, b, c = input().split()
# a, b, c = int(a), int(b), int(c)

# result = a*b*c / 8 / 1024 / 1024
# print('%.2f MB' % result)

# a = int(input())

# for i in range(1, a+1):
#     if i % 3 == 0:
#         continue
#     print(i, end=" ")

# a, m, d, n = input().split()
# a, m, d, n = int(a), int(m), int(d), int(n)

# # print(a+(n-1)*d)

# for i in range(n-1):
#     a = a * m + d
# print(a)

# a, b, c = input().split()
# a, b, c = int(a), int(b), int(c)

# d = 1

# while d % a != 0 or d % b != 0 or d % c != 0:
#     d += 1
# print(d)

# cnt = int(input())
# lst = input().split()
# d = {}

# for i in lst:
#     i = int(i)
#     d[i] = d.get(i, 0) + 1
# for i in range(1, 24):
#     if i not in d.keys():
#         print(0, end=' ')
#         continue
#     print(d[i], end=' ')


# cnt = int(input())
# l = input().split()
# for i in range(cnt):
#     l[i] = int(l[i])
# l.sort()
# print(l[0])

# cnt = int(input())
# array = [[0 for j in range(19)] for i in range(19)]

# for elem in range(cnt):
#     i, j = input().split()
#     i, j = int(i), int(j)
#     array[i-1][j-1] = 1

# for i in range(19):
#     for j in range(19):
#         print(array[i][j], end=' ')
#     print()

array = [[0 for j in range(19)] for i in range(19)]

for i in range(19):
    array[i] = list(map(int, input().split()))

cnt = int(input())

for d in range(cnt):
    i, j = input().split()
    i, j = int(i), int(j)
    for a in range(19):
        if array[a][j-1] == 0:
            array[a][j-1] = 1
        else:
            array[a][j-1] = 0

    for a in range(19):
        if array[i-1][a] == 0:
            array[i-1][a] = 1
        else:
            array[i-1][a] = 0

for i in range(19):
    for j in range(19):
        print(array[i][j], end=' ')
    print()
