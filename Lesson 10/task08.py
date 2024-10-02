thisdict = {
    0:10,
    1:20
}
key = int(input("Enter a key to remove "))
thisdict.pop(key)
print("Key removed\n")
x = thisdict.items()
print(x)