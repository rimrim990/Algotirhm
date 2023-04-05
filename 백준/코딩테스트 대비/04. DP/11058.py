# 백준 11058 크리보드
import sys
input = sys.stdin.readline

n = int(input())
dp = [i for i in range(n+1)]

for i in range(1, n+1):
  for j in range(i+3, n+1):
    dp[j] = max(dp[j], dp[i] * (j-i-1))

print(dp[n])