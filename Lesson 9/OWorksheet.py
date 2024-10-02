def binary_search(a, b, c, d):
    if c >= b:
        mid = (c + b) //2
        if a[mid] == d:
            return mid
        elif a[mid] > d:
            return binary_search(a, b, mid - 1, d)
        else:
            return binary_search(a, mid + 1, c, d)
    else:
        return - 1
def main():
    mylist = [1, 52, 557, 43445]