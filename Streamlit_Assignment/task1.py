import streamlit as st
st.title("Welcome To Streamlit!")
st.text_input("Enter your name: ")
greet = st.button("Greet Me!")
if greet:
    st.write("Hello!")