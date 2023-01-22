# https://stackoverflow.com/questions/38935169/convert-elements-of-a-list-into-binary
def to_binary(l):
  b = 0
  for n in l:
    b = 2 * b + n
  return b

def part1():
  lines = [l.strip() for l in open('input.txt')]
  rows = len(lines)
  cols = len(lines[0])
  common_bits = []
  for x in range(cols):
    c = {}
    for y in range(rows):
      v = lines[y][x]
      if not c.get(v):
        c[v] = 0
      c[v] += 1
    # too fancy, could just count number of 1's, and use len(lines) to find most common 1 or 0
    keys = list(c.keys())
    keys.sort(key=lambda k : c[k], reverse=True) # high to low
    common_bits.append(int(keys[0]))

  uncommon_bits = [(b - 1) * -1 for b in common_bits]
  uncommon_bin = to_binary(uncommon_bits)
  common_bin = to_binary(common_bits)
  print(common_bits, common_bin)
  print(uncommon_bits, uncommon_bin)
  print('power', common_bin * uncommon_bin)


part1()