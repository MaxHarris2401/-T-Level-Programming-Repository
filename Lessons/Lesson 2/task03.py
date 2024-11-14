CurrencyToChange = input("Enter Y to Convert to Yen or E to Convert To Euros: ")
NumPounds = int(input("Please enter amount in GBP "))
if CurrencyToChange == "Y":
    NumYen = NumPounds * 124.6
    print("£"+str(NumPounds),"in Yen is","¥"+str(NumYen))
elif CurrencyToChange == "E":
    NumEuros = NumPounds * 1.26
    print("£"+str(NumPounds),"in Euros is","€"+str(NumEuros))
else:
    print("Invalid code entered")