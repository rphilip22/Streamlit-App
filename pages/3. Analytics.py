import streamlit as st
from data_utils import load_data

st.set_page_config(page_title="Analytics", layout="wide")

st.title("Financial Analytics")

data = load_data()

if data.empty:
    st.write("No data available.")
else:
    # Calculate totals
    income = data[data["Type"] == "Income"]["Amount"].sum()
    expenses = data[data["Type"] == "Expense"]["Amount"].sum()

    # Bar chart
    st.subheader("Income vs Expenses")
    st.bar_chart({"Income": income, "Expenses": expenses})

    # Expense breakdown
    st.subheader("Expense Breakdown")

    expense_data = data[data["Type"] == "Expense"]

    if not expense_data.empty:
        category_totals = expense_data.groupby("Category")["Amount"].sum()
        st.bar_chart(category_totals)
    else:
        st.write("No expense data yet.")