import java.util.*;

class Solution {

    private static int COST = 25 * 50;
    private static Map<String, Integer[]> cost = new HashMap<>();

    public int solution(int[] picks, String[] minerals) {
        // 광물 캐는 비용
        cost.put("diamond", new Integer[] {1, 5, 25});
        cost.put("iron", new Integer[] {1, 1, 5});
        cost.put("stone", new Integer[] {1, 1, 1});

        dfs(picks, minerals, 0, 0);
        return COST;
    }

    // 현재 채집중인 광물의 인덱스, 누적 피로도
    private void dfs(int[] picks, String[] minerals, int idx, int acc) {
        int sum = picks[0] + picks[1] + picks[2];
        // 모든 광물 캤거나 사용할 곡괭이가 없음
        if (idx >= minerals.length || sum == 0) {
            COST = Math.min(COST, acc);
            return;
        }
        for (int i=0; i<3; i++) {
            // 재고 없음
            if (picks[i] == 0) continue;
            picks[i] -= 1;
            dfs(picks, minerals, idx+5, acc+mine(i, minerals, idx));
            picks[i] += 1;
        }
    }

    private int mine(int pick, String[] minerals, int idx) {
        int acc = 0;
        for (int i=0; i<5; i++) {
            if (idx+i >= minerals.length) break;
            acc += cost.get(minerals[idx+i])[pick];
        }
        return acc;
    }
}