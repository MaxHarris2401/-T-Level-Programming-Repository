def mergeSort(Unsorted):
    if len(Unsorted) > 1:
        mid = len(Unsorted)//2
        UnsortedHalf1 = Unsorted[:mid]
        UnsortedHalf2 = Unsorted[mid:]
        mergeSort(UnsortedHalf1)
        mergeSort(UnsortedHalf2)
        i = j = k = 0
        while i < len(UnsortedHalf1) and j < len(UnsortedHalf2):
            if UnsortedHalf1[i] < UnsortedHalf2[j]:
                Unsorted[k] = UnsortedHalf1[i]
                i += 1
            else:
                Unsorted[k] = UnsortedHalf2[j]
                j += 1
            k += 1
        while i < len(UnsortedHalf1):
            Unsorted[k] = UnsortedHalf1[i]
            i += 1
            k += 1
        while j < len(UnsortedHalf1):
            Unsorted[k] = UnsortedHalf2[j]
            j += 1
            k += 1
Unsorted = [23, 16, 6, 18, 14, 9, 17, 4]
print(Unsorted)
mergeSort(Unsorted)
print(Unsorted)