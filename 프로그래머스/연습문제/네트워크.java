import java.util.*;

class Solution {

    public int solution(int n, int[][] computers) {
        int[] parent = new int[n];

        // 배열 초기화
        for (int i=0; i<n; i++) {
            parent[i] = i;
        }

        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                if (computers[i][j] == 1 && find(parent,i) != find(parent,j)) {
                    union(parent, i, j);
                }
            }
        }

        Set<Integer> answer = new HashSet<>();
        for (int i=0; i<n; i++) {
            answer.add(find(parent, i));
        }

        return answer.size();
    }

    private int find(int[] parent, int a) {
        if (parent[a] != a) {
            parent[a] = find(parent, parent[a]);
        }

        return parent[a];
    }

    private void union(int[] parent, int a, int b) {
        int pa = find(parent, a), pb = find(parent, b);

        if (pa < pb) {
            parent[pb] = pa;
            return;
        }

        parent[pa] = pb;
    }
}