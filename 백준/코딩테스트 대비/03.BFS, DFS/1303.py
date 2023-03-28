# 백준 1303 전생
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(m)]

dy = [-1,1,0,0]; dx = [0,0,-1,1]

def bfs(cur, graph, size, color):
  m, n = size; cnt = 0
  graph[cur[0]][cur[1]] = 0
  q = deque([cur])
  while q:
    cy, cx = q.popleft(); cnt += 1
    for i in range(4):
      ny = cy + dy[i]; nx = cx + dx[i]
      if 0 <= ny < m and 0 <= nx < n:
        if graph[ny][nx] == color:
          graph[ny][nx] = 0
          q.append((ny, nx))

  return cnt * cnt

w_power = 0; b_power = 0; size = (m,n)
for i in range(m):
  for j in range(n):
    cur = (i, j)
    if graph[i][j] == 'W':
      w_power += bfs(cur, graph, size, 'W')
    elif graph[i][j] == 'B':
      b_power += bfs(cur, graph, size, 'B')

print(w_power, b_power)