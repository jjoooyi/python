import matplotlib.pyplot as plt

# Figure 객체 생성
fig = plt.figure()
print(type(fig))  # <class 'matplotlib.figure.Figure'>

ax = fig.add_subplot(111)  # 1, 1, 1
print(type(ax))  # <class 'matplotlib.axes._subplots.AxesSubplot'>
plt.show()


# Figure 객체를 생성하고 해당 Figure 객체에
# 여러 개의 AxesSubplot 객체를 생성하는 두 가지 작업을 한번에 하고자 할 때
# ax_list[0][0], ax_list[0][1], ax_list[1][0], ax_list[1][1]
fig, ax_list = plt.subplots(2, 2)

ax_list[0][0].plot([1, 2, 3, 4])
plt.show()
