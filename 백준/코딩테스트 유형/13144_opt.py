# 백준 13144. List of Unique Numbers
n = int(input())
arr = list(map(int, input().split()))
nums = [False for _ in range(100_001)]

# 투 포인터
def solve(n, arr, nums):
  left = 0; right = 0
  total = 0

  while left < n:
    # [left, right)
    while right < n:
      if nums[arr[right]]:
        break

      nums[arr[right]] = True
      right += 1
      total += right - left

    nums[arr[left]] = False
    left += 1

  return total

print(solve(n, arr, nums))