#made by Alden 1 1 1 3 2 4 9 9 7
go = True
userInput = []
while go:
    try:
        tempUserInput = input("Enter a set of numbers, separated by spaces: ").split(" ")
        for i in tempUserInput:
            userInput.append(int(i))
        go = False
    except:
        print("That isn't a valid list.")
#userInput should now be a list of numbers
def counting(arr):
    #instead of making multiple arrays, maybe make a dictionary?
    tempDict = {}
    tempArr = []
    tempArrIndexes = []
    for i in arr:
        if i not in tempArr:
            tempArr.append(i)
            tempArrIndexes.append(1)
            tempDict[i] = [1]
        else:
            tempDict[i][0] = tempDict[i][0] + 1
            tempArrIndexes[tempArr.index(i)] = tempArrIndexes[tempArr.index(i)] + 1
    #tempDict.sor TODO!!
    print(tempDict)
    tempArrFinalIndex = tempArrIndexes.copy()
    print(tempArr, tempArrIndexes,tempArrFinalIndex)
    tempArrFinalIndex.append(0)
    for i in range(len(tempArrIndexes)):
        tempArrFinalIndex[i+1] = tempArrFinalIndex[i]+tempArrFinalIndex[i+1]
    tempArrFinalIndex.pop()
    print(tempArr, tempArrIndexes,tempArrFinalIndex)

    #below sorts
    finalArr = arr.copy()
    for i in range(len(tempArrFinalIndex)):
        for j in range(tempArrIndexes[i]):
            finalArr[tempArrFinalIndex[i]-1] = tempArr[i]
            tempArrIndexes[i] = tempArrIndexes[i] - 1
    print(finalArr, tempArrIndexes, tempArrFinalIndex)
counting(userInput)
