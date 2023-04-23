# 백준 16987 계란으로 계란치기
import sys
input = sys.stdin.readline

n = int(input())
# 내구도, 무게
eggs = [list(map(int, input().split())) for _ in range(n)]

def hit(cur, eggs):
  if cur >= len(eggs):
    cnt = 0
    for egg, _ in eggs:
      if egg <= 0: cnt += 1
    return cnt

  total_cnt = 0; is_hit = False
  for i in range(len(eggs)):
    if i == cur or eggs[i][0] <= 0 or eggs[cur][0] <= 0:
      continue
    # 계란치기
    is_hit = True
    eggs[cur][0] -= eggs[i][1]
    eggs[i][0] -= eggs[cur][1]
    total_cnt = max(total_cnt, hit(cur+1, eggs))
    eggs[cur][0] += eggs[i][1]
    eggs[i][0] += eggs[cur][1]

  if not is_hit:
    total_cnt = hit(cur+1, eggs)

  return total_cnt

print(hit(0, eggs))