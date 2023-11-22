#Insertion Sort Algorithm
nums = input('Enter nums: ')
nums = nums.split(' ')
nums = [int(k) for k in nums]
for i in range(1, len(nums)):
  key = nums[i]
  j = i - 1
  while j > -1 and nums[j] > key:
    nums[j + 1] = nums[j]
    j -= 1
  nums[j + 1] = key
print(nums)
