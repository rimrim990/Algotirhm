# 백준 2252 줄 세우기

import sys
from collections import deque
input = sys.stdin.readline

# 학생 번호, 비교 횟수
n, m = map(int, input().split())
edges = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]

# 입력
for _ in range(m):
  a, b = map(int, input().split())
  # a -> b
  edges[a].append(b)
  indegree[b] += 1

q = deque([])
# 차수가 0인 노드 삽입
for i in range(1, n+1):
  # 의존성 없음
  if indegree[i] == 0:
    q.append(i)

res = []
# 순서대로 의존성 제거
while q:
  cur = q.popleft()
  res.append(cur)
  # 다음 노드
  for nxt in edges[cur]:
    indegree[nxt] -= 1
    # nxt 이전의 모든 노드 줄세우기 완료
    if indegree[nxt] == 0:
      q.append(nxt)

# 정답 출력
for i in res: print(i, end=" ")