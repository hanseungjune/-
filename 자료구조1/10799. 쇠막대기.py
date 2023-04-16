from collections import deque

lst = input().replace('()', '/')
stack = deque()
pieces = 0

for i in lst:
  if i == '(':
    stack.append(i)
  elif i == '/':
    pieces += len(stack)
  elif i == ')':
    stack.pop()
    pieces += 1

print(pieces)