from itertools import permutations

MAX = 9

def solution(n, weak, dist):
  wn = len(weak)
  weak.extend([w+n for w in weak])
  orders = list(permutations(dist, len(dist)))

  ans = MAX
  # weak 수리 순서 재조정
  for i in range(wn):
    ws = weak[i:i+wn]

    # 친구들 투입 순서 조정
    for order in orders:
      widx = 0

      # 친구 한 명씩 투입
      for j in range(len(order)):
        end = ws[widx]+order[j]

        # 이동 거리만큼 점검
        while widx < wn:
          if ws[widx] <= end:
            widx += 1
          else:
            break

        if widx >= wn:
          ans = min(ans, j+1)
          break

  return ans if ans != MAX else -1
