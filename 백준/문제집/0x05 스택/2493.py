# 백준 2493번 탑
import sys
input = sys.stdin.readline

n = int(input()) # 탑의 수
h = list(map(int, input().split())) # 높이
res = [0] # 결과
stack = [(h[0], 1)] # 스택 (수신기 높이, 위치)

for i in range(1, n):
  # 현재 수신기보다 더 낮은 좌측 수신기들 무시
  while stack and stack[-1][0] < h[i]:
    stack.pop()

  # 더 높은 수신기 없음
  if not stack:
    res.append(0)
  # 순차적으로 스택에 push 하므로, top 에 있는 수신기가 현재 노드와 제일 가까움
  else:
    res.append(stack[-1][1])

  stack.append((h[i], i+1))

for r in res: print(r, end=" ")