# BOJ 2668. 숫자 고르기
from collections import deque

n = int(input())
nums = [int(input()) for _ in range(n)]
cnt = [0 for i in range(n+1)]

for num in nums:
  cnt[num] += 1

dq = deque([])
for i in range(1, n+1):
  if cnt[i] == 0:
    dq.append(i)

while dq:
  cur = dq.popleft()
  pair = nums[cur-1]
  cnt[pair] -= 1

  if cnt[pair] == 0:
    dq.append(pair)

# 뽑힌 정수들의 개수
print(len(list(filter(lambda x: x>0, cnt))))

# 뽑힌 정수들
for i in range(1, n+1):
  if cnt[i] > 0:
    print(i)
