import time
import random

def bubbleSort(unSorted):

    start_time = time.time()

    toSort = unSorted[:]

    listLength = len(toSort)

    for passes in range(listLength-1):

        for i in range(0, listLength-1):

            if toSort[i] > toSort[i+1] :
                toSort[i], toSort[i+1] = toSort[i+1], toSort[i]

    print(f"Time taken for sort: {time.time() - start_time:.3f}s")

    return toSort

testList = [51,53,49,88,62,74,68,53,67,51,59,65,42,43,59,63,62,40,67,59]
print(testList,bubbleSort(testList))
