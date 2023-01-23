def update_board(b, n):
  for y in range(len(b)):
    for x in range(len(b[y])):
      if b[y][x] == n:
        b[y][x] = 'X'

def check_win(b):
  for row in b:
    xs = [c for c in row if c == 'X']
    if len(xs) == len(row):
      return True
  for x in range(len(b[0])):
    xs = [r[x] for r in b if r[x] == 'X']
    if len(xs) == len(b):
      return True
  return False

def calc_score(b, n):
  s = 0
  for y in range(len(b)):
    for x in range(len(b[y])):
      c = b[y][x]
      if c == 'X':
        continue
      s += int(c)
  return s * int(n)

def print_board(b):
  for r in b:
    print('' .join(r))

def part2():
  txt_chunks = open('input.txt').read().split('\n\n')
  numbers = txt_chunks[0].split(',')
  boards = []
  for c in txt_chunks[1:]:
    b = []
    for l in c.split('\n'):
      line = []
      for n in l.strip().replace('  ', ' ').split(' '):
        line.append(n)
      b.append(line)
    boards.append(b)

  won_boards = set()
  last_board = [None, None, None] # index, board, number @ finish, could just save last_score, but that's harder to debug
  for ni, n in enumerate(numbers):
    if len(won_boards) == len(boards):
      print('finish @', ni + 1, '/', len(numbers))
      break
    for bi, b in enumerate(boards):
      if bi in won_boards:
        continue
      update_board(b, n)
      w = check_win(b)
      if w:
        won_boards.add(bi)
        last_board = [bi, b, n]
  print('last_board', last_board[0] + 1)
  print_board(last_board[1])
  print('score', calc_score(last_board[1], last_board[2]))

part2()

def part1():
  txt_chunks = open('input.txt').read().split('\n\n')
  numbers = txt_chunks[0].split(',')
  boards = []
  for c in txt_chunks[1:]:
    b = []
    for l in c.split('\n'):
      line = []
      for n in l.strip().replace('  ', ' ').split(' '):
        line.append(n)
      b.append(line)
    boards.append(b)

  for ni, n in enumerate(numbers):
    for bi, b in enumerate(boards):
      update_board(b, n)
      w = check_win(b)
      if w:
        print('board', bi + 1, 'won @ number', ni, n)
        print('score', calc_score(b, n))
        print_board(b)
        return
