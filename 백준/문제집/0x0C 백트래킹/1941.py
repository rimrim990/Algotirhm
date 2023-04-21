# 백준 1941 소문난 칠공주
import sys
input = sys.stdin.readline

graph = [list(input().strip()) for _ in range(5)]
map = {}

dy = [-1,1,0,0]
dx = [0,0,-1,1]
ans = 0

# dfs + 메모이제이션
def dfs(ycnt, scnt, path):
  global ans

  if ycnt > 3:
    map[path] = (ycnt, scnt)

  elif map.get(path) == None:
    map[path] = (ycnt, scnt)
    if ycnt + scnt == 7:
      ans += 1
      return

    for p in range(25):
      pbit = 1 << p
      if pbit & path == 0: continue
      py = p // 5
      px = p % 5
      for i in range(4):
        ny = py + dy[i]
        nx = px + dx[i]
        if 0 <= ny < 5 and 0 <= nx < 5:
          nbit = 1 << (5*ny + nx)
          if nbit & path > 0: continue
          if graph[ny][nx] == 'Y':
            dfs(ycnt+1, scnt, path | nbit)
          else:
            dfs(ycnt, scnt+1, path | nbit)

# 모든 경우의 수 탐색
for i in range(5):
  for j in range(5):
    # 방문 경로
    bit = 1 << (5*i + j)
    if graph[i][j] == 'Y':
      dfs(1,0,bit)
    else:
      dfs(0,1,bit)

# 정답 출력
print(ans)