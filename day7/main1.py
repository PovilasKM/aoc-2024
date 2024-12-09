def verify(target, total, nums):
  if len(nums) == 0:
    return total
  if total > target:
    return total
  mul_res = verify(target, total * nums[0], nums[1:])
  if mul_res == target:
    return mul_res
  return verify(target, total + nums[0], nums[1:])


lines = open('data.txt', "r").read().split("\n")
instructions = []
for line in [x for x in lines if x]:
  result = int(line.split(':')[0])
  rest = [int(x) for x in line.split(': ')[1].split(' ')]
  instructions.append([result] + rest)

result = 0
for instruction in instructions:
  target = instruction[0]
  total = instruction[1]
  nums = instruction[2:]
  if target == verify(target, total, nums):
    result += target

print(result)
