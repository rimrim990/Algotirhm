# 백준 5557 1학년
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

dp = [[0 for _ in range(21)] for _ in range(n-1)]
dp[0][nums[0]] = 1

# 위치
for i in range(1, n-1):
  # 값 j 를 만들 수 있는 경우의 수
  for j in range(21):
    if dp[i-1][j] > 0:
      for nxt in (j+nums[i], j-nums[i]):
        # 값의 범위를 초과하지 않음
        if 0 <= nxt <= 20:
          dp[i][nxt] += dp[i-1][j]

print(dp[n-2][nums[-1]])