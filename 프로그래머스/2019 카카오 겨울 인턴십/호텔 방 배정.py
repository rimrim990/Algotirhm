import sys
sys.setrecursionlimit(10**6)

def solution(k, room_number):
    hotel = {}; answer = []
    for number in room_number:
        # 비어있는 방
        if hotel.get(number) is None:
            hotel[number] = number
            answer.append(number)
        # 비어있지 않음
        else:
            # target 보다 큰 값 중에서 가장 작은 값
            root = find(hotel, number)
            hotel[root+1] = root+1
            union(number, root+1, hotel)
            answer.append(root+1)

        # 추가된 수와 연속한 수가 존재하는지 검사
        for nxt in [answer[-1]-1, answer[-1]+1]:
            if hotel.get(nxt):
                union(nxt, answer[-1], hotel)

    return answer

# x 의 루트 노드 탐색
def find(parent, x):
    if parent.get(x) != x:
        parent[x] = find(parent, parent.get(x))
    return parent.get(x)

# 트리 x 와 트리 y 병합
def union(x, y, parent):
    px = find(parent, x)
    py = find(parent, y)
    if px > py:
        parent[py] = px
    else:
        parent[px] = py