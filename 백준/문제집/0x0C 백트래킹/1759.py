# 백준 1759 암호 만들기
import sys
input = sys.stdin.readline

l, c = map(int, input().split())
chars = input().split()
chars.sort()
voewls = ['a', 'e', 'i', 'o', 'u']

def dfs(idx, chars, visited):
  # 길이가 l 인 문자
  if len(visited) == l:
    vcnt = 0
    for vowel in voewls:
      if vowel in visited:
        vcnt += 1
    # 한 개 이상의 모음, 두 개 이상의 자음
    if vcnt >= 1 and l-vcnt >= 2:
      print(''.join(visited))
    return

  for i in range(idx, len(chars)):
    if chars[i] not in visited:
      visited.append(chars[i])
      dfs(i+1, chars, visited)
      visited.pop()

dfs(0, chars, [])