# 백준 10422 괄호
import sys
input = sys.stdin.readline

# [문자열의 길이]
dp = [0 for _ in range(5001)]
dp[0] = 1

NUM = 1000000007

for i in range(2, 5001, 2):
  # (S) 를 만들 수 있는 경우의 수
  dp[i] += dp[i-2]
  # ST 를 만들 수 있는 경우의 수
  for j in range(2, i, 2):
    dp[i] += (dp[j-2] * dp[i-j]) % NUM
  dp[i] %= NUM

t = int(input())
for _ in range(t):
  l = int(input())
  print(dp[l])