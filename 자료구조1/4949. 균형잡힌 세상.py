while True:
  try: 
    str_input = input()
    if str_input == '.':
      break
    stack = []
    for i in range(len(str_input)):
      if str_input[i] not in '()[]':
        continue
      if str_input[i] == '(':
        stack.append(str_input[i])
      elif str_input[i] == '[':
        stack.append(str_input[i])
      elif str_input[i] == ')':
        if not stack or stack[-1] != '(':
          print('no')
          break
        stack.pop()
      else:
        if not stack or stack[-1] != '[':
          print('no')
          break
        stack.pop()
    else:
      if not stack:
        print('yes')
      else:
        print('no')
  except Exception as e:
    print(e)
    break