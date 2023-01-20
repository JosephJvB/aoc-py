def part2():
  nums = [int(l.strip()) for l in open('input.txt')]
  inc = 0
  prev = None
  for i in range(len(nums)):
    if i < 2:
      continue
    s = nums[i - 2:i + 1]
    t = sum(s)
    if prev is None:
      prev = t
      continue
    if t > prev:
      inc += 1
    prev = t
  print('inc slices', inc)

part2()

def part1():
  inc = 0
  prev = None
  for l in open('input.txt'):
    n = int(l.strip())
    if prev is None:
      prev = n
      continue
    if prev < n:
      inc += 1
    prev = n

  print(inc, 'increasing steps')