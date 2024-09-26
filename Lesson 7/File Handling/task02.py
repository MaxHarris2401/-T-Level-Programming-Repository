def main():
    Username = input("Enter username ")
    Password = input("Enter password ")
    f = open("Passwordes.txt", "a")
    FullLine = (Username+" "+Password)
    f.write(FullLine)
    f.close()
    f = open("Passwordes.txt", "r")
    print("Username + Password written as",'"'+Username, Password+'"')
    
main()
    