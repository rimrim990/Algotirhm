# 백준 3973 Time To Live
import sys
import math
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def dfs(cur, graph, visited):
  for nxt in graph[cur]:
    if visited[nxt] != -1:
      continue
    visited[nxt] = visited[cur]+1
    dfs(nxt, graph, visited)

c = int(input())
for _ in range(c):
  n = int(input())
  graph = [[] for _ in range(n)]
  for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

  if n == 1:
    print(0)

  else:
    dist = [-1 for _ in range(n)]
    dist[0] = 0
    dfs(0, graph, dist)

    start = dist.index(max(dist))
    dist = [-1 for _ in range(n)]
    dist[start] = 0
    dfs(start, graph, dist)

    ttl = max(dist)
    print(math.ceil(ttl/2))