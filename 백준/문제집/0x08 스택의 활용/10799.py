 # 백준 10799 쇠막대기

 import sys
 input = sys.stdin.readline

 # 쇠막대기와 레이저
 ss = input().rstrip()
 stack = []; total_cnt = 0

 for section in ss.split('()'):
   # 이전에 올라온 막대기
   total_cnt += len(stack)
   for s in section:
     if s == '(':
       stack.append('(')
       # 새로운 막대기 추가
       total_cnt += 1
     else:
       stack.pop()

 print(total_cnt)