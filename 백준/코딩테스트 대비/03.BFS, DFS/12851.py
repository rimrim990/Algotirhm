# 백준 12581 숨바꼭질 2
import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
visited = [-1 for _ in range(100001)]
cnt = 0

q = deque([(n)]); visited[n] = 0
while q:
  cur = q.popleft()
  if cur == k:
    cnt += 1; continue
  for nxt in [2*cur, cur+1, cur-1]:
    if 0 <= nxt <= 100000:
      # 아직 방문하지 않았거나, 최단 거리로 방문할 수 있는 다른 경우의 수
      if visited[nxt] == -1 or visited[nxt] == visited[cur]+1:
        visited[nxt] = visited[cur] + 1
        q.append((nxt))

# 정답 출력
print(visited[k])
print(cnt)