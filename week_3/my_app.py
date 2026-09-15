import streamlit as st
st.title("Hello, streamlit!")
st.write("This is my first streamlit app.")

if st.button("Click me!"):
    st.write("🎉 You clicked the button! Nice work! 🚀")
else:
    st.write("Click the button to see what happens...")

import pandas as pd
st.subheader("Exploring Our Dataset")

df = pd.read_csv("data/sample_data-1.csv")
# if in Week_2 (. out week_3)
# pd.read_csv("./Week_2/sample_data.csv")

st.write("Here's out data")
st.dataframe(df)

city = st.selectbox('Select a city', df["City"].unique())
st.write(f"People in {city}")
st.dataframe(df[df["City"] == city])
st.bar_chart(df["Salary"])
