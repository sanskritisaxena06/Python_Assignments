# Question: A shopping application stores prices in a list and customer
# details in a dictionary. Pass them to functions using argument unpacking.

print("By sanskriti saxena")

def display_prices(*prices):
    print("Shopping Prices:", prices)
    print("Total Price:", sum(prices))


def display_customer(**details):
    print("Customer Details:")

    for key, value in details.items():
        print(key.capitalize() + ":", value)


prices = [100, 250, 350, 500]

customer = {
    "name": "Sanskriti",
    "city": "Bareilly",
    "age": 22
}

display_prices(*prices)
display_customer(**customer)