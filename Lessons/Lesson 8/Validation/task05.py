try:
    f = open("C:\Windows\System32\eapsvc.dll", "w")
except PermissionError as p:
    print(p)
else:
    print("Permission allowed")