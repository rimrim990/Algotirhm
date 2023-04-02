# 백준 17086 아기 상어 2
import sys
from collections import deque
input = sys.stdin.readline

# 세로, 가로
n, m = map(int, input().split())
graph = []; shark = []
visited = [[-1 for _ in range(m)] for _ in range(n)]

for i in range(n):
  graph.append(list(map(int, input().split())))
  for j in range(m):
    if graph[i][j] == 1:
      shark.append((i, j))
      visited[i][j] = 0

# 이동 좌표
dy = [0,0,-1,1,-1,-1,1,1]
dx = [1,-1,0,0,-1,1,-1,1]

# 각 아기 상어로부터 다른 칸 까지의 거리 계산
q = deque(shark)
while q:
  cy, cx = q.popleft()
  for i in range(8):
    ny = cy + dy[i]
    nx = cx + dx[i]
    if 0 <= ny < n and 0 <= nx < m:
      if visited[ny][nx] < 0:
        visited[ny][nx] = visited[cy][cx] + 1
        q.append((ny, nx))

max_dist = 0
for dist in visited:
  max_dist = max(max_dist, max(dist))
print(max_dist)