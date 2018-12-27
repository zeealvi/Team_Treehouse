first_name = input("What is your first name?"  )
last_name = input("what is your last name?"   )
print(first_name, last_name)
if first_name == "Ali":
    print( first_name, "is learning python")
elif first_name == "Kabita":
    print(first_name, " is learning with fellow communit")
else:
     print("you should totally learn python, {}!" .format(first_name))
print("have a great day {}!" .format(first_name, last_name))