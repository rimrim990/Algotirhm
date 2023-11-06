# 백준 20437. 문자열 게임 2
from math import inf
from collections import deque

t = int(input())

for _ in range(t):
  w = input()
  k = int(input())
  pos = [deque([]) for _ in range(26)]

  min_len = inf; max_len = 0
  for i in range(len(w)):
    idx = ord(w[i]) - ord('a')
    pos[idx].append(i)

    if len(pos[idx]) == k:
      length = pos[idx][-1] - pos[idx][0] + 1
      min_len = min(min_len, length)
      max_len= max(max_len, length)
      pos[idx].popleft()

  if min_len == inf or max_len == 0:
    print(-1)
  else:
    print(min_len, max_len)