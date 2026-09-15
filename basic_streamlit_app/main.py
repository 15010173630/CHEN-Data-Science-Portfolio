import streamlit as st
import pandas as pd

# Page title and a short description of the app
st.title("Video Game Sales Explorer")
st.write("Explore video game sales data and filter the games by platform.")

# Load the Video Game Sales CSV file
df = pd.read_csv("data/vgsales.csv")