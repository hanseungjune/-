import sys

trees = {}
idx = 0
while True:
  tree = sys.stdin.readline().strip()
  if not tree:
    break

  if tree in trees.keys():
    trees[tree] += 1
  else:
    trees[tree] = 1

  idx += 1

sort_trees = dict(sorted(trees.items()))

for item in sort_trees.items():
  print(f'{item[0]} {(item[1] / idx * 100):.4f}')