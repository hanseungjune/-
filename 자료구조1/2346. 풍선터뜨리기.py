# import sys
# input = sys.stdin.readline

# n = int(input())
# queue = list(map(int, input().split()))
# idxs = list(i for i in range(n))

# i = 0
# while queue and idxs:
#   if len(idxs) == 1:
#     print(idxs[0]+1, end='')
#     break
#   print(idxs[i]+1, end=' ')
#   next = queue.pop(i)
#   idxs.pop(i)

#   if next > 0:
#     i += next-1
#   elif next < 0:
#     i -= len(queue)+next

from collections import deque

n = int(input())
balloons = list(map(int, input().split()))

dq = deque([(i+1, balloons[i]) for i in range(n)])
answer = []
cur_idx = 0

while dq:
  idx, val = dq[cur_idx]
  answer.append(idx)
  dq.remove((idx, val))

  if not dq:
    break

  if val > 0:
    cur_idx = (cur_idx + val -1) % len(dq)
  else:
    cur_idx = (cur_idx + val) % len(dq)

print(*answer)