import time



nums = [17, 30, 41, 15, 7, 12, 23, 25, 12]

for i in range(len(nums)-1):
    

    min_idx = i
    for j in range(i+1, len(nums)):
        if nums[min_idx] > nums[j]:
            min_idx = j
    
    nums[i], nums[min_idx] = nums[min_idx], nums[i]
    print(f"Min Number {nums[i]}")

print ("Sorted array")
for i in range(len(nums)):
    print(nums[i],end=" ")
