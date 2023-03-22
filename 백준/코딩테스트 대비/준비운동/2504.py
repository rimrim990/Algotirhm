# 백준 2504 괄호의 값

import sys
input = sys.stdin.readline
seq = input().rstrip()

def split(seq):
  elem = []; stack = [];

  # XY 분할
  for s in seq:
    if s in ['(', '[']:
      if stack: elem[-1] += s
      else: elem.append(s)
      stack.append(s)
      continue

    # 올바르지 않은 문자열 - ex. ')', '(]'
    elif s == ')' and (not stack or stack[-1] != '('):
      return 0
    elif s == ']' and (not stack or stack[-1] != '['):
      return 0

    stack.pop()
    elem[-1] += s

  # 올바르지 않은 문자열 - ex. '())'
  if stack: return 0

  total = 0
  for e in elem:
    if e == '()':
      total += 2 # ()
    elif e == '[]':
      total += 3 # []
    else:
      res = split(e[1:-1]) # (X) 혹은 [X]
      res = res * 2 if e[0] == '(' else res * 3 # 가중치 부여
      # 올바르지 못한 문자열
      if res == 0: return 0
      total += res

  return total

print(split(seq))