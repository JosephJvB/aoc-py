# read up some solutions after solving myself
# learned that cost calc for part 2 is called triangular numbers
# can get triangular numbers like this:
import math
def tri_nums(n):
  return math.floor(n * (n + 1) / 2)


memory = {}
calcd = 0
frommem = 0
def calc_cost(n):
  extra = 0
  cost = 0
  global frommem
  global calcd
  if memory.get(n):
    frommem += 1
    return memory[n]
  for x in range(n):
    cost += 1
    cost += extra
    extra += 1
  calcd += 1
  memory[n] = cost
  return cost
def part1():
  crabs = [int(s) for s in open('input.txt').read().split(',')]
  minx = min(crabs)
  maxx = max(crabs)
  print('min, max', minx, maxx)
  cheapest = -1
  xpos = -1
  for x in range(minx, maxx):
    cost = sum([abs(c - x) for c in crabs])
    if cost < cheapest or cheapest == -1:
      cheapest = cost
      xpos = x
  print('cheapest x pos', cheapest, xpos)

# part1()
def part2():
  crabs = [int(s) for s in open('input.txt').read().split(',')]
  print('num crabs', len(crabs))
  minx = min(crabs)
  maxx = max(crabs)
  print('min, max', minx, maxx)
  cheapest = -1
  xpos = -1
  for x in range(minx, maxx):
    cost = sum([
      calc_cost(abs(c - x)) for c in crabs
    ])
    if cost < cheapest or cheapest == -1:
      cheapest = cost
      xpos = x
  print('cheapest x pos', cheapest, xpos)

part2()
print(calcd, frommem)