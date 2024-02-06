def insertionsort(aList):

    toSort = aList[:]

    listLength = len(toSort)

    # run the loop from second element to the last element
    for i in range(1,listLength):
        # key is the current number being compared against previous elements in the list
        key = toSort[i]
        # run the loop from previous element to first element (backwards)
        for j in range(i-1,-1,-1):
            # fitting key in the least position
            if key < toSort[j]:
                toSort[j+1] = toSort[j]
                print(toSort)
            else:
                # break the loop as we the key has reached its minimum position
                break

        # insert the key to the minimum position
        toSort[j+1] = key
        print(toSort)

    return toSort

toSort = [9,4,5,15,3]
print(toSort,insertionsort(toSort))
