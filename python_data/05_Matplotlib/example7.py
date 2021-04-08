import matplotlib.pyplot as plt
import pandas_datareader.data as web
import datetime
import mpl_finance as matfin
# import matplotlib.finance as matfin

# 캔들스틱 차트 그리기
# https://wikidocs.net/4766

start = datetime.datetime(2021, 3, 1)
end = datetime.date(2021, 3, 31)

sk_hynix = web.DataReader('000660.KS', 'yahoo', start, end)
print(sk_hynix.head())

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)
matfin.candlestick2_ohlc(ax, sk_hynix['Open'], sk_hynix['High'], sk_hynix['Low'],
                         sk_hynix['Close'], width=0.5, colorup='r', colordown='b')

plt.show()
