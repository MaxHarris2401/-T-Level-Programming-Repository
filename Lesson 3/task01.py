def main():
    mark = int(input("Please enter your exam mark "))
    if mark >= 60:
        print("Merit")
    elif mark >- 40:
        print("Pass")
    else:
        print("A mark of"+mark+" is a fail")
if __name__ == '__main__':
    main()