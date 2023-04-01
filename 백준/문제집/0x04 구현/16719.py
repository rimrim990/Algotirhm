# 백준 16719 ZOAC
import sys
input = sys.stdin.readline

s = input().rstrip()
stack = [(0, len(s))]; res = []

while stack:
  start, end = stack.pop()
  min_idx = -1; min_val = ord('z')+1
  for i in range(start, end):
    if ord(s[i]) < min_val:
      min_val = ord(s[i])
      min_idx = i
  if min_idx >= 0:
    res.append(min_idx)
    stack.append((start, min_idx))
    stack.append((min_idx+1, end))

# 정답출력
ss = ['' for _ in range(len(s))]
for idx in res:
  ss[idx] = s[idx]
  print(''.join(ss))