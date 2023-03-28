# 백준 1260 DFS 와 BFS
import sys
from collections import deque
input = sys.stdin.readline

# 정점의 개수, 간선의 개수, 시작 번호
n, m, v = map(int, input().split())
# 인접 리스트
graph = [[] for _ in range(n+1)]
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

# 작은 번호 먼저 방문하도록 정렬
for g in graph: g.sort()

def dfs(start, n, graph, visited):
  print(start, end=" ")
  for nxt in graph[start]:
    bit = 1 << nxt
    if bit & visited: continue
    visited |= dfs(nxt, n, graph, visited | bit)
  return visited

def bfs(start, n, graph):
  q = deque([start])
  visited = (1 << start)
  while q:
    cur = q.popleft()
    print(cur, end=" ")
    for nxt in graph[cur]:
      bit = 1 << nxt
      if bit & visited: continue
      q.append(nxt)
      visited |= bit

dfs(v, n, graph, 1<<v)
print()
bfs(v, n, graph)