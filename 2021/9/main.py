def neighbours(x, y):
  return [
    [x + 1, y],
    [x - 1, y],
    [x, y + 1],
    [x, y - 1],
  ]

def part1():
  grid = [[int(c) for c in l.strip()] for l in open('input.txt')]
  # low point if has no neighbours lower than it?
  low_points = []
  risk = 0
  for y in range(len(grid)):
    row = grid[y]
    for x in range(len(row)):
      c = grid[y][x]
      higher_neighbour = False
      for nx, ny in neighbours(x, y):
        if nx < 0 or ny < 0:
          continue
        if nx >= len(row) or ny >= len(grid):
          continue
        if grid[ny][nx] <= c:
          higher_neighbour = True
          break
      if not higher_neighbour:
        # low_points.append([x, y, c])
        risk += c + 1
  # print(low_points)
  print('risk', risk)

part1()
# 1830 - too high