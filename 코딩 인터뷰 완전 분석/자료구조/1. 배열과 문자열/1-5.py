# 1-5. 하나 빼기

'''
1. 최장 공통 수열의 길이 maxLen 구하기
2. 두 문자열의 길이 A 와 B 에 대하여, max(A, B) - maxLen 계산
'''
def solution(str_a, str_b):
  # 문자열 길이
  max_len = max(len(str_a), len(str_b))

  # 최장 공통 수열
  lcs = [[0 for j in range(len(str_b)+1)] for i in range(len(str_a)+1)]

  for i in range(1, len(str_a)+1):
    for j in range(1, len(str_b)+1):
      # 최댓값
      lcs[i][j] = max(lcs[i][j-1], lcs[i-1][j])

      # 두 문자가 동일할 경우
      if str_a[i-1] == str_b[j-1]:
        lcs[i][j] = max(lcs[i][j], lcs[i-1][j-1]+1)

  # 편집거리 계산
  edit_dist = max_len - lcs[len(str_a)][len(str_b)]

  # 편집 거리가 1 이내
  return edit_dist <= 1