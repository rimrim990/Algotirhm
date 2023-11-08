from collections import defaultdict

def solution(info, edges):
  graph = defaultdict(list)
  for parent, child in edges:
    graph[parent].append(child)

  gr = Graph(info, graph)
  gr.traverse(0, set())
  return gr.get_max_count()

class Graph:
  def __init__(self, info, edges):
    self.info = info
    self.edges = edges

    self.count = [1, 0]
    self.max_sheep = 1
    self.visited = [False for _ in range(len(info))]

  def traverse_next(self, nxt, will_visit):
    val = self.info[nxt]
    self.count[val] += 1
    self.visited[nxt] = True
    self.traverse(nxt, will_visit)
    self.visited[nxt] = False
    self.count[val] -= 1

  def can_movable(self, pos):
    val = self.info[pos]
    copy = self.count[:]
    copy[val] += 1
    return copy[0] > copy[1]

  def traverse(self, cur, will_visit):
    self.max_sheep = max(self.max_sheep, self.count[0])

    move_nxt = []
    for nxt in self.edges[cur]:
      if self.visited[nxt]:
        continue

      if self.can_movable(nxt):
        move_nxt.append(nxt)

      will_visit.add(nxt)

    # 이전에 방문하지 못했던 노드 재방문
    for nxt in will_visit:
      if self.can_movable(nxt):
        copy = will_visit.copy()
        copy.remove(nxt)
        self.traverse_next(nxt, copy)

    # 자식 노드 방문
    for nxt in move_nxt:
      copy = will_visit.copy()
      copy.remove(nxt)
      self.traverse_next(nxt, copy)

  def get_max_count(self):
    return self.max_sheep