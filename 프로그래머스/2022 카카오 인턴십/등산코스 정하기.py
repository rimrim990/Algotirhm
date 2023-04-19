from heapq import heappop, heappush

def solution(n, paths, gates, summits):
    answer = [n+1, 1e7+1]

    # 경로
    graph =[[] for _ in range(n+1)]
    for i, j , w in paths:
        graph[i].append((j,w))
        graph[j].append((i,w))

    hq = []
    intens = [-1 for _ in range(n+1)]

    for gate in gates:
        hq.append((0, gate))
        intens[gate] = 0

    while hq:
        cintens, cur = heappop(hq)
        # 최소 intensity 로 정상 도달
        if cur in summits:
            if cintens > answer[1]:
                break
            elif cintens < answer[1]:
                answer = [cur, cintens]
            elif cur < answer[0]:
                answer[0] = cur
            continue
        # 최소 경로가 아님
        if cintens > intens[cur]:
            continue
        # intensity 갱신
        for nxt, cost in graph[cur]:
            nintens = max(cintens, cost)
            if intens[nxt] == -1 or nintens < intens[nxt]:
                intens[nxt] = nintens
                heappush(hq, (nintens, nxt))

    return answer