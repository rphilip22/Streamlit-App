import streamlit as st

# Title
st.title("Personal Finance Tracker")

# Description
st.write("This app helps students track their daily expenses and understand their spending habits.")

# Input 1: Expense amount
amount = st.number_input("Enter expense amount ($):", min_value=0.0, step=1.0)

# Input 2: Category selection
category = st.selectbox(
    "Select expense category:",
    ["Education", "Housing", "Food", "Transport", "Entertainment", "Subscriptions", "Miscellaneous"]
)

# Button to process input
if st.button("Add Expense"):
    # Dynamic output
    st.write(f"You spent ${amount} on {category}.")

    # Simple conditional logic
    if amount > 100:
        st.warning("That’s a high expense! Try to save more.")
    else:
        st.success("Expense recorded successfully!")