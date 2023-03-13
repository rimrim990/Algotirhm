# 2-2. 뒤에서 k번째 원소 구하기 O(N)

# 단방향 연결 리스트
class single_linked_list:
  def __init__(self):
    # 리스트 헤드와 길이 정보 초기화
    self.head = None
    self.len = 0

def solution(linked_list, k):
  # 뒤에서 k 번째 원소
  target = linked_list.len - k
  res = linked_list.head

  # k 번째 원소 탐색
  while target > 0:
    res = res.next
    target -= 1

  return res