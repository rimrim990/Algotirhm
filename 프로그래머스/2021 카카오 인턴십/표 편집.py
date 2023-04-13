# from collections import deque
from heapq import heappush, heappop, heapify

def solution(n, k, cmds):
    copy = []
    cur = k # 현재 선택된 행 번호
    left = [-i for i in range(k)]; heapify(left) # 최대 힙
    right = [i for i in range(k+1, n)]; heapify(right) # 최소 힙

    for cmd in cmds:
        cmd = cmd.split()
        # 위로 x만큼 이동 - O(XloN)
        if cmd[0] == 'U':
            x = int(cmd[1])
            # 회전
            if x >= len(left)+len(right)+1:
                x %= len(left)+len(right)+1
            # 위로 이동
            if x <= len(left):
                for _ in range(x):
                    heappush(right, cur)
                    cur = -heappop(left)
            else:
                x = len(right)+len(left)+1-x
                for _ in range(x):
                    heappush(left, -cur)
                    cur = heapop(right)

        # 아래로 x만큼 이동 - O(XloN)
        elif cmd[0] == 'D':
            x = int(cmd[1])
            # 회전
            if x >= len(left) + len(right) + 1:
                x %= len(left)+len(right)+1
            # 아래로 이동
            if x <= len(right):
                for _ in range(x):
                    heappush(left, -cur)
                    cur = heappop(right)
            else:
                x = len(right)+len(left)+1-x
                for _ in range(x):
                    heappush(right, cur)
                    cur = -heappop(left)

        # 현재 선택한 행 삭제 - O(logN)
        elif cmd[0] == 'C':
            copy.append(cur)
            if right:
                cur = heappop(right)
            else:
                cur = -heappop(left)

        # 마지막으로 삭제한 행 복구 - O(logN)
        elif cmd[0] == 'Z':
            val = copy.pop()
            # 적절한 위치에 복구
            if val < cur:
                heappush(left, -val)
            else:
                heappush(right, val)

    answer = ['X' for _ in range(n)]
    for l in left: answer[-l] = 'O'
    for r in right: answer[r] = 'O'
    answer[cur] = 'O'
    return ''.join(answer)