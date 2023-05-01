# 백준 1504 특정한 최단 경로
import sys
import math
from heapq import heappop, heappush
input = sys.stdin.readline

n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(e):
  a, b, c = map(int, input().split())
  graph[a].append((b,c))
  graph[b].append((a,c))

v1, v2 = map(int, input().split())

def dijkstra(start):
  dist = [math.inf for _ in range(n+1)]
  dist[start] = 0
  hq = [(0, start)]
  while hq:
    ctime, cur = heappop(hq)
    if ctime > dist[cur]: continue
    for nxt, ntime in graph[cur]:
      if ctime + ntime < dist[nxt]:
        dist[nxt] = ctime + ntime
        heappush(hq, (dist[nxt], nxt))
  return dist

sdist = dijkstra(1)
v1dist = dijkstra(v1)
v2dist = dijkstra(v2)

# 1 -> v1 -> v2 -> n
d1 = sdist[v1] + v1dist[v2] + v2dist[n]
# 1 -> v2 -> v1 -> n
d2 = sdist[v2] + v2dist[v1] + v1dist[n]
res = min(d1, d2)
print(res if res < math.inf else -1)