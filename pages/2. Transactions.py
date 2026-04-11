import streamlit as st
from data_utils import load_data

st.set_page_config(page_title="Transactions", layout="wide")

st.title("📜 Transaction History")

data = load_data()

if data.empty:
    st.write("No transactions yet.")
else:
    st.dataframe(data)

    st.write(f"Total Transactions: {len(data)}")