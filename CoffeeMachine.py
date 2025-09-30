def CoffeeMachine(Water, Coffee_Powder, Sugar):

    Order = int(input("How many cup do you want?\n"))


    for cup in range(1, Order+1):
        Water_taken = 50
        Coffee_Powder_taken = 5
        Sugar_taken = 2

        print(f"Water for cup {cup} is :- {Water_taken}")
        print(f"Coffee_Powder for cup {cup} is :- {Coffee_Powder_taken}")
        print(f"Sugar for cup {cup} is :- {Sugar_taken}")
        print()

    Water_reduced = Water_taken * Order
    Coffee_Powder_reduced = Coffee_Powder_taken * Order
    Sugar_reduced = Sugar_taken * Order

    Water_left = Water - Water_reduced
    Coffee_Powder_left = Coffee_Powder - Coffee_Powder_reduced
    Sugar_left = Sugar - Sugar_reduced

    print(f"Remaining of Water : {Water_left}, Coffee_Powder : {Coffee_Powder_left} and Sugar : {Sugar_left}")

    return Water_left, Coffee_Powder_left, Sugar_left
# Initial values
Water = 1000
Coffee_Powder = 500
Sugar = 250

Again = True
while Again:
    Water, Coffee_Powder, Sugar = CoffeeMachine(Water, Coffee_Powder, Sugar)
    Repeat = input("Do you want any more cup to coffee (y/n)? :- ")
    if (Repeat != "y"):
        Again = False