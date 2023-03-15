# 2-3. 중간 노드 삭제 O(N)

# 단방향 연결 리스트
class single_linked_list:
  def __init__(self):
    # 리스트 헤드와 길이 정보 초기화
    self.head = None
    self.len = 0

# 단방향 연결 리스트, 삭제할 노드의 데이터
def solution(linked_list, data):
  cur = linked_list.head
  prev = None

  while cur is not None:
    # 삭제할 노드
    if cur.data == data:
      prev.next = cur.next

    # 다음 노드 탐색
    prev = cur
    cur = cur.next