import streamlit as st

st.set_page_config(page_title="Welcome to Streamlit", layout="wide")
st.title("Welcome to Streamlit!")
st.write("This is a simple Streamlit app to welcome users and collect their names.")

name = st.text_input("Enter your name:")
if st.button("Submit"): 
    st.write("Hello,", name," welcome to the app!")
