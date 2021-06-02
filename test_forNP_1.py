

nums = [3, 1, 2, 10, 1]
nums1 = []
for i in range(len(nums)):
    counter = 0
    for j in range(i + 1):
        counter += nums[j]
    nums1.append(counter)

print(nums1)
