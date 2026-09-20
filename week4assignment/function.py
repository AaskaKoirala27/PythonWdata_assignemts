
# function.py


def category_analysis(sales_data):
    """
    Count the number of transactions for each product category
    and find the most popular product category.
    """

    # Empty dictionary to store category counts
    category_count = {}

    # Go through every transaction
    for transaction in sales_data.values():

        # Get the product category
        category = transaction["Product_Category"]

        # If category already exists, increase its count
        if category in category_count:
            category_count[category] += 1

        # If category does not exist, create it
        else:
            category_count[category] = 1

    # Variables for finding the most popular category
    popular_category = None
    highest_count = 0

    # Check every category
    for category, count in category_count.items():

        if count > highest_count:
            highest_count = count
            popular_category = category

    return category_count, popular_category, highest_count
