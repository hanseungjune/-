import sys

n = int(sys.stdin.readline())
towers = list(map(int, sys.stdin.readline().split()))
# 몇번 탑 : 탑 높이
tower_cnt = [ (i+1, towers[i]) for i in range(n) ]

for i in range(n):  
  stack = []  
  # tower[i] 기준으로 반복문 돌면서 stack에 넣기
  move = i
  while True:
    for j in range(move, 0, -1):
      if towers[move] < towers[j]:
        stack.append((j,towers[j]))
        break

    for k in range(move+1, n):
      if towers[move] < towers[k]:
        stack.append((k,towers[k]))
        break
    else:
      break

    if len(stack) >= 2:
      if stack[-1][1] > stack[-2][1]:
        move = stack[-2][0]
      elif stack[-1][1] < stack[-2][1]:
        move = stack[-1][0]
      else:
        break
    else:
      move = stack[-1][0]
  
  result = set(stack)
  closedBuilding = 0
  min_dist = 1e9
  for ele in stack[::-1]:
    dist = abs(i - ele[0])
    if min_dist > dist:
      closedBuilding = ele[0]

  if len(result) == 0:
    print(0)
  else:
    print(len(result), closedBuilding+1)