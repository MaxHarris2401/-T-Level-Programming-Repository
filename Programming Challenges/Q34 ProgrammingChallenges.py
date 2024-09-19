Temp = input("Enter the current Temperature in centigrade: ")
if str.isdigit(Temp):
    Num=int(Temp)
    if Num < 0:
        print("Its Freezing")
    elif Num >=0 and Num <=10:
        print("Its very cold")
    elif Num >=10 and Num <=20:
        print("Its cold")
    elif Num >=20 and Num <=30:
        print("Its normal")
    elif Num >=30 and Num <=40:
        print("Its hot")
    elif Num >=40:
        print("Its very hot")
else:
    print("This is not a number")