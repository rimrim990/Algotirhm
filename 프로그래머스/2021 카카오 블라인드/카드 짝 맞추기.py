from itertools import permutations
from collections import defaultdict, deque
from math import inf

def solution(board, r, c):
  answer = inf
  cards = set()
  pairs = defaultdict(list)

  for i in range(4):
    for j in range(4):
      if board[i][j] > 0:
        cards.add(board[i][j])
        pairs[board[i][j]].append((i, j))

  for p in permutations(list(cards), len(cards)):
    answer = min(answer, card_game(board, (r, c), pairs, p, 0))
  return answer

def card_game(board, cur, pairs, per, idx):
  if idx == len(per):
    return 0

  total = inf
  p = per[idx]

  a, b = pairs[p][0], pairs[p][1]
  a_dist = bfs(board, cur, a) + bfs(board, a, b)
  b_dist = bfs(board, cur, b) + bfs(board, b, a)

  copy = [board[i][:] for i in range(4)]
  copy[a[0]][a[1]] = 0
  copy[b[0]][b[1]] = 0

  if a_dist < b_dist:
    res = a_dist + 2 + card_game(copy, b, pairs, per, idx+1)
    total = min(res, total)

  elif a_dist == b_dist:
    res1 = a_dist + 2 + card_game(copy, b, pairs, per, idx+1)
    res2 = b_dist + 2 + card_game(copy, a, pairs, per, idx+1)
    total = min(res1, res2, total)

  else:
    res = b_dist + 2 + card_game(copy, a, pairs, per, idx+1)
    total = min(res, total)

  return total

def bfs(board, pos, tar):
  dq = deque([(pos, 0)])
  dy = [-1,1,0,0]; dx = [0,0,1,-1]
  visit = [[False for _ in range(4)] for _ in range(4)]

  while dq:
    cur, cnt = dq.popleft()
    if cur == tar:
      return cnt

    # 한 칸 이동
    for i in range(4):
      ny, nx = cur[0] + dy[i], cur[1] + dx[i]
      if in_block(ny, nx) and not visit[ny][nx]:
        visit[ny][nx] = True
        dq.append(((ny, nx), cnt+1))

    # ctrl 이동
    for i in range(4):
      ny, nx = cur[0] + dy[i], cur[1] + dx[i]
      while in_block(ny, nx) and board[ny][nx] == 0:
        if not in_block(ny + dy[i], nx + dx[i]):
          break
        ny += dy[i]; nx += dx[i]

      if in_block(ny, nx) and not visit[ny][nx]:
        visit[ny][nx] = True
        dq.append(((ny, nx), cnt+1))

def in_block(y, x):
  return 0 <= y < 4 and 0 <= x < 4