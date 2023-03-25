# 백준 3085 사탕 게임

import sys
input = sys.stdin.readline

# 행렬 크기, 행렬
def solution(n, bomb):
  res = 0
  for i in range(n):
    for j in range(n):
      res = max(res, search(True, (i,j), bomb, True, bomb[i][j], 1))
      res = max(res, search(True, (i,j), bomb, False, bomb[i][j], 1))
  return res

def search(chance, cur, bomb, row, color, cnt):
  n = len(bomb); cy, cx = cur; max_cnt = cnt
  delta = [[1,1], [-1,1]] if row else [[1,-1], [1,1]]
  # case1. 연속된 경우
  idx = cx + 1 if row else cy + 1
  if idx < n:
    val = bomb[cy][idx] if row else bomb[idx][cx]
    if val == color:
      nxt = (cy, idx) if row else (idx, cx)
      return search(chance, nxt, bomb, row, color, cnt+1)
  # case2. 교환 가능한 경우
  if chance is True:
    # 두 칸 너머와 교환
    jump = False; nn = (cy, cx+2) if row else (cy+2, cx)
    if nn[0] < n and nn[1] < n and bomb[nn[0]][nn[1]] == color:
      jump = True; max_cnt = max(max_cnt, cnt+1)
    # 대각선과 교한
    for d in delta:
      ny = cy + d[0]; nx = cx + d[1]
      if 0 <= ny < n and 0 <= nx < n:
        if bomb[ny][nx] == color:
          if cnt == 1:
            max_cnt = max(max_cnt, search(False, (ny, nx), bomb, row, color, cnt+1))
          else:
            max_cnt = max(max_cnt, cnt+1)
          if jump:
            max_cnt = max(max_cnt, search(False, nn, bomb, row, color, cnt+2))

  return max_cnt

n = int(input())
bomb = [input().rstrip() for _ in range(n)]

print(solution(n, bomb))