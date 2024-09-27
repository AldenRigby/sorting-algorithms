import time

nums = [5, 9, 10, 12, 13, 7, 5]
print("Original list:", nums)

start = time.time()

swap_count = 0

for i in range(len(nums) - 1):
    min_idx = i
    for j in range(i + 1, len(nums)):
        if nums[min_idx] > nums[j]:
            min_idx = j
            
    if min_idx != i:
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
        swap_count += 1  # Increment the swap counter
        print(f"Swapped indices {i} and {min_idx}: {nums}")

end = time.time()

print("Sorted array:", nums)
print(f"\nTotal swaps: {swap_count}")
print("Time: " + str(int((end-start)*1000)) + " milliseconds")

