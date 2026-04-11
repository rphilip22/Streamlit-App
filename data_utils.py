import pandas as pd
import os

file_name = "data.csv"

def load_data():
    if not os.path.exists(file_name):
        pd.DataFrame(columns=["Type", "Amount", "Category"]).to_csv(file_name, index=False)

    return pd.read_csv(file_name)


def save_transaction(transaction_type, amount, category):
    with open(file_name, "a", newline="") as file:
        import csv
        writer = csv.writer(file)
        writer.writerow([transaction_type, amount, category])