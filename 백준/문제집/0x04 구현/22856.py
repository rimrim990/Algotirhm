# 백준 22856 트리 순회
import sys
input = sys.stdin.readline

# 트리 노드의 개수
n = int(input())

nodes = [[] for _ in range(n+1)]
parent = [-1 for _ in range(n+1)]
for _ in range(n):
  a, b, c = map(int, input().split())
  nodes[a] += [b,c]
  if b > 0: parent[b] = a
  if c > 0: parent[c] = a

# 유사 중위 순회의 마지막 노드 탐색
end = 1
while nodes[end][1] != -1:
  end = nodes[end][1]

# 유사 중위 순회
cur=1; cnt=0; visited = (1 << cur)
while 1:
  # 1. 왼쪽 자식 노드 방문
  if nodes[cur][0] > 0:
    bit = 1 << nodes[cur][0]
    if visited & bit == 0:
      cur = nodes[cur][0]
      visited |= bit; cnt += 1
      continue
  # 2. 오른쪽 자식 노드 방문
  if nodes[cur][1] > 0:
    bit = 1 << nodes[cur][1]
    if visited & bit == 0:
      cur = nodes[cur][1]
      visited |= bit; cnt += 1
      continue
  # 3. 유사 중위 순회의 끝
  if cur == end: break
  # 4. 부모 노드가 존재
  if parent[cur] > 0:
    cur = parent[cur]; cnt += 1

print(cnt)