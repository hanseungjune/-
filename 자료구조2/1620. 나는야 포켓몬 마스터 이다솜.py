import sys
n, m = map(int, sys.stdin.readline().split())
arr = ["" for _ in range(n)]
diction = dict()

for i in range(n):
  arr[i] = sys.stdin.readline().rstrip()
  diction[arr[i]] = i+1

for j in range(m):
  exp = sys.stdin.readline().rstrip()
  if exp.isdigit():
    print(arr[int(exp)-1])
  else:
    print(diction[exp])
