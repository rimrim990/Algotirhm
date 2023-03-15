# 파이썬으로 큐 구현하기

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

# 연결 리스트 기반 큐
class Queue:
  def __init__(self):
    self.head = None
    self.tail = None

   def is_empty(self):
       return self.head == None

   def peek(self):
    return self.head

  # tail 에 노드 삽입
  def append(self, data):
    node = Node(data)
    # tail 에 연결
    if self.tail is not None:
      self.tail.next = node
    self.tail = node
    # 처음 삽입되는 노드
    if self.head is None:
      self.head = node

  # head 에서 노드 제거
  def popleft(self):
    # 노드 없음
    if self.head is None:
      return None
    node = self.head
    self.head = node.next
    # node 가 tail 일 경우
    if self.tail == node:
      self.tail = None
    return node