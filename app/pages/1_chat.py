import streamlit as st
import openai

from collections import deque
from utils import persist, load_widget_state, nav_page
from streamlit_chat import message

load_widget_state()

st.set_page_config(initial_sidebar_state="collapsed", layout="wide")

st.write("<h2 align='center'>聊个天儿</h2>", unsafe_allow_html=True)

if "botchat" not in st.session_state:
    st.session_state["botchat"] = deque(["I'm a chatbot with chatgpt API. How can I help you?"])
if "humanchat" not in st.session_state:
    st.session_state["humanchat"] = deque(["Hi, who are you?"])

while len(st.session_state['botchat']) > 5:
    st.session_state['botchat'].popleft()
while len(st.session_state['humanchat']) > 5:
    st.session_state['humanchat'].popleft()


if "apikey" in st.session_state:
    openai.api_key = st.session_state["apikey"]

def on_click_send(msg):
    def helper():
        message=[{"role": "system", "content": "You are a helpful assistant."}]
        for i in range(len(st.session_state["humanchat"])):
            message.append({"role": "user", "content": st.session_state["humanchat"][i]})
            message.append({"role": "assistant", "content": st.session_state["botchat"][i]})
        message.append({"role": "user", "content": msg})
        st.session_state["humanchat"].append(msg)

        try:
            res = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=message
            )
            botchat = res["choices"][0]["message"]["content"]
            st.session_state["botchat"].append(botchat)
        except:
            st.session_state["botchat"].append("Sorry, I am currently offline, please retry later.")

    return helper

st.session_state["msg"] = st.text_area("Input", label_visibility="hidden")

_, mid, _ = st.columns(3)
mid.button("Send", on_click=on_click_send(st.session_state["msg"]), use_container_width=True)

for i in range(len(st.session_state["humanchat"])-1, -1, -1):
    message(st.session_state["botchat"][i], is_user=False, avatar_style="thumbs", seed="Miss kitty", key=f"b{i}")
    message(st.session_state["humanchat"][i], is_user=True, avatar_style="thumbs", seed="Muffin", key=f"h{i}")








