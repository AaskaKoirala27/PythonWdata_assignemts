# Module 4: File Input and Output
def read_sales_file(filename):

    data = []

    file = open(filename, "r")

    for line in file:

        name, gender, product, category, sales = line.strip().split(",")

        customer = {
            "name": name,
            "gender": gender,
            "product": product,
            "category": category,
            "sales": float(sales)
        }

        data.append(customer)

    file.close()

    return data

def save_customer(filename, customer):

    file = open(filename, "a")

    file.write(
        "\n" +
        customer["name"] + "," +
        customer["gender"] + "," +
        customer["product"] + "," +
        customer["category"] + "," +
        str(customer["sales"]) + "\n"
    )

    file.close()




