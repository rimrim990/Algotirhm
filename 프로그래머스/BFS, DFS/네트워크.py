from collections import deque

def solution(n, computers):
    answer = 0
    visited = [0 for _ in range(n)]
    for v in range(n):
        if not visited[v]:
            answer += 1
            bfs(v, computers, visited)
    return answer

def bfs(v, computers, visited):
    visited[v] = 1
    dq = deque([v])
    while dq:
        cur = dq.popleft()
        for nxt in range(len(computers)):
            if computers[cur][nxt] and not visited[nxt]:
                visited[nxt] = 1
                dq.append(nxt)