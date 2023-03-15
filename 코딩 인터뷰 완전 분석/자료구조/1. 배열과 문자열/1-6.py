# 1-6. 문자열 압축 - O(N)

def solution(s):
  res = [s[0]]
  cnt = 1

  for i in range(1, len(s)):
    # case1. 압축 대상
    if s[i] == s[i-1]:
      cnt += 1
      continue

    # case2. 다른 문자열 등장
    res.append(str(cnt))
    res.append(s[i])
    cnt = 1

  # 마지막 문자의 카운트 포함
  res.append(str(cnt))

  # 기존 문자열보다 길면 기존 문자열 반환
  res = ''.join(res)
  return s if len(res) > len(s) else res