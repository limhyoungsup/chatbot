from openai import OpenAI
import streamlit as st

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password",
                                   value="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")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"

assistant_id = "asst_TCsmMlFY3OJEifrwy5jSoEht"

thread_id = "thread_cL9wDeQKqO4rujnrQU1AjBya"

st.title("💬 보도자료 만드는 Chatbot")
st.caption("🚀 A ChatGPT chatbot made by Baiverse")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "보도자료를 작성할 내용을 적어주세요"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    client = OpenAI(api_key=openai_api_key)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(model="gpt-4", messages=st.session_state.messages)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)