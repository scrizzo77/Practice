import random
import time

def insertion(toSort):
    start_time = time.time()
    for i in range(1,len(toSort)):
        if toSort[i] >= toSort[i-1]:
            continue
        for j in range(i):
            if toSort[i] < toSort[j]:
                toSort[j],toSort[j+1:i+1] = toSort[i],toSort[j:i]
                break
    print(f"Time taken for sort: {time.time() - start_time:.3f}s")
    return toSort

toSort = []
for i in range(0,1000):
    toSort.append(random.randint(0, 100))

insertion(toSort)
