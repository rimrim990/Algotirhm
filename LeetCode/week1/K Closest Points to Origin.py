from math import sqrt

class Solution:
  def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    dists = []
    for x, y in points:
      dists.append((self.calculate_distance(y, x), x, y))

    dists.sort()
    results = [dist[1:] for dist in dists[:k]]
    return results

  def calculate_distance(self, y, x):
    dist = pow(x, 2) + pow(y, 2)
    return sqrt(dist)
