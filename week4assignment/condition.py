
# condition.py


def count_gender(sales_data):
    """
    Count the number of male and female customers.
    Uses conditional statements.
    """

    male_count = 0
    female_count = 0

    # Go through every transaction
    for transaction in sales_data.values():

        # Check whether the customer is male
        if transaction["Customer_Gender"] == "Male":
            male_count += 1

        # Check whether the customer is female
        elif transaction["Customer_Gender"] == "Female":
            female_count += 1

    return male_count, female_count
