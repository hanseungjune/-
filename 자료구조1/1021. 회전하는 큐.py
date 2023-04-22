import sys, math
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
queue = deque(i for i in range(1, n+1))
circle = list(map(int, input().split()))
cnt = 0
for c in range(len(circle)):
  print(circle[c])
  print(queue)
  while True:
    if circle[c] == queue[0]:
      queue.popleft()
      break
    if len(queue)//2 % 2 == 1:
      # 시계방향
      if 0 < c <= len(queue)//2:
        queue.appendleft(queue.pop())
        cnt += 1
      # 반시계방향
      else:
        queue.append(queue.popleft())
        cnt += 1
    else:
      # 시계방향
      if 0 < c <= len(queue)//2:
        queue.appendleft(queue.pop())
        cnt += 1
      # 반시계방향
      else:
        queue.append(queue.popleft())
        cnt += 1
  print('카운트 ', cnt)
print(cnt)