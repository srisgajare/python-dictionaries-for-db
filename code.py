import string

# Function to display main menu of options and take user input
def request_input():
    print(
        "\nMain menu\n1. Display database\n2. Retrieve item data\n3. Place order\n4. Restock item\n5. Add item\n6. Terminate\n"
    )
    # Store the user input in user_input variable
    user_input = int(input("Select an option from the menu > "))
    return user_input


# Function to display the database contents sorted according to part number
def display_db(partDB):
    print("\nRESPONSE: Displaying the Database sorted according to part number")
    print(
        "\n{:<15} {:<15} {:<15} {:<15}".format(
            "part_number", "part_name", "part_price", "part_quantity"
        )
    )
    # Sort according to part number and display the the contents of database
    for k, v in sorted(partDB.items()):
        part_name, part_price, part_qty = v
        print("{:<15} {:<15} {:<15} {:<15}".format(
            k, part_name, part_price, part_qty))


# Function to retrieve data about particular inventory and display the details
def retrieve_item(partDB):
    # Store the user entered part number in part_number variable
    part_number = int(input("Enter part number: "))
    # Display error message if the user entered part number is incorrect or doesn't exist in DB
    if not part_number in partDB.keys():
        print(
            "\nRESPONSE: Item details cannot be retrieved as the part number you entered is incorrect or doesn't exists.\n"
        )
    else:
        for k, v in partDB.items():
            # When the user entered part number matches the key, display the other required details of the item
            if k == part_number:
                part_name, part_price, part_qty = v
                print(
                    "\nRESPONSE: The details of the item with the part number %d are as follows"
                    % part_number
                )
                print(
                    "\n{:<15} {:<15} {:<15} {:<15}".format(
                        "part_number", "part_name", "part_price", "part_quantity"
                    )
                )
                print(
                    "{:<15} {:<15} {:<15} {:<15}".format(
                        k, part_name, part_price, part_qty
                    )
                )


# Function to place an order for an item
def place_order(partDB):
    # Store the user entered part number of the item
    part_number = int(
        input("Enter the part number for which you want to place an order:")
    )
    # Display error message if the user entered part number is incorrect or doesn't exist in DB
    if not part_number in partDB.keys():
        print(
            "\nRESPONSE: The order for the item cannot be placed as the part number you entered is incorrect or doesn't exists.\n"
        )
    else:
        # Store the user entered quantity of the item in the variable
        item_quantity = eval(
            input("Enter the item quantity to place an order: "))
        for k, v in partDB.items():
            # Work on the item whose key matches with the user entered part number
            if k == part_number:
                part_name, part_price, part_qty = v
                # If the user requested quantity is more than existing quantity display error message
                if item_quantity > part_qty:
                    print(
                        "\nRESPONSE: There are no enough supplies. Going back to main menu, Ensure you enter a smaller quantity next time.\n"
                    )
                else:
                    # Calculate the total price with tax for the item to be sold and update the quantity in DB
                    tax_price = part_price * item_quantity * 0.10
                    total_price = (part_price * item_quantity) + tax_price
                    print(
                        "\nRESPONSE: The order for %d items of %s with part number %d is placed. The total amount of the order including the 10 percent tax is $%.2f"
                        % (item_quantity, part_name, part_number, total_price)
                    )
                    partDB.update(
                        {part_number: [part_name, part_price,
                                       part_qty - item_quantity]}
                    )


# Function to restock an item in the database
def restock_item(partDB):
    # Store the user entered part number of the item to be restocked
    part_number = int(
        input("Enter the part number of the item to be restocked: "))
    # Display error message if the user entered part number is incorrect or doesn't exist in DB
    if not part_number in partDB.keys():
        print(
            "\nRESPONSE: Restocking of the item was unsuccessful as the part number you entered is incorrect or doesn't exists.\n"
        )
    else:
        # Enter the item quantity to be restocked
        item_quantity = eval(
            input("Enter the quantity of the item to be restocked: "))
        for k, v in partDB.items():
            # Work on the item whose key matches with the user entered part number
            if k == part_number:
                part_name, part_price, part_qty = v
                # Update quantity of the restocked item in the DB and display the details
                partDB.update(
                    {part_number: [part_name, part_price,
                                   item_quantity + part_qty]}
                )
                print(
                    "\nRESPONSE: The item with part number: %d has been restocked successfully. %d items have been added to the existing stock.\n"
                    % (part_number, item_quantity)
                )
                print(
                    "The existing quantity for %s was %d. After restocking the quantity now is %d.\n"
                    % (part_name, part_qty, item_quantity + part_qty)
                )


# Function to add a new item to database
def add_item(partDB):
    # Store user entered item details in respective variables
    new_item_part_number = int(input("Enter the new part number to be added:"))
    new_item_name = input("Enter the item name:")
    new_item_price = float(input("Enter the item price:"))
    new_item_quantity = int(input("Enter item quantity:"))
    # Update the partDB dictionary by adding the details of the new item and print the response
    partDB.update(
        {new_item_part_number: [new_item_name,
                                new_item_price, new_item_quantity]}
    )
    print(
        "\nRESPONSE: New item with part_number %d has been added to the database successfully!\n"
        % new_item_part_number
    )


# Function to terminate the program
def terminate(partDB):
    print(
        "\nRESPONSE: Printing details of the sorted and updated DB on screen and also saving it to output file"
    )
    # Print the DB header info on the screen
    print(
        "\n{:<15} {:<15} {:<15} {:<15}".format(
            "part_number", "part_name", "part_price", "part_quantity"
        )
    )
    with open("pythonOut.txt", "w") as f:
        # Write the DB header info to the output file
        print(
            "{:<15} {:<15} {:<15} {:<15}".format(
                "part_number", "part_name", "part_price", "part_quantity"
            ),
            file=f,
        )
        for k, v in sorted(partDB.items()):
            part_name, part_price, part_qty = v
            # Print the details of the sorted and updated database on the screen
            print(
                "{:<15} {:<15} {:<15} {:<15}".format(
                    k, part_name, part_price, part_qty)
            )
            # Write the updated database details to the output file
            print(
                "{:<15} {:<15} {:<15} {:<15}".format(
                    k, part_name, part_price, part_qty
                ),
                file=f,
            )
    f.close()


# Main function
def main():
    print(
        "\nSrishti Gajare - Homework2 - CS524\nThis is a python program to manage the parts DB\nThe program lets you view, add, restock, sell items and update the DB\n"
    )
    # Declare a dictionary to store the parts database details read from input file
    partDB = {}
    with open("pythonIn.txt", "r") as f:
        # Skip reading the header/line 1 from input file, comment the line below if there is no header
        next(f)
        # Read the input file line by line starting from line 2
        for line in f:
            # Store each line of the file as a list named splitLine
            splitLine = line.split()
            # Store first item in the splitLine list as dictionary key
            # Store dictionary value as a list containing the remaining database fields
            partDB[int(splitLine[0])] = [
                str(splitLine[1]),
                float(splitLine[2]),
                int(splitLine[3]),
            ]
    f.close()
    # Print statement to display contents of dictionary
    print("\nThe partDB dictionary key value pairs: ")
    print(partDB)
    # Call the request_input() function to store the user input
    user_input = request_input()
    # Based on the user input call the appropriate function to process the option
    while user_input < 6:
        if user_input == 1:
            display_db(partDB)
            user_input = request_input()
        elif user_input == 2:
            retrieve_item(partDB)
            user_input = request_input()
        elif user_input == 3:
            place_order(partDB)
            user_input = request_input()
        elif user_input == 4:
            restock_item(partDB)
            user_input = request_input()
        elif user_input == 5:
            add_item(partDB)
            user_input = request_input()
        # Print error message if user provides invalid input
        else:
            print("\nInvalid user input,select a number from 1 to 6\n")
            user_input = request_input()
    # Call the terminate function if the user input is 6
    if user_input == 6:
        terminate(partDB)


if __name__ == "__main__":
    main()
