from collections import deque

import sys
input = sys.stdin.readline
arr = input().strip()
stack = deque()
value = 1
answer = 0

for i in range(len(arr)):
  if arr[i] == '(':
    stack.append(arr[i])
    value *= 2
  elif arr[i] == '[':
    stack.append(arr[i])
    value *= 3
  elif arr[i] == ')':
    if len(stack) == 0 or stack[-1] == '[':
      print(0)
      break
    else:
      # 순회하는 값의 직전 인덱스 짝만 맞을 때만, 더해주고 나머지는 정리
      if arr[i-1] == '(':
        answer += value
      # 정리 로직
      stack.pop()
      value //= 2
  elif arr[i] == ']':
    if len(stack) == 0 or stack[-1] == '(':
      print(0)
      break
    else:
      # 순회하는 값의 직전 인덱스 짝만 맞을 때만, 더해주고 나머지는 정리
      if arr[i-1] == '[':
        answer += value
      # 정리 로직
      stack.pop()
      value //= 3

else:
  if stack:
    print(0)
  else:
    print(answer)