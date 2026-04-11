import streamlit as st
from data_utils import load_data, save_transaction

st.set_page_config(page_title="Budget Tracker", layout="wide")

st.title("💰 Budget Tracker")
st.write("Track your income and expenses easily.")

# Load data
data = load_data()

# Calculate stats
income = data[data["Type"] == "Income"]["Amount"].sum()
expenses = data[data["Type"] == "Expense"]["Amount"].sum()
balance = income - expenses

# Sidebar summary
st.sidebar.header("📊 Summary")
st.sidebar.metric("Income", f"${income:.2f}")
st.sidebar.metric("Expenses", f"${expenses:.2f}")
st.sidebar.metric("Balance", f"${balance:.2f}")

# Status message
if balance > 0:
    st.sidebar.success("🟢 You're saving money")
elif balance < 0:
    st.sidebar.error("🔴 You're overspending")
else:
    st.sidebar.warning("🟡 You're breaking even")

# Input section
st.subheader("Add Transaction")

transaction_type = st.radio("Type:", ["Income", "Expense"])
amount = st.number_input("Amount ($):", min_value=0.0, step=1.0)

if transaction_type == "Income":
    category = st.selectbox("Category:", ["Salary", "Gift", "Other"])
else:
    category = st.selectbox("Category:", ["Food", "Transport", "Entertainment", "Other"])

# Save button
if st.button("Add Transaction"):
    if amount == 0:
        st.error("Please enter a valid amount.")
    else:
        save_transaction(transaction_type, amount, category)
        st.success("✅ Transaction added!")

# Optional: show recent data
st.subheader("Recent Transactions")
st.dataframe(data.tail(5))