lines = [x for x in open('data.txt', "r").read().split("\n") if x]
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
# print(antennas)

unique_anti_locations = set()
for symbol in antennas.keys():
  locations = antennas[symbol]
  combinations = [(a, b) for idx, a in enumerate(locations) for b in locations[idx + 1:]]
  for combination in combinations:
    x1,y1 = combination[0]
    x2,y2 = combination[1]
    x_diff, y_diff = abs(x1 - x2), abs(y1 - y2)

    # scenario +
    if x_diff == 0 or y_diff == 0:
      unique_anti_locations.update([(max(x1, x2) + x_diff, max(y1, y2) + y_diff), (min(x1, x2) - x_diff, min(y1, y2) - y_diff)])
    # scenario \
    elif (x1 - x2 > 0 and y1-y2 > 0) or (x1 - x2 < 0 and y1-y2 < 0):
      unique_anti_locations.update(
        [(max(x1, x2) + x_diff, max(y1, y2) + y_diff), (min(x1, x2) - x_diff, min(y1, y2) - y_diff)])
    # scenario /
    else:
      unique_anti_locations.update(
        [(max(x1, x2) + x_diff, min(y1, y2) - y_diff), (min(x1, x2) - x_diff, max(y1, y2) + y_diff)])


# remove invalid (out of bounds)
unique_anti_locations = [loc for loc in unique_anti_locations if (len_x > loc[0] >= 0) and (len_y > loc[1] >= 0)]
# print(unique_anti_locations)
print(len(unique_anti_locations))

# for y, line in enumerate(lines):
#   for x, sym in enumerate(line):
#     if (x, y) in unique_anti_locations:
#       print('#', end='')
#     print(sym, end='')
#   print()
