list = [7, 10, 13, 17, 23, 40, 53, 71, 100, 201]
Find = int(input("Input a number to search "))
Start = 0
End = len(list)
Found = False
mid = (Start+End)//2
while Found == False and Start <= End:
    if list[mid] == Find:
        print("Found at", str(mid))
        Found = True
    else:
        if list[mid] > Find:
            End = mid+1
        else:
            Start = mid+1
    if Found == False:
        print("Not found")
        break