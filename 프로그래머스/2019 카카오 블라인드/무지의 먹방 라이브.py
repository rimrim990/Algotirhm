from heapq import heappop, heappush

def solution(food_times, k):
  n, hq = len(food_times), []
  for i in range(n):
    heappush(hq, (food_times[i], i))

  prev = 0
  while hq:
    diff = hq[0][0] - prev

    # 한 사이클을 돌 수 있음.
    if k >= diff * len(hq):
      k -= diff * len(hq)
      prev = heappop(hq)[0]
      continue

    # 한 사이클을 돌 수 없음.
    p = k // len(hq)
    k -= p * len(hq)
    hq.sort(key=lambda x: x[1])
    return hq[k][1] + 1

  return -1