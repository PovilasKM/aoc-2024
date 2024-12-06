def is_out(lines, x, y):
  if x < 0 or x >= len(lines[0]):
    return True
  if y < 0 or y >= len(lines):
    return True
  return False


lines = open('data.txt', "r").read().split("\n")
guard_loc = (0, 0)
next_change_map = [(0, -1), (1, 0), (0, 1), (-1, 0)]
next_change_counter = 0
lines = [list(x) for x in lines if x]
for y, line in enumerate(lines):
  for x, symbol in enumerate(line):
    if symbol == '^':
      guard_loc = (x, y)
lines[guard_loc[1]][guard_loc[0]] = 'X'

while True:
  next_change = next_change_map[next_change_counter]
  x, y = guard_loc[0], guard_loc[1]
  next_x, next_y = x + next_change[0], y + next_change[1]
  if is_out(lines, next_x, next_y):
    break
  if lines[next_y][next_x] == '#':
    next_change_counter = (next_change_counter + 1) % 4
    continue
  if lines[next_y][next_x] == '.' or lines[next_y][next_x] == 'X':
    lines[next_y][next_x] = 'X'
    guard_loc = (next_x, next_y)
  # for line in lines:
  #   print(line)
  # print('\n')

total = 0
for y, line in enumerate([x for x in lines if x]):
  for x, symbol in enumerate(line):
    if symbol == 'X':
      total += 1

print(total)
