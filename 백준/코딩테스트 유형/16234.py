# 백준 16234. 인구이동
from collections import deque

n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dy = [0,0,-1,1]
dx = [-1,1,0,0]

# 연합 구하기
def bfs(y, x, visit):
  global n, l, r
  unions = [(y, x)]
  total_sum = arr[y][x]

  dq = deque([(y,x)])
  while dq:
    cy, cx = dq.popleft()
    for i in range(4):
      ny, nx = cy + dy[i], cx + dx[i]
      if 0 <= ny < n and 0 <= nx < n:
        if visit[ny][nx]:
          continue

        delta = abs(arr[cy][cx] - arr[ny][nx])
        if l <= delta <= r:
          visit[ny][nx] = 1
          dq.append((ny, nx))
          unions.append((ny, nx))
          total_sum += arr[ny][nx]

  return unions, total_sum

def get_unions():
  visit = [[0 for _ in range(n)] for _ in range(n)]
  unions = []

  for y in range(n):
    for x in range(n):
      if visit[y][x]:
        continue
      visit[y][x] = 1
      union, total = bfs(y, x, visit)
      if len(union) == 1:
        continue
      unions.append((union, total))

  return unions

count = 0
while True:
  unions = get_unions()
  # 연합이 없음
  if not unions:
    break

  count += 1
  for union, total in unions:
    population = total // len(union)
    for y, x in union:
      arr[y][x] = population

print(count)