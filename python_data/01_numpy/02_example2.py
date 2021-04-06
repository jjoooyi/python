import numpy as np

# numpy 배열 가로축으로 합치기(옆으로 붙이기)
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
array3 = np.concatenate([array1, array2])

print(array3.shape)  # 배열의 크기
print(array3)


# 배열 형태 바꾸기
array1 = np.array([1, 2, 3, 4])
array2 = array1.reshape((2, 2))

print(array2)


# numpy 배열 세로축으로 합치기(아래로 붙이기)
array1 = np.arange(4).reshape(1, 4)
array2 = np.arange(8).reshape(2, 4)

print(array1)
print(array2)

array3 = np.concatenate([array1, array2], axis=0)


# numpy 배열 나누기
array = np.arange(8).reshape(2, 4)
left, right = np.split(array, [2], axis=1)  # 2번째 열을 기준으로 자름
print(left.shape)
print(right.shape)
print(array)
print(left)
print(right)
print(right[1][1])
