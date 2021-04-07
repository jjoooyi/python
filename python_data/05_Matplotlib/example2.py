import matplotlib.pyplot as plt
import numpy as np

# 선 그래프
x = np.arange(-9, 10)
y1 = x ** 2
plt.plot(
    x, y1,
    linestyle=':',
    marker='o',
    markerfacecolor='blue',
    markeredgecolor='red'
)
plt.show()


# 막대 그래프
plt.bar(x, y1)
plt.show()


# 누적 막대 그래프
# 0~1 사이의 랜덤값 10개 'numpy.ndarray'로 반환
x = np.random.rand(10)  # 아래 막대
y = np.random.rand(10)  # 중간 막대
z = np.random.rand(10)  # 위 막대
data = [x, y, z]
x_array = np.arange(10)  # x축 0~9
for i in range(0, 3):  # 누적 막대의 종류 3개
    plt.bar(
        x_array,  # 0부터 10까지의 x위치에서
        data[i],  # 각 높이대로 10개를 쌓음
        bottom=np.sum(data[:i], axis=0)
    )
plt.show()


# 스캐터 그래프
x = np.random.rand(10)
y = np.random.rand(10)
colors = np.random.randint(50, 100, 10)
sizes = np.pi * 1000 * np.random.rand(10)
plt.scatter(x, y, c=colors, s=sizes, alpha=0.7)
plt.show()
