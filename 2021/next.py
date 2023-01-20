import os

def main():
  p = os.path.dirname(os.path.realpath(__file__))
  folders = [n for n in os.listdir(p) if os.path.isdir(n)]
  dir_num = len(folders) + 1
  if dir_num > 25:
    return
  next_dir = p + '/' + str(dir_num)
  os.mkdir(next_dir)
  with open(next_dir + '/main.py', 'w') as f:
    pass
  with open(next_dir + '/input.txt', 'w') as f:
    pass
  print('created', next_dir, 'main.py and input.txt')


# if os.path.exists()

if __name__ == '__main__':
  main()