import streamlit as st

st.set_page_config(page_title="Welcome to Streamlit", layout="wide")
st.title("Welcome to Streamlit!")
name = st.text_input("Enter your name:")
st.button("Submit", on_click=lambda: st.write("Hello,", name," welcome to the app!"))
st.write("This is a simple Streamlit app to welcome users and collect their names.")
