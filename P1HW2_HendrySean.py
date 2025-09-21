 # Sean Hendry
 # 09/18/25
 # P1HW2
 # For this assignment you will create a program that does some basic math on numbers that are entered.

budget = int(input("Enter your budget: "))

destination = input("Enter your travel destination: ")

gas = int(input("How much do you think you will spend on gas? "))

hotel = int(input("Approximatley, how much will you need for accomodation/hotel? "))

food = int(input("Last, how much do you need for food? "))

finalbalance = budget - gas - hotel - food


print("------------Travel Expenses------------")
print("Location: ", destination)
print("Initial Budget: ", budget)

print("Fuel: ", gas)
print("Accomodation: ", hotel)
print("Food: ", food)

print("Remaining Balance: ", finalbalance)



