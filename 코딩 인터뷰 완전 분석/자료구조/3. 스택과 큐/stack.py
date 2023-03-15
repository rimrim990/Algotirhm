# 파이썬으로 큐 구현하기

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

# 연결 리스트 기반 스택
class Stack:
  def __init__(self):
    self.head = None
    self.tail = None

  def is_empty(self):
    return self.head is None

  def top(self):
    return self.tail

  # head 에 노드 삽입
  def push(self, data):
    node = Node(data)
    if self.head is not None:
      node.next = self.head
    self.head = node
    if self.tail is None:
      self.tail = node

  # head 에서 노드 제거
  def pop(self):
    if self.is_empty() is True:
      return None
    node = self.head
    self.head = node.next
    if node == self.tail:
      self.tail = None
    return node