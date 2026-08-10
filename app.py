import streamlit as st
import yfinance as yf 
import matplotlib.pyplot as plt 

#日本語フォント指定
plt.rcParams["font.family"] = "Noto Sans CJK JP"

st.title("株価分析ツール")
st.write("銘柄コードを入力して、株価の推移と移動平均線を確認できます。")

#ユーザー入力
ticker = st.text_input("銘柄コード（例:7203.T トヨタ自動車", "7203.T")
period = st.selectbox("期間", ["1mo", "3mo", "6mo", "1y", "2y"], index=2)

if st.button("株価を取得"):
    data = yf.download(ticker, period=period)

    if data.empty:
        st.error("データを取得できませんでした。銘柄コードを確認してください。")
    else:
        #移動平均線を計算
        data["MA25"] = data["Close"].rolling(window=25).mean()
        data["MA75"] = data["Close"].rolling(window=75).mean() 

        #グラフ描画
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(data["Close"], label="終値")
        ax.plot(data["MA25"], label="25日移動平均") 
        ax.plot(data["MA75"], label="75日移動平均")    
        ax.set_title(f"{ticker} 株価推移")
        ax.set_xlabel("日付")
        ax.set_ylabel("株価（円")
        ax.legend()

        st.pyplot(fig)

        #最新の株価情報も表示
        st.subheader("最新データ")
        st.dataframe(data.tail(5))
        