import java.util.*;

class Solution {
    private static final int MAX_TIME = 60 * 24 + 10;
    private static final int CLEAN_TIME = 10;

    public int solution(String[][] book_time) {
        int[] book = new int[MAX_TIME];

        for (String[] time : book_time) {
            int start = parse(time[0]);
            int end = parse(time[1]);

            book[start] += 1;
            book[end + CLEAN_TIME] -= 1;
        }

        // 누적합
        int answer = 0;
        for (int i=1; i<MAX_TIME; i++) {
            book[i] += book[i-1];
            answer = Math.max(answer, book[i]);
        }

        return answer;
    }

    private int parse(String time) {
        String[] hhmm = time.split(":");
        int hh = Integer.valueOf(hhmm[0]);
        int mm = Integer.valueOf(hhmm[1]);
        return hh*60 + mm;
    }
}