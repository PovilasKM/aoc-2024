def find_first_empty_index(symbols):
  for i in range(0, len(symbols)):
    if symbols[i][1] == -1 and symbols[i][0] > 0:
      return i
  return -1


line = open('data.txt', "r").read()[:-1]
total = 0
symbols = []
id = 0
is_space = False
for symbol in line:
  if is_space:
    symbols.append((int(symbol), -1))
  else:
    symbols.append((int(symbol), id))
    id += 1
  is_space = not is_space
# print(symbols)

no_space = False
i = len(symbols)-1
while i >= 0:
  if symbols[i][1] == -1:
    i -= 1
    continue
  while symbols[i][0] > 0:
    file_id = symbols[i][1]
    free_index = find_first_empty_index(symbols)
    if free_index == -1 or free_index > i:
      no_space = True
      break
    symbols[i] = (symbols[i][0] - 1, file_id)
    # this file is already here
    # if symbols[free_index-1][1] == file_id:
    #   symbols[free_index - 1] = (symbols[free_index-1][0] + 1, file_id)
    #   symbols[free_index] = (symbols[free_index][0] - 1, symbols[free_index][1])
    # # file is not already here
    # else:
    symbols[free_index] = (symbols[free_index][0] - 1, -1)
    symbols.insert(free_index, (1, file_id))
    i += 1
  i -= 1
  if no_space:
    break

# remove non-existing space
symbols = [x for x in symbols if x[1] != -1 and x[0] != 0]

# print(symbols)
# join same numbers going in a row
i = 0
target = len(symbols) -1
while i < target:
  if symbols[i][1] == symbols[i+1][1]:
    symbols[i] = (symbols[i][0] + symbols[i+1][0], symbols[i][1])
    symbols.pop(i+1)
    target -= 1
  i += 1

# print(symbols)
total = 0
i = 0
multiplier = 0
while i < len(symbols):
  for j in range(0, symbols[i][0]):
    total += multiplier * symbols[i][1]
    multiplier += 1
  i += 1

print(total)
