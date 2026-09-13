# Module 3: Custom Functions

def calculate_average(total_sales, number_of_customers):

    if number_of_customers > 0:
        average = total_sales / number_of_customers
        return average

    else:
        return 0


def popular_category(data):

    categories = {}

    for customer in data:

        category = customer["category"]

        if category in categories:
            categories[category] = categories[category] + 1

        else:
            categories[category] = 1

    most_popular = max(categories, key=categories.get)

    return most_popular

