import sys
from collections import defaultdict
sys.setrecursionlimit(1005)

def solution(nodeinfo):
    level_map = defaultdict(list)
    for i in range(len(nodeinfo)):
        x, y = nodeinfo[i]
        level_map[y].append((x,i+1))

    levels = list(level_map.keys())
    levels.sort(reverse=True)
    tree = [[] for _ in range(len(levels))]
    for i in range(len(levels)):
        tree[i] += level_map[levels[i]]
        tree[i].sort()
    answer = []
    answer.append(preorder(tree, 0, 0, -1, 1e5+1))
    answer.append(postorder(tree, 0, 0, -1, 1e5+1))
    return answer

# 전위 순회
def preorder(tree, level, idx, llimit, rlimit):
    x, num = tree[level][idx]; order = [num]
    if level == len(tree)-1: return [num]
    for i in range(len(tree[level+1])):
        val = tree[level+1][i][0]
        if llimit < val < x:
            order += preorder(tree, level+1, i, llimit, x)
        if x < val < rlimit:
            order += preorder(tree, level+1, i, x, rlimit)
    return order

# 후위 순회
def postorder(tree, level, idx, llimit, rlimit):
    x, num = tree[level][idx]; order = []
    if level == len(tree)-1: return [num]
    for i in range(len(tree[level+1])):
        val = tree[level+1][i][0]
        if llimit < val < x:
            order += postorder(tree, level+1, i, llimit, x)
        if x < val < rlimit:
            order += postorder(tree, level+1, i, x, rlimit)
    return order + [num]