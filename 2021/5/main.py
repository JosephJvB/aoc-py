import json
def parse():
  vents = []
  for line in open('input.txt'):
    v = []
    for c in line.split(' -> '):
      for p in c.split(','):
        v.append(int(p))
    vents.append(v)
  return vents

def make_grid(X, Y):
  return [['.' for x in range(X + 1)] for y in range(Y + 1)]
def copy_grid(g):
  return [l.copy() for l in g]

def add_diag_vent(v, coords):
  x1, y1, x2, y2 = v
  x = x1
  y = y1
  xinc = 1
  yinc = 1
  if x1 > x2:
    xinc = -1
  if y1 > y2:
    yinc = -1
  # s = ''.join([str(c) for c in v])
  # print(s, xinc, yinc, max(x1, x2))
  for i in range(abs(x1 - x2) + 1):
    c = f'{x}x{y}'
    # print(s, c)
    if not coords.get(c):
      coords[c] = 0
    coords[c] += 1
    y += yinc
    x += xinc

def add_straight_vent(v, coords):
  x1, y1, x2, y2 = v
  if x1 != x2:
    for x in range(min(x1, x2), max(x1, x2) + 1):
      c = f'{x}x{y1}'
      if not coords.get(c):
        coords[c] = 0
      coords[c] += 1
  if y1 != y2:
    for y in range(min(y1, y2), max(y1, y2) + 1):
      c = f'{x1}x{y}'
      if not coords.get(c):
        coords[c] = 0
      coords[c] += 1

def part2():
  vents = parse()
  coords = {}
  for v in vents:
    x1, y1, x2, y2 = v
    if x1 == x2 or y1 == y2:
      add_straight_vent(v, coords)
    else:
      add_diag_vent(v, coords)
  overlap = [k for k in coords if coords[k] > 1]
  print('overlap', len(overlap))
# part2()

def part1():
  vents = parse()
  straight_vents = []
  X = 0
  Y = 0
  for v in vents:
    x1, y1, x2, y2 = v
    if x1 == x2 or y1 == y2:
      X = max(x1, x2, X)
      Y = max(y1, y2, Y)
      straight_vents.append(v)
  with open('working/vents.json', 'w') as f:
    f.write(json.dumps(straight_vents))
  grid = make_grid(X, Y)
  copy = copy_grid(grid)
  coords = {}
  for v in straight_vents:
    x1, y1, x2, y2 = v
    g = copy_grid(copy)
    if x1 != x2:
      for x in range(min(x1, x2), max(x1, x2) + 1):
        c = f'{x}x{y1}'
        if not coords.get(c):
          coords[c] = 0
        coords[c] += 1
        g[y1][x] = 'x'
        grid[y1][x] = str(coords[c])
    if y1 != y2:
      for y in range(min(y1, y2), max(y1, y2) + 1):
        c = f'{x1}x{y}'
        if not coords.get(c):
          coords[c] = 0
        coords[c] += 1
        g[y][x1] = 'x'
        grid[y][x1] = str(coords[c])
    name = ''.join([str(c) for c in v])
    with open(f'working/{name}.txt', 'w') as f:
      f.write('\n'.join([''.join(l) for l in g]))
  with open('working/grid.txt', 'w') as f:
    f.write('\n'.join([''.join(l) for l in grid]))
  overlap = [k for k in coords if coords[k] > 1]
  print('overlap', len(overlap))
# part1()