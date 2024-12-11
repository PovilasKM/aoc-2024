def safe_add(_map, key, amount):
  if key not in _map.keys():
    _map[key] = amount
  else:
    _map[key] += amount


lines = open('data.txt', "r").read().split("\n")
total = 0
symbols = {}
for symbol in [x for x in lines if x][0].split(' '):
  if symbol not in symbols.keys():
    symbols[symbol] = 1
  else:
    symbols[symbol] += 1

iterations = 25

for i in range(0, iterations):
  new_symbols = {}
  for symbol in symbols.keys():
    amount = symbols[symbol]
    if symbol == '0':
      safe_add(new_symbols, '1', amount)
    elif len(symbol) % 2 == 0:
      safe_add(new_symbols, symbol[:len(symbol)//2], amount)
      safe_add(new_symbols, str(int(symbol[len(symbol)//2:])), amount)
    else:
      safe_add(new_symbols, str(int(symbol) * 2024), amount)
  symbols = new_symbols

# print(symbols)
print(sum(symbols.values()))
