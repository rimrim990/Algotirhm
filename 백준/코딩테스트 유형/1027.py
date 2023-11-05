# 백준 1027. 고층 건물
from collections import deque

n = int(input())
arr = list(map(int, input().split()))
count = [0 for _ in range(n)]

# 왼쪽 방향을 볼 때 보이는 건물
for x in range(1, n):
  left = deque([])
  for lx in range(x-1, -1, -1):
    cur = (arr[lx]-arr[x]) / (x-lx)
    if left and left[-1] >= cur:
      continue
    left.append(cur)
  count[x] += len(left)

# 오른쪽 방향을 볼 때 보이는 건물
for x in range(n-1):
  right = deque([])
  for rx in range(x+1, n):
    cur = (arr[rx]-arr[x]) / (rx-x)
    if right and right[-1] >= cur:
      continue
    right.append(cur)
  count[x] += len(right)

print(max(count))