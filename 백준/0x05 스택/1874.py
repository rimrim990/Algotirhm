# 백준 1874 스택 수열

import sys
input = sys.stdin.readline

# 입력
n = int(input())
seq = [int(input()) for _ in range(n)]

# push 카운트
cnt = 0
# 스택, 연산 결과
stack = []; res = []

for s in seq:
  while cnt < s:
    cnt += 1
    stack.append(cnt)
    res.append('+')

  if stack[-1] == s:
    stack.pop()
    res.append('-')
    continue

  # 만들 수 없음
  if cnt > s:
    print('NO')
    break

else:
  for r in res: print(r)