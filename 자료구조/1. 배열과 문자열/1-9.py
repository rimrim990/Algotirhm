# 1-9. 문자열 회전 - O(N)
from collections import deque

def solution(s1, s2):
  # 길이가 같지 않음
  if len(s1) != len(s2):
    return False

  # 큐
  sq = deque(s1)
  # 회전해서 같은지 판별
  for _ in range(len(s1)):
    # 1회전
    sq.append(sq.popleft())
    # 동일 여부 판단
    if ''.join(sq) == s2:
      return True

  return False