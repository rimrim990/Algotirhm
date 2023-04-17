# 백준 2616 소형기관차
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
cap = int(input())

# 구간합
acc = [0 for _ in range(n)]
acc[0] = sum(nums[:cap])
for i in range(1,n-cap+1):
  acc[i] += acc[i-1] - nums[i-1] + nums[i+cap-1]

# dp[기관차 번호][위치]
dp = [[0 for _ in range(n+1)] for _ in range(4)]
for i in range(1,4):
  for j in range(n-cap*i, -1, -1):
    dp[i][j] = max(dp[i][j+1], acc[j]+dp[i-1][j+cap])

print(dp[-1][0])