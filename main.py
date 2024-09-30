#Made by Samuel Ellis, Sam Rico, and Alden Rigby

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
            for i in range(30):
                userInput.append(random.randint(0,9))
        else:
            tempUserInput = tempUserInput.split(" ")
        for i in tempUserInput:
            userInput.append(int(i))
        go = False
    except:
        print("That isn't a valid list.")
#userInput should now be a list of numbers

def counting(arr): # by alden
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
        print(tempArr[i])
        for j in reversed(range(i)):
            #if the value behind is greater, move it forward. continue backwords through the array
            if tempArr[j] > tempArr[j+1]:
                tempArr[j], tempArr[j+1] = tempArr[j+1], tempArr[j]
                swaps = swaps + 1
            else:
                continue
            print(tempArr)
    end = time.time()
    print("Time: " + str(int((end-start)*1000)) + " milliseconds")
    print("Number of swaps: " + str(swaps))

def selection(arr): # by sam rico
    nums = arr.copy()
    #print original array
    print("Original list:", nums)

    #start the timer
    start = time.time()

    #create swap count variable that tracks the swaps in the sorting process
    swap_count = 0

    for i in range(len(nums) - 1): #iterate through the list except the last
        min_idx = i #initialize min_idx
        for j in range(i + 1, len(nums)): #do if new smalles element is found
            if nums[min_idx] > nums[j]: #check smallest element
                min_idx = j #updates smallest element
                
        if min_idx != i:
            nums[i], nums[min_idx] = nums[min_idx], nums[i] #swap elements
            swap_count += 1  # Increment the swap counter
            print(f"Swapped indices {i} and {min_idx}: {nums}")

    #stop the timer
    end = time.time()

    print("Sorted array:", nums)
    print(f"\nTotal swaps: {swap_count}")
    print("Time: " + str(int((end-start)*1000)) + " milliseconds")

def bubbleSort(array): # by sam ellis
    n = len(array)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
        if (swapped == False):
            break

def bubbleSortsteps(array):
    # the code is checking how long the list is.
    n = len(array)
    print(f"Length of arrayay: {array}")

    # Now it sets a for loop to run for ever element in the list.
    for i in range(n):
        # This is used to see if the code is done, if a swap happend then we know that it isnt fully sorted,
        # When the list is fully sorted the value will not be changed, and the code will be done.
        swapped = False

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # Look through the arrayay from 0 to n-i-1
            # Swap if the other number is greater
            # than the move to the next number

            if array[j] > array[j+1]:
                print(f"  Swapping: {array[j]} and {array[j + 1]}")
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
        print(f"Current sublist: {array[:n-i]} + {array[n-i:]}")
        if (swapped == False):
            break

def bubble(arr):
    array = arr.copy()
    alg = int(input('Would you like to see the steps\n 1(yes) 2(no)\n'))
    start = time.time()
    if alg == 1:
        bubbleSortsteps(array)
    else:
        bubbleSort(array)
    print("Sorted arrayay:\n")
    for i in range(len(array)):
        print("%d" % array[i], end=" ")
    endtime = time.time()
    print("\n time the program takes", round(endtime - start, 3),"Seconds")

#start
go = True
while go: # ask player for what algorithm they want
    print("\nBubble\nCounting\nInsertion\nSelection")
    tempUserInput = input("What sorting algorithm would you like to use? ").lower()
    if tempUserInput not in ["bubble", "counting", "insertion", "selection"]:
        print("\nBubble\nCounting\nInsertion\nSelection")
        tempUserInput = input("Enter a valid sorting algorithm: ")
    else:
        if tempUserInput == "bubble":
            bubble(userInput)
        elif tempUserInput == "counting":
            counting(userInput)
        elif tempUserInput == "insertion":
            insertion(userInput)
        elif tempUserInput == "selection":
            selection(userInput)