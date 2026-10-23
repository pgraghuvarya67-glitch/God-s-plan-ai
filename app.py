import streamlit as st
from google import genai

st.set_page_config(
    page_title="GOD'S PLAN AI",
    page_icon="🙏"
)

st.title("🙏 GOD'S PLAN AI")
st.write("Welcome, bro! Ask me anything.")

st.caption("Your personal AI chatbot 🤖")

question = st.chat_input("Type your question here...")

if question:
    with st.chat_message("user"):
        st.write(question)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                client = genai.Client(
                    api_key=st.secrets["GEMINI_API_KEY"]
                )

                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=question
                )

                st.write(response.text)

            except Exception:
                st.error(
                    "Sorry bro! Something went wrong. "
                    "Please try again."
                )
