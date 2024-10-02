results = [6, 12, 4, 23, 17, 19, 4]
search_item = int(input("Please enter a value to search "))
found = False
for value in range(6):
    if results[value] == search_item:
        found = True
if found==True:
    print("Item Found")
else: 
    print("Item not found")