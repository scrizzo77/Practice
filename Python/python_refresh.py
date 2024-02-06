def processlist(aList):

    aListCopy = aList[:]

    listLength = len(aListCopy)

    for index in range(0,listLength):
        # add the list position to the list element
        aListCopy[index] += index

    return aListCopy

### main - call and test function ###

testList = [1,2,3,4]
print(testList,processlist(testList))
