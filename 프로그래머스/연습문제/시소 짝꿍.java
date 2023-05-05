import java.util.*;

class Solution {
    public long solution(int[] weights) {
        // 오름차순 정렬
        Arrays.sort(weights);

        // 무게 측정
        long answer = 0;
        int[] w = new int[1001];
        for (int weight : weights) {
            answer += w[weight];
            if (weight % 3 == 0) answer += w[weight*2/3];
            if (weight % 2 == 0) answer += w[weight/2];
            if (weight % 4 == 0) answer += w[weight*3/4];
            // 무게 추가
            w[weight]++;
        }
        return answer;
    }
}