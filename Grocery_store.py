Availability = ["Apples", "Banana", "Milk", "Bread", "Meat"]
Apple = 1.99
Banana = .99
Milk = 3.99
Bread = 2.99
Meat = 4.99


Tax_Charge = .08875

def Shopping_basket ():
    return (total_quantity * Milk)

shopping_list =[]

first_name = input("What is your first name? ")
last_name = input("What is your last name? ")

print("Welcome to Grocery_Store {}" .format (first_name + " " +last_name))


def show_help():
    print("What should we pick up at store?")
    print ("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'SHOW' to see the shopping list.
Enter 'Availability' to see items available for purchase.
    """)

def add_to_list (item):
    shopping_list.append(item)
    print("Added:!! list has {} items".format(len(shopping_list)))



def show_list():
    print("Here is your list:")
    for item in shopping_list:
        print(item)
def show_inventory():
    print("Items availabel for purchase")
    for item in Availability:
        print (item)


show_help()
while True:
    new_item = input ("> ")

    if new_item == "DONE":
        break
    elif new_item == "HELP":
        show_help()
        continue
    elif new_item == "SHOW":
        show_list()
        continue
    elif new_item == "Availability":
        show_inventory()
        continue
    add_to_list(new_item)
show_list()

# if new_item == {"Milk", "Bread", "Apple", "Banana", "Meat"}:
quantity = input("How many {}" " would you like?".format(shopping_list) )

total_quantity = int(quantity)

print("Would you like to purchase gorcery Y/N ?")

confirmation_purchase = input ()
if confirmation_purchase.upper() == "Y" :
    print (" Please use credit card to complete your purchase")

else:
    print("Please update your shopping cart")


total_amount_due = Shopping_basket*(quantity)
print("Total amount due is ${}" .format(total_amount_due))


'''

    try:
        number_tickets = int(number_tickets)
        if number_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
    except ValueError as err:
        print("Oh no! We ran into an issue. {}. Please try again." .format(err))

   # else:

print("Would you like to purchase tickets Y/N ?")

        prompt_confirmation = input ()
        if prompt_confirmation.upper() == "Y" :
            print (" Please use credit card to complete your purchase")
            tickets_remaining -= number_tickets
        else:
            print("Please update your shopping cart")
print ("Sorry we are sold out")
'''