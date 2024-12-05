import re

lines = open('data2.txt', "r").read().split("\n")
total = 0
all_pattern = 'don\'t\(\)|do\(\)|mul\([0-9]{1,3}\,[0-9]{1,3}\)'
mul_pattern = 'mul\(([0-9]{1,3})\,([0-9]{1,3})\)'
do = True
for line in [x for x in lines if x]:
  matches = re.findall(all_pattern, line)
  for i, match in enumerate(matches):
    if match == "don't()":
      do = False
    elif match == 'do()':
      do = True
    elif match.startswith('mul'):
      if not do:
        continue
      else:
        nums = re.findall(mul_pattern, match)
        total += int(nums[0][0]) * int(nums[0][1])

print(total)
