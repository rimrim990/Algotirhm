# 3-4. 스택 정렬 - O(N^2)

# 정렬해야 할 아이템이 들어있는 스택, 버퍼 용도의 빈 스택
def stack_sort(stack, buf):
  while len(stack) > 0 :
    data = stack.pop()
    # buf 보다 data 가 큼
    while len(buf) > 0 and buf[-1] < data:
      stack.append(buf.pop())
    # data 는 buf 에 있는 수들보다 작거나 같다
    buf.append(data)
  return buf