#made by Alden 1 1 1 3 2 4 9 9 7
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
                print(tempArr)
            else:
                continue
    end = time.time()
    print("Time: " + str(int((end-start)*1000)) + " milliseconds")
    print("Number of swaps: " + str(swaps))
insertion(userInput)