from math import inf

def solution(sales, links):
  n = len(sales)

  # 그래프
  graph = [[] for _ in range(n+1)]
  for a, b in links:
    graph[a].append(b)

  # 초기화
  dp = [[inf, inf] for _ in range(n+1)]
  for i in range(1, n+1):
    if not graph[i]:
      dp[i][1] = 0

  dfs(1, dp, graph, sales)

  return min(dp[1])

def dfs(cur, dp, graph, sales):
  sub_sum = 0

  # 서브 트리의 최소 합
  for nxt in graph[cur]:
    dfs(nxt, dp, graph, sales)
    sub_sum += min(dp[nxt])

  # cur이 워크숍에 참석.
  dp[cur][0] = sales[cur-1] + sub_sum

  # cur이 워크숍에 참석하지 않음.
  for nxt in graph[cur]:
    # nxt가 워크숍에 반드시 참여함.
    delta = -min(dp[nxt]) + dp[nxt][0]
    dp[cur][1] = min(dp[cur][1], sub_sum + delta)