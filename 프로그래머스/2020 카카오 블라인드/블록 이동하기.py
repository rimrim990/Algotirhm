from collections import deque

dy = [0,0,1,-1]
dx = [1,-1,0,0]

def solution(b):
  n = len(b)
  board = [[1]*(n+2) for _ in range(n+2)]

  for i in range(n):
    for j in range(n):
      board[i+1][j+1] = b[i][j]

  dq = deque([])
  dq.append(((1,1), (1,2), 0))
  visited = set([((1,1), (1,2))])

  while dq:
    cur1, cur2, cnt = dq.popleft()

    # 도착
    if cur1 == (n, n) or cur2 == (n, n):
      return cnt

    # 한 칸 이동하기
    for i in range(4):
      nxt1 = (cur1[0]+dy[i], cur1[1]+dx[i])
      nxt2 = (cur2[0]+dy[i], cur2[1]+dx[i])
      if board[nxt1[0]][nxt1[1]] == 0 and board[nxt2[0]][nxt2[1]] == 0:
        if (nxt1, nxt2) not in visited:
          visited.add((nxt1, nxt2))
          dq.append((nxt1, nxt2, cnt+1))

    cands = []
    # 가로 방향
    if cur1[0] == cur2[0]:
      for d in [-1, 1]:
        if board[cur1[0]+d][cur1[1]] == 0 and board[cur2[0]+d][cur2[1]] == 0:
          cands.append((cur1, (cur1[0]+d, cur1[1])))
          cands.append((cur2, (cur2[0]+d, cur2[1])))

    # 세로 방향
    elif cur1[1] == cur2[1]:
      for d in [-1, 1]:
        if board[cur1[0]][cur1[1]+d] == 0 and board[cur2[0]][cur2[1]+d] == 0:
          cands.append((cur1, (cur1[0], cur1[1]+d)))
          cands.append((cur2, (cur2[0], cur2[1]+d)))

    for cand in cands:
      nxt1, nxt2 = sorted(cand)
      if (nxt1, nxt2) not in visited:
        visited.add((nxt1, nxt2))
        dq.append((nxt1, nxt2, cnt+1))

  return -1