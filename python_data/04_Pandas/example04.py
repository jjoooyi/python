import pandas as pd
import numpy as np


# 데이터 프레임 그룹화
# 1)
df = pd.DataFrame([
    ['Apple', 7, 'Fruit'],
    ['Banana', 3, 'Fruit'],
    ['Beef', 5, 'Meal'],
    ['Kimchi', 4, 'Meal']],
    columns=['Name', 'Frequency', 'Type'])
print(df)
print(df.groupby(['Type']).sum())

# 2)
df = pd.DataFrame([
    ['Apple', 7, 5, 'Fruit'],
    ['Banana', 3, 6, 'Fruit'],
    ['Beef', 5, 2, 'Meal'],
    ['Kimchi', 4, 8, 'Meal']],
    columns=["Name", "Frequency", "Importance", "Type"])
print(df)
print(df.groupby(['Type']).aggregate([min, max, np.average]))

# 3)
df = pd.DataFrame([
    ['Apple', 7, 5, 'Fruit'],
    ['Banana', 3, 6, 'Fruit'],
    ['Beef', 5, 2, 'Meal'],
    ['Kimchi', 4, 8, 'Meal']],
    columns=["Name", "Frequency", "Importance", "Type"])


def my_filter(data):
    return data['Frequency'].mean() >= 5


df = df.groupby('Type').filter(my_filter)
print(df)

# 4)
df = pd.DataFrame([
    ['Apple', 7, 5, 'Fruit'],
    ['Banana', 3, 6, 'Fruit'],
    ['Beef', 5, 2, 'Meal'],
    ['Kimchi', 4, 8, 'Meal']],
    columns=["Name", "Frequency", "Importance", "Type"])
df = df.groupby('Type').get_group('Fruit')
print(df)

# 5)
df = pd.DataFrame([
    ['Apple', 7, 5, 'Fruit'],
    ['Banana', 3, 6, 'Fruit'],
    ['Beef', 5, 2, 'Meal'],
    ['Kimchi', 4, 8, 'Meal']],
    columns=["Name", "Frequency", "Importance", "Type"])
df["Gap"] = df.groupby("Type")["Frequency"].apply(lambda x: x - x.mean())
print(df)


# 데이터 프레임 다중화
df = pd.DataFrame(
    np.random.randint(1, 10, (4, 4)),
    index=[['1차', '1차', '2차', '2차'], ['공격', '수비', '공격', '수비']],
    columns=['1회', '2회', '3회', '4회']
)
print(df)
print(df[["1회", "2회"]].loc["2차"])


# 피벗 테이블 기초
df = pd.DataFrame([
    ['Apple', 7, 5, 'Fruit'],
    ['Banana', 3, 6, 'Fruit'],
    ['Coconut', 2, 6, 'Fruit'],
    ['Rice', 8, 2, 'Meal'],
    ['Beef', 5, 2, 'Meal'],
    ['Kimchi', 4, 8, 'Meal']],
    columns=["Name", "Frequency", "Importance", "Type"])
df = df.pivot_table(
    index="Importance", columns="Type", values="Frequency",
    aggfunc=np.max)
print(df)
