import time
import random

def insertionsort(aList):

    count = 0

    toSort = aList[:]

    listLength = len(toSort)

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

def optimised_insertion(aList):

    count = 0

    toSort = aList[:]
    
    start_time = time.time()
    
    for i in range(1,len(toSort)):
        count += 1
        if toSort[i] >= toSort[i-1]:
            continue
        
        for j in range(i):
            if toSort[i] < toSort[j]:
                toSort[j],toSort[j+1:i+1] = toSort[i],toSort[j:i]
                break
            
    print(f"Time taken for sort: {time.time() - start_time:.3f}s")
    print("#of comparisons = ", count)
    
    return toSort


toSort = []
for i in range(0,1000):
    toSort.append(random.randint(0, 100))

insertionsort(toSort)
optimised_insertion(toSort)
