# https://stackoverflow.com/questions/38935169/convert-elements-of-a-list-into-binary
def to_binary(l):
  b = 0
  for n in l:
    b = 2 * b + n
  return b

def get_ox_char(l, x):
  rows = len(l)
  half = rows / 2
  zeros = 0
  for y in range(rows):
    v = l[y][x]
    if v == '0':
      zeros += 1

  if zeros == half:
    return '1'
  if zeros < half:
    return '1'
  if zeros > half:
    return '0'

def part2():
  lines = [l.strip() for l in open('input.txt')]

  oxlines = lines.copy()
  co2lines = lines.copy()
  oxpref = ''
  co2pref = ''
  for x in range(len(lines[0])):
    # every loop must calculate next most common char for each remaining set
    if len(oxlines) != 1:
      oxpref += get_ox_char(oxlines, x)
      oxlines = [l for l in oxlines if l.startswith(oxpref)]
    if len(co2lines) != 1:
      co2pref += '0' if get_ox_char(co2lines, x) == '1' else '1'
      co2lines = [l for l in co2lines if l.startswith(co2pref)]

  lastox = oxlines[0]
  lastco2 = co2lines[0]

  print(lastox, lastco2)
  ox_bin = to_binary(int(c) for c in list(lastox))
  co2_bin = to_binary(int(c) for c in list(lastco2))
  print(ox_bin, co2_bin)
  print(ox_bin * co2_bin)

  # 001100001000 110011110011
  # 776 3315
  # 2572440 - too low

  # 001100111001 110100101111
  # 825 3375
  # 2784375

def part1():
  lines = [l.strip() for l in open('input.txt')]
  rows = len(lines)
  cols = len(lines[0])
  common_bits = []
  uncommon_bits = []
  half = rows / 2
  for x in range(cols):
    c = 0
    uc = 1
    zeros = 0
    for y in range(rows):
      v = lines[y][x]
      if v == '0':
        zeros += 1
    if zeros < half:
      c = 1
      uc = 0
    common_bits.append(c)
    uncommon_bits.append(uc)

  uncommon_bin = to_binary(uncommon_bits)
  common_bin = to_binary(common_bits)
  print(common_bits, common_bin)
  print(uncommon_bits, uncommon_bin)
  print('power', common_bin * uncommon_bin)


part2()