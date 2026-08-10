import yfinance as yf
import matplotlib.pyplot as plt 

#matplotlibで日本語フォント（Noto Sans CJK JP）を指定
plt.rcParams["font.family"] = "Noto Sans CJK JP"

#銘柄コードを指定（例：トヨタ自動車）
ticker = "7203.T"
data = yf.download(ticker, period="6mo")

#移動平均線を計算
data["MA25"] = data["Close"].rolling(window=25).mean()
data["MA75"] = data["Close"].rolling(window=75).mean()

#終値と移動平均線をグラフ化
plt.figure(figsize=(10, 5))
plt.plot(data["Close"], label="終値")
plt.plot(data["MA25"], label="25日移動平均")
plt.plot(data["MA75"], label="75日移動平均")
plt.title(f"{ticker} 株価推移（過去６ヶ月)")
plt.xlabel("日付")
plt.ylabel("株価（円")
plt.legend()
plt.savefig("stock_chart.png")

