from heapq import heappush, heappop

def solution(n, start, end, roads, trap_info):
    # 함정 정보
    traps = [0 for _ in range(n+1)]
    for t in trap_info:
        traps[t] = 1

    # 경로 정보
    path = [[] for _ in range(n+1)]
    # 반대 경로
    reverse_path = [[] for _ in range(n+1)]
    for p, q, s in roads:
        path[p].append((q,s))
        if traps[p] or traps[q]:
            reverse_path[q].append((p,s))

    # 시간, 방 번호, 함정
    hq = [(0, start, 0)]
    # 활성화된 트랩 번호
    dist = [{} for _ in range(n+1)]
    dist[start][0] = 0
    while hq:
        elapsed, cur, active = heappop(hq)
        cbit = 1 << cur
        # 탐색 종료
        if cur == end: continue
        # 정방향 경로 탐색
        for nxt, cost in path[cur]:
            nbit = 1 << nxt
            if ((active & cbit) > 0) != ((active & nbit) > 0): continue
            nactive = active
            # 비활성화
            if active & nbit:
                nactive -= nbit
            # 활성화
            elif traps[nxt]:
                nactive += nbit
            if not dist[nxt].get(nactive) or dist[nxt][nactive] > elapsed + cost:
                dist[nxt][nactive] = elapsed + cost
                heappush(hq, (dist[nxt][nactive], nxt, nactive))

        for nxt, cost in reverse_path[cur]:
            nbit = 1 << nxt
            if ((active & cbit) >0) == ((active & nbit)>0): continue
            nactive = active
            # 활성화 -> 비활성화
            if active & nbit:
                nactive -= nbit
            # 비활성화 -> 활성화
            elif traps[nxt]:
                nactive += nbit
            if not dist[nxt].get(nactive) or dist[nxt][nactive] > elapsed + cost:
                dist[nxt][nactive] = elapsed + cost
                heappush(hq, (dist[nxt][nactive], nxt, nactive))

    # 마지막 방은 트랩이 아님
    return min(dist[end].values())