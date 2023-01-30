import itertools

def parse2():
  lines = []
  for l in open('input.txt'):
    l = l.strip()
    segments = [s.split(' ') for s in l.split(' | ')]
    lines.append(segments)
  return lines

def seg_to_digits_2(s, m2):
  l = len(s)
  m1 = {
    2: 1,
    3: 7,
    4: 4,
    7: 8,
  }
  if m1.get(l):
    return m1[l]
  if m2.get(s):
    return m2[s]
  print('key', s, 'not in map', m2)
  exit()

def valid_digit(perm, segment):
  pass

def create_map(poss_signals, signal):
  m = {} # use signal values to create map
  poss_signals = itertools.permutations('abcdefg')
  # digits to find: 0, 2, 3, 5, 6, 9
  # ignore = 2, 3, 4, 7
  to_find = {
    5: [2, 3, 5],
    6: [0, 6, 9],
  }
  pass


  return m

def part2():
  lines = parse2()
  total = 0
  poss_signals = itertools.permutations('abcdefg')
  for signal, output in lines:
    m2 = create_map(poss_signals, signal)
    v = ''
    for seg in output:
      d = seg_to_digits_2(seg, m2)
      v += str(d)
    print('line value', v)
    total += int(v)

part2()

def parse():
  signal_segments = []
  output_segments = []
  for l in open('input.txt'):
    l = l.strip()
    s, o = l.split(' | ')
    signal_segments += s.split(' ')
    output_segments += o.split(' ')
  return [signal_segments, output_segments]

def seg_to_digits(s):
  l = len(s)
  m = {
    2: 1,
    3: 7,
    4: 4,
    7: 8,
  }
  if m.get(l):
    return m[l]
  return None

def part1():
  signal, output = parse()
  known = 0
  print(output)
  for s in output:
    r = seg_to_digits(s)
    if r is not None:
      known += 1
  print('known digits', known)

# part1() # 452