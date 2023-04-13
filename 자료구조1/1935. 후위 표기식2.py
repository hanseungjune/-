import sys
input = sys.stdin.readline

n = int(input())
lst = list(input().strip())
num = [int(input()) for i in range(n)]

stack = []

for i in lst:
  if i.isalpha():
    stack.append(num[ord(i)-65])
  else:
    b = stack.pop()
    a = stack.pop()

    if i == '+':
      a += b 
    elif i == '-':
      a -= b
    elif i == '*':
      a *= b
    elif i == '/':
      a /= b
    
    stack.append(a)

print(f"{stack[0]:.2f}")