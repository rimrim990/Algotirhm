# 백준 18258 큐2

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque()

for _ in range(n):
  commands = input().split()

  if commands[0] == 'push':
    q.append(int(commands[1]))

  elif commands[0] == 'pop':
    val = q.popleft() if q else -1
    print(val)

  elif commands[0] == 'size':
    print(len(q))

  elif commands[0] == 'empty':
    val = 0 if q else 1
    print(val)

  elif commands[0] == 'front':
    val = q[0] if q else -1
    print(val)

  elif commands[-1] == 'back':
    val = q[-1] if q else -1
    print(val)