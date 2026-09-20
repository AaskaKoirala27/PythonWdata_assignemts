
# main.py

from data import sales_data

import condition
import loop
import function
import io_file


# ==================================================
# SALES DATA ANALYZER
# ==================================================

print("========================================")
print("        SALES DATA ANALYZER")
print("========================================")


# ==================================================
# LOAD PREVIOUSLY ADDED TRANSACTIONS
# ==================================================

# Get transactions that were saved during previous runs
saved_transactions = io_file.load_transactions()


# Add previously saved transactions to the main dataset
for saved_transaction in saved_transactions:

    # Create a new numeric key
    new_number = max(sales_data.keys()) + 1

    sales_data[new_number] = saved_transaction


# ==================================================
# ASK USER WHETHER TO ADD A NEW TRANSACTION
# ==================================================

add_transaction = input(
    "\nDo you want to add a new transaction? (yes/no): "
).lower()


# ==================================================
# ADD NEW TRANSACTION
# ==================================================

if add_transaction == "yes":

    print("\nEnter New Transaction Details")
    print("----------------------------------------")


    # --------------------------------------------------
    # TRANSACTION ID VALIDATION
    # --------------------------------------------------

    while True:

        transaction_id = input("Transaction ID: ")

        # Assume that the ID does not exist
        id_exists = False

        # Check all existing transactions
        for transaction in sales_data.values():

            if transaction["Transaction_ID"] == transaction_id:

                id_exists = True
                break

        # If ID already exists
        if id_exists:

            print(
                "Invalid ID: Transaction ID already exists."
            )

            print(
                "Please enter a different Transaction ID."
            )

        # If ID is unique
        else:

            break


    # --------------------------------------------------
    # OTHER TRANSACTION DETAILS
    # --------------------------------------------------

    date = input("Date (YYYY-MM-DD): ")

    city = input("City: ")


    # --------------------------------------------------
    # CUSTOMER GENDER
    # --------------------------------------------------

    customer_gender = input(
        "Customer Gender (Male/Female): "
    ).capitalize()


    # Keep asking until valid gender is entered
    while customer_gender not in ["Male", "Female"]:

        print(
            "Invalid gender. Please enter Male or Female."
        )

        customer_gender = input(
            "Customer Gender (Male/Female): "
        ).capitalize()


    # --------------------------------------------------
    # CUSTOMER AGE
    # --------------------------------------------------

    while True:

        try:

            customer_age = int(
                input("Customer Age: ")
            )

            if customer_age <= 0:

                print(
                    "Invalid age. Please enter a positive number."
                )

            else:

                break

        except ValueError:

            print(
                "Invalid input. Age must be a number."
            )


    # --------------------------------------------------
    # PRODUCT DETAILS
    # --------------------------------------------------

    product_category = input(
        "Product Category: "
    )

    product_name = input(
        "Product Name: "
    )


    # --------------------------------------------------
    # QUANTITY
    # --------------------------------------------------

    while True:

        try:

            quantity = int(
                input("Quantity: ")
            )

            if quantity <= 0:

                print(
                    "Invalid quantity. "
                    "Please enter a positive number."
                )

            else:

                break

        except ValueError:

            print(
                "Invalid input. Quantity must be a number."
            )


    # --------------------------------------------------
    # UNIT PRICE
    # --------------------------------------------------

    while True:

        try:

            unit_price = float(
                input("Unit Price (NPR): ")
            )

            if unit_price <= 0:

                print(
                    "Invalid price. "
                    "Please enter a positive number."
                )

            else:

                break

        except ValueError:

            print(
                "Invalid input. Price must be a number."
            )


    # --------------------------------------------------
    # PAYMENT METHOD
    # --------------------------------------------------

    payment_method = input(
        "Payment Method: "
    )


    # --------------------------------------------------
    # SALES AMOUNT
    # --------------------------------------------------

    while True:

        try:

            sales = float(
                input("Sales (NPR): ")
            )

            if sales <= 0:

                print(
                    "Invalid sales amount. "
                    "Please enter a positive number."
                )

            else:

                break

        except ValueError:

            print(
                "Invalid input. Sales must be a number."
            )


    # --------------------------------------------------
    # CUSTOMER TYPE
    # --------------------------------------------------

    customer_type = input(
        "Customer Type (New/Returning): "
    )


    # ==================================================
    # CREATE NEW TRANSACTION
    # ==================================================

    new_transaction = {

        "Transaction_ID": transaction_id,

        "Date": date,

        "City": city,

        "Customer_Gender": customer_gender,

        "Customer_Age": customer_age,

        "Product_Category": product_category,

        "Product_Name": product_name,

        "Quantity": quantity,

        "Unit_Price_NPR": unit_price,

        "Payment_Method": payment_method,

        "Sales_NPR": sales,

        "Customer_Type": customer_type
    }


    # ==================================================
    # ADD TRANSACTION TO CURRENT DATA
    # ==================================================

    new_number = max(sales_data.keys()) + 1

    sales_data[new_number] = new_transaction


    # ==================================================
    # SAVE TRANSACTION PERMANENTLY
    # ==================================================

    io_file.save_transaction(new_transaction)


    print("\nNew transaction added successfully!")
    print("The transaction has been saved permanently.")


# ==================================================
# IF USER DOES NOT WANT TO ADD DATA
# ==================================================

elif add_transaction == "no":

    print("\nUsing the existing sales data.")


# ==================================================
# INVALID YES/NO INPUT
# ==================================================

else:

    print("\nInvalid choice.")
    print("Using the existing sales data.")


# ==================================================
# MODULE 1
# CONDITIONAL STATEMENT
# ==================================================

male_count, female_count = condition.count_gender(
    sales_data
)


# ==================================================
# MODULE 2
# LOOP
# ==================================================

total_sales, average_sales = loop.calculate_sales(
    sales_data
)


# ==================================================
# MODULE 3
# CUSTOM FUNCTION
# ==================================================

category_count, popular_category, popular_count = (
    function.category_analysis(sales_data)
)


# ==================================================
# DISPLAY RESULTS
# ==================================================

print("\n========================================")
print("         SALES ANALYSIS RESULTS")
print("========================================")

print(
    f"Total Sales: NPR {total_sales:.2f}"
)

print(
    f"Average Sales: NPR {average_sales:.2f}"
)

print(
    f"Total Male Customers: {male_count}"
)

print(
    f"Total Female Customers: {female_count}"
)

print(
    f"Most Popular Product Category: "
    f"{popular_category}"
)

print(
    f"Number of Transactions in "
    f"{popular_category}: {popular_count}"
)


# ==================================================
# DISPLAY ALL CATEGORY COUNTS
# ==================================================

print("\nTransactions per Product Category:")

for category, count in category_count.items():

    print(
        f"{category}: {count}"
    )


# ==================================================
# MODULE 4
# FILE I/O
# ==================================================

io_file.write_report(
    total_sales,
    average_sales,
    male_count,
    female_count,
    popular_category,
    popular_count,
    category_count
)


# Read the report from the saved file
report = io_file.read_report()


# ==================================================
# DISPLAY SAVED FILE REPORT
# ==================================================

print("\n========================================")
print("          SAVED FILE REPORT")
