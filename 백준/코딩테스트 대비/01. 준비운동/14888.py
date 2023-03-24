# 백준 14888 연산자 끼워넣기

import math
import sys
input = sys.stdin.readline

# 입력
n = int(input()) # 수의 개수
seq = list(map(lambda x: int(x), input().split())) # 수열 A
opr = list(map(lambda x: int(x), input().split())) # +, -, x, /

# 최댓값, 최솟값
max_val = -math.inf; min_val = math.inf

def dfs(val, idx):
  global max_val, min_val, n

  # 모든 연산자 사용
  if idx == n:
    max_val = max(max_val, val)
    min_val = min(min_val, val)
    return

  for i in range(4):
    if opr[i] == 0: continue
    opr[i] -= 1
    # 연산
    if i==0:
      res=val+seq[idx]
    elif i==1:
      res=val-seq[idx]
    elif i==2:
      res=val*seq[idx]
    elif i==3:
      res=abs(val)//seq[idx]
      res=-res if val<0 else res
    # 백트래킹
    dfs(res, idx+1)
    opr[i] += 1

# 탐색
dfs(seq[0], 1)

# 출력
print(max_val, min_val, sep='\n')