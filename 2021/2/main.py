def part1():
  X = 0
  Y = 0
  for l in open('input.txt'):
    d, q = l.strip().split(' ')
    q = int(q)
    if d == 'forward':
      X += q
    if d == 'down':
      Y -= q
    if d == 'up':
      Y += q
  print('pos', X, Y)
  depth = Y * -1
  print('depth', depth)
  print('ans', X * depth)

def part2():
  X = 0
  Y = 0
  A = 0
  for l in open('input.txt'):
    d, q = l.strip().split(' ')
    q = int(q)
    if d == 'forward':
      X += q
      Y += (A * q)
    if d == 'down':
      # Y += q
      A += q
    if d == 'up':
      # Y -= q
      A -= q
    print(d, q, 'xya', X, Y, A)
  print('pos', X, Y, A)
  print('depth', Y)
  print('ans', X * Y)

part2()