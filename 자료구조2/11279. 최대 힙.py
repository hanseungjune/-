import sys
import heapq as hq

heap = []
n = int(input())
for i in range(n):
  x = int(input())
  if x:
    hq.heappush(heap, (-x, x))
  else:
    if len(heap) >= 1:
      print(hq.heappop(heap)[1])
    else:
      print(0)