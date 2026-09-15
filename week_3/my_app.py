import streamlit as st
st.title("Hello, streamlit!")
st.write("This is my first streamlit app.")

if st.button("Click me!"):
    st.write("🎉 You clicked the button! Nice work! 🚀")
else:
    st.write("Click the button to see what happens...")

import pandas as pd
st.subheader("Exploring Our Dataset")

df = pd.read_csv("/Users/chenyujun/Documents/GitHub/CHEN-Data-Science-Portfolio/week_3/data/sample_data-1.csv")