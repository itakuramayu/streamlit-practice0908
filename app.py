import streamlit as st

# st.title("掛け算")
# st.write("入力した数字を掛け算します。")
# st.write("１つ目の数字を入力してください")
# a=st.number_input("Insert a number")
# st.write("2つ目の数字を入力してください")
# b=st.number_input("Insert a number")
# st.write("計算結果は",a*b)

qp = st.query_params
round_num = int(qp.get("round", "1"))  # なければ 1
st.write(f"現在のラウンド: {round_num}")

if st.button("次のラウンドへ"):
    round_num += 1
    st.query_params["round"] = str(round_num)  # URLを更新
    st.write(f"次のラウンドは {round_num} です")