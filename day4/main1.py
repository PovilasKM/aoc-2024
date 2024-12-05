lines = [x for x in open('data.txt', "r").read().split("\n") if x]

for line in lines:
  print(line)

xmases = 0

# diagonal /
diagonal_lines = []
start_x = 0
start_y = 0
while (start_x < len(lines[0]) -1 or start_y < len(lines)):
  line = ''
  y = start_y

  for i in range(start_x, -1, -1):
    if y + 1 > len(lines):
      break
    line += lines[y][i]
    y += 1  # fishy su Y
  diagonal_lines.append(line)
  if start_x + 1 < len(lines[0]):
    start_x += 1
  else:
    start_y += 1

for line in diagonal_lines:
  xmases += line.count('XMAS')
# / backwards
for line in diagonal_lines:
  xmases += line.count('SAMX')

# diagonal \
diagonal_lines = []
start_x = len(lines[0])-1
start_y = 0
while (start_x > 0 or start_y < len(lines)):
  line = ''
  y = start_y

  for i in range(start_x, len(lines[0])):
    if y + 1 > len(lines):
      break
    line += lines[y][i]
    y += 1  # fishy su Y
  diagonal_lines.append(line)
  if start_x - 1 >= 0:
    start_x -= 1
  else:
    start_y += 1

for line in diagonal_lines:
  xmases += line.count('XMAS')
# \ backwards
for line in diagonal_lines:
  xmases += line.count('SAMX')

# horizontal
for line in lines:
  xmases += line.count('XMAS')
# horizontal backwards
for line in lines:
  xmases += line.count('SAMX')

# vertical
for i in range(len(lines)):
  vertical_line = ''
  for line in lines:
    vertical_line += line[i]
  xmases += vertical_line.count('XMAS')
  # vertical backwards
  xmases += vertical_line.count('SAMX')

print(xmases)
