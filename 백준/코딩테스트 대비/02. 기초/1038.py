# 백준 1038 감소하는 수

import sys
input = sys.stdin.readline

# n 번째 감소하는 수 찾기
n = int(input())
# 감소하는 수 dp - [자릿수]
nums = [[] for _ in range(10)]
# 자릿수가 1인 감소하는 수 초기화
for i in range(10):
  nums[0].append(str(i))

'''
모든 감소하는 수 탐색
'''
# 감소하는 수의 자릿수 - 최대 값 987654321
for i in range(1, 10):
  # 감소하는 수의 시작 숫자 - 0~9
  for j in range(10):
    # 이전 값 재사용
    for k in nums[i-1]:
      # 이전 값보다 시작 숫자가 더 커야 감소하는 숫자 생성 가능
      if int(k[0]) < j: nums[i].append(str(j) + k)

# n 번째 감소하는 수
res = -1
for num in nums:
  for i in num:
    if n == 0: res = int(i); break
    else: n -= 1
  if res >= 0: break

print(res)