# BOJ 1863. 스카이라인 쉬운거

n = int(input())
cnt = 0
stack = []

for _ in range(n):
  x, y = map(int, input().split())

  while stack and y < stack[-1]:
    stack.pop()

  if y == 0:
    continue

  if not stack or stack[-1] < y:
    cnt += 1
    stack.append(y)

print(cnt)
