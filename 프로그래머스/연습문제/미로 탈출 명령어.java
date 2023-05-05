import java.util.*;

class Solution {
    // d, l, r, u
    private static int[] dy = {1,0,0,-1};
    private static int[] dx = {0,-1,1,0};
    private static char[] dir = {'d','l','r','u'};
    private Node start, end;

    public String solution(int n, int m, int x, int y, int r, int c, int k) {
        start = new Node(x, y, "");
        end = new Node(r, c, "");
        return bfs(n, m, k);
    }

    private String bfs(int n, int m, int k) {
        // 경로 사전순으로 최소 힙 생성
        PriorityQueue<Node> pq = new PriorityQueue<>((n1, n2) -> {
            return n1.path.compareTo(n2.path);
        });
        // 시작 위치
        pq.offer(start);
        while (!pq.isEmpty()) {
            Node cur = pq.poll();
            if (cur.y == end.y && cur.x == end.x && cur.path.length() == k)
                return cur.path;
            for (int i=0; i<4; i++) {
                int ny = cur.y + dy[i];
                int nx = cur.x + dx[i];
                if (ny > 0 && ny <= n && nx > 0 && nx <= m) {
                    // 도달 가능할 경우만 추가
                    int dist = Math.abs(ny-end.y) + Math.abs(nx-end.x);
                    String nPath = cur.path + dir[i];
                    if (dist+nPath.length() > k) continue;
                    if ((k-nPath.length()-dist) % 2 == 1) continue;
                    pq.offer(new Node(ny, nx, cur.path + dir[i]));
                }
            }
        }
        return "impossible";
    }

    private static class Node {
        int y, x;
        String path;
        public Node(int y, int x, String path) {
            this.y = y;
            this.x = x;
            this.path = path;
        }
    }
}