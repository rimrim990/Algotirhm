# 백준 17298 오큰수

import sys
input = sys.stdin.readline

n = int(input()) # 수열 A 의 크기
arr = list(map(int, input().split())) # 수열 A
stack = [arr.pop()]; res = [-1]

for a in reversed(arr):
  # a 로 인해 a 보다 작은 수들은 가려진다
  while stack and stack[-1] <= a:
    stack.pop()

  # 오큰수가 없음
  if not stack:
    res.append(-1)
  else:
    res.append(stack[-1])

  if not stack or a < stack[-1]:
    stack.append(a)

# 출력
for i in range(n-1, -1, -1):
  print(res[i], end=' ')