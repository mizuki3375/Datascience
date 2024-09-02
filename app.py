import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# タイトルと説明
st.title("データ分析ダッシュボード")

# CSVファイルのアップロード
uploaded_file = st.file_uploader("CSVファイルをアップロードしてください", type=["csv"])

if uploaded_file is not None:
    # CSVファイルを読み込む
    df = pd.read_csv(uploaded_file)
    
    # データの表示
    st.write("データプレビュー:")
    st.write(df.head())

    # グラフ作成のための列選択
    st.write("グラフを作成する列を選択してください:")
    x_column = st.selectbox("X軸の列", df.columns)
    y_column = st.selectbox("Y軸の列", df.columns)

    # グラフタイプの選択
    st.write("グラフの種類を選択してください:")
    graph_type = st.selectbox("グラフの種類", ["折れ線グラフ", "棒グラフ", "散布図", "ヒストグラム"])

    # グラフの作成
    fig, ax = plt.subplots(figsize=(10, 6))
    
    if graph_type == "折れ線グラフ":
        ax.plot(df[x_column], df[y_column])
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
        st.write(f"{x_column} と {y_column} の折れ線グラフ:")

    elif graph_type == "棒グラフ":
        ax.bar(df[x_column], df[y_column])
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
        st.write(f"{x_column} と {y_column} の棒グラフ:")

    elif graph_type == "散布図":
        ax.scatter(df[x_column], df[y_column])
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
        st.write(f"{x_column} と {y_column} の散布図:")

    elif graph_type == "ヒストグラム":
        ax.hist(df[y_column], bins=20)
        st.write(f"{y_column} のヒストグラム:")

    # Streamlitにグラフを表示
    st.pyplot(fig)

else:
    st.write("CSVファイルをアップロードしてください。")
