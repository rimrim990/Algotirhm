# 백준 17070 파이프 옮기기 1

import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# [파이프 상태][y좌표][x좌표]
dp = [[[-1 for _ in range(n)] for _ in range(n)] for _ in range(3)]

# 깊이 우선 탐색
def search(state, pos, arr):
  # (N,N) 도착
  if pos == (n-1, n-1):
    dp[state][pos[0]][pos[1]] = 1

  # 아직 방문하지 않은 노드
  elif dp[state][pos[0]][pos[1]] < 0:
    cnt = 0
    # 가로 파이프 이동
    if state == 0:
      if check_x(pos, arr):
        cnt += search(state, (pos[0], pos[1]+1), arr)
      if check_xy(pos, arr):
        cnt += search(2, (pos[0]+1, pos[1]+1), arr)

    # 세로 파이프 이동
    elif state == 1:
      if check_y(pos, arr):
        cnt += search(state, (pos[0]+1, pos[1]), arr)
      if check_xy(pos, arr):
        cnt += search(2, (pos[0]+1, pos[1]+1), arr)

    # 대각선 파이프 이동
    elif state == 2:
      if check_x(pos, arr):
        cnt += search(0, (pos[0], pos[1]+1), arr)
      if check_y(pos, arr):
        cnt += search(1, (pos[0]+1, pos[1]), arr)
      if check_xy(pos, arr):
        cnt += search(2, (pos[0]+1, pos[1]+1), arr)

    dp[state][pos[0]][pos[1]] = cnt

  return dp[state][pos[0]][pos[1]]

# 가로 방향으로 이동 가능한지 확인
def check_x(cur, arr):
  cy, cx = cur
  if cx+1 < n and arr[cy][cx+1] == 0:
    return True
  else: return False

# 세로 방향으로 이동 가능한지 확인
def check_y(cur, arr):
  cy, cx = cur
  if cy+1 < n and arr[cy+1][cx] == 0:
    return True
  else: return False

# 대각선 방향으로 이동 가능한지 확인
def check_xy(cur, arr):
  cy, cx = cur
  if cy+1 < n and cx+1 < n:
    if arr[cy+1][cx] == 0 and arr[cy][cx+1] == 0 and arr[cy+1][cx+1] == 0:
      return True
  return False

# 초기 파이프 상태, 초기 위치
state = 0; pos = (0,1)
print(search(state, pos, arr))