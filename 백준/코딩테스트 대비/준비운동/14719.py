# 백준 14719 빗물
import sys
input = sys.stdin.readline

# 세로, 가로
h, w = map(int, input().split())
# 블록 높이
p = list(map(int, input().split()))
# 빗물이 고인 구간
rains = []

# start 에 대응되는 end 탐색
def search(start):
  idx = start; val = 0
  for end in range(start+1, w):
    if p[end] >= p[start]:
      return end
    if p[end] >= val:
      idx = end; val = p[end]
  return idx

i = 0
# i - 시작 지점의 기둥 위치
while i < w-1:
  # 빗물이 고일 수 있음
  if p[i] > 0 and p[i] >= p[i+1]:
    j = search(i)
    if i != j:
      rains.append((i, j))
      i = j
      continue
  # 빗물이 고일 수 없으므로 다음 영역 탐색
  i += 1

# 고인 빗물의 영역 계산
total = 0
for s, e in rains:
  # 빗물의 최대 높이
  depth = min(p[s], p[e])
  for i in range(s+1, e):
    total += depth - p[i]

# 출력
print(total)