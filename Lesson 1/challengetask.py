import datetime
currentdate = datetime.datetime.now()
bYear = input("Enter the year you were born ")
bMonth = input("Enter the month you were born ")
bDay = input("Enter the day you were born ")
birthday = datetime.datetime(int(bYear), int(bMonth), int(bDay))
date1 = currentdate
date2 = birthday
howold = (date1 - date2).days
print("You are",howold,"years old")
