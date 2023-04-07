# 백준 12865 평범한 배낭
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1, 0] for _ in range(k+1)]
dp[0][0] = 0

# 배낭의 무게
for i in range(k+1):
  # j 번째 물건을 포함했을 때의 가치 계산
  for j in range(n):
    w, v = wv[j]; bit = 1 << j
    # 만들 수 없는 조합
    if dp[i][0] < 0 or i+w > k: continue
    # 이미 사용완료
    if bit & dp[i][1] > 0: continue
    if dp[i][0]+v > dp[i+w][0]:
      dp[i+w][0] = dp[i][0]+v
      dp[i+w][1] = dp[i][1] | bit

# k 만큼 채우지 못하는 경우 포함
# 아무것도 채우지 못하는 경우 포함
print(max(map(lambda x: x[0], dp)))