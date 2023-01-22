# https://stackoverflow.com/questions/38935169/convert-elements-of-a-list-into-binary
def to_binary(l):
  b = 0
  for n in l:
    b = 2 * b + n
  return b

def part2():
  lines = [l.strip() for l in open('input.txt')]
  rows = len(lines)
  cols = len(lines[0])
  half = rows / 2


  oxmatch = []
  co2match = []
  for x in range(cols):
    zeros = 0
    for y in range(rows):
      v = lines[y][x]
      if v == '0':
        zeros += 1
    if zeros == half:
      oxmatch.append('1')
      co2match.append('0')
    if zeros < half:
      oxmatch.append('1')
      co2match.append('0')
    if zeros > half:
      oxmatch.append('0')
      co2match.append('1')

  oxmatches = lines.copy()
  co2matches = lines.copy()
  for x in range(cols):
    _ox = ''.join(oxmatch[0:x])
    _co2 = ''.join(co2match[0:x])
    if len(oxmatches) != 1:
      oxmatches = [l for l in oxmatches if l.startswith(_ox)]
    if len(co2matches) != 1:
      co2matches = [l for l in co2matches if l.startswith(_co2)]

  lastox = oxmatches[0]
  lastco2 = co2matches[0]

  print(lastox, lastco2)
  ox_bin = to_binary(int(c) for c in list(lastox))
  co2_bin = to_binary(int(c) for c in list(lastco2))
  print(ox_bin, co2_bin)
  print(ox_bin * co2_bin)

  # 001100001000, 110011110011
  # 776 3315
  # 2572440 - too low

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