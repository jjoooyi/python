# https://blog.naver.com/hankrah/221761664080
# 딕셔너리 정렬

my_dict = {'e':5, 'b':6, 'a':2, 'd':7, 'c':1}

print(sorted(my_dict))  # ['a', 'b', 'c', 'd', 'e']
print(sorted(my_dict.keys())) # ['a', 'b', 'c', 'd', 'e']
print(sorted(my_dict, key=lambda x:my_dict[x])) # ['c', 'a', 'e', 'b', 'd'] value 순
print(sorted(my_dict, key=lambda x:my_dict[x], reverse=True)) # ['d', 'b', 'e', 'a', 'c'] value 역순

# 딕셔너리를 key에 따라 정렬 하는 방법
# dict.items() : (key, value) tuple 리스트 리턴
# 1)
print(sorted(my_dict.items()))
print(sorted(my_dict.items(), reverse=True))

# 2)
print(sorted(my_dict.items(), key=lambda x:x[0]))

# 3)
import operator
print(sorted(my_dict.items(), key=operator.itemgetter(0)))
print(sorted(my_dict.items(), key=operator.itemgetter(0), reverse=True))


# 딕셔너리를 value에 따라 정렬 하는 방법
# 1)
print(sorted(my_dict.items(), key=lambda x:x[1]))
print(sorted(my_dict.items(), key=lambda x:x[1], reverse=True))

# 2)
import operator
print(sorted(my_dict.items(), key=operator.itemgetter(1)))
print(sorted(my_dict.items(), key=operator.itemgetter(1), reverse=True))

# 딕셔너리 value가 같으면 key에 따라 정렬하는 방법
import operator
print(sorted(my_dict.items(), key=operator.itemgetter(0, 1)))