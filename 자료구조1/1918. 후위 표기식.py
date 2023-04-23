import sys
from collections import deque
input = sys.stdin.readline
stack = deque()
lst= deque(input().strip())
res=''
for l in lst:
  if l.isalpha():
    res+=l
  else:
    if l == '(':
      stack.append(l)
    elif l == '*' or l =='/':
      while stack and (stack[-1] == '*' or stack[-1] == '/'):
        res += stack.pop()
      stack.append(l)
    elif l == '+' or l == '-':
      while stack and stack[-1] != '(':
        res += stack.pop()
      stack.append(l)
    elif l == ')':
      while stack and stack[-1] != '(':
        res += stack.pop()
      stack.pop()
while stack:
  res += stack.pop()
print(res)
          
