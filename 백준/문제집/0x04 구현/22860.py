# 백준 22860 폴더 정리
import sys
from collections import deque
input = sys.stdin.readline

# 폴더의 총 개수, 파일의 총 개수
n, m = map(int, input().split())
dir = {}

for _ in range(n+m):
  a, b, c = input().split()
  if dir.get(a) is None: dir[a] = [(b, c)]
  else: dir[a].append((b,c))
  if c and dir.get(b) is None: dir[b] = []

def search(query, dir):
  q = deque([(query)]); cnt = 0; files = set()
  while q:
    cur = q.popleft()
    for name, is_dir in dir[cur]:
      if is_dir == '1':
        q.append(name)
      else:
        files.add(name); cnt += 1
  return len(files), cnt

q = int(input())
for _ in range(q):
  query = input().rstrip().split("/")
  set_cnt, cnt = search(query[-1], dir)
  print(set_cnt, cnt)