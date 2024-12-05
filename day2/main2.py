def is_safe(nums):
  is_increase = nums[0] < nums[1]
  for i, num in enumerate(nums[:-1]):
    if not ((nums[i] < nums[i + 1]) == is_increase) or not (1 <= abs(nums[i] - nums[i + 1]) <= 3):
      return False
  return True


lines = open('data2.txt', "r").read().split("\n")
safeLines = 0
for line in [x for x in lines if x]:
  nums = [int(x) for x in line.split(' ')]
  _is_safe = is_safe(nums)
  if _is_safe:
    safeLines += 1
  else:
    for i in range(len(nums)):
      _is_safe = is_safe(nums[:i] + nums[i + 1:])
      if _is_safe:
        safeLines += 1
        break
print(safeLines)
