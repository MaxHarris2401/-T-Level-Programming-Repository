try:
    f = open("weoeoeoe.txt", "r")
except FileNotFoundError as e:
    print(e)
else:
    print("found")