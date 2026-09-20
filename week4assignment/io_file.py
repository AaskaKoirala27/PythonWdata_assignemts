
# io_file.py

import json
import os


# ==================================================
# SAVE NEW TRANSACTION
# ==================================================

def save_transaction(transaction):
    """
    Saves a newly added transaction permanently
    into added_transactions.json.
    """

    filename = "added_transactions.json"

    # Check if the JSON file already exists
    if os.path.exists(filename):

        # Open the existing file and read its data
        with open(filename, "r") as file:
            transactions = json.load(file)

    else:
        # If the file does not exist,
        # start with an empty list
        transactions = []

    # Add the new transaction
    transactions.append(transaction)

    # Save the updated transactions
    with open(filename, "w") as file:
        json.dump(transactions, file, indent=4)


# ==================================================
# LOAD PREVIOUSLY SAVED TRANSACTIONS
# ==================================================

def load_transactions():
    """
    Loads previously saved transactions from
    added_transactions.json.
    """

    filename = "added_transactions.json"

    # If the file does not exist,
    # return an empty list
    if not os.path.exists(filename):
        return []

    try:

        # Open the JSON file
        with open(filename, "r") as file:
            transactions = json.load(file)

        return transactions

    except json.JSONDecodeError:

        # If the JSON file is empty or damaged,
        # return an empty list
        print("Warning: Could not read saved transactions.")
        return []


# ==================================================
# WRITE SALES REPORT
# ==================================================

def write_report(total_sales, average_sales,
                 male_count, female_count,
                 popular_category, popular_count,
                 category_count):
    """
    Writes the complete sales analysis report
    into sales_report.txt.
    """

    with open("sales_report.txt", "w") as file:

        file.write("========================================\n")
        file.write("          SALES ANALYSIS REPORT\n")
        file.write("========================================\n")

        file.write(
            f"Total Sales: NPR {total_sales:.2f}\n"
        )

        file.write(
            f"Average Sales: NPR {average_sales:.2f}\n"
        )

        file.write(
            f"Total Male Customers: {male_count}\n"
        )

        file.write(
            f"Total Female Customers: {female_count}\n"
        )

        file.write(
            f"Most Popular Product Category: "
            f"{popular_category}\n"
        )

        file.write(
            f"Number of Transactions in "
            f"{popular_category}: {popular_count}\n"
        )

        file.write("\n")

        file.write(
            "Transactions per Product Category:\n"
        )

        # Write every category and its count
        for category, count in category_count.items():

            file.write(
                f"{category}: {count}\n"
            )

        file.write(
            "========================================\n"
        )


# ==================================================
# READ SALES REPORT
# ==================================================

def read_report():
    """
    Reads the saved sales report.
    """

    with open("sales_report.txt", "r") as file:

        report = file.read()

    return report
