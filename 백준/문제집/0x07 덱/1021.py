# 백준 1021 회전하는 큐

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
deq = deque([i for i in range(1, n+1)])
total_cnt = 0

for a in arr:
  idx = deq.index(a)

  # 왼쪽에서 접근하는게 더 빠름
  if idx <= len(deq) // 2:
    while deq[0] != a:
      deq.append(deq.popleft())
      total_cnt += 1

  # 오른쪽에서 접근하는 게 더 빠름
  else:
    while deq[0] != a:
      deq.appendleft(deq.pop())
      total_cnt += 1

  if deq[0] == a: deq.popleft()

print(total_cnt)