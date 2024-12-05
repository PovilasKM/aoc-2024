lines = [x for x in open('data2.txt', "r").read().split("\n") if x]

# append the array
for x in range(len(lines)):
  lines[x] = '.' + lines[x] + '.'
lines.insert(0, '.' * len(lines[0]))
lines.append('.' * len(lines[0]))

for line in lines:
  print(line)

xmases = 0

for y, line in enumerate(lines):
  for x, letter in enumerate(line):
    if letter != 'A':
      continue
    if (((lines[y - 1][x - 1] == 'M' and lines[y + 1][x + 1] == 'S') or (
      lines[y - 1][x - 1] == 'S' and lines[y + 1][x + 1] == 'M')) and
      ((lines[y - 1][x + 1] == 'M' and lines[y + 1][x - 1] == 'S') or (
        lines[y - 1][x + 1] == 'S' and lines[y + 1][x - 1] == 'M'))):
      xmases += 1
print(xmases)
