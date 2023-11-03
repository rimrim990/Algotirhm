# 백준 13144. List of Unique Numbers
n = int(input())
nums = list(map(int, input().split()))
words = {}

# 투 포인터
def solve(n, nums):
  left = 0; right = 0
  total = 0; prev = None

  while left < n:
    # [left, right)
    while right < n:
      if words.get(nums[right]) == True:
        break

      words[nums[right]] = True
      right += 1

    total += count(prev, (left, right-1))
    prev = (left, right-1)

    words[nums[left]] = False
    left += 1

  return total

def count(prev, cur):
  total = cal(*cur)
  if prev and prev[1] >= cur[0]:
    total -= cal(cur[0], prev[1])
  return total

def cal(left, right):
  if left == right: return 1
  length = right-left+1
  return length * (length+1) // 2

print(solve(n, nums))