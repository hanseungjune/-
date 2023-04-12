import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
  data = input().split()
  lst.append(data)

stack = []
for i in range(n):
  if lst[i][0] == 'push':
    stack.append(int(lst[i][1]))
  
  elif lst[i][0] == 'top':
    if len(stack) == 0: print(-1)
    else: 
      top = stack[-1]
      print(top)

  elif lst[i][0] == 'size':
    print(len(stack))

  elif lst[i][0] == 'empty':
    if len(stack) == 0: print(1)
    else:
      print(0)

  elif lst[i][0] == 'pop':
    if len(stack) == 0: print(-1)
    else: 
      pop = stack.pop()
      print(pop)