from heapq import heappop, heappush

def solution(board):
    n = len(board)
    dy = [0,0,-1,1]
    dx = [1,-1,0,0]
    dd = [0,0,1,1] # 좌우 이동 / 상하 이동

    # 최소 힙 - 비용, 좌표, 방향
    hq = [(0,0,0,-1)]
    visited = [[[-1,-1] for _ in range(n)] for _ in range(n)] # 방향, 좌표
    visited[0][0] = [0,0]

    while hq:
        # 좌우 - 0, 상하 - 1
        cost, cy, cx, cd = heappop(hq)
        if cy == n-1 and cx == n-1:
            return cost
        if cost > visited[cy][cx][cd]:
            continue
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            nd = dd[i]
            is_corner = cd != nd and cd != -1
            if 0 <= ny < n and 0 <= nx < n and board[ny][nx] == 0:
                ncost = cost + 600 if is_corner else cost + 100
                if visited[ny][nx][nd] < 0 or ncost < visited[ny][nx][nd]:
                    visited[ny][nx][nd] = ncost
                    heappush(hq, (ncost, ny, nx, nd))