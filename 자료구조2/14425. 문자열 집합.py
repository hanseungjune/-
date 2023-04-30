# 문자열 개수n, m
# 집합 s에 포함 되어있는 문자열
# 검사해야하는 문자열
import sys
n, m = map(int, sys.stdin.readline().split())

stack = set()
for _ in range(n):
  stack.add(sys.stdin.readline().rstrip())

cnt = 0
for i in range(m):
  check = sys.stdin.readline().rstrip()
  if check in stack:
    cnt += 1

print(cnt)