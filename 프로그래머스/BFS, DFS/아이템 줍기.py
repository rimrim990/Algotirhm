from collections import deque

def solution(rectangles, chax, chay, ix, iy):
    dy = [-1,1,0,0]; dx = [0,0,-1,1]
    # 좌표, 직사각형 id
    dq = deque([(chay, chax, check(rectangles, chax, chay, chax, chay))])
    visited = [[-1 for _ in range(51)] for _ in range(51)]
    visited[chay][chax] = 0
    while dq:
        cy, cx, cid = dq.popleft()
        # 아이템 도착
        if iy == cy and ix == cx:
            break
        for i in range(4):
            ny = cy + dy[i]; nx = cx + dx[i]
            if 0 < ny <= 50 and 0 < nx <= 50 and visited[ny][nx] < 0:
                nid = check(rectangles, cx, cy, nx, ny)
                # 동일한 사각형 위에 있음
                if nid & cid:
                    visited[ny][nx] = visited[cy][cx] +1
                    dq.append((ny, nx, nid))
    return visited[iy][ix]

def check(rectangles, px, py, nx, ny):
    rid = 0
    for i in range(len(rectangles)):
        x0, y0, x1, y1 = rectangles[i]
        # 다른 사각형 내부의 점 - 둘레가 아님
        if x0 < (px + nx) / 2 < x1 and y0 < (py + ny) / 2< y1:
            return False
        # 둘레를 따라 이동
        elif x0 <= nx <= x1 and ny in [y0, y1]:
            rid |= 1 << i
        elif y0 <= ny <= y1 and nx in [x0, x1]:
            rid |= 1 << i
    return rid