import numpy as np

# Numpy의 사칙연산
array = np.random.randint(1, 10, size=4).reshape(2, 2)
print(array)

result_array = array * 10
print(result_array)


# 서로 다른 형태의 Numpy 연산
# 브로드캐스팅: 형태가 다른 배열을 연산할 수 있도록 배열의 형태를 동적으로 변환
array1 = np.arange(4).reshape(2, 2)  # (2 x 2)
array2 = np.arange(2)  # (1 x 2)

array3 = array1 + array2
print(array3)

array1 = np.arange(0, 8).reshape(2, 4)
array2 = np.arange(0, 8).reshape(2, 4)
array3 = np.concatenate([array1, array2], axis=0)  # 아래쪽으로 합치기
array4 = np.arange(0, 4).reshape(4, 1)  # (4 x 1)

print(array3 + array4)
