def solution(numbers, hand):
    answer = []
    left = '*'; right = '#'
    for number in numbers:
        if number in [1,4,7]:
            answer.append('L')
            left = number
            continue
        if number in [3,6,9]:
            answer.append('R')
            right = number
            continue
        # 더 가까운 손가락으로 누르기
        thand = get_hand(left, right, number, hand)
        if thand == 'left':
            answer.append('L')
            left = number
        else:
            answer.append('R')
            right = number
    return ''.join(answer)

def get_hand(left, right, target, hand):
    lx, ly = get_xy(left)
    rx, ry = get_xy(right)
    tx, ty = get_xy(target)
    distl = abs(lx-tx) + abs(ly-ty)
    distr = abs(rx-tx) + abs(ry-ty)
    if distl < distr: return 'left'
    if distl > distr: return 'right'
    return hand

def get_xy(pos):
    if pos == '*': return (0,3)
    if pos == '#': return (2, 3)
    if pos == 0: return (1, 3)
    return ((pos-1) % 3 ,(pos-1) // 3)