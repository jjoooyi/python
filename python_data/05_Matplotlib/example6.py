import matplotlib.pyplot as plt
import pandas_datareader.data as web


# 수정 종가와 거래랑 한번에 그리기
# https://wikidocs.net/4765
sk_hynix = web.DataReader('000660.KS', 'yahoo')

fig = plt.figure(figsize=(12, 8))

top_axes = plt.subplot2grid((4, 4), (0, 0), rowspan=3, colspan=4)
bottom_axes = plt.subplot2grid((4, 4), (3, 0), rowspan=1, colspan=4)
bottom_axes.get_yaxis().get_major_formatter().set_scientific(False)

top_axes.plot(sk_hynix.index, sk_hynix['Adj Close'], label='Adjusted Close')
bottom_axes.plot(sk_hynix.index, sk_hynix['Volume'])

plt.tight_layout()
plt.show()
