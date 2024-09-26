Num1 = int(input("Enter a number "))
try:
    print("You entered:", Num1)
except KeyboardInterrupt as e:
    print("Input canceled by the user.",e)
