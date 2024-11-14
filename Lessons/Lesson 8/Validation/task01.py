num=int(input("Number? "))
try:
    num / 0
except ZeroDivisionError as ZeroError:
    print(ZeroError)
