from collections import deque

def solution(begin, target, words):
    n = len(words)
    visited = {}; visited[begin] = 0
    dq = deque([begin])
    while dq:
        cur = dq.popleft()
        if cur == target:
            return visited[cur]
        for nxt in words:
            if diff(cur, nxt) == 1 and not visited.get(nxt):
                visited[nxt] = visited[cur] + 1
                dq.append(nxt)
    return 0

def diff(w1, w2):
    cnt = 0
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            cnt += 1
    return cnt