print("Italian Holiday")
Money = 500
print("You have","€"+str(Money))
FoodCost = int(input("Enter how much spent on food: "))
TripsCost = int(input("Enter how much spent on trips: "))
PresentCost = int(input("Enter how much spent on presents: "))
NewMoneyVal = Money - FoodCost - TripsCost - PresentCost
print("You have","€"+str(NewMoneyVal),"Remaining.")
NewMoneyVal = NewMoneyVal * 1.26
print("Which is","£"+str(NewMoneyVal),"in Pounds")
if NewMoneyVal <= Money:
    print("You have overspent.")