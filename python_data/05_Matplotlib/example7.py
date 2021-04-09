import matplotlib.pyplot as plt
import pandas_datareader.data as web
import datetime
import mpl_finance as matfin
# import matplotlib.finance as matfin
import matplotlib.ticker as ticker

# 캔들스틱 차트 그리기
# https://wikidocs.net/4766

start = datetime.datetime(2021, 3, 1)
end = datetime.date(2021, 3, 31)

sk_hynix = web.DataReader('000660.KS', 'yahoo', start, end)
print(sk_hynix.head())
# 주가 존재하지 않을 경우 예외처리
sk_hynix = sk_hynix[sk_hynix['Volume'] > 0]  # 3월 1일은 장이 열리지 않아 값이 없음
print(sk_hynix.index[0].strftime('%Y-%m-%d'))  # 2021-03-02

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)

name_list = []
day_list = []

# ticker 표기할 위치값 생성
# day_list = range(len(sk_hynix))
# x축 ticker에 표기할 값 구하기
# 날짜 값만 추출
# for day in sk_hynix.index:
#     name_list.append(day.strftime('%d'))

# 거래일이 월요일인 날에만 년-월-일 표기
for i, day in enumerate(sk_hynix.index):
    if day.dayofweek == 0:
        day_list.append(i)
        name_list.append(day.strftime('%Y-%m-%d') + '(Mon)')

# ticker 위치 지정하고 값 표기
ax.xaxis.set_major_locator(ticker.FixedLocator(day_list))
ax.xaxis.set_major_formatter(ticker.FixedFormatter(name_list))

matfin.candlestick2_ohlc(ax, sk_hynix['Open'], sk_hynix['High'], sk_hynix['Low'],
                         sk_hynix['Close'], width=0.5, colorup='r', colordown='b')

plt.show()
