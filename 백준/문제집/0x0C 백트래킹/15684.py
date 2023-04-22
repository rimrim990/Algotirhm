# 백준 15684 사다리 조작
import sys
import math
input = sys.stdin.readline
n, m, h = map(int, input().split())

# [세로 선 번호][가로 점선의 번호]
ladder = [[i for _ in range(h+1)] for i in range(n+1)]
for _ in range(m):
  a, b = map(int, input().split())
  ladder[b][a] = b+1
  ladder[b+1][a] = b

ans = math.inf

def dfs(y, cnt, n, h, ladder):
  global ans
  # 설치 완료
  if check(n, h, ladder):
    if ans == -1: ans = cnt
    else: ans = min(ans, cnt)
    return
  # 불가능하거나 최솟값이 아님
  if cnt >= 3:
    return

  # 사다리 설치
  for i in range(y, n):
    for j in range(1, h+1):
      if ladder[i][j] != i: continue
      if ladder[i+1][j] != i+1: continue
      ladder[i][j] = i+1
      ladder[i+1][j] = i
      dfs(i, cnt+1, n, h, ladder)
      ladder[i][j] = i
      ladder[i+1][j] = i+1

# i 번째 사다리가 i 에 도달하는지 검사
def check(n, h, ladder):
  # i 번째 사다리
  for i in range(1, n+1):
    cur = i
    for j in range(1, h+1):
      cur = ladder[cur][j]
    if cur != i:
      return False
  return True

# 정답출력
dfs(1, 0, n, h, ladder)
print(ans if ans != math.inf else -1)