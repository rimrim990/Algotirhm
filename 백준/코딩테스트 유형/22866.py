# 백준 22866. 탑 보기
from collections import deque
from math import inf

n = int(input())
arr = list(map(int, input().split()))
count = [0 for _ in range(n)]
num = [-inf for _ in range(n)]

# 왼쪽 방향으로 볼 수 있는 건물
left = deque([(arr[0], 1)])
for x in range(1, n):
  while left and left[-1][0] <= arr[x]:
    left.pop()
  if left:
    count[x] += len(left)
    num[x] = left[-1][1]
  left.append((arr[x], x+1))

# 오른쪽 방향으로 볼 수 있는 건물
right = deque([(arr[-1], n)])
for x in range(n-1, -1, -1):
  while right and right[-1][0] <= arr[x]:
    right.pop()
  if right:
    count[x] += len(right)
    if (x+1) - num[x] > right[-1][1] - (x+1):
      num[x] = right[-1][1]
  right.append((arr[x], x+1))

for x in range(n):
  res = f'{count[x]} '
  if num[x] > 0:
    res += f'{num[x]}'
  print(res)