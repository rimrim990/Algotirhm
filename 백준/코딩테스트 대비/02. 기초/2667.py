# 백준 2667 단지번호붙이기

import sys
from collections import deque
input = sys.stdin.readline

# 정사각형 한변의 크기
n = int(input())
# 아파트 단지
apart = [list(map(int, input().rstrip())) for _ in range(n)]

def solution(n, apart):
  # 아파트 단지에 속한 아파트의 수 집계
  apart_cnt = []
  # 인접한 아파트 좌표
  dy = [-1,1,0,0]; dx = [0,0,1,-1]

  for i in range(n):
    for j in range(n):
      if apart[i][j] == 1:
        apart_cnt.append(bfs((i, j), (dy, dx), apart))

  # 오름차순 정렬
  apart_cnt.sort()
  print(len(apart_cnt))
  for cnt in apart_cnt:
    print(cnt)

# 현재 위치, 이동 좌표, 아파트 정보
def bfs(cur, delta, apart):
  y, x = cur; dy, dx = delta
  # 현재 단지에 속한 아파트의 수
  cnt = 0; n = len(apart); apart[y][x] = 0
  q = deque([(y, x)])

  while q:
    cy, cx = q.popleft()
    cnt += 1
    # 이웃 아파트 탐색
    for i in range(4):
      ny = cy + dy[i]; nx = cx + dx[i]
      if 0 <= ny < n and 0 <= nx < n:
        # 아파트가 존재하는 경우
        if apart[ny][nx] == 1:
          apart[ny][nx] = 0
          q.append((ny, nx))

  return cnt

# 정답 출력
solution(n, apart)