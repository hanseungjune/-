from collections import deque
n = int(input())

# 제일 위의 카드 버리기
# 위에서 2번째 카드 버리기
# 제일 밑에 있는 카드 버리기

lst = list(map(int, input().split()))[::-1]
floor = [i for i in range(n, 1, -1)]
print(lst)
print(floor)
front= [1]
dq = deque()
# for command in lst[1:]:
