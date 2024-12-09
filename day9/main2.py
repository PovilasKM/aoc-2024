def find_first_empty_index(symbols, size):
  for i in range(0, len(symbols)):
    if symbols[i][1] == -1 and symbols[i][0] >= size:
      return i
  return -1


line = open('data2.txt', "r").read()[:-1]
total = 0
symbols = []
id = 0
is_space = False
for symbol in line:
  if is_space:
    symbols.append((int(symbol), -1))
  else:
    symbols.append((int(symbol), id, False))
    id += 1
  is_space = not is_space
# print(symbols)

i = len(symbols)-1
while i >= 0:
  if symbols[i][1] == -1 or symbols[i][2]:
    i -= 1
    continue
  file_id = symbols[i][1]
  block_size = symbols[i][0]
  free_index = find_first_empty_index(symbols, block_size)
  if free_index == -1 or free_index > i:
    i -=1
    continue
  symbols[i] = (block_size, -1)
  symbols[free_index] = (symbols[free_index][0] - block_size, -1)
  symbols.insert(free_index, (block_size, file_id, True))

# print(symbols)
# remove non-existing space
symbols = [x for x in symbols if x[0] != 0]

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
    if symbols[i][1] != -1:
      total += multiplier * symbols[i][1]
    multiplier += 1
  i += 1

print(total)
