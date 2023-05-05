import java.util.*;

class Solution {
    private int curTime;
    private Deque<String> remains = new ArrayDeque<>();
    private Map<String, Integer> remainTime = new HashMap<>();

    public String[] solution(String[][] plans) {
        // 시작 순서로 정렬
        Arrays.sort(plans, (p1, p2) -> {
            return p1[1].compareTo(p2[1]);
        });
        curTime = getTime(plans[0][1]);
        return doWork(plans);
    }

    private String[] doWork(String[][] plans) {
        List<String> answer = new LinkedList<>();
        for (int i=0; i<plans.length-1; i++) {
            // 현재 과제 처리
            int amount = Integer.valueOf(plans[i][2]);
            int nxtTime = getTime(plans[i+1][1]);
            // 처리 완료
            if (amount <= nxtTime-curTime) {
                curTime += amount;
                answer.add(plans[i][0]);
            } else { // 후순위로 밀림
                amount -= (nxtTime-curTime);
                curTime = nxtTime;
                remains.push(plans[i][0]);
                remainTime.put(plans[i][0], amount);
            }
            // 밀린 과제 처리
            while (curTime < nxtTime && !remains.isEmpty()) {
                String id = remains.peekFirst();
                int ra = remainTime.get(id);
                if (ra <= nxtTime-curTime) {
                    curTime += ra;
                    answer.add(remains.pop());
                } else {
                    ra -= (nxtTime-curTime);
                    curTime = nxtTime;
                    remainTime.put(id, ra);
                }
            }
            // 더이상 처리할 과제 없을 경우 다음 시간으로 넘어감 !
            if (remains.isEmpty()) curTime = nxtTime;
        }
        // 마지막 과제 처리
        answer.add(plans[plans.length-1][0]);
        // 남은 과제 처리
        while(!remains.isEmpty()) {
            answer.add(remains.pop());
        }
        return answer.toArray(new String[answer.size()]);
    }

    private int getTime(String time) {
        String[] hhmm = time.split(":");
        int hh = Integer.valueOf(hhmm[0]);
        int mm = Integer.valueOf(hhmm[1]);
        return hh * 60 + mm;
    }
}