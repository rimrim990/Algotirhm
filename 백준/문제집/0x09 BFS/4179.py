# 백준 4179 불!

import sys
from collections import deque
input = sys.stdin.readline

# 세로, 가로
r, c = map(int, input().split())
maze = [list(input().rstrip()) for _ in range(r)]

q = deque([])
visited = [[-1 for _ in range(c)] for _ in range(r)]

start = []; fire = []
for i in range(r):
  for j in range(c):
    if maze[i][j] == 'J':
      start.append((i, j, False))
      # 방문 시각
      visited[i][j] = 0
    elif maze[i][j] == 'F':
      fire.append((i, j, True))

# 불이 난 위치 먼저 큐에 삽입
q += fire
q += start

dx = [-1,1,0,0]; dy=[0,0,-1,1]

while q:
  cur_y, cur_x, is_fire = q.popleft()

  # 가장자리 - 탈출 성공
  if not is_fire:
    if cur_y == r-1 or cur_y == 0 or cur_x == c-1 or cur_x == 0:
      print(visited[cur_y][cur_x] + 1)
      break

  # 이동
  for i in range(4):
    nx = cur_x + dx[i]
    ny = cur_y + dy[i]
    if 0 <= nx < c and 0 <= ny < r:
      # 벽
      if maze[ny][nx] == '#':
        continue
      # 불이 번진다
      if is_fire and maze[ny][nx] != 'F':
        maze[ny][nx] = 'F'
        q.append((ny, nx, is_fire))
        continue
      # 이동 가능하면서 아직 방문하지 않음
      if not is_fire and maze[ny][nx] == '.' and visited[ny][nx] < 0:
        visited[ny][nx] = visited[cur_y][cur_x] + 1
        q.append((ny, nx, is_fire))

else:
  print('IMPOSSIBLE')