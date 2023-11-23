N = 201

def solution(board):
  n = len(board)
  answer = 0

  while True:
    points = [[] for _ in range(N)]
    for y in range(n):
      for x in range(n):
        points[board[y][x]].append((y, x))

    cnt = 0
    for i in range(1, N):
      if points[i] and check(n, board, points[i]):
        cnt += 1
        answer += 1
        clear(board, points[i])

    if cnt == 0:
      break

  return answer

def clear(board, point):
  for py, px in point:
    board[py][px] = 0

def check(n, board, point):
  max_x, min_x = 0, n
  max_y, min_y = 0, n

  for py, px in point:
    max_x = max(max_x, px)
    min_x = min(min_x, px)
    max_y = max(max_y, py)
    min_y = min(min_y, py)

  p = point[0]
  num = board[p[0]][p[1]]

  for x in range(min_x, max_x+1):
    flag = False
    lower_y = 0

    if board[min_y][x] == num:
      flag = True
      lower_y = min_y

    for y in range(lower_y, max_y+1):
      # 다른 블록이 가로막고 있음
      if board[y][x] not in [num, 0]:
        return False

      # 빈 공간을 채울 수 없음
      if flag and board[y][x] == 0:
        return False

      if board[y][x] == num:
        flag = True

  return True