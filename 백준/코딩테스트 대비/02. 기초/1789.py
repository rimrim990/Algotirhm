# 백준 1789 수들의 합

import sys
input = sys.stdin.readline

# 수들의 합
s = int(input())

# n(n+1) <= 2s
res = -1
for n in range(2*s):
  if n*(n+1) <= 2*s:
    res = n
  else:
    break

print(res)