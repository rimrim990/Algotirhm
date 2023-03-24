# 백준 16916 부분 문자열

import sys
input = sys.stdin.readline
s = input().rstrip() # 비교 대상
p = input().rstrip() # 패턴

# KMP 테이블
table = [0 for _ in range(len(p))]
i = 0
for j in range(1, len(p)):
  while i > 0 and p[i] != p[j]:
    i = table[i-1]

  if p[i] == p[j]:
    i += 1
    table[j] = i

# KMP
i = 0
for j in range(len(s)):
  while i > 0 and p[i] != s[j]:
    i = table[i-1]

  if p[i] == s[j]:
    i += 1
    if i == len(p):
      print(1)
      break

else:
  print(0)
