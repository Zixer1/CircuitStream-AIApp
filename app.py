import streamlit as st
import requests
import os
from dotenv import load_dotenv
from openai import OpenAI

st.set_page_config(page_title="Zeus AI", page_icon="⚡", layout="wide")

st.title("Welcome to Zeus, our own AI model on the Web!")
st.subheader("This is my first app")
count = 0
with st.sidebar:
    st.header("Settings tab")
    with st.form("settings"):
        name = st.text_input("What is your name?")
        sources = st.multiselect("Mood:", ["My first app", "My second app"])
        creativity = st.slider("Creativity:", 0.0, 1.0, 0.5)
        saved = st.form_submit_button("Save")
    if saved:
        st.write(f"{name} saved sources: {sources} and creativity: {creativity}")

# commit : git commit -m "Added interface options, settings, etc"
# git push -u origin main

prompt = st.chat_input("Ask something here...")

if prompt:
    with st.chat_message("user"):
        st.write(f"{prompt}")
    with st.chat_message("assistant"):
        if prompt == "Cat Fact":
            r = requests.get("https://catfact.ninja/fact")
            fact = r.json()["fact"]
            st.write(f"{fact}")
        else:
            load_dotenv()
            client = OpenAI(
                base_url="https://api.groq.com/openai/v1",
                api_key = os.environ.get("AI_TOKEN") or st.secrets["AI_TOKEN"],
            )
            r = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}],
            )
            st.write(r.choices[0].message.content)