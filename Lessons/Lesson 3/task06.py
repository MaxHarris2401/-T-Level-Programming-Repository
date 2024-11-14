def MembershipType():   
    Age = int(input("Enter your age "))
    YearsGym = int(input("Enter how long you have been in attendance "))
    if Age <=18:
        TypeMembership = "Junior"
        if YearsGym >=2:
            Price = 40
        else:
            Price = 60
    elif Age >=19 or Age <=49:
        TypeMembership = "Senior"
        if YearsGym >=10:
            Price = 90
        else:
            Price = 120
    elif Age >=50:
        TypeMembership = "Veteran"
        if YearsGym >=10:
            Price = 50
        else:
            Price = 80
    print("You have",TypeMembership,"membership and must pay £"+str(Price)+".")
MembershipType()