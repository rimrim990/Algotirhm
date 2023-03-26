# 백준 21611 마법사 상어와 블리자드

import sys
input = sys.stdin.readline

# 격자 크기 (홀수), 블리자드 횟수
n, m = map(int, input().split())
marble = [list(map(int, input().split())) for _ in range(n)]
attack = [list(map(int, input().split())) for _ in range(m)]

'''
문제 풀이
'''
def solution(n, m, marble, attack):
  # 폭발한 구슬의 개수 집계
  exp_sum = 0
  # 구슬 위치와 id 매핑 생성
  id_map = make_id_map(n, marble)
  # 상하좌우 탐색
  delta = [(-1,0), (1,0), (0,-1), (0,1)]
  for d, s in attack:
    # 1. 블리자드 공격
    blizard(n, marble, s, d)
    # 2. 구슬 이동
    move(n, marble, id_map, delta)
    # 3. 구슬 폭발
    while True:
      exp = explode(n, marble, id_map)
      # 점수의 합 계산
      for i in range(3): exp_sum += exp[i] * (i+1)
      # 폭발 종료
      if sum(exp) == 0: break
      # 폭발로 빈 자리가 생겼으므로 구슬 이동
      move(n, marble, id_map, delta)

    # 4. 구슬 그룹 변화
    group(n, marble, id_map)

  # 정답 반환
  return exp_sum

'''
블리자드 공격
'''
def blizard(n, marble, s, d):
  # 상어 위치
  pos = (n-1)//2
  dy = [-1,1,0, 0]; dx = [0,0,-1,1]
  for i in range(1, s+1):
    ny = dy[d-1] * i + pos
    nx = dx[d-1] * i + pos
    # 구슬 파괴
    marble[ny][nx] = 0

'''
구슬 맵 생성
'''
def make_id_map(n, marble):
  # 구슬 번호를 위치로 매핑
  id_map = [-1 for _ in range(n*n)]
  # 이동 방향
  delta = [(0,-1),(1,0),(0,1),(-1,0)]; di = 0
  by = (n-1)//2; bx = (n-1)//2
  # 칸 번호
  idx = 1
  # 이동 크기
  for i in range(1, n):
    loop = 2 if i < n-1 else 3
    for j in range(loop):
      for k in range(i):
        by += delta[di][0]
        bx += delta[di][1]
        id_map[idx] = (by, bx); idx += 1
      di += 1
      di %= 4
  return id_map

'''
구슬 이동
'''
def move(n, marble, id_map, delta):
  while True:
    # 구슬의 이동 횟수
    move_cnt = 0
    # 2 번 구슬부터 이동
    for id in range(2, n*n):
      # id 구슬의 좌표
      cy, cx = id_map[id]
      if marble[cy][cx] == 0:
        continue
      # id 가 1 더 작은 칸이 비어 있을 경우
      ty, tx = id_map[id-1]
      if marble[ty][tx] == 0:
        # 구슬 이동
        move_cnt += 1
        marble[ty][tx] = marble[cy][cx]
        marble[cy][cx] = 0
    if not move_cnt: break

'''
구슬 폭발
'''
def explode(n, marble, id_map):
  # 폭발이 일어난 횟수
  explode_cnt = [0,0,0]
  # 폭발하게 될 구역의 번호
  target = []; fy, fx = id_map[1]
  target.append([(fy, fx)])
  for id in range(2, n*n):
    cy, cx = id_map[id]
    py, px = target[-1][-1]
    if marble[py][px] == 0: continue
    # 이전 구슬과 색깔이 연속되는 경우
    if marble[py][px] == marble[cy][cx]:
      target[-1].append((cy, cx))
    else:
      target.append([(cy,cx)])

  # 구슬 폭발
  for tar in target:
    # 4개 이상 연속할 경우에만 폭발
    if len(tar) >= 4:
      for ty, tx in tar:
        explode_cnt[marble[ty][tx]-1] += 1
        marble[ty][tx] = 0
  # 폭발한 구슬의 수 반환
  return explode_cnt

'''
구슬 그룹
'''
def group(n, marble, id_map):
  target = []; fy, fx = id_map[1]
  if marble[fy][fx]: target.append([(fy, fx)])
  # 그룹핑할 구슬 없음
  else: return
  # 연속하는 구슬 집계
  for id in range(2, n*n):
    cy, cx = id_map[id]
    py, px = target[-1][-1]
    if marble[cy][cx] == 0: break
    # 구슬 색깔이 연속되는 경우
    if marble[py][px] == marble[cy][cx]:
      target[-1].append((cy, cx))
    else:
      target.append([(cy,cx)])

  # 그룹핑된 새로운 구슬 맵
  new_marble = [0]
  for t in target:
    # 구슬 개수, 구슬 번호
    a = len(t); b = marble[t[0][0]][t[0][1]]
    new_marble.append(a)
    new_marble.append(b)

  # 구슬 맵 업데이트
  for i in range(1, n*n):
    cy, cx = id_map[i]
    if i < len(new_marble):
      marble[cy][cx] = new_marble[i]
    else:
      marble[cy][cx] = 0

# 정답 출력
print(solution(n, m, marble, attack))