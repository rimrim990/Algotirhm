import java.util.*;

class Solution {

    private static final int[] dy = {-1,1,0,0};
    private static final int[] dx = {0,0,-1,1};

    public int solution(String[] board) {
        int n = board.length;
        int m = board[0].length();
        Integer[] start = new Integer[2];
        Integer[] end = new Integer[2];
        for (int i=0; i<board.length; i++) {
            for (int j=0; j<board[i].length(); j++) {
                // 시작 지점
                if (board[i].charAt(j) == 'R') {
                    start[0] = i;
                    start[1] = j;
                }
                // 도착 지점
                else if (board[i].charAt(j) == 'G') {
                    end[0] = i;
                    end[1] = j;
                }
            }
        }

        int answer = bfs(start, end, board, n, m);
        return answer;
    }

    private int bfs(Integer[] start, Integer[] end, String[] board, int n, int m) {
        // 방문 기록
        int[][] visited = new int[n][m];
        visited[start[0]][start[1]] = 1;

        // 방문 큐
        Queue<Integer[]> q = new LinkedList<>();
        q.add(start);

        while (!q.isEmpty()) {
            Integer[] cur = q.poll();
            if (cur[0] == end[0] && cur[1] == end[1]) break;

            for (int i=0; i<4; i++) {
                Integer[] nxt = slide(cur, board, dy[i], dx[i], n, m);
                // 아직 방문하지 않음
                if (visited[nxt[0]][nxt[1]] == 0) {
                    visited[nxt[0]][nxt[1]] = visited[cur[0]][cur[1]] + 1;
                    q.add(nxt);
                }
            }
        }
        return visited[end[0]][end[1]]-1;
    }

    private Integer[] slide(Integer[] cur, String[] board, int dy, int dx, int n, int m) {
        Integer[] nxt = {cur[0], cur[1]};
        // 다음 칸으로 이동 가능
        while (check(nxt[0]+dy, n) && check(nxt[1]+dx, m)) {
            if (board[nxt[0]+dy].charAt(nxt[1]+dx) == 'D') break;
            nxt[0] += dy;
            nxt[1] += dx;
        }
        return nxt;
    }

    private boolean check(Integer cur, Integer limit) {
        if (cur >= 0 && cur < limit) {
            return true;
        }
        return false;
    }
}