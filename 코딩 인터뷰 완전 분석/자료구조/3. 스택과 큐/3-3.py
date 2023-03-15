# 3-3. 접시 무더기

class SetOfStacks:
  def __init__(self, limit):
    # 스택 집합
    self.stacks = [[]]
    self.limit = limit

  def push(self, data):
    # 마지막 스택이 limit 을 넘었는지 검사
    if len(self.stacks[-1]) == self.limit:
      self.stacks.append([])
    # 마지막 스택에 원소 삽입
    self.stacks[-1].append(data)

  def pop(self):
    # 마지막 스택에 원소가 존재하는지 검사
    if len(self.stacks[-1]) == 0:
      self.stacks.pop()
    # 원소를 제거할 스택이 존재하는지 검사
    if len(self.stacks) == 0:
      return None
    return self.stacks[-1].pop()