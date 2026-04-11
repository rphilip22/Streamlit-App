import streamlit as st
from data_utils import load_data, save_transaction

data = load_data()

st.title("📊 Analytics")

data = load_data()

income = data[data["Type"] == "Income"]["Amount"].sum()
expenses = data[data["Type"] == "Expense"]["Amount"].sum()

st.subheader("Income vs Expenses")
st.bar_chart({"Income": income, "Expenses": expenses})

st.subheader("Expense Breakdown")

expense_data = data[data["Type"] == "Expense"]

if not expense_data.empty:
    category_totals = expense_data.groupby("Category")["Amount"].sum()
    st.bar_chart(category_totals)
else:
    st.write("No expense data yet.")