# 2-6. 회문
from collections import defaultdict

# 입력 - 두 개의 단방향 연결리스트
def solution(linked_list):
  cur = linked_list.head
  prev = None
  # 중복 카운트를 위한 해시 테이블
  cnt = defaultdict(int)

  while cur is not None:
    cnt[cur.data] += 1

    # 다음 노드 탐색
    prev = cur
    cur = cur.next

  is_cent_word = False
  for k in cnt.keys():
    if cnt[k] == 0:
      continue
    elif is_cent_word is True:
      return False
    is_cent_word = True

  return is_cent_word is True