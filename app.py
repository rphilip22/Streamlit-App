import streamlit as st

st.title("Student Budget Tracker")

st.write("Track your income and expenses easily.")

# Input 1: Transaction type
transaction_type = st.radio(
    "Select transaction type:",
    ["Income", "Expense"]
)

# Input 2: Amount
amount = st.number_input("Enter amount ($):", min_value=0.0, step=1.0)

# Input 3: Category
category = st.selectbox(
    "Select category:",
    ["Salary", "Food", "Transport", "Entertainment", "Other"]
)

# Button
if st.button("Add Transaction"):
    st.write(f"{transaction_type} of ${amount} recorded under {category}.")

    if transaction_type == "Expense" and amount > 100:
        st.warning("⚠️ High expense!")
    else:
        st.success("✅ Transaction recorded!")