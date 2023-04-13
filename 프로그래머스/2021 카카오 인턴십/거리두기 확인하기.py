def solution(places):
    answer = []
    for place in places:
        res = check(place)
        answer.append(res)
    return answer

def check(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                if not safe(place, i, j):
                    return 0
    return 1

def safe(place, y, x):
    dy = [-1,1,0,0, 1,1,-1,-1, 2,-2,0,0]
    dx = [0,0,-1,1, 1,-1,1,-1, 0,0,2,-2]

    # 맨해튼 거리 탐색
    for i in range(12):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < 5 and 0 <= nx < 5:
            if place[ny][nx] == 'P':
                # 맨해튼 거리 1일 때
                if i < 4: return False
                # 맨해튼 거리 2이고 대각선 방향일 때
                elif i < 8:
                    if place[ny][x] != 'X' or place[y][nx] != 'X':
                        return False
                # 맨해튼 거리가 2이고 직선 방향일 때
                else:
                    if place[(ny+y)//2][(nx+x)//2] != 'X':
                        return False
    return True