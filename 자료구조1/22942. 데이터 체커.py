import sys
input = sys.stdin.readline
n = int(input())

stack = []
for _ in range(n):
  x, r = map(int, input().split())
  stack.append({x+r, x, x-r})
  
    
