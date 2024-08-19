import streamlit as st

# 初期設定
if 'step' not in st.session_state:
    st.session_state.step = 1
    st.session_state.answers = []
    st.session_state.guess = None

# 質問リスト（シンプルな例）
questions = [
    "それは生き物ですか？",
    "それはフィクションのキャラクターですか？",
    "それは人間ですか？",
    "それは映画に出てきますか？"
]

# 簡単な推測アルゴリズム（サンプルのために簡単なロジックを使用）
def make_guess(answers):
    if answers == [True, True, True, True]:
        return "あなたが考えているのは、スーパーマンです！"
    elif answers == [True, True, True, False]:
        return "あなたが考えているのは、ハリーポッターです！"
    elif answers == [True, True, False, True]:
        return "あなたが考えているのは、キングコングです！"
    else:
        return "まだ正確に当てられませんでした。"

# 質問を進める
if st.session_state.step <= len(questions):
    question = questions[st.session_state.step - 1]
    st.write(f"質問 {st.session_state.step}: {question}")
    
    yes = st.button("はい")
    no = st.button("いいえ")

    if yes:
        st.session_state.answers.append(True)
        st.session_state.step += 1
    elif no:
        st.session_state.answers.append(False)
        st.session_state.step += 1
else:
    if st.session_state.guess is None:
        st.session_state.guess = make_guess(st.session_state.answers)
    
    st.write(st.session_state.guess)
    restart = st.button("もう一度プレイ")

    if restart:
        st.session_state.step = 1
        st.session_state.answers = []
        st.session_state.guess = None
