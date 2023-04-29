import sys

for _ in range(int(sys.stdin.readline())):
  cursor = sys.stdin.readline().strip()
  left, right = [], []

  for cur in cursor:
    if cur == '<':
      if left:
        right.append(left.pop())
    elif cur == '>':
      if right:
        left.append(right.pop())
    elif cur == '-':
      if left:
        left.pop()
    else:
      left.append(cur)

  left.extend(reversed(right))
  print(''.join(left))