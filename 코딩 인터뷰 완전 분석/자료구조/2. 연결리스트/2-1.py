# 2-1. 중복 없애기 O(N)

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

# 단방향 연결 리스트 가정
def solution(head):
  # 중복 체크를 위한 해시 테이블
  checked = {}
  # 현재 노드와 이전 노드
  cur = head; prev = None
  while cur != None:
    # 중복 체크
    if checked.get(cur.data) is not None:
      # 연결 끊기
      if prev != None:
        prev.next = cur.next
      # 헤더 갱신
      if cur == head:
        head = cur.next

    # 해시 테이블 갱신
    checked[cur.data] = True
    # 다음 노드 탐색
    prev = cur
    cur = cur.next