import time
import random
 
array=[]
amount = int(input("How many items would you like to sort\n:"))
for i in range(amount):
    array.append(random.randint(1,10000))
print('The list has over', amount,"Items in the list")

start = time.time()

def bubbleSort(array):
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


alg = int(input('Would you like to see the steps\n 1(yes) 2(no)\n'))
if alg == 1:
    bubbleSortsteps(array)
else:
    bubbleSort(array)

print("Sorted arrayay:\n")
for i in range(len(array)):
    print("%d" % array[i], end=" ")
endtime = time.time()
print("\n time the program takes", round(endtime - start, 3),"Seconds")