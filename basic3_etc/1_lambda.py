# 시퀀스(Sequence) : 문자열, 리스트, 튜플 등의 인덱스(Index)를 가지는 자료형
# len(시퀀스 자료형) : 시퀀스 자료형의 길이를 출력하는 함수
# 반복문 등에서 사용될 수 있음

# 람다식 : 함수의 형태를 더욱 짧게 쓸 수 있도록 해주는 문법
add = lambda x, y: x + y
print(add(1,2))

# map() : 다수의 원소에 대한 함수의 결과를 한번에 얻을 수 있도록 도와줌
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

func = lambda a, b: a + b
result = map(func, list1, list2)
print(list(result))