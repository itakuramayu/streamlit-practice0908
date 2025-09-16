import streamlit as st
import random
st.title("♦ High and Low Game ♠")
# st.title("掛け算")
# st.write("入力した数字を掛け算します。")
# st.write("１つ目の数字を入力してください")
# a=st.number_input("Insert a number")
# st.write("2つ目の数字を入力してください")
# b=st.number_input("Insert a number")
# st.write("計算結果は",a*b)

# qp = st.query_params
# round_num = int(qp.get("round", "1"))  # なければ 1
# st.write(f"現在のラウンド: {round_num}")

# if st.button("次のラウンドへ"):
#     round_num += 1
#     st.query_params["round"] = str(round_num)  # URLを更新
#     st.write(f"次のラウンドは {round_num} です")import streamlit as st

# --- セッション状態の初期化 ---
if "round" not in st.session_state:
    st.session_state.round = 1
    st.session_state.wins = 0
    st.session_state.finished = False
    st.session_state.last_result = None  # 直前の勝負結果を保持

# --- ゲームが終わっていないとき ---
if not st.session_state.finished:
    st.write(f"第 {st.session_state.round} 回戦 / 全5回戦")

    # まだ勝負していないときだけカードを配る
    if st.session_state.last_result is None:
        st.session_state.my_card = random.randint(1, 13)
        st.session_state.opponent_card = random.randint(1, 13)

    st.write(f"あなたのカード: {st.session_state.my_card}")

    choice = st.radio(
        "あなたのカードは、相手のカードより…",
        ("大きい", "小さい", "同じ"),
        key=f"choice_{st.session_state.round}"
    )

    # 勝負ボタン
    if st.button("勝負！", key=f"fight_{st.session_state.round}"):
        opponent_card = st.session_state.opponent_card
        my_card = st.session_state.my_card
        st.write(f"相手のカード: {opponent_card}")

        result = None
        if opponent_card > my_card and choice == "大きい":
            result = "win"
        elif opponent_card < my_card and choice == "小さい":
            result = "win"
        elif opponent_card == my_card and choice == "同じ":
            result = "win"

        if result == "win":
            st.success("勝ち！")
            st.session_state.wins += 1
        else:
            st.error("負け…")

        st.session_state.last_result = "done"  # このラウンドは終了済み

    # 勝負済みのときに次に進むボタンを出す
    if st.session_state.last_result == "done":
        if st.session_state.round < 5:
            if st.button("➡ 次のラウンドへ"):
                st.session_state.round += 1
                st.session_state.last_result = None
                st.rerun()
        else:
            if st.button("📢 結果発表！！"):
                st.session_state.finished = True
                st.session_state.last_result = None
                st.rerun()

# --- 全5回終わったときの結果表示 ---
else:
    st.write(" 全5回戦 結果 🌟")
    st.write(f"勝利数: {st.session_state.wins} / 5")

    if st.session_state.wins >= 3:
        st.success("あなたの勝ちです！👏🎉")
    else:
        st.error("あなたの負けです…😢")

    # もう一回！
    if st.button("もう一回！"):
        st.session_state.round = 1
        st.session_state.wins = 0
        st.session_state.finished = False
        st.session_state.last_result = None
        st.rerun()
