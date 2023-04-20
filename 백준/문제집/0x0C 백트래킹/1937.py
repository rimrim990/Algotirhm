# 백준 1937 욕심쟁이 판다
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n = int(input())
bamboo = [list(map(int, input().split())) for _ in range(n)]
memo = [[-2 for _ in range(n)] for _ in range(n)]

dy = [-1,1,0,0]
dx = [0,0,-1,1]

# dfs 메모이제이션
def dfs(y, x, memo):
  if memo[y][x] == -2:
    # 방문 중 표시
    memo[y][x] = -1
    res = 1
    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]
      if 0 <= ny < len(memo) and 0 <= nx < len(memo):
        if bamboo[ny][nx] > bamboo[y][x] and memo[ny][nx] != -1:
          res = max(res, dfs(ny, nx, memo)+1)
    memo[y][x] = res
  return memo[y][x]

res = 0
for i in range(n):
  for j in range(n):
    res = max(res, dfs(i, j, memo))
print(res)