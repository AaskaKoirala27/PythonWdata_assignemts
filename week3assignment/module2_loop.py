# Module 2: Loop Statement

def process_customers(data):

    total_sales = 0
    male_customers = 0
    female_customers = 0

    for customer in data:

        total_sales = total_sales + customer["sales"]

        if customer["gender"] == "Male":
            male_customers = male_customers + 1

        elif customer["gender"] == "Female":
            female_customers = female_customers + 1

    return total_sales, male_customers, female_customers




