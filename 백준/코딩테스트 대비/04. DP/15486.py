# 백준 15486 퇴사 2
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [0 for _ in range(n+2)]

for i in range(1, n+1):
  # 아무것도 하지 않기
  dp[i] = max(dp[i-1], dp[i])
  # 오늘 상담 받기
  end = i + arr[i-1][0]
  if end <= n+1:
    dp[end] = max(dp[end], dp[i] + arr[i-1][1])

print(max(dp[n], dp[n+1]))