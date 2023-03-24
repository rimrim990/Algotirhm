# 백준 1806 부분합

import sys
input = sys.stdin.readline

# 수열의 길이, 부분합
n, s = map(int, input().split())
seq = list(map(int, input().split()))

min_len = n+1
end = 1; total = seq[0]

# [start, end) 의 부분합
for start in range(n):
  while total < s and end < n:
    total += seq[end]
    end += 1
  # 부분합의 길이
  if total >= s:
    min_len = min(min_len, end-start)
    total -= seq[start]
  else:
    break

print(min_len if min_len <= n else 0)