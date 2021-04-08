import matplotlib.pyplot as plt
import numpy as np

x = range(0, 100)
y = [v*v for v in x]
plt.plot(x, y, 'ro')
plt.show()


fig = plt.figure()  # Figure 객체 생성
ax1 = fig.add_subplot(2, 1, 1)  # 2X1의 첫번째 subplot
ax2 = fig.add_subplot(2, 1, 2)  # 2X1의 두번째 subplot
ax1.plot(x, y)
ax2.bar(x, y)
plt.show()

# sine, cosine 그래프
x = np.arange(0.0, 2*np.pi, 0.1)  # 0-2 π 사이에서 0.1 간격

fig = plt.figure()  # Figure 객체 생성
ax1 = fig.add_subplot(211)  # 2X1의 첫번째 subplot
ax2 = fig.add_subplot(212)  # 2X1의 두번째 subplot

ax1.plot(x, np.sin(x), 'b--')
ax2.plot(x, np.cos(x), 'r--')

ax1.set_xlabel('x')
ax1.set_ylabel('sin(x)')
ax2.set_xlabel('x')
ax2.set_ylabel('cos(x)')
plt.show()
