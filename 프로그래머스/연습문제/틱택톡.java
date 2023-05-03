class Solution {
    private static char[][] board;
    private static int n;

    public int solution(String[] b) {
        board = new char[3][3];
        char[][] record = new char[3][3];

        for (int i=0; i<b.length; i++) {
            for (int j=0; j<b[i].length(); j++) {
                if (b[i].charAt(j) != '.') n++;
                board[i][j] = b[i].charAt(j);
                record[i][j] = '.';
            }
        }
        return search(record, 'O', 0);
    }

    private int search(char[][] record, char turn, int cnt) {
        if (cnt == n) return 1;
        if (win(record) == true) return 0;
        char nxt = turn == 'O' ? 'X' : 'O';

        for (int i=0; i<3; i++) {
            for (int j=0; j<3; j++) {
                if (board[i][j] == turn && record[i][j] == '.') {
                    record[i][j] = turn;
                    // 생성 가능
                    if (search(record, nxt, cnt+1) == 1) return 1;
                    record[i][j] = '.';
                }
            }
        }
        return 0;
    }

    private boolean win(char[][] board) {
        for (int i=0; i<3; i++) {
            // 가로
            if (board[i][0] == board[i][1] && board[i][1] == board[i][2]) {
                if (board[i][0] != '.') return true;
            }
            // 세로
            if (board[0][i] == board[1][i] && board[1][i] == board[2][i]) {
                if (board[0][i] != '.') return true;
            }
        }
        // 대각선
        if (board[0][0] == board[1][1] && board[1][1] == board[2][2]) {
            if (board[0][0] != '.') return true;
        }
        if (board[2][0] == board[1][1] && board[1][1] == board[0][2]) {
            if (board[2][0] != '.') return true;
        }
        return false;
    }
}