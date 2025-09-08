import streamlit as st

st.title("掛け算")
st.write("入力した数字を掛け算します。")
st.write("１つ目の数字を入力してください")
a=st.number_input()
st.write("2つ目の数字を入力してください")
b=st.number_input()
st.write(a*b)