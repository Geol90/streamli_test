import streamlit as st

st.title("Hello World")
st.write("*Data Science Course 2024*")


import pandas as pd
df = pd.read_csv('data/Bastar Craton(1).csv')

st.dataframe(df)