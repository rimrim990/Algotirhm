import java.util.*;

class Solution {

    private List<Integer> answer = new LinkedList<>();

    public int[] solution(int n, int m, int[][] queries) {
        // 배열 초기화하기
        int[][] mat = new int[n][m];
        for (int i=0; i<n; i++) {
            for (int j=0; j<m; j++) {
                mat[i][j] = (i*m) + (j+1);
            }
        }

        // 회전하기
        for (int[] query : queries) {
            int res = rotate(mat, query);
            answer.add(res);
        }

        return answer.stream()
            .mapToInt(Integer::intValue)
            .toArray();
    }

    private int rotate(int[][] mat, int[] query) {
        int y1 = query[0]-1, x1 = query[1]-1;
        int y2 = query[2]-1, x2 = query[3]-1;

        int prev = mat[y1][x1];
        int minVal = prev;

        // 회전하기
        for (int x=x1+1; x<=x2; x++) {
            int tmp = prev;
            prev = mat[y1][x];
            mat[y1][x] = tmp;
            minVal = Math.min(minVal, prev);
        }

        for (int y=y1+1; y<=y2; y++) {
            int tmp = prev;
            prev = mat[y][x2];
            mat[y][x2] = tmp;
            minVal = Math.min(minVal, prev);
        }

        for (int x=x2-1; x>=x1; x--) {
            int tmp = prev;
            prev = mat[y2][x];
            mat[y2][x] = tmp;
            minVal = Math.min(minVal, prev);
        }

        for (int y=y2-1; y>=y1; y--) {
            int tmp = prev;
            prev = mat[y][x1];
            mat[y][x1] = tmp;
            minVal = Math.min(minVal, prev);
        }

        return minVal;
    }
}