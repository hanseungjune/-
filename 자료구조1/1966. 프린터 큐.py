from collections import deque

n = int(input())

for i in range(n):
    # 문서 개수, 목표 문서 인덱스
    cnt, target = map(int, input().split())
    # 문서 중요도 리스트
    docs = deque(map(int, input().split()))
    # 문서 인덱스 리스트
    idxs = deque(range(cnt))

    # 순서
    sequence = 0
    while True:
      if docs[0] == max(docs):
        sequence += 1
        if idxs[0] == target:
          print(sequence)
          break
        else:
          docs.popleft()
          idxs.popleft()
      else:
        docs.append(docs.popleft())
        idxs.append(idxs.popleft())

    # 9, 1, 1, 1, 1, 1
    # 2, 3, 4, 5, 0, 1