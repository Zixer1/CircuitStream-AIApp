import streamlit as st
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

with st.chat_message("user"):
    st.write(f"Hello, I am alex! Welcome to AI Level 2.")
with st.chat_message("assistant"):
    st.write(f"Hello {name}, I am Zeus! Welcome to AI Level 2.")

prompt = st.chat_input("Ask something here...")
if prompt:
    with st.chat_message("user"):
        st.write(prompt)
