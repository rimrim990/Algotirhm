# 백준 1700 멀티탭 스케줄링

from collections import defaultdict, deque
import sys
input = sys.stdin.readline

# 멀티탭 구멍의 수, 전기 용품의 총 사용횟수
n, k = map(int, input().split())
# 전기용품 사용 순서
orders = list(map(int, input().split()))

# 전기용품의 사용 순서 맵
use_cnt = defaultdict(deque)
for i in range(k):
  # "전기용품 이름": "사용 순서" 큐
  use_cnt[orders[i]].append(i)

cnt = 0; plugs = []

for order in orders:
  # case1. 이미 꽂혀있음
  if order in plugs:
    use_cnt[order].popleft()
    continue

  # case2. 플러그 자리 남음
  if n > 0:
    n -= 1
    plugs.append(order)
    use_cnt[order].popleft()
    continue

  # case3. 자리 없음
  target = -1; target_use = -1
  for p in plugs:
    # 사용되지 않음
    if not use_cnt[p]: target = p; break
    # 가장 나중에 사용됨
    if use_cnt[p][0] > target_use:
      target = p; target_use = use_cnt[p][0]
  # 가장 나중에 사용될 제품과 교체
  cnt += 1
  plugs.remove(target); plugs.append(order)
  use_cnt[order].popleft()

print(cnt)