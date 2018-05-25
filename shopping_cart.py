# shopping_cart.py

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

# print(products)

import datetime
import os.path

id_inputs = []
cart_list = []

def product_by_id(product_id):
    return [product for product in products if str(product["id"]) == product_id]

def sum_cart_subtotal(cart):
    total = 0
    for item in cart:
        total = total + item["price"]
    return round(total, 2)

def calc_sales_tax(cost):
    return round(cost * .08875, 2)

def sum_cart_total(subtotal, sales_tax):
    return round(subtotal + sales_tax, 2)

def print_top_header():
    datetimeobject = datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m-%d %H:%M:%S')
    header_string = "--------------------------------\nMy Grocery Store\n--------------------------------\n"
    header_string = header_string + "Web: www.mystore.com\nPhone: 1.123.456.7890\nCheckout Time: " + str(datetimeobject) + "\n--------------------------------"
    return header_string

def print_cart_items(cart):
    shopping_cart_string = "Shopping Cart Items:\n"
    for item in cart:
        shopping_cart_string = shopping_cart_string + " + " + item["name"] + " (${0:.2f})\n".format(item["price"])
    shopping_cart_string = shopping_cart_string + "--------------------------------"
    return shopping_cart_string

def print_sale_price_details(subtotal, sales_tax, total):
    sale_price_details_string = "Subtotal: $" + str(subtotal) + "\nPlus NYC Sales Tax (8.875%): $" + str(sales_tax) + "\nTotal: $" + str(total)
    sale_price_details_string = sale_price_details_string + "\n--------------------------------\nThanks for your business! Please come again."
    return sale_price_details_string

def print_receipt():
    print(print_top_header())
    print(print_cart_items(cart_list))
    subtotal = sum_cart_subtotal(cart_list)
    sales_tax = calc_sales_tax(subtotal)
    total = sum_cart_total(subtotal, sales_tax)
    print(print_sale_price_details(subtotal, sales_tax, total))

def write_reciept_to_file():
    datetimeobject = datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m-%d-%H-%M-%S')
    filename = str(datetimeobject) + ".txt"
    filepath = "Desktop/PythonClass/point-of-sale-app/receipts/"
    with open(os.path.join(os.path.expanduser('~'), filepath, filename), "w") as file:
        file.write(print_top_header())
        file.write("\n" + print_cart_items(cart_list))
        subtotal = sum_cart_subtotal(cart_list)
        sales_tax = calc_sales_tax(subtotal)
        total = sum_cart_total(subtotal, sales_tax)
        file.write("\n" + print_sale_price_details(subtotal, sales_tax, total))


while True:
    product_id = input("Please input a product identifier, or 'DONE' if there are no more items: ")
    if product_id.lower() == 'done':
        break;
    if product_by_id(product_id):
        product = product_by_id(product_id)[0]
        cart_list.append(product)
    else:
        print("Hey, are you sure that product identifier is correct? Please try again!")

print_receipt()
write_reciept_to_file()
