import streamlit as st
import pandas as pd
import os

st.title("📊 Financial Analytics")

file_name = "data.csv"

if not os.path.exists(file_name):
    st.write("No data available.")
else:
    data = pd.read_csv(file_name)

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
        st.write("No expenses yet.")