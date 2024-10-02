def Groceries():
    while True:
        groceries = input("Enter how much you spent on groceries: ")
        try:
            float(groceries)
        except:
            print("Invalid number entered")
        else:
            break
    print("You spent "+groceries+" on groceries.")
    return groceries
def Groceries():
    while True:
        groceries = input("Enter how much you spent on groceries: ")
        try:
            float(groceries)
        except:
            print("Invalid number entered")
        else:
            break
    print("You spent "+groceries+" on groceries.")
    return groceries

def menu():
    Categories = ["groceries","entertainment","travel","rent"]
    while True:
        print("Enter a category to input expenses or type N to quit")
        for i in range(len(Categories)):
            print(Categories[i].upper())
        Option = input(">>> ")
        if Option.lower() == Categories[0]:
            GroceriesCost = Groceries()
        elif Option.lower() == Categories[1]:
            print("Y")
        elif Option.lower() == Categories[2]:
            print("Y")
        elif Option.lower() == Categories[3]:
            print("Y")
        elif Option.lower() == "n":
            Sure = input("Are you sure you want to quit? Type Y to confirm ")
            if Sure.upper() == "Y":
                break
        else:
            print("Invalid option entered")
menu()