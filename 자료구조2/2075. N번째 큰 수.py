import sys, heapq

n = int(sys.stdin.readline())
hq = []
for i in range(n):
  lst = list(map(int, sys.stdin.readline().split()))
  if not hq:
    for num in lst:
      heapq.heappush(hq, num)
  else:
    for num in lst:
      if hq[0] < num:
        heapq.heappush(hq, num)
        heapq.heappop(hq)
print(hq[0])