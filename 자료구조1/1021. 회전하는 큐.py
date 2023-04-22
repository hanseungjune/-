import sys, math
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
queue = deque(i for i in range(1, n+1))
circle = list(map(int, input().split()))
cnt = 0

for c in circle:
    while True:
        if queue[0] == c:
            queue.popleft()
            break
        else:
            if queue.index(c) < len(queue)/2:
                while queue[0] != c:
                    queue.append(queue.popleft())
                    cnt += 1
            else:
                while queue[0] != c:
                    queue.appendleft(queue.pop())
                    cnt += 1
print(cnt)