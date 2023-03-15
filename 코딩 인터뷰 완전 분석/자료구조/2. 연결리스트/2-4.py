# 2-4. 분할 O(N)

# 단방향 연결 리스트
class single_linked_list:
  def __init__(self):
    # 리스트 헤드와 길이 정보 초기화
    self.head = None
    self.len = 0

# x 보다 작은 값들을 헤드에 삽입
def solution(linked_list, x):
  cur = linked_list.head
  prev = None

  while cur is not None:
    # 헤드에 삽입할 노드
    if cur.data < x:
      # 1. 현재 위치에서 삭제
      if prev is not None:
        prev.next = cur.next

      # 2. 헤드에 삽입
      cur.next = linked_list.head.next
      linked_list.head = cur

    # 다음 노드 탐색
    prev = cur
    cur = cur.next