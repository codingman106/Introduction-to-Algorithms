nums = input('Enter nums: ').split(' ')
nums = [int(k) for k in nums]
for i in range(len(nums)):
  for j in range(1, len(nums)):
    if nums[j] < nums[j - 1]:
      nums[j], nums[j - 1] = nums[j - 1], nums[j]
print(nums)