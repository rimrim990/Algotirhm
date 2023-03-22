# 백준 1062 가르침

import sys
input = sys.stdin.readline

# 단어의 개수, 가르쳐야 하는 단어의 수
n, k = map(int, input().split())
words = [] # 단어

for _ in range(n): # 비트 마스킹
  word = 0 # 비트 벡터
  for w in input().rstrip():
    bit = 1 << (ord(w)-ord('a'))
    word |= bit
  words.append(word)

read = 0 # 읽을 수 있는 단어 초기화
for c in set('antatica'):
  bit = 1 << (ord(c)-ord('a'))
  read |= bit

def solution(k, idx, read): # 생성 가능한 조합
  max_cnt = 0

  if k == 0:
    for word in words:
      if word & read == word: max_cnt += 1
    return max_cnt

  for i in range(idx, 27):
    bit = 1 << i
    if bit & read > 0: continue
    max_cnt = max(max_cnt, solution(k-1, i+1, read | bit))

  return max_cnt

# 정답 출력
print(solution(k-5, 0, read) if k >= 5 else 0)