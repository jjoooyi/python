import numpy as np

list_data = [1, 2, 3]
array = np.array(list_data)  # 리스트 데이터를 numpy 자료형으로 변환

print(array.size)
print(array.dtype)
print(array[1])

# 0부터 3까지의 배열 만들기
array1 = np.arange(4)
print(array1)

# 4x4 행렬을 만들면서 0으로 초기화 하면서 데이터 형은 float으로 지정
array2 = np.zeros((4, 4), dtype=float)
print(array2)

# 3x3 행렬을 만들면서 1로 초기화 하면서 데이터 형은 문자열로 지정
array3 = np.ones((3, 3), dtype=str)
print(array3)

# 0부터 9까지 랜덤하게 초기화 된 3x3배열 만들기
array4 = np.random.randint(0, 10, (3, 3))
print(array4)

# 평균이 0이고, 표준편차가 1인 표준 정규를 띄는 배열(표준 정규 분포)
array5 = np.random.normal(0, 1, (3, 3))
print(array5)
