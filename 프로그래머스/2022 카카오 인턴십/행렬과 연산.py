from collections import deque

def solution(rc, operations):
  r = len(rc); c = len(rc[0])

  top = deque(rc[0][1:-1])
  bottom = deque(rc[-1][1:-1])
  left = deque([rc[i][0] for i in range(r)])
  right = deque([rc[i][-1] for i in range(r)])
  center = deque([deque(rc[i][1:-1]) for i in range(1, r-1)])

  for op in operations:
    if op == "ShiftRow":
      # 행 밀기
      center.appendleft(top)
      top = bottom
      bottom = center.pop()

      left.appendleft(left.pop())
      right.appendleft(right.pop())

    elif op == "Rotate":
      # 시계 방향 회전
      top.appendleft(left.popleft())
      bottom.append(right.pop())
      right.appendleft(top.pop())
      left.append(bottom.popleft())

  center.appendleft(top)
  center.append(bottom)

  return [[l] + list(c) + [r] for l,c,r in zip(left, center, right)]