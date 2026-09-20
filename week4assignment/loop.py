
# loop.py


def calculate_sales(sales_data):
    """
    Calculate total sales and average sales.
    Uses a loop to go through all transactions.
    """

    total_sales = 0
    transaction_count = 0

    # Loop through every transaction
    for transaction in sales_data.values():

        # Add the sales amount
        total_sales += transaction["Sales_NPR"]

        # Count the transaction
        transaction_count += 1

    # Avoid division by zero
    if transaction_count > 0:
        average_sales = total_sales / transaction_count
    else:
        average_sales = 0

    return total_sales, average_sales
