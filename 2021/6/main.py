def part1(fish):
  NUM_DAYS = 18
  for day in range(NUM_DAYS):
    spawned = []
    print('day', day, 'fish', len(fish))
    for i in range(len(fish)):
      fish[i] -= 1
      if fish[i] == -1:
        fish[i] = 6
        spawned.append(8)
    fish += spawned
  print('fish', len(fish))

def part2(fish):
  day_fishnum_map = {}
  for i in range(9):
    day_fishnum_map[i] = 0
  for f in fish:
    day_fishnum_map[f] += 1
  NUM_DAYS = 256
  for day in range(NUM_DAYS):
    next_dict = {}
    num_parents = day_fishnum_map[0] # day 0 fish will give birth
    for i in range(9):
      if i == 0:
        next_dict[8] = num_parents # spawn new fish
      else:
        next_dict[i - 1] = day_fishnum_map[i]
    next_dict[6] += num_parents # add parents back to day 6
    day_fishnum_map = next_dict
  print(day_fishnum_map)
  fcount = sum([v for v in day_fishnum_map.values()])
  print('fish', fcount)


if __name__ == '__main__':
  input_list = [int(s) for s in open('input.txt', 'r').read().split(',')]
  # part1(input_list)
  part2(input_list)