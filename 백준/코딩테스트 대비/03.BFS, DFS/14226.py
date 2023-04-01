# 백준 14226 이모티콘
import sys
from collections import deque
input = sys.stdin.readline

s = int(input())
q = deque([(1, 0)])
# 화면 스티커의 개수, 클립보드 스티거의 개수
visited = [[-1 for _ in range(1025)] for _ in range(1025)]
visited[1][0] = 0

while q:
  cur, clip = q.popleft()
  time = visited[cur][clip]
  # 생성 완료
  if cur == s: break
  # 화면에 있는 이모티콘 1개 삭제
  if cur > 1 and visited[cur-1][clip] < 0:
    q.append((cur-1, clip))
    visited[cur-1][clip] = time + 1
  # 클립보드에서 화면으로 복사
  if cur+clip <= 1024 and visited[cur+clip][clip] < 0:
    q.append((cur+clip, clip))
    visited[cur+clip][clip] = time + 1
  # 클립보드로 복사
  if visited[cur][cur] < 0:
    q.append((cur, cur))
    visited[cur][cur] = time + 1

print(min(filter(lambda x: x >= 0, visited[s])))