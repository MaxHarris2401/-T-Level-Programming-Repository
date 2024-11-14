from datetime import datetime
def main():
    Age = input("Please enter age: ")
    DOB = input("Please enter Date of Birth: ")
    DOBSTR = datetime.strptime(DOB, '%b %d %Y')
    Name = input("Please enter name: ")
    validateAge(Age)
    if not(validateAge(Age)):
        print("This is NOT a valid age")
    if not(validateDate(DOB)):
        print("This is NOT a valid date")
    validateName(Name)
    if not(validateName(Name)):
        print("This is NOT a valid name")
def validateAge(Age):
    if str.isdigit(Age):
        return True
    else:
        return False
def validateName(Name):
    for c in Name:
        if str.isdigit(c):
            return False
        return True
if __name__ == '__main__':
    main()

    