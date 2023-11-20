# 백준 9328. 열쇠
from collections import deque

dy = [0,0,1,-1]
dx = [1,-1,0,0]

def has_key(alpha, keys):
  key = get_key(alpha)
  return keys[key]

def is_key(alpha):
  return alpha.islower()

def is_door(alpha):
  return alpha.isupper()

def get_key(alpha):
  if is_door(alpha):
    return ord(alpha) - ord('A')

  return ord(alpha) - ord('a')

def bfs(h, w, entry, graph, keys, wait):
  dq = deque([])
  visited = [[False] * w for _ in range(h)]

  for e in entry:
    dq.append(e)
    visited[e[0]][e[1]] = True

  cnt = 0
  while dq:
    cy, cx = dq.popleft()

    for i in range(4):
      ny, nx = cy + dy[i], cx + dx[i]
      if 0 <= ny < h and 0 <= nx < w:
        if visited[ny][nx] or graph[ny][nx] == '*':
          continue

        # 통과할 수 없는 문
        if is_door(graph[ny][nx]) and not has_key(graph[ny][nx], keys):
          key = get_key(graph[ny][nx])
          wait[key].add((ny, nx))
          continue

        # 열쇠 획득
        if is_key(graph[ny][nx]):
          key = get_key(graph[ny][nx])
          keys[key] = True

          for wk in wait[key]:
            visited[wk[0]][wk[1]] = True
            dq.append(wk)

        # 문서 획득
        if graph[ny][nx] == '$':
          cnt += 1

        visited[ny][nx] = True
        dq.append((ny, nx))

  return cnt


t = int(input())
for _ in range(t):
  #높이, 너비
  h, w = map(int, input().split())
  graph = [input() for _ in range(h)]
  keys = [False] * 26

  # 보유한 열쇠
  for key in input():
    if key == '0': break
    idx = get_key(key)
    keys[idx] = True

  # 출입문 찾기
  entry = []; cnt = 0
  wait = [set() for _ in range(26)]
  for i in range(h):
    cands = [0, w-1] if 0 < i < h-1 else range(w)
    for j in cands:
      if graph[i][j] == '*':
        continue

      if is_door(graph[i][j]) and not has_key(graph[i][j], keys):
        key = get_key(graph[i][j])
        wait[key].add((i, j))
        continue

      entry.append((i, j))

      if graph[i][j] == '$':
        cnt += 1

      elif is_key(graph[i][j]):
        key = get_key(graph[i][j])
        keys[key] = True

        for wk in wait[key]:
          entry.append((i, j))

  # 문서 훔치기
  print(bfs(h, w, entry, graph, keys, wait) + cnt)