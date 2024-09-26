Array = [0, 1, 2, 3, 4, 5, 6]
try:
    Array.writefile()
except AttributeError as e:
    print(e)