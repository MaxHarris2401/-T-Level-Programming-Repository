list = [7, 10, 13, 17, 23, 40, 53, 71, 100, 201]
search_item = int(input("Please enter a value to search "))
found = False
for value in range(len(list)):
    if list[value] == search_item:
        found = True
if found==True:
    print("Item Found")
else: 
    print("Item not found")