# 백준 1197 최소 스패닝 트리

import sys
input = sys.stdin.readline

# 정점의 개수, 간선의 개수
v, e = map(int, input().split())
edges = []; parent = [i for i in range(v+1)]

for _ in range(e):
  # 시작, 도착, 가중치
  a, b, c = map(int, input().split())
  # 간선 리스트
  edges.append((a,b,c))

# 크루스칼 알고리즘
edges.sort(key=lambda x: x[2])

def find(a, parent):
  if parent[a] != a:
    a = find(parent[a], parent)
  return parent[a]

def union(a, b, parent):
  pa = find(a, parent)
  pb = find(b, parent)
  # 더 작은 값을 루트 노드로 설정
  if pa <= pb: parent[pb] = pa
  else: parent[pa] = pb

total_cost = 0

for a, b, cost in edges:
  pa = find(a, parent)
  pb = find(b, parent)

  # 이미 하나의 트리로 연결되어 있음
  # 사이클 생성 방지
  if pa == pb: continue
  union(a, b, parent)
  total_cost += cost

print(total_cost)