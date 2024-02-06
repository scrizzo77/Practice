import time
import random

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

    end_time = time.time()
    print(f"Time taken for bubble sort #1: {end_time - start_time:.3f}s")
    print("#of comparisons = ", count)

    return toSort

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

    end_time = time.time()
    print(f"Time taken for bubble sort #2: {end_time - start_time:.3f}s")
    print("#of comparisons = ", count)

    return toSort


def bubbleSort3(unSorted):

    toSort = unSorted[:]

    listLength = len(toSort)

    count = 0

    start_time = time.time()

    for passes in range(listLength-1):

        swapped = False
        for i in range(0, listLength-passes-1):
            count += 1

            if toSort[i] > toSort[i+1] :
                toSort[i], toSort[i+1] = toSort[i+1], toSort[i]
                swapped = True
        if swapped == False:
            break

    end_time = time.time()
    print(f"Time taken for bubble sort #3: {end_time - start_time:.3f}s")
    print("#of comparisons = ", count)
    print("length of list = ", listLength)

    return toSort

def selectionsort(unSorted):

    toSort = unSorted[:]

    listLength = len(toSort)

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
        if start != minimum:
            temp = toSort[start]
            toSort[start] = toSort[minimum]
            toSort[minimum] = temp

    end_time = time.time()
    print(f"Time taken for selection sort: {end_time - start_time:.3f}s")
    print("#of comparisons = ", count)
    
    return toSort

testList = []
for i in range(0,10000):
    testList.append(random.randint(0, 10000))
# print(testList,bubbleSort(testList))
bubbleSort1(testList)
bubbleSort2(testList)
selectionsort(testList)
#print(sortedList)
