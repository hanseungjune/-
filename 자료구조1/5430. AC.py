import sys
from collections import deque

t = int(sys.stdin.readline())
for _ in range(t):
  p = sys.stdin.readline().strip()
  n = int(sys.stdin.readline())
  lst = sys.stdin.readline().strip()[1:-1].split(',')
  queue = deque(lst)

  flag = 1
  if n == 0:
    queue = deque()
  r = 0
  for j in p:
    if j == 'R':
      r += 1
    elif j == 'D':
      if len(queue) == 0:
        print("error")
        flag = 0
        break
      else:
        if r % 2 == 0:
          queue.popleft()
        else:
          queue.pop()
  else:
    if r % 2 == 0:
      print("[" + ",".join(queue) + "]")
    else:
      queue.reverse()
      print("[" + ",".join(queue) + "]")