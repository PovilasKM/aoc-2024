lines = open('data.txt', "r").read().split("\n")
safeLines = 0
for line in [x for x in lines if x]:
  nums = [int(x) for x in line.split(' ')]
  is_increase = nums[0] < nums[1]
  is_safe = True
  for i, num in enumerate(nums[:-1]):
    if not ((nums[i] < nums[i + 1]) == is_increase) or not (1 <= abs(nums[i] - nums[i + 1]) <= 3):
      is_safe = False

  if is_safe:
    safeLines += 1
print(safeLines)
