try:
    f = open("test.txt", "r")
except UnicodeDecodeError as e:
    print(e)
else:
    print("found")