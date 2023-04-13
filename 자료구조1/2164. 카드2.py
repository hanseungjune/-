from collections import deque
n = int(input())

cards = deque(i for i in range(1, n+1))

bool = 0

while len(cards) > 1:
  if bool == 0:
    cards.popleft()
    bool += 1
  else:
    a = cards.popleft()
    cards.append(a)
    bool += 1
  bool %= 2

print(cards[0])
