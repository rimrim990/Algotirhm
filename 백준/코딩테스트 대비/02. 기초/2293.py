
# 백준 2293 동전 1

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [0 for _ in range(k+1)]

# 집합을 구성하는 원소가 다르므로 중복이 없다
for coin in coins:
  if coin > k: continue
  dp[coin] += 1
  # coin 을 포함한 모든 경우의 수 계산
  for i in range(coin+1, k+1):
    dp[i] += dp[i-coin]