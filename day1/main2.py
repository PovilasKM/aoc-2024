lines = open('data2.txt', "r").read().split("\n")
total = 0
lists = [[], []]
for line in [x for x in lines if x]:
  [a, b] = line.split('   ')
  lists[0].append(int(a))
  lists[1].append(int(b))

for a in lists[0]:
  total += a * lists[1].count(a)
print(total)
