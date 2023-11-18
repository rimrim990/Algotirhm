import sys
sys.setrecursionlimit(10**6)

def solution(n, path, order):
  graph = [[] for _ in range(n)]
  for a, b in path:
    graph[a].append(b)
    graph[b].append(a)

  prior = [0 for _ in range(n)]
  for a, b in order:
    prior[b] = a

  if prior[0]:
    return False

  wait = [0 for _ in range(n)]
  visited = [False for _ in range(n)]
  visited[0] = True
  dfs(0, graph, wait, visited, prior)

  return all(visited[i] for i in range(n))

def dfs(cur, graph, wait, visited, prior):
  for nxt in graph[cur]:
    if visited[nxt]:
      continue

    if not visited[prior[nxt]]:
      wait[prior[nxt]] = nxt
      continue

    visited[nxt] = True
    dfs(nxt, graph, wait, visited, prior)

    visited[wait[nxt]] = True
    dfs(wait[nxt], graph, wait, visited, prior)