class Solution {
    public int[] solution(int[] sequence, int k) {
        int[] answer = search(sequence, k);
        return answer;
    }

    // 합이 k 인 구간 탐색
    private int[] search(int[] sequences, int k) {
        int end = 0, acc = sequences[0];
        int[] answer = {0, sequences.length-1};
        // [start, end] 구간의 합
        for (int start=0; start < sequences.length; start++) {
            while (end < sequences.length-1 && acc < k) {
                acc += sequences[++end];
            }

            if (acc == k) {
                if (answer[1]-answer[0] > end-start) {
                    answer[0] = start;
                    answer[1] = end;
                }
            }
            acc -= sequences[start];
        }
        return answer;
    }
}