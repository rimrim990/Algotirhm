import java.util.*;

class Solution {
    Pair start, end, lever; // 시작 지점, 출구, 레버
    int n, m; // 직사각형의 세로, 가로 길이
    int[] dy = {-1,1,0,0};
    int[] dx = {0,0,-1,1};

    public int solution(String[] maps) {
        n = maps.length;
        m = maps[0].length();
        for (int i=0; i<n; i++) {
            for (int j=0; j<m; j++) {
                switch (maps[i].charAt(j)) {
                    case 'S':
                        start = new Pair(i, j);
                        break;
                    case 'L':
                        lever = new Pair(i, j);
                        break;
                    case 'E':
                        end = new Pair(i, j);
                        break;
                }
            }
        }
        int n1 = bfs(maps, start, lever);
        int n2 = bfs(maps, lever, end);
        if (n1 == -1 || n2 == -1) return -1;
        else return n1 + n2;
    }

    private int bfs(String[] maps, Pair start, Pair end) {
        int[][] visit = new int[n][m];
        visit[start.y][start.x] = 1;

        Queue<Pair> q = new LinkedList();
        q.add(start);

        while (!q.isEmpty()) {
            Pair cur = q.poll();
            // 목적지 도착
            if (cur.y == end.y && cur.x == end.x) {
                return visit[cur.y][cur.x]-1;
            }

            for (int i=0; i<4; i++) {
                int ny = cur.y + dy[i];
                int nx = cur.x + dx[i];
                if (ny >= 0 && ny < n && nx >= 0 && nx < m) {
                    // 아직 방문하지 않음
                    if (visit[ny][nx] == 0 && maps[ny].charAt(nx) != 'X') {
                        visit[ny][nx] = visit[cur.y][cur.x]+1;
                        q.add(new Pair(ny, nx));
                    }
                }
            }
        }
        return -1;
    }

    private static class Pair {
        int y, x;

        public Pair(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }
}