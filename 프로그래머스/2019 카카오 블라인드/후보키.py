from itertools import combinations

def solution(relation):
    n = len(relation[0]); nums = [i for i in range(n)]
    cand_key = {}
    for i in range(1, n+1):
        # 가능한 후보키
        for key in combinations(nums, i):
            # 후보키 비트맵 생성
            bit = 0
            for k in key:
                bit |= 1 << k
            if not minimum(cand_key, bit):
                continue
            if not unique(relation, key):
                continue
            cand_key[bit] = 1
    return len(cand_key)

def minimum(cand_key, bit):
    # 부분 집합 존재 여부 검사
    for key in cand_key:
        if key & bit == key:
            return False
    return True

def unique(relations, cand):
    dup = []
    for relation in relations:
        cur = []
        for c in cand:
            cur.append(relation[c])
        if cur in dup:
            return False
        dup.append(cur)
    return True