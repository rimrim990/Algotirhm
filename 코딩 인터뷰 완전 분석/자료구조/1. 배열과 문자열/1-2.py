# 1-2. 순열 관계
from collections import defaultdict

# O(N)
def solution(str_a, str_b):
  if len(str_a) != len(str_b):
    False

  alpha_a = defaultdict(int)
  alpha_b = defaultdict(int)

  # 문자열 구성 요소 카운트 - O(N)
  for i in range(len(str_a)):
    alpha_a[str_a[i]] += 1
    alpha_b[str_b[i]] += 1

  # 구성 요소가 일치하는지 검사 - O(N)
  for key in alpha_a.keys():
    if alpha_a[key] != alpha_b[key]:
      return False

  return True

# 정렬하여 비교 - O(NlogN)
def solution_with_sort(str_a, str_b):
  return sorted(str_a) == sorted(str_b)