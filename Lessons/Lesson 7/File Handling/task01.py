import os
def main():
    filename = input("Enter file name ")
    validFile = os.path.isfile("f:\\test.txt")
    f = open(filename, "a")
    text = input("Enter text ")
    f.write(text + "\n")
    f.close()
    f = open("f:\\test.txt", "r")
    for lines in f:
        print(lines)
    f.close()
main()
