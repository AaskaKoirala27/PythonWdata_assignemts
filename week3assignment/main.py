# Main Program

from module1_condition import classify_sale
from module2_loop import process_customers
from module3_function import calculate_average, popular_category
from module4_io import read_sales_file, save_customer


# Read existing customer data from file
customers = read_sales_file("cafe_sales.txt")


print("========================================")
print("       MOVIE CAFE SALES ANALYZER")
print("========================================")


# Ask user if they want to add a customer
choice = input("\nDo you want to add a new customer? (yes/no): ")


if choice.lower() == "yes":

    print("\nEnter New Customer Details")

    name = input("Enter customer name: ")
    gender = input("Enter gender (Male/Female): ")
    product = input("Enter product: ")
    category = input("Enter category (Food/Drinks/Snacks): ")
    sales = float(input("Enter sales amount: Rs. "))


    new_customer = {
        "name": name,
        "gender": gender,
        "product": product,
        "category": category,
        "sales": sales
    }


    # Save new customer to file
    save_customer("cafe_sales.txt", new_customer)

    # Add new customer to current data
    customers.append(new_customer)

    print("\nCustomer added successfully!")


elif choice.lower() == "no":

    print("\nNo new customer was added.")


else:

    print("\nInvalid choice. No new customer was added.")


# Calculate total sales and customer counts
total_sales, male_customers, female_customers = process_customers(customers)


# Calculate average sales
average_sales = calculate_average(
    total_sales,
    len(customers)
)


# Find most popular category
most_popular = popular_category(customers)


# Display final report
print("\n========================================")
print("           SALES REPORT")
print("========================================")

print("Total Sales: Rs.", total_sales)
print("Average Sales: Rs.", round(average_sales, 2))
print("Total Male Customers:", male_customers)
print("Total Female Customers:", female_customers)
print("Most Popular Category:", most_popular)


# Display sale classification
print("\nSale Classification")
print("----------------------------------------")

for customer in customers:

    result = classify_sale(customer["sales"])

    print(
        customer["name"],
        "- Rs.",
        customer["sales"],
        "-",
        result
    )


print("========================================")

