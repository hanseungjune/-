import sys
import heapq

heap = []
n = int(sys.stdin.readline())
for i in range(n):
  x = int(sys.stdin.readline())
  if x:
    heapq.heappush(heap, (-x, x))
  else:
    if len(heap) >= 1:
      print(heapq.heappop(heap)[1])
    else:
      print(0)