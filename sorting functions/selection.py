#made by Samuel Rico Rodriguez Correa Melo Rey Reyes.

import time

#original array
nums = [5, 9, 10, 12, 13, 7, 5]

#print original array
print("Original list:", nums)

#start the timer
start = time.time()

#create swap count variable that tracks the swaps in the sorting process
swap_count = 0

for i in range(len(nums) - 1): #iterate through the list except the last one
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

