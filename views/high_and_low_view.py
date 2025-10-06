import streamlit as st
import pandas as pd

def run_ui(game_class):
    st.title("♦ High and Low Game ♠")

    # --- 初期化 ---
    if "game" not in st.session_state:
        st.session_state.game = game_class()

    game = st.session_state.game

    # --- 終了チェック ---
    if game.is_finished():
        st.subheader("🎮 ゲーム終了")
        st.write(f"💰 最終チップ: **{game.chips}**")

        # 勝敗判定
        if game.chips > 100:
            st.success("🏆 あなたの勝ちです！ 🎉")
        else:
            st.error("😢 あなたの負けです…")

        # 履歴表示
        df = pd.DataFrame(game.history)
        st.table(df)

        if st.button("🔄 もう一回！"):
            st.session_state.game = game_class()
            st.rerun()
        st.stop()


    # --- 勝負前 UI ---
    if not game.is_round_finished():
        st.write(f"💰 現在のチップ: {game.chips}")
        st.write(f"🔢 ラウンド: {game.round}/3")

        bet = st.number_input(
            "ベット額を入力してください",
            min_value=1,
            max_value=game.chips,
            value=game.bet,
            step=1
        )

        base_card = game.draw_base_card()
        st.write(f"🃏 ベースカード: {base_card}")

        choice = st.radio("選択してください", ["High", "Draw", "Low"])

        if st.button("🔥 勝負！"):
            game.play_round(choice, bet)
            st.rerun()

    # --- 勝負後 UI ---
    else:
        st.write(f"結果カード: {game.result_card}")

        bet = game.history[-1]["bet"]
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
