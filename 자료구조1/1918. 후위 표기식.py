import sys
from collections import deque

input = sys.stdin.readline

stack = deque()
lst = deque(input().strip())
res = ''

# 우선순위 비교하려고
priority = {'+': 1, '-': 1, '*': 2, '/': 2}

for l in lst:
    if l.isalpha():
        res += l
    elif l == '(':
        stack.append(l)
    elif l == ')':
        while stack and stack[-1] != '(':
            res += stack.pop()
        # '(' 이거 마지막에 빼려고 하는 거
        stack.pop()
    else:
        # 우선순위가 크면 res에 바로 더하는게 맞음, 우선순위가 같거나 낮으면 그냥 스택으로 push
        while stack and stack[-1] != '(' and priority[stack[-1]] >= priority[l]:
            res += stack.pop()
        stack.append(l)

while stack:
    res += stack.pop()

print(res)