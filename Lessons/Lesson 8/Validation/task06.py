Array = [0, 1, 2, 3, 4, 5, 6]
try:
    print(Array[7])
except IndexError as e:
    print(e)