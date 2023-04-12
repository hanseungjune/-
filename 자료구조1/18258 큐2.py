import sys
from collections import deque
input = sys.stdin.readline


n = int(input())

queue = deque()
answer = []
for _ in range(n):
  data = input().split()
  if data[0] == 'push':
    queue.append(data[1])
  elif data[0] == 'front':
    if len(queue) == 0: answer.append(-1)
    else:
      answer.append(queue[0])
  elif data[0] == 'back':
    if len(queue) == 0: answer.append(-1)
    else:
      answer.append(queue[-1])
  elif data[0] == 'pop':
    if len(queue) == 0: answer.append(-1)
    else:
      a = queue.popleft()
      answer.append(a)
  elif data[0] == 'size':
    answer.append(len(queue))
  elif data[0] == 'empty':
    if len(queue) == 0: answer.append(1)
    else: answer.append(0)

for _ in answer:
  print(_)