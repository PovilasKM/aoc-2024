lines = open('data2.txt', "r").read().split("\n")
maze = []
trailheads = []
for y, line in enumerate([x for x in lines if x]):
  maze_row = []
  for x, num in enumerate([int(x) for x in line]):
    maze_row.append(num)
    if num == 0:
      trailheads.append((x+1, y+1))
  maze.append(maze_row)
# print(trailheads)

# append the maze
for x in range(len(maze)):
  maze[x] = [0] + maze[x] + [0]
maze.insert(0, [0] * len(maze[0]))
maze.append([0] * len(maze[0]))

directions = [(1,0),(0,1),(-1,0),(0,-1)]
summits = 0
for trailhead in trailheads:
  head_summits = []
  heads = [trailhead]
  while len(heads) > 0:
    new_heads = []
    for head in heads:
      current_spot = maze[head[1]][head[0]]
      for direction in directions:
        new_spot = maze[head[1]+direction[1]][head[0]+direction[0]]
        if new_spot == current_spot + 1:
          if new_spot == 9:
            head_summits.append((head[0] + direction[0], head[1] + direction[1]))
          else:
            new_heads.append((head[0]+direction[0], head[1]+direction[1]))
    heads = new_heads
  # print(len(head_summits))
  summits += len(head_summits)
print(summits)

