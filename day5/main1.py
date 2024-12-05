lines = open('data.txt', "r").read().split("\n")
total = 0
rules = {}
orders = []
rules_processed = 0
for line in [x for x in lines if x]:
  if '|' in line:
    a,b = line.split('|')
    a = int(a)
    b = int(b)
    if a in rules.keys():
      rules[a].add(b)
    else:
      rules[a] = {b}
  else:
    orders.append([int(x) for x in line.split(',')])

for rule_key in rules:
  next_keys = rules[rule_key]
  is_before = next_keys
  while len(next_keys) != 0:
    tmp_next_keys = set()
    for key in next_keys:
      is_before.add(key)
      if key in rules.keys() and key not in is_before:
        tmp_next_keys.update(rules[key])
    next_keys = tmp_next_keys
  rules[rule_key] = is_before
  rules_processed += 1

for order in orders:
  is_in_order = True
  for i, num in enumerate(order):
    next_elements = order[i+1:]
    if num not in rules.keys():
      continue
    if not set(next_elements).issubset(rules[num]):
      is_in_order = False
      break

    previous_elements = order[:i]
    if len(set(previous_elements).intersection(rules[num])) > 0:
      is_in_order = False
      break

  if is_in_order:
    total += int(order[(len(order)-1)//2])

print(total)

