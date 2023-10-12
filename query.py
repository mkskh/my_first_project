from data import warehouse1, warehouse2

# YOUR CODE STARTS HERE

# Get the user name
username = input("\nUsername: ")

# Greet the user
print(f"\nHello, {username}!\nWhat would you like to do?")

# Show the menu and ask to pick a choice
def main():
    print("\n 1 - List items by warehouse\n 2 - Search an item and place an order\n 3 - Quit\n")
    choice1 = input("Type the number of the operation: ")

    # If they pick 1
    if choice1 == "1":
        print("\n  Items in warehouse 1:\n")
        for item in warehouse1:
            print(item)
        print("\n  Items in warehouse 2:\n")
        for item in warehouse2:
            print(item)

    # Else, if they pick 2
    elif choice1 == "2":
        count1 = 0
        count2 = 0
        loc1 = False
        loc2 = False
        choice2 = input("\nInput the name of wanted item: ")
        
        for item in warehouse1:
            if choice2 == item:
                count1 += 1
                loc1 = True
        for item in warehouse2:
            if choice2 == item:
                count2 += 1
                loc2 = True
                
        count = count1 + count2

        if loc1 == True and loc2 == False:
            loc = "Warehouse 1"
        elif loc1 == False and loc2 == True:
            loc = "Warehouse 2"
        elif loc1 == True and loc2 == True:
            loc = "Both warehouses"
        elif loc1 == False and loc2 == False:
            loc = "Not in stock"

        def max():   
            if count1 > count2:
                return (f"{count1} items in Warehouse 1")
            elif count1 < count2:
                return (f"{count2} items in Warehouse 2")
            elif count1 == count2:
                return (f"{count1} items in each Warehouse")
            
            

        print(f"\nAmount available: {count}\nLocation: {loc}\nMaximum availability: {max()}\n")

        def order():
            yesno = input("Would you like to order this item? (y/n) : ")

            if yesno == "y":

                def howmany():
                    how_many = int(input("\nHow many would you like to order?\nType '0' if you want to cancel your order. - "))

                    def inner():
                        if how_many == 0:
                            return print(f'\nThank you for your visit, {username}.')
                        elif how_many > 0 and how_many <= count:
                            return print(f'\n{how_many} {choice2} have been ordered.\nThank you for your visit, {username}.')
                        else:
                            print(f'\n{"*" * 50}\nThere are not this many available.\n\nThe maximum amount that can be ordered is {count}!\n{"*" * 50}')
                            return howmany()
                    return inner()
                howmany()

            elif yesno == "n":
                print(f'\nThank you for your visit, {username}.')

            else:
                print("\nPlease enter only 'y' or 'n' !")
                order()

        order()
        
    # Else, if they pick 3
    #
    elif choice1 == '3':
        print(f'\nThank you for your visit, {username}.')

    # Else
    else:
        print(f'\n{"-" * 40}\nPlease enter only numbers 1, 2 or 3!\n{"-" * 40}')
        main()

main()
# Thank the user for the visit