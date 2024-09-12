#login
def login():
    Username = input("Input a username: ")
    WordPass = input("Input a password: ")
    if Username == "Admin" and WordPass == "deity" or Username == "User" and WordPass == "mortal":
        print("Logged in")
    else:
        print("Invalid Username or password.")
login()