import datetime
dtoday=datetime.datetime.now()
#returns number of days we are in year
print(dtoday.strftime("%j"))
#returns what day it is today
print(dtoday.strftime("%A"))
#current year and current minute
print(dtoday.strftime("%Y %M"))