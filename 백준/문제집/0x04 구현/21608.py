# 백준 21608 상어 초등학교

import sys
input = sys.stdin.readline

# 좌석 정보
n = int(input())
seat = [[0 for _ in range(n)] for _ in range(n)]
likes = [[] for _ in range(n*n+1)]

dx = [-1,1,0,0]; dy = [0,0,-1,1]
# 인접한 좋아하는 학생의 수와 빈 좌석의 수 집계
def find(seat, like):
  n = len(seat)
  max_like = 0; cand = []
  # 좌석 탐색
  for i in range(n):
    for j in range(n):
      if seat[i][j]: continue
      like_cnt = 0; empty_cnt = 0
      # 인접 좌석 탐색
      for k in range(4):
        ny = i + dy[k]; nx = j + dx[k]
        if 0 <= ny < n and 0 <= nx < n:
          # 비어있는 좌석
          if not seat[ny][nx]:
            empty_cnt += 1
          # 좋아하는 사람 착석
          elif seat[ny][nx] in like:
            like_cnt += 1
      if like_cnt > max_like:
        max_like = like_cnt
        cand = [(empty_cnt, i, j)]
      elif like_cnt == max_like:
        cand.append((empty_cnt, i, j))

  # 1. 좋아하는 사람이 가장 많은 좌석
  # 2. 비어있는 칸이 가장 맣은 칸
  # 3. 행 번호가 가장 작은 칸
  # 4. 열 번호가 가장 작은 칸
  cand.sort(key=lambda x: (-x[0], x[1], x[2]))
  return cand[0][1:]

for _ in range(n*n):
  sid, *like = list(map(int, input().split()))
  likes[sid] += like
  y, x = find(seat, like)
  # 자리 착석
  seat[y][x] = sid

# 만족도 계산
total_score = 0
for i in range(n):
  for j in range(n):
    # 인근 자리에 앉을 좋아하는 학생의 수 집계
    score = 0; sid = seat[i][j]
    for k in range(4):
      ny = i + dy[k]; nx = j + dx[k]
      if 0 <= ny < n and 0 <= nx < n:
        # sid 가 좋아하는 학생
        if seat[ny][nx] in likes[sid]:
          score += 1
    score = pow(10, score-1) if score else 0
    total_score += score

print(total_score)