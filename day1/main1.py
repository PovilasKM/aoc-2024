lines = open('data.txt', "r").read().split("\n")
total = 0
lists = [[], []]
for line in [x for x in lines if x]:
  [a, b] = line.split('   ')
  lists[0].append(int(a))
  lists[1].append(int(b))
lists[0].sort()
lists[1].sort()
for i, a in enumerate(lists[0]):
  total += abs(a - lists[1][i])
print(total)
