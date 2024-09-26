def main():
    NumArray = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    myArray = []
    
    for i in NumArray:
        EnterNum = int(input("Please enter a number "))
        myArray.append(EnterNum)
    
    displayMenu(myArray)
    
    return myArray
def displayMenu(myArray):
    while True:
        Choice = input("Please enter a choice of:\nCount\nSum\nAverage\nMin\nMax\n>>> ")
        if Choice.upper() == "COUNT":
            getCount(myArray)
        elif Choice.upper() == "SUM":
            getSum(myArray)
        elif Choice.upper() == "AVERAGE":
            getAverage(myArray)
        elif Choice.upper() == "MIN":
            getMin(myArray)
        elif Choice.upper() == "MAX":
            getMax(myArray)
        elif Choice.upper() == "EXIT":
            break
        else:
            print("Invalid data entered")
def getCount(myArray):
    print("Length: "+str(len(myArray)))
def getSum(myArray):
    print("Total sum: "+str(sum(myArray)))
def getAverage(myArray):
    print("Average: "+str(sum(myArray)/len(MyArray)))
def getMin(myArray):
    print("Minimum Number: "+str(min(myArray)))
def getMax(myArray):
    print("Minimum Number: "+str(max(myArray)))
main()