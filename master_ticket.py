Ticket_Price = 10
Service_Charge = 2
tickets_remaining = 100

def calculate_price (num_of_tickets):
    return num_of_tickets * Ticket_Price + Service_Charge

while tickets_remaining >= 1:

    print("There are {} tickets remaining" . format(tickets_remaining))

    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")

    print("Welcome to ticket master {}" .format (first_name + " " +last_name))
    number_tickets = input("How many tickets would you like to purchase {} ?" .format (first_name + " " +last_name))

    try:
        number_tickets = int(number_tickets)
        if number_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
    except ValueError as err:
        print("Oh no! We ran into an issue. {}. Please try again." .format(err))

    else:
        total_amount_due = calculate_price(number_tickets)
        print("Total amount due is ${}" .format(total_amount_due))

        print("Would you like to purchase tickets Y/N ?")

        prompt_confirmation = input ()
        if prompt_confirmation.upper() == "Y" :
            print (" Please use credit card to complete your purchase")
            tickets_remaining -= number_tickets
        else:
            print("Please update your shopping cart")
print ("Sorry we are sold out")
