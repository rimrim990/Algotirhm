# 백주 15989 1,2,3 더하기 4
import sys
input = sys.stdin.readline

dp = [0 for _ in range(10001)]
nums = [1,2,3]
for num in nums:
  dp[num] += 1
  for i in range(num+1, 10001):
    dp[i] += dp[i-num]

t = int(input())
for _ in range(t):
  n = int(input())
  print(dp[n])