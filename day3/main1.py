import re

lines = open('data.txt', "r").read().split("\n")
total = 0
pattern = 'mul\(([0-9]{1,3})\,([0-9]{1,3})\)'
for line in [x for x in lines if x]:
  muls = re.findall(pattern, line)
  for mul in muls:
    total += int(mul[0]) * int(mul[1])
print(total)
