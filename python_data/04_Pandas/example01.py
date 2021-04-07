import pandas as pd

array = pd.Series(['apple', 'banana', 'carrot'], index=['a', 'b', 'c'])
print(array)
print(array['a'])


# dict 자료형을 Series로 바꾸기
data = {
    'a': 'apple',
    'b': 'banana',
    'c': 'carrot'
}

array = pd.Series(data)
print(array)
print(array['a'])


# 데이터 프레임
word_dict = {
    'Apple': '사과',
    'Banana': '바나나',
    'Carrot': '당근',
    'Durian': '두리안'
}
frequency_dict = {
    'Apple': 3,
    'Banana': 5,
    'Carrot': 7,
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

score = summary['frequency'] * summary['importance']
summary['score'] = score

print(summary)


# 데이터 프레임 슬라이싱
# 1) 이름을 기준으로 슬라이싱
print(summary.loc['Banana':'Carrot', 'importance':])

# 2) 인덱스를 기준으로 슬라이싱
print(summary.iloc[1:3, 2:])


# 데이터 프레임 연산
summary.loc['Apple', 'importance'] = 5  # 데이터의 변경
summary.loc['Elderberry'] = ['엘더베리', 5, 3, 15]  # 새 데이터 삽입


# 엑셀로 내보내기/불러오기
summary.to_csv('summary.csv', encoding='utf-8-sig')
saved = pd.read_csv('summary.csv', index_col=0)  # index_col 인덱스로 지정할 컬럼
print(saved)
