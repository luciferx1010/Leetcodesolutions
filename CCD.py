def display_sub_menu(main_menu):
    sub_menu = ""
    if main_menu == "C":
        print("Coffee Menu:")
        print("1. Espresso Coffee")
        print("2. Cappuccino Coffee")
        print("3. Latte Coffee")
        sub_menu = input("Enter the number for your choice: ")
    elif main_menu == "T":
        print("Tea Menu:")
        print("1. Plain Tea")
        print("2. Assam Tea")
        print("3. Ginger Tea")
        print("4. Cardamom Tea")
        print("5. Masala Tea")
        print("6. Lemon Tea")
        print("7. Green Tea")
        print("8. Organic Darjeeling Tea")
        sub_menu = input("Enter the number for your choice: ")
    elif main_menu == "S":
        print("Soup Menu:")
        print("1. Hot and Sour Soup")
        print("2. Veg Com Soup")
        print("3. Tomato Soup")
        print("4. Spicy Tomato Soup")
        sub_menu = input("Enter the number for your choice: ")
    elif main_menu == "B":
        print("Beverage Menu:")
        print("1. Hot Chocolate Drink")
        print("2. Badam Drink")
        print("3. Badam-Pista Drink")
        sub_menu = input("Enter the number for your choice: ")
    else:
        print("Invalid input. Please enter a valid main menu option.")

    if sub_menu:
        print(f"You selected: {get_sub_menu_name(main_menu, sub_menu)}")

def get_sub_menu_name(main_menu, sub_menu):
    menu_names = {
        "C": ["Espresso Coffee", "Cappuccino Coffee", "Latte Coffee"],
        "T": ["Plain Tea", "Assam Tea", "Ginger Tea", "Cardamom Tea", "Masala Tea", "Lemon Tea", "Green Tea", "Organic Darjeeling Tea"],
        "S": ["Hot and Sour Soup", "Veg Com Soup", "Tomato Soup", "Spicy Tomato Soup"],
        "B": ["Hot Chocolate Drink", "Badam Drink", "Badam-Pista Drink"]
    }
    main_menu_name = {
        "C": "Coffee",
        "T": "Tea",
        "S": "Soup",
        "B": "Beverage"
    }
    return menu_names[main_menu][int(sub_menu)-1] if sub_menu.isnumeric() and int(sub_menu) in range(1, len(menu_names[main_menu])+1) else f"Invalid {main_menu_name[main_menu]} menu selection."

# Main program
print("Welcome to CCD")
main_menu = input("Enter the first letter of the main menu (C for Coffee, T for Tea, S for Soup, B for Beverage): ")
display_sub_menu(main_menu.upper())
