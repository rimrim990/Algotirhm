# 백준 12869 뮤탈리스크
import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
hp = list(map(int, input().split())) + [0] * 3
hp.sort(reverse=True)

attack = [9,3,1]
dp = [[[61 for _ in range(hp[2]+1)] for _ in range(hp[1]+1)] for _ in range(hp[0]+1)]
dp[hp[0]][hp[1]][hp[2]] = 0

for i in range(hp[0], 0, -1):
  for j in range(hp[1], -1, -1):
    for k in range(hp[2], -1, -1):
      # 공격 대상
      tar = list(filter(lambda x: x>0, [i,j,k]))
      # 모든 가능한 공격의 경우의 수
      for t in permutations(tar, len(tar)):
        t = list(t)
        for l in range(len(t)):
          t[l] = max(0, t[l]-attack[l])
        t = sorted(t, reverse=True) + [0] * 3
        dp[t[0]][t[1]][t[2]] = min(dp[t[0]][t[1]][t[2]], dp[i][j][k]+1)

print(dp[0][0][0])