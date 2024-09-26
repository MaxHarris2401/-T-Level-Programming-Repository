num1 = int(input("Number 1 "))
num2 = int(input("Number 2 "))
try:
    num1/num2
except ArithmeticError as e:
    print(e)
else:
    print(num1/num2)