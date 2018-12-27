import math



def split_check (total,number_of_people):
    if number_of_people <=1:
        raise ValueError ("More than 1 person is needed to split the check")
    return math.ceil( total / number_of_people)

try:
    total_due = float(input ("Whats the total amount due of check? "))
    number_of_people = int(input ("What is total number of people? "))
    amount_due = split_check(total_due,number_of_people)

except ValueError as err:
    print("Oh no! This is not a valid value try again")
    print ("({})".format(err))
else:

    print ("Each person owes ${}".format(amount_due))

# example code below to check monthly payments 
'''

def monthly_payment(total_amount, number_of_payments):
    if number_of_payments <=1:
        raise ValueError ("Number of payments have to be greater than 1")
    return math.ceil(total_amount / number_of_payments)

try:
    total_fee = float(input ("what is the total fee of course? "))
    number_of_Payments = int(input("Total number of payments? "))
except ValueError:
    print("Try a neumeric Fee?")
else:
    fee_due = monthly_payment(total_fee,number_of_Payments)
    print ("Each payment is ${}".format(fee_due))
'''