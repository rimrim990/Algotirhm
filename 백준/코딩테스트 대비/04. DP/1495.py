# 백준 1495 기타리스트
import sys
input = sys.stdin.readline

n, s, m = map(int, input().split())
v = list(map(int, input().split()))

dp = [[False for _ in range(1001)] for _ in range(n+1)]
dp[0][s] = True

for i in range(1, n+1):
  for j in range(m+1):
    if not dp[i-1][j]: continue
    # volumne up
    if 0 <= j + v[i-1] <= m:
      dp[i][j + v[i-1]] = True
    # volumn down
    if 0 <= j - v[i-1] <= m:
      dp[i][j - v[i-1]] = True

for i in range(m, -1, -1):
  if dp[n][i]: print(i); break
else: print(-1)