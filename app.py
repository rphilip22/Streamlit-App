import streamlit as st
from data_utils import load_data, save_transaction

st.set_page_config(page_title="Student Budget Tracker", layout="wide")

# --- CENTERED TITLE ---
st.markdown("<h1 style='text-align: center;'>Student Budget Tracker</h1>", unsafe_allow_html=True)

# --- PAGE SELECTOR (TOP) ---
page = st.radio(
    "",
    ["Overview", "Transactions", "Analytics", "Insights"],
    horizontal=True
)

# --- PAGE TITLE ---
st.markdown(f"<h3 style='text-align: center;'>{page}</h3>", unsafe_allow_html=True)

# Load data
data = load_data()

# ====================================================================================================
# PAGE 1: OVERVIEW
# ====================================================================================================
if page == "Overview":

    income = data[data["Type"] == "Income"]["Amount"].sum()
    expenses = data[data["Type"] == "Expense"]["Amount"].sum()
    balance = income - expenses

    st.subheader("📊 Summary")

    col1, col2, col3 = st.columns(3)

    col1.metric("Income", f"${income:,.2f}")
    col2.metric("Expenses", f"${expenses:,.2f}")
    col3.metric("Balance", f"${balance:,.2f}")

    # Status message
    if balance > 0:
        st.success("🟢 You're saving money")
    elif balance < 0:
        st.error("🔴 You're overspending")
    else:
        st.warning("🟡 You're breaking even")

    st.subheader("➕ Add Transaction")

    transaction_type = st.radio("Type:", ["Income", "Expense"])
    amount = st.number_input("Amount ($):", min_value=0.0, step=1.0)
    description = st.text_input("Description (optional):")

    if transaction_type == "Income":
        category = st.selectbox("Category:", ["Salary", "Gift", "Other"])
    else:
        category = st.selectbox("Category:", ["Education", "Food", "Subscriptions", "Transport", "Entertainment", "Other"])

    if st.button("Add Transaction"):
        if amount == 0:
            st.error("Please enter a valid amount.")
        else:
            save_transaction(transaction_type, description, amount, category, )
            st.success("✅ Transaction added!")

            st.rerun()

# ====================================================================================================
# PAGE 2: TRANSACTIONS
# ====================================================================================================
elif page == "Transactions":

    if data.empty:
        st.write("No transactions yet.")
    else:
        st.write(f"Total Transactions: {len(data)}")
        st.dataframe(data)

# ====================================================================================================
# PAGE 3: ANALYTICS
# ====================================================================================================
elif page == "Analytics":

    if data.empty:
        st.write("No data available.")
    else:
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

# ====================================================================================================
# PAGE 4: INSIGHTS
# ====================================================================================================
elif page == "Insights":
        expense_data = data[data["Type"] == "Expense"]
        income = data[data["Type"] == "Income"]["Amount"].sum()
        expenses = data[data["Type"] == "Expense"]["Amount"].sum()
        balance = income - expenses

        if not expense_data.empty:
            most_common_category = expense_data.groupby("Category").size().idxmax() # Most common expense category
            st.write(f"Your most common expense category is: {most_common_category}")

            highest_expense_category = expense_data.groupby("Category")["Amount"].sum().idxmax() # Highest expense category by amount
            st.write(f"You spent the most on: {highest_expense_category}")

        #Show savings rate as a smart insight
        if income > 0:
            savings_rate = (balance / income) * 100

            if savings_rate > 30:
                st.success(f"Great job! You are saving {savings_rate:.1f}% of your income.")
            elif savings_rate > 10:
                st.warning(f"You are saving {savings_rate:.1f}%. Try to increase it.")
            else:
                st.error(f"Your savings rate is low ({savings_rate:.1f}%). Consider cutting expenses.")


            st.header("WORK IN PROGRESS...")
        
        else:
            st.write("No expenses recorded yet.")

# ====================================================================================================