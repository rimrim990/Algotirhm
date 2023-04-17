from collections import defaultdict

def solution(tickets):
    tmap = defaultdict(list)
    for i in range(len(tickets)):
        a, b = tickets[i]
        # 티겟 번호, 도착지
        tmap[a].append((b, i))

    # 알파벳 순으로 정렬
    for key in tmap:
        tmap[key].sort()

    visited = [0 for _ in range(len(tickets))]
    tids = dfs("ICN", tmap, visited, [])
    return ["ICN"] + list(map(lambda x: tickets[x][1], tids))

def dfs(cur, tmap, visited, res):
    # 모든 티켓 사용 완료
    if len(res) == len(visited):
        return res
    for nxt, tid in tmap[cur]:
        # 아직 사용하지 않은 티켓
        if not visited[tid]:
            visited[tid] = 1
            t = dfs(nxt, tmap, visited, res + [tid])
            if t: return t
            visited[tid] = 0