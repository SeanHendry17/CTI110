# P3LAB
# Sean Hendry
# 10/18/25
# This program allows the user to enter a money (float) value with two places after the decimal

amount = float(input("Enter the amount of money as a float: "))

cents = int(round(amount * 100))

dollars = cents // 100
cents = cents - dollars * 100

quarters = cents // 25
cents = cents - quarters * 25

dimes = cents // 10
cents = cents - dimes * 10

nickel = cents // 5
cents = cents - nickel * 5

pennies = cents

if dollars == 1:
    print("1 Dollar")
elif dollars > 1:
    print(dollars, "Dollars")


if quarters == 1:
    print("1 Quarter")
elif quarters > 1:
    print(quarters, "Quarters")


if dimes == 1:
    print("1 Dime")
elif dimes > 1:
    print(dimes, "Dimes")

if nickel == 1:
    print("1 Nickel")
elif nickel > 1:
    print(nickel, "Nickels")

if pennies == 1:
    print("1 Penny")
elif pennies > 1:
    print(pennies, "Pennies")
