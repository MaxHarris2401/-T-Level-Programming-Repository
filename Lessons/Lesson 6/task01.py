def main():
    myArray = ["Tim", "Nigel", "Steve", "Maggie"]
    while True:
        UserOption = getUserChoice()
        if UserOption == 1:
            newPerson = input("Input the name you would like to write: ")
            myArray.append(newPerson)
            print(newPerson, "written to the list.")
        elif UserOption == 2:
            for i in myArray:
                print(i)
        elif UserOption == 3:
            SearchIndex = int(input("Enter name to search: "))
            print(myArray[SearchIndex])
        elif UserOption == 4:
            myArray.clear()
            print("List cleared")
        elif UserOption == 5:
            break
        else:
            print("Invalid menu number entered, try again")
def getUserChoice():
    print("1 - Enter New Name\n2 - Display All Names\n3 - Display Specific name by index\n4 - Clear list of names\n5 - Exit")
    UserOption = int(input("Enter which option you would like to use: "))
    return UserOption
main()
    