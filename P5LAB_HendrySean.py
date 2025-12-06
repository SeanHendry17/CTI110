# Sean Hendry
# 11/30/25
# P5LAB
# Program will simulate a customer using a self-checkout machine

import random


def disperse_change(change):

    change = int(round(change * 100))

    dollars = change // 100
    change = change - dollars * 100

    quarters = change // 25
    change = change - quarters * 25

    dimes = change // 10
    change = change - dimes * 10

    nickel = change // 5
    change = change - nickel * 5

    pennies = change

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


def main():

    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe: ${amount_owed:.2f}")

    money_in = float(input("How much money will you put into the machine? "))

    change = money_in - amount_owed
    print(f"Change is: ${change:.2f}")
    print()
    disperse_change(change)


main()
