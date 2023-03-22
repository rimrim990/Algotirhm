# 백준 1916 최소비용 구하기

import sys
import math
from heapq import heappop, heappush
input = sys.stdin.readline

n = int(input()) # 도시 개수
m = int(input()) # 버스 개수
bus = [[] for _ in range(n+1)] # 인접 리스트

# 입력
for _ in range(m):
  start, end, cost = map(int, input().split())
  bus[start].append((end, cost))

a, b = map(int, input().split()) # 출발, 도착

# 다익스트라
def dijkstra(x, y, n):
  # x 에서 다른 노드까지의 이동 비용
  dist = [math.inf for _ in range(n+1)]
  dist[x] = 0
  # 최소힙 (이동 비용, 노드 번호)
  hq = [(dist[x], x)]

  while len(hq):
    cost, cur = heappop(hq)
    # 최단 거리가 아님
    if cost != dist[cur]: continue
    # 이웃 노드 탐색
    for nxt, nxt_cost in bus[cur]:
      # 최단 거리 갱신
      if cost + nxt_cost < dist[nxt]:
        dist[nxt] = cost + nxt_cost
        heappush(hq, (dist[nxt], nxt))

  return dist[y]

print(dijkstra(a, b, n))