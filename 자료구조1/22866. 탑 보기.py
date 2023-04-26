import sys
from collections import deque

n = int(sys.stdin.readline())
towers = deque(map(int, input().split()))
# 몇번 탑 : 탑 높이
tower_cnt = { i+1 : towers[i] for i in range(n) }

stack = []
for i in range(n):
  # tower[i] 기준으로 반복문 돌면서 stack에 넣기
  move = i
  while True:
    for j in range(move, 0, -1):
      if towers[move] > towers[j]:
        stack.append({j:towers[j]})
        break

    for k in range(move+1, n):
      if towers[move] > towers[k]:
        stack.append({k:towers[k]})
        break

    if stack[-1][1] > stack[-2][1]:
      move = stack[-2][0]
    elif stack[-1][1] < stack[-2][1]:
      move = stack[-1][0]
    else:
      break
  
  result = set(stack)
  closedBuilding = i
  for ele in stack:
    abs(i - ele[0])