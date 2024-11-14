integer = input("Enter number integer ")
try:
    int(integer)
except ValueError as e:
    print(e)
else:
    print("cool")

