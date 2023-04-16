import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
  lst = list(input().strip())
  
  stack = []
  for i in range(len(lst)):
    if lst[0] == ')': 
      print('NO') 
      break

    if lst[i] == ')':
      if len(stack) == 0: 
        print('NO')
        break
      else:
        stack.pop()

    if lst[i] == '(':
      stack.append(lst[i])
  else:
    if len(stack) >= 1:
      print('NO')
    else:
      print('YES')