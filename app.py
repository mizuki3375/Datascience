import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# タイトルと説明を追加
st.title("データ分析ダッシュボード")
st.write("このダッシュボードでは、CSVファイルをアップロードしてデータを分析することができます。")

# CSVファイルのアップロード
uploaded_file = st.file_uploader("CSVファイルをアップロードしてください", type=["csv"])

if uploaded_file is not None:
    # CSVファイルをDataFrameに読み込む
    df = pd.read_csv(uploaded_file)
    
    # データの表示
    st.write("アップロードされたデータのプレビュー:")
    st.write(df.head())

    # 基本統計情報の表示
    st.write("基本統計情報:")
    st.write(df.describe())

    # グラフ表示のための列選択
    st.write("グラフを作成する列を選択してください:")
    x_column = st.selectbox("X軸の列", df.columns)
    y_column = st.selectbox("Y軸の列", df.columns)

    # 折れ線グラフの作成
    st.write(f"{x_column} と {y_column} の折れ線グラフ:")
    fig, ax = plt.subplots()
    ax.plot(df[x_column], df[y_column])
    st.pyplot(fig)

    # ヒストグラムの作成
    st.write(f"{y_column} のヒストグラム:")
    fig, ax = plt.subplots()
    ax.hist(df[y_column], bins=20)
    st.pyplot(fig)

else:
    st.write("CSVファイルをアップロードしてください。")
