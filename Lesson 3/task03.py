def GreaterInteger():
    Int1 = int(input("Enter a number: "))
    Int2 = int(input("Enter another number: "))
    if Int1 > Int2:
        GreaterInteger = Int1
        print(GreaterInteger,"is the bigger number.")
    elif Int2 > Int1:
        GreaterInteger = Int2
        print(GreaterInteger,"is the bigger number.")
    else:
        print("The numbers are equal")
GreaterInteger()