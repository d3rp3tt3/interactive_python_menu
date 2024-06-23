# Menu dictionary
menu = {
    "Snack": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meal": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drink": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
order_list = []

# Launch the store and present a greeting to the customer
print(" 🌮 🥤 🍩 Welcome to Super Duper Food Mart! 🍩 🥤 🌮\n")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("Here are the types of things you can order:")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input(
        "\nPlease enter the number for the menu category: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"\nYou chose to order a '{
                  menu_category_name}'.\n")

            # Print out the menu options from the menu_category_name
            print(f"Here are the items from the '{menu_category_name}' menu:")
            i = 1
            menu_items = {}
            print("\n")
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | "
                              + f"{key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            # 2. Ask customer to input menu item number
            menu_item = input(
                "\nEnter the number of the menu item you'd like to order: ")

            # 3. Check if the customer typed a number
            if menu_item.isdigit():

                # Convert the menu selection to an integer
                menu_item = int(menu_item)

                # 4. Check if the menu selection is in the menu items
                if menu_item in menu_items.keys():

                    # Store the item name as a variable
                    item_name = menu_items[menu_item]["Item name"]

                    # Ask the customer for the quantity of the menu item
                    quantity = input(
                        f"How many '{item_name}' would you like to order? ")

                    # Check if the quantity is a number, default to 1 if not
                    if quantity.isdigit:
                        quantity = int(quantity)
                    else:
                        quantity = 1

                    # Add the item name, price, and quantity to the order list
                    order_list.append({
                        "Item name": item_name,
                        "Price": menu_items[menu_item]["Price"],
                        "Quantity": quantity
                    })

                # Tell the customer that their input isn't valid
            else:
                print("You didn't select a number.")

            # Tell the customer they didn't select a menu option
        else:
            print(f"{menu_category} is not an option on the menu.")

    # Tell the customer they didn't select a number
    else:
        print("You didn't select a number.")

    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input(
            "Would you like order anything else? Type (Y)es or (N)o: ")
        # 5. Check the customer's input
        match keep_ordering.lower():
            # Keep ordering
            case 'y':
                place_order = True
            # Exit the keep ordering question loop
                break
            # Complete the order
            case 'n':
                place_order = False
            # Since the customer decided to stop ordering, thank them for
            # their order
                print("\nThank you for your order!\n")

            # Exit the keep ordering question loop
                break
            case _:
                # Tell the customer to try again
                print("Please select a valid option.")

# Print out the customer's order
print("Here's a summary of your order:\n")

# Uncomment the following line to check the structure of the order
# print(order)

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Loop through the items in the customer's order
# I think we can do this with enumerate later, but for now, we'll use range
for item_index in range(len(order_list)):
    # Store the item name as a variable
    item_name = order_list[item_index]["Item name"]

    # Store the price as a variable
    price = order_list[item_index]["Price"]

    # 7. Store the dictionary items as variables
    quantity = order_list[item_index]["Quantity"]

    # 8. Calculate the number of spaces for formatted printing
    num_item_spaces = 25 - len(item_name)
    num_price_spaces = 5 - len(str(price))
    num_quantity_spaces = 10 - len(str(quantity))

    # 9. Create space strings
    item_spaces = " " * num_item_spaces
    price_spaces = " " * num_price_spaces
    quantity_spaces = " " * num_quantity_spaces

    # 10. Print the item name, price, and quantity
    print(f"{item_name}{item_spaces} | ${price}{price_spaces} | {quantity}")


# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.
print(" " * 42)
# print("_" * 42)
total_cost = round(sum([item["Price"] * item["Quantity"]
                   for item in order_list]), 2)
print(f"👾👾👾 Your total is: ${total_cost} 👾👾👾\n")
