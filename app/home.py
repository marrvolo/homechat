import streamlit as st

from utils import persist, load_widget_state, nav_page
from collections import deque

# Load from existing widget state
load_widget_state()

st.set_page_config(initial_sidebar_state="collapsed", layout="wide")

st.write("## 输入 OpenaiAPI Key:")
st.text_input("apikey", key="apikey", label_visibility="hidden")

if st.button("GO"):
    st.session_state["humanchat"] = deque(["Hi, who are you?"])
    st.session_state["botchat"] = deque(["I'm a chatbot with chatgpt API. How can I help you?"])

    persist("apikey")
    persist("botchat")
    persist("humanchat")
    nav_page("chat")