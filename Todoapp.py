import streamlit as st

st.title("Today's To-do List")

st.subheader("📌 할 일 목록")

if "user_list" not in st.session_state:
    st.session_state.user_list = []

tasks = [
    "1. SQLD 시험 접수",
    "2. AI 리터러시 과제 제출",
    "3. 대학영어 과제 제출"
]

for task in tasks:

    with st.container(border=True):
        st.write(task)

name = st.text_input("오늘의 할 일 추가하기")
btn = st.button("등록")
