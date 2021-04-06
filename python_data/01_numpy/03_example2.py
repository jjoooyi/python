import numpy as np

# Numpy의 마스킹 연산
# 마스킹: 각 원소에 대하여 체크
# Numpy 원소의 값을 조건에 따라 바꿀 때는 다음과 같이 합니다.
# 반복문을 이용할 때보다 매우 빠르게 동작합니다.
# 대체로 이미지 처리(Image Processing)에서 자주 활용됩니다.

array1 = np.arange(16).reshape(4, 4)
print(array1)

array2 = array1 < 10
print(array2)

array1[array2] = 100
print(array1)


# Numpy 집계 함수
array = np.arange(16).reshape(4, 4)

print("최댓값: ", np.max(array))
print("최솟값: ", np.min(array))
print("합계: ", np.sum(array))
print("평균값: ", np.mean(array))

# 특정 열의 모든 행의 값 더하기
print("열 합계: ", np.sum(array, axis=0))
print("행 합계: ", np.sum(array, axis=1))
