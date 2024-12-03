lines = open('data1.txt', "r").read().split("\n")
total = 0
for line in [x for x in lines if x]:
  print(line)
print(total)
