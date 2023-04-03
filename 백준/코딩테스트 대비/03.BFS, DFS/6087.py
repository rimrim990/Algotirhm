 # 백준 6078 레이저 통신
 import sys
 from heapq import heappush, heappop
 input = sys.stdin.readline

 w, h = map(int, input().split())
 graph = []; mirror = []

 # 레이저의 위치
 for i in range(h):
   graph.append(list(input().rstrip()))
   for j in range(w):
     if graph[i][j] == 'C':
       mirror.append((i,j))

 start = mirror[0]; end = mirror[1]
 dy = [-1,1,0,0]; dx = [0,0,-1,1]

 def bfs(start, end, graph):
   h = len(graph); w = len(graph[0])
   # 행, 열, 진행 방향
   visited = [[[-1,-1,-1,-1] for _ in range(w)] for _ in range(h)]
   visited[start[0]][start[1]] = [0,0,0,0]
   # 거울 사용 횟수가 적은 노드 - 최소 힙
   heap = [(0, *start, -1)]
   while heap:
     # 거울 사용 횟수, 위치, 진행 방향
     cnt, cy, cx, dir = heappop(heap)
     if cy == end[0] and cx == end[1]:
       break
     # 최단 경로가 아님
     if dir >= 0 and visited[cy][cx][dir] < cnt:
       continue
     for i in range(4):
       ny = cy + dy[i]
       nx = cx + dx[i]
       # 거울 사용 횟수
       ncnt = cnt
       if dir >= 0 and dir != i: ncnt+=1
       # 이웃 노드 탐색
       if 0 <= ny < h and 0 <= nx < w:
         if graph[ny][nx] == '*': continue
         # 1. 아직 방문하지 않음
         # 2. 최솟값 갱신
         if visited[ny][nx][i] < 0 or ncnt < visited[ny][nx][i]:
           visited[ny][nx][i] = ncnt
           heappush(heap, (ncnt, ny, nx, i))
   return min(filter(lambda x: x >= 0, visited[end[0]][end[1]]))

 # 정답 출력
 print(bfs(start, end, graph))