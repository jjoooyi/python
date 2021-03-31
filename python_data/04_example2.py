import numpy as np

# Numpy 원소 오름차순 정렬
array = np.array([5, 9, 10, 3, 1])
array.sort()
print(array)
print(array[::-1])  # 내림차순 정렬


# 각 열을 기준으로 정렬
array = np.array(([5, 9, 10, 3, 1], [8, 3, 4, 2, 5]))
print(array)
array.sort(axis=0)  # 열기준 오름차순 정렬
print(array)


# 균일한 간격으로 데이터 생성
array = np.linspace(0, 10, 5)  # 시작값, 끝값, 데이터 개수
print(array)


# 난수의 재연 (실행마다 결과 동일)
np.random.seed(7)
print(np.random.randint(0, 10, (2, 3)))


# Numpy 배열 객체 복사
array1 = np.arange(0, 10)
array2 = array1.copy()


# 중복된 원소 제거
array = np.array([1, 1, 2, 2, 2, 3, 3, 4])
print(np.unique(array))
