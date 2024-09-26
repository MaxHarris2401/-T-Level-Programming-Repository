num1 = input("Enter one number ")
num2 = input("Enter another number ")
try:
    float(num1)
    float(num2)
except TypeError as TE:
    print(TE)
else:
    print("work")