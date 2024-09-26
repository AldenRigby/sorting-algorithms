import time
import random


nums = []
for i in range(1000):
    nums.append(random.randint(1,1000))
print(nums)

start = time.time()
for i in range(len(nums)-1):
    

    min_idx = i
    for j in range(i+1, len(nums)):
        if nums[min_idx] > nums[j]:
            min_idx = j
    
    nums[i], nums[min_idx] = nums[min_idx], nums[i]
    print(f"Min Number {nums[i]}")
end = time.time()
print ("Sorted array")
for i in range(len(nums)):
    print(nums[i],end=" ")
print("\n The program takes", round(end - start, 10), "seconds.")
