# BOJ 5972. 택배 배송
from math import inf
from heapq import heappop, heappush

n,m = map(int, input().split())
edges = [[] for _ in range(n+1)]

for _ in range(m):
  a,b,c = map(int, input().split())
  edges[a].append((b,c))
  edges[b].append((a,c))

dist = [inf for _ in range(n+1)]
dist[1] = 0
hq = [(0, 1)]

while hq:
  total, cur = heappop(hq)
  for nxt, cost in edges[cur]:
    if total + cost < dist[nxt]:
      dist[nxt] = total + cost
      heappush(hq, (dist[nxt], nxt))

print(dist[n])
