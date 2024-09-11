Temp = int(input("Enter the current Temperature in centigrade: "))
if Temp < 0:
    print("Its Freezing")
elif Temp >=0 and Temp <=10:
    print("Its very cold")
elif Temp >=10 and Temp <=20:
    print("Its cold")
elif Temp >=20 and Temp <=30:
    print("Its normal")
elif Temp >=30 and Temp <=40:
    print("Its hot")
elif Temp >=40:
    print("Its very hot")