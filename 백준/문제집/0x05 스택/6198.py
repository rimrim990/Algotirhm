# 백준 6198 옥상 정원 꾸미기

import sys
input = sys.stdin.readline

n = int(input()) # 빌딩의 개수
h = [int(input()) for _ in range(n)] # 높이

total = 0 # 빌딩 수의 합
stack = [(h.pop(), 0)] # 높이, 볼 수 있는 빌딩 수

for cur in reversed(h):
  visible = 0 # 현재 빌딩에서 볼 수 있는 옥상의 수

  # 누적
  while stack and stack[-1][0] < cur:
    visible += 1
    visible += stack.pop()[1]

  total += visible

  # 시야에 들어올 수 있는 빌딩 스택
  if not stack or cur <= stack[-1][0]:
    stack.append((cur, visible))

print(total)
