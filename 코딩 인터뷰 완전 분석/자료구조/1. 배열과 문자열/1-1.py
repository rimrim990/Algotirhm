# 1-1. 중복이 없는가
# 자료구조를 사용한 해법 (해시 테이블) - O(N)
def solution_with_ds(str):
  alpha = {}
  for s in str:
    # 중복
    if alpha.get(s) is not None:
      return True
    alpha[s] = True

  # 중복 없음
  return False

# 자료구조를 사용하지 않은 해법 - O(NlogN)
def solution_without_ds(str):
  # 정렬
  str = sorted(str)
  for i in range(1, len(str)):
    # 중복
    if str[i] == str[i-1]:
      return True

  # 중복 없음
  return False

# 비트마스킹
def solution_updated(str):
  # 중복 체크를 위한 비트 벡터
  check = 0
  for s in str:
    # 캐릭터를 비트로 변환
    val = ord(s) - ord('a')
    bit = 1 << val

    # 중복 검사
    if check & bit: return False
    check = check | bit

  return True