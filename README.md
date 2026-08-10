<<<<<<< HEAD
(# 株価分析ツール (Stock Analyzer)
=======
# stock-analyzer
株価データを取得・分析・可視化するツール



# 株価分析ツール (Stock Analyzer)
>>>>>>> 2ef0352b66f238ef0c20e9fe98a3afca619e88e6

指定した銘柄の株価データを取得し、移動平均線を用いてテクニカル分析・可視化するWebアプリです。

## デモ

Streamlit上で銘柄コードと期間を入力すると、株価推移グラフと最新データが表示されます。

## 使用技術

- Python
- yfinance(株価データ取得)
- pandas(データ加工)
- matplotlib(グラフ描画)
- Streamlit(Webアプリ化)

## 機能

- 銘柄コードを入力して株価推移をグラフ表示
- 25日/75日移動平均線の算出・表示
- 期間の選択(1ヶ月〜2年)
- 最新5日分のデータをテーブル表示

## 実行方法

\`\`\`bash
pip install -r requirements.txt
streamlit run app.py
\`\`\`

## 工夫した点

- 日本語フォント対応(matplotlibでのNoto Sans CJK JP設定)
- WSL2環境での開発・動作確認

## 今後の展望

- 複数銘柄の比較表示
- RSIなど追加のテクニカル指標の実装
- 機械学習を用いた株価予測機能

