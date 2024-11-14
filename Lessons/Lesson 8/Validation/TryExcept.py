var = input("Numbber ")
try:
    int(var)
except TypeError as t:
    print("Error of type "+t)
except Exception as e: #exception for all error types
    print("No worky",e)
    return 0 #wierd thing that forces python to use the finally even when error thrown
else:
    print("Worked wonderfully")
    var = int(var)
    var *= 77
    var /= 13
    print(var)
finally:
    print("always happens")
    #file.close 