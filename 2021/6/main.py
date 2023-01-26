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
  fish_list = [0 for i in range(9)]
  for f in fish:
    fish_list[f] += 1
  NUM_DAYS = 256
  for day in range(NUM_DAYS):
    parents = fish_list[0] # day 0 fish will give birth
    next_fish = []
    for i in range(1, 9):
      next_fish.append(fish_list[i])
    next_fish.append(parents)
    next_fish[6] += parents # add parents back to day 6
    fish_list = next_fish
  print(fish_list)
  print('fish', sum(fish_list))


if __name__ == '__main__':
  input_list = [int(s) for s in open('input.txt', 'r').read().split(',')]
  # part1(input_list)
  part2(input_list)