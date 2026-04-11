import streamlit as st
import pandas as pd
import os

st.title("📜 Transaction History")

file_name = "data.csv"

if not os.path.exists(file_name):
    st.write("No data yet.")
else:
    data = pd.read_csv(file_name)

    st.dataframe(data)

    st.write(f"Total Transactions: {len(data)}")