import streamlit as st
st.title("Hello, streamlit!")
st.write("This is my first streamlit app.")

if st.button("Click me!"):
    st.write("🎉 You clicked the button! Nice work! 🚀")
else:
    st.write("Click the button to see what happens...")