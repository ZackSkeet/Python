Numberofcarsat10cents = 0
Numberofcarsat15cents = 0
Numberofcarsat25cents = 0
Tax = 0

Capacity = int("What is your cars engine capacity?")
if Capacity != 0

    elif Capacity >= 3000:
        Tax = Tax + Capacity * 0.25
        Numberofcarsat25cents = Numberofcarsat25cents + 1
    elif Capacity >= 1000:
        Tax = Tax + Capacity * 0.15
        Numberofcarsat15cents = Numberofcarsat15cents + 1
    elif Capacity < 0:
        Tax = Tax + Capacity * 0.10
        Numberofcarsat10cents = Numberofcarsat10cents + 1
    elif Capacity < 0:
        print("This is a negative number!")

choice = input("Do you have any more cars?").lower()
if choice == 'yes':
    Capacity = int("What is your cars engine capacity?")

elif choice == 'no':
    print("Tax owed:" + str(Tax))
    print("Number of cars taxed at 25 cents per cc" + str(int(Numberofcarsat25cents))".")
    print("Number of cars taxed at 15 cents per cc" + str(int(Numberofcarsat15cents))".")
    print("Number of cars taxed at 10 cents per cc" + str(int(Numberofcarsat10cents))".")
