from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline

data = input().strip()

lst = deque()
stack = deque()
answer = set()

for index, d in enumerate(list(data)):
  if d == '(':
    stack.append(index)
  elif d == ')':
    start = stack.pop()
    end = index
    lst.append((start, end))

for i in range(1, len(lst)+1):
  for j in combinations(lst, i):
    data_cp = list(data)
    for k in j:
      start, end = k
      data_cp[start] = ''
      data_cp[end] = ''
    answer.add(''.join(data_cp))

for ans in sorted(answer):
  print(ans)  