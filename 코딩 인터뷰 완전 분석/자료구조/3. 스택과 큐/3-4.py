# 3-4. 스택으로 큐

class MyQueue:
  def __init__(self):
    # stack1. input 버퍼
    self.sin = []
    # stack2. output 버퍼
    self.sout = []

  def add(self, data):
    self.sin.append(data)

  def remove(self):
    # 원소가 없음
    if len(self.sin) + len(self.sout) == 0:
      return None

    if len(self.sout) == 0:
      while len(self.sin) > 0:
        data = self.sin.pop()
        self.sout.append(data)

    return self.sout.pop()