TextbookPrice = 15
NumBooks = int(input("Please enter the quantity of books: "))
LoyalCustomer = input("Type Y or N to confirm if you are a loyal customer ")
if NumBooks >= 10 or NumBooks <= 19:
    DiscountPrice = TextbookPrice * 0.95
    DiscountPrice = DiscountPrice * NumBooks
    Discount = 5
elif NumBooks >= 20:
    DiscountPrice = TextbookPrice * 0.80
    DiscountPrice = DiscountPrice * NumBooks
    Discount = 10
else:
    DiscountPrice = TextbookPrice
    DiscountPrice = DiscountPrice * NumBooks
    Discount = 0
if LoyalCustomer == "Y":
    Postage = 0
elif LoyalCustomer == "N":
    Postage = 5
Price = DiscountPrice + Postage
if Discount != "0%":
    print("You ordered",NumBooks,"books \nwith a discount of",Discount,"\nTotal cost will be £"+str(Price),"with postage")
else:
    print("You ordered",NumBooks,"\nTotal cost will be £"+str(Price),"with postage")
