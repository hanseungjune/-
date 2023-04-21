n = int(input())

cnt = 0
for _ in range(n):
  lst = list(input())
  stack = []

  for l in lst:
    if len(stack) == 0:
      stack.append(l)
    else:
      if l == "A":           
        if stack[-1] == "B":
            stack.append(l)
        elif stack[-1] == "A":
            stack.pop()
      elif l == "B":
        if stack[-1] == "A":
            stack.append(l)
        elif stack[-1] == "B":
            stack.pop()
  if len(stack) == 0:
    cnt += 1

print(cnt)