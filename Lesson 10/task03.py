thisdict = {
    0:10,
    1:20
}
Search = int(input("Enter value "))
for x in thisdict.keys():
    if Search in thisdict:
        print("Found")
        break
    else:
        print("Not found")
        break
