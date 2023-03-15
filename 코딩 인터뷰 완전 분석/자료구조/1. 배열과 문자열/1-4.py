# 1-4. 회문 (palindrome) 순열
from collections import defaultdict

def solution(str):
  # 소문자로 정규화
  str = str.lower()
  # 각 문자의 등장 횟수 카운트
  alpha = defaultdict(int)

  for s in str:
    # 공백 문자 무시
    if s == ' ': continue
    alpha[s] += 1

  # 중심 문자
  is_cent_word = False

  # 팰린드롬 생성 가능한지 검사
  for key, val in alpha.items():
    if val % 2 == 0:
      continue
    elif is_cent_word is True:
      return False

    # 중심 문자
    is_cent_word = True

  # 중심 문자 없으면 False 반환
  return is_cent_word is True