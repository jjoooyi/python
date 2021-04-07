import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3]
y = [1, 2, 3]

plt.plot(x, y)
plt.title('My Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.savefig('plot1.png')
plt.show()


x = np.linspace(0, np.pi * 10, 500)  # PI * 10 너비에 500개의 점을 균일하게 찍기
fig, axes = plt.subplots(2, 1)  # 2개의 그래프가 들어가는 Figure 생성
axes[0].plot(x, np.sin(x))  # 첫 번재 그래프는 sin 그래프
axes[1].plot(x, np.cos(x))  # 두 번째 그래프는 cos 그래프
fig.savefig('sin&cos.png')
plt.show()


# 선그래프 그리기
# 1)
x = np.arange(-9, 10)
y = x ** 2
# 라인 스타일은 '-', ':', '-.', '--'등이 사용될 수 있음
plt.plot(x, y, linestyle=':', marker='*')
# X축 및 Y축에서 특정 범위를 자를수도 있음
plt.show()

# 2)
x = np.arange(-9, 10)
y1 = x ** 2
y2 = -x
plt.plot(x, y1, linestyle='-', marker='*', color='red', label='y = x * x')
plt.plot(x, y2, linestyle=':', marker='o', color='blue', label='y = -x')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(
    shadow=True,
    borderpad=1
)
plt.show()
