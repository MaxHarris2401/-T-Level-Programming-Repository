thisdict = {
    0:10,
    1:20
}
update = int(input("Enter new value "))
thisdict.update({len(thisdict)+1: update})
print(thisdict.items())