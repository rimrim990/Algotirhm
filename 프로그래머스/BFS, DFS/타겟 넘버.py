def solution(numbers, target, idx=0, total=0):
    if idx >= len(numbers):
        if target == total: return 1
        else: return 0
    cnt = 0
    cnt += solution(numbers, target, idx+1, total+numbers[idx])
    cnt += solution(numbers, target, idx+1, total-numbers[idx])
    return cnt

def solution_dp(numbers, target):
    # [위치][값+1000]
    dp = [[0 for _ in range(2001)] for _ in range(22)]
    dp[0][1000] = 1
    for i in range(len(numbers)):
        for j in range(2001):
            # 이전 번호를 조합하여 j-1000 생성 가능
            if dp[i][j] > 0:
                for nxt in [j-numbers[i], j+numbers[i]]:
                    if 0 <= nxt <= 2000:
                        dp[i+1][nxt] += dp[i][j]
    return dp[len(numbers)][target+1000]