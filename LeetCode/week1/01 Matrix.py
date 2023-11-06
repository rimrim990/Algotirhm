from collections import deque

class Solution:
  dy = [0, 0, -1, 1]
  dx = [1, -1, 0, 0]

  def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
    m, n = len(mat), len(mat[0])
    return self.bfs(m, n, mat)

  def bfs(self, m: int, n: int, mat: List[List[int]]) -> List[List[int]]:
    dq = deque([])
    result = [[-1 for _ in range(n)] for _ in range(m)]

    for y in range(m):
      for x in range(n):
        if mat[y][x] == 0:
          dq.append((y, x))
          result[y][x] = 0

    while dq:
      cy, cx = dq.popleft()
      for i in range(4):
        ny, nx = cy + self.dy[i], cx + self.dx[i]
        if 0 <= ny < m and 0 <= nx < n:
          # pass already visited node
          if result[ny][nx] >= 0:
            continue

          dq.append((ny, nx))
          result[ny][nx] = result[cy][cx] + 1

    return result