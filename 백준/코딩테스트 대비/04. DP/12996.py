# 백준 12996 Acka
import sys
from itertools import combinations
input = sys.stdin.readline

s, a, b, c = map(int, input().split())

# [남은 앨범의 수][남은 a][남은 b][남은 c]
memo = [[[[-1 for _ in range(c+1)] for _ in range(b+1)] for _ in range(a+1)] for _ in range(s)]

# dfs + 메모이제이션
def dfs(a, b, c, cnt):
  global s
  if cnt == s:
    if sum([a, b, c]) == 0:
      return 1
    else: return 0

  if sum([a, b, c]) == 0:
    return 0

  if memo[cnt][a][b][c] == -1:
    # 남아있는 가수 필터링
    ava = []
    for idx, val in enumerate([a,b,c]):
      if val > 0: ava.append(idx)
    total = 0
    # 가능한 경우의 수
    for i in range(len(ava)):
      for cand in combinations(ava, i+1):
        new_val = [a, b, c]
        for j in range(len(cand)):
          new_val[cand[j]] -= 1
        total += dfs(new_val[0], new_val[1], new_val[2], cnt+1) % 1000000007
    memo[cnt][a][b][c] = total % 1000000007

  return memo[cnt][a][b][c]

print(dfs(a, b, c, 0))