# 백준 11049 행렬 곱셈 순서
import sys
import math
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
# [i, j] 행렬 계산에 필요한 곱셈 연산의 최솟값
dp = [[math.inf for _ in range(n)] for _ in range(n)]

# 메모이제이션 - 중복 연산 제거
def dfs(i, j):
  if i == j:
    return 0

  elif dp[i][j] == math.inf:
    # 곱셈 연산 횟수의 최솟값
    cnt = math.inf
    for k in range(i, j):
      res = dfs(i, k) + dfs(k+1, j)
      res += matrix[i][0] * matrix[k][1] * matrix[j][1]
      cnt = min(cnt, res)
    dp[i][j] = cnt

  return dp[i][j]

print(dfs(0, n-1))