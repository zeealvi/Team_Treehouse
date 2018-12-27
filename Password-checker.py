import sys

MASTER_PASSWORD= "Zeeshan"
password = input("Please enter Password ... ")
attempt_count = 1
while password != MASTER_PASSWORD:
    if attempt_count > 3:
        sys.exit("Too many invalid password attempts")

    password = input("Invalid password, Try again..")
    attempt_count += 1
print("Welcome ")