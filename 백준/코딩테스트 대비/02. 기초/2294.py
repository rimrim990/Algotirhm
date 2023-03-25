# 백준 2294 동전 2

import sys
import math
input = sys.stdin.readline

n, k = map(int, input().split())
# 중복 제거
coins = set([int(input()) for _ in range(n)])
# 만드는데 필요한 코인의 개수
dp = [math.inf for _ in range(k+1)]

# 서로 다른 구성요소를 갖는 집합이므로 겹치지 않음
for coin in coins:
  # 만들 수 없음
  if coin > k: continue
  dp[coin] = 1
  for i in range(coin+1, k+1):
    dp[i] = min(dp[i-coin] + 1, dp[i])

print(dp[k] if dp[k] < math.inf else -1)