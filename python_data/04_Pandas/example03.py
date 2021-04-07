import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randint(1, 10, (2, 2)),
                  index=[0, 1], columns=['A', 'B'])

# 데이터 프레임 출력하기
print(df)
# 컬럼 A의 각 원소가 5보다 작거나 같은지 출력
print(df['A'] <= 5)
# 컬럼 A의 원소가 5보다 작고, 컬럼 B의 원소가 8보다 작은 행 추출
print(df.query('A <= 5 and B <= 8'))


# 데이터 프레임 개별연산
# 1)
df = pd.DataFrame([[1, 2, 3, 4], [1, 2, 3, 4]], index=[
                  0, 1], columns=["A", "B", "C", "D"])
print(df)
df = df.apply(lambda x: x+1)
print(df)


def addOne(x):
    return x+1


df = df.apply(addOne)
print(df)

# 2)
df = pd.DataFrame([
    ['Apple', 'Apple', 'Carrot', 'Banana'],
    ['Durian', 'Banana', 'Apple', 'Carrot']],
    index=[0, 1],
    columns=["A", "B", "C", "D"])
print(df)
df = df.replace({'Apple': 'Airport'})
print(df)
