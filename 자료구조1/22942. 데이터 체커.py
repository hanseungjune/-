# import sys
# input = sys.stdin.readline
# n = int(input())
# stack = []
# for _ in range(n):
#   x, r = map(int, input().split())
#   stack.append((x, r))

# for i in range(len(stack)):
#   xi, ri = stack[i]
#   for j in range(len(stack)):
#     if i == j:
#       continue
#     xj, rj = stack[j]
#     dist = abs(xi - xj)
#     rdiff = abs(ri - rj)
#     rsum = abs(ri + rj)

#     if ri+rj == dist:
#       flag = 1
#       break
#     elif dist == ri-rj or dist == rj-ri:
#       flag = 1
#       break
#     elif rdiff < dist < rsum:
#       flag = 1
#       break
#     else:
#       pass
#   if flag == 1:
#     break

# if flag == 1:
#   print('NO')
# else:
#   print('YES')  

# ✨ 입력

import sys
input = sys.stdin.readline
N = int(input())
circle = []

# ✨ 준비
for i in range(N):
    a,b = map(int,input().split())
    circle.append((a-b,i))
    circle.append((a+b,i))
    
circle.sort()

# ✨ 비교
stack = []
for i in range(N*2):
    d, c = circle[i]
    if len(stack)==0:
        stack.append(circle[i])
    elif stack:
        if stack[-1][1] == c:
            stack.pop()
        else:
            stack.append(circle[i])
else:
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')