import pandas as pd
import os
import csv

file_name = "data.csv"

def load_data():
    # Create file if it doesn't exist
    if not os.path.exists(file_name):
        pd.DataFrame(columns=["Type", "Amount", "Category", "Description"]).to_csv(file_name, index=False)

    return pd.read_csv(file_name)


def save_transaction(transaction_type, amount, category, description):
    with open(file_name, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([transaction_type, amount, category, description])