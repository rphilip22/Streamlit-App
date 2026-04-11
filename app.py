import streamlit as st

st.title("Budget Tracker")

st.write("Track your income and expenses easily.")

# Input 1: Transaction type
transaction_type = st.radio(
    "Select transaction type:",
    ["Income", "Expense"]
)

# Input 2: Amount
amount = st.number_input("Enter amount ($):", min_value=0.0, step=1.0)

# Input 3: Category
if transaction_type == "Income":
    category = st.selectbox(
        "Select category:",
        ["Salary", "Gift", "Other"]
    )
else:
    category = st.selectbox(
        "Select category:",
        ["Education","Food", "Transport", "Entertainment", "Other"]
    )

# Button
if st.button("Add Transaction"):

    if amount == 0:
        st.error("Please enter a valid amount.")
    else:
        # Save to CSV
        with open(file_name, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([transaction_type, amount, category])

        # Output
        st.write(f"{transaction_type} of ${amount} recorded under {category}.")

        if transaction_type == "Expense" and amount > 100:
            st.warning("⚠️ High expense!")
        else:
            st.success("✅ Transaction recorded!")

try:
    data = pd.read_csv(file_name)
    st.subheader("Transaction History")
    st.dataframe(data)
except:
    st.write("No data yet.")