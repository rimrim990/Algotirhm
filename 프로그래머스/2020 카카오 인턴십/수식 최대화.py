from collections import deque
from itertools import permutations

def solution(expression):
    answer = 0
    # 문자와 숫자로 분리
    expr = []; num = []
    for e in expression:
        if e not in ['*', '-', '+']:
            num.append(e)
        else:
            expr.append(int(''.join(num)))
            expr.append(e)
            num = []
    expr.append(int(''.join(num)))

    # 연산자 우선순위 생성
    for oprs in permutations(['*', '+', '-'], 3):
        res = expr[:]
        # 연산자 우선순위에 따라 식 계산
        for opr in oprs:
            res = evaluate(opr, res)
        # 최댓값 갱신
        answer = max(answer, abs(res[0]))
    return answer

# 연산자 계산
def evaluate(opr, expr):
    res = []
    expr = deque(expr)
    while expr:
        e = expr.popleft()
        if e != opr:
            res.append(e)
            continue
        n1 = res.pop()
        n2 = expr.popleft()
        if e == '*':
            res.append(n1 * n2)
        elif e == '+':
            res.append(n1+n2)
        elif e == '-':
            res.append(n1-n2)
    return res