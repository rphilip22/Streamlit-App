import streamlit as st

# Title
st.title("Personal Finance Tracker")

# Description
st.write("This app helps students track their daily expenses and understand their spending habits.")

# Input 1: Expense Amount Input
amount = st.number_input("Enter expense amount ($):", min_value=0.0, step=1.0)

# Input 2: Category Selection
category = st.selectbox(
    "Select expense category:",
    ["Education", "Housing", "Food", "Transport", "Entertainment", "Subscriptions", "Miscellaneous"]
)

# Input Processing and Output Production
if st.button("Add Expense"):
    # Dynamic output
    st.write(f"You spent ${amount} on {category}.")

    # Simple Conditional Logic
    if amount > 50:
        st.warning("That is a high expense! Try to save more.")
    else:
        st.success("Expense recorded successfully!")