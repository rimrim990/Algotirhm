# 2-5. 리스트의 합

# 입력 - 두 개의 단방향 연결리스트
def solution(lla, llb):
  max_len = max(lla.len, llb.len)
  cur = None
  a_cur = lla.head; b_cur = llb.head

  for i in range(max_len):
    data = Node(a_cur.data + b_cur.data)
    # 자릿수 별로 분리하여 새로운 노드 삽입
    while data > 0:
      if cur is None:
        cur = Node(data % 10)
      else:
        cur.next = Node(data % 10)
      data //= 10