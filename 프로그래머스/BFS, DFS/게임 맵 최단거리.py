from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    dq = deque([(0,0)])
    visited = [[-1 for _ in range(m)] for _ in range(n)]
    visited[0][0] = 1
    dy = [-1,1,0,0]; dx = [0,0,-1,1]
    while dq:
        cy, cx = dq.popleft()
        for i in range(4):
            ny = cy + dy[i]; nx = cx + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if visited[ny][nx] == -1 and maps[ny][nx] == 1:
                    visited[ny][nx] = visited[cy][cx] + 1
                    dq.append((ny, nx))
    return visited[n-1][m-1]