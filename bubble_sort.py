import time
import random
 
arr=[]
amount = int(input("How many items would you like to sort\n:"))
for i in range(amount):
    arr.append(random.randint(1,100))
print('The list has over', amount,"Items in the list")

start = time.time()

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break

def bubbleSortsteps(arr):
    # the code is checking how long the list is.
    n = len(arr)

    # Now it sets a for loop to run for ever element in the list.
    for i in range(n):
        # This is used to see if the code is done, if a swap happend then we know that it isnt fully sorted,
        # When the list is fully sorted the value will not be changed, and the code will be done.
        swapped = False

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break



bubbleSort(arr)

print("Sorted array:\n")
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")
endtime = time.time()
print("\n time the program takes", round(endtime - start, 3),"Seconds")