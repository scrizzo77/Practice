import time
import random

def selectionSort(aList):

    toSort = aList[:]
    count = 0

    start_time = time.time()

    for start in range(0, listLength):

        #set minimum to start lt beginning of pass
        minimum = start

        for i in range(start+1, listLength):
            count += 1
            # find the position of the smallest element
            if toSort[i] < toSort[minimum]:
                minimum = i
            
        # swap element at start position with
        # the element at the minimum position
        temp = toSort[start]
        toSort[start] = toSort[minimum]
        toSort[minimum] = temp

    print(f"Time taken for sort: {time.time() - start_time:.3f}s")
    print("#of comparisons = ", count)

    return aList

def bubbleSort2(unSorted):

    toSort = unSorted[:]

    listLength = len(toSort)

    count = 0

    start_time = time.time()

    for passes in range(listLength-1):

        for i in range(0, listLength-passes-1):
            count += 1

            if toSort[i] > toSort[i+1] :
                toSort[i], toSort[i+1] = toSort[i+1], toSort[i]

    print(f"Time taken for sort: {time.time() - start_time:.3f}s")
    print("#of comparisons = ", count)

    return toSort

def bubbleSort1(unSorted):

    toSort = unSorted[:]

    listLength = len(toSort)
    count = 0

    start_time = time.time()

    for passes in range(listLength-1):

        for i in range(0, listLength-1):
            count += 1

            if toSort[i] > toSort[i+1] :
                toSort[i], toSort[i+1] = toSort[i+1], toSort[i]
                
    print(f"Time taken for sort: {time.time() - start_time:.3f}s")
    print("#of comparisons = ", count)

    return toSort

def insertionSort(aList):

    toSort = aList[:]

    listLength = len(toSort)
    count = 0

    i = 1
    j = 1

    start_time = time.time()

    while i < listLength:
        count += 1
        if toSort[i] < toSort[i-1]:
            toSort[i], toSort[i-1] = toSort[i-1], toSort[i]
            i -= 1
            if i <= 0:
                i = j + 1
            else:
                continue
        else:
            i += 1
            j = i

    print(f"Time taken for sort: {time.time() - start_time:.3f}s")
    print("#of comparisons = ", count)

    return toSort


testList = []
for i in range(1000,0,-1):
    testList.append(i)

listLength = len(testList)



bubbleSort1(testList)

bubbleSort2(testList)

selectionSort(testList)

insertionSort(testList)
