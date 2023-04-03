# 백준 16930 달리기
import sys
from collections import deque
input = sys.stdin.readline

# 세로, 가로, 최대 이동 크기
n, m, k = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]
y1, x1, y2, x2 = map(int, input().split())

visited = [[-1 for _ in range(m+1)] for _ in range(n+1)]; visited[y1][x1] = 0
q = deque([(y1, x1)])

dy = [-1,1,0,0]; dx = [0,0,-1,1]

while q:
  cy, cx = q.popleft()
  if cy == y2 and cx == x2:
    break
  for i in range(4):
    for j in range(1, k+1):
      ny = cy + dy[i] * j
      nx = cx + dx[i] * j
      # 경계 초과 - 탐색 중지
      if not (0 < ny <= n) or not (0 < nx <=m): break
      # 벽에 가로막힘 - 탐색 중지
      if graph[ny-1][nx-1] == '#': break
      if visited[ny][nx] < 0:
          visited[ny][nx] = visited[cy][cx] + 1
          q.append((ny, nx))
      # 중복 탐색 제거
      elif visited[ny][nx] <= visited[cy][cx]: break

print(visited[y2][x2])