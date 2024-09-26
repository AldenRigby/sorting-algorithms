#use this chunk of code to get an input from the user
import random
import time
go = True
userInput = []
while go:
    try:
        tempUserInput = input("Enter a set of numbers, separated by spaces. Leave blank for a random list. ")
        if tempUserInput == "":
            userInput = []
            for i in range(10):
                userInput.append(random.randint(0,9))
        else:
            tempUserInput = tempUserInput.split(" ")
        for i in tempUserInput:
            userInput.append(int(i))
        go = False
    except:
        print("That isn't a valid list.")
#userInput should now be a list of numbers

def counting(arr):
    start = time.time()
    #setup
    comparisons = 0
    tempDict = {}
    tempArr = []
    tempArrIndexes = []

    #add all unique values to the dictionary
    for i in arr:
        comparisons = comparisons + 1
        if i not in tempArr:
            tempArr.append(i)
            tempArrIndexes.append(1)
            tempDict[i] = [1]
        else:
            tempDict[i][0] = tempDict[i][0] + 1
            tempArrIndexes[tempArr.index(i)] = tempArrIndexes[tempArr.index(i)] + 1

    #setup the list
    for i in range(len(list(tempDict.keys()))):
        comparisons = comparisons + 1
        tempArr[i] = list(tempDict.keys())[i]
        tempArrIndexes[i] = tempDict[list(tempDict.keys())[i]][0]

    print(arr)
    print(tempArr, tempArrIndexes)
    #this sorts the dictionary based on the key
    myKeys = list(tempDict.keys())
    myKeys.sort()
    tempDict = {i: tempDict[i] for i in myKeys}

    for i in range(len(list(tempDict.keys()))):
        comparisons = comparisons + 1
        tempArr[i] = list(tempDict.keys())[i]
        tempArrIndexes[i] = tempDict[list(tempDict.keys())[i]][0]

    tempArrFinalIndex = tempArrIndexes.copy()

    print(tempArr, tempArrIndexes)

    tempArrFinalIndex.append(0)
    #get the indexes array
    for i in range(len(tempArrIndexes)):
        comparisons = comparisons + 1
        tempArrFinalIndex[i+1] = tempArrFinalIndex[i]+tempArrFinalIndex[i+1]
    tempArrFinalIndex.pop()

    print(tempArr, tempArrIndexes, tempArrFinalIndex)

    #below sorts
    finalArr = arr.copy()
    for i in range(len(finalArr)):
        comparisons = comparisons + 1
        finalArr[i] = 0
    for i in range(len(tempArrFinalIndex)):
        for j in range(tempArrIndexes[i]):
            comparisons = comparisons + 1
            finalArr[tempArrFinalIndex[i]-j-1] = tempArr[i]
            tempArrIndexes[i] = tempArrIndexes[i] - 1
            print(finalArr, tempArrIndexes, tempArrFinalIndex[i])
    print(finalArr)
    end = time.time()
    print("Time: " + str(int((end-start)*1000)) + " milliseconds")
    print("Comparisons: " + str(comparisons))

def insertion(arr): # by alden
    start = time.time()
    tempArr = arr.copy()
    swaps = 0
    #repeat as many times as the length of the array
    for i in range(len(tempArr)):
        print(tempArr[i], end=" ")
        for j in reversed(range(i)):
            #if the value behind is greater, move it forward. continue backwords through the array
            if tempArr[j] > tempArr[j+1]:
                tempArr[j], tempArr[j+1] = tempArr[j+1], tempArr[j]
                swaps = swaps + 1
        print(tempArr)
    end = time.time()
    print("Time: " + str(int((end-start)*1000)) + " milliseconds")
    print("Number of swaps: " + str(swaps))

#start
go = True
while go: #oops this isn't working for some reason ill deal with it later
    print("Bubble\nCounting\nInsertion\nSelection")
    tempUserInput = input("What sorting algorithm would you like to use? ").lower()
    if tempUserInput not in ["bubble", "counting", "insertion", "selection"]:
        tempUserInput = input("Enter a valid sorting algorithm: ")
    else:
        go = False
        if tempUserInput == "bubble":
            #bubble(userInput)
            pass
        elif tempUserInput == "counting":
            counting(userInput)
        elif tempUserInput == "insertion":
            insertion(userInput)
        elif tempUserInput == "selection":
            #selection(userInput)
            pass