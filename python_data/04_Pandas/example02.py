import pandas as pd
import numpy as np

# 데이터 프레임 Null 여부 확인
word_dict = {
    'Apple': '사과',
    'Banana': '바나나',
    'Carrot': '당근',
    'Durian': '두리안'
}
frequency_dict = {
    'Apple': 3,
    'Banana': 5,
    'Carrot': np.nan,
    'Durian': 2
}
importance_dict = {
    'Apple': 3,
    'Banana': 2,
    'Carrot': 1,
    'Durian': 1
}

word = pd.Series(word_dict)
frequency = pd.Series(frequency_dict)
importance = pd.Series(importance_dict)
summary = pd.DataFrame({
    'word': word,
    'frequency': frequency,
    'importance': importance
})

print(summary)
print(summary.notnull())
print(summary.isnull())
summary['frequency'] = summary['frequency'].fillna('데이터없음')
print(summary)


# 시리즈 자료형 연산
array1 = pd.Series([1, 2, 3], index=['A', 'B', 'C'])
array2 = pd.Series([4, 5, 6], index=['B', 'C', 'D'])

array1 = array1.add(array2, fill_value=0)  # 값이 존재하지 않는(겹치지 않는) 부분은 0으로 채움
print(array1)


# 데이터 프레임 자료형 연산
array1 = pd.DataFrame([[1, 2], [3, 4]], index=['A', 'B'])
array2 = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], index=['B', 'C', 'D'])
print(array1)
print(array2)
array1 = array1.add(array2, fill_value=0)
print(array1)


# 데이터 프레임 집계 함수
print('컬럼 1의 합:', array1[1].sum())
print(array1.sum())

# 데이터 프레임 정렬 함수
summary = summary.sort_values('frequency', ascending=False)  # 내림차순으로 정렬
print(summary)
