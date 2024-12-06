def is_out(lines, x, y):
  if x < 0 or x >= len(lines[0]):
    return True
  if y < 0 or y >= len(lines):
    return True
  return False


def is_loop(lines, init_guard_loc, new_blockage):
  lines[new_blockage[1]][new_blockage[0]] = ('#', set())
  next_change_map = [(0, -1), (1, 0), (0, 1), (-1, 0)]
  next_change_counter = 0
  guard_loc = (init_guard_loc[0], init_guard_loc[1])
  while True:
    # for line in lines:
    #   print([x[0] for x in line])
    # print('\n')
    next_change = next_change_map[next_change_counter]
    x, y = guard_loc[0], guard_loc[1]
    next_x, next_y = x + next_change[0], y + next_change[1]
    if is_out(lines, next_x, next_y):
      return False
    if lines[next_y][next_x][0] == '#':
      next_change_counter = (next_change_counter + 1) % 4
      continue
    if lines[next_y][next_x][0] == '.':
      lines[next_y][next_x] = ('X', {(x, y)})
      guard_loc = (next_x, next_y)
      # print('guard loc now: ({0},{1}), next: ({2},{3})'.format(x, y, next_x, next_y))
    elif lines[next_y][next_x][0] == 'X':
      if (x, y) in lines[next_y][next_x][1]:
        # print(lines[next_y][next_x][1], (x, y), (next_x, next_y))
        # for line in lines:
        #   print([x[0] for x in line])
        # print('\n')
        return True
      lines[next_y][next_x] = ('X', lines[next_y][next_x][1].union({(x, y)}))
      guard_loc = (next_x, next_y)
  return False


lines = open('data2.txt', "r").read().split("\n")
lines = [list(x) for x in lines if x]
init_guard_loc = (0, 0)
for y, line in enumerate(lines):
  for x, symbol in enumerate(line):
    if symbol == '^':
      init_guard_loc = (x, y)

lines = [[(x, set()) for x in line] for line in lines]
lines[init_guard_loc[1]][init_guard_loc[0]] = ('X', {(init_guard_loc[0], init_guard_loc[1])})

total = 0
for y, line in enumerate(lines):
  for x, symbol in enumerate(line):
    if symbol[0] == '.':
      lines_copy = [line[:] for line in lines]
      if is_loop(lines_copy, init_guard_loc, (x, y)):
        total += 1
  # print('done line {}'.format(y))

print(total)
