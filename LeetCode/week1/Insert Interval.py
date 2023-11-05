class Solution:
  def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    idx = 0
    n = len(intervals)
    merged = []

    # add to left
    while idx < n and intervals[idx][1] < new_interval[0]:
      merged.append(intervals[idx])
      idx += 1

    # merge intervals
    while idx < n and intervals[idx][0] <= new_interval[1]:
      new_interval[0] = min(new_interval[0], intervals[idx][0])
      new_interval[1] = max(new_interval[1], intervals[idx][1])
      idx += 1

    merged.append(new_interval)

    # add to right
    while idx < n:
      merged.append(intervals[idx])
      idx += 1

    return merged