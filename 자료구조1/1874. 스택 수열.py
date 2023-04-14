n = int(input())
stack = []
answer = []
flag = 0
cur = 1

for i in range(n):
  num = int(input())
  while cur <= num:
    answer.append("+")
    stack.append(cur)
    cur += 1

  if stack[-1] == num:
    stack.pop()
    answer.append("-")
  else:
    print('NO')
    flag = 1
    break

if flag == 0:
  for j in answer:
    print(j)
