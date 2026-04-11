import streamlit as st
from data_utils import load_data

st.title("📜 Transaction History")

data = load_data()

st.dataframe(data)

st.write(f"Total Transactions: {len(data)}")