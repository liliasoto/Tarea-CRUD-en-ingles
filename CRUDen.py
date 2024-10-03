#-----------------------------------------------------
# Name: CRUDen.py
# Goal: Performs CRUD operations on a list
# Assignment due on September 13, 2024
# Author: Lilia Soto Llamas
# Date: September 5, 2024
#-----------------------------------------------------

# Declare the list globally
storage = []

#-----------------------------------------------------
# Add items to the list
#-----------------------------------------------------
def create_item():
    cycle = "y"
    while cycle.lower() == "y":  # .lower() to accept both "y" and "Y"
        data = input("Enter the item: ").strip()  # .strip() to remove any leading or trailing spaces
        if data:  # To verify if the data is not empty
            storage.append(data)
            print("Item saved successfully!")
        else:
            print("You can't add an empty value.")

        cycle = input("Do you want to add another item (Y/N)? ").strip()
    else:
        print("Okay, no more items added.")

#-----------------------------------------------------
# Search items in the list
#-----------------------------------------------------
def search_items():
    cycle = "y"
    while cycle.lower() == "y":  # Accepts both 'Y' and 'y'
        try:
            pos = int(input("Which position were you looking for?: "))  # Try converting input to an integer
            if 1 <= pos <= len(storage):  # Check if the position is within a valid range
                print("Item at position {}: {}".format(pos, storage[pos - 1]))
            else:
                print("That position does not exist.")  # If the position is out of range
        except ValueError:
            print("Error: You must enter a valid integer.")  # Handles non-integer input

        cycle = input("Do you want to search for another item (Y/N)? ").strip()
    else:
        print("Search ended.")

#-----------------------------------------------------
# Update items in the list
#-----------------------------------------------------
def update_item():
    cycle = "y"
    while cycle.lower() == "y":  # Accepts both 'Y' and 'y'
        try:
            pos = int(input("Which position do you want to change?: "))  # Try converting input to an integer
            if 1 <= pos <= len(storage):  # Check if the position is within a valid range
                newItem = input("What would you like to replace it with?: ")
                storage[pos - 1] = newItem  # Replace the item at the given position
                print("Position updated successfully!")
            else:
                print("That position does not exist.")  # If the position is out of range
        except ValueError:
            print("Error: You must enter a valid integer.")  # Handles invalid input

        cycle = input("Do you want to replace another item (Y/N)? ").strip()  # Repeat the option
    else:
        print("Changes finished.")

#-----------------------------------------------------
# Delete items from the list
#-----------------------------------------------------
def delete_item():
    cycle = "y"
    while cycle.lower() == "y":  # Accepts both 'Y' and 'y'
        try:
            pos = int(input("Which position do you want to delete?: "))  # Convert input to an integer
            if 1 <= pos <= len(storage):  # Check if the position is within a valid range
                storage.pop(pos - 1)
                print("Position deleted successfully!")
            else:
                print("That position does not exist.")  # If the position is out of range
        except ValueError:
            print("Error: You must enter a valid integer.")  # Handles invalid input
        cycle = input("Do you want to delete another item (Y/N)? ").strip()  # Repeat the option
    else:
        print("Deletion process finished.")

#-----------------------------------------------------
# List items
#-----------------------------------------------------
def read_items():
    for i in storage:
        print("Item: {}".format(i))  # Use a for loop to display each item in the list

#-----------------------------------------------------
# Application dashboard
#-----------------------------------------------------
def dashboard():
    while True:
        print("-- CRUD Operations with Lists --")
        print("1. Add items to the list")
        print("2. Search items in the list")
        print("3. Update items in the list")
        print("4. Delete items from the list")
        print("5. List items")
        print("6. Exit")

        try:
            option = int(input("Enter an option between 1 and 6: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if option == 1:
            create_item()
        elif option == 2:
            search_items()
        elif option == 3:
            update_item()
        elif option == 4:
            delete_item()
        elif option == 5:
            read_items()
        elif option == 6:
            print("See you next time!")
            break  # Exit the loop when option 6 is chosen
        else:
            print("Please choose a number between 1 and 6.")

def main():
    dashboard()

if __name__ == "__main__":
    main()
