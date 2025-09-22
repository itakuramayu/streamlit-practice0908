import streamlit as st
import pandas as pd
import os
import sys
sys.path.append(os.getcwd())
from model.high_and_low import HighLowGame

st.title("♦ High and Low Game ♠")

# --- 初期化 ---
if "game" not in st.session_state:
    st.session_state.game = HighLowGame()

game = st.session_state.game

# --- 終了チェック ---
if game.is_finished():
    st.subheader("🎮 ゲーム終了")
    st.write(f"最終チップ: {game.chips}")
    df = pd.DataFrame(game.history)
    st.table(df)

    if st.button("🔄 もう一回！"):
        st.session_state.game = HighLowGame()
        st.rerun()
    st.stop()

# --- 状態表示 ---
st.write(f"💰 現在のチップ: {game.chips}")
st.write(f"🔢 ラウンド: {game.round}/3")

# --- ベット額入力 ---
bet = st.number_input(
    "ベット額を入力してください",
    min_value=1,
    max_value=game.chips,
    value=game.bet,
    step=1
)

# --- ベースカード表示 ---
base_card = game.draw_base_card()
st.write(f"🃏 ベースカード: {base_card}")

# --- 選択肢 ---
choice = st.radio("選択してください", ["High", "Draw", "Low"])

# --- 勝負ボタン ---
if st.button("🔥 勝負！") and game.outcome is None:
    outcome, result_card = game.play_round(choice, bet)

# --- 結果表示 ---
if game.outcome is not None:
    st.write(f"結果カード: {game.result_card}")
    if game.outcome == "win":
        st.success(f"🎉 勝ち！ +{bet}チップ")
    elif game.outcome == "draw":
        st.info("🤝 引き分け（チップ変動なし）")
    else:
        st.error(f"💀 負け！ -{bet}チップ")

    st.write(f"💰 現在のチップ: {game.chips}")

    next_label = "結果発表へ" if game.round == 3 else "➡ 次のラウンドへ"
    if st.button(next_label):
        game.next_round(bet)
        st.rerun()
