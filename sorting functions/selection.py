import time



nums = [17, 30, 41, 15, 7, 12, 23, 25, 12]

for i in range(len(nums)-1):
    

    min_idx = i
    for j in range(i+1, len(nums)):
        if nums[min_idx] > nums[j]:
            min_idx = j
<<<<<<< HEAD:selection.py
    
    nums[i], nums[min_idx] = nums[min_idx], nums[i]
    print(f"Min Number {nums[i]}")
=======
    A[i], A[min_idx] = A[min_idx], A[i]
>>>>>>> 10ecb4db04b2f8a65503845976913e4060ed802a:sorting functions/selection.py

print ("Sorted array")
for i in range(len(nums)):
    print(nums[i],end=" ")
