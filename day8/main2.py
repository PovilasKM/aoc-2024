def is_not_both_out_of_bounds(coords, len_x, len_y):
  x1, y1 = coords[0]
  x2, y2 = coords[1]
  if (x1 < 0 or x1 >= len_x or y1 < 0 or y1 >= len_y) and (x2 < 0 or x2 >= len_x or y2 < 0 or y2 >= len_y):
    return False
  return True


lines = [x for x in open('data2.txt', "r").read().split("\n") if x]
total = 0
antennas = {}
for y, line in enumerate(lines):
  for x, symbol in enumerate(line):
    if symbol == '.':
      continue
    if symbol not in antennas.keys():
      antennas[symbol] = [(x, y)]
    else:
      antennas[symbol].append((x, y))
len_x = len(lines[0])
len_y = len(lines)

unique_anti_locations = set()
for symbol in antennas.keys():
  locations = antennas[symbol]
  combinations = [(a, b) for idx, a in enumerate(locations) for b in locations[idx + 1:]]
  if len(combinations) == 1:
    continue
  for combination in combinations:
    x1, y1 = combination[0]
    x2, y2 = combination[1]
    x_diff, y_diff = abs(x1 - x2), abs(y1 - y2)

    unique_anti_locations.update([combination[0], combination[1]])
    # scenario +
    if x_diff == 0 or y_diff == 0:
      coords = [(max(x1, x2), max(y1, y2)), (min(x1, x2), min(y1, y2))]
      while is_not_both_out_of_bounds(coords, len_x, len_y):
        coords = [(coords[0][0] + x_diff, coords[0][1] + y_diff), (coords[1][0] - x_diff, coords[1][1] - y_diff)]
        unique_anti_locations.update(coords)
    # scenario \
    elif (x1 - x2 > 0 and y1 - y2 > 0) or (x1 - x2 < 0 and y1 - y2 < 0):
      coords = [(max(x1, x2), max(y1, y2)), (min(x1, x2), min(y1, y2))]
      while is_not_both_out_of_bounds(coords, len_x, len_y):
        coords = [(coords[0][0] + x_diff, coords[0][1] + y_diff), (coords[1][0] - x_diff, coords[1][1] - y_diff)]
        unique_anti_locations.update(coords)
    # scenario /
    else:
      coords = [(max(x1, x2), min(y1, y2)), (min(x1, x2), max(y1, y2))]
      while is_not_both_out_of_bounds(coords, len_x, len_y):
        coords = [(coords[0][0] + x_diff, coords[0][1] - y_diff), (coords[1][0] - x_diff, coords[1][1] + y_diff)]
        unique_anti_locations.update(coords)

# remove invalid (out of bounds)
unique_anti_locations = [loc for loc in unique_anti_locations if (len_x > loc[0] >= 0) and (len_y > loc[1] >= 0)]
print(len(unique_anti_locations))

# for y, line in enumerate(lines):
#   for x, sym in enumerate(line):
#     if (x, y) in unique_anti_locations:
#       print('#', end='')
#     else:
#       print(sym, end='')
#   print()
