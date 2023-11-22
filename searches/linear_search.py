nums = [int(k) for k in input().split()]
target = int(input())
def lsearch(nums, target):
  for i in range(len(nums)):
    if nums[i] == target:
      return i
  return None
print(f'The index of {target} in {nums} is', lsearch(nums, target))