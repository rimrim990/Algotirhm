import java.util.*;

class Solution {
    public int[] solution(int[] numbers) {
        int[] answer = new int[numbers.length];
        Deque<Integer> stack = new ArrayDeque<>();
        for (int i=numbers.length-1; i>=0; i--) {
            // 작거나 같은 수 전부 제거
            while (!stack.isEmpty() && stack.peek() <= numbers[i]) {
                stack.pop();
            }
            // 뒷 큰수 존재 여부 검사
            if (!stack.isEmpty()) answer[i] = stack.peek();
            else answer[i] = -1;
            stack.push(numbers[i]);
        }
        return answer;
    }
}